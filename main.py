import tkinter as tk
import io
import core

# 创建画板


def start_drawing(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y


def draw(event):
    global prev_x, prev_y
    canvas.create_line(prev_x, prev_y, event.x,
                       event.y, fill='black', width=13)
    prev_x, prev_y = event.x, event.y

# 保存图像


def save_image():
    postscript = canvas.postscript(colormode='color')
    image_data = io.BytesIO(postscript.encode('utf-8'))
    num = core.work(image_data)
    print(num)
    label.configure(text="你写的数字是" + str(num))


def clear_canvas():
    canvas.delete("all")


# 创建主窗口
window = tk.Tk()

# 创建画布
canvas = tk.Canvas(window, width=280, height=280, bg='white')
canvas.pack()

# 绑定事件
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)

# 创建按钮
button_save = tk.Button(window, text="分析", command=save_image)
button_save.pack()

button_clear = tk.Button(window, text="清除", command=clear_canvas)
button_clear.pack()

label = tk.Label(window, text='暂无结果', font=('Arial', 20))
label.pack()

# 开始主循环
window.mainloop()
