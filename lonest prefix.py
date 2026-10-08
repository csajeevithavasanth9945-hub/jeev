def longest_prefix(lists):
    long_prefix=""
    shortest=min(len(lists[0]),len(lists[1]),len(lists[2]))
    for i in range(shortest):
        if lists[0][i]==lists[1][i]==lists[2][i]:
            long_prefix+=lists[0][i]
        else:
            break
    return long_prefix
    #print(long_prefix)             
            
lists=["flower",'flo',"flonadaze"]
print(longest_prefix(lists))