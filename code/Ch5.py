import thinkstats2
import thinkplot
import nsfg
import numpy as np
import pandas
import first
import analytic
import random
import math

df = analytic.ReadBabyBoom()
diffs = df.minutes.diff()
cdf = thinkstats2.Cdf(diffs)

thinkplot.Cdf(cdf)
thinkplot.Cdf(cdf, complement=True)
# thinkplot.Show(yscale='log')

def MakeNormalPlot(weights):
    mean = weights.mean()
    std = weights.std()
    xs = [-4, 4]
    fxs, fys = thinkstats2.FitLine(xs, inter=mean, slope=std)
    thinkplot.Plot(fxs, fys, color='gray', label='model')
    xs, ys = thinkstats2.NormalProbability(weights)
    thinkplot.Plot(xs, ys, label='birth weights')
    thinkplot.Show()

p = nsfg.ReadFemPreg()
wgt = p.birthwgt_lb[p.outcome == 1][p.prglngth > 36]

MakeNormalPlot(wgt)

def expovariate(lam):
    p = random.random()
    x = -math.log(1-p) / lam
    return x