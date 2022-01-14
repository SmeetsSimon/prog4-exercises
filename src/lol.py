videokaarten = [
    {
        "merk": "NVIDIA",
        "naam": "RTX 3080",
        "architectuur": "Ampere",
        "geheugen": 10,
        "busbreedte": 320,
        "diesize": 628,
    },
    {
        "merk": "AMD",
        "naam": "RX 6800",
        "architectuur": "RDNA 2",
        "geheugen": 16,
        "busbreedte": 256,
        "diesize": 520,
    },
]

for i in videokaarten:
    print(i["merk"])