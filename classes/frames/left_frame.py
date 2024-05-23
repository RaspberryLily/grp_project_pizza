# /classes/frames/left_frame.py

import customtkinter as CTk
import tkinter as tk
from PIL import Image, ImageTk
from classes.frames.utilities import switch_to_light_mode


class LeftFrame:
    def __init__(self, master, images):
        LeftFrame.instance = self
        self.master = master
        self.images = images
        self.setup_frame()

    def setup_frame(self):
        self.outer_frame = CTk.CTkFrame(
            master=self.master, border_color="grey", border_width=2, corner_radius=12
        )
        self.outer_frame.grid(row=0, column=0, sticky="nsew")
        self.outer_frame.grid_rowconfigure(1, weight=1)
        self.outer_frame.grid_columnconfigure(0, weight=1)

        self.logo_frame = CTk.CTkFrame(
            master=self.outer_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        self.logo_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.logo = CTk.CTkFrame(master=self.logo_frame)
        self.logo.grid(row=0, column=0, padx=10, pady=10)

        self.logo_frame_label = CTk.CTkLabel(
            master=self.logo, image=self.images["logo_image"], text=None
        )
        self.logo_frame_label.grid()

        self.setup_light_switch_frame()
        self.setup_scrolling_banner_frame()

    def setup_light_switch_frame(self):
        self.outer_switch_frame = CTk.CTkFrame(
            master=self.outer_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        self.outer_switch_frame.grid(row=2, column=0, padx=10, pady=10, sticky="sew")

        self.switch_frame = CTk.CTkFrame(
            master=self.outer_switch_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        self.switch_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.light_mode_switch_frame = CTk.CTkFrame(
            master=self.switch_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        self.light_mode_switch_frame.grid(
            row=1, column=0, padx=35, pady=10, sticky="ew"
        )

        self.light_mode_switch = CTk.CTkSwitch(
            master=self.light_mode_switch_frame,
            fg_color="#0a5c5c",
            progress_color="#7cbfb1",
            text="Light Mode",
            border_width=2,
            border_color="grey",
            corner_radius=12,
            command=lambda: switch_to_light_mode(self.light_mode_switch.get()),
        )
        self.light_mode_switch.grid()

    def setup_scrolling_banner_frame(self):
        current_mode = CTk.get_appearance_mode()
        bg_color = "#dbdbdb" if current_mode == "light" else "#2b2b2b"
        self.canvas_frame = tk.Canvas(self.outer_frame, width=200, bg=bg_color)
        self.canvas_frame.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")

        self.banner_image = Image.open("data/pictures/banner.png")
        self.banner_photo = ImageTk.PhotoImage(self.banner_image)
        self.banner = self.canvas_frame.create_image(
            0, 0, anchor="nw", image=self.banner_photo
        )

        def scroll_banner():
            self.canvas_frame.move(self.banner, 0, 1)
            x, y = self.canvas_frame.coords(self.banner)

            if y >= self.canvas_frame.winfo_height():
                self.canvas_frame.coords(self.banner, x, -self.banner_image.height)

            self.master.after(10, scroll_banner)

        scroll_banner()
