import matplotlib.pyplot as plt
import numpy as np
import __main__ as main

from agent import Agent
from game import Game
from board import Board

import PySimpleGUI as sg

from lang import lang_DE
LANG_DICT = lang_DE





class gui():

    def update_game_state(self, board):
        self.board = board
        for row in range(3):
            for col in range(3):
                label = Board.field_state_to_str_map[self.board[row][col]]
                self.window[(row,col)].update(label)
        

    def update_top_message(self, message):
        self.window['-HEAD_TEXT-'].update(message)

    def listen_input(self):
        event, values = self.window.Read()
        print(event, values)
        return event

    def write(self, message):
        print(message)
        self.update_top_message(message)


    def gui_duel(self, agent, opponent, no_episodes, rng, *, verbose=False):

        display_text = 'Example'

        sg.theme('DarkAmber')    # Keep things interesting for your users

        BUTTON_SIZE = (2,2)

        self.layout = [[[sg.Text(LANG_DICT['new_game']), sg.Text(size=(20,1), key='-HEAD_TEXT-')],
                   [sg.Button(' ', size=BUTTON_SIZE, key=(0,0)), sg.Button(' ', size=BUTTON_SIZE, key=(0,1)), sg.Button(' ', size=BUTTON_SIZE, key=(0,2))],
                   [sg.Button(' ', size=BUTTON_SIZE, key=(1,0)), sg.Button(' ', size=BUTTON_SIZE, key=(1,1)), sg.Button(' ', size=BUTTON_SIZE, key=(1,2))],
                   [sg.Button(' ', size=BUTTON_SIZE, key=(2,0)), sg.Button(' ', size=BUTTON_SIZE, key=(2,1)), sg.Button(' ', size=BUTTON_SIZE, key=(2,2))]
                   ]]

        self.window = sg.Window(LANG_DICT['game_title'], self.layout)

        # a modified version of main.duel with GUI implementation
        history_result = []
        while True:             # Event Loop

            # if game is not None:
            #     HEAD_TEXT = 'NEW TITLE'

            event, values = self.window.Read(timeout=1)
            self.window['-HEAD_TEXT-'].update('Neues Spiel')

            main.duel(agent, opponent, no_episodes, rng, verbose=verbose, print_file=self)

            # (state, winner) = game.play(verbose)

            # if event in (None, 'Exit'):
            #     break
            # if callable(event):
            #     event()
            # window['-HEAD_TEXT-'].update(HEAD_TEXT)

        window.close()







        
        

        # if state == Game.GameState.DRAW:
        #     history_result.append(0.0)
        #     for p in game.players:
        #         final_reward = 0.0
        #         p.update_policy(final_reward)
        # else:
        #     if winner == game.assigned_markers[0]:
        #         history_result.append(1.0)
        #     else:
        #         history_result.append(-1.0)
        #     for p in game.players:
        #         if winner == p.marker:
        #             final_reward = 1.0
        #         else:
        #             final_reward = -1.0
        #         p.update_policy(final_reward)

        # if episode > 0 and episode % 1000 == 0:
        #     print(episode)