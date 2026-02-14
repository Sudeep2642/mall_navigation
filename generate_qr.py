import qrcode

locations = [
    "Entrance",
    "Lift",
    "Food Court",
    "Nike Store",
    "Zara",
    "Restroom",
    "Exit"
]

for loc in locations:
    img = qrcode.make(loc)
    img.save(f"{loc}.png")
