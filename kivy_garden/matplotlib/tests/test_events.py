from kivy.tests import GraphicUnitTest

class TestEvents(GraphicUnitTest):
    from kivy_garden.matplotlib.tests.test_app import AppTest
    app = AppTest()

    def test_run_app(self):
        self.app.run()
