import tkinter as tk
from tkinter import ttk

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]

def calculate_relationship_status():
    p1 = entry_p1.get().lower().replace(" ", "")
    p1_list = list(p1)

    p2 = entry_p2.get().lower().replace(" ", "")
    p2_list = list(p2)

    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index + 1:]

    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[: split_index]
            result = right + left
        else:
            result = result[: len(result) - 1]

    result_label.config(text="Relationship status: " + result[0], foreground=color_dict.get(result[0], "black"))
    relationship_status.set(result[0])

def clear_input_fields():
    entry_p1.delete(0, tk.END)
    entry_p2.delete(0, tk.END)
    result_label.config(text="Relationship status: ")
    relationship_status.set("")

# Create main window
root = tk.Tk()
root.title("Relationship Status Calculator")

# Define colors
color_dict = {
    "Friends": "green",
    "Love": "red",
    "Affection": "blue",
    "Marriage": "purple",
    "Enemy": "black",
    "Siblings": "brown"
}

# Create and place widgets
style = ttk.Style()
style.configure("TButton", foreground="white", background="#4CAF50", font=('Helvetica', 10, 'bold'))

label_p1 = tk.Label(root, text="Player 1 name:", font=('Helvetica', 12))
label_p1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_p1 = tk.Entry(root, font=('Helvetica', 12))
entry_p1.grid(row=0, column=1, padx=10, pady=5)

label_p2 = tk.Label(root, text="Player 2 name:", font=('Helvetica', 12))
label_p2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_p2 = tk.Entry(root, font=('Helvetica', 12))
entry_p2.grid(row=1, column=1, padx=10, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_relationship_status)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Relationship status: ", font=('Helvetica', 14, 'bold'))
result_label.grid(row=3, column=0, columnspan=2)

relationship_status = tk.StringVar()
relationship_dropdown = ttk.Combobox(root, textvariable=relationship_status, values=["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"], state="readonly", font=('Helvetica', 12))
relationship_dropdown.grid(row=4, column=0, columnspan=2, pady=10)
relationship_dropdown.set("")

clear_button = ttk.Button(root, text="Clear", command=clear_input_fields)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
