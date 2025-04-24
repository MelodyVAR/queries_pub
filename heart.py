import turtle
import math

def draw_heart():
    # 设置窗口
    window = turtle.Screen()
    window.bgcolor('white')
    window.title('Love Heart')
    
    # 创建画笔
    pen = turtle.Turtle()
    pen.speed(2)  # 设置绘制速度
    pen.color('red', 'red')  # 设置画笔颜色和填充颜色
    pen.pensize(2)
    
    # 开始绘制
    pen.begin_fill()
    pen.left(140)  # 左转140度
    pen.forward(180)  # 向前移动
    
    # 绘制右半边曲线
    for i in range(200):
        pen.right(1)
        pen.forward(1)
    
    # 绘制心形尖角
    pen.left(120)
    
    # 绘制左半边曲线
    for i in range(200):
        pen.right(1)
        pen.forward(1)
    
    pen.forward(180)
    pen.end_fill()  # 结束填充
    
    # 隐藏画笔
    pen.hideturtle()
    
    # 显示文字
    pen.up()
    pen.goto(0, -50)
    pen.color('red')
    pen.write('Love', align='center', font=('Arial', 20, 'bold'))
    
    # 保持窗口显示
    window.mainloop()

if __name__ == '__main__':
    draw_heart()