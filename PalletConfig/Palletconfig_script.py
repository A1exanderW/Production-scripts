"This is a script to calculate all the possible pallet configs for shipping"

"Date: 13/05/2020, Contact: alexander.wang@bioproton.com"
"""
Assumptions: The maximum pallet size is 8*9=72
Configuration results still need to be checked that bags per layer= 6-8 with top layer 4-8
And load sizes can be evenly distributed within container
"""

total_weight = int(input('What is the total weight (kg)?\n'))
weight=int(input('What is the bag weight (kg)?\n'))
pallets=int(input('How many pallets total?\n'))
diff_btwn= int(input('What is the maximum difference between the pallet sizes allowed (kg)?\n'))


x=int(total_weight/weight)
var1=int(x/pallets)
combo=[]
for i1 in range (var1,73):
    for j1 in range (10,pallets):
        t1=i1*j1
        a1=total_weight-t1
        j2=pallets-j1
        i2=a1/j2
        t2=i2*j2
        if i2>0:     
            if abs(i1-i2)<diff_btwn and (float(i2)).is_integer():
                print("No. of bags={}, No. of pallets={}, Total bags={}".format(i1,j1,t1))
                print("No. of bags={}, No. of pallets={}, Total bags={}\n".format(int(i2),j2,int(t2)))
                combo.append(t1)
            else:
                None                
        else:
            None

print("Total combinations={}".format(len(combo)))  
                 
 
