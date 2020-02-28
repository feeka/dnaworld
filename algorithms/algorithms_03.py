import sys
from collections import defaultdict
from itertools import combinations, product
from functools import reduce

alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
def kmer_mismatches(kmer, d):
    mismatches = [kmer] 
    if d== 0:
        return mismatches
    
    for dist in range(1, d+1):
        for change_indices in combinations(range(len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in zip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches




def motif_enumeration(dna, k, d):
    motif_sets = [{kmer for i in range(len(seq)-k+1) for kmer in kmer_mismatches(seq[i:i+k], d)} for seq in dna]
    return sorted(list(reduce(lambda a,b: a & b, motif_sets)))      


def count(Motifs):
    count = {} 
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = count(Motifs)
    for symbol in 'ACGT':
        for j in range(k):
            profile[symbol][j] = profile[symbol][j]/float(t)
    return profile

def consensus(Motifs):
    
    k = len(Motifs[0])
    counts = count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if counts[symbol][j] > m:
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def score(Motifs):
    profile = count(Motifs)
    Consensus = consensus(Motifs)
    t = len(Motifs)
    score = 0
    for i in range(len(Motifs[0])):
        score = score + (t - profile[Consensus[i]][i])
    return score

def pr(Text, Profile):
    pr = 1
    for i in range(len(Text)):
        pr = pr*Profile[Text[i]][i]
    return pr

def profile_most_probable_pattern(Text, Profile):
    T = len(Text)
    K = len(Profile['A'])
    prob = 0
    x = Text[0:K]
    for i in range(T - K + 1):
        Subtext = Text[i:i+K]
        temp_prob = pr(Subtext,Profile)
        if temp_prob > prob:
            prob = temp_prob
            x = Subtext
    return x

def greedy_motif_search(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = profile(Motifs[0:j])
            Motifs.append(profile_most_probable_pattern(Dna[j], P))
        if score(Motifs) < score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


###############################################MAINCODE#########################################################################
def MedianString(Dna, k): #MEDIANSTRING(Dna, k)
    Distance = float("inf") #distance ← ∞
    for i in range(0, 4**k): #for i ←0 to 4k −1
        Pattern = NumberToPattern(i, k) #Pattern ← NumberToPattern(i, k)
        if Distance > distanceBetweenPatternAndStrings(Pattern, Dna): #if distance > DistanceBetweenPatternAndStrings(Pattern, Dna)
            Distance = distanceBetweenPatternAndStrings(Pattern, Dna) #distance ← DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern #Median ← Pattern
    return Median
###############################################MAINCODE#########################################################################

###################################################SubCodes#####################################################################
################################HammingDistance#########################################
def distanceBetweenPatternAndStrings(Pattern, Dna): #distanceBetweenPatternAndStrings(Pattern, Dna)
    k = len(Pattern) #k ← |Pattern|
    Distance = 0 #distance ← 0
    for string in  Dna: #for each string Text in Dna
        hammingDistance = float("inf") #HammingDistance ← ∞
        for i in range(0, len(string)-k+1): #for each k-mer Pattern’ in Text
            if hammingDistance > HammingDistance(Pattern, string[i:i+k]): #if HammingDistance > HammingDistance(Pattern, Pattern’)
                hammingDistance = HammingDistance(Pattern, string[i:i+k]) #HammingDistance ← HammingDistance(Pattern, Pattern’)
        Distance = Distance + hammingDistance#distance ← distance + HammingDistance
    return Distance
################################distanceBetweenPatternAndStrings#########################################

################################HammingDistance#########################################
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
################################HammingDistance#########################################

################################NumberToPattern#########################################
def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = Quotient(index, 4)
    r = Remainder(index, 4)
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    return PrefixPattern + symbol

def reverse(text):
    result = ''
    count = len(text) -1
    for x in text:
        result += text[count]
        count -=1
    return result

def NumberToSymbol(r):
    if r == 0:
        return "A"
    elif r == 1:
        return "C"
    elif r == 2:
        return "G"
    else:
        return "T"

def Remainder(num, n):
    return int(num)%n

def Quotient(num, n):
    return int(num)//n
################################NumberToPattern#########################################