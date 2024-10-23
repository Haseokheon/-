import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class PDFViewer(tk.Toplevel):
    def __init__(self, pdf_path):
        super().__init__()
        self.title("PDF Viewer with Coordinates")
        
        self.pdf_document = fitz.open(pdf_path)
        self.current_page_num = 0
        
        self.canvas = tk.Canvas(self, cursor="cross")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.canvas.bind("<Motion>", self.show_coordinates)
        
        self.coord_label = tk.Label(self, text="Coordinates: (x, y)")
        self.coord_label.pack()
        
        self.load_page(self.current_page_num)
        
    def load_page(self, page_num):
        page = self.pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        mode = "RGB" if pix.n < 4 else "RGBA"
        image = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        self.img = ImageTk.PhotoImage(image)
        
        self.canvas.config(width=pix.width, height=pix.height)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        
    def show_coordinates(self, event):
        x, y = event.x, event.y
        self.coord_label.config(text=f"Coordinates: ({x}, {y})")

def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        viewer = PDFViewer(file_path)
        viewer.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    open_pdf()
