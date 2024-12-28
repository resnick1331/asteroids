# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, bullets)
	
	print("Starting asteroids!")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	asteroid_field = AsteroidField()
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for i in updatable:
			i.update(dt)

		for a in asteroids:
			if a.collision(player):
				print("Game Over!")
				sys.exit()
			for b in bullets:
				if a.collision(b):
					a.split()
					b.kill()

		pygame.Surface.fill(screen, (1,1,1))
		
		for d in drawable:
			d.draw(screen)

		pygame.display.flip()

		dt= clock.tick(60) /1000
		


if __name__ == "__main__":
    main()
