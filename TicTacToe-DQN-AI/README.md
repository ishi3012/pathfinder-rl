# Tic-Tac-Toe AI with Deep Q-Networks (DQN)

<!-- 🚀 An AI-powered **Tic-Tac-Toe game** that learns to play optimally using **Deep Q-Networks (DQN)**, trained through **Reinforcement Learning (RL)**. Play against a trained AI that continuously improves through self-play! -->
🚀 An AI-powered **Tic-Tac-Toe game** that learns to play optimally, trained through **Reinforcement Learning (RL)**. Play against a trained AI that continuously improves through self-play! 
---

## 📌 Features
<!-- ✅ **AI-powered Tic-Tac-Toe** with **DQN (Deep Q-Networks)**   -->
✅ **Self-learning AI** that improves over time  
✅ **Play vs AI** with real-time decision-making  
✅ **Web Interface with Flask/Streamlit**  
✅ **Customizable training parameters** for better learning  

---

## 📥 Installation & Setup
### 🔹 Clone the Repository
```bash
git clone https://github.com/ishi3012/rl-lab
cd TicTacToe-DQN-AI
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🎮 Running the Project

### 1️⃣ Train and Play with AI (Single File)
All functionalities, including training and gameplay, are handled within **`game_logic.py`**. To run the project, use the following command:
```bash
python src/game_logic.py
```
📌 **This script will train the AI using Deep Q-Learning and allow you to play against it in various modes.**

### 2️⃣ Play Against AI (CLI Version)
Run the script to interact with the AI in a **command-line interface**:
```bash
python src/game_logic.py --cli
```
You'll be prompted to **enter your moves**, and the AI will respond accordingly.

### 3️⃣ Run GUI Version
Launch a graphical interface for Tic-Tac-Toe:
```bash
python src/game_logic.py --gui
```
This will open a **modern Tic-Tac-Toe board**, allowing you to **click to make your moves** against the AI.

### 4️⃣ Run Web App (Flask)
Host the AI-powered Tic-Tac-Toe game using Flask:
```bash
python src/game_logic.py --flask
```
Then open **http://127.0.0.1:5000/** in your browser to play.

### 5️⃣ Run Web App (Streamlit)
For a web-based experience with a user-friendly UI, launch the AI with **Streamlit**:
```bash
streamlit run src/game_logic.py
```
This starts an interactive web-based Tic-Tac-Toe AI, making it easy to play and visualize the AI’s learning process.

---





## 📂 Project Structure
```
📂 TicTacToe-DQN-AI  # Tic-Tac-Toe AI Project
│── 📂 models        # Stores trained models
│   │── dqn_tictactoe.pth  # Trained DQN model
│── 📂 src           # Source code for the project
│   │── game_logic.py  # DQN AI training script
│── 📂 notebooks   # Jupyter Notebooks for experiments
│── 📜 README.md   # Documentation for this project
│── 📜 requirements.txt  # Python dependencies
```

<!-- ---

## ⚡ Customization
- Adjust **AI Training Parameters** in `src/train_dqn.py`  
- Modify **GUI Design** in `src/gui_tictactoe.py`  
- Customize **Web Interface** in `src/app.py` (Flask) or `src/streamlit_app.py`  

--- -->

<!-- ## 🚀 Deployment Options
✅ **Flask & Render:** Deploy Tic-Tac-Toe AI using **Flask + Render.com**  
✅ **Streamlit Cloud:** Deploy **Tic-Tac-Toe AI** on **Streamlit Sharing**  
✅ **GitHub Actions:** Automate training updates & deployment  

--- -->

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

## 📩 Contact & Contributions
<!-- - 🔗 [GitHub :](https://github.com/ishi3012) -->
- 📧 [Email :](shilpa.musale02@gmail.com)

🚀 **Feel free to fork, contribute, and improve this project!** 🏆

---

### 🎉 Enjoy playing Tic-Tac-Toe with an AI that learns! 🚀

