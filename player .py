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
        self.root.geometry("400x200")
        
        mixer.init()

        self.current_file = None

        # UI Elements
        self.add_buttons()

    def add_buttons(self):
        play_btn = tk.Button(self.root, text="Play", command=self.play_media, width=10)
        play_btn.pack(pady=10)

        pause_btn = tk.Button(self.root, text="Pause", command=self.pause_media, width=10)
        pause_btn.pack(pady=10)

        stop_btn = tk.Button(self.root, text="Stop", command=self.stop_media, width=10)
        stop_btn.pack(pady=10)

        open_file_btn = tk.Button(self.root, text="Open File", command=self.open_file, width=10)
        open_file_btn.pack(pady=10)

    def open_file(self):
        file_types = [
            ("Audio Files", "*.mp3;*.wav;*.ogg"),
            ("Video Files", "*.mp4;*.avi;*.mkv"),
            ("All Files", "*.*")
        ]

        file_path = filedialog.askopenfilename(filetypes=file_types)

        if file_path:
            self.current_file = file_path
            self.play_media()

    def play_media(self):
        if not self.current_file:
            messagebox.showwarning("No File", "Please select a file first!")
            return
        
        mixer.music.load(self.current_file)
        mixer.music.play()

    def pause_media(self):
        mixer.music.pause()

    def stop_media(self):
        mixer.music.stop()
        self.current_file = None

if __name__ == "__main__":
    # Determine platform
    os_platform = platform.system()
    print(f"Running on {os_platform}")

    root = tk.Tk()
    app = MediaPlayer(root)
    root.mainloop()
