import unittest
from os import path
import sys
sys.path.append(path.abspath(path.dirname(__file__)))
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from calcs_tests import TestDamageCalculator
from calcs_tests.armor_mitigation_tests import TestArmorMitigation
from calcs_tests.rogue_tests import TestRogueDamageCalculator
from calcs_tests.rogue_tests import TestRogueDamageCalculatorLevels
from calcs_tests.rogue_tests.Aldriana_tests import TestAldrianasRogueDamageCalculator
from core_tests.exceptions_tests import TestInvalidInputException
from objects_tests.buffs_tests import TestBuffsTrue, TestBuffsFalse, TestBuffsLevel
from objects_tests.stats_tests import TestStats, TestWeapon, TestGearBuffs
from objects_tests.procs_tests import TestProcsList, TestProc
from objects_tests.race_tests import TestRace
from objects_tests.rogue_tests.rogue_glyphs_tests import TestRogueGlyphs
from objects_tests.rogue_tests.rogue_talents_tests import TestAssassinationTalents
from objects_tests.rogue_tests.rogue_talents_tests import TestCombatTalents
from objects_tests.rogue_tests.rogue_talents_tests import TestSubtletyTalents
from objects_tests.rogue_tests.rogue_talents_tests import TestRogueTalents

if __name__ == "__main__":
    unittest.main()
