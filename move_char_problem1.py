def move(s):
    result = ''
    for c in s:
        if c == ' ':
            result += ' '
            continue
        o = ord(c) - ord('a')
        o = (o + 2) % 26
        r = chr(ord('a') + o)
        result += r
    return result


if __name__ == '__main__':
    s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'
    s = 'map'
    print(move(s))
