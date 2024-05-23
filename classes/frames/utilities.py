# /classes/frames/utilities.py

import customtkinter as CTk
import sys
import subprocess


def switch_to_light_mode(is_light_mode):
    from classes.frames.left_frame import LeftFrame

    CTk.set_appearance_mode("light" if is_light_mode else "dark")
    bg_color = "#dbdbdb" if is_light_mode else "#2b2b2b"
    LeftFrame.instance.canvas_frame.config(bg=bg_color)


def restart_program():
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()


def update_shopping_cart(
    scrollable_shoppingcart, item, images, enable_dropdown_callback=None
):
    item_frame = CTk.CTkFrame(master=scrollable_shoppingcart)
    item_frame.pack(fill="x", pady=5)

    formatted_price = "{:.2f}€".format(item["Preis"])
    item_label = CTk.CTkLabel(
        master=item_frame, text=f"{item['Name']} - {formatted_price}"
    )
    item_label.pack(side="left")

    remove_button = CTk.CTkButton(
        master=item_frame,
        image=images["remove_button"],
        width=20,
        height=20,
        text=None,
        command=lambda: [
            item_frame.destroy(),
            enable_dropdown_callback("normal") if enable_dropdown_callback else None,
        ],
    )

    remove_button.pack(side="right")
