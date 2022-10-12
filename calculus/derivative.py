from manim import *


class PowerRule(Scene):
    def construct(self):
        eq1 = MathTex(r"\frac{d}{dx}x^n", r"=", r"nx^{n-1}")
        eq2 = MathTex(r"\frac{d}{dx}x^3", r"=", r"x^3")
        eq3 = MathTex(r"\frac{d}{dx}x^3", r"=", r"3x^{3-1}")
        eq4 = MathTex(r"\frac{d}{dx}x^3", r"=", r"3x^2")

        self.play(Write(eq1))
        self.play(eq1.animate.move_to(UP))
        self.play(Write(eq2))
        self.play(Transform(eq2, eq3))
        self.play(Transform(eq2, eq4))

        self.wait(2)


class ProofPowerRule(Scene):
    def construct(self):
        title = Text("Power Rule").scale(0.7).move_to(3 * UP)
        x3 = MathTex("x^3")
        x3_1 = MathTex(r"\frac{d}{dx}", "x^3")
        x3_def = MathTex("=", r"\lim_{h \to 0}", r"\frac{(x+h)^3 - x^3}{h}")
        x3_def_1 = MathTex(
            "=", r"\lim_{h \to 0}", r"\frac{x^3 + 3x^2 h + 3xh^2 + h^3 - x^3}{h}")
        x3_def_2 = MathTex(
            "=", r"\lim_{h \to 0}", r"\frac{ 3x^2 h + 3xh^2 + h^3 }{h}")
        x3_def_3 = MathTex(
            "=", r"\lim_{h \to 0}", r"3x^2  + 3xh + h^2")
        x3_def_4 = MathTex(
            "=", r"3x^2  + 3x(0) + 0^2")
        x3_def_5 = MathTex(
            "=", r"3x^2")

        self.play(Write(title))
        self.play(Write(x3))
        self.play(Transform(x3, x3_1))
        self.play(ReplacementTransform(x3, x3_1.move_to(LEFT*3)))
        self.play(Write(x3_def.next_to(x3_1)))
        self.wait()
        self.play(Transform(x3_def, x3_def_1.next_to(x3_1)))
        self.wait()
        self.play(Transform(x3_def, x3_def_2.next_to(x3_1)))
        self.wait()
        self.play(Transform(x3_def, x3_def_3.next_to(x3_1)))
        self.wait()
        self.play(Transform(x3_def, x3_def_4.next_to(x3_1)))
        self.wait()
        self.play(Transform(x3_def, x3_def_5.next_to(x3_1)))
        self.play(ReplacementTransform(x3_1, x3.move_to(3 * RIGHT)),
                  ReplacementTransform(x3_def, x3_def_5.next_to(x3_1)))
        self.wait(2)
