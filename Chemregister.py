import json
import time

def formulaProcessor(old_formula):
    new_formula = []
    item_counter = 0
    subset_counter = 0
    letter_counter = 0
    for subset in old_formula:
        new_formula.append([""])
        for letter in subset:
            try:
                if subset[letter_counter+1].isupper():
                    new_formula[subset_counter][item_counter] += letter
                    new_formula[subset_counter].append("")
                    item_counter += 1
                else:
                    new_formula[subset_counter][item_counter] += letter
            except:
                new_formula[subset_counter][item_counter] += letter
            letter_counter += 1
        item_counter = 0
        letter_counter = 0
        subset_counter += 1
    return new_formula

def elementConverter(formula, Elements):
    for subset in range(len(formula)):
        for element in range(len(formula[subset])):
            try:
                formula[subset][element] = Elements[formula[subset][element]]["element name"]
            except:
                pass
    return formula


Elements = json.loads(open("Elements.json", "r").read())

original_formula = input("Input a chemical formula:\t")
processed_formula = elementConverter(formulaProcessor(original_formula.replace(" ", "").split("+")), Elements)

startTime = time.time()
print(processed_formula)
print(f"\n[Process took {float(time.time() - startTime)} seconds]")
