from kivy.tests import GraphicUnitTest

class TestEvents(GraphicUnitTest):
    from kivy_garden.matplotlib.tests.test_app import TestApp
    app = TestApp()

    def test_run_app(self):
        self.app.run()
