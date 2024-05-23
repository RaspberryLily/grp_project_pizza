import customtkinter as CTk
import json


class Pizza:
    def __init__(self, master, scrollable_order, update_shopping_cart_callback):
        self.master = master
        self.scrollable_order = scrollable_order
        self.update_shopping_cart_callback = update_shopping_cart_callback
        self.enable_dropdown_callback = lambda state: (
            self.dropdown_size.configure(state=state)
        )
        self.item_added = False

    def options(self, _=None):
        for widget in self.scrollable_order.winfo_children():
            widget.destroy()

        with open("data/datenbank.json", "r") as file:
            data = json.load(file)

        # Size selection
        select_size_label = CTk.CTkLabel(
            self.scrollable_order,
            text="Bitte die gewünschte Größe der Pizza auswählen:",
        )
        select_size_label.pack(pady=20)

        pizza_sizes = [pizza for pizza in data["Speisen"]["Pizza"]["Sorte"]]
        pizza_size_var = CTk.StringVar(value="Größe wählen")
        self.dropdown_size = CTk.CTkOptionMenu(
            self.scrollable_order,
            values=[pizza["Name"] for pizza in pizza_sizes],
            variable=pizza_size_var,
        )
        self.dropdown_size.pack()

        self.dropdown_size.configure(
            command=lambda _: (
                self.update_shopping_cart_callback(
                    next(
                        (
                            pizza
                            for pizza in pizza_sizes
                            if pizza["Name"] == self.dropdown_size.get()
                        ),
                        None,
                    ),
                    self.enable_dropdown_callback,
                ),
                self.dropdown_size.configure(state="disabled"),
                setattr(self, "item_added", True),
            )
        )

        # Ingredient selection
        select_ingredients_label = CTk.CTkLabel(
            self.scrollable_order, text="Bitte Zutaten auswählen:"
        )
        select_ingredients_label.pack(pady=(10, 0))

        self.ingredient_vars = {}
        for ingredient in data["Speisen"]["Zutaten"]:
            var = CTk.IntVar()
            checkbox = CTk.CTkCheckBox(
                self.scrollable_order,
                text=ingredient["Name"],
                variable=var,
                onvalue=1,
                offvalue=0,
            )
            checkbox.pack(anchor="w")
            self.ingredient_vars[ingredient["Name"]] = var
