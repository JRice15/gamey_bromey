import math

#Interface
#Test_number=input("What number would you like to test?: ")

def output(Test_number):

    Total_digits=len(Test_number)
    Sets_A = math.ceil(int(Total_digits)/2)
    Sets_T = math.floor(int(Total_digits)/2)

    #Assigns the the Names A2, T4, A7 etc to values
    list1 = {}
    for i in range(Total_digits):

        var1=int(Test_number[i])
        if i%2==0:
            name1="a"
        else :
            name1="t"
        order1=math.floor(i/2)+1
        order1=str(order1)
        value1=name1+order1
        list1[value1]=var1

    #Defines total A's and T's
    Total_A=0
    Total_T=0
    for i in list1:
        if "a" in i:
            Total_A = list1[i]+Total_A
        else:
            Total_T = list1[i]+Total_T

    #Outputs Final t's value
    def final_t(Total_digits):
        for i in list1:
            if "t" in i and str(math.floor((int(Total_digits))/2)) in i:
                var1=list1[i]
                return var1
    final_t=(final_t(Total_digits)) 

    #Outputs Primary Value
    def primary(Total_A):
        primary=math.floor(((Total_A+1)**2)/4)
        return primary
    primary=primary(Total_A)
    #print ("    Primary: ",primary) #Extra spaces for alignment

    #Outputs Secondary Value

    if 't1' in list1.keys():
        def secondary():
            list2 = []
            for i in list1:
                if "1" in i:
                    list2.append(list1[i])
            return list2
        list2 = secondary()

        if Total_A % 2 == 0:
    #    if list1['a1'] % 2 == 0:
            var1 = math.ceil((list2[0] * list2[1])/2)
        else:
            var1 = math.floor((list2[0] * list2[1])/2)
        secondary = var1
    else:
        secondary = 0
    #print ("  Secondary: ",secondary) #Extra spaces for alignment

    #Outputs Tertiary values
    #Mostly right 

    if  't2' in list1.keys():
        def A_values(Sets_A): #Lists the numeric values of the A's
            listv = []
            for i in list1:
                if "a" in i:
                    listv.append(list1[i])
            return listv
        listv = (A_values(Sets_A))
        #print (listv)

        def multiplier(Sets_A): #Number of times each individual A will be added
            listm = []
            for j in range(1, len(listv) + 1): 
                var1 = math.floor( ( list1['t2'] + ( Sets_A - j ) ) / Sets_A )
                listm.append(var1)
            return listm
        listm = multiplier(Sets_A)
        #print (listm)


        if list1['t2'] % 2 == 0:
            listmv = [listv[i]*listm[i] for i in range(len(listv))] #multiplies above functions then sums them
            tertiary = sum(listmv)
        else:
            listsub = [1,0]
            listm = [listm[i]-listsub[i] for i in range(len(listm))]
            listmv = [listv[i]*listm[i] for i in range(len(listv))] #multiplies above functions then sums them - the last a1
            tertiary = sum (listmv) 
            tertiary += math.floor((sum(listv))/Sets_A) #adds the average of the a values, don't know why but it works
        #print (listm) #adjusted listm
    else:
        tertiary = 0 
    #print ("   Tertiary: ",tertiary) #Extra spaces for alignment

    #Outputs Quarternary Correction Value

    if  't2' in list1.keys():
        if (Total_A % Sets_A == 1) and (list1['t2'] % Sets_A == 1) and (list1['t1'] % Sets_A == 1) and (list1['a2'] % Sets_A == 0):
            quarternary = 1
        else:
            quarternary = 0
    else:
        quarternary = 0
    #print ("Quarternary: ",quarternary)

    #Outputs final value
    #print ("     Output: ",primary + secondary + tertiary + quarternary) #Extra spaces for alignment

    return primary + secondary + tertiary + quarternary

    #find out if/why total A is important