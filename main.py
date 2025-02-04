import schemdraw
import schemdraw.elements as elm
import tkinter as tk
from PIL import Image, ImageTk
import io
from tkinter import font, ttk
import Circuit1  as C
import Circuit10 as C1
import Circuit7 as C2
import Circuit6 as C3
import Circuit2  as C4
import Circuit3  as C5
import Circuit4  as C6
import Circuit8  as C7
import Circuit9  as C8
from tkinter import simpledialog
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

Circuit_inputs= {"Circuit 1":[5,"VCC","VBB","RB","RC","BETA"],"Circuit 2":[6,"VCC","VBB","RB","RC","RE","BETA"],
                 "Circuit 9":[7,"VEE","VCC","RB1","RC","BETA","RE","RB2"],"Circuit 6":[6,"VCC","RB1","RC","BETA","RE","RB2"],
                 "Circuit 3":[4,"VCC","RB","RC","BETA"],"Circuit 4":[4,"VCC","RB","RC","BETA"],"Circuit 8":[5,"VCC","RB","RC","BETA","RE",],
                 "Circuit 5":[6,"VCC","RB","RC","BETA","RE","VEE"],"Circuit 7":[5,"VCC","RB","RC","BETA","RE"]}

def clean_frames():
    for widget in frame_1.winfo_children():
        widget.destroy()
    for widget in frame_2.winfo_children():
        widget.destroy()
    for widget in frame_3.winfo_children():
        widget.destroy()
    for widget in frame_4.winfo_children():
        widget.destroy()

