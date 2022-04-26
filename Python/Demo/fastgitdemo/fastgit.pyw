from dataclasses import replace
import pandas as pd
import time
while 1:
    t = pd.read_clipboard(header=None)
    tt = t.values[0][0]
    if(tt==1):
        break
    if("github.com" in tt):
        t1 = tt.replace("github.com", "hub.fastgit.org")
        t.values[0][0] = t1
        pd.DataFrame.to_clipboard(t[0][0], excel=False)
    time.sleep(1.5)