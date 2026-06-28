'''
Given two arrays with unique numbers, arr1 and arr2, find whether there exists an array, 
arr3 which has arr1 and arr2 both as its subsequence and arr3 has all unique numbers. 
Return true or false.
Example:

Sample 1:
arr1 = [2, 3, 5, 1]
arr2 = [4, 3, 5, 1, 9]
Ans: true
arr3 could be [2, 4, 3, 5, 1, 9]

Sample 2:
arr1 = [2, 3, 5, 1]
arr2 = [2, 3, 1, 5]
Ans: false

1st attempt - flawed solution
class solution:
    def unique_supersequence (self, arr1,arr2):
        print("function called")
        print (arr1)
        print(arr2)
        arr3 = arr1[:]
        j=-1
        for i in range (len(arr2)):
            if arr2[i] in arr3[j+1:]:
                j = arr3.index(arr2[i])
            elif j == -1:
                arr3.insert(0,arr2[i])
            else:
                arr3.insert(j+1,arr2[i])
        
        return len(arr3) == len(set(arr3))

if __name__ == "__main__":
    solver = solution()
    print("begin solution")
    print (solver.unique_supersequence([2, 3, 5, 1],[4, 3, 5, 1, 9]))
    print (solver.unique_supersequence([2, 3, 5, 1],[2, 3, 1, 5]))
    print (solver.unique_supersequence([2, 3, 5, 1],[2, 3, 5, 5]))

'''
class solution:
    def unique_supersequence(self,arr1,arr2):
        common_list = list ( set(arr1) & set(arr2))
        print(common_list)
        id1=[]
        id2=[]
       
        for i in common_list:
            id1.append(arr1.index(i))
            id2.append(arr2.index(i))
        # srt_id1 = sorted(id1)
        # srt_id2 = sorted(id2)
        print(id1,'\n',id2)
        # return (id1 == srt_id1 and id2== srt_id2)
        

if __name__ == "__main__":
    solver = solution()
    print("begin solution")
    print (solver.unique_supersequence([2, 3, 5, 1],[4, 3, 5, 1, 9]))
    print (solver.unique_supersequence([2, 3, 5, 1],[2, 3, 1, 5]))
    # print (solver.unique_supersequence([2, 3, 5, 1],[2, 3, 5, 5]))

