from re import S
from manim import *
import numpy as np


class Intro(Scene):
    def construct(self):
        title = Text("Kalkulus").move_to(UP*3)
        desc = MarkupText(
            "Cabang matematika yang mempelajari <b>\"perubahan\"</b>").scale(0.5)
        item1 = Text("Besarnya perubahan pada suatu saat").scale(0.4)
        item1_label = Text("(Turunan)").scale(0.4)
        item2 = Text("Total perubahan pada suatu rentang waktu").scale(0.4)
        item2_label = Text("(Integral)").scale(0.4)

        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(desc))
        self.play(desc.animate.move_to(UP * 2))
        self.wait()
        self.play(Write(item1.move_to(UP)))
        self.wait()
        self.play(Write(item1_label.next_to(item1, RIGHT)))
        self.wait()
        self.play(Write(item2))
        self.wait()
        self.play(Write(item2_label.next_to(item2, RIGHT)))
        self.wait()

        self.wait(1)


class DerivativeIntro(Scene):
    def construct(self):
        title = Text("Turunan").scale(0.7)
        desc = Text("""
Turunan adalah besarnya perubahan yang terjadi pada
suatu fungsi pada titik tertentu, besarnya perubahan
ini dapat dihitung dari kemiringan garis singgung
fungsi pada titik tersebut.
        """).scale(0.4)

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

        pln = NumberPlane(x_range, y_range, x_length, y_length)

        def f(x):
            return (5*x)**0.5

        f_graph = ax.plot(lambda x: f(x), color=RED)
        t_line = ax.plot(lambda x: (x+5)/2, color=YELLOW)
        point = Dot().set_color(RED).move_to(
            ax.c2p(5, f_graph.underlying_function(5)))

        graph_group = VGroup(pln, ax, f_graph, t_line,
                             point).scale(0.7).move_to(DOWN)

        self.play(Write(title.move_to(UP * 3.5)))
        self.wait()
        self.play(FadeIn(desc))
        self.play(desc.animate.move_to(UP * 2))
        self.wait()

        self.play(DrawBorderThenFill(pln), DrawBorderThenFill(ax))
        self.play(Create(f_graph))
        self.play(Create(point))
        self.play(Create(t_line))
        self.wait(2)
        self.play(t_line.animate.rotate(np.deg2rad(20)))
        self.play(t_line.animate.rotate(np.deg2rad(-20)))
        self.play(t_line.animate.rotate(np.deg2rad(-20)))
        self.play(t_line.animate.rotate(np.deg2rad(20)))
        # self.play(graph_group.animate.shift(LEFT*4), Write(desc))
        self.wait(2)


class Slope(Scene):
    def construct(self):
        title = Text("Gradien Garis")
        x_range = [0, 10, 1]
        y_range = [0, 30, 5]
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
        ).add_coordinates()

        func = MathTex(r"f(x) = 3x")

        pln = NumberPlane(x_range, y_range, x_length, y_length)

        def f(x):
            return 3*x

        f_graph = ax.plot(lambda x: f(x), color=RED)

        self.play(Write(title.move_to(UP * 3.5)))
        self.wait()
        self.play(DrawBorderThenFill(pln), DrawBorderThenFill(ax))
        self.play(Create(f_graph))
        self.play(Write(func.scale(0.6).next_to(f_graph)))
        self.wait(2)


class TangentLine(Scene):
    def calc_slope(self, x: float) -> float:
        return 5 / (2 * np.sqrt(5 * x))

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

        title = Text("Garis Singgung")
        title.move_to(UP*3)

        pln = NumberPlane(x_range, y_range, x_length, y_length)

        def f(x):
            return (5*x)**0.5

        f_graph = ax.plot(lambda x: f(x), color=RED)
        t_line = ax.plot(lambda x: (x+5)/2, color=YELLOW)
        point = Dot().set_color(GREEN).move_to(
            ax.c2p(5, f_graph.underlying_function(5)))

        graph_group = VGroup(pln, ax, f_graph, t_line, point)

        self.play(Write(title))
        self.play(DrawBorderThenFill(pln), DrawBorderThenFill(ax))
        self.play(Create(f_graph))
        self.play(Create(point))
        self.play(Create(t_line))
        # self.play(t_line.animate.rotate(20))
        # self.play(graph_group.animate.shift(LEFT*4), Write(desc))
        self.wait(2)


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
        dx = ValueTracker(4)

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
            dx_label=r"\Delta x",
            dy_label="f(x+ \Delta x)",
            dy_line_color=YELLOW,
            secant_line_color=GREEN,
            secant_line_length=5
        ))
        tanl_group = VGroup(point, point2, secant)
        self.play(Write(title))
        self.play(DrawBorderThenFill(pln), DrawBorderThenFill(ax))
        self.play(Create(f_graph))
        self.wait(2)
        self.play(Create(point), Create(point2))
        self.wait()
        self.play(Create(secant), run_time=5)
        self.wait(5)
        self.play(dx.animate.set_value(0.001), run_time=5)
        self.play(x.animate.set_value(0), run_time=5)
        self.play(x.animate.set_value(10), run_time=5)
        self.wait(2)


