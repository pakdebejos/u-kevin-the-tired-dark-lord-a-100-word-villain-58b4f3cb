"""Pay the Toll: a tired villain's monologue, about 100 words.

The program writes one monologue - about 100 words, at most 600
characters (484 characters) - to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR
locally, /output in the grader). The text is a fixed constant with no
trailing newline, so both of the grader's runs write byte-identical output.
"""
import os

LINE = "Pay the toll. Yes, the same toll. I have stood on this bridge for three hundred years and the river has never once paid me back. You want passage? Then listen. I keep the ledgers, I mend the planks, I feed the toll-goat, and still the carts come at dawn. The last hero left a sock. I keep it. I once dreamed of a throne. Now I dream of a chair. A chair, and a door that locks, and one whole night without a knock. Cross, then. But leave a coin for the goat. He works harder than I do."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
