import matplotlib.pyplot as plt
import numpy as np

curva_carga = [
    0.40,  # 00h
    0.35,  # 01h
    0.30,  # 02h
    0.28,  # 03h
    0.30,  # 04h
    0.40,  # 05h
    0.55,  # 06h
    0.70,  # 07h
    0.75,  # 08h
    0.65,  # 09h
    0.60,  # 10h
    0.68,  # 11h
    0.80,  # 12h
    0.75,  # 13h
    0.70,  # 14h
    0.68,  # 15h
    0.72,  # 16h
    0.78,  # 17h
    0.90,  # 18h
    0.95,  # 19h
    0.92,  # 20h
    0.85,  # 21h
    0.70,  # 22h
    0.55   # 23h
]

fig, ax = plt.subplots()
x = np.arange(0,24,1)

plt.plot(x,curva_carga)
plt.grid(True)
plt.show()