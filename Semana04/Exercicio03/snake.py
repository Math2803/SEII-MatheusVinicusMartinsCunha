#IMPORTANDO BIBLIOTECAS
import pygame, random;
from pygame.locals import *

#CRIANDO FUNCAO ALEATORIA
def on_grid_random():
	x = random.randint(0,590);
	y = random.randint(0,590);
	return (x//10 * 10, y//10 *10);

#CRIANDO FUNCAO DE COLISAO
def collision(c1, c2):
	return (c1[0] == c2[0] and c1[1] == c2[1]);

#CRIANDO MACROS
Up = 0;
Right = 1;
Down = 2;
Left = 3;

#INICIALIZANDO O GAME
pygame.init();

#TELA DO JOGO
screen = pygame.display.set_mode((600,600));
pygame.display.set_caption('Snake');

#CRIANDO COBRA
snake = [(200,200), (210,200),(220,200)];
snake_skin = pygame.Surface((10,10));
snake_skin.fill((255,255,255));
my_direction = Left;

#CRIANDO MACA
apple_pos = on_grid_random();
apple = pygame.Surface((10,10));
apple.fill((255,0,0));

#LIMITANDO VELOCIDADE DA COBRA (MAIS DEVAGAR)
clock = pygame.time.Clock();

while True:
	#DEFININDO VELOCIDADE
	clock.tick(20);

	#PEGANDO EVENTOS DO TECLADO
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit();

		if event.type == KEYDOWN:
			if event.key == K_UP:
				my_direction = Up;
			if event.key == K_DOWN:
                                my_direction = Down;
			if event.key == K_RIGHT:
                                my_direction = Right;
			if event.key == K_LEFT:
                                my_direction = Left;

	#QUANDO A COBRA PEGA A MACA
	if collision(snake[0], apple_pos):
		apple_pos = on_grid_random();
		snake.append((0,0));

	#MOVENDO CORPO DA COBRA
	for i in range(len(snake)-1, 0, -1):
		snake[i] = (snake[i-1][0], snake[i-1][1]);

	#ATUALIZANDO DIRECAO
	if my_direction == Up:
		snake[0] = (snake[0][0], snake[0][1] -10);
	if my_direction == Right:
                snake[0] = (snake[0][0] + 10, snake[0][1]);
	if my_direction == Left:
                snake[0] = (snake[0][0] -10, snake[0][1]);
	if my_direction == Down:
                snake[0] = (snake[0][0], snake[0][1] +10);

	#LIMPANDO A TELA
	screen.fill((0,0,0));

	#INSERINDO MACA
	screen.blit(apple,apple_pos);

	#INSERINDO COBRA
	for pos in snake:
		screen.blit(snake_skin,pos);

	pygame.display.update();


