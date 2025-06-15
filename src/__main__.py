from rules.RSPRulesBase import RSPRule
from utils.RulesCollector import get_rules
from utils.RulesEnforcer import RulesEnforcer
from utils.RulesEnums import GameMode


# Inspired by The Big Bang Theory:
# https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock
#
# This implementation uses the "Rules" design pattern to avoid a large
# set of nested if/elif/else or switch-case statements.
# Each rule is encapsulated in a class that knows when it applies.
# This makes the code easy to extend (e.g., adding new game modes or gestures)
# without modifying the core logic (open/closed principle).

def get_player_choice(player_name: str, valid_gestures: set[str]) -> str:
    while True:
        choice = input(f"Enter {player_name} choice: ").strip().lower()
        if choice in valid_gestures:
            return choice
        print(f"Invalid choice. Valid options are: {', '.join(sorted(valid_gestures))}")

def main():
    print("Welcome to Rock, Scissors, Paper, Lizard, Spock!")

    while True:
        print("Do you want to play classic Rock, Scissors, Paper (type '1') or the Lizard-Spock variant (type '2')?")
        choice = input(">> ").strip()

        if choice == "2":
            game_mode = GameMode.LizardSpockVariant
        else:
            if choice != "1":
                print("Invalid input. Defaulting to classic mode.")
            game_mode = GameMode.Classic

        # Discover applicable rules using dynamic introspection
        rules = list(get_rules(game_mode))
        
        # Build valid gestures dynamically from rules
        valid_gestures = set()
        # Id like to find a linq equivalent to avoid looping
        for rule in rules:
            valid_gestures.add(rule.winner.lower())
            
        enforcer = RulesEnforcer(rules)

        player1_choice = get_player_choice("Player 1", valid_gestures)
        player2_choice = get_player_choice("Player 2", valid_gestures)

        try:
            result = enforcer.evaluate(player1_choice, player2_choice)
        except ValueError as e:
            result = f"Error: {e}"

        print(result)

        print("Do you want to play again? (y/n)")
        again = input(">> ").strip().lower()
        if again != "y":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
