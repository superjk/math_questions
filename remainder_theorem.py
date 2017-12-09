# coding=utf-8
mtp = ['ini','','','','','','','','','','','','','']
answers = []
i1=1
while i1 <= 13:
    mtp[i1]=input('If we count them by' + str(i1) + ' s ' + 'and how many left do we have?(If no restriction press Enter)')
    i1 = i1+1
dgt = input('In how many digits would you like to get your answers?')
for j in range(10**(int(dgt)-1),10**int(dgt)):
    i2=1
    while i2 <= 13:
        if mtp[i2] != '' and j % i2 != int(mtp[i2]):
            break
        elif i2 == 13:
            answers.append(j)
            break
        else:
            i2 = i2+1
for answer in answers:
    print('Answers:' + str(answer) + '\n')
print('There are '+str(len(answers))+' answers.'+ '\n')
#---end of the code---

# coding=utf-8
# traditional chinese version
mtp = ['ini','','','','','','','','','','','','','']
answers = []
i1=1
while i1 <= 13:
    mtp[i1]=input(str(i1) + '個' + str(i1) + '個拿剩幾個?(不限制直接按Enter)')
    i1 = i1+1
dgt = input('幾位數?')
for j in range(10**(int(dgt)-1),10**int(dgt)):
    i2=1
    while i2 <= 13:
        if mtp[i2] != '' and j % i2 != int(mtp[i2]):
            break
        elif i2 == 13:
            answers.append(j)
            break
        else:
            i2 = i2+1
for answer in answers:
    print('答案：' + str(answer) + '\n')
print('共'+str(len(answers))+'個答案'+ '\n')
