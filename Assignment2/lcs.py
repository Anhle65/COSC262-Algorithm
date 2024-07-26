
def lcs(s1, s2, cache = None):
    if cache == None:
        cache = []
    result = ""
    cache = [[0] * (len(s2)+1) for row in range(len(s1)+1)]
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i][j-1], cache[i-1][j])
    i = len(s1)-1
    j = len(s2)-1
    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            result = s1[i] + result
            i -= 1
            j -= 1
        else:
            if cache[i-1][j] >= cache[i][j-1]:
                i -= 1
            else:
                j -= 1
    return result
# A simple test that should run without caching
# s1 = "Look at me, I can fly!"
# s2 = "Look at that, it's a fly"
# lcs_string = lcs(s1, s2)
# print(lcs_string)
s1 = "*abbcccddddeeeeeffffgghhijjkkkllllmmmmm*"
s2 = "abcdefghijklmnopqrst"
lcs_string = lcs(s1, s2)
print(lcs_string)