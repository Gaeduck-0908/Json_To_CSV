import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import json
import csv

def json_to_csv(json_data, output_path):
    try:
        data_list = json.loads(json_data)
        
        with open(output_path, mode='w', newline='', encoding='utf-8') as csv_file:
            if len(data_list) > 0:
                writer = csv.DictWriter(csv_file, fieldnames=data_list[0].keys())
                writer.writeheader()
                writer.writerows(data_list)
                
        messagebox.showinfo("완료", f"CSV 파일로 성공적으로 저장되었습니다: {output_path}")
    except Exception as e:
        messagebox.showerror("오류", f"CSV 변환 중 오류가 발생했습니다: {e}")

def convert_to_csv():
    json_data = text_box.get("1.0", tk.END).strip()
    if json_data:
        try:
            output_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if output_path:
                json_to_csv(json_data, output_path)
        except Exception as e:
            messagebox.showerror("오류", f"CSV 변환 중 오류가 발생했습니다: {e}")
    else:
        messagebox.showwarning("경고", "JSON 데이터를 입력해주세요.")

def create_gui():
    root = tk.Tk()
    root.title("JSON to CSV 변환기")
    root.geometry("600x450")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 14), padding=10)
    style.configure('TButton', font=('Helvetica', 12), padding=10)
    style.configure('TFrame', background='#f0f0f0')
    style.configure('TText', font=('Helvetica', 12))

    frame = ttk.Frame(root, padding="20 20 20 20", style='TFrame')
    frame.pack(expand=True, fill=tk.BOTH)

    label = ttk.Label(frame, text="JSON 데이터를 입력하세요", style='TLabel')
    label.pack(pady=10)

    global text_box
    text_box = tk.Text(frame, height=12, width=60, font=('Helvetica', 12), relief="solid", borderwidth=1)
    text_box.pack(pady=10)

    convert_button = ttk.Button(frame, text="CSV로 변환", command=convert_to_csv, style='TButton')
    convert_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
