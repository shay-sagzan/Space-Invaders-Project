class HitsManager:
    # Initial Variables
    enemyShoots = []
    playerShoots = []
    entities = []

    def addEntity(self, entity):
        self.entities.append(entity)

    def addEnemies(self, enemies):
        for enemy in enemies:
            self.addEntity(enemy)

    def addEnemyBullet(self, bullet, shooter):
        self.enemyShoots.append([bullet, shooter])

    def addPlayerBullet(self, bullet, shooter):
        self.playerShoots.append([bullet, shooter])

    def checkHits(self):
        def checkHitsFor(shoots, filter):
            while shoots:
                bullet, shooter = shoots.pop()
                for entity in self.entities:
                    if filter(entity) and entity.pos == bullet:
                        entity.kill()
                        self.entities.remove(entity)
                        shooter.destroyShot(bullet)
        checkHitsFor(self.enemyShoots, lambda x: not x.isAlien)
        checkHitsFor(self.playerShoots, lambda x: x.isAlien)