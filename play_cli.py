import json
import random
from contracts.PromptCourt import PromptCourt


def load_prompts(path="data/prompt-packs.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    prompts = []
    for pack in data.values():
        prompts.extend(pack)
    return prompts


def ask_players():
    raw = input("Enter player names (comma-separated, e.g. alice,bob,carol): ").strip()
    players = [p.strip() for p in raw.split(",") if p.strip()]
    if len(players) < 2:
        print("Need at least 2 players.")
        return ask_players()
    return players


def main():
    print("=== Prompt Court CLI (Prototype) ===")
    players = ask_players()

    game = PromptCourt()
    for p in players:
        game.join(p)

    prompts = load_prompts()
    prompt = random.choice(prompts)

    print("\nRound Prompt:")
    print(f"{prompt}\n")

    print("Each player: type your answer and press Enter.")
    for p in players:
        ans = input(f"{p}'s answer: ").strip()
        if not ans:
            ans = "(no answer)"
        game.submit(p, ans)

    xp = game.finalize()

    print("\n=== Round Complete ===")
    print(f"Submissions received: {len(game.submissions)}")
    print("\nXP Leaderboard:")
    ranked = sorted(xp.items(), key=lambda kv: kv[1], reverse=True)
    for i, (player, points) in enumerate(ranked, start=1):
        print(f"{i}. {player}: {points} XP")

    print("\nTip: run again for a new random prompt.")


if __name__ == "__main__":
    main()
