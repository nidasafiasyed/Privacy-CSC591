import pandas as pd
from tld import get_tld
import networkx as nx
import matplotlib.pyplot as plt

def getdomains(domains,csvfile):
    site=csvfile.replace("csv", "com")
    print("-------------------")
    print("Site: "+site)
    print("-------------------")
    print "List of third party domains: "
    l=[]
    for domain in domains:
        res = get_tld(domain, as_object=True)
        if (res.fld.find(site)==-1):
            if res.fld not in l:
                l.append(res.fld)

    for item in l:
        print item

    generategraph(site,l)


def generategraph(site,domains):
    G = nx.Graph()
    G.add_node(site)
    G.add_nodes_from(domains)
    for domain in domains:
        G.add_edge(site, domain)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
        

    

if __name__ == "__main__":
    filenames=['macys.csv','cnn.csv','bankofamerica.csv']
    for csvfile in filenames:
        df=pd.read_csv(csvfile)
        domains=df[df.columns[1]]
        getdomains(domains,csvfile)


    
    #for key,value in graph.items():
    #    print key,value

    #df1=pd.read_csv('macys.csv')
    #df2=pd.read_csv('cnn.csv')
    #df3=pd.read_csv('bankofamerica.csv')
    #domain1=df1[df1.columns[2]]
    #domain2=df2[df2.columns[2]]
    #domain3=df3[df3.columns[2]]
    #print set(domain1).intersection(set(domain2)) 

