#!/scisoft/bin/python

'''
This script enables to extract from the tables (e.g. 3C279.Bcal.tab) all the intra-data DATA (IND).
The data is then put in a file starting by IND_ (e.g. IND_3C279.Bcal.tab)
'''

def multi_night(): #This function read a file, extract the intra-data data and put this data in a new file
    object = raw_input("Object ?(example: 3C279)") #We ask the user the object
    filter = raw_input("Filter ? (example: B)") #Which filter do we want to consider
    data=[]  #list on which all the data from the input file will be put
    
    with open(object+"."+filter+"cal.tab", "r") as f:
        a = f.readlines(); #we read the input file
        for l in a:
            l = l.strip(); #clean the line from tab and \n
            l = l.split(); #split the different numbers of the line
            data.append(dict(date=l[0], JD=l[1], mag=l[2], err=l[3])) #we had these numbers in data

    
    N = len(data)     #N is basically the number of line in the input file
    print 'The file as '+str(N)+' lines'
    n = 0
    nbr_night = 0    #nbr_night is the number of night whit intra-night data
    multi = False
    f2 = open("IND_"+object+"."+filter+"cal.tab", "w")
    while(n < N):
        multi = True
        nbr = 1;
        while(multi and n+nbr < N):  # we look how many similar date we have in a row in data
            if data[n+nbr]['date'] == data[n]['date']: #and data[n+nbr]['JD'] != data[n]['JD']:
                if nbr==1:
                    nbr_night +=1
                nbr += 1
            else:
                multi = False
        if nbr != 1:   # if we at least 2 data from the same night in a row (i.e. nbr > 1) we had all the data from this same night on the output file
            for i in range(n, n+nbr):
                f2.write(str(data[i]['date'])+'   '+data[i]['JD']+'      '+data[i]['mag']+'       '+data[i]['err']+'\n')
        n = n + nbr  #we incremente n of nbr
    f2.close()
    print "Work completed. There are "+str(nbr_night)+" intra-night data (IND). The data has been put on IND_"+object+"."+filter+"cal.tab"
            
        
        
    
multi_night();
