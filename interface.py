from tkinter import *

class Interface:

    width = 200
    height = 200

    def __init__(self, toplevel):
        self.main_frame(toplevel)

    def main_frame(self, toplevel):
        root_frame = Frame(toplevel,
                           width=4*self.width,
                           height=4*self.height,
                           bg="Red")
        root_frame.grid(row=0, column=0)

def main():
    root = Tk()
    root.maxsize(800, 800)
    Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
