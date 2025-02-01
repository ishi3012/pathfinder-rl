import streamlit as st
import numpy as np
import pickle
import random
import os

# Define Tic-Tac-Toe class with training and AI logic
class TicTacToeAI:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.board = np.full((3, 3), '-', dtype=str)
        self.q_table = {}  # Q-table for training
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.load_q_table()  # Load model if available
        self.current_player = 'X' 

    def reset_board(self):
        self.board.fill('-')

    def get_state(self):
        return ''.join(self.board.flatten())

    def get_valid_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r, c] == '-']

    def choose_action(self):
        state = self.get_state()
        if random.uniform(0, 1) < self.epsilon:  # Exploration
            return random.choice(self.get_valid_moves())
        else:  # Exploitation
            q_values = {move: self.q_table.get((state, move), 0) for move in self.get_valid_moves()}
            return max(q_values, key=q_values.get) if q_values else random.choice(self.get_valid_moves())

    def make_move(self, row, col, player):
        if self.board[row, col] == '-':
            self.board[row, col] = player
            return True
        return False

    # def check_winner(self):
    #     for i in range(3):
    #         if all(self.board[i, :] == self.board[i, 0]) and self.board[i, 0] != '-':
    #             return True
    #         if all(self.board[:, i] == self.board[0, i]) and self.board[0, i] != '-':
    #             return True
    #     if all(np.diag(self.board) == self.board[0, 0]) and self.board[0, 0] != '-':
    #         return True
    #     if all(np.diag(np.fliplr(self.board)) == self.board[0, 2]) and self.board[0, 2] != '-':
    #         return True
    #     return False

    def check_winner(self, player):
        """Correctly check if the given player has won."""
        for i in range(3):
            if all(self.board[i, :] == player) or all(self.board[:, i] == player):
                return True
        if all(np.diag(self.board) == player) or all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def update_q_table(self, state, action, reward, next_state):
        old_value = self.q_table.get((state, action), 0)
        future_q = max([self.q_table.get((next_state, move), 0) for move in self.get_valid_moves()], default=0)
        self.q_table[(state, action)] = old_value + self.alpha * (reward + self.gamma * future_q - old_value)

    def train(self, episodes=5000):
        for _ in range(episodes):
            self.reset_board()
            game_history = []
            while True:
                state = self.get_state()
                action = self.choose_action()
                self.make_move(*action, 'X')

                if self.check_winner():
                    reward = 1
                    self.update_q_table(state, action, reward, self.get_state())
                    break
                elif len(self.get_valid_moves()) == 0:
                    reward = 0
                    self.update_q_table(state, action, reward, self.get_state())
                    break
                else:
                    game_history.append((state, action))
                    self.switch_player()

            for state, action in game_history:
                self.update_q_table(state, action, -1, self.get_state())

        self.save_q_table()

    def save_q_table(self):
        with open("q_table.pkl", "wb") as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self):
        if os.path.exists("q_table.pkl"):
            with open("q_table.pkl", "rb") as f:
                self.q_table = pickle.load(f)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


# Streamlit UI
st.title("🤖 Tic-Tac-Toe AI Trainer & Game")

# Initialize AI
if "ai" not in st.session_state:
    st.session_state.ai = TicTacToeAI()

# Training Section
st.header("🎓 Train AI")
if st.button("Train AI (5,000 games)"):
    st.session_state.ai.train(episodes=5000)
    st.success("AI training completed! Ready to play.")

# Game Section
st.header("🎮 Play Against AI")

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = np.full((3, 3), '-', dtype=str)
    st.session_state.current_player = "O"

def reset_game():
    """Reset the board"""
    st.session_state.board = np.full((3, 3), '-', dtype=str)
    st.session_state.current_player = "O"

def make_move(row, col):
    """Handle human move and AI response"""
    if st.session_state.board[row, col] == '-':
        st.session_state.board[row, col] = "O"  # Human plays 'O'
        if st.session_state.ai.check_winner('O'):
            st.session_state.winner = "🎉 You Win!"
            return

        if len(st.session_state.ai.get_valid_moves()) == 0:
            st.session_state.winner = "🤝 It's a Draw!"
            return

        # AI move
        ai_move = st.session_state.ai.choose_action()
        st.session_state.board[ai_move] = "X"
        if st.session_state.ai.check_winner('X'):
            st.session_state.winner = "😢 AI Wins!"
            return
        if len(st.session_state.ai.get_valid_moves()) == 0:
            st.session_state.winner = "It's a Draw! 🤝"
            return
        # AI move
        ai_move = st.session_state.ai.choose_action()
        st.session_state.board[ai_move] = "X"
        if st.session_state.ai.check_winner():
            st.session_state.winner = "AI Wins! 😢"
            return

# Display board
st.session_state.winner = None
# for r in range(3):
#     cols = st.columns(3)
#     for c in range(3):
#         with cols[c]:
#             if st.button(st.session_state.board[r, c] if st.session_state.board[r, c] != '-' else " ", key=f"{r}{c}"):
#                 make_move(r, c)

st.write("### 🏆 Tic-Tac-Toe Board")

board_placeholder = st.empty()

def render_board():
    """Render the Tic-Tac-Toe board with correct alignment."""
    with board_placeholder.container():
        for r in range(3):
            cols = st.columns(3)
            for c in range(3):
                with cols[c]:
                    if st.session_state.board[r, c] == '-':
                        if st.button(" ", key=f"{r}{c}"):
                            make_move(r, c)
                    else:
                        st.button(st.session_state.board[r, c], disabled=True, key=f"{r}{c}_disabled")

render_board()


# Display result
if st.session_state.winner:
    st.subheader(st.session_state.winner)

st.button("Restart Game", on_click=reset_game)
