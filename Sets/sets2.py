import random

radios = {"rmf": set(), "zet": set(), "maryja": set(), "eska": set(), "dub": set(),
          "hardcore": set(), "trojka": set(), "classy": set(), "guetta": set(), "nihon": set()}

states = {"dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie",
          "małopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie",
          "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie",
          "zachodniopomorskie"}

for radio in radios.values():
    chance = random.random()
    for state in states:
        if random.random() > chance:
            radio.add(state)

    if len(radio) == 16:
        radio.pop()

print("All radios: ")
for key, value in radios.items():
    print(f"{key}: {value}")
