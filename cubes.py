import pygame

pygame.init() 
screen = pygame.display.set_mode((900,300))
pygame.display.set_caption("Momentum")

class cube:
	def __init__(self,colour,width,x,y,mass,vel):
		self.colour = colour;
		self.width = width;
		self.x = x;
		self.y = y;
		self.mass = mass;
		self.vel = vel;
		self.clack = pygame.mixer.Sound('clack.wav');
		self.clack.set_volume(0.1)
		self.count = 0;

	def drawcube(self):
		pygame.draw.rect(screen, self.colour, (self.x,self.y, self.width,self.width));

	def move(self):	
		self.x += self.vel;		

	def collide(self, other):
		if not(self.x + self.width < other.x or self.x> other.x + other.width):
			pygame.mixer.Sound.play(self.clack);
			self.count += 0.5;
			print(int(self.count));			
			initv1 = self.vel;
			initv2 = other.vel;
			self.vel = ( ((self.mass - other.mass) / (self.mass + other.mass))*initv1 + ((2*other.mass)/ (self.mass + other.mass))*initv2);
			other.vel = ( ( (2*self.mass) / (self.mass + other.mass) )*initv1 + ((other.mass - self.mass)/(self.mass + other.mass))* initv2);			

	def wall(self):
		if self.x < 100:
			self.vel = self.vel * -1;
			pygame.mixer.Sound.play(self.clack);
			self.count+=1;
			print(int(self.count));




big_cube = cube((0,200,160), 70,500,200,  1  ,-0.08);
small_cube = cube((0,160,200), 40,250,230,1,0);
running = True;

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False;


	screen.fill((0,0,0));
	pygame.draw.rect(screen, (255,255,255), (95,0,5,270));
	pygame.draw.rect(screen, (255,255,255), (95,270,900,5));
	big_cube.drawcube();
	big_cube.move();
	small_cube.drawcube();
	small_cube.move();
	small_cube.collide(big_cube);
	big_cube.collide(small_cube);
	small_cube.collide(big_cube);
	small_cube.wall();
	pygame.display.update();



pygame.quit();