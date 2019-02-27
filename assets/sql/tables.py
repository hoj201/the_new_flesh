import matplotlib.pyplot as plt
import numpy as np
np.random.seed(43)
import draw

fig, ax = plt.subplots(1,1)
ax.axis('equal')
plt.axis([0, 1, 0, 1])
ax.axis('off')
ys = np.random.rand(3)
draw.draw_column(ax,0)
points_0 = [draw.Point(x=0, y=y) for y in ys]
for p in points_0:
    draw.draw_dot(ax,p)
plt.savefig("one_column_table.pdf")


draw.draw_column(ax,0.25)
points_1 = [draw.Point(x=0.25, y=y) for y in np.random.rand(3)]
lines = [draw.LineSegment(p0,p1) for (p0,p1) in zip(points_0,points_1)]
for line in lines:
    draw.draw_line_segment(ax, line)

plt.savefig("two_column_table.pdf")

draw.draw_column(ax, 0.5)
points_2 = [draw.Point(x=0.5, y=y) for y in np.random.rand(3)]
triangles = [draw.Triangle(*_) for _ in zip(points_0,points_1, points_2)]
for t in triangles:
    draw.draw_triangle(ax, t)

plt.savefig("three_column_table.pdf")
