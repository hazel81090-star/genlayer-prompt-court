# GenLayer Prompt Court

A multiplayer mini-game concept for GenLayer community sessions (5–15 min rounds), where players submit answers to prompts and results are finalized with a subjective-consensus style flow.

## Mission Fit
- Multiplayer / room-based
- 5–15 min rounds
- Replayable weekly (prompt packs)
- Leaderboard + XP distribution
- Demonstrates Intelligent Contract + optimistic/dispute finalization idea

## Repo Contents
- `contracts/PromptCourt.py` – prototype game logic
- `data/prompt-packs.json` – weekly replay prompts
- `docs/architecture.md` – architecture overview
- `docs/game-rules.md` – simple rules
- `docs/troubleshooting.md` – common issues

## Run demo locally
After installing Python 3.10+:

```bash
python run_demo.py
```

You should see a sample XP leaderboard printed in terminal.

## Play it locally (interactive)
```bash
python play_cli.py
```

Then:
1. Enter player names (comma-separated)
2. Answer one random prompt per player
3. View leaderboard output

## Author
GitHub: hazel81090-star
Wallet: 0xdf5b716a7f85f6249de76EfD5779aA93baFf833c
