import matplotlib.pyplot as plt
import numpy as np
np.random.seed(4)
import draw

fig, ax = plt.subplots(1,1)
ax.axis('equal')
plt.axis([-0.05, 1.05, 0, 1])
ax.axis('off')
N=2
draw.draw_column(ax,0)
draw.draw_column(ax,0.25)
Y0 = list(np.random.rand(N))
Y1 = list(np.random.rand(N))
points_0 = [draw.Point(x=0, y=y) for y in Y0]
points_1 = [draw.Point(x=0.25, y=y) for y in Y1]
lines_0 = [draw.LineSegment(p0,p1) for (p0,p1) in zip(points_0,points_1)]
for line in lines_0:
    draw.draw_line_segment(ax, line)

text_var = plt.text(0.375,0.5, "CROSS JOIN", horizontalalignment="center" )

M=2
draw.draw_column(ax,0.5)
Y2 = list(np.random.rand(M))

for y in zip(Y2):
    a = draw.Point(x=0.5,y=y)
    draw.draw_dot(ax, a)

plt.text(0.625,0.5, "=", horizontalalignment="center")
draw.draw_column(ax,0.75)
draw.draw_column(ax,0.875)
draw.draw_column(ax,1.0)

for ya,yb in zip(Y0,Y1):
    for yc in Y2:
        a, b, c = draw.Point(x=0.75,y=ya), draw.Point(x=0.875,y=yb), draw.Point(x=1.0,y=yc)
        draw.draw_triangle(ax, draw.Triangle(a,b,c))

plt.savefig("cross_join.pdf")
