import json
import time

elements = json.loads(open("Elements.json", "r").read())

forumla_original = input("Input a chemical formula:\t")
processed_forumla = forumla_original.replace(" ", "").split("+")

new_formula = []
item_counter = 0
subset_counter = 0
for subset in processed_forumla:

    new_formula.append([""])
    
    for letter in subset:

        if letter.isupper():
            new_formula[subset_counter][item_counter] += letter

        elif letter.islower():
            new_formula[subset_counter][item_counter] += letter
            new_formula[subset_counter].append("")
            item_counter +=1

    subset_counter += 1

startTime = time.time()
print(new_formula)
print(f"\n[Process took {time.time() - startTime} seconds]")