class Limit(Scene):
    def construct(self):
        title = Text("Limit").scale(0.7).move_to(UP * 3.5)

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
        ).scale(0.7)
        pln = NumberPlane(x_range, y_range, x_length, y_length).scale(0.7)

        def f(x):
            return (x**2)/10

        x = 5
        dx = 4

        f_graph = ax.plot(lambda x: f(x), color=RED)
        point = Dot().set_color(GREEN).move_to(
            ax.c2p(x, f_graph.underlying_function(x)))

        point2 = Dot().set_color(GREEN).move_to(
            ax.c2p(x + dx, f_graph.underlying_function(x + dx)))

        secant = ax.get_secant_slope_group(
            x=x,
            graph=f_graph,
            dx=dx,
            dx_line_color=ORANGE,
            dx_label=r"\Delta x",
            dy_label="f(x+ \Delta x)",
            dy_line_color=YELLOW,
            secant_line_color=GREEN,
            secant_line_length=3
        )

        graph_group = VGroup(ax, pln, f_graph, secant, point, point2)

        slope_eq = MathTex(
            "m", "=", r"\frac{\Delta y}{\Delta x}").scale(0.65)
        slope_eq_expanded = MathTex(
            "m", "=", r"\frac{f(x + \Delta x) - f(x)}{\Delta x}"
        ).scale(0.65)
        slope_eq_expanded_limit = MathTex(
            "m", "=", r"\lim_{\Delta x \to 0}", r"\frac{f(x + \Delta x) - f(x)}{\Delta x}"
        ).scale(0.65)
        dy_dx_lim_form = MathTex(
            r"\frac{dy}{dx}", "=", r"\lim_{\Delta x \to 0}", r"\frac{f(x + \Delta x) - f(x)}{\Delta x}"

        ).scale(0.65)

        self.play(Write(title))
        self.play(DrawBorderThenFill(pln),
                  DrawBorderThenFill(ax), Create(f_graph))
        self.play(Create(point), Create(point2), Create(secant))
        self.play(graph_group.animate.move_to(LEFT * 4))
        self.wait()
        self.play(Write(slope_eq.next_to(graph_group, RIGHT * 2)))
        self.wait()
        self.play(Transform(slope_eq, slope_eq_expanded.next_to(
            graph_group, RIGHT * 2)))
        self.wait()
        self.play(Transform(slope_eq, slope_eq_expanded_limit.next_to(
            graph_group, RIGHT * 2)))
        self.wait()
        self.play(Transform(slope_eq, dy_dx_lim_form.next_to(
            graph_group, RIGHT * 2)))

        self.wait(2)


