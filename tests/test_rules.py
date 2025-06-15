import unittest
from rules.RSPRulesBase import RSPRule
from utils.RulesEnforcer import RulesEnforcer
from utils.RulesEnums import GameMode
from utils.RulesCollector import get_rules

# Sample rule class for testing
class TestRule(RSPRule):
    @property
    def winner(self): return "rock"

    @property
    def loser(self): return "scissors"

    @property
    def action(self): return "crushes"

    @property
    def applicable_modes(self): return GameMode.Classic

class RulesEngineTests(unittest.TestCase):

    def test_rule_applies_true(self):
        rule = TestRule()
        self.assertTrue(rule.applies("rock", "scissors"))

    def test_rule_applies_false(self):
        rule = TestRule()
        self.assertFalse(rule.applies("scissors", "rock"))

    def test_rule_applicable_mode_true(self):
        rule = TestRule()
        self.assertTrue(rule.applicable(GameMode.Classic))

    def test_rule_applicable_mode_false(self):
        rule = TestRule()
        self.assertFalse(rule.applicable(GameMode.LizardSpockVariant))

    def test_rules_engine_player1_wins(self):
        engine = RulesEnforcer([TestRule()])
        result = engine.evaluate("rock", "scissors")
        self.assertIn("Player 1 wins!", result)

    def test_rules_engine_player2_wins(self):
        engine = RulesEnforcer([TestRule()])
        result = engine.evaluate("scissors", "rock")
        self.assertIn("Player 2 wins!", result)

    def test_rules_engine_tie(self):
        engine = RulesEnforcer([TestRule()])
        result = engine.evaluate("rock", "rock")
        self.assertEqual(result, "It's a tie!")

    def test_get_rules_returns_applicable_rules(self):
        rules = list(get_rules(GameMode.Classic | GameMode.LizardSpockVariant))
        self.assertTrue(any(isinstance(r, RSPRule) for r in rules))
        self.assertTrue(all(r.applicable(GameMode.Classic) or r.applicable(GameMode.LizardSpockVariant) for r in rules))

if __name__ == "__main__":
    unittest.main()
