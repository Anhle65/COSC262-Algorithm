
def lcs(s1, s2, cache = None):
    if cache == None:
        cache = {}
    if s1 == "" or s2 == "":
        cache[(len(s1), len(s2))] = ""
        return ""
    elif s1[-1] == s2[-1]:
        cache[(len(s1), len(s2))] = lcs(s1[:-1], s2[:-1], cache) + s1[-1]
    else:
        if (len(s1), len(s2)) in cache:
            return cache[(len(s1), len(s2))]
        longer = None
        soln1= lcs(s1[:-1], s2, cache)
        soln2= lcs(s1, s2[:-1], cache) 
        if len(soln1) > len(soln2):
            longer = soln1
        else:
            longer = soln2
        cache[(len(s1), len(s2))] = longer
    return cache[(len(s1), len(s2))]
        

        
# A simple test that should run without caching
s1 = "abcde"
s2 = "qbxxd"
lcs_string = lcs(s1, s2)
print(lcs_string)
# s1 = "balderdash!"
# s2 = "balderdash!"
# print(lcs(s1, s2))