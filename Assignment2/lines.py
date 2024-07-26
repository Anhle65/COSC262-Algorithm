def line_edits(s1, s2):
    lines_s1= s1.splitlines()
    lines_s2= s2.splitlines()
    table = [[0]*(len(lines_s2) + 1) for _ in range(len(lines_s1) + 1)]
    for i in range(len(lines_s1)+1):
        table[i][0] = i
    for j in range(len(lines_s2)+1):
        table[0][j] = j
    for row in range(1,len(lines_s1)+1):
        for col in range(1,len(lines_s2)+1):
            if lines_s1[row-1] == lines_s2[col-1]:
                table[row][col] = table[row-1][col-1]
            else:
                table[row][col] = min(table[row-1][col], table[row][col-1], table[row-1][col-1]) + 1
    result = []
    i,j = len(lines_s1), len(lines_s2)
    while i > 0 and j >0:
        if lines_s1[i-1] == lines_s2[j-1]:
            result.insert(0,("C", lines_s1[i-1], lines_s2[j-1]))
            i-=1
            j-=1
        else:
            minimum = min(table[i-1][j], table[i][j-1], table[i-1][j-1])
            if minimum == table[i-1][j-1]:
                result.insert(0,("S", lines_s1[i-1], lines_s2[j-1]))
                i-=1
                j-=1
            elif minimum == table[i][j-1]:
                result.insert(0,("I", "", lines_s2[j-1]))
                j-=1
            else:
                result.insert(0,("D", lines_s1[i-1], ""))
                i-=1        
    return result