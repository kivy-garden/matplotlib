def test_matplotlib_use_backend():
    import matplotlib
    import matplotlib.pyplot as plt

    plt.close('all')
    matplotlib.use("module://kivy_garden.matplotlib.backend_kivyagg")

    plt.plot([1, 2, 3, 4])
    plt.ylabel("some numbers")

    plt.show(block=False)
