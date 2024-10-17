from task_template import TEXTS

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""

# Funkce pro analýzu

def text_analysis(text_):
    total_words = 0
    title_words = 0
    upper_words = 0
    lower_words = 0
    numeric_words = 0
    numeric_sum = 0
    length_frequency = {}
    commas = ("-" * 40)

    for text in text_.split():
        total_words += 1
        if text.istitle():
            title_words += 1
        elif text.isupper():
            upper_words += 1
        elif text.islower():
            lower_words += 1
        elif text.isnumeric():
            numeric_words += 1
            numeric_sum += int(text)
                
        length = len(text.strip(".,!?"))  
        if length in length_frequency:
            length_frequency[length] += 1
        else:
            length_frequency[length] = 1
        
    print(f"Ve vybraném textu je {total_words} slov.")
    print(f"Ve vybraném textu je/jsou {title_words} slov/a s počatečním velkým písmenem.")
    print(f"Ve vybraném textu je {upper_words} slov/o psané/ých velkými písmeny.")
    print(f"Ve vybraném textu je {lower_words} slov s malými písmeny.")
    print(f"Ve vybraném textu je/jsou {numeric_words} slova/o s číselným stringem.")
    print(f"Suma všech čísel v textu je {numeric_sum}.")

    print(f"{commas}\nLEN|  OCCURENCES  |NR.\n{commas}")
    for length, count in sorted(length_frequency.items()):
        print(f"{length} | {'*' * count} |{count}")

# Hlavní funkce
def login():
    username = input("přihlašovací jméno: ")
    password = input("heslo: ")

    commas = ("-" * 40)

    registered_users = {
        "bob" : "123",
        "ann" : "pass123",
        "mike": "password123",
        "liz" : "pass123"
    }

    if registered_users.get(username) == password:
        print(f"{commas}\nVítej v aplikaci, {username}\nMáme 3 texty, které je třeba analyzovat.\n{commas}")

        try:
            number_selection = int(input(f"Zadejte číslo v rozmezí 1 - 3: "))
            print(commas)
            if number_selection < 1 or number_selection > 3:
                print("Číslo není v rozmezí 1 - 3, ukončuji program.")
                exit()
        except ValueError:
            print("Zadali jste neplatný vstup, ukončuji program.")
            exit()
        
        if number_selection == 1:
            text_ = TEXTS[0]
            text_analysis(text_)
        elif number_selection == 2:
            text_ = TEXTS[1]
            text_analysis(text_)
        elif number_selection == 3:
            text_ = TEXTS[2]
            text_analysis(text_)
    else :
        print("Neregistrovaný uživatel, ukončuji program..")
login()


