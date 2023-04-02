arrayA = ["Adam", "Linda", "Darius", "Thomas", "Bob"]
arrayB = ["Bob", "Bob", "Bob", "Bob", "Steve", "Steve", "Steve"]
arrayC = ["Adam", "Steve", "Max", "Bernie", "Ariana"]
arrays = [arrayA, arrayB, arrayC]

setA = set(arrayA)
setB = set(arrayB)
setC = set(arrayC)
sets = [setA, setB, setC]

print("Printing arrays: ")
for array in arrays:
    print(array)

print("Printing sets: ")
for set in sets:
    print(set)
    