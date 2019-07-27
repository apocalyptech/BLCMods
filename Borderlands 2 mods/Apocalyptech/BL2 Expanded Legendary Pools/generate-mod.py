#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2018, CJ Kucera
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

try:
    from modprocessor import ModProcessor
    mp = ModProcessor()
except ModuleNotFoundError:
    print('')
    print('********************************************************************')
    print('To run this script, you will need to copy or symlink modprocessor.py')
    print('from the parent directory, so it exists here as well.  Sorry for')
    print('the bother!')
    print('********************************************************************')
    print('')
    sys.exit(1)

###
### Output variables
###

mod_name = 'BL2 Expanded Legendary Pools'
mod_version = '1.1.1'
output_filename = '{}.blcm'.format(mod_name)
input_filename = 'input-file-mod.txt'

###
### Construct the mod!
###

# What percentage of Purple drops should be gemstones?
pct_gemstones = 0.25

# Legendary Pool management
unique_hotfixes = []
pearl_hotfixes = []
seraph_hotfixes = []
eff_hotfixes = []
for (guntype, legendaries, uniques, pearls, seraphs, effs, num_undesirables) in [
        (
            'AssaultRifles',
            [
                # Regular Legendaries
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Bandit_5_Madhouse',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Dahl_5_Veruc',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBuster',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Torgue_5_KerBlaster',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Vladof_5_Sherdifier',
                'GD_Aster_Weapons.AssaultRifles.AR_Bandit_3_Ogre',
                'GD_Anemone_Weapons.AssaultRifle.Brothers.AR_Jakobs_5_Brothers',
            ],
            [
                # Uniques
                'GD_Iris_Weapons.AssaultRifles.AR_Torgue_3_BoomPuppy',
                'GD_Iris_Weapons.AssaultRifles.AR_Vladof_3_Kitten',
                'GD_Orchid_BossWeapons.AssaultRifle.AR_Jakobs_3_Stinkpot',
                'GD_Orchid_BossWeapons.AssaultRifle.AR_Vladof_3_Rapier',
                'GD_Sage_Weapons.AssaultRifle.AR_Bandit_3_Chopper',
                'GD_Sage_Weapons.AssaultRifle.AR_Jakobs_3_DamnedCowboy',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Dahl_3_Scorpio',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Jakobs_3_Stomper',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Torgue_3_EvilSmasher',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Vladof_3_Hail',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.AssaultRifle.AR_Bandit_6_Sawbar',
                'GD_Gladiolus_Weapons.AssaultRifle.AR_Dahl_6_Bearcat',
                'GD_Lobelia_Weapons.AssaultRifles.AR_Jakobs_6_Bekah',
            ],
            [
                # Seraphs
                'GD_Aster_RaidWeapons.AssaultRifles.Aster_Seraph_Seeker_Balance',
                'GD_Orchid_RaidWeapons.AssaultRifle.Seraphim.Orchid_Seraph_Seraphim_Balance',
                'GD_Sage_RaidWeapons.AssaultRifle.Sage_Seraph_LeadStorm_Balance',
            ],
            [
                # Effervescents
                'GD_Anemone_Weapons.AssaultRifle.AR_Dahl_6_Toothpick',
                'GD_Anemone_Weapons.AssaultRifle.PeakOpener.AR_Torgue_5_PeakOpener',
            ],
            0,
        ),
        (
            'Launchers',
            [
                # Regular Legendaries
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Pyrophobia',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Tediore_5_Bunny',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol',
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet',
            ],
            [
                # Uniques
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_3_TheHive',
                'GD_Orchid_BossWeapons.Launcher.RL_Torgue_3_12Pounder',
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer',
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Bandit_3_Roaster',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.Launchers.RL_Torgue_6_Tunguska',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.RPG.Ahab.Orchid_Seraph_Ahab_Balance',
            ],
            [
                # Effervescents
                'GD_Anemone_Weapons.Rocket_Launcher.WorldBurn.RL_Torgue_5_WorldBurn',
            ],
            1,
        ),
        (
            'Pistols',
            [
                # Regular Legendaries
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Gub',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Gunerang',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Hornet',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Vladof_5_Infinity',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Maliwan_5_ThunderballFists',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun',
                'GD_Anemone_Weapons.A_Weapons_Legendary.Pistol_Dahl_5_Hector_Hornet',
            ],
            [
                # Uniques
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Judge',
                'GD_Aster_Weapons.Pistols.Pistol_Maliwan_3_GrogNozzle',
                'GD_Orchid_BossWeapons.Pistol.Pistol_Jakobs_ScarletsGreed',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensHead',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Dahlminator',
                'GD_Iris_Weapons.Pistols.Pistol_Torgue_3_PocketRocket',
                'GD_Sage_Weapons.Pistols.Pistol_Jakobs_3_Rex',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Law',
                'GD_Orchid_BossWeapons.Pistol.Pistol_Maliwan_3_LittleEvie',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Teapot',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Vladof_3_Veritas',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Bandit_3_Tenderbox',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.Pistol.Pistol_Jakobs_6_Unforgiven',
                'GD_Gladiolus_Weapons.Pistol.Pistol_Vladof_6_Stalker',
                'GD_Lobelia_Weapons.Pistol.Pistol_Maliwan_6_Wanderlust',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.Pistol.Devastator.Orchid_Seraph_Devastator_Balance',
                'GD_Sage_RaidWeapons.Pistol.Sage_Seraph_Infection_Balance',
                'GD_Aster_RaidWeapons.Pistols.Aster_Seraph_Stinger_Balance',
            ],
            [
                # Effervescents
            ],
            1,
        ),
        (
            'Shotguns',
            [
                # Regular Legendaries
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Tediore_5_Deliverance',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall',
                'GD_Anemone_Weapons.Shotgun.Overcompensator.SG_Hyperion_6_Overcompensator',
            ],
            [
                # Uniques
                'GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Hydra',
                'GD_Orchid_BossWeapons.Shotgun.SG_Bandit_3_JollyRoger',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_HeartBreaker',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Dog',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Blockhead',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo',
                'GD_Orchid_BossWeapons.Shotgun.SG_Jakobs_3_OrphanMaker',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Landscaper',
                'GD_Iris_Weapons.Shotguns.SG_Hyperion_3_SlowHand',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_Shotgun1340',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_RokSalt',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_TidalWave',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Teeth',
                'GD_Aster_Weapons.Shotguns.SG_Torgue_3_SwordSplosion',
                'GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Twister',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Triquetra',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.Shotgun.SG_Hyperion_6_Butcher',
                'GD_Lobelia_Weapons.Shotguns.SG_Torgue_6_Carnage',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance',
                'GD_Sage_RaidWeapons.Shotgun.Sage_Seraph_Interfacer_Balance',
                'GD_Aster_RaidWeapons.Shotguns.Aster_Seraph_Omen_Balance',
            ],
            [
                # Effervescents
                'GD_Anemone_Weapons.Shotguns.SG_Torgue_3_SwordSplosion_Unico',
            ],
            0,
        ),
        (
            'SMG',
            [
                # Regular Legendaries
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Bandit_5_Slagga',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_BabyMaker',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Emperor',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch',
            ],
            [
                # Uniques
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_BoneShredder',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Bane',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Commerce',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Chulainn',
                'GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Lascaux',
                'GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk',
                'GD_Sage_Weapons.SMG.SMG_Hyperion_3_YellowJacket',
                'GD_Aster_Weapons.SMGs.SMG_Bandit_3_Orc',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.SMG.SMG_Tediore_6_Avenger',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance',
                'GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance',
                'GD_Aster_RaidWeapons.SMGs.Aster_Seraph_Florentine_Balance',
            ],
            [
                # Effervescents
                'GD_Anemone_Weapons.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
                'GD_Anemone_Weapons.SMG.SMG_Tediore_6_Infection_Cleaner',
            ],
            0,
        ),
        (
            'SniperRifles',
            [
                # Regular Legendaries
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Lyudmila',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Volcano',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader',
                'GD_Anemone_Weapons.A_Weapons_Unique.Sniper_Jakobs_3_Morde_Lt',
            ],
            [
                # Uniques
                'GD_Sage_Weapons.SniperRifles.Sniper_Jakobs_3_ElephantGun',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Buffalo',
                'GD_Iris_Weapons.SniperRifles.Sniper_Jakobs_3_Cobra',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie',
                'GD_Orchid_BossWeapons.SniperRifles.Sniper_Maliwan_3_Pimpernel',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Morningstar',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_Sloth',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Tresspasser',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Longbow',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.sniper.Sniper_Maliwan_6_Storm',
                'GD_Lobelia_Weapons.sniper.Sniper_Jakobs_6_Godfinger',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.sniper.Patriot.Orchid_Seraph_Patriot_Balance',
                'GD_Sage_RaidWeapons.sniper.Sage_Seraph_HawkEye_Balance',
            ],
            [
                # Effervescents
                'GD_Anemone_Weapons.sniper.Sniper_Jakobs_6_Chaude_Mama',
            ],
            0,
        ),
        ]:

    # First set up a hotfix for the base pool initialization
    initial_pool = []
    for legendary in legendaries:
        initial_pool.append((legendary, 1, 'WeaponBalanceDefinition'))
    for i in range(len(uniques) + len(pearls) + len(seraphs) + len(effs) + num_undesirables):
        initial_pool.append((None, 0))
    mp.register_str('weapon_pool_clear_{}'.format(guntype.lower()),
        'level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems {}'.format(
            guntype,
            mp.get_balanced_items(initial_pool),
            ))

    # Hotfixes to add uniques
    for (idx, unique) in enumerate(uniques):
        unique_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + idx,
                unique
                ))

    # Hotfixes to add pearls
    for (idx, pearl) in enumerate(pearls):
        pearl_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + len(uniques) + idx,
                pearl
                ))

    # Hotfixes to add seraphs
    for (idx, seraph) in enumerate(seraphs):
        seraph_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + len(uniques) + len(pearls) + idx,
                seraph
                ))

    # Hotfixes to add effervescents
    for (idx, eff) in enumerate(effs):
        eff_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + len(uniques) + len(pearls) + len(seraphs) + idx,
                eff
                ))

