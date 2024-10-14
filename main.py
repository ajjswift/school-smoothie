#smoothies - JSON Data Set - www.101computing.net/smoothies-json-data-set
import json

print("Smoothies Recipes:")
print("--------------------")  
print("These are all the ingredients used in our selection of 20 refreshing smoothies:")      
print("Almond Butter, Almond Milk, Apple Juice, Avocado, Banana, Blueberries, Carrot, Chia Seeds, Cinnamon, Cocoa Powder, Coconut Milk, Coconut Water, Cucumber, Fresh Mint, Ginger, Greek Yogurt, Green Apple, Honey, Honeydew Melon, Kale, Kiwi, Lemon Juice, Lime Juice, Mango, Matcha Powder, Mixed Berries, Nutmeg, Oats, Orange Juice, Papaya, Peanut Butter, Pineapple, Protein Powder, Pumpkin Puree, Raspberries, Spinach, Strawberries, Turmeric.")
print("--------------------")  
print("\n") 


# load JSON data from file
file = open('smoothies.json','r')
data = json.load(file)
file.close()

smoothies = data['smoothies']


includeIngredients = []
complete = False
while not complete:
    ingredient = input('Enter an ingredient to include: ')
    if ingredient == '':
        complete = True
    else:
        includeIngredients.append(ingredient.title())


excludeIngredients = []
complete = False
while not complete:
    ingredient = input('Enter an ingredient to exclude: ')
    if ingredient == '':
        complete = True
    else:
        excludeIngredients.append(ingredient.title())

allowedSmoothies = []

for smoothie in smoothies:
    if set(includeIngredients).issubset(set(smoothie['Ingredients'])):
        allowedSmoothies.append(smoothie)

for smoothie in allowedSmoothies:
    if len(excludeIngredients) > 0:
        if set(excludeIngredients).issubset(set(smoothie['Ingredients'])):
            allowedSmoothies.remove(smoothie)

if len(allowedSmoothies) == 0:
    print('No smoothies matching your criteria found.')
else:
    print("--------------------")
    for smoothie in allowedSmoothies:
      print(smoothie["Name"])
      print(smoothie["Recipe"])
      print("--------------------")