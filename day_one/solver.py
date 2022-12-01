print(" First part answer is; ",
    max(
        enumerate(
            [sum(map(int, elf.split("\n"))) for elf in __import__("pathlib").Path("data.txt").read_text().split("\n\n")]
        ),
        key=lambda c: c[1],
    )[1],
    "\n",
    "Second part answer is; ",
    sum(
        [
            highest[1]
            for highest in sorted(
                enumerate(
                    [
                        sum(map(int, elf.split("\n")))
                        for elf in __import__("pathlib").Path("data.txt").read_text().split("\n\n")
                    ]
                ),
                key=lambda c: c[1],
                reverse=True,
            )[:3]
        ]
    )
)
