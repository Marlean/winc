# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_firstgoal = 'Ruud Gullit'
player_secondgoal = 'Marco van Basten'


goal_0 = 32
goal_1 = 54

scorers = player_firstgoal + " " + str(goal_0) + ", " + player_secondgoal + " " + str(goal_1)

print(scorers)

report = f'{player_firstgoal} scored in the {goal_0}nd minute\n{player_secondgoal} scored in the {goal_1}th minute'

print(report)

player = 'Ronald Koeman'

end_first_name = player.find(' ') 
print(end_first_name)

first_name = player[:end_first_name]
print(first_name)

start_last_name = (player.find(' ') + 1)
print(start_last_name)

last_name = player[start_last_name:]
print(last_name)

last_name_len = len(last_name)
print(last_name_len)

#name_short should be R. Koeman
name_short = f'{player[0]}. {last_name}'
print(name_short)

chanted_name = first_name + "! "
print(chanted_name)

chant = chanted_name * len(first_name)  
chant = chant[:-1]
print(chant)

good_chant = chant[-1] != " "
print(good_chant)

print(2 != 3)
print(2 != 2)
