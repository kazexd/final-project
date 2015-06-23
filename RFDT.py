from sklearn.ensemble import RandomForestClassifier
def readdata(filename):
    _file = open(filename,'r')
    atts_num = len(_file.readline().split(','))-2
    atts, label = [], []
    for eachline in _file:
        line_atts = eachline.split(',')
        sample = []
        for i in range(atts_num):
            sample.append(float(line_atts[i+1]))
        atts.append(sample)
        label.append(int(line_atts[atts_num+1]))
    _file.close()
    return atts, label
def main():
    X,Y = readdata('train.csv')
    RF = RandomForestClassifier(n_jobs = -1)
    RF = RF.fit(X,Y)
    
    testdata = open('test.csv','r')
    length = len(testdata.readline().split(','))-1
    print length
    test_atts = []
    for eachline in testdata:
        line_atts = eachline.split(',')
        atts = []
        for i in range(0,length):
            try:
                atts.append(float(line_atts[i+1]))
            except:
                print i+1
        test_atts.append(atts)
    output = open('output.csv','w')
    output.write('id,label\n')
    for i in range(len(test_atts)):
        label = RF.predict(test_atts[i])
        output.write(str(i)+','+str(int(label))+'\n')
if __name__ == '__main__':
    main()