import customtkinter as ctk
import random
from collections import Counter

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Dice ASCII faces
dice_faces = {
    1: "   •   ",
    2: " •   • ",
    3: " • • • ",
    4: "• • • •",
    5: "• • • •\n   •   ",
    6: "• • •\n• • •"
}

# AI Class
class DiceAI:
    def __init__(self):
        self.history = []

    def update(self, roll):
        self.history.append(roll)

    def predict_next(self):
        if len(self.history) == 0:
            return "No data"
        count = Counter(self.history)
        return count.most_common(1)[0][0]

    def get_stats(self):
        count = Counter(self.history)
        total = len(self.history)

        stats = ""
        for i in range(1, 7):
            freq = count[i]
            prob = (freq / total * 100) if total > 0 else 0
            stats += f"{i}: {freq} ({prob:.2f}%)\n"
        return stats

# Main App
class DiceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dice Simulator with AI")
        self.geometry("500x500")

        self.ai = DiceAI()

        # Title
        self.title_label = ctk.CTkLabel(self, text="🎲 Dice Simulator", font=("Arial", 22))
        self.title_label.pack(pady=15)

        # Dice Display
        self.dice_label = ctk.CTkLabel(self, text="Roll the dice!", font=("Courier", 24))
        self.dice_label.pack(pady=20)

        # Prediction Label
        self.prediction_label = ctk.CTkLabel(self, text="AI Prediction: -", font=("Arial", 14))
        self.prediction_label.pack(pady=10)

        # Stats Box
        self.stats_box = ctk.CTkTextbox(self, width=300, height=150)
        self.stats_box.pack(pady=10)
        self.stats_box.insert("0.0", "No data yet")

        # Roll Button
        self.roll_button = ctk.CTkButton(self, text="Roll Dice 🎲", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Exit Button
        self.exit_button = ctk.CTkButton(self, text="Exit", fg_color="red", command=self.quit)
        self.exit_button.pack(pady=10)

    def roll_dice(self):
        result = random.randint(1, 6)

        # Update Dice Display
        self.dice_label.configure(text=f"You rolled: {result}\n{dice_faces[result]}")

        # Update AI
        self.ai.update(result)

        # Prediction
        prediction = self.ai.predict_next()
        self.prediction_label.configure(text=f"AI Prediction: {prediction}")

        # Stats
        stats = self.ai.get_stats()
        self.stats_box.delete("0.0", "end")
        self.stats_box.insert("0.0", stats)

# Run App
if __name__ == "__main__":
    app = DiceApp()
    app.mainloop()
