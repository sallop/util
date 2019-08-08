#/usr/bin/env python
# -*- encoding: utf-8 -*-

import subprocess
import time
import itertools

import datetime

DIFF_JST_FROM_UTC = 9

utc_now = datetime.datetime.utcnow()
now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
# diff = now - utc_now # datetime.delta

denom = 3
delta = datetime.timedelta(days=1) / denom

timeslice = [(utc_now + delta*i).isoformat() for i in range(4)]

for t in timeslice:
    print(t)

template = "start={0}\n  end={1}"
periods = []
for i, start in enumerate(timeslice[:-1]):
    end = timeslice[i+1]
    period = template.format(start, end)
    # str.format(**kw)
    periods.append(period)

for period in periods:
    print(period)