def Analysis_circuit(inputs,selected_circuit,selected_Type):
    clean_frames()
    d = schemdraw.Drawing()
    result = {}
    if selected_circuit == "Circuit 1":
        if(selected_Type == "NPN"):
            d = C.draw_circuit1_NPN(d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VBB"][1])
            show_drawing_in_tkinter(d, frame_1)
            result = C.Analysis_for_circuit1_NPN(inputs["VBB"][0],inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
            d = schemdraw.Drawing()
            d = result[1](d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VBB"][1])
        else:
            d = C.draw_circuit1_PNP(d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VBB"][1])
            show_drawing_in_tkinter(d, frame_1)
            result = C.Analysis_for_circuit1_PNP(inputs["VBB"][0],inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
            d = schemdraw.Drawing()
            d = result[1](d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VBB"][1])

    elif selected_circuit == "Circuit 2":
        if selected_Type == "NPN":
                d = C4.draw_circuit2_NPN(d,inputs["VBB"][1],inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C4.Analysis_for_circuit2_NPN(inputs["VBB"][0],inputs["RB"][0],inputs["RE"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["VBB"][1],inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
        else:
                d = C4.draw_circuit2_PNP(d,inputs["VBB"][1],inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C4.Analysis_for_circuit2_PNP(inputs["VBB"][0],inputs["RB"][0],inputs["RE"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["VBB"][1],inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1]) 
    elif selected_circuit == "Circuit 3":
        if selected_Type == "NPN":
                d = C5.draw_circuit3_NPN(d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C5.Analysis_for_circuit3_NPN(inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1])
        else:
                d = C5.draw_circuit3_PNP(d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C5.Analysis_for_circuit3_PNP(inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1]) 
    elif selected_circuit == "Circuit 4":
        if selected_Type == "NPN":
                d = C6.draw_circuit4_NPN(d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C6.Analysis_for_circuit4_NPN(inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1])
        else:
                d = C6.draw_circuit4_PNP(d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C6.Analysis_for_circuit4_PNP(inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["RC"][1],inputs["VCC"][1]) 
    elif selected_circuit == "Circuit 5":
        if selected_Type == "NPN":
                d = C3.draw_circuit6_NPN(d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1],inputs["VEE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C3.Analysis_for_circuit6_NPN(inputs["VEE"][0],inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0],inputs["RE"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1],inputs["VEE"][1])
        else:
                d = C3.draw_circuit6_PNP(d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1],inputs["VEE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C3.Analysis_for_circuit6_PNP(inputs["VEE"][0],inputs["RB"][0],inputs["BETA"][0],inputs["VCC"][0],inputs["RC"][0],inputs["RE"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1],inputs["VEE"][1])  
    elif selected_circuit == "Circuit 6":
        if selected_Type == "NPN":
                d = C2.draw_circuit7_NPN(d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C2.Analysis_for_circuit7_NPN(inputs["RB2"][0],inputs["RB1"][0],inputs["VCC"][0],inputs["RC"][0],inputs["RE"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
        else:
                d = C2.draw_circuit7_PNP(d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C2.Analysis_for_circuit7_PNP(inputs["RB2"][0],inputs["RB1"][0],inputs["VCC"][0],inputs["RC"][0],inputs["RE"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])  
    elif selected_circuit == "Circuit 7":
        if selected_Type == "NPN":
                d = C7.draw_circuit8_NPN(d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C7.Analysis_for_circuit8_NPN(inputs["VCC"][0],inputs["RE"][0],inputs["RB"][0],inputs["RC"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
        else:
                d = C7.draw_circuit8_PNP(d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C7.Analysis_for_circuit8_PNP(inputs["VCC"][0],inputs["RE"][0],inputs["RB"][0],inputs["RC"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
    elif selected_circuit == "Circuit 8":
        if selected_Type == "NPN":
                d = C8.draw_circuit9_NPN(d,inputs["RC"][1],inputs["RB"][1],inputs["RE"][1],inputs["VCC"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C8.Analysis_for_circuit9_NPN(inputs["VCC"][0],inputs["RC"][0],inputs["RB"][0],inputs["RE"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RC"][1],inputs["RB"][1],inputs["RE"][1],inputs["VCC"][1])
        else:
                d = C8.draw_circuit9_PNP(d,inputs["RC"][1],inputs["RB"][1],inputs["RE"][1],inputs["VCC"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C8.Analysis_fort_circuit9_PNP(inputs["VCC"][0],inputs["RC"][0],inputs["RB"][0],inputs["RE"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB"][1],inputs["VCC"][1],inputs["RC"][1],inputs["RE"][1])
    elif selected_circuit == "Circuit 9":
            if selected_Type == "NPN":
                d = C1.draw_circuit10_NPN(d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VEE"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C1.Analysis_for_circuit10_NPN(inputs["RB2"][0],inputs["RB1"][0],inputs["VEE"][0],inputs["VCC"][0],inputs["RC"][0],inputs["RE"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VEE"][1],inputs["RE"][1])
            else:
                d = C1.draw_circuit10_PNP(d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VEE"][1],inputs["RE"][1])
                show_drawing_in_tkinter(d, frame_1)
                result = C1.Analysis_for_circuit10_PNP(inputs["RB2"][0],inputs["RB1"][0],inputs["VEE"][0],inputs["VCC"][0],inputs["RC"][0],inputs["RE"][0],inputs["BETA"][0])
                d = schemdraw.Drawing()
                d = result[1](d,inputs["RB1"][1],inputs["RB2"][1],inputs["VCC"][1],inputs["RC"][1],inputs["VEE"][1],inputs["RE"][1])
    
    show_drawing_in_tkinter(d, frame_2)
    text = f"State of BJT : {result[0][0]}\n IB : {result[0][1]} mA\n IC : {result[0][2]} mA\n VCE (NPN) or VEC (PNP) : {result[0][3]} V\n"
    label = tk.Label(frame_4, text=text, font=("Helvetica", 10))
    label.pack(padx=10, pady=10)
    label1 = tk.Label(frame_3, text=result[2], font=("Helvetica", 10))
    label1.pack(padx=10, pady=10)
    
    
    
   
# تابع‌های مختلف برای رسم مدارهای مختلف
def draw_circuit(selected_circuit,selected_Type):
    clean_frames()
    d = schemdraw.Drawing()
    label = tk.Label(frame_1, text= selected_circuit, font=("Helvetica", 11,'bold'))
    label.pack(padx=10, pady=10)
    if selected_circuit == "Circuit 1":
        if selected_Type == "NPN":
            d = C.draw_circuit1_NPN(d)
        else:
            d = C.draw_circuit1_PNP(d)
    elif selected_circuit == "Circuit 2":
        if selected_Type == "NPN":
            d = C4.draw_circuit2_NPN(d)
        else:
            d = C4.draw_circuit2_PNP(d)
    elif selected_circuit == "Circuit 3":
        if selected_Type == "NPN":
            d = C5.draw_circuit3_NPN(d)
        else:
            d = C5.draw_circuit3_PNP(d)
    elif selected_circuit == "Circuit 4":
        if selected_Type == "NPN":
            d = C6.draw_circuit4_NPN(d)
        else:
            d = C6.draw_circuit4_PNP(d)
    elif selected_circuit == "Circuit 5":
        if selected_Type == "NPN":
            d = C3.draw_circuit6_NPN(d)
        else:
            d = C3.draw_circuit6_PNP(d)  
    elif selected_circuit == "Circuit 6":
        if selected_Type == "NPN":
            d = C2.draw_circuit7_NPN(d)
        else:
            d = C2.draw_circuit7_PNP(d)
    elif selected_circuit == "Circuit 7":
        if selected_Type == "NPN":
            d = C7.draw_circuit8_NPN(d)
        else:
            d = C7.draw_circuit8_PNP(d)
    elif selected_circuit == "Circuit 8":
        if selected_Type == "NPN":
            d = C8.draw_circuit9_NPN(d)
        else:
            d = C8.draw_circuit9_PNP(d)
    elif selected_circuit == "Circuit 9":
        if selected_Type == "NPN":
            d = C1.draw_circuit10_NPN(d)
        else:
            d = C1.draw_circuit10_PNP(d)
    show_drawing_in_tkinter(d, frame_1)
    
def open_input_window(selected_circuit,selected_Type):
    # ایجاد یک پنجره جدید
    input_window = tk.Toplevel(root)
    # از کاربر می‌خواهیم که تعداد ورودی‌ها را وارد کند
    num_inputs = Circuit_inputs[selected_circuit][0]
    # لیستی برای ذخیره ورودی‌ها
    input_entries = []
    
    # ایجاد ورودی‌ها به تعداد مورد نظر
    for i in range(num_inputs):
        temp=""
        if Circuit_inputs[selected_circuit][i+1]=="VCC" or Circuit_inputs[selected_circuit][i+1]=="VBB" or Circuit_inputs[selected_circuit][i+1]=="VEE" :
            temp = Circuit_inputs[selected_circuit][i+1] +" (Volts)"
        elif Circuit_inputs[selected_circuit][i+1]=="RB" or Circuit_inputs[selected_circuit][i+1]=="RC" or Circuit_inputs[selected_circuit][i+1]=="RE":
            temp = Circuit_inputs[selected_circuit][i+1]+" (K ohms)"
        elif Circuit_inputs[selected_circuit][i+1]=="RB1" or Circuit_inputs[selected_circuit][i+1]=="RB2":
            temp = Circuit_inputs[selected_circuit][i+1]+" (K ohms)"
        else:
            temp = Circuit_inputs[selected_circuit][i+1]
        label = tk.Label(input_window, text=temp)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(input_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        input_entries.append(entry)
        
    
    # دکمه برای ارسال ورودی‌ها
    def submit_inputs():
        inputs={}
        for i in range(num_inputs):
            temp=""
            if Circuit_inputs[selected_circuit][i+1]=="VCC" or Circuit_inputs[selected_circuit][i+1]=="VBB" or Circuit_inputs[selected_circuit][i+1]=="VEE":
                temp=input_entries[i].get()+"V"
            elif Circuit_inputs[selected_circuit][i+1]=="RB" or Circuit_inputs[selected_circuit][i+1]=="RC" or Circuit_inputs[selected_circuit][i+1]=="RE" :
                temp=input_entries[i].get()+"K"
            elif Circuit_inputs[selected_circuit][i+1]=="RB1" or Circuit_inputs[selected_circuit][i+1]=="RB2":
                temp=input_entries[i].get()+"K"
            else :
                temp=input_entries[i].get()
            inputs[Circuit_inputs[selected_circuit][i+1]] = (int(input_entries[i].get()),temp)
        print(inputs)
        Analysis_circuit(inputs,selected_circuit,selected_Type)
        
        input_window.destroy()

    submit_button = tk.Button(input_window, text="OK", command=submit_inputs)
    submit_button.grid(row=num_inputs, columnspan=2, pady=10)


# تنظیمات فونت دکمه‌ها
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# ایجاد منوی کشویی برای انتخاب مدار
options = [f"Circuit {i}" for i in range(1, 10)]  # ایجاد لیست مدارها از Circuit 1 تا Circuit 18
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # پیش‌فرض اولین گزینه

Types = ["NPN","PNP"]
selected_option1 = tk.StringVar(root)
selected_option1.set(Types[0])  # پیش‌فرض اولین گزینه

# فریم پایین برای دکمه‌ها و منوی کشویی
bottom_frame = tk.Frame(root, bg="lightgray")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# منوی کشویی برای انتخاب مدار
dropdown_menu = ttk.Combobox(bottom_frame, textvariable=selected_option1, values=Types, font=button_font,state="readonly")
dropdown_menu.set("Select Type of BJT")  # تنظیم مقدار پیش‌فرض
dropdown_menu.pack(side=tk.LEFT, padx=10, pady=10)

dropdown_menu = ttk.Combobox(bottom_frame, textvariable=selected_option, values=options, font=button_font,state="readonly" )
dropdown_menu.set("Select Circuit")  # تنظیم مقدار پیش‌فرض
dropdown_menu.pack(side=tk.LEFT, padx=10, pady=10)

# دکمه برای رسم مدار انتخاب شده
draw_button = tk.Button(bottom_frame, text="Draw Selected Circuit", command=lambda: draw_circuit(selected_option.get(),selected_option1.get()))
draw_button.config(font=button_font, bg="green", fg="white", padx=15, pady=10, relief="raised", bd=3)
draw_button.pack(side=tk.RIGHT, padx=10, pady=10)

draw_button = tk.Button(bottom_frame, text="Enter inputs", command=lambda: open_input_window(selected_option.get(),selected_option1.get()))
draw_button.config(font=button_font, bg="red", fg="white", padx=15, pady=10, relief="raised", bd=3)
draw_button.pack(side=tk.TOP, padx=10, pady=10)

# اجرای پنجره اصلی
root.mainloop()
