# Exercise 1
arrayA = ["Adam", "Linda", "Darius", "Thomas", "Bob", "Steve"]
arrayB = ["Bob", "Bob", "Bob", "Bob", "Steve", "Steve", "Steve", "James"]
arrayC = ["Adam", "Steve", "Max", "Bernie", "Ariana"]
arrays = [arrayA, arrayB, arrayC]

print("Printing arrays: ")
for array in arrays:
    print(array)

# Exercise 2
setA = set(arrayA)
setB = set(arrayB)
setC = set(arrayC)
sets = [setA, setB, setC]

print("\nPrinting sets: ")
for set in sets:
    print(set)

# Exercise 3

print("\nNames both in A and B: ")
print(setA.intersection(setB))

print("\nNames both in A, B, and C: ")
print(setA.intersection(setB).intersection(setC))

print("\nNames in C (but not in A): ")
print(setC.difference(setA))

print("\nNames in B (but not in A and C): ")
print(setB.difference(setA.intersection(setC)))

print("\nNames from all sets: ")
print(setA.union(setB).union(setC))

print("\nNames in A, but not in sum of B and C: ")
print(setA.difference(setB.union(setC)))
