from typing import Iterator
import inspect
from rules.RSPRulesBase import RSPRule
from utils.RulesEnums import GameMode
import rules.RulesClassic
import rules.RuleLizardSpock

# This looks for all of the rules that are applicable to the game mode
def get_rules(game_mode: GameMode) -> Iterator[RSPRule]:
    for cls in RSPRule.__subclasses__():
        if not inspect.isabstract(cls):
            try:
                rule = cls()
                if rule.applicable(game_mode):
                    yield rule
            except TypeError:
                continue


