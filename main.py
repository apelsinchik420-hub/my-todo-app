from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TodoApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Верхняя панель ввода
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.task_input = TextInput(hint_text='Что нужно сделать?', multiline=False)
        add_btn = Button(text='+', size_hint_x=None, width=50, background_color=(0, 0.7, 0, 1))
        add_btn.bind(on_press=self.add_task)
        
        input_layout.add(self.task_input)
        input_layout.add(add_btn)
        self.main_layout.add(input_layout)
        
        # Скроллируемый список задач
        scroll = ScrollView()
        self.task_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        
        scroll.add_self(self.task_list) if hasattr(scroll, 'add_self') else scroll.add_widget(self.task_list)
        self.main_layout.add(scroll)
        
        return self.main_layout

    def add_task(self, instance):
        text = self.task_input.text.strip()
        if text:
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)
            cb = CheckBox(size_hint_x=None, width=40)
            lbl = Label(text=text, halign='left', valign='middle')
            lbl.bind(size=lbl.setter('text_size'))
            
            # Зачеркивание при клике на чекбокс
            cb.bind(active=lambda checkbox, value: setattr(lbl, 'color', (0.5, 0.5, 0.5, 1) if value else (1, 1, 1, 1)))
            
            del_btn = Button(text='X', size_hint_x=None, width=40, background_color=(0.7, 0, 0, 1))
            del_btn.bind(on_press=lambda btn: self.task_list.remove_widget(row))
            
            row.add_widget(cb)
            row.add_widget(lbl)
            row.add_widget(del_btn)
            self.task_list.add_widget(row)
            self.task_input.text = ''

if __name__ == '__main__':
    TodoApp().run()
