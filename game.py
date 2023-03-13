from random import randrange
enemy_names_list= [ 'aquiles', 'yoncleiver', 'gery', 'bryan']
enemy_attributes_list = [' he has a gun', 'he has a knife' , 'he looks like Jeffrey' , ' he knows your weaknesses']

class Hero:
    def __init__(self, name, points, rewards):
        self.name = name
        self.position = 0
        self.points = points
        self.rewards = rewards
        
    def __str__(self):
        structure = '------------------------------------------\n'
        structure += 'Hero: ' + self.name + '\n'
        structure += 'Position' + str(self.position)
        structure += 'Points: ' + str(self.points) + '\n'
        structure += 'Rewards: ' + str(self.rewards) + '\n'
        structure += '------------------------------------------\n'
        return structure
    
class Enemy:
    def __init__(self, name, position, introduction, damage):
        self.name = name
        self.position = position
        self.introduction = introduction
        self.damage = damage
        
    def __str__(self):
        structure = '_____________________________________________\n'
        structure += 'Enemy: ' + self.name + '\n'
        structure += 'Position: '+ str(self.position)
        structure += 'Introduction: '+str(self.introduction) + '\n'
        structure += 'Damage: ' + str(self.damage) + '\n'
        structure += '---------------------------------------------\n'
        return structure
    
def gaming(hero, enemies, game_lenght):
    print (' Lets start!!!')
    for play in range (1, game_lenght + 1):
        input("\n Press return to go foward. \n")
        hero.position = play
        print (hero.name + ' is in position ' + str(hero.position))
        for enemy in enemies:
            if hero.position == enemy.position:
                hero.points -= enemy.damage
                print (' You have been attacked by ' + enemy.name + ' and your damage is ' + str (enemy.damage) + ' points ')
                
            else:
                grab = randrange (10, 101)
                hero.rewards += grab
                print('Received ' + str (grab) + ' rewards')
                print('Hero total rewards: ' + str(hero.rewards))
        if hero.points <= 0:
            print ('\n' + hero.name + ' lost ')
            break
        
    if hero.points > 0:
        print('Achieved!!! ' + hero.name + ' wins!')
        
def main():
    game_lenght = 10
    hero = Hero (' TITI', 100, 10)
    qtt_enemies = randrange(int(0.3 * game_lenght), int(0.7 * game_lenght))
    enemies =[]
    for i in range(0,3):
        
        enemy_position, enemy_damage = randrange (1, game_lenght), randrange (20, 51)
        new_enemy = (Enemy(enemy_names_list[i],enemy_position, enemy_attributes_list[i], enemy_damage ))
        
        enemies.append(new_enemy)
        
        #print (hero)
    gaming(hero,enemies,game_lenght)
        
if __name__ == "__main__":
    main()