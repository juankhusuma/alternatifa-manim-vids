from manim import *


class Equation(Scene):
    def construct(self):
        equation_1 = MathTex("w", "\\times", "v", "=", "1")
        equation_1.shift(UP*2).scale(2)
        equation_2 = MathTex("v", "=", "w^{-1}")
        equation_2.scale(2)
        equation_3 = MathTex("w", "\\times", "w^{-1}", "=", "1")
        equation_3.shift(UP*2).scale(2)

        self.play(Write(equation_1), Write(equation_2))
        self.wait(2)
        self.play(FadeOut(equation_1[2]))

        self.play(
            TransformMatchingShapes(
                VGroup(equation_1[0:2], equation_1[3:], equation_2[2].copy()),
                equation_3,
            )
        )