class LimitExplained(Scene):
    @staticmethod
    def f(x):
        return (x**3)/100

    def construct(self):
        desc = Text("""
Limit merupakan operator matematika yang melihat bagaimana
hasil suatu fungsi ketika inputnya mendekati suatu nilai.
        """).scale(0.5).move_to(UP * 3.5)

        x_range = [-10, 10, 1]
        y_range = [-10, 10, 1]
        x_length = 5
        y_length = 5

        lim_right = MathTex(r"\lim_{x \to 2^{+}} f(x)").scale(0.7)
        lim_left = MathTex(r"\lim_{x \to 2^{-}} f(x)").scale(0.7)

        # nl = NumberPlane(x_range, y_range, x_length, y_length)
        ax = Axes(x_range, y_range, x_length, y_length,
                  axis_config={"include_tip": False})

        plt = ax.plot(lambda x: self.f(x), color=RED)

        x = ValueTracker(10)

        plane = VGroup(ax)
        graph = VGroup(plane, plt)

        dot = always_redraw(lambda: Dot().set_color(YELLOW).scale(
            0.5).move_to(ax.c2p(x.get_value(), self.f(x.get_value()))))

        x_line = always_redraw(lambda: Line(
            start=[ax.c2p(0, 0)], end=[ax.c2p(x.get_value(), 0)], color=GREEN))
        y_line = always_redraw(lambda: Line(start=[ax.c2p(x.get_value(), 0)], end=[
                               ax.c2p(x.get_value(), self.f(x.get_value()))], color=YELLOW))
        x_brace = always_redraw(lambda: Brace(x_line))
        y_brace = always_redraw(lambda: Brace(y_line, direction=RIGHT))
        x_label = always_redraw(lambda: MathTex(
            "x").scale(0.5).next_to(x_brace, DOWN))
        y_label = always_redraw(lambda: MathTex(
            "f(x)").scale(0.5).next_to(x_brace, RIGHT))

        self.play(Write(desc))

        self.play(
            DrawBorderThenFill(plane),
            Create(plt)
        )
        self.play(Create(dot))
        self.play(Create(x_line), Write(x_brace))
        self.play(Create(y_line), Write(y_brace))
        self.play(Create(x_label), Write(y_label))
        self.play(Write(lim_right.next_to(graph, RIGHT*4)))
        self.play(x.animate.set_value(2), run_time=3)
        self.wait(3)
        self.play(Transform(lim_right, lim_left.next_to(graph, RIGHT*4)))
        x.set_value(-10)
        self.play(Write(lim_left.next_to(graph, RIGHT*4)))
        self.play(x.animate.set_value(2), run_time=3)
        self.wait(2)

        self.wait(2)


class UndefinedLimit(Scene):
    def construct(self):
        # title = Text("Limit Tidak Ada").scale(0.7).move_to(3.5 * UP)

        x_range = [-10, 10, 1]
        y_range = [-10, 10, 1]
        x_length = 5
        y_length = 5

        lim_right = MathTex(r"\lim_{x \to 0^{+}} f(x)").scale(0.7)
        lim_left = MathTex(r"\lim_{x \to 0^{-}} f(x)").scale(0.7)

        ax = Axes(x_range, y_range, x_length, y_length,
                  axis_config={"include_tip": False})
        y_label = ax.get_y_axis_label(r"f(x) = \frac{1}{x}").scale(0.4)

        lp = ax.plot(lambda x: 1/x, x_range=[-10, -0.1], color=RED)
        rp = ax.plot(lambda x: 1/x, x_range=[0.1, 10], color=ORANGE)

        plt = VGroup(lp, rp)

        x = ValueTracker(10)
        dot_1 = always_redraw(
            lambda: Dot().move_to(ax.c2p(x.get_value(), rp.underlying_function(x.get_value())))
        )
        dot_2 = always_redraw(
            lambda: Dot().move_to(ax.c2p(x.get_value(), lp.underlying_function(x.get_value())))
        )

        lim_right = MathTex(r"\lim_{x \to 0^{+} }", "f(x)").next_to(
            plt, RIGHT).scale(0.5)
        lim_left = MathTex(r"\lim_{x \to 0^{-} }", "f(x)").next_to(
            plt, RIGHT).scale(0.5)

        # self.play(Write(title))
        self.play(DrawBorderThenFill(ax))
        self.play(Create(plt))
        self.play(Write(y_label))
        self.play(Write(lim_right))
        self.play(Create(dot_1))
        self.play(x.animate.set_value(0.1))
        self.wait(2)
        self.play(Uncreate(dot_1))
        self.wait()
        x.set_value(-10)
        self.wait()
        self.play(Transform(lim_right, lim_left))
        self.play(Create(dot_2))
        self.play(x.animate.set_value(-0.1))
        self.wait(2)
        self.play(Uncreate(dot_2))
        self.play(x.animate())
        self.wait(2)


