import tkinter as tk
from tkinter import messagebox
from dictionary import Dictionary

class DictionaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English Dictionary")
        self.root.geometry("400x300")

        self.create_widgets()
        self.dictionary = Dictionary()

    def create_widgets(self):
        # Input Field
        self.word_label = tk.Label(self.root, text="Enter a word:")
        self.word_label.pack(pady=10)

        self.word_entry = tk.Entry(self.root, width=30)
        self.word_entry.pack(pady=5)

        # Search Button
        self.search_button = tk.Button(self.root, text="Search", command=self.search_word)
        self.search_button.pack(pady=20)

        # Result Area
        self.result_area = tk.Text(self.root, width=50, height=10, wrap=tk.WORD)
        self.result_area.pack(pady=10)

    def search_word(self):
        word = self.word_entry.get().strip()
        if word:
            meaning = self.dictionary.get_meaning(word)
            if meaning:
                self.result_area.delete(1.0, tk.END)  # Clear previous results
                self.result_area.insert(tk.END, f"Meaning of '{word}':\n{meaning}")
            else:
                messagebox.showinfo("Result", "Word not found!")
        else:
            messagebox.showwarning("Input Error", "Please enter a word.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
