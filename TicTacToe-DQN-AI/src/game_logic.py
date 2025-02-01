import streamlit as st
import numpy as np
import pickle
import random
import os

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="🤖", layout="centered")

class TicTacToeAI:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}  # Q-table for training
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.load_q_table()  # Load model if available

    def reset_board(self):
        return np.full((3, 3), '-', dtype=str)

    def get_state(self, board):
        return ''.join(board.flatten())

    def get_valid_moves(self, board):
        return [(r, c) for r in range(3) for c in range(3) if board[r, c] == '-']

    def choose_action(self, board):
        state = self.get_state(board)
        if random.uniform(0, 1) < self.epsilon:  # Exploration
            return random.choice(self.get_valid_moves(board))
        else:  # Exploitation
            q_values = {move: self.q_table.get((state, move), 0) for move in self.get_valid_moves(board)}
            return max(q_values, key=q_values.get) if q_values else random.choice(self.get_valid_moves(board))

    def check_winner(self, board, player):
        for i in range(3):
            if all(board[i, :] == player) or all(board[:, i] == player):
                return True
        if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
            return True
        return False

    def save_q_table(self):
        with open("q_table.pkl", "wb") as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self):
        if os.path.exists("q_table.pkl"):
            with open("q_table.pkl", "rb") as f:
                self.q_table = pickle.load(f)

st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .stApp {
            background-color: #121212;
        }
        .stButton>button {
            background-color: #1e88e5;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #1565c0;
        }
        .win-message {
            font-size: 24px;
            font-weight: bold;
            color: #FFD700;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Tic-Tac-Toe AI Trainer & Game")

if "ai" not in st.session_state:
    st.session_state.ai = TicTacToeAI()
if "board" not in st.session_state:
    st.session_state.board = st.session_state.ai.reset_board()
    st.session_state.winner = None

def reset_game():
    st.session_state.board = st.session_state.ai.reset_board()
    st.session_state.winner = None

def make_move(row, col):
    if st.session_state.board[row, col] == '-' and not st.session_state.winner:
        st.session_state.board[row, col] = "O"  # Human plays 'O'
        if st.session_state.ai.check_winner(st.session_state.board, 'O'):
            st.session_state.winner = "🎉 You Win!"
            return

        if len(st.session_state.ai.get_valid_moves(st.session_state.board)) == 0:
            st.session_state.winner = "🤝 It's a Draw!"
            return

        # AI move
        ai_move = st.session_state.ai.choose_action(st.session_state.board)
        st.session_state.board[ai_move] = "X"
        if st.session_state.ai.check_winner(st.session_state.board, 'X'):
            st.session_state.winner = "😢 AI Wins!"
            return

st.subheader("🎮 Play Against AI")

for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        with cols[c]:
            button_style = "color: white; font-size: 24px; height: 50px; width: 50px; background-color: #333; border: 1px solid white;"
            if st.session_state.board[r, c] == '-':
                if st.button(" ", key=f"{r}{c}", help="Click to play", use_container_width=True):
                    make_move(r, c)
            else:
                st.button(st.session_state.board[r, c], disabled=True, key=f"{r}{c}_disabled", use_container_width=True)

if "winner" in st.session_state and st.session_state.winner:
    st.markdown(f'<p class="win-message">{st.session_state.winner}</p>', unsafe_allow_html=True)

st.button("🔄 Restart Game", on_click=reset_game)

st.subheader("🎓 Train AI")
if st.button("📈 Train AI (5,000 games)"):
    st.session_state.ai.train(episodes=5000)
    st.success("✅ AI training completed! Ready to play.")
