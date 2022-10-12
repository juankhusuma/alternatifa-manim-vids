from manim import *


class Tangent(Scene):
    def construct(self):
        x_range = [0, 10, 1]
        y_range = [0, 10, 1]
        x_length = 5
        y_length = 5

        ax = Axes(
            x_range,
            y_range,
            x_length,
            y_length,
            axis_config={
                "include_tip": False,
            }
        )
        title = Text("Definisi Turunan")
        title.move_to(UP*3)
        pln = NumberPlane(x_range, y_range, x_length, y_length)

        def f(x):
            return (x**2)/10

        x = ValueTracker(5)
        dx = ValueTracker(2)

        f_graph = ax.plot(lambda x: f(x), color=RED)
        point = always_redraw(lambda: Dot().set_color(GREEN).move_to(
            ax.c2p(x.get_value(), f_graph.underlying_function(x.get_value())))
        )
        point2 = always_redraw(lambda: Dot().set_color(GREEN).move_to(
            ax.c2p(x.get_value() + dx.get_value(), f_graph.underlying_function(x.get_value() + dx.get_value())))
        )
        secant = always_redraw(lambda: ax.get_secant_slope_group(
            x=x.get_value(),
            graph=f_graph,
            dx=dx.get_value(),
            dx_line_color=ORANGE,
            dx_label="x + h",
            dy_label="f(x+h)",
            dy_line_color=YELLOW,
            secant_line_color=GREEN,
            secant_line_length=5
        ))
        tanl_group = VGroup(point, point2, secant)
        self.play(Write(title))
        self.play(DrawBorderThenFill(pln), DrawBorderThenFill(ax))
        self.play(Create(f_graph))
        self.wait()
        self.play(Create(tanl_group))
        self.play(dx.animate.set_value(0.001), run_time=5)
        self.play(x.animate.set_value(0), run_time=5)
        self.play(x.animate.set_value(10), run_time=5)
        self.wait(2)
