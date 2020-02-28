def HammingDistance(p, q):
    count=0
    for i in range(0,len(p)):
        if p[i]!=q[i]:
            count+=1
    return count
def ApproximatedHammingDistance(p,q,dev):
    err_count = 0
    for i in range(0,len(p)):
        if p[i]!=q[i]:
            err_count+=1
        else:
            err_count +=0
    if err_count<=dev:
        return True
    return False

def ApproximatedPatternMatching(Text,Pattern,d):
    positions = []
    for i in range(0,len(Text)):
        print(Text[i:i+len(Pattern)])
        if ApproximatedHammingDistance(Text[i:i+len(Pattern)],Pattern,d):
            positions.append(i)
        elif len(Text[i:len(Text)])<=len(Pattern):
            break
    return positions
str_from_file = open('dataset_9_4.txt', 'r').read()


def ApproximatePatternCount(Text, Pattern, d):
    count = 0
    for i in range(len(Text)-len(Pattern)):
        Pt = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern, Pt) <= d:
            count=count+1
    return count
print(HammingDistance("TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC","GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"))
print(ApproximatePatternCount("CATGCCATTCGCATTGTCCCAGTGA","CCC",2))
