import tkinter as tk


def highlight_selection():
    text_widget = root.focus_get()

    if isinstance(text_widget, tk.Text):
        try:
            start_index = text_widget.index(tk.SEL_FIRST)
            end_index = text_widget.index(tk.SEL_LAST)
            selected_text = text_widget.get(start_index, end_index)
            marked_text = selected_text
            text_widget.delete(start_index, end_index)
            text_widget.insert(start_index, marked_text)
            text_widget.tag_add("highlight", start_index, f"{start_index}+{len(marked_text)}c")

            print(f"Highlighted from [h_begin]: {start_index} to [h_end]: {start_index}+{len(marked_text)}c")
        except tk.TclError:
            print("No text selected.")


def submit():
    text1_content = text_widget1.get("1.0", tk.END).strip()
    text2_content = text_widget2.get("1.0", tk.END).strip()
    print("Text Box 'Before':\n", text1_content)
    print("\nText Box 'After':\n", text2_content)


def search_validate():
    if search_validate_var.get():
        print("Search/Validate checked")
    else:
        print("Search/Validate unchecked")


def search_replace():
    if search_replace_var.get():
        print("Search + Replace checked")
    else:
        print("Search + Replace unchecked")


root = tk.Tk()
root.title("")

search_validate_var = tk.BooleanVar()
search_replace_var = tk.BooleanVar()

search_validate_checkbox = tk.Checkbutton(root, text="Search/Validate", variable=search_validate_var, command=search_validate)
search_replace_checkbox = tk.Checkbutton(root, text="Search + Replace", variable=search_replace_var, command=search_replace)

label_before = tk.Label(root, text="Before:")
label_after = tk.Label(root, text="After:")

text_widget1 = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_widget2 = tk.Text(root, wrap=tk.WORD, height=10, width=40)

text_widget1.tag_config("highlight", background="yellow")
text_widget2.tag_config("highlight", background="yellow")

highlight_button = tk.Button(root, text="Highlight", command=highlight_selection)

submit_button = tk.Button(root, text="Submit", command=submit)

search_validate_checkbox.pack(pady=5)
search_replace_checkbox.pack(pady=5)
label_before.pack(pady=5)
text_widget1.pack(pady=10)
label_after.pack(pady=5)
text_widget2.pack(pady=10)
highlight_button.pack(pady=5)
submit_button.pack(pady=5)

root.mainloop()
