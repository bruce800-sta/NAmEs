import customtkinter as ctk
from PIL import Image
from logic import import_elements, valid_match, get_matching_elements, format_elements, format_no_match


def main():
    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("NAmEs")
    app.geometry("360x400")
    app.iconbitmap("assets/names_icon.ico")

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
    image_icon = ctk.CTkImage(Image.open("assets/names.png"), size=(190, 190))
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


if __name__ == "__main__":
    main()
