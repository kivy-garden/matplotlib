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
        UnitTestTouch(0.5, 0.5).touch_down()

    def test_touch_down_scrolldown(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(0, 0)
        touch.profile = 'button'
        touch.button = 'scrolldown'
        touch.touch_down()

    def test_touch_down_scrolluo(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(0, 0)
        touch.profile = 'button'
        touch.button = 'scrollup'
        touch.touch_down()

    def test_touch_up(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(0.5, 0.5)
        touch.touch_down()
        touch.touch_up()

    def test_touch_up_scrolldown(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(0, 0)
        touch.profile = 'button'
        touch.button = 'scrolldown'
        touch.touch_down()
        touch.touch_up()

    def test_touch_up_scrolluo(self):
        self.render(self.figure_canvas)
        touch = UnitTestTouch(0, 0)
        touch.profile = 'button'
        touch.button = 'scrollup'
        touch.touch_down()
        touch.touch_up()

    def test_touch_move(self):
        self.render(self.figure_canvas)
        UnitTestTouch(0.5, 0.5).touch_move(0.5, 0.5)
