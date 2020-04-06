import Terrain 
import numpy as np
import random as r 
class Square:  
    def __init__(self, elevation, variance, lat, lon, size, precip):    
        # Attributes of a Biome/Tile
        #Positoning of Biome
        self.occupation = None
        self.lat = lat - size/2
        self.lon = lat
        self.elevation = elevation 
        #Physical Attributes
        elevation_constant = 100 - elevation - 40*abs(size/2 - lat)/(size/2)
        self.temp = 1.2 * r.uniform(elevation_constant-variance, elevation_constant+variance)
        self.precipitation = precip
        #Vegitation and Sustainability
        self.max_nutri =  (self.temp/2 + self.precipitation)
        self.regen_nutri = self.precipitation/2 + self.temp
        
    # Retrieves instance variables: Biome   
    def setOccupation(self, species):  
        self.species = species     
    def getOccupation(self):      
        return self.species
    # Retrieves instance variables: Nutritional Value   
    def setNutri(self, nutri):  
        self.nutri = nutri      
    def getNutri(self):      
        return self.nutri  
    


def BiomeGeneration(size, variance):  
    terrain_array = Terrain.terrain_generation(size) 
    precip_array = Terrain.terrain_generation(size) 
    simulation_board = [[0 for x in range(size)] for y in range(size)] 
    n = [[0 for x in range(size)] for y in range(size)]
    for lat in range(size):
        for lon in range(size):
            simulation_board[lat][lon] = Square(terrain_array[lat][lon], variance, lat, lon, size, precip_array[lat][lon])
            ex = simulation_board[lat][lon]
            n[lat][lon] = ex.precipitation

    
    return simulation_board

