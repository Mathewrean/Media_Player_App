import os
import sys
import platform
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer

class MediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform Media Player")
        self.root.geometry("500x400")
        self.root.configure(bg="#2f2f2f")  # Dark background for contrast

        mixer.init()

        self.current_file = None

        # UI Elements
        self.add_ui_elements()

    def add_ui_elements(self):
        # Title Label
        title_label = tk.Label(self.root, text="Media Player", font=("Helvetica", 20, "bold"), bg="#2f2f2f", fg="#ff9900")
        title_label.pack(pady=20)

        # File Selection Button
        open_file_btn = tk.Button(self.root, text="Open File", command=self.open_file, width=15, font=("Helvetica", 12), bg="#5bc0de", fg="black", relief="raised", bd=3)
        open_file_btn.pack(pady=10)

        # Control Buttons Frame
        controls_frame = tk.Frame(self.root, bg="#2f2f2f")
        controls_frame.pack(pady=30)

        play_btn = tk.Button(controls_frame, text="Play", command=self.play_media, width=10, font=("Helvetica", 12), bg="#ff7f32", fg="black", relief="raised", bd=3)
        play_btn.grid(row=0, column=0, padx=10)

        pause_btn = tk.Button(controls_frame, text="Pause", command=self.pause_media, width=10, font=("Helvetica", 12), bg="#5bc0de", fg="black", relief="raised", bd=3)
        pause_btn.grid(row=0, column=1, padx=10)

        stop_btn = tk.Button(controls_frame, text="Stop", command=self.stop_media, width=10, font=("Helvetica", 12), bg="#ff7f32", fg="black", relief="raised", bd=3)
        stop_btn.grid(row=0, column=2, padx=10)

        # Status Label
        self.status_label = tk.Label(self.root, text="Select a file to play", font=("Helvetica", 12), bg="#2f2f2f", fg="#5bc0de")
        self.status_label.pack(pady=10)

    def open_file(self):
        file_types = [
            ("Audio Files", "*.mp3;*.wav;*.ogg"),
            ("Video Files", "*.mp4;*.avi;*.mkv"),
            ("All Files", "*.*")
        ]

        file_path = filedialog.askopenfilename(filetypes=file_types)

        if file_path:
            self.current_file = file_path
            self.status_label.config(text=f"Loaded: {os.path.basename(file_path)}")
            self.play_media()

    def play_media(self):
        if not self.current_file:
            messagebox.showwarning("No File", "Please select a file first!")
            return
        
        try:
            mixer.music.load(self.current_file)
            mixer.music.play()
            self.status_label.config(text="Playing...")
        except Exception as e:
            messagebox.showerror("Playback Error", f"Unable to play file: {e}")

    def pause_media(self):
        mixer.music.pause()
        self.status_label.config(text="Paused")

    def stop_media(self):
        mixer.music.stop()
        self.current_file = None
        self.status_label.config(text="Stopped")

if __name__ == "__main__":
    os_platform = platform.system()
    print(f"Running on {os_platform}")

    root = tk.Tk()
    app = MediaPlayer(root)
    root.mainloop()

