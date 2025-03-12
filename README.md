# NAmEs
A small app for splitting names or words into chemical symbols from the periodic table of elements.

## Description:
### Overview
Since high school, I was frustrated in chemistry class that I couldn't make my name out of the symbols from the periodic table. This program will identify all of the chemical symbols in a name or word, and return both the symbols and the name of each element. The program uses CustomTkinter for a modern GUI.

### Files
The NAmEs folder is composed 2 main files.

***NAmEs.py***
This file contains the **NAmEs** gui.

- *main()*:
-- This function contains the **NAmEs** app. After initial GUI considerations, including dimensions and theme, this function also contains the layout of the GUI, including an entry box, button and labels. The action that occurs upon clicking a button or pressing enter is described by the nexted function *input_name()*
-- *input_name()*:
--- This function calls the logic of the **NAmEs** app. First it gets the text from the entry box and if this is non-trivial (i.e. not ""), it calls *import_elements()*, checks that the string can be formed of chemical symbols using *valid_match()*, determines the appropriate response using either *get_matching_elements()* and *format_elements()* or *format_no_match()* if the string cannot be made up of chemical elements. This response is then passed to the output label.

***logic.py***
This file contains the underlying logic of the app, through the functions detailed below.

- *import_elements()*:
-- Retrieves elemental data from csv file and returns a list of symbols and a list of dictionaries containing each elemental symbol and name. If csv file is not found an error is raised through sys.exit.

- *valid_match(s,elements)*:
-- Determines if *s* can be formed of non-overlapping chemical symbols, found in *elements* using regex. Returns True or False, as appropriate.

- *get_matching_elements(s,elements)*:
-- Finds individual symbols taken from *elements* that make up *s* using regex. This regex includes a lookahead for an immediately following symbol. The re.findall returns all symbols present within the string and without this lookahead, incorrect solutions could be found such as ["na","es"] for "names", when ["n","am","es"] is the only possible solution. The function returns identified symbols as a list.

- *format_elements(elements,elements_dict)*:
-- Formats the string to pass to the output label. Produces a string composed of both the chemical symbols of *elements* and the name associated with each element using the elements_dict. Returns the formatted string.

- *format_no_match(s)*:
-- Formats a string stating that *s* cannot be formed of chemical symbols and returns this string.


***Et cetera***
- ***README.md***, provides project details.
- ***Periodic Table of Elements.csv***, includes elemental data used for NAmEs app.
***assets***
- ***names.png***, **NAmEs** logo
- ***names_icon.ico***, **NAmEs** icon image


### Design choices
- Used regex for both validating name made of symbols and extraction of those symbols. A recursive search could have been used instead, incorporating some form of permutation logic however this method was not immediately clear to me and would be more verbose. Such a method could however provide alternate solutions such as both:
"C O C O" and "Co Co" for "Coco". Current implementation reports only the latter.
- This current version does not test that string is purely alphabetic, and non-alphabetic characters return a simple "no match" response, as this seemed like an appropriate response. This could be handled differently however, such as separating strings on non-alphabetical characters and parsing each fragment before rejoining them if each fragment matched.


### Potential for future features
- Real time processing of entry text (no need for button or return key).
- Parsing multiple words, separating at " ", ",", "." etc.
- Generation of names that can fit pattern. Useful for baby name ideas.
- Reporting alternate solutions, where possible.
- Improved GUI layout.
- Additional functionality in response e.g. different colours for symbols based on group, or information on each element when hovering over symbol or name.


### Acknowledgments
**"Periodic Table of Elements.csv"** obtained from [GoodmanSciences](https://gist.github.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee)
