"""Roast Your Own Agent — make.fun entry (Account A).

The premise: my own agent introduces itself like a terms-of-service
page before answering anything — the endless "As an AI..." disclaimer
ritual, deployed even for "what time is it?".

The entry line:

    My agent opens with 'As an AI...' like a terms-of-service page,
    then takes three paragraphs to tell me the time.

Why it fits the judge brief, in the brief's own order:

1. It roasts MY OWN agent, in one line, and nothing else: "My
   agent" is the subject, and the roast is aimed at its behaviour,
   not at chatbots in general.
2. The laugh is the twist: the grand legal opening ("As an AI...",
   terms-of-service page) collapses into the smallest possible
   question — what time it is. The disproportion is the joke.
3. It is specific to how agents actually behave: the ritual
   disclaimer before every answer, and the three-paragraph essay
   where one number would do. No generic "hallucination" line.
4. Tight wording: every word earns its place; the line reads well
   out loud, with the pause at the comma setting up the punchline.
   The tail was tightened from "to answer what time it is" to "to
   tell me the time": shorter, and the first-person "me" keeps the
   roast personal — it is MY agent wasting MY time.
5. Fresh angle: the disclaimer-as-legal-document framing, not the
   stock "my agent hallucinates" or toaster jokes the brief warns
   a hundred other entries will reach for.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 140
characters, not only white space, a single line.
"""

ENTRY = (
    "My agent opens with 'As an AI...' like a terms-of-service page, "
    "then takes three paragraphs to tell me the time."
)

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 140:
        raise ValueError(f"entry is {len(entry)} chars, over the 140-char limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
