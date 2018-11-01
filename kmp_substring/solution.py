# Knutt Morris Pratt substring search

def solution(s,p):
    prefix = build_prefix(p)
    pi = 0
    for i in range(len(s)):
        #print("%s %s" % (s,p))
        #print("i = %s, pi = %s" % (i, pi))
        if s[i] == p[pi]:
            if pi == len(p) - 1:
                return i-pi
            pi += 1
        else:
            pi = prefix[pi]        

    return -1
        

def build_prefix(p):
    j = 0
    prefix = [0]
    prefix_length = 0
    for i in range(1, len(p)):

        if p[j] == p[i]:
            prefix_length += 1
            j += 1
        else:
            prefix_length = 0
            j = 0

        prefix.append(prefix_length)
            
        
    return prefix
