from abc import ABC, abstractmethod
from enum import IntFlag
from .RSPRulesBase import RSPRule
from utils.RulesEnums import GameMode

# --- Classic Rules ----
class RockCrushesScissors(RSPRule):
    @property
    def winner(self): return "Rock"

    @property
    def loser(self): return "Scissors"

    @property
    def action(self): return "crushes"

    @property
    def applicable_modes(self): return GameMode.Classic | GameMode.LizardSpockVariant

class ScissorsCutPaper(RSPRule):
    @property
    def winner(self): return "Scissors"

    @property
    def loser(self): return "Paper"

    @property
    def action(self): return "cut"

    @property
    def applicable_modes(self): return GameMode.Classic | GameMode.LizardSpockVariant

class PaperCoversRock(RSPRule):
    @property
    def winner(self): return "Paper"

    @property
    def loser(self): return "Rock"

    @property
    def action(self): return "covers"

    @property
    def applicable_modes(self): return GameMode.Classic | GameMode.LizardSpockVariant
