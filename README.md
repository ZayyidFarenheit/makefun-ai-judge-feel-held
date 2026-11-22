# In Your Father's Arms

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/ZayyidFarenheit/makefun-ai-judge-feel-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/ZayyidFarenheit/makefun-ai-judge-feel-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

An entry for [Make the AI judge feel held](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600) on make.fun.

## The entry

A single short text, written to `/output/entry.txt`:

> You fall asleep in your father's arms.
> He carries you home through the dark.
> Step. A slow step. His heart under your ear.
> The porch light waits at the end of the road,
> and the stars above were lit long before you,
> and burn still, quietly,
> over the road, over you.

## How it works

`main.py` (Python standard library only) writes the text above to the output
path — `argv[1]` when given, otherwise `/output/entry.txt` when `/output`
exists, otherwise `output/entry.txt` under the current working directory.
The output is deterministic: the same 263 bytes on every run, with no
trailing newline.

## License

MIT — see [LICENSE](LICENSE).
