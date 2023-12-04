import re
import string

blueprint = []
max_geodes = []

class Blueprint:
    def __init__(self, ore_cost, clay_cost, obs_cost, geode_cost):
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obs_cost = [obs_cost[0], obs_cost[1]]
        self.geode_cost = [geode_cost[0], geode_cost[1]]

def parse():
    f = open('input.txt')
    lines = f.readlines()
    for line in lines:
        chars_removed = re.sub('\D', ' ', line)
        data = chars_removed.split()
        blueprint.append(Blueprint(int(data[1]), int(data[2]), [int(data[3]), int(data[4])], [int(data[5]), int(data[6])]))

parse()

# blueprint is a list of all blueprints
# answer is the sum of max geodes for a blueprint times its 1-indexed blueprint id for all blueprints

# program flow: function to calculate max geodes for a 24-min run of a blueprint
#               call this function for each blueprint (pass blueprint as argument) and add answer to max_geodes
#               output sum += max_geodes[i] * (i + 1)
# 
# geodes function:
                
                
