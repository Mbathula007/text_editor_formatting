class Solution(object):
    
    def __init__(self,list_,length):
        
        self.max_length = length
        self.list_ = list_
        self.dp = {}
        self.memo = {}
    def cost(self,start,end):
        count = 0
        import sys
        for i in range(start,end):
            count = count + len(self.list_[i])+1
        if count > self.max_length :
            return sys.maxsize
        else :
            return (self.max_length - count)**3
    
    def text_justification_helper(self,start,n):
        import sys
        t = sys.maxsize
        k = None
        if start in self.memo :
            return self.memo[start]
        if start == n :
            return 0
        for j in range(start+1,n+1): 
            m = self.cost(start,j) + (self.text_justification_helper(j,n))
            if m < t :
                t = m
                k = j
        self.dp[start] = k
        self.memo[start] = t
        return t

    def text_justification(self):
        l = len(self.list_)
        self.text_justification_helper(0,l)
        return self.dp
    def print_string(self):
        i = 0
        while True:
            if i == len(self.list_):
                break
            t = self.dp[i]
            str_ = ""
            for i in range(i,t):
                str_ = str_ + self.list_[i] + str(" ")
            print(len(str_))
            if len(str_)<self.max_length :
                str_ = str_ + "a"*(self.max_length-len(str_))
            print('\033[94m' + str_)
        
            i = t
        

"""
x = Solution(["What","must","be","acknowledgment","shall","be"],16)
"""
s = "obvious (MS Word/Open Office) algorithm: put as many words that fit on first line repeat "
y = Solution(s.split(" "),20)
"""
print(x.text_justification())
print(x.print_string())
"""
print(y.text_justification())
print(y.print_string())