# 🥗 CLI: Food Calorie Calculator
CLI application designed to help you track and calculate your nutritional intake.

## 🚀 Key Features

-   **📜 Preset Ingredients**: Choose from a predefined list of common ingredients or edit the list to your own liking.
-   **➕ Custom Ingredient Entry**: Add temporary ingredients outside predefined list. 
-   **⚖️ Dynamic Weight Calculation**: Input the weight in grams for any ingredient to get the exact calorie count.
-   **🛡️ Error Handling**: Basic input protection mainly to prevent crashing from unintended input.
-   **🚪 Easy Exit**: Simple escape sequence to terminate the application whenever you're finished.

---

## 🛠️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/hevyriffs/cli_calorie_calculator.git
    cd cli_calorie_calculator

    ```
2.  **Run the Application**
    No external dependencies required! Just pure Python.
    ```bash
    python calorie_calculator.py
    ```

---

## 📖 How to Use

### 1. Select from List
When prompted, select an ingredient from the displayed list by entering it's name, afterwards provide the weight of the ingredient in grams, you will be automatically reprompted after each provided ingredient, duplicates are not allowed.

### 2. Add Custom Ingredient
If your ingredient isn't on the list, enter a name of your ingredient, given you proceed with the action you will be asked for weight and the ingredient's calories per 100g.

### 3. Exit the App and Display Results
Type 'x', or your custom escape sequence at the beginning of the prompt to exit the loop and display calculated results.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---