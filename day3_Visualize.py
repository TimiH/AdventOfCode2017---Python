import day3 as d
import pandas as pd

a = [x for x in range(1,1000001)]
b =[d.steps(x) for x in range(1,1000001)]
df = pd.DataFrame(a, columns=['N'])
df["Steps"] = b
df.plot(x='N',y='Steps')
