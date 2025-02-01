import streamlit as st
import numpy as np
import pickle
import random
import os

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="🤖", layout="centered")

class TicTacToeAI:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}         # Q-table for training (placeholder implementation)
        self.alpha = alpha        # Learning rate
        self.gamma = gamma        # Discount factor
        self.epsilon = epsilon    # Exploration rate
        self.load_q_table()       # Load saved model if available

    def reset_board(self):
        """Return a new 3x3 board filled with '-' characters."""
        return np.full((3, 3), '-', dtype=str)

    def get_state(self, board):
        """Convert the board into a string state."""
        return ''.join(board.flatten())

    def get_valid_moves(self, board):
        """Return a list of all valid moves as (row, col) tuples."""
        return [(r, c) for r in range(3) for c in range(3) if board[r, c] == '-']

    def choose_action(self, board):
        """Choose an action based on the current board state using ε-greedy strategy."""
        state = self.get_state(board)
        valid_moves = self.get_valid_moves(board)
        if not valid_moves:
            return None
        if random.uniform(0, 1) < self.epsilon:
            # Exploration: pick a random valid move.
            return random.choice(valid_moves)
        else:
            # Exploitation: pick the move with the highest Q-value.
            q_values = {move: self.q_table.get((state, move), 0) for move in valid_moves}
            return max(q_values, key=q_values.get) if q_values else random.choice(valid_moves)

    def check_winner(self, board, player):
        """Check if the given player ('X' or 'O') has won."""
        for i in range(3):
            if all(board[i, :] == player) or all(board[:, i] == player):
                return True
        if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
            return True
        return False

    def save_q_table(self):
        """Save the Q-table to a file."""
        with open("q_table.pkl", "wb") as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self):
        """Load the Q-table from a file if it exists."""
        if os.path.exists("q_table.pkl"):
            with open("q_table.pkl", "rb") as f:
                self.q_table = pickle.load(f)

    def train(self, episodes=5000):
        """
        Train the AI over a number of episodes.
        This is a placeholder training loop. Replace it with your own Q-learning updates.
        """
        for episode in range(episodes):
            board = self.reset_board()
            done = False
            # Simple training simulation: let the AI (as 'X') play against random moves ('O').
            while not done:
                valid_moves = self.get_valid_moves(board)
                if not valid_moves:
                    break
                move = self.choose_action(board)
                if move is None:
                    break
                board[move] = "X"
                if self.check_winner(board, "X"):
                    # Placeholder: update Q-table for win if desired.
                    done = True
                    break
                valid_moves = self.get_valid_moves(board)
                if not valid_moves:
                    break
                opponent_move = random.choice(valid_moves)
                board[opponent_move] = "O"
                if self.check_winner(board, "O"):
                    # Placeholder: update Q-table for loss if desired.
                    done = True
                    break
        # Save the Q-table after training.
        self.save_q_table()

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
            color: #e0e0e0;
        }
        .stApp {
            background-color: #f5f5f5;
            color: #333;
        }
        .stButton>button {
            background-color: #ff9800;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #e68900;
        }
        .win-message {
            font-size: 24px;
            font-weight: bold;
            color: #120af5;
            text-align: center;
        }
        .tic-tac-toe-grid button {
            font-size: 24px;
            height: 70px;
            width: 70px;
            background-color: #ffffff;
            color: #ffffff;
            border: 2px solid #ffffff;
            border-radius: 5px;
            transition: 0.3s;
        }
        .tic-tac-toe-grid button:hover {
            background-color: #444;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Tic-Tac-Toe AI Trainer & Game")

# Initialize session state variables
if "ai" not in st.session_state:
    st.session_state.ai = TicTacToeAI()
if "board" not in st.session_state:
    st.session_state.board = st.session_state.ai.reset_board()
    st.session_state.winner = None

def reset_game():
    """Reset the game board and winner status."""
    st.session_state.board = st.session_state.ai.reset_board()
    st.session_state.winner = None

def make_move(row, col):
    """
    Process a human move at position (row, col), then let the AI respond.
    """
    # Process human move if the cell is empty and game is not over.
    if st.session_state.board[row, col] == '-' and not st.session_state.winner:
        st.session_state.board[row, col] = "O"  # Human plays 'O'
        if st.session_state.ai.check_winner(st.session_state.board, "O"):
            st.session_state.winner = "🎉 You Win!"
            return
        if not st.session_state.ai.get_valid_moves(st.session_state.board):
            st.session_state.winner = "🤝 It's a Draw!"
            return

        # Process AI move.
        ai_move = st.session_state.ai.choose_action(st.session_state.board)
        if ai_move is not None:
            st.session_state.board[ai_move] = "X"
            if st.session_state.ai.check_winner(st.session_state.board, "X"):
                st.session_state.winner = "😢 AI Wins!"
                return

st.subheader("🎮 Play Against AI")
# Display the board in a grid layout
grid_container = st.container()
with grid_container:
    for r in range(3):
        cols = st.columns(3)
        for c in range(3):
            with cols[c]:
                if st.session_state.board[r, c] == '-':
                    if st.button(" ", key=f"{r}-{c}", help="Click to play", use_container_width=True):
                        make_move(r, c)
                else:
                    st.button(st.session_state.board[r, c],
                              disabled=True,
                              key=f"{r}-{c}-disabled",
                              use_container_width=True)

if st.session_state.winner:
    st.markdown(f'<p class="win-message">{st.session_state.winner}</p>', unsafe_allow_html=True)

st.button("🔄 Restart Game", on_click=reset_game)

st.subheader("🎓 Train AI")
if st.button("📈 Train AI (5,000 games)"):
    st.session_state.ai.train(episodes=5000)
    st.success("✅ AI training completed! Ready to play.")


