from contracts.PromptCourt import PromptCourt


def main():
    game = PromptCourt()

    # players join
    for p in ["alice", "bob", "carol", "dave"]:
        game.join(p)

    # one round of submissions
    game.submit("alice", "Use bounded voting and dispute windows for fairness.")
    game.submit("bob", "Combine AI scoring with transparent human challenge steps.")
    game.submit("carol", "Weekly rotating prompts keep replayability high.")
    game.submit("dave", "Add anti-spam and one-submission-per-player rules.")

    # finalize + print leaderboard
    xp = game.finalize()

    print("=== Prompt Court Demo Complete ===")
    print("Players:", ", ".join(game.players))
    print("Submissions:", len(game.submissions))
    print("\nXP Leaderboard:")

    ranked = sorted(xp.items(), key=lambda kv: kv[1], reverse=True)
    for i, (player, points) in enumerate(ranked, start=1):
        print(f"{i}. {player}: {points} XP")


if __name__ == "__main__":
    main()
