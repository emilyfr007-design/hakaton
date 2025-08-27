# from kivy.config import Config
#
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '600')
#
# from kivy.app import App
# from kivy.uix.screenmanager import Screen, ScreenManager
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.floatlayout import FloatLayout
# from kivy.graphics import Color, Rectangle
# from forex_python.converter import CurrencyRates
#
# # Convert RGB to Kivy's RGBA format (divide by 255)
# forest_green = (255 / 255, 200 / 255, 255 / 255, 1)
# light_brown = (255 / 255, 70 / 255, 255 / 255, 1)
# off_pink = (255 / 255, 160 / 255, 255 / 255, 1)
# off_white = (255 / 255, 135 / 255, 255 / 255, 1)
#
#
# class Welcome(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.add_widget(FloatLayout())
#         with self.canvas.before:
#             Color(*forest_green)
#             self.rect = Rectangle(size=self.size, pos=self.pos)
#             self.bind(size=self._update_rect, pos=self._update_rect)
#
#         title = Label(text="welcome to Pinktect", font_size='24sp', color=light_brown)
#         intro_txt = Label(text="Are you ready to Convert?", color=light_brown)
#         self.btn_next = Button(text="ENTER", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5},
#                                background_color=light_brown)
#         self.btn_next.bind(on_release=self.next)
#
#         master = BoxLayout(orientation="vertical", padding=25, spacing=20)
#         master.add_widget(title)
#         master.add_widget(intro_txt)
#         master.add_widget(self.btn_next)
#         self.add_widget(master)
#
#     def _update_rect(self, instance, value):
#         self.rect.pos = instance.pos
#         self.rect.size = instance.size
#
#     def next(self, *args):
#         self.manager.current = "convert_screen"
#
#
# class ConvertScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.add_widget(FloatLayout())
#         with self.canvas.before:
#             Color(*forest_green)
#             self.rect = Rectangle(size=self.size, pos=self.pos)
#             self.bind(size=self._update_rect, pos=self._update_rect)
#
#         text = Label(text="Converter App", color=light_brown, font_name="Arial", font_size=30, bold=True)
#         amt_text = Label(text="Enter name:", halign="left", color=light_brown, bold=True)
#         from_txt = Label(text="Enter Password:", halign="left", color=light_brown, bold=True)
#         to_txt = Label(text="To Currency:", halign="left", color=light_brown, bold=True)
#         self.amount = TextInput(hint_text="100", background_color=off_pink, hint_text_color=forest_green)
#         self.from_currency = TextInput(hint_text="USD", background_color=off_pink, hint_text_color=forest_green)
#         self.to_currency = TextInput(hint_text="EUR", background_color=off_pink, hint_text_color=forest_green)
#         self.convert_btn = Button(text="Convert Now", size_hint=(0.5, None), pos_hint={'center_x': 0.5},
#                                   background_color=off_pink, bold=True)
#
#         final_amt = Label(text="Converted Amount:", valign='middle', color=light_brown)
#         self.results = Label(text="", valign='middle', color=light_brown, font_size=20)
#
#         self.convert_btn.bind(on_release=self.next)
#
#         row1 = BoxLayout(size_hint=(0.8, None), height='30sp')
#         row2 = BoxLayout(size_hint=(0.8, None), height='30sp')
#         row3 = BoxLayout(size_hint=(0.8, None), height='30sp')
#         row4 = BoxLayout(size_hint=(0.8, None), height='30sp')
#         row5 = BoxLayout(size_hint=(0.8, None), height='30sp')
#
#         row1.add_widget(amt_text)
#         row1.add_widget(self.amount)
#         row2.add_widget(from_txt)
#         row2.add_widget(self.from_currency)
#         row3.add_widget(to_txt)
#         row3.add_widget(self.to_currency)
#         row4.add_widget(final_amt)
#         row5.add_widget(self.results)
#
#         master = BoxLayout(orientation="vertical", padding=25, spacing=20)
#         master.add_widget(text)
#         master.add_widget(row1)
#         master.add_widget(row2)
#         master.add_widget(row3)
#         master.add_widget(row4)
#         master.add_widget(row5)
#
#         master.add_widget(self.convert_btn)
#         self.add_widget(master)
#
#     def _update_rect(self, instance, value):
#         self.rect.pos = instance.pos
#         self.rect.size = instance.size
#
#     def next(self, _):
#         self.convert_now()
#
#     def convert_now(self):
#         self.results.text = ""
#
#         try:
#             amt = float(self.amount.text)
#         except ValueError:
#             self.results.text = "Error: Enter a valid numeric amount"
#             return
#
#         from_cur = self.from_currency.text.upper()
#         to_cur = self.to_currency.text.upper()
#
#         c = CurrencyRates()
#         try:
#             rates = c.get_rate(from_cur, to_cur)
#             convert_amt = amt * rates
#             text = f"{amt} {from_cur} is equal to {round(convert_amt, 2)} {to_cur}"
#         except Exception as e:
#             text = f"Error: {e}"
#
#         self.results.text = text
#
#
# class Home(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(Welcome(name="welcome_screen"))
#         sm.add_widget(ConvertScreen(name="convert_screen"))
#         return sm
#
#
# if __name__ == "__main__":
#     app = Home()
#     app.run()