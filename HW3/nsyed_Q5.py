import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3


def toprelays(countries):
    print '\nList of top 5 countries hosting Tor relays'
    print '------------------------------------------'

    dictcount={}
    for country in countries:
        if country not in dictcount:
            dictcount[country]=1
        else:
            dictcount[country]+=1

    countrycount=sorted(dictcount.items(),key=lambda kv:kv[1],reverse=True)

    for item in list(countrycount)[0:5]:
        print "Country: %s\n# of Tor relays: %d" % item

def topbandwidth(routdic):
    print '\nList of top 5 bandwidth-contributing relays'
    print '-------------------------------------------'

    
    bandwidth=sorted(routdict.items(),key=lambda kv:kv[1],reverse=True)

    for item in list(bandwidth)[0:5]:
        print "Relay Node: %s\nBandwidth: %d" % item


def venndiagram(guard,exit,bandwidth):
    gnecount=0
    gcount=0
    ecount=0
    mcount=0
    gband=00
    eband=0
    gneband=0
    mband=0
    
    for gflag,eflag,kb in zip(guard,exit,bandwidth):
        if kb=='None':
            kb=0
        kb=int(kb)
        if gflag==1:
            gcount+=1
            gband+=kb
        if eflag==1:
            ecount+=1
            eband+=kb
        if gflag==1 and eflag==1:
            gnecount+=1
            gneband+=kb
        if gflag==0 and eflag==0:
            mcount+=1
            mband+=kb
        

    venn3(subsets=(gcount,ecount,gnecount,mcount,0,0,0), set_labels=('Guard','Exit','Middle'))
    plt.show()

    print '\nCumulative bandwidths'
    print '-------------------------------------------'
    print 'Bandwidth of all guard relays: %d' % gband
    print 'Bandwidth of all exit relays: %d' % eband
    print 'Bandwidth of all guard and exit relays: %d' % gneband
    print 'Bandwidth of all middle relays: %d' % mband







if __name__ == "__main__":
    filename='Tor_query_EXPORT.csv'
    df=pd.read_csv(filename)
    countries=df['Country Code']
    df['Relay'] = df['Router Name'].map(str) +" " + df['IP Address'].map(str) +" " + df['Hostname'].map(str)+" " + df['ORPort'].map(str)
    toprelays(countries)
    routers=df['Router Name']
    bandwidth=df['ConsensusBandwidth']
    routdict=df.set_index('Relay')['ConsensusBandwidth'].to_dict()
    for key,value in routdict.items():
        if routdict[key]=='None':
            routdict[key]=0
        routdict[key]=int(routdict[key])

    topbandwidth(routdict)
    guard=df['Flag - Guard']
    exit=df['Flag - Exit']

    venndiagram(guard,exit,bandwidth)

