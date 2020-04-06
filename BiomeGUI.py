import Biome
import matplotlib.pyplot as plt
import numpy as np
size = 100

simulation_board = Biome.BiomeGeneration(size, 5)
ele = [[0 for x in range(size)] for y in range(size)]
for lat in range(size):
        for lon in range(size):
            ex = simulation_board[lat][lon]
            ele[lat][lon] = ex.elevation
plt.figure(0)
plt.imshow(ele,'jet')
plt.title('Elevation')
plt.colorbar()

precip = [[0 for x in range(size)] for y in range(size)]
for lat in range(size):
        for lon in range(size):
            ex = simulation_board[lat][lon]
            precip[lat][lon] = ex.precipitation
plt.figure(1)
plt.imshow(precip,'Blues')
plt.title('Precipitation')
plt.colorbar()

temp = [[0 for x in range(size)] for y in range(size)]
for lat in range(size):
        for lon in range(size):
            ex = simulation_board[lat][lon]
            temp[lat][lon] = ex.temp

plt.figure(2)
plt.imshow(temp,'hot')
plt.title('Temperature')
plt.colorbar()


nutri = [[0 for x in range(size)] for y in range(size)]
for lat in range(size):
        for lon in range(size):
            ex = simulation_board[lat][lon]
            nutri[lat][lon] = ex.max_nutri
plt.figure(3)
plt.imshow(nutri,'ocean_r')
plt.title('Nutrition')
plt.colorbar()
plt.show()
