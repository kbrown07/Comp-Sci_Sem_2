people_list = ["your dentist", "Big brother", "Small brother", "Squirrel"]
comp_list = ["is cool", "is cute", "is kind"]

import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] +  " " + comp_list[num_comp])