mp.register_str('legendary_unique_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in unique_hotfixes]
    ))

mp.register_str('legendary_pearl_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in pearl_hotfixes]
    ))

mp.register_str('legendary_seraph_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in seraph_hotfixes]
    ))

mp.register_str('legendary_eff_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in eff_hotfixes]
    ))

# Legendary shield/grenade pool configuration.  Doing this a bit differently since there's
# not nearly as many shields/grenades to handle as weapons.

items = {
    'shield': {
        'GD_Itempools.ShieldPools.Pool_Shields_Absorption_06_Legendary': [
            ('1340', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_1340', 1),
            ('equitas', 3, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_Equitas', 1),
            ('sponge', 4, 'GD_Iris_SeraphItems.Sponge.Iris_Seraph_Shield_Sponge_Balance', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Booster_06_Legendary': [
            ('potogold', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_PotOGold', 1),
            ('bigboomblaster', 2, 'GD_Iris_SeraphItems.BigBoomBlaster.Iris_Seraph_Shield_Booster_Balance', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Chimera_06_Legendary': [
            ('evolution', 1, 'GD_Orchid_RaidWeapons.Shield.Anshin.Orchid_Seraph_Anshin_Shield_Balance', 1)
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Juggernaut_06_Legendary': [
            ('hoplite', 1, 'GD_Iris_SeraphItems.Hoplite.Iris_Seraph_Shield_Juggernaut_Balance', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_NovaShields_Explosive_06_Legendary': [
            ('deadlybloom', 0, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_DeadlyBloom', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Roid_06_Legendary': [
            ('order', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_Order', 1),
            ('lovethumper', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_04_LoveThumper', 1),
            ('punchee', 3, 'GD_Iris_SeraphItems.Pun-chee.Iris_Seraph_Shield_Pun-chee_Balance', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Standard_06_Legendary': [
            ('manlyman', 1, 'GD_Orchid_Shields.A_Item_Custom.S_BladeShield', 1),
            ('roughrider', 2, 'GD_Sage_Shields.A_Item_Custom.S_BucklerShield', 1),
            ('antagonist', 3, 'GD_Aster_ItemGrades.Shields.Aster_Seraph_Antagonist_Shield_Balance', 1),
            ('blockade', 4, 'GD_Aster_ItemGrades.Shields.Aster_Seraph_Blockade_Shield_Balance', 1),
            ('retainer', 5, 'GD_Anemone_Balance_Treasure.Shields.ItemGrade_Gear_Shield_Worming', 0.33),
            ('easy_mode', 6, 'GD_Anemone_ItemPools.Shields.ItemGrade_Gear_Shield_Nova_Singularity_Peak', 0.33),
            ('cracked_sash', 7, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_CrackedSash', 1),
            ],
        },
    'grenade': {
        'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary': [
            ('breath_of_terra', 12, 'GD_GrenadeMods.A_Item_Legendary.GM_FlameSpurt', 1),
            ('fireball', 13, 'GD_Aster_GrenadeMods.A_Item.GM_Fireball', 1),
            ('fuster_cluck', 14, 'GD_GrenadeMods.A_Item_Custom.GM_FusterCluck', 1),
            ('kiss_of_death', 15, 'GD_GrenadeMods.A_Item_Custom.GM_KissOfDeath', 1),
            ('lightning_bolt', 16, 'GD_Aster_GrenadeMods.A_Item.GM_LightningBolt', 1),
            ('magic_missile', 17, 'GD_Aster_GrenadeMods.A_Item.GM_MagicMissileRare', 1),
            ('crossfire', 18, 'GD_Iris_SeraphItems.Crossfire.Iris_Seraph_GrenadeMod_Crossfire_Balance', 1),
            ('meteor_shower', 19, 'GD_Iris_SeraphItems.MeteorShower.Iris_Seraph_GrenadeMod_MeteorShower_Balance', 1),
            ('o_negative', 20, 'GD_Iris_SeraphItems.ONegative.Iris_Seraph_GrenadeMod_ONegative_Balance', 1),
            ('antifection', 21, 'GD_Anemone_GrenadeMods.A_Item_Legendary.GM_Antifection', 1),
            ('electric_chair', 22, 'GD_Anemone_GrenadeMods.A_Item_Legendary.GM_StormFront', 1),
            ('midnight_star', 23, 'GD_Orchid_GrenadeMods.A_Item_Custom.GM_Blade', 1),
            ('sky_rocket', 24, 'GD_GrenadeMods.A_Item_Custom.GM_SkyRocket', 1),
            ],
        },
    'relic': {
        'GD_Itempools.ArtifactPools.Pool_ArtifactsReward': [
            # Uniques:
            ('midnight_star', 11, 'GD_Orchid_Artifacts.A_Item_Unique.A_Blade', 0.3),
            ('deputys_badge', 12, 'GD_Artifacts.A_Item_Unique.A_Deputy', 0.3),
            ('opportunity', 13, 'GD_Artifacts.A_Item_Unique.A_Opportunity', 0.3),
            ('endowment', 14, 'GD_Artifacts.A_Item_Unique.A_Endowment', 0.3),
            ('amulet', 15, 'GD_Aster_Artifacts.A_Item_Unique.A_MysteryAmulet', 0.1),
            ('sheriffs_badge', 16, 'GD_Artifacts.A_Item_Unique.A_Sheriff', 0.3),
            ('afterburner', 17, 'GD_Artifacts.A_Item_Unique.A_Afterburner', 0.3),
            # E-Tech:
            ('ancients_blood', 18, 'GD_Gladiolus_Artifacts.A_Item.A_VitalityStockpile_VeryRare', 0.3),
            ('ancients_bone', 19, 'GD_Gladiolus_Artifacts.A_Item.A_ElementalProficiency_VeryRare', 0.3),
            ('ancients_heart_1', 20, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityAssault_VeryRare', 0.15),
            ('ancients_heart_2', 21, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityLauncher_VeryRare', 0.15),
            ('ancients_heart_3', 22, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityPistol_VeryRare', 0.15),
            ('ancients_heart_4', 23, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityShotgun_VeryRare', 0.15),
            ('ancients_heart_5', 24, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacitySMG_VeryRare', 0.15),
            ('ancients_heart_6', 25, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacitySniper_VeryRare', 0.15),
            ('ancients_skin', 26, 'GD_Gladiolus_Artifacts.A_Item.A_ResistanceProtection_VeryRare', 0.3),
            # Seraph:
            ('seraphs_blood', 27, 'GD_Orchid_Artifacts.A_Item_Unique.A_SeraphBloodRelic', 0.3),
            ('seraphs_breath', 28, 'GD_Sage_Artifacts.A_Item.A_SeraphBreath', 0.3),
            ('seraphs_might', 29, 'GD_Iris_SeraphItems.Might.Iris_Seraph_Artifact_Might_Balance', 0.3),
            ('seraphs_shadow', 30, 'GD_Aster_Artifacts.A_Item_Unique.A_SeraphShadow', 0.3),
            # Effervescent:
            ('mouthwash', 31, 'GD_Anemone_Relics.A_Item_Unique.A_Sheriff', 0.25),
            ('hard_carry', 32, 'GD_Anemone_Relics.A_Item_Unique.A_Deputy', 0.25),
            # Junk:
            ('vault_hunter', 33, 'GD_Artifacts.A_Item_Unique.A_VaultHunter', 0.3),
            ('winter_is_over', 34, 'GD_Anemone_Relics.A_Item.A_Elemental_Status_Rare', 0.3),
            ],
        },
    'gemstone': {
        'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare': [
            ('ar', 5, 'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_ARs_04_Gemstone', 5),
            ],
        'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare': [
            ('pistol', 8, 'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Pistols_04_Gemstone', 8),
            ],
        'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare': [
            ('shotgun', 5, 'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Shotguns_04_Gemstone', 5),
            ],
        'GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare': [
            ('smg', 5, 'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_SMGs_04_Gemstone', 5),
            ],
        'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare': [
            ('sniper', 5, 'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Snipers_04_Gemstone', 5),
            ],
        },
    'pistol': {
        'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary': [
            ('fire_drill', 30, 'GD_Anemone_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Infinity_DD', 1),
            ],
        },
    'launcher': {
        'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary': [
            ('error_message', 13, 'GD_Orchid_BossWeapons.RPG.Ahab.Orchid_Boss_Ahab_Balance_NODROP', 1),
            ],
        },
    }
for (itemtype, itemdict) in items.items():
    for (pool, itemlist) in itemdict.items():
        for (label, index, itemname, scale) in itemlist:
            if itemtype == 'gemstone':
                # Math derived from:  x/(x+n) = r
                # Where `r` is the desired ratio of gemstones, `x` is the weight
                # we want to assign to the gemstone pool (ie: the value we're solving
                # for), and `n` being the current weight of the pool without gems.
                weight = round((pct_gemstones*scale)/(1-pct_gemstones), 6)
                mp.set_bi_item_pool('{}_{}'.format(itemtype, label),
                    pool,
                    index,
                    itemname,
                    weight=weight,
                    )
            else:
                if itemtype == 'launcher' or itemtype == 'pistol':
                    invbalance = 'WeaponBalanceDefinition'
                else:
                    invbalance = 'InventoryBalanceDefinition'
                mp.set_bi_item_pool('{}_{}'.format(itemtype, label),
                    pool,
                    index,
                    itemname,
                    invbalance=invbalance,
                    scale=scale,
                    )

# Load in our purple scales
purple_scales = {}
for (key, label, scale_world, scale_individual, scale_epic, scale_treasure) in [
        ('base', 'Stock Purple Drop Rate', 1, 1, 2.5, 5),
        ('1.3x', '1.3x Purple Drop Rate', 1.333333, 1.333333, 3.333333, 6.666666),
        ('1.6x', '1.6x Purple Drop Rate', 1.666666, 1.666666, 4.166666, 8.333333),
        ]:
    with open('input-file-purples.txt') as df:
        purple_scales[key] = df.read().format(
                section_label=label,
                scale_world=scale_world,
                scale_individual=scale_individual,
                scale_epic=scale_epic,
                scale_treasure=scale_treasure,
                )

# Load in our legendary scales.
leg_scales = {}
for (key, label, scale_most, scale_com, scale_relic_full, scale_relic_half, scale_relic_amulet) in [
        ('base', 'Stock Legendary Drop Rate', 3, 1, .3, .15, .1),
        ('2x', 'Doubled Legendary Drop Rate', 6, 2, .6, .3, .2),
        ('3x', 'Tripled Legendary Drop Rate', 9, 3, .9, .45, .3),
        ]:
    with open('input-file-legendary.txt') as df:
        leg_scales[key] = df.read().format(
                section_label=label,
                # World drops:
                weapon_scale=scale_most,
                shield_scale=scale_most,
                grenade_scale=scale_most,
                com_scale=scale_com,
                # Special-case relic stuff:
                relic_scale_full=scale_relic_full,
                relic_scale_half=scale_relic_half,
                relic_scale_amulet=scale_relic_amulet,
                # Epic Chests:
                relic_scale_chest=scale_most,
                com_scale_chest=scale_most,
                grenade_scale_chest=scale_most,
                item_scale_chest=scale_com,
                shield_scale_chest=scale_most,
                weapon_scale_chest_most=scale_com,
                weapon_scale_chest_sniper=scale_most,
                # Individual weapon pools:
                ind_weapon_scale=scale_com,
                )

###
### Everything below this point is constructing the actual patch file
###

# Now read in our main input file
with open(input_filename, 'r') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        mp=mp,
        purple_scale_base=purple_scales['base'],
        purple_scale_13x=purple_scales['1.3x'],
        purple_scale_16x=purple_scales['1.6x'],
        leg_scale_base=leg_scales['base'],
        leg_scale_2x=leg_scales['2x'],
        leg_scale_3x=leg_scales['3x'],
        )
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod to: {}'.format(output_filename))
