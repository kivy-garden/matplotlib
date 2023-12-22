from kivy.app import App
#import matplotlib
#matplotlib.use("module://kivy_garden.matplotlib.backend_kivy")
from matplotlib.figure import Figure
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


class TestApp(App):
    def build(self):
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4])
        return FigureCanvasKivyAgg(figure=fig)



# def test_run_app():
#     TestApp().run()