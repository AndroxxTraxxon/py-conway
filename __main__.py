"""
Author: David Culbreth
Class: CS6375A: Python & Machine Learning
Professor: Dr. Art Hanna
Final Exam: Conway's Game of Life

__main__.py
"""
import time
import tkinter as tk
import tkinter.filedialog as filedialog
import sys

from conway import Conway

def parse_file(worldfile):
    row_count = int(worldfile.readline().strip())
    col_count = int(worldfile.readline().strip())
    data = []
    for r in range(row_count):
        row = tuple(c=='*' for c in worldfile.readline().strip())
        assert len(row) == col_count, f"Row {r} is too long!"
        data.append(row)
    return row_count, col_count, data

if __name__ == "__main__":
    root = tk.Tk()
    filepath = None
    if len(sys.argv) < 2:
        filepath = filedialog.askopenfilename(title="Open Conway World...", 
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    else:
        filepath = sys.argv[1]

    with open(filepath) as worldfile:
        row_count, col_count, cells = parse_file(worldfile) 

    app = Conway(row_count, col_count, cells, root)
    while True:
        app.tick()
        root.update()
        root.update_idletasks()
        time.sleep(0.5)
    # root.mainloop()