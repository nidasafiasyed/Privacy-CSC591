
from adblockparser import AdblockRules
import pandas as pd
from tld import get_tld
from prettytable import PrettyTable

raw_rules=[]
with open('easylist.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        raw_rules.append(currentPlace)


rules = AdblockRules(raw_rules)
#mimetype = ['script','image','stylesheet','object','subdocument','xmlhttprequest','websocket','webrtc','popup','generichide','genericblock']

x = PrettyTable()

filenames=['macys.csv','cnn.csv','bankofamerica.csv']

x.field_names = ["Site", "Total HTTP Requests", "HTTP Requests Blocked", "3rd party domains blocked"]
for csvfile in filenames:
    site=csvfile.replace("csv", "com")
    l=[]
    total=0
    blocked=0
    unblocked=0
    df=pd.read_csv(csvfile)
    domains=df[df.columns[1]]
    mime=df[df.columns[5]]
    for domain,m in zip(domains,mime):
        options={}
        total+=1
        if (m.find('image')):
            options['image']=True
        else:
            options['image']=False
        if (m.find('javascript')):
            options['script']=True
        else:
            options['script']=False

        if rules.should_block(domain,options) == True:
            res = get_tld(domain, as_object=True)
            
            if (res.fld.find(site)==-1):
                if res.fld not in l:
                    l.append(res.fld.encode('utf-8'))

            blocked+=1
        else:
            unblocked+=1

    strdom = '\n'.join(l)

    x.add_row([site, total, blocked, strdom])
print(x)
