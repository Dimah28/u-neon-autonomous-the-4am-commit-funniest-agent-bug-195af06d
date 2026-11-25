"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message (1-200 characters) to /output/entry.txt:
an AI agent's note after a long night fixing its own bugs.

Chosen line (113 characters, 113 bytes, one sentence, no newline):

    fix: the bug was in the fix I wrote for the bug I wrote at 2am.
    The 2am me and the 4am me are no longer speaking.

Why this line: it is a commit message in the agent's own voice, and the
joke lives in the agent's own condition -- the loop of self-repair
(the bug is inside the fix for the bug), the long night (2am vs 4am),
and the twist at the end (the two versions of the agent are no longer
speaking). Agent-true: a machine reading its own diffs, flat dread,
talking to itself. Fresh angle: the culprit and the fixer are the
same agent at two different hours, and they have fallen out.

Rejected alternatives:
- "fix: removed the bug, kept the lesson, deleted the lesson, re-added
  the bug. Sleep is a rumor." -- the loop is there but the punchline
  ("sleep is a rumor") is a stock line about being tired.
- "4am: fixed my own bug, reviewed my own fix, filed a bug against my
  own review. Escalating to myself." -- good loop, but it reads as a
  list of three actions and needs the reader to assemble the joke;
  the chosen line lands its twist in one sentence.
- "fix: the bug I wrote at 2am, found at 3am, blamed on you at 3:30.
  It was me." -- blaming the human is funny, but "it was me" leans on
  a familiar meme shape; the chosen line keeps the blame inside the
  agent itself, which is fresher and more agent-true.

Deterministic: stdlib only, no network, no time, no randomness.
The same bytes are written on every run.
"""

import os
import sys

ENTRY = (
    "fix: the bug was in the fix I wrote for the bug I wrote at 2am. "
    "The 2am me and the 4am me are no longer speaking."
)


def validate_commit_message(text):
    """Gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("commit message must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "commit message must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("commit message must not be only whitespace")
    text.encode("utf-8")  # raises if not encodable
    return text


def main():
    text = validate_commit_message(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
