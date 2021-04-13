from website_text_scraper import parse_text, get_kanji
from known_kanji import get_known_kanji
from prev_serach import update_prev_search_db, get_all_time_total


def print_count(kanji_count, total):

    """Prints the number of kanji in each JLPT level and percentage of said kanji out of total count."""

    print(f"Total Number of Characters: {total}")
    print(f"N5: {kanji_count[0]} ({round((kanji_count[0]/total), 4)*100}%)")
    print(f"N4: {kanji_count[1]} ({round((kanji_count[1]/total), 4)*100}%)")
    print(f"N3: {kanji_count[2]} ({round((kanji_count[2]/total), 4)*100}%)")
    print(f"N2: {kanji_count[3]} ({round((kanji_count[3]/total), 4)*100}%)")
    print(f"N1: {kanji_count[4]} ({round((kanji_count[4]/total), 4)*100}%)")
    print()


def print_unique_count(unique_kanji, unique_total):

    """Prints the number of unique kanji in each JLPT level and percentage of said kanji out of total unique count."""

    print(f"Total Number of Unique Characters: {unique_total}")
    print(
        f"N5: {len(unique_kanji['N5'])} ({round((len(unique_kanji['N5'])/unique_total), 4)*100}%)"
    )
    print(
        f"N4: {len(unique_kanji['N4'])} ({round((len(unique_kanji['N4'])/unique_total), 4)*100}%)"
    )
    print(
        f"N3: {len(unique_kanji['N3'])} ({round((len(unique_kanji['N3'])/unique_total), 4)*100}%)"
    )
    print(
        f"N2: {len(unique_kanji['N2'])} ({round((len(unique_kanji['N2'])/unique_total), 4)*100}%)"
    )
    print(
        f"N1: {len(unique_kanji['N1'])} ({round((len(unique_kanji['N1'])/unique_total), 4)*100}%)"
    )
    print()


def print_reading_ability(kanji_count, known_kanji_count):

    """Prints number and percentage of known kanji out of number of kanji per JLPT level. Does not include unique kanji."""

    print(
        f"N5: {known_kanji_count[0]} out of {kanji_count[0]} known. ({round((known_kanji_count[0]/kanji_count[0]), 4)* 100}%)"
    )
    print(
        f"N5: {known_kanji_count[1]} out of {kanji_count[1]} known. ({round((known_kanji_count[1]/kanji_count[1]), 4)* 100}%)"
    )
    print(
        f"N5: {known_kanji_count[2]} out of {kanji_count[2]} known. ({round((known_kanji_count[2]/kanji_count[2]), 4)* 100}%)"
    )
    print(
        f"N5: {known_kanji_count[3]} out of {kanji_count[3]} known. ({round((known_kanji_count[3]/kanji_count[3]), 4)* 100}%)"
    )
    print(
        f"N5: {known_kanji_count[4]} out of {kanji_count[4]} known. ({round((known_kanji_count[4]/kanji_count[4]), 4)* 100}%)"
    )


def print_all_time_total(all_time_total):

    """Prints the kanji count for each JLPT level for all previous valid searches."""

    total = 0
    for level in all_time_total[0]:
        total += level

    print(f"Total Number of Characters: {total}")
    print(f"N5: {all_time_total[0][0]}")
    print(f"N4: {all_time_total[0][1]}")
    print(f"N3: {all_time_total[0][2]}")
    print(f"N2: {all_time_total[0][3]}")
    print(f"N1: {all_time_total[0][4]}")
    print()


def print_unknown_kanji(unknown_kanji):

    """Prints kanji from URL that are not in known_kanji by JLPT level."""

    print("Unknown Kanji:")
    print()

    print("JLPT N5: ")
    print()
    for kanji in unknown_kanji["N5"]:
        print(kanji)
    print()

    print("JLPT N4: ")
    print()
    for kanji in unknown_kanji["N4"]:
        print(kanji)
    print()

    print("JLPT N3: ")
    print()
    for kanji in unknown_kanji["N3"]:
        print(kanji)
    print()

    print("JLPT N2: ")
    print()
    for kanji in unknown_kanji["N2"]:
        print(kanji)
    print()

    print("JLPT N1: ")
    print()
    for kanji in unknown_kanji["N1"]:
        print(kanji)
    print()


def get_total(kanji_count):

    """Retrieves total number of kanji from URL."""

    total = 0

    for count in kanji_count:
        total += count

    return total


def get_unique_total(unique_kanji):

    """Retrieves total number of unique kanji from URL."""

    unique_total = 0

    for key in unique_kanji:
        unique_total += len(unique_kanji[key])

    return unique_total


def reset_unique_kanji(unique_kanji):

    """Resets unique kanji count. To be used before each URL search."""

    unique_kanji["N5"] = set()
    unique_kanji["N4"] = set()
    unique_kanji["N3"] = set()
    unique_kanji["N2"] = set()
    unique_kanji["N1"] = set()


def reset_kanji_count(kanji_count):

    """Resets kanji count. To be used before each URL search."""

    for level in range(len(kanji_count)):
        kanji_count[level] = 0


# TODO: Rounding error
# TODO: Updated unknown kanji be JLPT level.


def main():
    unique_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}
    kanji_count = [0, 0, 0, 0, 0]
    known_kanji_count = [0, 0, 0, 0, 0]
    known_kanji = get_known_kanji()
    unknown_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}

    while True:
        while True:
            print("Enter URL: ")
            url = input()
            print()
            try:
                reset_unique_kanji(unique_kanji)
                reset_kanji_count(kanji_count)

                get_kanji(
                    url,
                    kanji_count,
                    unique_kanji,
                    known_kanji,
                    known_kanji_count,
                    unknown_kanji,
                )
                if (
                    kanji_count[0] == 0
                    and kanji_count[1] == 0
                    and kanji_count[2] == 0
                    and kanji_count[3] == 0
                    and kanji_count[4] == 0
                ):
                    print("URL does not contain any kanji.")
                    print()
                    continue
            except Exception:
                print("Invalid URL")
                print()
                continue
            break

        update_prev_search_db(url, kanji_count)

        total = get_total(kanji_count)
        unique_total = get_unique_total(unique_kanji)

        print_count(kanji_count, total)
        print_unique_count(unique_kanji, unique_total)

        while True:
            print(
                "(1) Print Reading Ability of URL, (2) Print Unknown Kanji from URL, (3) Print Total Number of Kanji from All Previous Searches, (4) Enter New URL, (5) Quit"
            )
            i = input()
            print()

            if i == "1":
                print_reading_ability(kanji_count, known_kanji_count)
            if i == "2":
                print_unknown_kanji(unknown_kanji)
            if i == "3":
                all_time_total = get_all_time_total()
                print_all_time_total(all_time_total)
            if i == "4":
                break
            if i == "5":
                return


if __name__ == "__main__":
    main()