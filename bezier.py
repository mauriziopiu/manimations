from manim import *
import numpy as np

class BezierCurveSegment(Scene):
    def construct(self):
        p0 = [-3.0, -2.0, 0.0]
        p1 = [-2.5, 2.0, 0.0]
        p2 = [2.5, 2.0, 0.0]
        p3 = [3.0, -2.0, 0.0]
        
        # visualise parameters
        self.showParameters(p0, p1, p2, p3)
        
        # put params in matrix form: P
        p_mat = np.array([p0, p1, p2, p3])
        
        default_bez = bezier(points=p_mat)
        
        # initialise characteristic matrix
        char_mat_bezier = np.array([[-1.0, 3.0, -3.0, 1.0],
                                     [3.0, -6.0, 3.0, 0.0],
                                     [-3.0, 3.0, 0.0, 0.0],
                                     [1.0, 0.0, 0.0, 0.0]])
        
        # calculate parameters F(t)
        def f(t):
            t_vec = np.array([t**3, t**2, t, 1])
            f_vec = t_vec @ char_mat_bezier
            return f_vec
        
        # calculate result P(t)
        def p(t):
            f_vec = f(t)
            p_vec = f_vec @ p_mat
            return p_vec            
        
        # setup path drawing
        path = VMobject(color=GREEN)
        dot = Dot(p0, color=GREEN)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        self.add(path)
        
        # Default Bezier Implementation
        # defaultPath = VMobject(color=RED)
        # defaultDot = Dot(p0, color=RED)
        # defaultPath.set_points_as_corners([defaultDot.get_center(), defaultDot.get_center()])
        # self.add(defaultPath)
        
        t = 0.0
        while t <= 1.0:
            previous_path = path.copy()
            new_pos = p(t)
            
            dot.set_x(new_pos[0])
            dot.set_y(new_pos[1])
            dot.set_z(new_pos[2])
            
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
            
            # Default Bezier Implementation
            # previous_df_path = defaultPath.copy()
            # new_default_pos = default_bez(t)
            
            # defaultDot.set_x(new_default_pos[0])
            # defaultDot.set_y(new_default_pos[1])
            # defaultDot.set_z(new_default_pos[2])
            
            # previous_df_path.add_points_as_corners([defaultDot.get_center()])
            # defaultPath.become(previous_df_path)
            t += 0.02
            self.wait(.05)
        
        self.wait(2)
        
    def showParameters(self, p0, p1, p2, p3):
        p0_dot = Dot(p0, color=BLUE)
        p0_label = Text(f"P_0 = ({p0_dot.get_x()}, {p0_dot.get_y()}, {p0_dot.get_z()})")
        p0_label.scale(.5).next_to(p0_dot.get_center(), DOWN, buff=0.5)
        self.add(p0_dot)
        self.add(p0_label)
        
        p1_dot = Dot(p1, color=BLUE)
        p1_label = Text(f"P_1 = ({p1_dot.get_x()}, {p1_dot.get_y()}, {p1_dot.get_z()})")
        p1_label.scale(.5).next_to(p1_dot.get_center(), UP, buff=0.5)
        self.add(p1_dot)
        self.add(p1_label)
        
        p2_dot = Dot(p2, color=BLUE)
        p2_label = Text(f"P_2 = ({p2_dot.get_x()}, {p2_dot.get_y()}, {p2_dot.get_z()})")
        p2_label.scale(.5).next_to(p2_dot.get_center(), UP, buff=0.5)
        self.add(p2_dot)
        self.add(p2_label)
        
        p3_dot = Dot(p3, color=BLUE)
        p3_label = Text(f"P_3 = ({p3_dot.get_x()}, {p3_dot.get_y()}, {p3_dot.get_z()})")
        p3_label.scale(.5).next_to(p3_dot.get_center(), DOWN, buff=0.5)
        self.add(p3_dot)
        self.add(p3_label)
        
        l01 = Line(start=p0, end=p1, color=WHITE)
        self.add(l01)
        l12 = Line(start=p1, end=p2, color=WHITE)
        self.add(l12)
        l23 = Line(start=p2, end=p3, color=WHITE)
        self.add(l23)
        
        
        
        
        
        
        