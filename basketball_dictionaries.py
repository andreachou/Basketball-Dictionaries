# Challenge 1: Update the Constructor

"""

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.

"""
# player list
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

class Player:
    
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    def display_player_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        


Kevin = Player(players[0])
Kevin.display_player_info() # output: Kevin Durant, 34, small forward, Brooklyn Nets

Jason = Player(players[1])
Jason.display_player_info() # output: Jason Tatum, 24, small forward, Boston Celtics




# Challenge 2: Create instances using individual player dictionaries.

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

class Player:
    
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    def display_player_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)


# Create your Player instances here!
# player_jason = ???
player_jason = Player(jason["name"], jason["age"], jason["position"], jason["team"])
player_jason.display_player_info()




# Challenge 3: Make a list of Player instances from a list of dictionaries

class Player:
    new_team = []

    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        self.new_team.append(self)  # add the object to new_team list



player_michael = Player("Michael", 32, "PG", "Bull")
player_kobe = Player("Kobe", 28, "PG", "Lakers")

for player in Player.new_team:
    print(player.name)





# NINJA BONUS: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.

class Player:
    new_team = []

    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        self.new_team.append(self)

    @classmethond
    def get_team(cls, team_list):




player_michael = Player("Michael", 32, "PG", "Bull")
player_kobe = Player("Kobe", 28, "PG", "Lakers")

for player in Player.new_team:
    print(player.name)