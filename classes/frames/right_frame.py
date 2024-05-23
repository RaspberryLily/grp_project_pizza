# /classes/frames/right_frame.py

import customtkinter as CTk
from CTkSpinbox import CTkSpinbox
from classes.frames.utilities import restart_program


class RightFrame:
    def __init__(self, master, images):
        self.master = master
        self.images = images
        self.category_label = None
        self.setup_frame()

    def setup_frame(self):
        self.order_frame = CTk.CTkFrame(
            master=self.master, border_color="grey", border_width=2, corner_radius=12
        )
        self.order_frame.grid(row=0, column=2, sticky="nsew")

        self.setup_order_icon_frame()
        self.setup_scrollable_shoppingcart_frame()
        self.setup_payment_frame()

    def setup_order_icon_frame(self):
        order_icon_frame = CTk.CTkFrame(
            master=self.order_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
            width=220,
            height=70,
        )
        order_icon_frame.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        order_icon_label = CTk.CTkLabel(
            master=order_icon_frame, image=self.master.images["order_image"], text=None
        )
        order_icon_label.grid(row=0, column=0, sticky="nsew", padx=(80, 0), pady=8)

    def setup_scrollable_shoppingcart_frame(self):
        scrollable_shoppingcart_frame = CTk.CTkFrame(
            master=self.order_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        scrollable_shoppingcart_frame.grid(
            row=1, column=0, padx=10, pady=25, sticky="ew"
        )

        self.scrollable_shoppingcart = CTk.CTkScrollableFrame(
            master=scrollable_shoppingcart_frame,
            width=330,
            height=560,
            scrollbar_button_color="#7cbfb1",
            scrollbar_button_hover_color="#b3e6db",
        )
        self.scrollable_shoppingcart.grid()

    def setup_payment_frame(self):
        payment_frame = CTk.CTkFrame(
            master=self.order_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        payment_frame.grid(row=2, column=0, padx=10, pady=10)

        self.restart_button = CTk.CTkButton(
            master=payment_frame, text="Restart", command=restart_program
        )
        self.restart_button.grid(padx=100, pady=15)

    def set_category_label(self, category_name):
        if self.category_label is None:
            self.category_label = CTk.CTkLabel(
                master=self.scrollable_shoppingcart,
                text=category_name,
                anchor="center",
                font=("Arial", 20),
            )
            self.category_label.grid()

            self.spin_var = CTk.IntVar()
            self.order_amount_spinbox = CTkSpinbox(
                master=self.scrollable_shoppingcart,
                start_value=1,
                min_value=1,
                max_value=10,
                variable=self.spin_var,
                scroll_value=0,
                command=self.update_order_amount,
            )
            self.order_amount_spinbox.grid()
        else:
            self.category_label.configure(text=category_name)

    def update_order_amount(self, count):
        print(f"Order amount: {count}")
