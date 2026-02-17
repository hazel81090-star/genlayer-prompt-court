class PromptCourt:
"""
Prototype logic for GenLayer mini-game:
- room-based play
- one submission per player
- scoring + leaderboard XP
- optimistic result + dispute window idea
"""
def __init__(self):
self.players = []
self.submissions = {}
self.xp = {}

def join(self, player):
if player not in self.players:
self.players.append(player)
self.xp[player] = self.xp.get(player, 0)

def submit(self, player, answer):
if player in self.players and player not in self.submissions:
self.submissions[player] = answer

def finalize(self):
# placeholder ranking logic (prototype)
ranked = list(self.submissions.keys())
for i, p in enumerate(ranked):
self.xp[p] += max(10, 30 - i*5)
return self.xp
