"""
Author: David Culbreth
Class: CS6375A: Python & Machine Learning
Professor: Dr. Art Hanna
Final Exam: Conway's Game of Life

conway.py
"""

import tkinter as tk
import os
from PIL import Image, ImageTk

pwd = os.path.dirname(__file__)
img_dir = os.path.join(pwd, 'img')
empty_img_path = os.path.join(img_dir, "Empty.png")
filled_img_path = os.path.join(img_dir, "Filled.png")
empty_image = Image.open(empty_img_path)
filled_image = Image.open(filled_img_path)

class Conway:
    def __init__(self, num_rows:int, num_cols:int, cells:list, root:tk.Tk):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_data = cells
        self.labels = list()
        # Re-title the window
        root.title("Culbreth Final: Conway's Game of Life")
        # these TK images need to be initialized after TK has been started, hence in the init.
        self.empty_img = ImageTk.PhotoImage(empty_image)
        self.filled_img = ImageTk.PhotoImage(filled_image)
        # Initialize the labels
        for r in range(num_rows):
            row = list()
            for c in range(num_cols):
                cur_image = None
                if self.cell_data[r][c]:
                    cur_image = self.filled_img
                else:
                    cur_image = self.empty_img
                label = tk.Label(root, image=cur_image)
                label.grid(row=r, column=c,sticky=tk.NSEW)
                row.append(label)
            self.labels.append(row)
        tk.Button(root, text="Next Gen", command=self.tick).grid(
            row=self.num_rows, column=0, columnspan=self.num_cols//2, sticky=tk.EW)
        tk.Button(root, text="Exit",command=root.destroy).grid(
            row=self.num_rows,column=self.num_cols//2, columnspan=self.num_cols - self.num_cols//2, sticky=tk.EW)
        root.resizable(width=False, height=False)

    def tick(self):
        self.process_world()
        self.update_labels()

    def process_world(self):
        new_data = list()
        col_range = range(self.num_cols)
        row_range = range(self.num_rows)
        for r in row_range:
            new_row = list()
            for c in col_range:
                cell = self.cell_data[r][c]

                neighbor_count = 0
                for _r, _c in ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)):
                    if (r + _r) in row_range and (c + _c) in col_range:
                        if self.cell_data[r + _r][c + _c]:
                            neighbor_count += 1

                if cell and neighbor_count in (2,3):
                    new_row.append(True)
                elif (not cell) and neighbor_count >= 3:
                    new_row.append(True)
                else:
                    new_row.append(False)
            new_data.append(tuple(new_row))
        self.cell_data = new_data


    def update_labels(self):
        for label_row, cell_row in zip(self.labels, self.cell_data):
            for label, cell in zip(label_row, cell_row):
                if cell:
                    cur_image = self.filled_img
                else:
                    cur_image = self.empty_img
                label.configure(image=cur_image)
