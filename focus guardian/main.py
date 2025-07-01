import tkinter as tk
from tkinter import messagebox
import time
import threading
import random
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from pynput import mouse, keyboard

# Motivational quotes
QUOTES = [
    "Stay focused and never give up!",
    "Your only limit is your mind.",
    "Small steps every day lead to big results.",
    "Discipline is the bridge between goals and success.",
    "Push yourself because no one else is going to do it for you."
]

class FocusGuardian:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Focus Guardian")
        self.root.geometry("400x300")

        self.is_focusing = False
        self.start_time = None

        self.create_widgets()
        self.init_db()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Focus Guardian", font=("Arial", 14))
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Focus", command=self.start_focus, bg="green", fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop Focus", command=self.stop_focus, bg="red", fg="white", state="disabled")
        self.stop_button.pack(pady=5)

        self.report_button = tk.Button(self.root, text="Show Report", command=self.show_report)
        self.report_button.pack(pady=20)

    def init_db(self):
        self.conn = sqlite3.connect("focus_data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS focus_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                duration INTEGER
            )
        """)
        self.conn.commit()

    def start_focus(self):
        self.is_focusing = True
        self.start_time = time.time()
        self.last_activity_time = time.time()
        self.label.config(text="You're focusing... Stay strong!")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        self.monitor_thread = threading.Thread(target=self.monitor_idle_time, daemon=True)
        self.monitor_thread.start()
        self.start_listeners()

    def start_listeners(self):
        def on_activity(*args):
            self.last_activity_time = time.time()

        self.mouse_listener = mouse.Listener(on_move=on_activity, on_click=on_activity)
        self.keyboard_listener = keyboard.Listener(on_press=on_activity)
        self.mouse_listener.start()
        self.keyboard_listener.start()

    def monitor_idle_time(self):
        while self.is_focusing:
            idle_duration = time.time() - self.last_activity_time
            if idle_duration > 60:
                self.label.config(text="⚠️ You seem distracted! Get back on track.")
            time.sleep(5)

    def stop_focus(self):
        if self.is_focusing:
            self.is_focusing = False
            if hasattr(self, 'mouse_listener'): self.mouse_listener.stop()
            if hasattr(self, 'keyboard_listener'): self.keyboard_listener.stop()

            duration = int(time.time() - self.start_time)
            self.save_session(duration)
            self.label.config(text=random.choice(QUOTES))
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            messagebox.showinfo("Focus Session Saved", f"You focused for {duration} seconds!")

    def save_session(self, duration):
        today = datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute("INSERT INTO focus_sessions (date, duration) VALUES (?, ?)", (today, duration))
        self.conn.commit()

    def show_report(self):
        self.cursor.execute("SELECT date, SUM(duration) FROM focus_sessions GROUP BY date")
        data = self.cursor.fetchall()

        if not data:
            messagebox.showinfo("Report", "No data to show yet!")
            return

        dates = [row[0] for row in data]
        durations = [row[1] / 60 for row in data]  # convert seconds to minutes

        plt.figure(figsize=(8, 4))
        plt.bar(dates, durations, color='skyblue')
        plt.xlabel("Date")
        plt.ylabel("Focus Time (minutes)")
        plt.title("Daily Focus Report")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FocusGuardian()
    app.run()
