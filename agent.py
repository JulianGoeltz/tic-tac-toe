import json
import numpy as np


class Agent:

    action_idx_to_move = {
        row * 3 + col: (row, col) for row in range(3) for col in range(3)
    }

    move_to_action_idx = {value: key for key, value in action_idx_to_move.items()}

    def __init__(self, seed):
        self.policy = {}
        self.rng = np.random.default_rng(seed)

    def get_move(self, game):
        hsh = game.state_hash()

        if hsh not in self.policy:
            print("new state", hsh)
            self.policy[hsh] = np.ones(9) * 1 / 9.0

        while True:
            action_idx = np.argmax(self.sample_action(self.policy[hsh]))
            move = self.action_idx_to_move[action_idx]
            if game.is_empty(move[0], move[1]):
                return move

    def load_policy(self, fn):
        with open(fn, "r") as f:
            policy = json.load(f)
        for hsh in policy:
            policy[hsh] = np.array(policy[hsh])
        self.policy = policy

    def sample_action(self, probs):
        return self.rng.multinomial(1, pvals=probs)

    def save_policy(self, fn):
        policy = {}
        for hsh in self.policy:
            policy[hsh] = self.policy[hsh].tolist()

        with open(fn, "w") as f:
            json.dump(policy, f)
