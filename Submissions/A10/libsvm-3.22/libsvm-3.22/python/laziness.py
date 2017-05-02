count =0
out=open("lazyvectors.txt",'wb')
while count <100:
    print "test"
    if (count%10==0):
        out.write('\n')
    if count !=66:
        name ="vectors[" +str(count)+"],"

    if count ==99:
        name = "vectors[" + str(count) + "]"
    out.write('\t%s' % name)
    count += 1