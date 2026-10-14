import random

state = {}

def setup():
    f = open("words.txt", "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    line = random.choice(lines).strip()
    parts = line.split(":")
    
    state["word"] = parts[0].lower()
    state["hint"] = parts[1]
    state["letters"] = []
    state["errors"] = 0
    state["max"] = 6
    state["active"] = True

def draw():
    fname = str(state["errors"]) + ".txt"
    f = open(fname, "r", encoding="utf-8")
    print(f.read())
    f.close()
    
    print("Подсказка:", state["hint"])
    display = ""
    for char in state["word"]:
        if char in state["letters"]:
            display += char
        else:
            display += "*"
    print("Слово:", display)
    state["current_display"] = display

def ask():
    char = input("Введите букву: ").lower()
    if char not in state["letters"]:
        state["letters"].append(char)
        if char not in state["word"]:
            state["errors"] += 1

def check():
    if state["errors"] >= state["max"]:
        print("Вы проиграли! Слово было:", state["word"])
        state["active"] = False
    elif "*" not in state["current_display"]:
        print("Поздравляем! Вы угадали!")
        state["active"] = False

def is_alive():
    return state["active"]