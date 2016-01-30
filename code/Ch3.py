import thinkstats2
import thinkplot
import nsfg
import numpy as np
import pandas

pmf = thinkstats2.Pmf([1,1,2,2,2,3,4,7])
# print(pmf.Total())
# print(pmf)
width = .45
h = thinkplot.Pmf(pmf)
preg = nsfg.ReadFemPreg()
first = preg.birthord[preg.birthord == 1]
other = preg.birthord[preg.birthord != 1]
first_pmf = thinkstats2.Pmf(first)
other_pmf = thinkstats2.Pmf(other)
# thinkplot.PrePlot(2, cols=2)
# thinkplot.Hist(first_pmf, align='right', width=width)
# thinkplot.Hist(other_pmf, align='left', width=width)
# thinkplot.Config(xlabel='weeks',ylabel='probability',axis=[27, 46, 0, 0.6])
# thinkplot.PrePlot(2)
# thinkplot.SubPlot(2)
# thinkplot.Pmfs([first_pmf, other_pmf])
# thinkplot.Show(xlabel='weeks',axis=[27, 46, 0, 0.6])
# thinkplot.show()

array = np.random.randn(4,2)
df = pandas.DataFrame(array)
print(df)
df.columns = ['A','B']
df.index = ['a','b','c','d']
a = df.loc['a']
z = df.iloc[0]
y = df['a':'c']
u = df[0:3]

def meanPMFOthers():
    s = 0.0
    for val in other_pmf:
        s += val * other_pmf[val]
    return s

def variancePMFOthers():
    s = 0
    mean = meanPMFOthers()
    for val in other_pmf:
        s += other_pmf[val] * np.square(val-mean)
    return s

