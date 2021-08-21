from manimlib import *

class test(Scene):
    def construct(self):
        ctext = Text("공리(Axiom)", font='Sans', font_size=48).shift(2*LEFT)
        mtext = TexText("$\\sin{\\theta}^2 + B^2 = C^2$ 피타고라스", font_size=48).next_to(ctext)
        VGroup(ctext, mtext).arrange(buff=1)
        self.play(Write(ctext))
        self.play(FadeIn(mtext, UP))
        self.wait(3)