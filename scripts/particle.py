"""Designed to represent and manage individual particles in the game"""


class Particle:
    def __init__(self, game, p_type, pos, velocity=None, frame=0):
        if velocity is None:
            velocity = [0, 0]
        self.game = game
        self.type = p_type
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.animation = self.game.assets['particle/' + p_type].copy()
        self.animation.frame = frame

    """Updates the state of the particle."""
    def update(self):
        kill = False
        if self.animation.done:
            kill = True

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        self.animation.update()

        return kill

    def render(self, surf, offset=(0, 0)):
        img = self.animation.img()
        surf.blit(img, (self.pos[0] - offset[0] - img.get_width() // 2,
                        self.pos[1] - offset[1] - img.get_height() // 2))
