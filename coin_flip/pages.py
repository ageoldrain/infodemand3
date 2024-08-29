from otree.api import Page, WaitPage
from .models import C


P_FAIR = 0.5
P_BIASED = 0.75 # The probability of heads of the biased coin

class Introduction(Page):
    """
    Introduction page providing some information about the game.
    """
    def is_displayed(self):
        return self.round_number == 1

class Introduction1point5(Page):
    """
    Second introduction page providing some information about the game.
    """
    def is_displayed(self):
        return self.round_number == 1

class Introduction2(Page):
    """
    Third introduction page with instructions about the experiment. 
    """
    def is_displayed(self):
        return self.round_number == 1


class RoundInfo(Page):
    """
    Page displaying round information
    """
    
    def vars_for_template(self):
        return {
            'round_number': self.round_number
        }
    def is_displayed(self):
        return self.round_number <= C.NUM_ROUNDS


class ChooseCoin(Page):
    """
    Page where participant chooses between 'fair' and 'biased' coin.
    """
    form_model = 'player'
    form_fields = ['coin_choice']

  #  return {
  #          'round_number': self.round_number
  #      }

    def vars_for_template(self):
        return {
            'round_number': self.round_number
        }

    def is_displayed(self):
        return self.round_number <= C.NUM_ROUNDS

    def before_next_page(self):
        # Flip the chosen coin after the player makes a choice.
        self.player.flip_chosen_coin(p_fair=P_FAIR, p_biased=P_BIASED)


class RevealCoinOutcome(Page):
    """
    Page revealing the outcome of the chosen coin.
    """
    def vars_for_template(self):
        return {
            'chosen_coin_result': self.player.chosen_coin_result, 'round_number': self.round_number
        }
    
    def is_displayed(self):
        return self.round_number <= C.NUM_ROUNDS

class ChoosePermutation(Page):
    """
    Page where participant chooses between four options.
    """
    form_model = 'player'
    form_fields = ['coin_permutation_choice']

    def before_next_page(self):
        # Flip the chosen coin after the player makes a choice.
        self.player.flip_chosen_coin(p_fair=P_FAIR, p_biased=P_BIASED)

    def is_displayed(self):
        return self.round_number <= C.NUM_ROUNDS

    def vars_for_template(self):
        return {
            'round_number': self.round_number
        }



class Results(Page):
    """
    Show overall results or feedback.
    """
    def vars_for_template(self):
        # Sum over all the winnings from each player (i.e. each round)
        return {
            'winnings': sum([player.total_winnings for player in self.player.in_all_rounds()])
        }
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS

page_sequence = [Introduction, Introduction1point5, Introduction2, ChooseCoin, RevealCoinOutcome, ChoosePermutation, Results]
