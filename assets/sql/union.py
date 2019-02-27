import matplotlib.pyplot as plt
import numpy as np
np.random.seed(43)
import draw

fig, ax = plt.subplots(1,1)
ax.axis('equal')
plt.axis([0, 1.25, 0, 1])
ax.axis('off')
N=3
draw.draw_column(ax,0)
draw.draw_column(ax,0.25)
y0 = list(np.random.rand(N))
y1 = list(np.random.rand(N))
points_0 = [draw.Point(x=0, y=y) for y in y0]
points_1 = [draw.Point(x=0.25, y=y) for y in y1]
lines_0 = [draw.LineSegment(p0,p1) for (p0,p1) in zip(points_0,points_1)]
for line in lines_0:
    draw.draw_line_segment(ax, line)

plt.text(0.375,0.5, "UNION", horizontalalignment="center" )

M=2
draw.draw_column(ax,0.5)
draw.draw_column(ax,0.75)
y2 = list(np.random.rand(M))
y3 = list(np.random.rand(M))
points_2 = [draw.Point(x=0.5, y=y) for y in y2]
points_3 = [draw.Point(x=0.75, y=y) for y in y3]
for a,b in zip(points_2, points_3):
    draw.draw_line_segment(ax, draw.LineSegment(a,b))

plt.text(0.875,0.5, "=", horizontalalignment="center")
draw.draw_column(ax,1.0)
draw.draw_column(ax,1.25)
for ya,yb in zip(y0+y2, y1+y3):
    a, b = draw.Point(x=1.0,y=ya), draw.Point(x=1.25,y=yb)
    draw.draw_line_segment(ax, draw.LineSegment(a,b))

plt.savefig("union.pdf")
