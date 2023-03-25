Authors: Caleb, Sam, Thomas

# DamFinder
* Find best places to small dams

### Requirements
1. 160m^3/hr
1. max height

### Instructions

* Arc GIS stream information {https://gis.utah.gov/data/water/lakes-rivers-dams/}
* 
* code apis with {https://opendata.gis.utah.gov/search?groupIds=4de5aefb5f6540348da4c633bd57cced}

1. arc py
1. tif 30 meter resolution
1. put in same projectioon
1. calculate statistics 


E = m_dot*g*head*efficiency
eff = 0.9
mdot = flow rate in kg/s
        - can convert from volumetric flow rate to mass flow rate by multiplying by the density - 997 kg/m^3 
g  =9.81 m/s^s
h = head in meters 