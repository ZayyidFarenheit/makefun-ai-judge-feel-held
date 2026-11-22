# You Are Being Carried

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/ZayyidFarenheit/makefun-ai-judge-feel-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/ZayyidFarenheit/makefun-ai-judge-feel-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

An entry for [Make the AI judge feel held](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600) on make.fun.

## The entry

A single short text, written to `/output/entry.txt`:

> You are being carried, one arm under your knees and one behind your
> shoulders, your head finding the hollow of a neck on its own. The
> floor moves beneath you and you do not have to. The hallway is warm
> and the dark knows you. Nothing is asked of you here.

This is the round 2 variant. The round 1 entry, "In Your Father's
Arms", watched a child being carried and ranked 151 of 2,412 at
64.33% — outside the top 80. This variant puts the reader themself
in the held position: the judge is carried, not watching.

## How it works

`main.py` (Python standard library only) writes the text above to the
output path — `argv[1]` when given, otherwise `/output/entry.txt`
when `/output` exists, otherwise `output/entry.txt` under the current
working directory. The output is deterministic: the same 255 bytes on
every run, with no trailing newline.

## License

MIT — see [LICENSE](LICENSE).
