from kivy.tests import GraphicUnitTest, UnitTestTouch


class TestEvents(GraphicUnitTest):

    @classmethod
    def setUpClass(cls):
        from matplotlib.figure import Figure
        from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4])
        cls.figure_canvas = FigureCanvasKivyAgg(figure=fig)

    def test_resize_screen(self):
        self.render(self.figure_canvas)

    def test_touch_down(self):
        self.render(self.figure_canvas)
        UnitTestTouch(x=0.5, y=0.5).touch_down()

    def test_touch_down_scrolldown(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(x=0, y=0)
        touch.profile = 'button'
        touch.button = 'scrolldown'
        touch.touch_down()

    def test_touch_down_scrolluo(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(x=0, y=0)
        touch.profile = 'button'
        touch.button = 'scrollup'
        touch.touch_down()

    def test_touch_up(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(x=0.5, y=0.5)
        touch.touch_down()
        touch.touch_up()

    def test_touch_up_scrolldown(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(x=0, y=0)
        touch.profile = 'button'
        touch.button = 'scrolldown'
        touch.touch_down()
        touch.touch_up()

    def test_touch_up_scrolluo(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(x=0, y=0)
        touch.profile = 'button'
        touch.button = 'scrollup'
        touch.touch_down()
        touch.touch_up()

    def test_touch_move(self):
        self.render(self.figure_canvas)
        UnitTestTouch(x=0.5, y=0.5).touch_move(x=0.5, y=0.5)

    def test_on_key_down(self):
        from kivy.base import EventLoop
        from kivy.core.window import Keyboard

        EventLoop.ensure_window()
        window = EventLoop.window
        key = 'tab'
        key_code = (key, Keyboard.keycodes[key])
        print(Keyboard.keycodes)

        self.figure_canvas.keyboard_on_key_down(
            window, key_code, text='tab', modifiers=[])

    def test_on_key_up(self):
        from kivy.base import EventLoop
        from kivy.core.window import Keyboard

        EventLoop.ensure_window()
        window = EventLoop.window
        key = 'tab'
        key_code = (key, Keyboard.keycodes[key])
        print(Keyboard.keycodes)
        self.figure_canvas.keyboard_on_key_up(
            window, key_code)
