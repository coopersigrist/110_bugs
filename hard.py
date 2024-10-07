# Goal: Fix the code so that it works correctly
# set a break point on line 20 and start to explore
import random

# Should get a random number (1 - 9) for each player
def get_nums(player_ids):
    rand_list=[]
    for i in range(len(player_ids)):
        rand_list.append(random.randint(1, 10))
    return rand_list

def play_game():
    num_players = int(input("How many players:"))
    player_ids = list(range(num_players))
    while len(player_ids) > 1:
        nums = get_nums(player_ids)
        max_score = max(nums)
        print(f" The scores for the players with ids {player_ids} is {nums}")
        index = 0
        for id in player_ids:
            if nums[index] != max_score:
                player_ids.remove(id)
            index += 1
                    
    print(f"The player with id {player_ids[0]} wins!")

play_game()