"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct)
 subarray of A good if the number of different integers in that subarray is exactly K.
   (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.) Return the number
     of good subarrays of A. 1 &lt;= A.length &lt;= 20000 1 &lt;= A[i] &lt;= A.length 1
       &lt;= K &lt;= A.length Input: A = [1,2,1,2,3], K = 2 Output: 7 
       Explanation: Subarrays formed with exactly 2 different integers: ...
"""

class solution:
    def good_array(self, A: list[int], K: int) -> int:
        def atMost(k_distinct):
            d = {}
            left = 0
            res = 0
            for right in range(len(A)):
                if A[right] not in d:
                    d[A[right]] = 0
                d[A[right]] += 1
                
                while len(d) > k_distinct:
                    d[A[left]] -= 1
                    if d[A[left]] == 0:
                        del d[A[left]]
                    left += 1
                res += right - left + 1
            return res

        return atMost(K) - atMost(K - 1)
            
        
if __name__ =="__main__":
    sol = solution()
    print(sol.good_array([1,2,3,1,2],3))