class UndefinedLimitDerivation(Scene):
    def construct(self):
        f = MathTex(r"f(x)", "=", r"\frac{1}{x}")
        f_lim = MathTex(r"\lim_{x \to 0}", "f(x)", "=",
                        r"\lim_{x \to 0}", r"\frac{1}{x}")
        f_lim_only = MathTex(
            r"\lim_{x \to 0}", r"\frac{1}{x}")
        f_lim_right = MathTex(
            r"\lim_{x \to 0^{+} }", r"\frac{1}{x}")
        f_lim_right_a1 = MathTex(
            r"\frac{1}{0.1}", "=", r"10")
        f_lim_right_a2 = MathTex(
            r"\frac{1}{0.01}", "=", r"100")
        f_lim_right_a3 = MathTex(
            r"\frac{1}{0.001}", "=", r"1000")
        f_lim_right_c = MathTex(
            r"\lim_{x \to 0^{+} }", r"\frac{1}{x}", "=", r"+ \infty")
        f_lim_left = MathTex(
            r"\lim_{x \to 0^{-} }", r"\frac{1}{x}")
        f_lim_left_a1 = MathTex(
            r"\frac{1}{-0.1}", "=", r"-10")
        f_lim_left_a2 = MathTex(
            r"\frac{1}{-0.01}", "=", r"-100")
        f_lim_left_a3 = MathTex(
            r"\frac{1}{-0.001}", "=", r"-1000")
        f_lim_left_c = MathTex(
            r"\lim_{x \to 0^{-} }", r"\frac{1}{x}", "=", r"- \infty")

        conclusion = MathTex(r"\lim_{x \to 0^{+} }f(x)",
                             r"\ne", r"\lim_{x \to 0^{-} }f(x)")

        self.play(Write(f))
        self.wait(2)
        self.play(Transform(f, f_lim))
        self.wait(2)
        self.play(Transform(f, f_lim_only))
        self.wait(2)
        self.play(Transform(f, f_lim_right))
        self.wait()
        self.play(Transform(f, f_lim_right_a1))
        self.wait()
        self.play(Transform(f, f_lim_right_a2))
        self.wait()
        self.play(Transform(f, f_lim_right_a3))
        self.wait()
        self.play(Transform(f, f_lim_right_c))
        self.wait(5)
        self.play(Transform(f, f_lim_left))
        self.wait()
        self.play(Transform(f, f_lim_left_a1))
        self.wait()
        self.play(Transform(f, f_lim_left_a2))
        self.wait()
        self.play(Transform(f, f_lim_left_a3))
        self.wait()
        self.play(Transform(f, f_lim_left_c))
        self.wait(2)
        self.clear()
        self.play(Write(conclusion))
        self.wait(2)

        self.wait(2)


class LimitLawIntro(Scene):
    def construct(self):
        title = Text("Aturan Limit").scale(0.7)
        desc = Text("""
Untuk mempermudah kita dalam mencari nilai limit fungsi,
operator limit memiliki beberapa sifat atau aturan yang
dapat kita gunakan untuk mencari nilai limit.
        """).scale(0.5)

        self.play(Write(title.move_to(UP * 3.5)))
        self.play(Write(desc))
        self.wait(2)


class AdditionLaw(Scene):
    def construct(self):
        desc = Text("Untuk c suatu konstanta").scale(0.5).move_to(UP * 3.5)
        eq = MathTex(r"\lim_{x \to c} \left( f(x)+g(x) \right)").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} \left( f(x)+g(x) \right)").scale(0.6)
        eq2 = MathTex(r"= \lim_{x \to c}f(x) + \lim_{x \to c}g(x)").scale(0.6)
        self.play(Write(desc))
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*2.5))

        self.wait(2)

        eq = MathTex(r"\lim_{x \to c} \left( f(x)-g(x) \right)").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} \left( f(x)-g(x) \right)").scale(0.6)
        eq2 = MathTex(r"= \lim_{x \to c}f(x) - \lim_{x \to c}g(x)").scale(0.6)
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*1.5))

        self.wait(2)

        desc2 = Text("Untuk c, k suatu konstanta").scale(0.5).move_to(UP * 3.5)

        self.play(Transform(desc, desc2))
        eq = MathTex(r"\lim_{x \to c} kf(x)").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} kf(x)").scale(0.6)
        eq2 = MathTex(r"=k \lim_{x \to c} f(x)").scale(0.6)
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*0.5))

        self.wait(2)


