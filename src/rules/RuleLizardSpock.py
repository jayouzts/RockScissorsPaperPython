from abc import ABC, abstractmethod
from enum import IntFlag
from .RSPRulesBase import RSPRule
from utils.RulesEnums import GameMode

# --- Lizard-Spock Rules ---
class RockCrushesLizard(RSPRule):
    @property
    def winner(self): return "Rock"

    @property
    def loser(self): return "Lizard"

    @property
    def action(self): return "crushes"

    @property
    def applicable_modes(self): return GameMode.LizardSpockVariant

class LizardPoisonsSpock(RSPRule):
    @property
    def winner(self): return "Lizard"

    @property
    def loser(self): return "Spock"

    @property
    def action(self): return "poisons"

    @property
    def applicable_modes(self): return GameMode.LizardSpockVariant

class SpockSmashesScissors(RSPRule):
    @property
    def winner(self): return "Spock"

    @property
    def loser(self): return "Scissors"

    @property
    def action(self): return "smashes"

    @property
    def applicable_modes(self): return GameMode.LizardSpockVariant

class ScissorsDecapitateLizard(RSPRule):
    @property
    def winner(self): return "Scissors"

    @property
    def loser(self): return "Lizard"

    @property
    def action(self): return "decapitate"

    @property
    def applicable_modes(self): return GameMode.LizardSpockVariant

class LizardEatsPaper(RSPRule):
    @property
    def winner(self): return "Lizard"

    @property
    def loser(self): return "Paper"

    @property
    def action(self): return "eats"

    @property
    def applicable_modes(self): return GameMode.LizardSpockVariant

class PaperDisprovesSpock(RSPRule):
    @property
    def winner(self): return "Paper"

    @property
    def loser(self): return "Spock"

    @property
    def action(self): return "disproves"

    @property
    def applicable_modes(self): return GameMode.LizardSpockVariant

class SpockVaporizesRock(RSPRule):
    @property
    def winner(self): return "Spock"

    @property
    def loser(self): return "Rock"

    @property
    def action(self): return "vaporizes"

    @property
    def applicable_modes(self): return GameMode.LizardSpockVariant