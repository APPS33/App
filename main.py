from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

class ToDoApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # خلفية التطبيق
        with self.root.canvas.before:
            Color(0.95, 0.95, 0.95, 1) # لون رمادي فاتح جداً
            self.rect = Rectangle(size=(2000, 2000), pos=self.root.pos)

        # العنوان
        self.root.add_widget(Label(text="قائمة مهامي", font_size=30, color=(0.2, 0.6, 1, 1), bold=True))

        # منطقة الإدخال
        input_area = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.task_input = TextInput(hint_text="اكتب مهمة جديدة...", multiline=False, halign='right')
        add_btn = Button(text="إضافة", background_color=(0.2, 0.8, 0.2, 1), size_hint_x=0.3)
        add_btn.bind(on_press=self.add_task)
        
        input_area.add_widget(add_btn)
        input_area.add_widget(self.task_input)
        self.root.add_widget(input_area)

        # قائمة المهام (Scrollable)
        self.scroll = ScrollView()
        self.task_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        self.scroll.add_widget(self.task_list)
        self.root.add_widget(self.scroll)

        return self.root

    def add_task(self, instance):
        if self.task_input.text:
            task_box = BoxLayout(size_hint_y=None, height=50, spacing=5)
            lbl = Label(text=self.task_input.text, color=(0, 0, 0, 1), halign='right')
            del_btn = Button(text="X", size_hint_x=0.2, background_color=(1, 0.3, 0.3, 1))
            
            del_btn.bind(on_press=lambda btn: self.task_list.remove_widget(task_box))
            
            task_box.add_widget(del_btn)
            task_box.add_widget(lbl)
            self.task_list.add_widget(task_box)
            self.task_input.text = ""

if __name__ == '__main__':
    ToDoApp().run()
