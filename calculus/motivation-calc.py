from manim import *
from manim_physics import *


class FallingSnapshot(SpaceScene):
    def construct(self):
        circle = Circle(radius=0.25).shift(UP)
        circle.set_fill(RED, 0.5)
        # circle.shift(DOWN + RIGHT)

        # rect = Square().shift(UP)
        # rect.rotate(PI / 4)
        # rect.set_fill(YELLOW_A, 1)
        # rect.shift(UP * 2)
        # rect.scale(0.5)

        pln = NumberPlane(x_range=[0, 30, 1], y_range=[
                          0, 30, 1], y_length=10, x_length=10).move_to(UL*3)

        ground = Line([-4, -3.5, 0], [4, -3.5, 0])
        wall1 = Line([-4, -3.5, 0], [-4, 3.5, 0])
        wall2 = Line([4, -3.5, 0], [4, 3.5, 0])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(pln)
        )
        self.make_rigid_body(circle)  # Mobjects will move with gravity
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(5)
