spin = input()
charge = input()

particles = [
    {"name": "Strange", "class": "Quark", "spin": "1/2", "charge": "-1/3"},
    {"name": "Charm", "class": "Quark", "spin": "1/2", "charge": "2/3"},
    {"name": "Electron", "class": "Lepton", "spin": "1/2", "charge": "-1"},
    {"name": "Neutrino", "class": "Lepton", "spin": "1/2", "charge": "0"},
    {"name": "Photon", "class": "Boson", "spin": "1", "charge": "0"}
]

for particle in particles:
    if spin == particle["spin"] and charge == particle["charge"]:
        print(f"{particle['name']} {particle['class']}")
