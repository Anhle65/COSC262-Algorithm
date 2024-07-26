
def line_edits(s1, s2):
    lines_s1= s1.splitlines()
    lines_s2= s2.splitlines()
    table = [[0]*(len(lines_s2) + 1) for _ in range(len(lines_s1) + 1)]
    for row in range(1,len(lines_s1)+1):
        table[row][0] = row
        for col in range(1,len(lines_s2)+1):
            table[0][col] = col
            if lines_s1[row-1] == lines_s2[col-1]:
                table[row][col] = table[row-1][col-1]
            else:
                table[row][col] = min(table[row-1][col], table[row][col-1], table[row-1][col-1]) + 1
    result = []
    i,j = len(lines_s1), len(lines_s2)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and lines_s1[i-1] == lines_s2[j-1]:
            result.insert(0,("C", lines_s1[i-1], lines_s2[j-1]))
            i-=1
            j-=1
        elif i > 0 and j > 0 and table[i][j] == table[i - 1][j - 1] + 1:
            result.insert(0,('S', lines_s1[i - 1], lines_s2[j - 1]))
            i -= 1
            j -= 1
        elif i > 0 and table[i][j] == table[i - 1][j] + 1:
            result.insert(0,('D', lines_s1[i - 1], ''))
            i -= 1
        else:
            result.insert(0,('I', '', lines_s2[j - 1]))
            j -= 1
    return result
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
# s1 = "Line1\nLine2\nLine3\nLine4\n"
# s2 = "Line5\nLine4\nLine3\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)
# s1 = "Line1\n"
# s2 = ""
# table = line_edits(s1, s2)
# for row in table:
#     print(row)