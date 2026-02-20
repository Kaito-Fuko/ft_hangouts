import tkinter as tk
from database import get_contact

# contact button
class HomeFrame(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		self.refresh()

	def refresh(self):
		contact = get_contact()

		for c in contact:
			tk.Button(self, text=c[1], height=2).pack(fill="X")