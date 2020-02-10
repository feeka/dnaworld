def MinimumSkew(Genome):
    positions = []
    SkewGenome = Skew(Genome)
    m = min(SkewGenome.values())
    n = len(Genome)
    for i in range(1, n+1):
        if SkewGenome[i] == m:
            positions.append(i)
    return positions

def Skew(Genome):
    skew = {}
    n = len(Genome)
    for i in range(1, n+1):
        skew[0] = 0
        if Genome[i-1] == "G":
            skew[i] = skew[i-1] + 1
        elif Genome[i-1] == "C":
            skew[i] = skew[i-1] - 1
        else:
            skew[i] = skew[i-1]
    return skew
