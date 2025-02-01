# Reinforcement Learning Projects


🚀 A collection of Reinforcement Learning (RL) projects implementing Q-Learning, Deep Q-Networks (DQN), and Policy Gradient methods in various environments. Each project showcases different RL concepts with implementations in Python, OpenAI Gym, TensorFlow/PyTorch, and web-based applications.

## 📌 Projects in Repository

This repository currently contains the following RL projects:

| 📁 Project          | 🏆 Algorithm               | 🖥️ Implementation                    |
|---------------------|--------------------------|--------------------------------------|
| **CliffWalking-RL** | Q-Learning               | OpenAI Gym, NumPy                   |
| **TicTacToe-DQN-AI** | Deep Q-Networks (DQN)    | PyTorch, Streamlit  |
| **Snake-RL**        | Deep Q-Learning          | PyTorch, Pygame                     |

More projects will be added over time! 🚀

## 📂 Repository Structure
```
📂 RL-Projects-Portfolio (Root Repository) 
│
├── 📂 CliffWalking-RL (Cliff Walking using Q-Learning)
│       ├── 📂 src (Python code)
│       ├── 📂 logs (Training logs)
│       ├── 📜 README.md (Project documentation)
│
├── 📂 TicTacToe-DQN-AI (Tic-Tac-Toe AI using Deep Q-Networks)
│       ├── 📂 src (Source code: training, GUI, web app)
│       ├── 📂 models (Saved trained models)
│       ├── 📂 web (Web frontend for Flask & Streamlit)
│       ├── 📂 logs (Training logs)
│       ├── 📜 README.md (Project documentation)
│
├── 📂 Snake-RL (Snake game AI using Deep Q-Learning)
│       ├── 📂 src (Python code for training & playing)
│       ├── 📂 models (Saved trained models)
│       ├── 📜 README.md (Project documentation)
│
├── 📜 README.md (This file - Main repository documentation)
├── 📜 LICENSE (License for the repository)
```

## 📥 Installation & Setup

### 🔹 Clone the Repository
```
git clone https://github.com/YOUR_USERNAME/RL-Projects-Portfolio.git
cd RL-Projects-Portfolio
```

### 🔹 Install Dependencies
```
cd TicTacToe-DQN-AI
pip install -r requirements.txt

```

## 🚀 Running the Projects

### 1️⃣ CliffWalking-RL (Q-Learning)
Description: An AI learns to walk across a dangerous cliff without falling using Q-learning.

Run Training
```
cd CliffWalking-RL/src
python train_q_learning.py
```
Run AI Agent
```
python play_q_learning.py
```

### 2️⃣ Tic-Tac-Toe AI (DQN)
Description: A Deep Q-Networks (DQN) based AI that learns to play Tic-Tac-Toe through reinforcement learning.

Run Training
```
cd TicTacToe-DQN-AI/src
python train_dqn.py
```
Play Against AI (CLI Version)
```
python play_vs_ai.py
```
Run GUI Version
```
python gui_tictactoe.py
```

Run Web App (Flask)
```
cd TicTacToe-DQN-AI
python app.py
```
Open http://127.0.0.1:5000/ in your browser.

Run Web App (Streamlit)
```
streamlit run streamlit_app.py
```
### 3️⃣ Snake Game AI (DQN)
Description: The Snake Game AI learns to play the classic Snake Game using Deep Q-Learning.

Run Training
```
cd Snake-RL/src
python train_snake.py
```
Run AI Agent
```
python play_snake.py
```
Run GUI Version
```
python gui_snake.py
```

## 📊 Visualizing AI Training

Each project includes a training visualization script that plots the AI's learning progress.

Example for Tic-Tac-Toe AI:
```
python visualize_training.py
```

## 🌍 Deployment Options
- ✅ Flask & Render: Deploy Tic-Tac-Toe AI using Flask + Render.com
- ✅ Streamlit Cloud: Deploy Tic-Tac-Toe AI on Streamlit Sharing
- ✅ GitHub Actions: Automate training updates & deployment

## 🛠️ Customization
- Modify hyperparameters (learning rate, gamma, epsilon) in training scripts.
- Adjust reward functions to improve learning.
- Customize UI (Tkinter, Flask, Streamlit, Pygame) to enhance user experience.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## 📩 Contact & Contributions

- 🔗 [GitHub :](https://github.com/ishi3012)
- 📧 [Email :](shilpa.musale02@gmail.com)

🚀 Feel free to fork, contribute, and improve these projects! 🏆