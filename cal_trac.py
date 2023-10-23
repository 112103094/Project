import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, font

CALORIE_GOAL_LIMIT = 5000   # kcal
PROTEIN_GOAL = 180  # grams
FAT_GOAL = 80  # grams
CARBS_GOAL = 300  # grams

today = []
calories_eaten = []


class Food:
    def __init__(self, name, calories, protein, fat, carbs):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs


def add_food():
    food_window = Tk()
    food_window.title("Add Food")
    food_window.geometry("900x800")
    food_window.configure(bg="#ffff0f")  # Set background color

    name_label = Label(food_window, text="Name:", font=("Arial", 34), bg="#ffffff", fg="#ff0000")  # Set label colors
    name_label.pack(pady=30)
    name_entry = Entry(food_window, width=30)
    name_entry.pack()

    calories_label = Label(food_window, text="Calories:", font=("Arial", 34), bg="#ffffff", fg="#00ff00")  # Set label colors
    calories_label.pack(pady=30)
    calories_entry = Entry(food_window, width=30)
    calories_entry.pack()

    proteins_label = Label(food_window, text="Proteins:", font=("Arial", 34), bg="#ffffff", fg="#0000ff")  # Set label colors
    proteins_label.pack(pady=30)
    proteins_entry = Entry(food_window, width=30)
    proteins_entry.pack()

    fats_label = Label(food_window, text="Fats:", font=("Arial", 34), bg="#ffffff", fg="#ff00ff")  # Set label colors
    fats_label.pack(pady=30)
    fats_entry = Entry(food_window, width=30)
    fats_entry.pack()

    carbs_label = Label(food_window, text="Carbs:", font=("Arial", 34), bg="#ffffff", fg="#ffff00")  # Set label colors
    carbs_label.pack(pady=30)
    carbs_entry = Entry(food_window, width=30)
    carbs_entry.pack()

    def save_food():
        name = name_entry.get()
        calories = int(calories_entry.get())
        proteins = int(proteins_entry.get())
        fats = int(fats_entry.get())
        carbs = int(carbs_entry.get())

        food = Food(name, calories, proteins, fats, carbs)
        today.append(food)
        calories_eaten.append(calories)

        food_window.destroy()

    save_button = Button(food_window, text="Save", command=save_food, bg="#000000", fg="#ffffff")  # Set button colors
    save_button.pack(pady=10)

    food_window.mainloop()


def visualize_progress():
    calorie_sum = sum(food.calories for food in today)
    protein_sum = sum(food.protein for food in today)
    fats_sum = sum(food.fat for food in today)
    carbs_sum = sum(food.carbs for food in today)

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
    axs[0, 0].set_title("Macronutrients Distribution", fontsize=16)
    axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
    axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
    axs[0, 1].set_title("Macronutrients Progress", fontsize=16)
    axs[1, 0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
    axs[1, 0].set_title("Calories Goal Progress", fontsize=16)
    nutrients = ['Calories', 'Protein', 'Fats', 'Carbs']
    values = [calorie_sum, protein_sum, fats_sum, carbs_sum]
    axs[1, 1].bar(nutrients, values)
    axs[1, 1].set_xlabel("Nutrient")
    axs[1, 1].set_ylabel("Nutrient Value")
    axs[1, 1].set_title("Nutrient Distribution", fontsize=16)

    fig.tight_layout()
    plt.show()


root = Tk()
root.title("Calorie Tracker")
root.geometry("900x800")
root.configure(bg="#ffffff")  # Set background color

add_food_button = Button(root, text="Add a new food", command=add_food, font=("Arial", 44), bg="#0000ff", fg="#ffffff")  # Set button colors
add_food_button.pack(pady=60)

visualize_button = Button(root, text="Visualize progress", command=visualize_progress, font=("Arial", 44), bg="#00ff00", fg="#000000")  # Set button colors
visualize_button.pack(pady=60)

quit_button = Button(root, text="Quit", command=root.destroy, font=("Arial", 44), bg="#ff0000", fg="#ffffff")  # Set button colors
quit_button.pack(pady=60)

root.mainloop()

