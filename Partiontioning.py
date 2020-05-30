"""QUESTION :Partitioning problem:
An arbitrary list of positive integers of any length and in any order
Determine if the list is partitionable or not. A partitioned list is one where it can be split into 2 sub-lists with equal sum. A sub-list can be any arbitrary (any set of numbers in any order) selection of numbers out of the parent list.
Enumerate the list of cases to solve to minimize execution time and provide the Order of the algorithm
Provide code showing the implementation in Python.
Example:
List = 1,2,3,4,5,6,7 = Partitionable 
List = 1,10,5,21,4 = Not Partitionable
List = 1,10,5,21,4,1 = Partitionable
Please provide the code and make sure you follow the coding standards and the time it took them to complete it."""
#SOLUTION:
#As per as my understanding if a list [x1,x2,x3,x4,x5,x6,x7] is let say Partitionable which means, say [x1,x2,x3]=x1+x2+x3 =x and [x4,x5,x6,x7]=x4+x5+x6+x7=x, which is also mean that
# x1+x2+x3+x4+x5+x6+x7 = 2x 
#So my logic will be if a list is Partionable (only two partition) only if the sum of all numbers in list is EVEN (This Way we can check that string is partionable or not)
#To generate the partionable cases the sum of numbers should be x which is (sum of all nos in list)/2

def check_partitionable(input_list):
    list_sum = sum(input_list)
    if list_sum%2 == 0:
        #print("List is Partitionable")
        return True
    else:
        #print("List is Non Partitionable")
        return False

def check_case(input_list,list_sum,list1,list2):
    if list1 is None:
        list1=[]
    result=[]
    index=0
    list_sum_chk =list_sum
    for num in input_list:
        
        list_sum_chk = list_sum_chk-num
        list1.append(num)
        #print(list2)
        list2.pop(0)
        #print(list_sum_chk)
        if list_sum_chk ==0:            
            result.append(list1)
            result.append(list2)
            
            if sum(list1) == sum(list2):
                print("List is partionable")
                print(result)
                break

        if len(str(int(list_sum_chk))) ==1:
            
            #print("list 1"+str(list1))
            #print("list 2"+str(list2))

            if list_sum_chk in list2:
                list2.remove(list_sum_chk)
                list1.append(list_sum_chk)
                result.append(list1)
                result.append(list2)
                if sum(list1)==sum(list2):

                    print("List is partionable")
                    print(result)
                    break
        
        if list_sum_chk < 0:
            new_list = input_list.copy()
            pop_elem =new_list.pop(index)
            new_list.append(pop_elem)
            check_case(new_list,list_sum,None,new_list.copy())
            break


    index= index+1
       


'Testing the code:'
#=============Inputs to be tested===============
#input_list =[1,2,3,4]
#input_list =[1,2,3,4,5,6,7]
#input_list=[1,1]
#input_list =[1,2,3]
input_list =[11,1,5,6,4,4,2,11]
#input_list=[1,10,5,21,4,1]
#input_list =[1,10,5,21,4]
#=================================================

list1 =[]
list2= input_list.copy()
summ = sum(input_list)
list_sum = summ/2



partitionable_flag =check_partitionable(input_list)
if partitionable_flag:
    #print(list_sum)
    print("input list : "+str(input_list))
    check_case(input_list,int(list_sum),list1,list2)
else:
    print("input list : "+str(input_list))
    print("String is not partionable to two sublist")


