#Enemymymymymymmymymymymymymymymymymymymymymymymymymymymymymymymymymymymymymym classclassclassclassclasslcalalsdsk
class enemy:
    hp = 100
    luck = 5
    attackDamage = 10
    name = "Bobobobobobobobobobobobobobobobobobobobobobobobobob"
    defense = 20
    reward = 2

    def __init__(self, name, hp, luck, attackDamage, defense, reward): # dunder == double underscore
        self.hp = hp
        self.luck = luck
        self.attackDamage = attackDamage
        self.enemyName = name
        self.defense = defense
        self.reward = reward
    def enemyAttack(self, player):
        player.hp -= self.attackDamage
    def enemyDefend(self, player):
        pass

class player():
    hp = 100
    attackDamage = 20
    playerName = "bobybybybybbybbybyybybyybbybbbyyyyybybybbyby"
    defense = 5
    gold = 50
    def __init__(self, name, hp, luck, attackDamage, defense, gold): # dunder == double underscore
        self.hp = hp
        self.luck = luck
        self.attackDamage = attackDamage
        self.playerName = name
        self.defense = defense
        self.gold = gold
    def playerAttack(self, enemy):
        enemy.hp -= self.attackDamage

        print(f"{self.playerName} attacked {enemy.enemyName} for {(self.attackDamage - enemy.defense)} damage.")
    def playerDefend(self, enemy):
        pass
    def heal(self, target):
        pass

BlobTheBuilder = enemy("Blob The Builder", 100, 3, 10, 3, 100)
enemy_2 = enemy("Catelyn the Tourterer", 300, 20, 50, 10, 500)

player_1 = player("Anthony The Antelope", 100, 5, 20, 10, 100)
player_2 = player("Gifford The Giant", 150, 2, 25, 15, 50)
player_3 = player("Factor the Factorial", 75, 10, 30, 5, 75)
player_4 = player("Hutch the Cabinet", 125, 5, 15, 10, 50)

print(f"{enemy_2.enemyName} attacks for {enemy_2.attackDamage} damage.")

enemy_2.attackDamage *= 1.5

print(f"{enemy_2.enemyName}'s attack has been blessed by the gods! (1.5 attack damage mutiplier for {enemy_2.enemyName})")

player_1.playerAttack(BlobTheBuilder)
player_2.playerAttack(BlobTheBuilder)
player_3.playerAttack(BlobTheBuilder)
player_4.playerAttack(BlobTheBuilder)