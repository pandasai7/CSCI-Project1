from direct.showbase.ShowBase import ShowBase
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        SetupScene(self)
        

def SetupScene(self):

    #UNIVERSE
    self.Universe = self.loader.loadModel('./Assets/Universe/Universe.x')
    self.Universe.reparentTo(self.render)
    universeTex = self.loader.loadTexture('./Assets/Universe/universe.jpg')
    self.Universe.setTexture(universeTex, 1)
    self.Universe.setScale(15000)
    
    #PLANET-1
    self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x") #load planet model and assign to Planet1
    self.Planet1.reparentTo(self.render) #makes Planet1 a child of the camera (self.render), making it visible
    self.Planet1.setPos(1000, 1000, 2500) #Places planet at these XYZ coords
    self.Planet1.setScale(350) #sets the scale/size of the planet
    p1Tex = self.loader.loadTexture('./Assets/Planets/earth.jpg')
    self.Planet1.setTexture(p1Tex, 1)
    #PLANET-2
    self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
    self.Planet2.reparentTo(self.render)
    self.Planet2.setPos(2000, 2000, 2500)
    self.Planet2.setScale(275)
    p2Tex = self.loader.loadTexture('./Assets/Planets/saturn.jpg')
    self.Planet2.setTexture(p2Tex, 1)
    #PLANET-3
    self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
    self.Planet3.reparentTo(self.render)
    self.Planet3.setPos(3000, 3000, 2500)
    self.Planet3.setScale(500)
    p3Tex = self.loader.loadTexture('./Assets/Planets/mars.jpg')
    self.Planet3.setTexture(p3Tex, 1)
    #PLANET-4
    self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
    self.Planet4.reparentTo(self.render)
    self.Planet4.setPos(-1000, -1000, 2500)
    self.Planet4.setScale(200)
    p4Tex = self.loader.loadTexture('./Assets/Planets/purple.jpg')
    self.Planet4.setTexture(p4Tex, 1)
    #PLANET-5
    self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
    self.Planet5.reparentTo(self.render)
    self.Planet5.setPos(-2000, -2000, 2500)
    self.Planet5.setScale(150)
    p5Tex = self.loader.loadTexture('./Assets/Planets/loaf.jpg')
    self.Planet5.setTexture(p5Tex, 1)
    #PLANET-6
    self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
    self.Planet6.reparentTo(self.render)
    self.Planet6.setPos(-3000, -3000, 2500)
    self.Planet6.setScale(450)
    p6Tex = self.loader.loadTexture('./Assets/Planets/shamrock.jpg')
    self.Planet6.setTexture(p6Tex, 1)

    #DRONE DEFENDER
    self.DroneDefender = self.loader.loadModel("./Assets/Spaceships/DroneDefender/DroneDefender.x")
    self.DroneDefender.reparentTo(self.render)
    self.DroneDefender.setPos(0, 750, 0)
    self.DroneDefender.setScale(25)
    droneDefenderTex = self.loader.loadTexture('./Assets/Spaceships/DroneDefender/octotoad1_auv.png')
    self.DroneDefender.setTexture(droneDefenderTex, 1)
    
    #SPACESTATION-1B
    self.Station1B = self.loader.loadModel("./Assets/Space Station/SpaceStation1B/spaceStation.x")
    self.Station1B.reparentTo(self.render)
    self.Station1B.setPos(0, 0, -750)
    self.Station1B.setScale(25)
    station1bTex = self.loader.loadTexture('./Assets/Space Station/SpaceStation1B/SpaceStation1_Dif2.png')
    self.Station1B.setTexture(station1bTex, 1)
    
app = MyApp()
app.run()