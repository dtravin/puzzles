def solution(a):
    s = []
    max_area = 0
    i = 0
    while i < len(a):
        top = s[-1] if len(s) > 0 else None
        print('i=%s  S %s, max_area %s, top %s' % (i, s, max_area, top) )
        if len(s) == 0 or a[i] >= a[s[-1]]:
            s.append(i)
            i += 1
        else:
            top = s.pop()
            print('Candidate %s * %s' % ((i-top), a[top]))
            max_area = max(max_area, (i-top)*a[top])

    while len(s) > 0:
            top = s.pop()
            print('Candidate %s * %s' % ((i-top), a[top]))
            max_area = max(max_area, (i-top)*a[top])

    print('Result: %s\n' % max_area)

    return max_area
