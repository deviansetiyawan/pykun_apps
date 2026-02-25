"""
Password generator application
"""

import toga
import hashlib
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class pykun_apps(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

        self.input_string = toga.TextInput(
            placeholder="Input your SALT...",
            style=Pack(width=250, padding=10)
        )

        instruction_label = toga.Label(
            "Input your SALT:",
            style=Pack(padding=(5, 0))
        )

        generate_btn = toga.Button(
            "Generate Password",
            on_press=self.generate_password,
            style=Pack(padding=10)
        )

        self.output_pass = toga.TextInput(
            readonly=True,
            placeholder="Hasil password di sini",
            style=Pack(width=250, padding=10)
        )

        main_box.add(instruction_label)
        main_box.add(self.input_string)
        main_box.add(generate_btn)
        main_box.add(self.output_pass)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        def generate_password(self, widget):
            raw_text = self.input_string.value
            
            if not raw_text:
                self.output_pass.value = "Input tidak boleh kosong!"
                return

            hash_object = hashlib.sha256(raw_text.encode())
            hex_dig = hash_object.hexdigest()
            
            final_password = hex_dig[:12].capitalize() + "!"
            
            self.output_pass.value = final_password

def main():
    return pykun_apps()
