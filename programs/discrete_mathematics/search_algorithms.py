i_list = []
j_list = []
m_list = []

def binary_search(list_to_search, target):
    x = target
    i = 1
    #i_list.append(i)

    j = len(list_to_search)
    #j_list.append(j)

    while i < j:
        m = int(int(i+j)/2)

        i_list.append(i)
        j_list.append(j)
        m_list.append(m)

        if(list_to_search[m] < x):
            i = m + 1
        else:
            j = m

    #temporary solution because I don't know what's wrong
    i_list.append(i+1)
    j_list.append(j+1)

    #m_list.append(m)
    if x == list_to_search[m]:
        return i
    else:
        return 0

list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

# put letter to search here
print(binary_search(list, 'Y') + 1)
'''
print(i_list)
print(j_list)
print(m_list)
'''

print("i\tj\tai\taj\tm\tam")
i=0
#print(j_list[i])
#print(list[j_list[i]-1])
while i < len(m_list):
    print(str(i_list[i]) + "\t"
    + str(j_list[i]) + "\t"
    + list[i_list[i]-1] + "\t"
    + list[j_list[i]-1] + "\t"
    + str(m_list[i]) + "\t"
    + list[m_list[i]-1])
    i += 1
print(str(i_list[i]) + "\t" + str(j_list[i]))