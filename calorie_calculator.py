import re
basic_ingredients = {
    'flour':3.64,'sugar':3.87, 'oil':8.84, 'carbohydrates':4,'fat':9,'protein':4,'milk':0.46,'yoghurt':0.549,'tofu':1.46,
    'cocoa':2.88, 'chocolate':5.5, 'butter':7.20
    }
running = True
ingredients_added = []
total_calories = 0

while running:
    for ingr in basic_ingredients:
        print (ingr.capitalize(), end =" | ")
    ingredient_name = input("\n\nSelect from the provided list of ingredients or list your own (x to exit): ")
    #Provides an option to exit the loop
    if ingredient_name.lower() == "x":
        running = False
    
    elif ingredient_name in basic_ingredients: #Validation
        try:
            #If ingredient was not added to the calculation yet, will append ingredient details to a list to prevent duplicates
            unique_ingr = [ingr['name'] for ingr in ingredients_added]
            if ingredient_name not in unique_ingr:               
                weight = float(input("Enter the weight in grams: "))
                if weight > 0:
                    calorie_equation = float(weight * basic_ingredients[ingredient_name])
                    ingredient = {
                        'name': ingredient_name,
                        'weight': weight,
                        'calorie': calorie_equation
                    }
                    ingredients_added.append(ingredient)
                else:
                    print ("\nNegative numbers not allowed")
            #In case of duplicate ingredient input, informs the user and provides option to update the ingredient details
            else:
                update_answer = input("Ingredient already listed, would you like to update the weight of the ingredient? (Y/N): ").capitalize()
                # Reprompts the user until a valid input is made
                while not update_answer in ["Y","N"]:
                    update_answer = input("Ingredient already listed, would you like to update the weight of the ingredient? (Y/N): ").capitalize()
                #Updates the ingredient details
                if update_answer == "Y":
                    
                    weight = float(input("Enter the weight in grams: "))
                    if weight > 0:
                        calorie_equation = float(weight * basic_ingredients[ingredient_name])

                        for ing in ingredients_added:   #Shows updated ingredient details
                            if ing['name'] == ingredient_name:
                                ing['weight'], ing['calorie'] = weight, calorie_equation
                                print (f"\nCurrent weight: {ing['weight']:g}g of {ingredient_name} \nCurrent calories: {ing['calorie']:g}kcal\n")
                            else:
                                continue
                #Outputs current ingredient details          
                else:
                    for i_added in ingredients_added:
                        if i_added['name'] == ingredient_name:
                            print(f"\nCurrent weight: {i_added['weight']:.2fg}g of {ingredient_name} \nCurrent calories: {i_added['calorie']:g}kcal\n")
                    continue

        except ValueError:
            print ("Invalid input! A number must be entered.")
        except TypeError:
            print ("Data operation not supported")
        except Exception:
            print ("Unexpected error occured!")
        finally:
                print ()

    #Validates input and gives user an option to add their own food or ingredient to calculate
    elif re.fullmatch(r'[a-zA-Z ]+', ingredient_name):
        unique_ingr = [ingr['name'] for ingr in ingredients_added]

        if ingredient_name not in unique_ingr:  #Adds new ingredient if it isn't listed yet   
            answer = input(f"Would you like to add {ingredient_name} to the ingredients list? (Y/N): ").capitalize()

            while not answer in ["Y","N"]:
                answer = input(f"Would you like to add {ingredient_name} to the ingredients list? (Y/N): ").capitalize()
            
            if answer == "Y":
                try:
                    weight = float(input("Enter the weight in grams: "))
                    if weight > 0:
                        caloric_load = float (input(f"Enter kcal of {ingredient_name} per 100g: "))
                        calorie_equation = float(weight * (caloric_load/100))
                        ingredient = {
                            'name':ingredient_name,
                            'weight': weight,
                            'calorie': calorie_equation
                        }
                        ingredients_added.append(ingredient)
                    else:
                        print ("\nNegative numbers are not allowed")
                except ValueError:
                    print ("Invalid input! A number must be entered.")
                except TypeError:
                    print ("Data operation not supported")
                except Exception:
                    print ("Unexpected error occured!")
                finally:
                    print ()
            else:
                print("Action aborted")
                continue

        elif ingredient_name in unique_ingr: #Repeat of line 31
            update_answer = input("Ingredient already listed, would you like to update the weight of the ingredient? (Y/N): ").capitalize()
            
            while not update_answer in ["Y","N"]:
                update_answer = input("Ingredient already listed, would you like to update the weight of the ingredient? (Y/N): ").capitalize()
            
            if update_answer == "Y":
                weight = float(input("Enter the weight in grams: "))
                if weight > 0:
                
                    for ing in ingredients_added:
                        if ing['name'] == ingredient_name:
                            calorie_equation = float(weight * (ing['calorie']/ing['weight']))
                            ing['weight'], ing['calorie'] = weight, calorie_equation
                            print (f"\nCurrent weight: {ing['weight']:g}g of {ingredient_name} \nCurrent calories: {ing['calorie']:g}kcal\n")  
                        else:
                            continue
                else:
                    print ("\nNegative numbers are not allowed")            
            #Outputs current ingredient details          
            else:
                for i_added in ingredients_added:
                    if i_added['name'] == ingredient_name:
                        print(f"\nCurrent weight: {i_added['weight']:.2fg}g of {ingredient_name} \nCurrent calories: {i_added['calorie']:g}kcal\n")
                continue
        else:
            print("Unexpected error occured")
    else:
        print (f"Unable to list {ingredient_name}")

print ("\n------------------------------------------------------------")
print ("------------------- Nutrition information ------------------")
print ("------------------------------------------------------------\n")

for ingredient in ingredients_added:
    print (f"Ingredient: {ingredient['name'].capitalize():<15} | Weight: {ingredient['weight']:>5g}g | Calorie: {ingredient['calorie']:>5g}kcal")
    total_calories += ingredient['calorie']

print (f"\nYour meal equates to a total of {total_calories:g}kcal")

