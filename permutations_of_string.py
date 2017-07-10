"""

"a" -> "a"

"ab" -> "ab", "ba"

"abc" -> "cab", "acb", "abc", "cba", "bca", "bac"

"""


class Solution(object):
    def get_perms(self, stp):
        """
        :type stp: string
        """
        
        # stp is the string to permute
                
        # base case, there is nothing to permute,
        # simply return the single character string
        if len(stp) == 1:
            return stp
        
        # cpl = current permutation list
        cpl = []
        
        # chop off last char stp(n), find all perms of s1 to s(n-1)
        # insert last char into every position of the string
        # sp = string permutation
        last = stp[-1]
        
        for sp in self.get_perms(stp[:-1]):
            i=0
            while i < len(sp):
                cpl.append ( sp[:i] + last + sp[i:] )
                i+=1
            cpl.append(sp + last)
        
        return cpl
    
    
def main():
    
    solution = Solution()
    
     
    print(str(solution.get_perms("abcd")))
    
    
if __name__ == '__main__':
    main()