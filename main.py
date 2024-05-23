# /main.py

import customtkinter as CTk
import os
from PIL import Image
from classes.frames.left_frame import LeftFrame
from classes.frames.middle_frame import MiddleFrame
from classes.frames.right_frame import RightFrame


class App(CTk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry(f"{1202}x{807}")
        self.title("Restaurant FIAE 'Papa Python'")
        self.load_images()
        self.minsize(800, 600)
        self.resizable(False, False)

        # Initialize frames
        self.left_frame = LeftFrame(self, self.images)
        self.right_frame = RightFrame(self, self.images)
        self.middle_frame = MiddleFrame(self, self.images, self.right_frame)

        self.left_frame.outer_frame.grid(sticky="nsew")
        self.right_frame.order_frame.grid(sticky="nsew")
        self.middle_frame.middle_frame.grid(sticky="nsew")

    def load_images(self):
        self.images = {
            "logo_image": CTk.CTkImage(
                Image.open("data/pictures/logo.png"), size=(180, 180)
            ),
            "pizza_icon": CTk.CTkImage(
                Image.open("data/pictures/icons/pizza_icon.png"), size=(60, 60)
            ),
            "pasta_icon": CTk.CTkImage(
                Image.open("data/pictures/icons/pasta_icon.png"), size=(60, 60)
            ),
            "dessert_icon": CTk.CTkImage(
                Image.open("data/pictures/icons/dessert_icon.png"), size=(60, 60)
            ),
            "drink_icon": CTk.CTkImage(
                Image.open("data/pictures/icons/beverage_icon.png"), size=(60, 60)
            ),
            "order_image": CTk.CTkImage(
                Image.open("data/pictures/order.png"), size=(200, 70)
            ),
            "remove_button": CTk.CTkImage(
                Image.open("data/pictures/icons/remove_button.png"), size=(20, 20)
            ),
            #'banner_image': Image.open("data/pictures/banner.png")
        }

    def set_root_directory():
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)


if __name__ == "__main__":
    App.set_root_directory()
    app = App()
    app.mainloop()
