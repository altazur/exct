import tkinter as tk
import tkinter.filedialog as filedialog
from ExifRemover import CleanExif

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def open_image_file(self):
        self.filename = tk.filedialog.askopenfilename(initialdir = '/', title = 'Select image', filetypes=(("JPEG" ,"*.jpg"), ("PNG", "*.png"), ("TIFF", "*.tiff"), ("All files", "*.")))
        self.file_path_var.set(self.filename)

    def clean_exif(self):
        if self.filename is not None:
            self.filename_save = tk.filedialog.askdirectory()
            CleanExif.return_image_without_exif(self.filename, self.filename_save)

    def create_widgets(self):
        # Label widget
        self.app_name = tk.Label(self, text='exct')
        self.app_name.pack(side='top')
       
        # ImageFile path widget
        self.load_file_label = tk.Label(self, text='Imagefile')
        self.load_file_label.pack(side='left')

        # ImageFile entry (shows path)
        self.file_path_var = tk.StringVar()
        self.file_path_var.set("Click 'Open' to select image file")
        self.file_path = tk.Entry(self, textvariable=self.file_path_var, state='disabled')
        self.file_path.pack(side='right')

        # Open button
        self.open_file_button = tk.Button(self, text='Open', command=self.open_image_file)
        self.open_file_button.pack(side='right')
        
        # CleanExif button (opens 'save file' dialog)
        self.clean_exif_save_button = tk.Button(self, text='Clean Exif', command=self.clean_exif)
        self.clean_exif_save_button.pack(side='bottom')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
