from manim import *
import numpy as np

class HermiteCurve(Scene):
    def construct(self):
        p0 = [-2.0, -1.5, 0.0] # control point 0
        p0t = [-3.0, 4.0, 0.0] # tangent vector at control point 0
        p1 = [3.0, 1.0, 0.0] # control point 1
        p1t = [-3.0, -5.0, 0.0] # tangent vector at control point 1
        
        # visualise parameters
        self.showParameters(p0, p0t, p1, p1t)
        
        # put params in matrix form: P
        p_mat = np.array([p0, p1, p0t, p1t])
        
        # initialise characteristic matrix
        char_mat_hermite = np.array([[2.0, -2.0, 1.0, 1.0],
                                     [-3.0, 3.0, -2.0, -1.0],
                                     [0.0, 0.0, 1.0, 0.0],
                                     [1.0, 0.0, 0.0, 0.0]])
        
        # calculate parameters F(t)
        def f(t):
            t_vec = np.array([t**3, t**2, t, 1])
            f_vec = t_vec @ char_mat_hermite
            return f_vec
        
        # calculate result P(t)
        def p(t):
            f_vec = f(t)
            p_vec = f_vec @ p_mat
            return p_vec            
        
        # setup path drawing
        path = VMobject()
        dot = Dot(p0)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        self.add(path)
        
        t = 0.0
        while t <= 1.0:
            previous_path = path.copy()
            new_pos = p(t)
            
            dot.set_x(new_pos[0])
            dot.set_y(new_pos[1])
            dot.set_z(new_pos[2])
            
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
            t += 0.02
            self.wait(.05)
        
        self.wait(2)
        
    def showParameters(self, p0, p0t, p1, p1t):
        p0_dot = Dot(p0, color=BLUE)
        p0t_dot = Dot(p0t, color=BLUE)
        p0t_arrow = Arrow(start=p0, end=(p0_dot.get_center() + p0t_dot.get_center()), color=WHITE)
        
        p0_label = Text(f"P_0 = ({p0_dot.get_x()}, {p0_dot.get_y()}, {p0_dot.get_z()})")
        p0_label.scale(.5).next_to(p0_dot.get_center(), DOWN, buff=0.5)
        p0t_label = Text(f"P_0ᵗ = ({p0t_dot.get_x()}, {p0t_dot.get_y()}, {p0t_dot.get_z()})")
        p0t_label.scale(.5).next_to((p0_dot.get_center() + (0.5 *p0t_dot.get_center())), LEFT, buff=0.5) # in the middle of the arrow's path
        
        self.add(p0_dot)
        self.add(p0t_arrow)
        self.add(p0_label)
        self.add(p0t_label)
        
        p1_dot = Dot(p1, color=RED)
        p1t_dot = Dot(p1t, color=RED)
        p1t_arrow = Arrow(start=p1, end=(p1_dot.get_center() + p1t_dot.get_center()), color=WHITE)
        
        p1_label = Text(f"P_1 = ({p1_dot.get_x()}, {p1_dot.get_y()}, {p1_dot.get_z()})")
        p1_label.scale(.5).next_to(p1_dot.get_center(), RIGHT, buff=0.5)
        p1t_label = Text(f"P_1ᵗ = ({p1t_dot.get_x()}, {p1t_dot.get_y()}, {p1t_dot.get_z()})")
        p1t_label.scale(.5).next_to((p1_dot.get_center() + (0.5 *p1t_dot.get_center())), RIGHT, buff=0.5) # in the middle of the arrow's path
        
        self.add(p1_dot)
        self.add(p1t_arrow)
        self.add(p1_label)
        self.add(p1t_label)
        
        
        