from skyfield.api import load

#Creates timescale and asks current time
ts = load.timescale()
t = ts.now()

planets = load('de421.bsp')

mars = planets['mars barycenter']
barycentric = mars.at(t)