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

    def test_screen(self):
        self.render(self.figure_canvas)

