class EffectController:
    particleDummy = None

    def __init__(self):
        self.track = None
        self.startEffect = None
        self.endEffect = None
        self.f = None
        self.p0 = None


    def createTrack(self):
        pass


    def destroy(self):
        #print 'default - destroy'
        self.finish()
        if self.f:
            self.f.cleanup()

        self.f = None
        self.p0 = None
        self.removeNode()
        
    def destroyRain(self):
        #print 'rainObj - destroy'
        self.finish()
        if self.f:
            self.f.cleanup()

        self.f = None
        self.p0 = None
        self.detachNode()
        
    def cleanUpRain(self):
        #print 'rainObj - cleanUpEffect'
        if self.f:
            self.f.disable()

        self.removeNode()


    def cleanUpEffect(self):
        #print 'default - cleanUpEffect'
        self.setPosHpr(0, 0, 0, 0, 0, 0)
        if self.f:
            self.f.disable()

        self.detachNode()


    def reallyCleanUpEffect(self):
        self.cleanUpEffect()
        self.finish()


    def play(self, lod = None):
        if lod != None:

            try:
                self.createTrack(lod)
            except TypeError:
                e = None
                raise TypeError('Error loading %s effect.' % self.__class__.__name__)


        self.createTrack()
        self.track.start()


    def stop(self):
        if self.track:
            self.track.pause()

        if self.startEffect:
            self.startEffect.pause()

        if self.endEffect:
            self.endEffect.pause()

        self.cleanUpEffect()


    def finish(self):
        if self.track:
            self.track.pause()

        if self.startEffect:
            self.startEffect.pause()

        if self.endEffect:
            self.endEffect.pause()



    def startLoop(self, lod = None):
        if lod != None:

            try:
                self.createTrack(lod)
            except TypeError:
                e = None
                raise TypeError('Error loading %s effect.' % self.__class__.__name__)


        self.createTrack()
        if self.startEffect:
            self.startEffect.start()



    def stopLoop(self):
        if self.startEffect:
            self.startEffect.pause()
            self.startEffect = None

        if self.endEffect and not self.endEffect.isPlaying():
            self.endEffect.start()



    def getTrack(self):
        if not self.track:
            self.createTrack()

        return self.track


    def enableEffect(self):
        if self.f and self.particleDummy:
            self.f.start(self, self.particleDummy)
        elif self.f:
            self.f.start(self, self)



    def disableEffect(self):
        if self.f:
            self.f.disable()
