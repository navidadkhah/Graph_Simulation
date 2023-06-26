import tkinter as tk
from tkinter import ttk
import webview
# import required library
import webbrowser
from tkinter import *

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulation Project")

        self.main_page()

    def main_page(self):
        # Clear previous page
        self.clear_page()

        # Create buttons for navigation
        buttons = []
        for i in range(1, 10):
            button = ttk.Button(
                self.root,
                text=f"Page {i}",
                command=lambda i=i: self.navigate_to_page(i),
                width=10,
                style="Custom.TButton"
            )
            buttons.append(button)
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=10, pady=10)

        self.current_page_buttons = buttons

    def clear_page(self):
        # Clear the current buttons
        if hasattr(self, "current_page_buttons"):
            for button in self.current_page_buttons:
                button.destroy()

        # Clear the current frame
        if hasattr(self, "current_page_frame"):
            self.current_page_frame.destroy()

    def navigate_to_page(self, page_num):
        # Clear previous page
        self.clear_page()

        if page_num == 1:
            self.page_1()
        elif page_num == 2:
            self.page_2()
        elif page_num == 3:
            self.page_3()
        elif page_num == 4:
            self.page_4()
        elif page_num == 5:
            self.page_5()
        elif page_num == 6:
            self.page_6()
        elif page_num == 7:
            self.page_7()
        elif page_num == 8:
            self.page_8()
        elif page_num == 9:
            self.page_9()
       
    def page_1(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/15X1j3HtpJk3SR-_huqm8jF7de34aCWg1#scrollTo=IKe4SEKE6o1v")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")

    def page_2(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/1oCoBmj_vIQmTtJ_JnpoC7JtzcaA8mO6R")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")

    def page_3(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/1kuYGFLco2dEexx3CbQFAX4pDynGKeQex#scrollTo=3G5wM8NjH_l8")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")
    
    def page_5(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/1wiEsKoqnPBOmD-uNIbZvd8JKzKr8wPpk")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")

    def page_6(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/1q1MM2-Cs1vHjcRcZWZ02MpU1Rb6ZIoUt")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")
    
    def page_7(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/1KN5Doo4jn8NP9MBtN8JBNEg4d6Rw8Vjo")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")

    def page_8(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/17jEtoa-L-pgJgGXFr26rqZP_m7nFMtSt")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")

    def page_8(self):
      self.clear_page()
      root = Tk()
      # setting GUI title
      root.title("WebBrowsers")
      # setting GUI geometry
      root.geometry("660x660")
      # call webbrowser.open() function.
      webbrowser.open("https://colab.research.google.com/drive/1MFV-gNNyqPQVZH8esQGeqmbzvk2gQOuM")

      frame = tk.Frame(self.root, width=400, height=250, bg="lightblue")
      frame.grid(row=1, column=0, columnspan=3)

      back_button = ttk.Button(frame, text="Back", command=self.main_page, width=12, style="Custom.TButton")
      back_button.place(x=100,y=-200, rely=1.0, anchor=tk.SW, bordermode="outside")


if __name__ == "__main__":
    gui = GUI()
    gui.root.mainloop()