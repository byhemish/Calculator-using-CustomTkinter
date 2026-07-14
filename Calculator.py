import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("360x520")
        self.resizable(False, False)

        self.expression = ""

        self.display = ctk.CTkEntry(
            self,
            width=320,
            height=60,
            font=("Arial", 28),
            justify="right"
        )
        self.display.pack(pady=20)

        self.display.insert(0, "0")

        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)

        buttons = [
            ["C", "(", ")", "CE"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for row_index, row in enumerate(buttons):
            for col_index, text in enumerate(row):
                button = ctk.CTkButton(
                    frame,
                    text=text,
                    width=70,
                    height=60,
                    font=("Arial", 20),
                    command=lambda value=text: self.button_click(value)
                )
                button.grid(row=row_index, column=col_index, padx=5, pady=5)

    def button_click(self, value):
        if value == "C":
            self.expression = ""
            self.update_display("0")

        elif value == "CE":
            self.expression = self.expression[:-1]
            self.update_display(self.expression if self.expression else "0")

        elif value == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.update_display(result)
            except Exception:
                self.expression = ""
                self.update_display("Error")

        else:
            if self.display.get() in ("0", "Error"):
                self.expression = value
            else:
                self.expression += value

            self.update_display(self.expression)

    def update_display(self, text):
        self.display.delete(0, "end")
        self.display.insert(0, text)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()