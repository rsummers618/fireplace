from ..utils import *


##
# Minions

# Cogmaster
class GVG_013:
	def atk(self, i):
		if self.controller.field.filter(race=Race.MECHANICAL):
			return i + 2
		return i


# Stonesplinter Trogg
class GVG_067:
	events = [
		Play(OPPONENT, SPELL).on(Buff(SELF, "GVG_067a"))
	]


# Burly Rockjaw Trogg
class GVG_068:
	events = [
		Play(OPPONENT, SPELL).on(Buff(SELF, "GVG_068a"))
	]


# Antique Healbot
class GVG_069:
	action = [Heal(FRIENDLY_HERO, 8)]


# Ship's Cannon
class GVG_075:
	events = [
		Summon(CONTROLLER, PIRATE).on(Hit(RANDOM_ENEMY_CHARACTER, 2))
	]


# Explosive Sheep
class GVG_076:
	deathrattle = [Hit(ALL_MINIONS, 2)]


# Mechanical Yeti
class GVG_078:
	deathrattle = [GiveSparePart(ALL_PLAYERS)]


# Clockwork Gnome
class GVG_082:
	deathrattle = [GiveSparePart(CONTROLLER)]


# Madder Bomber
class GVG_090:
	action = [Hit(RANDOM_CHARACTER, 1) * 6]


# Piloted Shredder
class GVG_096:
	def deathrattle(self):
		return [Summon(CONTROLLER, randomCollectible(type=CardType.MINION, cost=2))]


# Tinkertown Technician
class GVG_102:
	def action(self):
		if self.poweredUp:
			return [Buff(SELF, "GVG_102e"), GiveSparePart(CONTROLLER)]


# Micro Machine
class GVG_103:
	# That card ID is not a mistake
	events = [
		TURN_BEGIN.on(Buff(SELF, "GVG_076a"))
	]
