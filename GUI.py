import Engine
import pygame
from Graphics_Constants import *
import random

# Initialize chess engine

init_board = "xxxxxxxxxx" \
			"xxxxxxxxxx" \
			"xrnbqkbnrx" \
			"xppppppppx" \
			"xoooooooox" \
			"xoooooooox" \
			"xoooooooox" \
			"xoooooooox" \
			"xPPPPPPPPx" \
			"xRNBQKBNRx" \
			"xxxxxxxxxx" \
			"xxxxxxxxxx"
init_board = list(init_board)
init_state = [init_board, 0, -1, 0, 1, [1,1,1,1], init_board.index('K'), init_board.index('k')]
engine = Engine.IZII()



import string

class GUI:
	def __init__(self):
		pygame.init()
		self.board = init_board
		self.size = [SCREEN_WIDTH, SCREEN_HEIGHT]
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Chess")
		pygame.mouse.set_visible(False)

		# Create our objects and set the data
		self.done = False
		self.clock = pygame.time.Clock()
		self.BackGround = Background('images/chess_board.jpg', [0, 0])
		self.score = 0
		self.game_over = False
		self.initialize_images()
		self.Move = 0
		self.i = 0
		self.current_state = init_state
		self.history = []
		pygame.display.set_caption("Chess")
		pygame.mouse.set_visible(False)

		self.coordinates = []
		for i in range(8):
			for j in range(8):
				self.coordinates.append([i + 1, j + 1])
		# print(self.self.coordinates)
		# self.turn = 0
		# self.en_passant = -1
		self.initialize_board()

	def initialize_board(self):
		screen = self.screen
		screen.fill([255, 255, 255])
		screen.blit(self.BackGround.image, self.BackGround.rect)
		for i in range(20, 120):
			xbuffer = -35
			ybuffer = -35
			sq64 = self.sq120_sq64(i)
			if self.board[i] == 'P':
				screen.blit(self.white_pawn,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'p':
				screen.blit(self.black_pawn,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'K':
				screen.blit(self.white_king,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'k':
				screen.blit(self.black_king,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'Q':
				screen.blit(self.white_queen,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'q':
				screen.blit(self.black_queen,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'R':
				screen.blit(self.white_rook,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'r':
				screen.blit(self.black_rook,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'B':
				screen.blit(self.white_bishop,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'b':
				screen.blit(self.black_bishop,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'N':
				screen.blit(self.white_knight,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'n':
				screen.blit(self.black_knight,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer,
							 self.coordinates[sq64 - 1][0] * 52 + ybuffer])
	def initialize_images(self):
		self.white_king = pygame.image.load("images/white_king.gif").convert_alpha()
		self.white_king_rect = self.white_king.get_rect()

		self.white_bishop = pygame.image.load("images/white_bishop.gif").convert_alpha()
		self.white_bishop_rect = self.white_bishop.get_rect()

		self.white_queen = pygame.image.load("images/white_queen.gif").convert_alpha()
		self.white_queen_rect = self.white_queen.get_rect()

		self.white_rook = pygame.image.load("images/white_rook.gif").convert_alpha()
		self.white_rook_rect = self.white_rook.get_rect()

		self.white_pawn = pygame.image.load("images/white_pawn.gif").convert_alpha()
		self.white_pawn_rect = self.white_king.get_rect()

		self.white_knight = pygame.image.load("images/white_knight.gif").convert_alpha()
		self.white_king_rect = self.white_knight.get_rect()

		"""black"""
		self.black_king = pygame.image.load("images/black_king.gif").convert_alpha()
		self.black_king_rect = self.black_king.get_rect()

		self.black_queen = pygame.image.load("images/black_queen.gif").convert_alpha()
		self.black_queen_rect = self.white_queen.get_rect()

		self.black_bishop = pygame.image.load("images/black_bishop.gif").convert_alpha()
		self.black_bishop_rect = self.white_bishop.get_rect()

		self.black_rook = pygame.image.load("images/black_rook.gif").convert_alpha()
		self.black_rook_rect = self.white_rook.get_rect()

		self.black_pawn = pygame.image.load("images/black_pawn.gif").convert_alpha()
		self.black_pawn_rect = self.black_king.get_rect()

		self.black_knight = pygame.image.load("images/black_knight.gif").convert_alpha()
		self.black_king_rect = self.black_knight.get_rect()

	def process_events(self):
		""" Process all of the events. Return a "True" if we need to close the window. """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			# if event.type == pygame.MOUSEBUTTONDOWN:
			# if self.game_over:
			# self.__init__()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					# all_moves = engine.get_all_moves_at_state(self.current_state)
					# if len(all_moves) == 0:
					# 	print("CHECK MATE")
					# else:
					# 	self.history.append(self.current_state)
					# 	if self.current_state[1] == 0:
					# 		n = engine.best_move(self.current_state, 3)
					# 		self.current_state = engine.run_move_at_state(self.current_state, all_moves[n])
						# else:
						#
						# 	from_sq = input("Enter from sq: ")
						# 	to_sq = input("Enter to sq: ")
						# 	from_sq64 = engine.RF_sq64(from_sq[0], int(from_sq[1]))
						# 	to_sq64 = engine.RF_sq64(to_sq[0], int(to_sq[1]))
						# 	sq120_move = [engine.sq64_to_sq120(from_sq64), engine.sq64_to_sq120(to_sq64)]
						# 	while sq120_move not in all_moves:
						# 		from_sq = input("Enter from sq: ")
						# 		to_sq = input("Enter to sq: ")
						# 		from_sq64 = engine.RF_sq64(from_sq[0], int(from_sq[1]))
						# 		to_sq64 = engine.RF_sq64(to_sq[0], int(to_sq[1]))
						# 		sq120_move = [engine.sq64_to_sq120(from_sq64), engine.sq64_to_sq120(to_sq64)]
						# 	self.current_state = engine.run_move_at_state(self.current_state, sq120_move)
						# self.board = self.current_state[0]
					return False
				if event.key == pygame.K_SPACE:
					if len(self.history) > 0:
						self.current_state = self.history.pop()
						self.board = self.current_state[0]
					return False

		return False

	def step(self):
		if not self.game_over:
			# self.done = self.process_events()
			self.process_events()
			self.display_frame(self.screen)
			self.clock.tick(2)
		if self.done is True:
			pygame.quit()

	def run_steps(self):
		while True:
			self.step()
			# all_moves = engine.get_all_moves_at_state(self.current_state)
			# if len(all_moves) == 0:
			# 	print("CHECK MATE")
			# else:
				# n = engine.best_move(self.current_state)
				# self.current_state = engine.run_move_at_state(self.current_state, all_moves[n])

		# print(root.children)
		# print("wtf: ", wtf)
		# 		self.board = self.current_state[0]
			# myisabel.run_chess()
			# self.board = myisabel.get_board()

	def sq120_sq64(self, sq):
		sq120 = []
		for i in range(120):
			# if i < 21:
			# 	sq120.append(-1)
			# if i > 100:
			# 	sq120.append(-1)
			# else:
			sq120.append(-1)
		skip = 0
		for i in range(20, 100):
			if i % 10 != 0 and (i - 9) % 10 != 0:
				sq120[i] = i - 20 - skip
			if i % 10 == 0 and i != 20:
				skip += 2
		return sq120[sq]

	def display_frame(self, screen):
		""" Display everything to the screen for the game. """



		all_moves = engine.get_all_moves_at_state(self.current_state)
		if len(all_moves) == 0:
			print("CHECK MATE")
		else:
			self.history.append(self.current_state)
			if self.current_state[1] == 1:
				n = engine.best_move(self.current_state, 3)
				self.current_state = engine.run_move_at_state(self.current_state, all_moves[n])

			elif self.current_state[1] == 0:
				# all_moves = engine.get_all_moves_at_state(self.current_state)
				from_sq = self.ask(screen, "Enter from sq: ")
				to_sq = self.ask(screen, "Enter to sq: ")
				if from_sq == -1 or to_sq == -1:
					print("undo")
				else:

					while len(from_sq) != 2 or len(to_sq) != 2:
						from_sq = self.ask(screen, "Enter from sq: ")
						to_sq = self.ask(screen, "Enter to sq: ")
					while not from_sq[1].isdigit() or not to_sq[1].isdigit():
						from_sq = self.ask(screen, "Enter from sq: ")
						to_sq = self.ask(screen, "Enter to sq: ")

					from_sq64 = engine.RF_sq64(from_sq[0], int(from_sq[1]))
					to_sq64 = engine.RF_sq64(to_sq[0], int(to_sq[1]))
					sq120_move = [engine.sq64_to_sq120(from_sq64), engine.sq64_to_sq120(to_sq64)]

					while sq120_move not in all_moves:
						from_sq = self.ask(screen, "Enter from sq: ")
						to_sq = self.ask(screen, "Enter to sq: ")
						while len(from_sq) != 2 or len(to_sq) != 2:
							from_sq = self.ask(screen, "Enter valid from sq: ")
							to_sq = self.ask(screen, "Enter to sq: ")
						while not from_sq[1].isdigit() or not to_sq[1].isdigit():
							from_sq = self.ask(screen, "Enter from sq: ")
							to_sq = self.ask(screen, "Enter to sq: ")
						from_sq64 = engine.RF_sq64(from_sq[0], int(from_sq[1]))
						to_sq64 = engine.RF_sq64(to_sq[0], int(to_sq[1]))
						sq120_move = [engine.sq64_to_sq120(from_sq64), engine.sq64_to_sq120(to_sq64)]
					self.current_state = engine.run_move_at_state(self.current_state, sq120_move)

			self.board = self.current_state[0]
		#
		# for i in range(20, 120):
		# 	xbuffer = -35
		# 	ybuffer = -35
		# 	sq64 = self.sq120_sq64(i)
		# 	if self.board[i] == 'P':
		# 		screen.blit(self.white_pawn,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'p':
		# 		screen.blit(self.black_pawn,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'K':
		# 		screen.blit(self.white_king,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'k':
		# 		screen.blit(self.black_king,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'Q':
		# 		screen.blit(self.white_queen,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'q':
		# 		screen.blit(self.black_queen,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'R':
		# 		screen.blit(self.white_rook,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'r':
		# 		screen.blit(self.black_rook,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'B':
		# 		screen.blit(self.white_bishop,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'b':
		# 		screen.blit(self.black_bishop,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'N':
		# 		screen.blit(self.white_knight,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		# 	if self.board[i] == 'n':
		# 		screen.blit(self.black_knight,
		# 					[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		screen.fill([255, 255, 255])
		screen.blit(self.BackGround.image, self.BackGround.rect)
		for i in range(20, 120):
			xbuffer = -35
			ybuffer = -35
			sq64 = self.sq120_sq64(i)
			if self.board[i] == 'P':
				screen.blit(self.white_pawn,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'p':
				screen.blit(self.black_pawn,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'K':
				screen.blit(self.white_king,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'k':
				screen.blit(self.black_king,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'Q':
				screen.blit(self.white_queen,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'q':
				screen.blit(self.black_queen,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'R':
				screen.blit(self.white_rook,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'r':
				screen.blit(self.black_rook,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'B':
				screen.blit(self.white_bishop,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'b':
				screen.blit(self.black_bishop,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'N':
				screen.blit(self.white_knight,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
			if self.board[i] == 'n':
				screen.blit(self.black_knight,
							[self.coordinates[sq64 - 1][1] * 52 + xbuffer, self.coordinates[sq64 - 1][0] * 52 + ybuffer])
		pygame.display.flip()

	def display_box(self, screen, name):
		fontobject = pygame.font.Font(None, 30)
		# NAME BOX
		pygame.draw.rect(screen, (0, 0, 0), (0, 452, 300, 30), 0)
		# pygame.draw.rect(screen, WHITE, (100, 450, 304, 34), 1)
		if len(name) != 0:
			screen.blit(fontobject.render(name, 1, (255, 255, 255)),
						(2, 460))
		pygame.display.flip()

	def ask(self, screen, question1):
		pygame.font.init()
		name = []
		self.display_box(screen, question1 + "-> " + "".join(name))
		while 1:
			inkey = self.get_key()
			if inkey == pygame.K_SPACE:
				self.current_state = self.history.pop()
				self.board = self.current_state[0]
				return -1
			if inkey == pygame.K_BACKSPACE:
				name = name[0:-1]
			elif inkey == pygame.K_RETURN:
				break
			elif inkey == pygame.K_MINUS:
				name.append("_")
			elif inkey <= 127:
				name.append(chr(inkey))
			elif inkey <= 127:
				name.append(chr(inkey))
			self.display_box(screen, question1 + "-> " + "".join(name))

		return "".join(name)
	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == pygame.KEYDOWN:
				return event.key
			else:
				pass
class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

# b = "xxxxxxxxxx" \
# 	"xxxxxxxxxx" \
# 	"xrnbqkbnrx" \
# 	"xppppppppx" \
# 	"xoooooooox" \
# 	"xoooooooox" \
# 	"xoooooooox" \
# 	"xoooooooox" \
# 	"xPPPPPPPPx" \
# 	"xRNBQKBNRx" \
# 	"xxxxxxxxxx" \
# 	"xxxxxxxxxx"
# # 0 - 9
# # 10 - 19
# # 20 - 29  20, 1, 2, 3, 4, 5, 6, 7, 8, 29
# # 30 - 39 .. 30, 9, 10, 11, 12, 13, 14, 15, 16, 39
# # 120 - 129
#
# b = list(b)



gui = GUI()
gui.run_steps()

# test_transforms()
# test_RF_sq64()
# test_sq64()
# test_sq120()
# print_full_board(b)
# test_sq64_RF()

# test_white_pawn()
# run_chess()

