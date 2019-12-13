class Moon():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.dx = 0
        self.dy = 0
        self.dz = 0

    def apply_gravity(self,other):
        if(other.x < self.x):
            self.dx+=-1
        if(other.x > self.x):
            self.dx+=1
        if(other.y < self.y):
            self.dy+=-1
        if(other.y > self.y):
            self.dy+=1
        if(other.z < self.z):
            self.dz+=-1
        if(other.z > self.z):
            self.dz+=1

    def pot_energy(self):
        return abs(self.x)+abs(self.y)+abs(self.z)

    def kin_energy(self):
        return abs(self.dx)+abs(self.dy)+abs(self.dz)
    
    def tot_energy(self):
        return self.pot_energy() * self.kin_energy()


    def simualte(self):
        self.x+=self.dx
        self.y+=self.dy
        self.z+=self.dz
        
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return str([self.x,self.y,self.z])


moons = [Moon(6,10,10),
        Moon(-9,3,17),
        Moon(9,-4,14),
        Moon(4,14,4)]

for i in range(1000):
    for moon in moons:
        for other in moons:
            moon.apply_gravity(other)

    for moon in moons:
        moon.simualte()

    print(moons[1].x)

energy = 0
for moon in moons:
    energy+=moon.tot_energy()

print(energy)

for moon in moons:
    print(moon)