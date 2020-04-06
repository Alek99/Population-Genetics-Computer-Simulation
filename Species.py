import Biome
import numpy as np, numpy.random
class Species:  
    def __init__(self, species_uuid, mutation_factor):
        self.uuid =  species_uuid 
        self.max_hunger = species_uuid[0][0]
        self.current_hunger = self.max_hunger
        self.speed = species_uuid[0][1]
        self.reproduction_rate = species_uuid[0][2]
        self.vision_radius = species_uuid[0][3]
        self.food_strategy = species_uuid[0][4]
        self.food_pickupsize = species_uuid[0][5]
        self.life_expectancy =  species_uuid[0][6]
        
    def setHunger(self, hunger):  
        self.current_hunger = hunger    
    def getNutri(self):      
        return self.current_hunger 

size = 100
simulation_board = Biome.BiomeGeneration(size, 5)
mutation_factor = 0

def PopulateBoard(simulation_board, size, mutation_factor):
    for i in range(size):
        for j in range(size):
            curr_tile = simulation_board[i][j]
            if curr_tile.occupation is None:
                uuid_array = np.random.dirichlet(np.ones(8),size=1)
                curr_tile.occupation = Species(uuid_array, mutation_factor)
    return simulation_board

def SimlarityCheck(uuid_array1, uuid_array2):
    diff = 0
    for i in range(len(uuid_array1[0])):
        val1, val2 = uuid_array1[0][i], uuid_array2[0][i]
        diff += abs((val1-val2)/((val1+val2)/2))
    return diff/len(uuid_array1[0])


PopulateBoard(simulation_board, size, mutation_factor)
check1 = simulation_board[0][0]
check1 =check1.occupation
check2 = simulation_board[2][2]
check2  =check2.occupation
print(check1.uuid, check2.uuid)
print(SimlarityCheck(check1.uuid, check2.uuid))

