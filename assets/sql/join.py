import matplotlib.pyplot as plt
import numpy as np
np.random.seed(43)
import draw

fig, ax = plt.subplots(1,1)
ax.axis('equal')
plt.axis([-0.05, 1.55, 0, 1])
ax.axis('off')
N=3
draw.draw_column(ax,0)
draw.draw_column(ax,0.25)
Y0 = list(np.random.rand(N))
Y1 = list(np.random.rand(N))
points_0 = [draw.Point(x=0, y=y) for y in Y0]
points_1 = [draw.Point(x=0.25, y=y) for y in Y1]
lines_0 = [draw.LineSegment(p0,p1) for (p0,p1) in zip(points_0,points_1)]
for line in lines_0:
    draw.draw_line_segment(ax, line)

text_var = plt.text(0.375,0.5, "INNER JOIN", horizontalalignment="center" )

M=2
draw.draw_column(ax,0.5)
draw.draw_column(ax,0.75)
Y2 = list(np.random.rand(M))

for ya,yb in zip(Y1, Y2):
    a,b = draw.Point(x=0.5,y=ya), draw.Point(x=0.75,y=yb)
    draw.draw_line_segment(ax, draw.LineSegment(a,b))

plt.text(0.875,0.5, "=", horizontalalignment="center")
draw.draw_column(ax,1.0)
draw.draw_column(ax,1.25)
draw.draw_column(ax,1.5)

for ya,yb,yc in zip(Y0,Y1,Y2):
    a, b, c = draw.Point(x=1.0,y=ya), draw.Point(x=1.25,y=yb), draw.Point(x=1.5,y=yc)
    draw.draw_triangle(ax, draw.Triangle(a,b,c))

plt.savefig("inner_join.pdf")
text_var.set_text("OUTER JOIN")

for ya,yb in zip(Y0[M:], Y1[M:]):
    a, b = draw.Point(x=1.0,y=ya), draw.Point(x=1.25,y=yb)
    draw.draw_line_segment(ax, draw.LineSegment(a,b))

plt.savefig("outer_join.pdf")
