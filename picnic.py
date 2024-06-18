import tkinter as tk
import random

root = tk.Tk()
root.title("Picnic Bag List")
root.geometry("400x400")

picnic_items = ['bottle', 'tiffin', 'ID card', 'chocolates', 'chips', 'tickets', 'hanky']

list_label = tk.Label(root, text=f"Listed_Items : {picnic_items}", justify=tk.LEFT, wraplength=300)
list_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

def generate_random_number():
    random_index = random.randint(0, len(picnic_items) - 1)
    random_label.config(text=f"Put item no {random_index + 1} in the bag")  # +1 to show 1-based index

generate_button = tk.Button(root, text="Which item to put in bag?", command=generate_random_number, bg="blue", fg="white")
generate_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

random_label = tk.Label(root, text="")
random_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()

