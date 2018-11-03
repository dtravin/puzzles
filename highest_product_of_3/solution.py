def solution(a):
    high = max(a[0], a[1])
    low = min(a[0], a[1])

    hp2_high = a[0] * a[1]
    hp2_low = a[0] * a[1]

    hp3 = -10E8

    for e in a[2:]:
        hp3 = max(hp3, hp2_high * e, hp2_low * e)

        hp2_low = min(hp2_low, low * e, high * e)
        hp2_high = max(hp2_high, low * e, high * e)

        low = min(low, e)
        high = max(high, e)

    return hp3
