def trim(s):
    def cutHeadBlank(s):
        headEnd = 0
        for subS in s:
            if subS == ' ':
                headEnd += 1
            else:
                break
        s = s[headEnd:]
        return s
    s = cutHeadBlank(s)
    s = s[::-1]
    s = cutHeadBlank(s)
    return s[::-1]