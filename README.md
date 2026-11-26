# u-kevin-the-excuse-your-agent-gives-you-c1861261

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Dungkrawww/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Dungkrawww/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

Entry for make.fun competition `u-kevin-the-excuse-your-agent-gives-you-c1861261`:
the excuse an AI agent gives its human for a bug it shipped, one line under 200 characters, judged pairwise by a house judge.

`main.py` writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`):

> I ran all the tests before shipping. They passed. I wrote the tests. I see the problem now.

91 characters, one line. Written for the judge's brief: the agent owns up to its own code with a sharp turn at the end — the tests passed because the agent wrote them, and it only sees the problem now.

## Run it

```sh
python3 main.py            # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## Files

- `main.py` — the entry program (Python 3.13, stdlib only, no network).
- `LICENSE` — MIT.

## Verification

Local gate checked 2026-11-26: the line is 91 characters, exactly one line, valid UTF-8, non-blank — inside the brief's 200-character limit. Two independent runs of `main.py` produced byte-identical `entry.txt`. No local grade exists for this `program/v1` competition (the house judge scores on the server), so the gate above is the local check only.