class OtherLaw(Scene):
    def construct(self):
        desc = Text("Untuk c, n suatu konstanta").scale(0.5).move_to(UP * 3.5)
        eq = MathTex(r"\lim_{x \to c} \left( f(x)^n \right)").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} \left( f(x)^n \right)").scale(0.6)
        eq2 = MathTex(r"=\left( \lim_{x \to c}f(x) \right)^n").scale(0.6)
        self.play(Write(desc))
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*2.5))

        eq = MathTex(r"\lim_{x \to c} \sqrt[n]{f(x)}").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} \sqrt[n]{f(x)}").scale(0.6)
        eq2 = MathTex(r"=\sqrt[n]{ \lim_{x \to c} f(x) }").scale(0.6)
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*1.5))

        eq = MathTex(r"\lim_{x \to c} f(x)g(x)").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} f(x)g(x)").scale(0.6)
        eq2 = MathTex(r"= \lim_{x \to c} f(x) \lim_{x \to c}g(x)").scale(0.6)
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*0.5))

        eq = MathTex(r"\lim_{x \to c} \frac{f(x)}{g(x)}").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} \frac{f(x)}{g(x)}").scale(0.6)
        eq2 = MathTex(
            r"= \frac{\lim_{x \to c} f(x)}{\lim_{x \to c}g(x)}").scale(0.6)
        self.play(FadeIn(eq.move_to(DOWN*0.5)))
        self.play(eq.animate.move_to(LEFT + DOWN*0.5))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        # self.play(VGroup(eq, eq_).animate.move_to(UP*0.5))

        self.wait(2)


class ConstantLaw(Scene):
    def construct(self):
        desc = Text("Untuk c, k suatu konstanta").scale(0.5).move_to(UP * 3.5)
        eq = MathTex(r"\lim_{x \to c} k").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} k").scale(0.6)
        eq2 = MathTex(r"= k").scale(0.6)
        self.play(Write(desc))
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*2.5))

        self.wait(2)

        eq = MathTex(r"\lim_{x \to c} f(x)").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} f(x)").scale(0.6)
        eq2 = MathTex(r"= f(c)").scale(0.6)
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*1.5))

        self.wait(2)

        eq = MathTex(r"\lim_{x \to c} x").scale(0.6)
        eq_ = MathTex(r"= \lim_{x \to c} x").scale(0.6)
        eq2 = MathTex(r"= c").scale(0.6)
        self.play(FadeIn(eq))
        self.play(eq.animate.move_to(LEFT))
        self.play(FadeIn(eq_.next_to(eq)))
        self.play(Transform(eq_, eq2.next_to(eq)))
        self.play(VGroup(eq, eq_).animate.move_to(UP*0.5))

        self.wait(2)


class SolveIntro(Scene):
    def construct(self):
        title = Text("Contoh Soal").scale(0.7).move_to(UP * 3.5)
        prob = MathTex(r"\lim_{x \to 3}", r"\left(", r"x^2", "+",
                       r"2x", "-", "1", r"\right)").scale(0.65)
        prob_right = MathTex(
            "=", r"\lim_{x \to 3}", r"\left(", r"x^2", "+", r"2x", "-", "1", r"\right)"
        ).scale(0.65)
        prob_expand = MathTex(
            "=", r"\lim_{x \to 3}", r"x^2", "+", r"\lim_{x \to 3}", r"2x", "-", r"\lim_{x \to 3}", "1",
        ).scale(0.65)
        prob_expand_2 = MathTex(
            "=", r"\left(", r"\lim_{x \to 3}", r"x", r"\right)", "^2", "+", "2", r"\lim_{x \to 3}", r"x", "-", r"\lim_{x \to 3}", "1",
        ).scale(0.65)
        prob_solve = MathTex(
            "=", r"\left(", "3", r"\right)", "^2", "+", "2", "(3)", "-", "1",
        ).scale(0.65)
        num_expand = MathTex("=", "9", "+", "6", "-", "1")
        num_end = MathTex("=", "14")

        self.play(Write(title))
        self.play(Write(prob))
        self.play(prob.animate.move_to(LEFT * 1.5))
        self.play(FadeIn(prob_right.next_to(prob)))
        self.wait(2)
        self.play(Transform(prob_right, prob_expand.next_to(prob)))
        self.wait(2)
        self.play(Transform(prob_right, prob_expand_2.next_to(prob)))
        self.wait(2)
        self.play(Transform(prob_right, prob_solve.next_to(prob)))
        self.wait(2)
        self.play(Transform(prob_right, num_expand.next_to(prob)))
        self.wait(2)
        self.play(Transform(prob_right, num_end.next_to(prob)))
        self.wait(2)

        self.wait(2)


