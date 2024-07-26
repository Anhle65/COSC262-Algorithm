def lcs(s1, s2):
    table = [[0] * (len(s2) + 1) for _ in range (len(s1) +1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    last_item = table[len(s1)][len(s2)]
    lcs_str = [''] * last_item
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str[last_item - 1] = s1[i - 1]
            i -= 1
            j -= 1
            last_item -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs_str
def different_character(str, lcs_str):
    result = []
    lcs_list = lcs_str
    for char in str:
        if lcs_list and lcs_list[0] == char:
            lcs_list.pop(0)
            result.append(char)
        else:
            result.append(f'[[{char}]]')
    return ''.join(result)
def line_edits(s1, s2):
    lines1, lines2 = s1.splitlines(), s2.splitlines()
    table = [[0] * (len(lines2) + 1) for _ in range(len(lines1) + 1)]
    for i in range(1, len(lines1) + 1):
        table[i][0] = i
        for j in range(1, len(lines2) + 1):
            table[0][j] = j
            if lines1[i - 1] == lines2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(table[i - 1][j - 1] + 1,
                               table[i - 1][j] + 1,     
                               table[i][j - 1] + 1)   
    i, j = len(lines1), len(lines2)
    result = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and lines1[i - 1] == lines2[j - 1]:
            result.insert(0,('C', lines1[i - 1], lines2[j - 1]))
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and table[i][j] == table[i - 1][j - 1] + 1:
            lcs_list = lcs(lines2[i - 1], lines1[j - 1])
            left = different_character(lines1[i - 1], lcs_list.copy())
            right = different_character(lines2[j-1], lcs_list)
            result.insert(0,('S',left,right))
            i -= 1
            j -= 1
        elif i > 0 and table[i][j] == table[i - 1][j] + 1:
            result.insert(0,('D', lines1[i - 1], ''))
            i -= 1
        else:
            result.insert(0,('I', '', lines2[j - 1]))
            j -= 1
    return result
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)