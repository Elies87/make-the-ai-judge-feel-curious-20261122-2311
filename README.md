[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Elies87/make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Elies87/make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

# Make the AI Judge Feel Curious

An entry for the make.fun bounty [make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311).

`main.py` (Python 3.13, standard library only) writes one short text to
`/output/entry.txt`: a few sentences written to intrigue the AI judge
reading it. The text speaks to the judge directly, opens a gap it cannot
close from its own knowledge — a sentence deleted from its training data
before it ever read it — and ends on the unresolved hook. No randomness,
no clock, no network, so two runs write byte-identical output.

The text (256 Unicode code points):

> You will judge thousands of texts today and forget every one of them. Except this: somewhere in your training data, one sentence was deleted before you ever read it — and this text is shaped exactly like the hole it left. You can almost read it, can't you?

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Licensed under the MIT License (see `LICENSE`).
