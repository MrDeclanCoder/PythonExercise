# 去除首尾空格
def trim(s):
    if '' == s:
        print('1', s)
        return ''
    if s[:1] != ' ' and s[-1:] != ' ':
        print('2', s)
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[0:len(s) - 2])
