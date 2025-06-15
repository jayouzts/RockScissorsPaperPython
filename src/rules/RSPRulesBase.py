from abc import ABC, abstractmethod
from enum import IntFlag
from typing import Final
from utils.RulesEnums import GameMode

class RSPRule(ABC):
    @property
    @abstractmethod
    def winner(self) -> str:
        pass

    @property
    @abstractmethod
    def loser(self) -> str:
        pass

    @property
    @abstractmethod
    def action(self) -> str:
        pass

    @property
    @abstractmethod
    def applicable_modes(self) -> GameMode:
        pass

    def applicable(self, current_game_mode: GameMode) -> bool:
        return bool(self.applicable_modes & current_game_mode)

    def applies(self, player1_choice: str, player2_choice: str) -> bool:
        return (
            self.winner.strip().lower() == player1_choice.strip().lower() and
            self.loser.strip().lower() == player2_choice.strip().lower()
        )
