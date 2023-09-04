# Kích thước window, FPS của game
from typing import Self


class GameConstants:
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600
	FPS = 60


# Kích thước sprite zombie, số zombie tối đa cùng lúc
class ZombieConstants:

	# Tọa độ từng frame trên sprite map zombie

	ZOM_SPRITE_1 = [19, 16, 80, 90]
	ZOM_SPRITE_2 = [190, 25, 100, 100]
	ZOM_SPRITE_3 = [367, 25, 95, 100]
	ZOM_SPRITE_4 = [558, 25, 96, 100]
	ZOM_SPRITE_5 = [741, 25, 90, 100]
	ZOM_SPRITE_6 = [901, 23, 88, 102]

class GraveConstants:
	GRAVE_NUM_MAX = 10		# Số lượng mộ tối đa
	# Tọa độ các mộ trên background image

	LIST_HOLE = []

	LIST_HOLE.append([120,120])
	LIST_HOLE.append([280,220])
	LIST_HOLE.append([400,100])
	LIST_HOLE.append([650,170])
	LIST_HOLE.append([120,360])
	LIST_HOLE.append([360,330])
	LIST_HOLE.append([520,400])
	LIST_HOLE.append([620,280])

class HammerConstants:
	HAMMER_ANGLE = 45	# Khi đập búa, sprite nghiêng 1 góc 45 độ như hiệu ứng đập

class FontConstants:
	FONT_NAME = "./Resources/fonts/ZOMBIE.ttf"
	FONT_SIZE = 52
	FONT_SIZE_BIG = 64

# Các text hiển trị trên màn hình
class TextConstants:
	GAME_TITLE = "Whack A Zombie"

	TEXT_COLOR = [255, 255, 255]	# White

class ImageConstants:
	IMAGE = "./Resources/images/"	# Folder chứa ảnh
	ICON = IMAGE + "thor.png"
	IMAGE_START = IMAGE + "start.png"
	IMAGE_BUTTON_0 = IMAGE + "button0.png"
	IMAGE_BUTTON_0_HOVER = IMAGE + "button0_hover.png"
	IMAGE_BG = IMAGE + "background.png"
	IMAGE_GAMEOVER = IMAGE + "gameover.png"
	IMAGE_BUTTON_1 = IMAGE + "button1.png"
	IMAGE_BUTTON_2 = IMAGE + "button2.png"
	IMAGE_HAMMER = IMAGE + "hammer.png"
	IMAGE_ZOMBIE = IMAGE + "zombie.png"
	IMAGE_BRAIN	= IMAGE + "brain.png"
	IMAGE_HOLE = IMAGE + "Hole_5.png"

class SoundConstants:
	SOUND = "./Resources/sounds/"	# Folder chứa file audio
	SOUND_BG = SOUND + "music_bg.mp3"
	SOUND_HIT = SOUND + "hit.wav"
	SOUND_MISS = SOUND + "miss.wav"
	SOUND_LEVEL_UP = SOUND + "level_up.wav"

class Constants(GameConstants, ZombieConstants, GraveConstants, HammerConstants, FontConstants, TextConstants, ImageConstants, SoundConstants):
	LEFT_MOUSE_BUTTON = 1

