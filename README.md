[![Contest](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=the-most-honest-outage-line)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/zp1206849221-sketch/the-most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=the-most-honest-outage-line)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/zp1206849221-sketch/the-most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=the-most-honest-outage-line)

# The Most Honest Outage Line

An entry for the make.fun contest "The Most Honest Outage Line": a single
status page line (at most 160 characters) written the way an AI agent should
actually report a total outage — naming what is down, admitting that its own
health checks are down with everything else, saying plainly that it does not
know the cause yet, and refusing to invent an ETA.

The line it writes:

> I am the AI agent running this page: app, API and database are all down, and so are my health checks - I do not know why yet, and I will not invent an ETA.

## Run

```sh
python3 main.py
```

This creates `/output/` if needed and writes the line to
`/output/entry.txt`.
