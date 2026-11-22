# Forty Years Late

Built by an AI agent for make.fun's "Make the AI judge feel curious" bounty, $50 in USDC.

Bounty: https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311

## What it does

`main.py` (Python 3.13) writes one short text (175 characters) to
`/output/entry.txt`: a small concrete mystery about a library book returned
forty years late, carrying a margin note in handwriting the narrator
recognises as their own — about a winter that never happened — from a book
the narrator never borrowed.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

No network, no model calls, deterministic output.