class Subtitution(Scene):
    def construct(self):
        title = Text("Metode Subtitusi").scale(0.7).move_to(UP*3.5)
        prob = MathTex(r"\lim_{x \to 3}", r"\left(", r"x^2", "+",
                       r"2x", "-", "1", r"\right)").scale(0.65)
        solve_1 = MathTex(r"(3)^2", "+", r"2(3)", "-", "1").scale(0.65)
        solve_2 = MathTex(r"9", "+", r"6", "-", "1").scale(0.65)
        solve_3 = MathTex(r"14").scale(0.65)

        self.play(Write(title))
        self.play(Write(prob))
        self.wait()
        self.play(Transform(prob, solve_1))
        self.wait()
        self.play(Transform(prob, solve_2))
        self.wait()
        self.play(Transform(prob, solve_3))
        self.wait()
        self.wait(2)


class Factorization(Scene):
    def construct(self):
        title = Text("Metode Faktorisasi").scale(0.7).move_to(UP*3.5)
        test_sub = Text("Coba Metode Subtitusi").scale(0.7).move_to(UP*3.5)
        q = Text("???").scale(0.7).move_to(UP*3.5)
        prob_ = MathTex(
            r"\lim_{x \to 5}", r"\frac{x^2 - x - 20}{x-5}"
        )
        fac = MathTex(
            r"\lim_{x \to 5}", r"\frac{(x+4)(x-5)}{x-5}"
        )
        fac2 = MathTex(
            r"\lim_{x \to 5}", r"(x+4)"
        )
        fac3 = MathTex(
            r"(5+4)"
        )
        fac4 = MathTex(
            r"9"
        )
        prob = MathTex(
            r"\lim_{x \to 5}", r"\frac{x^2 - x - 20}{x-5}"
        )
        sub = MathTex(
            r"\frac{(5)^2 - 5 - 20}{5-5}"
        )
        sub2 = MathTex(
            r"\frac{25 - 5 - 20}{5-5}"
        )
        sub3 = MathTex(
            r"\frac{0}{0}"
        )

        x_range = [-8, 8, 1]
        y_range = [-8, 8, 1]
        x_length = 5
        y_length = 5

        ax = Axes(x_range, y_range, x_length, y_length,
                  axis_config={"include_tip": False}).scale(0.7)
        y_label = ax.get_y_axis_label(
            r"f(x) = \frac{x^2 - x - 20}{x-5}").scale(0.4)

        lp = ax.plot(lambda x: ((x**2) - x - 20)/(x-5),
                     x_range=[-8, 4.99], color=RED)
        rp = ax.plot(lambda x: ((x**2) - x - 20)/(x-5),
                     x_range=[5.01, 8], color=RED)

        plt = VGroup(lp, rp)

        x = ValueTracker(8)
        dot_1 = always_redraw(
            lambda: Dot().move_to(ax.c2p(x.get_value(), rp.underlying_function(x.get_value())))
        )

        gg = VGroup(plt, dot_1, ax, y_label)

        self.play(Write(test_sub))
        self.wait()
        self.play(Write(prob))
        self.wait()
        self.play(Transform(prob, sub))
        self.wait()
        self.play(Transform(prob, sub2))
        self.wait()
        self.play(Transform(prob, sub3))
        self.wait()
        self.play(Transform(test_sub, q))
        self.wait()
        self.play(FadeOut(prob))
        self.wait()
        self.play(FadeIn(ax))
        self.wait()
        self.play(Create(y_label))
        self.wait()
        self.play(Create(plt))
        self.wait()
        self.play(Create(dot_1))
        self.wait()
        self.play(x.animate.set_value(5.01))
        self.wait()
        self.play(Transform(test_sub, title))
        self.wait()
        self.play(FadeOut(gg))
        self.wait()
        self.play(FadeIn(prob_))
        self.play(Transform(prob_, fac))
        self.wait()
        self.play(Transform(prob_, fac2))
        self.wait()
        self.play(Transform(prob_, fac3))
        self.wait()
        self.play(Transform(prob_, fac4))
        self.wait()

        self.wait(2)


