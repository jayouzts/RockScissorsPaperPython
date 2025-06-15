from rules.RSPRulesBase import RSPRule

class RulesEnforcer:
    def __init__(self, rules: list[RSPRule]):
        self._rules = list(rules)  # Convert to list in case rules is a generator
        
    def evaluate(self, player1_choice: str, player2_choice: str) -> str:
        """
        Evaluates the outcome of a match between two player choices using the rule set.
        If multiple rules match, an exception is raised due to ambiguity.

        Scaling Note:
        This implementation uses a linear scan over the rules for each check.
        With a small rule set (10–50), this is acceptable.
        However, if you had 1,000+ rules or needed high-throughput evaluations,
        consider indexing rules by (winner, loser) or (choice1, choice2) tuples
        to reduce lookup time using a dictionary.
        """
        
        if len(self._rules) == 0:
            return "No rules found"
        
    
        # Check if player 1 wins
        p1_matches = [r for r in self._rules if r.applies(player1_choice, player2_choice)]

        if len(p1_matches) > 1:
            raise ValueError(f"Ambiguous rule match: multiple rules found for {player1_choice} vs {player2_choice}")
        elif len(p1_matches) == 1:
            rule = p1_matches[0]
            return f"Player 1 wins! {rule.winner} {rule.action} {rule.loser}."

        # Check if player 2 wins
        p2_matches = [r for r in self._rules if r.applies(player2_choice, player1_choice)]

        if len(p2_matches) > 1:
            raise ValueError(f"Ambiguous rule match: multiple rules found for {player2_choice} vs {player1_choice}")
        elif len(p2_matches) == 1:
            rule = p2_matches[0]
            return f"Player 2 wins! {rule.winner} {rule.action} {rule.loser}."

        # Neither rule matched
        return "It's a tie!"
