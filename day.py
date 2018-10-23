#Ranin


import sys
month=(sys.argv[1])
day=int(sys.argv[2])



dict={'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}

def day_year(dict,month,day):
    sumofmonth=0
    for i in dict:
        x=dict[i]
        sumofmonth+=x
        if i==month:
            return sumofmonth-(dict[i]-day)
print(day_year(dict,month,day))            
