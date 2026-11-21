from graphics.rectangle import area as r_area
from graphics.rectangle import perimeter as r_perimeter

from graphics.circle import area as c_area
from graphics.circle import perimeter as c_perimeter

from g_3d.cuboid import area as cb_area
from g_3d.cuboid import perimeter as cb_perimeter


from g_3d.sphere import area as s_area
from g_3d.sphere import perimeter as s_perimeter

#rectangle
print("rectangle")
print("area:", r_area(10,5))
print("perimeter:", r_perimeter(10,5))

#circle
print("\ncircle")
print("area:",c_area(7))
print("perimeter:",c_perimeter(7))

#cuboid
print("\ncuboid")
print("surface area:",cb_area(5,4,3))
print("perimeter:",cb_perimeter(5,4,3))

#sphere
print("\nsphere")
print("surface area:",s_area(7))
print("great circle circumference:",s_perimeter(7))