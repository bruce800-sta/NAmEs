import csv
import re
import sys

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