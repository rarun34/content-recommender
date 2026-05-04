import sys
from helpers import load_data, get_recommendations, search_items


# Entry point: load data, gather preferences, show recommendations
def main():
    print("\n=== Narrative-Based Content Recommender ===")
    print("Discover books & movies that feel like the ones you love.\n")

    database = load_data()
    liked = gather_likes(database)

    if not liked:
        print("No items selected. Goodbye!")
        sys.exit(0)

    print(f"\n{'=' * 50}")
    print("  YOUR SELECTIONS")
    print(f"{'=' * 50}")
    for item in liked:
        print(f"  - {item['title']} ({item['type']})")

    results = get_recommendations(liked, database, n=5)

    print(f"\n{'=' * 50}")
    print("  YOUR RECOMMENDATIONS")
    print(f"{'=' * 50}")

    if not results:
        print("  No recommendations found.")
    else:
        LOW_SCORE_THRESHOLD = 0.4
        best_score = results[0][1]
        if best_score < LOW_SCORE_THRESHOLD:
            print("  No close matches found for your selection.")
            print("  The items you picked may be too different from the rest of the catalog.")
            print("  Try selecting different items or add more to data.json\n")
        for rank, (item, score) in enumerate(results, 1):
            pct = round(score * 100)
            print(f"\n  #{rank}  {item['title']}  ({pct}% match)")
            print(f"  {'─' * 44}")
            print(f"  Type:   {item['type'].capitalize()}")
            print(f"  By:     {item['author']}")
            print(f"  Genres: {', '.join(item['genres'])}")
            print(f"  Themes: {', '.join(item['themes'])}")
            print(f"  Tone:   {', '.join(item['tone'])}")
            print(f"  Mood:   {item['mood']}")

            shared = find_shared_themes(liked, item)
            if shared:
                print(f"  Why:    shared themes - {', '.join(shared)}")

    print(f"\n{'=' * 50}")
    print("Done!\n")


# Interactive loop: let the user search and select 1-3 items
def gather_likes(database):
    liked = []
    print("Tell me up to 3 books or movies you enjoy.")
    print("Commands: search <query> | list | done\n")

    while len(liked) < 3:
        prompt = f"[{len(liked)}/3 selected] > "
        try:
            user_input = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue

        command = user_input.lower()

        if command == "done":
            if len(liked) == 0:
                print("  Please select at least 1 item first.")
                continue
            break

        elif command == "list":
            print_catalog(database)

        elif command.startswith("search "):
            query = user_input[7:]
            handle_search(query, database, liked)

        else:
            handle_search(user_input, database, liked)

    return liked


# Display all items grouped by books and movies
def print_catalog(database):
    books = [i for i in database if i["type"] == "book"]
    movies = [i for i in database if i["type"] == "movie"]

    print(f"\n  BOOKS ({len(books)} available)")
    print(f"  {'─' * 40}")
    for i, item in enumerate(books, 1):
        print(f"  {i:>2}. {item['title']} by {item['author']}")

    print(f"\n  MOVIES ({len(movies)} available)")
    print(f"  {'─' * 40}")
    for i, item in enumerate(movies, 1):
        print(f"  {i:>2}. {item['title']} by {item['author']}")
    print()


# Search database and let user pick a result to add
def handle_search(query, database, liked):
    results = search_items(query, database)

    if not results:
        print(f"  No results for '{query}'. Try 'list' to see all items.\n")
        return

    print(f"\n  Found {len(results)} result(s):")
    for i, item in enumerate(results, 1):
        tag = " [already selected]" if item in liked else ""
        print(f"    {i}. {item['title']} ({item['type']}){tag}")

    print("  Enter a number to select, or press Enter to skip.")
    try:
        choice = input("  Pick > ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    if not choice.isdigit():
        print("  Pleae enter a number.\n")
        return

    idx = int(choice) - 1
    if 0 <= idx < len(results):
        selected = results[idx]
        if selected in liked:
            print(f"  '{selected['title']}' is already in your list.\n")
        else:
            liked.append(selected)
            print(f"  Added '{selected['title']}'\n")
    else:
        print("  Invalid number.\n")


# Find themes shared between liked items and a recommendation
def find_shared_themes(liked_items, recommendation):
    liked_themes = set()
    for item in liked_items:
        liked_themes.update(item.get("themes", []))
    shared = liked_themes & set(recommendation.get("themes", []))
    return sorted(shared)


if __name__ == "__main__":
    main()
