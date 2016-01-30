import thinkstats2
import thinkplot
import nsfg
import numpy as np
import pandas
import first

p = nsfg.ReadFemPreg()
wgt = thinkstats2.Pmf(p.totalwgt_lb)

# first = p.birthord[p.birthord == 1]
# other = p.birthord[p.birthord != 1]
# live = p[p.outcome == 1]
# first = thinkstats2.Pmf(first)
live, firsts, others = first.MakeFrames()

# CDFLength = thinkstats2.Cdf(p.prglngth)
cdf = thinkstats2.Cdf(live.prglngth)

cdf1 = thinkstats2.Cdf(firsts.totalwgt_lb, label = 'first')
cdfo = thinkstats2.Cdf(others.totalwgt_lb, label = 'others')
thinkplot.PrePlot(2)
thinkplot.Cdfs([cdf1, cdfo])
thinkplot.Show()