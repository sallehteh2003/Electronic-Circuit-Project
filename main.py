import schemdraw
import schemdraw.elements as elm
import tkinter as tk
from PIL import Image, ImageTk
import io
from tkinter import font, ttk
import Circuit1 as C

# تابع برای نمایش رسم در Tkinter
def show_drawing_in_tkinter(drawing, frame_to_display):
    # ذخیره رسم در حافظه به عنوان تصویر PNG
    buf = io.BytesIO()
    drawing.save(buf)  # پارامتر format حذف شده است
    buf.seek(0)
    img = Image.open(buf)
    img_tk = ImageTk.PhotoImage(img)
    
    # نمایش تصویر در فریم مشخص شده
    label = tk.Label(frame_to_display, image=img_tk)
    label.image = img_tk  # نگهداری یک مرجع به تصویر
    label.pack()

# تنظیمات Tkinter
root = tk.Tk()
root.title("Circuit Drawer")
root.geometry("900x700")
root.resizable(False, False)  # ثابت کردن اندازه پنجره

# فریم بالا که به چهار بخش تقسیم می‌شود
frame_top = tk.Frame(root)
frame_top.pack(fill=tk.X, pady=10)

# تقسیم فریم بالا به چهار بخش با استفاده از grid
frame_1 = tk.Frame(frame_top)
frame_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

frame_2 = tk.Frame(frame_top)
frame_2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

frame_3 = tk.Frame(frame_top)
frame_3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

frame_4 = tk.Frame(frame_top)
frame_4.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

# تنظیم نسبت ستون‌ها
frame_top.grid_columnconfigure(0, weight=1)
frame_top.grid_columnconfigure(1, weight=1)
frame_top.grid_rowconfigure(0, weight=1)
frame_top.grid_rowconfigure(1, weight=1)


# ایجاد فریم برای نمایش مدار
frame = tk.Frame(root)
frame.pack()


# تابع‌های مختلف برای رسم مدارهای مختلف
def draw_circuit(selected_circuit):
    # پاک کردن محتوای هر فریم قبل از رسم مدار جدید
    for widget in frame_1.winfo_children():
        widget.destroy()
    for widget in frame_2.winfo_children():
        widget.destroy()
    for widget in frame_3.winfo_children():
        widget.destroy()
    for widget in frame_4.winfo_children():
        widget.destroy()

    d = schemdraw.Drawing()
    
    if selected_circuit == "Circuit 1":
        d = C.draw_circuit1_NPN(d)
        show_drawing_in_tkinter(d, frame_1)  # نمایش مدار در قسمت بالا چپ
    elif selected_circuit == "Circuit 2":
        d = C.draw_circuit1_PNP(d)
        show_drawing_in_tkinter(d, frame_1)
    elif selected_circuit == "Circuit 3":
        pass  # در صورت نیاز به اضافه کردن مدارهای جدید
    elif selected_circuit == "Circuit 18":
        pass  # در صورت نیاز به اضافه کردن مدارهای جدید
    
   

# تنظیمات فونت دکمه‌ها
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# ایجاد منوی کشویی برای انتخاب مدار
options = [f"Circuit {i}" for i in range(1, 19)]  # ایجاد لیست مدارها از Circuit 1 تا Circuit 18
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # پیش‌فرض اولین گزینه

# فریم پایین برای دکمه‌ها و منوی کشویی
bottom_frame = tk.Frame(root, bg="lightgray")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# منوی کشویی برای انتخاب مدار
dropdown_menu = ttk.Combobox(bottom_frame, textvariable=selected_option, values=options, font=button_font)
dropdown_menu.set("Select Circuit")  # تنظیم مقدار پیش‌فرض
dropdown_menu.pack(side=tk.LEFT, padx=10, pady=10)

# دکمه برای رسم مدار انتخاب شده
draw_button = tk.Button(bottom_frame, text="Draw Selected Circuit", command=lambda: draw_circuit(selected_option.get()))
draw_button.config(font=button_font, bg="green", fg="white", padx=15, pady=10, relief="raised", bd=3)
draw_button.pack(side=tk.RIGHT, padx=10, pady=10)

# اجرای پنجره اصلی
root.mainloop()
