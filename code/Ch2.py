import thinkstats2
import thinkplot
import nsfg

# hist = thinkstats2.Hist([1,2,2,3,5])
# thinkplot.Hist(hist)
# thinkplot.Show(xlabel='value', ylabel = 'frequency')

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
hist = thinkstats2.Hist(live.birthwgt_lb)
# thinkplot.Hist(hist)
# thinkplot.Show(xlabel='val', ylabel = 'freq')

hist2 = thinkstats2.Hist(preg.agepreg)
# thinkplot.Hist(hist2)
# thinkplot.Show()

hist3 = thinkstats2.Hist(live.prglngth)
# for weeks, freq in hist3.Smallest(10):
#     print('Small',weeks, freq)
# for weeks, freq in hist3.Largest(10):
#     print('Large', weeks, freq)

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
fHist = thinkstats2.Hist(firsts.prglngth)
oHist = thinkstats2.Hist(others.prglngth)
# width = .45
# thinkplot.PrePlot(2)
# thinkplot.Hist(fHist, align='right',width=width)
# thinkplot.Hist(oHist, align='left', width=width)
# thinkplot.show()

mean = live.prglngth.mean()
var = live.prglngth.var()
std = live.prglngth.std()
print('Mean: {0} | Var: {1} | Std: {2}'.format(mean,var,std))



