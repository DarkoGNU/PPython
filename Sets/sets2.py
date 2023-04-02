import random

radios = {"rmf": set(), "zet": set(), "maryja": set(), "eska": set(), "dub": set(),
          "hardcore": set(), "trojka": set(), "classy": set(), "guetta": set(), "nihon": set()}
radiosSorted = list(radios.items())

states = {"dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie",
          "małopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie",
          "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie",
          "zachodniopomorskie"}

for radio in radios.values():
    while (len(radio) == 0):
        chance = random.random()
        for state in states:
            if random.random() > chance:
                radio.add(state)

        if len(radio) == 16:
            radio.pop()

print("All radios: ")
for key, value in radios.items():
    print(f"{key}: {value}")

radiosSorted = sorted(radiosSorted, key=lambda item: len(item[1]), reverse=True)
print("\n\nAll radios (sorted by coverage): ")
for key, value in radiosSorted:
    print(f"{key}: {value}")

radiosCovering = list()
uncoveredStates = states.copy()

while len(uncoveredStates) != 0 and len(radiosSorted) > 0:
    state = radiosSorted.pop(0)
    radiosCovering.append(state)
    uncoveredStates.remove(state[1])

if len(uncoveredStates) == 0:
    print("\n\nRadios required to cover whole country: ")
    for key, value in uncoveredStates:
        print(f"{key}: {value}")
else:
    print("The radios don't cover whole country")
