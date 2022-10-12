from manim import *


class Limit(Scene):
    @staticmethod
    def f(x):
        return (x**3)/100

    def construct(self):
        x_range = [-10, 10, 1]
        y_range = [-10, 10, 1]
        x_length = 5
        y_length = 5

        nl = NumberPlane(x_range, y_range, x_length, y_length)
        ax = Axes(x_range, y_range, x_length, y_length,
                  axis_config={"include_tip": False})

        plt = ax.plot(lambda x: self.f(x), color=RED)

        title = Text("Limit").scale(0.5).move_to(UP*3)

        x = ValueTracker(4)

        plane = VGroup(nl, ax)
        graph = VGroup(plane, plt)

        dot = always_redraw(lambda: Dot().set_color(YELLOW).scale(
            0.5).move_to(ax.c2p(x.get_value(), self.f(x.get_value()))))

        self.play(
            Write(title)
        )
        self.play(
            DrawBorderThenFill(plane),
            Create(plt)
        )
        self.play(graph.animate.move_to(LEFT*4))
        self.play(Create(dot))
        self.play(x.animate.set_value(3), run_time=3)
        self.wait(2)


class UndefinedLimit(Scene):
    @staticmethod
    def f(x):
        return 5/x

    def construct(self):
        x_range = [-10, 10, 1]
        y_range = [-10, 10, 1]
        x_length = 5
        y_length = 5

        ax = Axes(
            x_range,
            y_range,
            x_length,
            y_length,
            axis_config={
                "include_tip": False
            }
        )

        plt1 = ax.plot(lambda x: self.f(
            x), x_range=[-10, -0.1], color=RED)
        plt2 = ax.plot(lambda x: self.f(x), x_range=[0.1, 10], color=BLUE)
        plt = VGroup(plt1, plt2)

        x = ValueTracker(4)
        point = always_redraw(lambda: Dot().set_color(GREEN).move_to(
            ax.c2p(x.get_value(), plt2.underlying_function(x.get_value()))))

        self.play(
            DrawBorderThenFill(ax)
        )
        self.play(
            Create(plt)
        )
        self.play(
            Create(point)
        )
        self.play(
            x.animate.set_value(0.4),
            run_time=3
        )
        self.wait(2)
