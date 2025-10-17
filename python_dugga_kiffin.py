# Part_1_Dugga
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

sum_abs = 0
for num in numbers:
   if abs(num) >= 10:
          sum_abs += num
  #      print(sum_abs)
print(f'Sum:{sum_abs}')

cube_list=[]
for num in numbers:
    if num < 0:
        cube_list.append(num*num*num)
        #print(f'{cube_list}')
        
print(f'List of negative numbers cubed: {cube_list}' )


abs_list = []
checked = []
first_repeat = None

for num in numbers:
    num_abs = abs(num)
    abs_list.append(num_abs)
    #print(f'{abs_list}')
    if num_abs in checked:
            first_repeat = num_abs
            break
    else:
        checked.append(num_abs)
print (first_repeat if first_repeat is not None else "No repeats" )

#Used AI to check the code.Intital code was re-looping through abs_list inside the outer loop


##Part 2##
import csv
import sys
import pandas as pd 
import matplotlib.pyplot as plt

input_file = sys.argv[1]

df = pd.read_csv(input_file, sep=',')
#print(f'{df}')

def histogram():
    plt.figure(figsize=(10, 6))
    plt.hist (df['fpkm_log2'], bins =5)
    plt.xlabel('Expression')
    plt.ylabel('Number of genes')
    plt.title('Distribtion of gene expression')
    plt.savefig('fpkm_distribution.png')
    plt.show()
    return

hist_fpkm = histogram()

#Forgot to add plt.show(). Used AI to catch that
