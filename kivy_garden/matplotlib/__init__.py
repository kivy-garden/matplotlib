"""
Matplotlib flower
=================


"""

from ._version import __version__
from .backend_kivy import (
    FigureCanvasKivy,
    FigureManagerKivy,
    GraphicsContextKivy,
    MPLKivyApp,
    NavigationToolbar2Kivy,
    RendererKivy,
)
from .backend_kivyagg import FigureCanvasKivyAgg

__all__ = (
    FigureCanvasKivy.__name__,
    FigureManagerKivy.__name__,
    RendererKivy.__name__,
    GraphicsContextKivy.__name__,
    NavigationToolbar2Kivy.__name__,
    MPLKivyApp.__name__,
    FigureCanvasKivyAgg.__name__,
)
