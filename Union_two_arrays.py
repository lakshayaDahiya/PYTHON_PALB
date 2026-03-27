
class Solution:    
    def findUnion(self, a, b):
        arr=[]
        for i in range(len(a)):
            for j in range(len(b)):
                    if a[i]==b[j]:
                        if a[i] not in arr:
                             arr.append(a[i])
                    if a[i] not in arr:
                        arr.append(a[i])
                    elif b[j] not in arr:
                        arr.append(b[j])
        return arr
                    
a = list(map(int, input("Enter first array elements: ").split()))
b = list(map(int, input("Enter second array elements: ").split()))

sol = Solution()
result = sol.findUnion(a,b)
print(result)



# for GFG:-
# class Solution:
#     def findUnion(self, a, b):
#         s = set()
        
#         for x in a:
#             s.add(x)
#         for x in b:
#             s.add(x)
            
#         return sorted(s)