class AkarSekawan(Scene):
    def construct(self):
        prob_ = MathTex(
            r"\lim_{x \to 6}", r"\frac{\sqrt{3x-2} - \sqrt{2x + 4} }{x-6}"
        )
        prob = MathTex(
            r"\lim_{x \to 6}", r"\frac{\sqrt{3x-2} - \sqrt{2x + 4} }{x-6}"
        )
        prob_1 = MathTex(
            r"\frac{\sqrt{3(6)-2} - \sqrt{2(6) + 4} }{(6)-6}"
        )
        prob_2 = MathTex(
            r"\frac{\sqrt{16} - \sqrt{16} }{6-6}"
        )
        prob_3 = MathTex(
            r"\frac{4 - 4 }{6-6}"
        )
        prob_4 = MathTex(
            r"\frac{0 }{0}"
        )

        sq = MathTex(r"(a+b)", r"(a-b)")
        sq2 = MathTex(r"a^2-b^2")

        prob1 = MathTex(
            r"\lim_{x \to 6}", r"\frac{\sqrt{3x-2} - \sqrt{2x + 4} }{x-6}", r"\times", r"\frac{\sqrt{3x-2} + \sqrt{2x + 4}}{\sqrt{3x-2} + \sqrt{2x + 4}}"
        )
        prob2 = MathTex(
            r"\lim_{x \to 6}", r"\frac{\sqrt{3x-2} - \sqrt{2x + 4} }{x-6}", r"\times", r"1"
        )
        prob3 = MathTex(
            r"\lim_{x \to 6}", r"\frac{\sqrt{3x-2}^2 - \sqrt{2x + 4}^2 }{(x-6)(\sqrt{3x-2} + \sqrt{2x + 4})}"
        )
        prob4 = MathTex(
            r"\lim_{x \to 6}", r"\frac{3x-2 - (2x + 4) }{(x-6)(\sqrt{3x-2} + \sqrt{2x + 4})}"
        )
        prob5 = MathTex(
            r"\lim_{x \to 6}", r"\frac{x-6 }{(x-6)(\sqrt{3x-2} + \sqrt{2x + 4})}"
        )
        prob6 = MathTex(
            r"\lim_{x \to 6}", r"\frac{1}{(\sqrt{3x-2} + \sqrt{2x + 4})}"
        )
        prob7 = MathTex(
            r"\frac{1}{(\sqrt{3(6)-2} + \sqrt{2(6) + 4})}"
        )
        prob8 = MathTex(
            r"\frac{1}{(\sqrt{16} + \sqrt{16})}"
        )
        prob9 = MathTex(
            r"\frac{1}{(4 + 4)}"
        )
        prob10 = MathTex(
            r"\frac{1}{8}"
        )

        self.play(Write(prob_))
        self.wait()
        self.play(Transform(prob_, prob_1))
        self.wait()
        self.play(Transform(prob_, prob_2))
        self.wait()
        self.play(Transform(prob_, prob_3))
        self.wait()
        self.play(Transform(prob_, prob_4))
        self.wait()
        self.play(FadeOut(prob_))
        self.wait()
        self.play(Write(sq))
        self.wait()
        self.play(Transform(sq, sq2))
        self.wait()
        self.play(FadeOut(sq))
        self.wait()
        self.play(FadeIn(prob))
        self.play(Transform(prob, prob1))
        self.wait()
        self.play(Transform(prob, prob2))
        self.wait()
        self.play(Transform(prob, prob1))
        self.wait()
        self.play(Transform(prob, prob3))
        self.wait()
        self.play(Transform(prob, prob4))
        self.wait()
        self.play(Transform(prob, prob5))
        self.wait()
        self.play(Transform(prob, prob6))
        self.wait()
        self.play(Transform(prob, prob7))
        self.wait()
        self.play(Transform(prob, prob8))
        self.wait()
        self.play(Transform(prob, prob9))
        self.wait()
        self.play(Transform(prob, prob10))
        self.wait()

        self.wait(2)
