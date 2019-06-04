from typing import List

from matplotlib import pyplot as plt
from shapely.geometry import Point


def plot_punkt(punkt: Point):
    """
    Plot et enkelt punkt på en graf
    """
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.scatter(punkt.x, punkt.y)
    ax.set_title('Punkt')


def plot_punkter(punkter: List[Point]):
    """
    Plot flere punkter på samme plot
    """
    x = [punkt.x for punkt in punkter]
    y = [punkt.y for punkt in punkter]
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    ax.set_title('Punkter')
