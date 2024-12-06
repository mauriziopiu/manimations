from manim import *
import numpy as np

class CreateHermiteCurve(Scene):
    def construct(self):
        
        p0 = (-2.0, -1.0, 0.0)
        p0t = (-4.0, 3.0, 0.0)
        point1a = Dot(point=p0, color=RED)
        p0_label = Text(f"P_0 = ({p0[0]}, {p0[1]}, {p0[2]})").scale(.5).next_to(point1a, DOWN, buff=0.5)
        point1b = Dot(point=p0t, color=RED)
        p0t_arrow = Arrow(start=p0, end=(point1a.get_center() + point1b.get_center()), color=WHITE)
        p0t_label = Text(f"P_0ᵗ = ({p0t[0]}, {p0t[1]}, {p0t[2]})").scale(.5).next_to(p0t_arrow, DOWN, buff=0.1)
        
        p1 = (3.0, 1.0, 0.0)
        p1t = (0.0, -10.0, 0.0)
        point2a = Dot(point=p1, color=BLUE)
        p1_label = Text(f"P_1 = ({p1[0]}, {p1[1]}, {p1[2]})").scale(.5).next_to(point2a, RIGHT, buff=0.5)
        point2b = Dot(point=p1t, color=BLUE)
        p1t_arrow = Arrow(start=p1, end=(point2a.get_center() + point2b.get_center()), color=WHITE)
        p1t_label = Text(f"P_1ᵗ = ({p1t[0]}, {p1t[1]}, {p1t[2]})").scale(.5).next_to(p1_label, DOWN, buff=1.5)     
        
        self.add(point1a)
        self.add(p0_label)
        # self.add(point1b) # this is a vector and not a point
        self.add(p0t_arrow)
        self.add(p0t_label)
        self.add(point2a)
        self.add(p1_label)
        # self.add(point2b) # this is a vector and not a point
        self.add(p1t_arrow)
        self.add(p1t_label)
        self.wait(1)
        
        t = 0.0
        line = (point2a.get_center() - point1a.get_center())
        while t <= 1.0:
            if (t != 0.0 and t != 1.0):
                px_1 = (2*(t**3) - 3*(t**2) + 1)*p0[0]
                px_2 = (-2*(t**3) + 3*(t**2))*p1[0]
                px_3 = (t**3 - 2*(t**2) + t)*p0t[0]
                px_4 = (t**3 - t**2)*p1t[0] 
                px = px_1 + px_2 + px_3 + px_4
                py_1 = (2*(t**3) - 3*(t**2) + 1)*p0[1]
                py_2 = (-2*(t**3) + 3*(t**2))*p1[1]
                py_3 = (t**3 - 2*(t**2) + t)*p0t[1]
                py_4 = (t**3 - t**2)*p1t[1] 
                py = py_1 + py_2 + py_3 + py_4
                pz_1 = (2*(t**3) - 3*(t**2) + 1)*p0[2]
                pz_2 = (-2*(t**3) + 3*(t**2))*p1[2]
                pz_3 = (t**3 - 2*(t**2) + t)*p0t[2]
                pz_4 = (t**3 - t**2)*p1t[2] 
                pz = pz_1 + pz_2 + pz_3 + pz_4
                p = Dot(point=(px, py, pz), radius=0.04, color=WHITE)
                self.add(p)
                
                self.wait(.05)
            t += 0.02;
            
        self.wait(2)
            
            
    def linear_interpolation(self, start, t, line):
        p = Dot(point=(start.get_center() + (t * line)), radius=0.05, color=WHITE)
        self.add(p)
    