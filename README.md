# 🎲 Dice Simulator with AI

A modern GUI-based dice rolling simulator built using **CustomTkinter**, enhanced with a simple AI that tracks roll history and predicts future outcomes.

---

## ✨ Features =>

- 🎯 **Random Dice Roll** (1–6)
- 🤖 **AI Prediction System**
- 📊 **Probability & Frequency Tracking**
- 🖥️ **Modern Dark-Themed GUI**
- 📦 **Lightweight & Easy to Run**

---

## 🧠 How the AI Works =>

The AI is based on a simple statistical approach:

- Stores previous dice rolls 📚 
- Uses `Counter` to calculate frequency 📊
- Predicts the **most frequently rolled number** 🔮

> ⚠️ Note: This is not true AI—just a basic probability-based prediction.

---

## 🖼️ Interface Overview =>

| Section            | Description |
|-------------------|------------|
| 🎲 Dice Display    | Shows the rolled number with ASCII face |
| 🤖 Prediction      | Displays AI’s next prediction |
| 📊 Stats Box       | Shows frequency & probability |
| 🎮 Roll Button     | Rolls the dice |
| ❌ Exit Button     | Closes the application |

---

## 🛠️ Requirements =>

Make sure you have the following installed on your device:

- Python 3.x 🐍
- `customtkinter`

### Install dependencies:

```bash
pip install customtkinter
