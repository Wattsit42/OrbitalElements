import numpy as np
import matplotlib.pyplot as plt

def rad_convert(angle):
    return (np.pi/180)*angle

class Planet:

    def __init__(self,orbital_param):
        self.orbital_param = orbital_param
        self.pos = [0.0,0.0,0.0]
        self.n = 2*np.pi/(self.orbital_param[0]**(3/2)) #I define n in this scope as I don't want to be calculating it every time I run the set_pos function

    def set_pos(self,t):
        a = self.orbital_param[0]
        lamda0 = rad_convert(self.orbital_param[1])
        e = self.orbital_param[2]
        w_bar = rad_convert(self.orbital_param[4])
        lamda_bar = lamda0 + self.n * t
        r = a*(1-e*np.cos(lamda_bar - w_bar))
        lamda = lamda_bar + 2*e*np.sin(lamda_bar - w_bar)
        self.pos[0] = r*np.cos(lamda)
        self.pos[1] = r*np.sin(lamda)
        self.pos[2] = r*rad_convert(self.orbital_param[3])*np.sin(lamda_bar-rad_convert(self.orbital_param[5]))

planetary_dataset = [[0.3871,252.25,0.20564,7.006,77.46,48.34,0.241,1.659*(10**-7)],[0.7233,181.98,0.00676,3.398,131.77,76.67,0.615,2.447*(10**-6)],[1,100.47,0.01673,0,102.93,0,1,3.039*(10**-6)],[1.5237,355.43,0.09337,1.852,336.08,49.71,1.881,3.226*(10**-7)],[5.2025,34.33,0.04854,1.299,14.27,100.29,11.87,9.542*(10**-4)],[9.5415,50.08,0.05551,2.494,92.86,113.64,29.47,2.857*(10**-4)],[19.188,314.20,0.04686,0.773,172.43,73.96,84.05,4.353*(10**-5)],[30.070,304.22,0.00895,1.770,46.68,131.79,164.9,5.165*(10**-5)]]
#[0.3871,252.25,0.20564,7.006,77.46,48.34,0.241,1.659*(10**-7)],[0.7233,181.98,0.00676,3.398,131.77,76.67,0.615,2.447*(10**-6)],[1,100.47,0.01673,0,102.93,0,1,3.039*(10**-6)],[1.5237,355.43,0.09337,1.852,336.08,49.71,1.881,3.226*(10**-7)],[5.2025,34.33,0.04854,1.299,14.27,100.29,11.87,9.542*(10**-4)],[9.5415,50.08,0.05551,2.494,92.86,113.64,29.47,2.857*(10**-4)],[19.188,314.20,0.04686,0.773,172.43,73.96,84.05,4.353*(10**-5)],[30.070,304.22,0.00895,1.770,46.68,131.79,164.9,5.165*(10**-5)]
# List for reference incase I want to remove any.
Planets = []

for i in range(len(planetary_dataset)):
    planet = Planet(planetary_dataset[i])
    Planets.append(planet)

fig = plt.figure()
ax = plt.axes(projection='3d')
time = np.linspace(0,164,100)
for t in time:
    #ax.clear() #Include if we just want the current positions
    positions = [[],[],[]]

    for planet in Planets:
        positions[0].append(planet.pos[0])
        positions[1].append(planet.pos[1])
        positions[2].append(planet.pos[2])
        planet.set_pos(t)

    ax.scatter(positions[0],positions[1],positions[2],)
    # ax.set_xlim([-35,35]) # Used to produce the 1:1:1 scaling
    # ax.set_ylim([-35,35])
    # ax.set_zlim([-35,35])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

fig.show()



