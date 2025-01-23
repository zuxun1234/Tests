import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import random

# 定义一个简单的立方体的顶点
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# 定义立方体的边
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def gpu_intensive_task(duration=2):
    """
    使用OpenGL创建一个图形渲染任务，运行指定时间。
    
    参数:
        duration (int): 任务持续时间（秒）。
    """
    # 初始化pygame
    pygame.init()
    print("Pygame初始化完成。")

    # 创建一个窗口
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("GPU占用测试")

    # 设置OpenGL参数
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    # 设置任务结束时间
    end_time = time.time() + duration

    # 渲染图形
    while time.time() < end_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # 渲染多个立方体
        for _ in range(10):
            glPushMatrix()
            glTranslatef(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))
            glRotatef(random.uniform(0, 360), 1, 1, 1)
            Cube()
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    # 退出pygame
    pygame.quit()
    print("GPU任务完成。")

def main(duration=2):
    """
    主函数，用于启动图形渲染任务。
    
    参数:
        duration (int): 持续时间（秒）。
    """
    print(f"目标GPU占用率: 70%")
    print(f"持续时间: {duration}秒")

    # 启动图形渲染任务
    gpu_intensive_task(duration)

if __name__ == "__main__":
    main(duration=2)