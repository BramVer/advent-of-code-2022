"""
# DRAW
rock vs  rock
0 == 0 => 0 -> draw

scissors vs scissors
2 - 2 => 0 -> draw

paper vs paper
1 - 1 => 0 -> draw


# LOSE
rock vs  scissors
0 - 2 => -2 -> lose

paper vs  rock
1 - 0 => 1 -> lose

scissors vs paper
2 - 1 => 1 -> lose


# WIN
rock vs  paper
0 - 1 => -1 -> win

paper vs  scissors
1 - 2 => -1 -> win

scissors vs rock
2 - 0 => 2 -> win

0.3333  - A
0.6666  - B
1.0     - C
1.3333  - X
1.6666  - Y
2.0     - Z

0 == DRAW
1 == LOSE
-2 == LOSE
-1 == WIN
2 == WIN
"""


print(
    sum(
        list(
            map(
                lambda x: (
                    (
                        (
                            (globals()["chars_"].find(x[1].lower()) % 3) + 1
                        )  # start-score
                        + (
                            3
                            if globals()["score"] == 0
                            else 0
                            if globals()["score"] in (-2, 1)
                            else 6
                            if globals()["score"] in (-1, 2)
                            else __import__("pdb").set_trace()
                        )
                        if not globals().__setitem__(
                            "score",
                            (
                                (globals()["chars_"].find(x[0].lower()) % 3)
                                - (globals()["chars_"].find(x[1].lower()) % 3)
                            ),
                        )
                        else None
                    )
                    if not globals().__setitem__(
                        "chars_",
                        f"{__import__('string').ascii_lowercase[:3]}{__import__('string').ascii_lowercase[-3:]}",
                    )
                    else None
                ),
                [
                    [r for r in round_.split(" ")]
                    for round_ in __import__("pathlib")
                    .Path("data.txt")
                    .read_text()
                    .split("\n")
                ],
            )
        )
    )
)
