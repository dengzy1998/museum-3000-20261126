"""Museum of the Year 3000 — make.fun entry.

The entry line (see LINE below) is the label a museum in the year 3000
puts beside an ordinary object from today — a plastic fork. Running this
file writes that line, byte-exact with no trailing newline, to
/output/entry.txt.

Duel record (proxy judge: openai/gpt-oss-120b via Groq, using the verbatim
judge brief from the kit's RULES.txt; every pair judged in both orders,
verdicts as VERDICT: A/B MARGIN: 1-5):

Candidates (all one sentence, <=200 chars, original):
  A  House key — "Citizens carried a small metal tooth everywhere..."
  B  Parking meter — "Citizens fed coins to this box to rent a patch of ground..."
  C  Plastic fork — "A single-use eating tool, discarded after one meal; scholars
     still debate whether humans ate with it or worshipped it." (141 chars)
  D  Kitchen sponge — "A soft yellow brick, soaked daily in food and soap..."
  E  Phone charger — "A lifeline tether humans slept beside..."
  F  Group chat — "A room with no walls where forty people talked at once..."

Results:
  Round 1:  A vs B split 1-1 (margin 3 each way).
            C beat D 2-0 (margin 3, 3).
            E beat F 1-0 (margin 5; the return leg failed on a transient
            Groq error and was not retried — the judge had already ruled
            F off-subject under criterion 1, a group chat being no object).
  Semi:     C beat E 2-0 (margin 3, 3) — the fork's "worshipped it" twist
            read fresher than the charger-lifeline gag.
  Final:    C vs B split 1-1 (margin 3 each way): the fork won one leg on
            immediacy ("worshipped it" lands on first read), the meter won
            the other on freshness.

Champion: C, the plastic fork. It won the tournament on overall record
(5 legs won, 1 lost — the best of the field; the meter went 2-2), with the
sharpest single punch ("scholars still debate whether humans ate with it
or worshipped it") and the cleanest deadpan-curatorial voice.

Note: several Groq calls failed transiently with an error response carrying
no 'choices' (intermittent API-side errors, not a prompt problem) and were
retried; the recorded verdicts above are all from successful calls.
"""

import os

LINE = (
    "Plastic fork, c. 2024. A single-use eating tool, discarded after one "
    "meal; scholars still debate whether humans ate with it or worshipped it."
)


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" keeps the written bytes identical on every platform:
    # exactly LINE, with no trailing newline added.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
