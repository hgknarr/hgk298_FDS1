def mean(userlist) :
    return round(sum(userlist)/len(userlist), 2)

def var(userlist) :
    s = 0
    for i in userlist:
        s = s + (i-mean(userlist))**2
    return round(s/len(userlist), 2)

def sd(userlist) :
    return round(var(userlist)**0.5, 2)

def se(userlist) :
    return round(sd(userlist)/((len(userlist))**0.5),2)

def zscore(userlist) :
    newnumber = int(input("enter a new observation: \n"))
    return round((newnumber - mean(userlist))/sd(userlist), 2)

def summary(userlist) :
    return print("mean = ", mean(userlist), "\n", "variance = ",
                 var(userlist), "\n", "standard deviation =",
                 sd (userlist), "\n", "standard error =", se(userlist))

def options() :
    print("[1]enter a new series of numbers", "\n",
      "[2]compute the mean", "\n",
      "[3]compute the variance", "\n",
      "[4]compute the standard deviation", "\n",
      "[5]compute the standard error", "\n",
      "[6]compute the z-score of a new observation", "\n",
      "[7]give a summary of the statistics", "\n")
