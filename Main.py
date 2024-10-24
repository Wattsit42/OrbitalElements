from multiprocessing.forkserver import set_forkserver_preload

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Structure of planetary_data
#[a,mew0,e,I,omega_bar,OMEGA,period,m/M]

#class Planet:

 #   def __init__(self,planetary_data):
 #       self.planetary_data = planetary_data
 #       self.n = 2*np.pi/(self.planetary_data[0]**(3/2))
 #       self.X = 0
 #       self.Y = 0
 #       self.Z = 0
 #       self.r = 0
 #       self.lamda0 = self.planetary_data[1]
 #       self.lamda_bar = 0 #mean longitude at epoch
 #       self.lamda = 0 #Approx replacement for theta
 #       self.beta = 0
 #       self.orbital_parameters(0)

#    def orbital_parameters(self,t):
#        e = self.planetary_data[2]
#        omega_bar = self.planetary_data[4]
#        self.lamda_bar = self.lamda0 + self.n * t
#        self.r = self.planetary_data[0]*(1 - e * np.cos(self.lamda_bar - omega_bar))
#        self.lamda = self.lamda_bar + 2 * e * np.sin(self.lamda_bar - omega_bar)
#        self.beta = self.planetary_data[3]*np.sin(self.lamda_bar - self.planetary_data[5])
#        self.X = self.r*np.cos(self.lamda)
#        self.Y = self.r*np.sin(self.lamda)
#        self.Z = self.r*self.beta


#planetary_dataset = [[0.3871,252.25,0.20564,7.006,77.46,48.34,0.241,1.659*10**-7],[0.7233,181.98,0.00676,3.398,131.77,76.67,0.615,2.447*10**-6],[1,100.47,0.01673,0,102.93,0,1,3.039*10**-6],[1.5237,355.43,0.09337,1.852,336.08,49.71,1.881,3.226*10**-7],[5.2025,34.33,0.04854,1.299,14.27,100.29,11.87,9.542*10**-4],[9.5415,50.08,0.05551,2.494,92.86,113.65,29.47,2.857*10**-4],[19.188,314.20,0.04686,0.773,172.43,73.96,84.05,4.353*10**-5],[30.070,304.22,0.00895,1.770,46.68,131.79,164.9,5.165*10**-5]]
#Planets = []
#Sets up the objects we want to operate on
#for i in range(len(planetary_dataset)):
#    planet = Planet(planetary_dataset[i])
#    Planets.append(planet)

#fig = plt.figure()
#ax = plt.axes(projection='3d')
#for t in range(0,1000):
#    ax.clear()
#    positions = [[],[],[]]
#
#    for planet in Planets:
#        positions[0].append(planet.X)
#        positions[1].append(planet.Y)
#        positions[2].append(planet.Z)
#        planet.orbital_parameters(t)

#    ax.scatter(positions[0],positions[1],positions[2],)
#    ax.set_xlim([-35, 35])
#    ax.set_ylim([-35, 35])
#    ax.set_zlim([-65, 65])
#    fig.show()

#Something was clearly going wrong up there, so let's give it another go...

class Planet:

    def __init__(self,orbital_param):
        self.orbital_param = orbital_param
        self.n = 2*np.pi/(self.orbital_param[0]**(3/2))
        self.lamda_bar0 = self.orbital_param[1]
        self.lamda = 0.0
        self.lamda_bar = 0.0
        self.pos = [0.0,0.0,0.0]
        self.set_pos(0)

    def set_pos(self,t):
        e = self.orbital_param[0]
        omega_bar = self.orbital_param[4]
        omega = self.orbital_param[5]
        self.lamda_bar = self.lamda_bar0 + self.n * t
        r = self.orbital_param[0]*(1-e*np.cos(self.lamda_bar-omega_bar))
        self.lamda = self.lamda_bar + 2*e*np.cos(self.lamda_bar-omega_bar)
        beta = self.orbital_param[3]*np.sin(self.lamda_bar-omega)
        self.pos[0] = r*np.cos(self.lamda)
        self.pos[1] = r*np.sin(self.lamda)
        self.pos[2] = r*np.cos(self.lamda-omega)

planetary_dataset = [[0.3871,252.25,0.20564,7.006,77.46,48.34,0.241,1.659*(10**-7)],[0.7233,181.98,0.00676,3.398,131.77,76.67,0.615,2.447*(10**-6)],[1,100.47,0.01673,0,102.93,0,1,3.039*(10**-6)],[1.5237,355.43,0.09337,1.852,336.08,49.71,1.881,3.226*(10**-7)],[5.2025,34.33,0.04854,1.299,14.27,100.29,11.87,9.542*(10**-4)],[9.5415,50.08,0.05551,2.494,92.86,113.64,29.47,2.857*(10**-4)],[19.188,314.20,0.04686,0.773,172.43,73.96,84.05,4.353*(10**-5)],[30.070,304.22,0.00895,1.770,46.68,131.79,164.9,5.165*(10**-5)]]
