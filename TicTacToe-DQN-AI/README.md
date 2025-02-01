# Tic-Tac-Toe AI with Deep Q-Networks (DQN)

🚀 An AI-powered **Tic-Tac-Toe game** that learns to play optimally using **Deep Q-Networks (DQN)**, trained through **Reinforcement Learning (RL)**. Play against a trained AI that continuously improves through self-play!

---

## 📌 Features
✅ **AI-powered Tic-Tac-Toe** with **DQN (Deep Q-Networks)**  
✅ **Self-learning AI** that improves over time  
✅ **Play vs AI** with real-time decision-making  
✅ **GUI with Tkinter or Web Interface with Flask/Streamlit**  
✅ **Customizable training parameters** for better learning  

---

## 📥 Installation & Setup
### 🔹 Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/TicTacToe-DQN-AI.git
cd TicTacToe-DQN-AI
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🎮 Running the Project
### 1️⃣ Train the AI (Deep Q-Learning)
Run the training script to train the AI:
```bash
python src/train_dqn.py
```
📌 **This will train the AI for thousands of episodes and save the trained model (`models/dqn_tictactoe.pth`).**  

### 2️⃣ Play Against AI (CLI Version)
```bash
python src/play_vs_ai.py
```
You'll be prompted to **enter your moves** in a **command-line interface** while the AI responds with its moves.

### 3️⃣ Run GUI Version
```bash
python src/gui_tictactoe.py
```
This will open a **modern Tic-Tac-Toe board**, where you can **click** to make your moves.

### 4️⃣ Run Web App (Flask)
```bash
cd TicTacToe-DQN-AI
python src/app.py
```
Open **http://127.0.0.1:5000/** in your browser.

### 5️⃣ Run Web App (Streamlit)
```bash
streamlit run src/streamlit_app.py
```
This launches an interactive **web-based Tic-Tac-Toe AI**.

---

## 📊 Visualizing Training Progress
To see how the AI improves over time, run:
```bash
python src/visualize_training.py
```
This plots the **training reward progression** over episodes.

---

## 📂 Project Structure
```
📂 TicTacToe-DQN-AI  # Tic-Tac-Toe AI Project
│── 📂 models        # Stores trained models
│   │── dqn_tictactoe.pth  # Trained DQN model
│── 📂 src           # Source code for the project
│   │── train_dqn.py  # DQN AI training script
│   │── play_vs_ai.py  # Command-line AI opponent
│   │── gui_tictactoe.py  # Tkinter-based GUI
│   │── app.py  # Flask backend for web app
│   │── streamlit_app.py  # Streamlit-based web app
│── 📂 web          # Frontend for Flask-based Web App
│   │── templates
│   │   │── index.html  # Main HTML file
│   │── static  # CSS/JS (if needed)
│── 📂 logs        # Stores training logs
│── 📂 notebooks   # Jupyter Notebooks for experiments
│── 📜 README.md   # Documentation for this project
│── 📜 requirements.txt  # Python dependencies
```

---

## ⚡ Customization
- Adjust **AI Training Parameters** in `src/train_dqn.py`  
- Modify **GUI Design** in `src/gui_tictactoe.py`  
- Customize **Web Interface** in `src/app.py` (Flask) or `src/streamlit_app.py`  

---

## 🚀 Deployment Options
✅ **Flask & Render:** Deploy Tic-Tac-Toe AI using **Flask + Render.com**  
✅ **Streamlit Cloud:** Deploy **Tic-Tac-Toe AI** on **Streamlit Sharing**  
✅ **GitHub Actions:** Automate training updates & deployment  

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 📩 Contact & Contributions
🐦 **Twitter:** [@yourusername](https://twitter.com/yourusername)  
🔗 **GitHub:** [your-github](https://github.com/YOUR_USERNAME)  
📧 **Email:** your-email@example.com  

🚀 **Feel free to fork, contribute, and improve this project!** 🏆

---

### 🎉 Enjoy playing Tic-Tac-Toe with an AI that learns! 🚀

