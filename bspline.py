from manim import *
import numpy as np

class ClosedQuadraticBSpline(MovingCameraScene):
    def construct(self):
        nmp = NumberPlane(x_range=[-120.0, 120.0, 5], y_range=[-60.0, 60.0, 5], background_line_style={"stroke_opacity": 1.0})
        self.add(nmp)
        self.play(self.camera.frame.animate.scale(20))
    
        p0 = [0.0, 1.0, 0.0]
        p1 = [-50.0, 0.0, 0.0]
        p2 = [-50.0, 50.0, 0.0]
        p3 = [0.0, 50.0, 0.0]
        p4 = [0.0, 50.0, 0.0]
        #p5 = [-25.0, 25.0, 0.0]
        
        # visualise parameters
        self.showPoint(p0, index=0, colorParam=RED)
        self.showPoint(p1, index=1, colorParam=RED)
        self.showPoint(p2, index=2, colorParam=RED)
        self.showPoint(p3, index=3, colorParam=RED)
        self.showPoint(p4, index=4, colorParam=RED)
        
        # put params in matrix form: P
        p_mat_1 = np.array([p0, p1, p2])
        p_mat_2 = np.array([p1, p2, p3])
        p_mat_3 = np.array([p2, p3, p4])
        
        # initialise characteristic matrix
        char_mat_quad = np.array([[1.0, -2.0, 1.0],
                            [-2.0, 2.0, 0.0],
                            [1.0, 1.0, 0.0]])
        
        # calculate parameters F(t)
        def f(t):
            t_vec = np.array([t**2, t, 1])
            f_vec = (0.5 * t_vec) @ char_mat_quad
            return f_vec
        
        # calculate result P(t)
        def p(t, p_mat):
            f_vec = f(t)
            p_vec = f_vec @ p_mat
            return p_vec            
        
        # setup path drawing
        path = VMobject(color=GREEN)
        dot = Dot(p0, color=GREEN)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        self.add(path)
        
        # t = 0.0
        # while t <= 1.0:
        #     previous_path = path.copy()
        #     new_pos = p(t, p_mat_1)
            
        #     dot.set_x(new_pos[0])
        #     dot.set_y(new_pos[1])
        #     dot.set_z(new_pos[2])
            
        #     previous_path.add_points_as_corners([dot.get_center()])
        #     path.become(previous_path)
            
        #     t += 0.02
        #     self.wait(.05)
        
        self.wait(2)
    
    def showPoint(self, p, index, colorParam):
        p_dot = Dot(point=p, color=colorParam)
        # p_label = Text(f"P_{index} = ({p_dot.get_x()}, {p_dot.get_y()}, {p_dot.get_z()})")
        # p_label.scale(.5).next_to(p_dot.get_center(), DOWN, buff=0.5)
        self.add()
        # self.add(p_label)
        
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
        
        
        
        
        
        
        