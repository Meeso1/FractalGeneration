import matplotlib.pyplot as plt
import numpy as np


def _plot_curve_on_axes(points: np.ndarray, axes: plt.Axes) -> None:
    """
    Plot a curve on the given axes.
    
    Args:
        points: A 2xn array defining points of the curve (x, y).
        axes: The matplotlib axes to plot on.
    """
    axes.plot(points[0], points[1], 'b-', linewidth=1)
    axes.axis('off')
    axes.axis('equal')


def plot_curve(points: np.ndarray, axes: plt.Axes | None = None, output_path: str | None = None) -> None:
    """
    Plot a curve from coordinate points.
    
    Args:
        points: A 2xn array defining points of the curve (x, y).
        axes: Optional matplotlib axes to plot on. If None, creates a new figure.
        output_path: Optional path to save the plot. If provided, saves instead of showing.
    """
    if axes is None:
        fig = plt.figure(figsize=(8, 8))
        _plot_curve_on_axes(points, fig.gca())
        
        if output_path is not None:
            plt.savefig(output_path, transparent=True)
        else:
            plt.show()
    else:
        _plot_curve_on_axes(points, axes)
