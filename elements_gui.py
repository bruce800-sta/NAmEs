import customtkinter as ctk
import csv
import re
import sys
from PIL import Image


def main():
    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("NAmEs")
    app.geometry("360x400")
    app.iconbitmap("names_icon.ico")

    def input_name(event=None):
        """
        examines user input to see if can be made from elemental symbols upon request,
        and updates response cell accordingly
        """
        user_str = entry.get()
        if user_str != "":
            elements_list, symbol_list = import_elements()
            if valid_match(user_str, symbol_list):
                matched_elements = get_matching_elements(user_str, symbol_list)
                result = format_elements(matched_elements, elements_list)
                symbol_label.configure(text=result)
            else:
                result = format_no_match(user_str)
                symbol_label.configure(text=result)

    ### gui layout ###
    
    # logo
    image_icon = ctk.CTkImage(Image.open("names.png"), size=(190, 190))
    image_label = ctk.CTkLabel(app, image=image_icon, text="")
    image_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

    # frame for user interaction
    input_frame = ctk.CTkFrame(app, fg_color="transparent")
    input_frame.grid(row=1, column=0, columnspan=3, rowspan=1)

    # entry box for name, triggers input query if return pressed 
    entry = ctk.CTkEntry(input_frame, placeholder_text="Enter name...", width=200)
    entry.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    entry.bind("<Return>", input_name)

    # button to trigger input query
    button = ctk.CTkButton(
        input_frame, text="Go", command=input_name, width=50, corner_radius=50
    )
    button.grid(row=0, column=2, padx=20, pady=20)

    # frame containing output text
    output_frame = ctk.CTkFrame(app, width=280, height=100)
    output_frame.grid(row=2, column=0, columnspan=3, rowspan=2, padx=20, pady=20)

    # text display showing result of input query
    elements_str = ""
    symbol_label = ctk.CTkLabel(output_frame, text="", width=300, height=50)
    symbol_label.grid(row=0, column=0, columnspan=3, rowspan=2, sticky="nsew")
    symbol_label.configure(text=elements_str)

    app.mainloop()

def import_elements():
    # retrieves elements data, including names and symbols
    try:
        with open("Periodic Table of Elements.csv") as file:
            elements = []
            reader = csv.DictReader(file)
            for row in reader:
                elements.append({"Element": row["Element"], "Symbol": row["Symbol"]})
        symbols = [element["Symbol"] for element in elements]
        return elements, symbols
    except FileNotFoundError:
        sys.exit("Elements list not found")

def valid_match(s, elements):
    # checks if str can be made exclusively from non-overlapping elemental symbols
    full_regex = re.compile("^(" + "|".join(elements) + ")+$", re.IGNORECASE)
    if full_regex.fullmatch(s):
        return True
    else:
        return False


def get_matching_elements(s, elements):
    # extracts non-overlapping, consecutive elemental symbols from str 
    find_regex = re.compile(
        "((?:"
        + "|".join(elements)
        + ")$|(?:"
        + "|".join(elements)
        + ")(?="
        + "|".join(elements)
        + "))",
        re.IGNORECASE,
    )
    return find_regex.findall(s)


def format_elements(elements, elements_dict):
    # formats response including elemental symbols and element names
    element_str = ""
    for element in elements:
        element_str += (element.title()) + " "
    element_str += "\n"
    for element in elements:
        for el in elements_dict:
            if element.title() == el["Symbol"]:
                element_str += el["Element"] + " "
    return element_str


def format_no_match(s):
    # responds with message in case that str cannot be formed  of elemental symbols alone
    return f"Sorry, {s.title()} can't be made from elemental symbols."


if __name__ == "__main__":
    main()
