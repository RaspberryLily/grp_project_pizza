# /classes/frames/middle_frame.py

import customtkinter as CTk
from classes.static.pizza import Pizza
from classes.frames.utilities import update_shopping_cart


class MiddleFrame:
    def __init__(self, master, images, right_frame):
        self.master = master
        self.images = images
        self.right_frame = right_frame
        self.setup_frame()
        self.show_welcome_message()

    def setup_frame(self):
        self.middle_frame = CTk.CTkFrame(
            master=self.master, border_color="grey", border_width=2, corner_radius=12
        )
        self.middle_frame.grid(row=0, column=1, sticky="nsew")

        self.setup_scrollable_order_frame()

        self.setup_category_frame("Pizza", 0, self.images["pizza_icon"])
        self.setup_category_frame("Pasta", 1, self.images["pasta_icon"])
        self.setup_category_frame("Dessert", 2, self.images["dessert_icon"])
        self.setup_category_frame("Drinks", 3, self.images["drink_icon"])

    def setup_category_frame(self, category_name, column, icon):
        category_frame = CTk.CTkFrame(
            master=self.middle_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        category_frame.grid(row=0, column=column, padx=10, pady=10, sticky="n")

        icon_frame = CTk.CTkFrame(master=category_frame)
        icon_frame.pack(pady=(10, 10), padx=(10, 10), anchor="center")

        category_label = CTk.CTkLabel(
            master=icon_frame, image=icon, text=None, cursor="hand2"
        )
        category_label.pack()

        if category_name == "Pizza":
            pizza = Pizza(
                self.master,
                self.scrollable_order,
                lambda item, callback=None: update_shopping_cart(
                    self.right_frame.scrollable_shoppingcart,
                    item,
                    self.master.images,
                    callback,
                ),
            )
            category_label.bind(
                "<Button-1>",
                lambda _, cname=category_name: (
                    self.right_frame.set_category_label(cname),
                    pizza.options() if not pizza.item_added else None,
                ),
            )

    def setup_scrollable_order_frame(self):
        scrollable_order_frame = CTk.CTkFrame(
            master=self.middle_frame,
            border_color="grey",
            border_width=2,
            corner_radius=12,
        )
        scrollable_order_frame.grid(
            row=1, column=0, columnspan=4, padx=10, pady=(10, 10), sticky="nsew"
        )

        self.scrollable_order = CTk.CTkScrollableFrame(
            master=scrollable_order_frame,
            width=545,
            height=650,
            scrollbar_button_color="#7cbfb1",
            scrollbar_button_hover_color="#b3e6db",
        )
        self.scrollable_order.pack(expand=True, fill="both", padx=10, pady=10)

    def show_welcome_message(self):
        self.welcome_label = CTk.CTkLabel(
            master=self.scrollable_order,
            text="Willkommen im Restaurant FIAE 'Papa Python'! Bitte wählen Sie eine Kategorie aus.",
            wraplength=500,
        )
        self.welcome_label.pack(pady=20)
