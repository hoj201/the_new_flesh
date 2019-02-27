from matplotlib import patches
from collections import namedtuple
import numpy as np


Point = namedtuple("Point", ["x", "y"])
LineSegment = namedtuple("LineSegment", ["p0", "p1"])
Triangle = namedtuple("Triangle", ["p0", "p1", "p2"])
#Tet = namedtuple("Tet", ["p0", "p1", "p2", "p3"])

def draw_column(ax, x):
    ax.plot([x,x],[0,1], color='black')

def draw_dot(ax, p):
    ax.scatter(p.x,p.y, color='black', alpha=1.0)

def draw_line_segment(ax, line):
    p0, p1 = line.p0, line.p1
    draw_dot(ax, p0)
    draw_dot(ax, p1)
    ax.plot([p0.x,p1.x], [p0.y, p1.y], color='black')


def draw_triangle(ax, triangle):
    p0,p1,p2 = triangle.p0, triangle.p1, triangle.p2
    draw_line_segment(ax, LineSegment(p0,p1))
    draw_line_segment(ax, LineSegment(p1,p2))
    draw_line_segment(ax, LineSegment(p2,p0))
    xy = np.array([
        [p0.x, p0.y],
        [p1.x, p1.y],
        [p2.x, p2.y]
    ])
    patch = patches.Polygon(xy, closed=True, color="black", alpha=0.2)
    ax.add_patch(patch)


def draw_tet(ax, tet):
    pass
