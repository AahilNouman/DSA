class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while(n!=1):
            if n in a:
                return False
            a.add(n)
            sums=0
            while(n>0):
                dig=n%10
                sums+=dig*dig
                n=n//10
            n=sums
        return True