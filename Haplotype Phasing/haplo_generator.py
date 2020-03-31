import numpy as np
import sys
import random
import time

# fill in the stars with obvious (100%) predication where 
# other individuals have all 0's or 2's
def fill_in_obvious(data):
    for i in range(len(data)):
        arr = [0, 0, 0]
        for j in range(len(data[i])):
            if data[i][j] == b'0':
                arr[0] += 1
            elif data[i][j] == b'2':
                arr[1] += 1
            elif data[i][j] == b'*':
                arr[2] += 1
        if arr[2] > 0:
            if arr[0] == 0 or arr[1] == 0:
                unmask = b'0'
                if arr[0] == 0:
                    unmask = b'2'
                for j in range(len(data[i])):
                    if data[i][j] == b'*':
                        data[i][j] = unmask;

# fill in the non obvious stars. 
def fill_in_non_obvious(data, check_range):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == b'*':
                candidate = b'0'
                similarity = -1.0
                left = check_range
                right = check_range
                if j - left < 0:
                    right += (left - j)
                    left = left - j
                elif j + right >= len(data[i]):
                    left -= ((j + right) - len(data[i]) + 1)
                    right = len(data[i]) - j - 1
                for k in range(len(data)):
                    if i == k or data[k][j] == b'*':
                        continue
                    else:
                        same_count = 0.0
                        for n in range(j-left, j+right+1):
                            if data[k][n] == b'*':
                                same_count += 0.5
                            elif data[k][n] == data[i][n]:
                                same_count += 1
                            elif data[i][n] == b'*':
                                if data[k][n] == b'0' or data[k][n] == b'2':
                                    same_count += 0.5
                        acc = same_count / (2 * left + 1)
                        if acc > similarity:
                            candidate = data[k][j]
                            similarity = acc
                data[i][j] = candidate


def realParse(data, haploSize):
    final_sol = []
    indexSize = (len(data[0]) + haploSize - 1) // haploSize 
    for i in range(indexSize):
        cut_genos = []
        for j in range(len(data)):
            if i*haploSize + haploSize > len(data[0]):
                cut_genos.append(data[j][i*haploSize:])
            else:
                cut_genos.append(data[j][i*haploSize:i*haploSize+haploSize])
        known = list()
        unknown = []
        result = []
        for m in range(len(cut_genos)):
            one_count = 0
            for j in range(len(cut_genos[m])):
                if cut_genos[m][j] == b'1':
                    one_count += 1
            if one_count < 2:
                hap1 = []
                hap2 = []
                for j in range(len(cut_genos[m])):
                    if cut_genos[m][j] == b'0':
                        hap1.append(b'0')
                        hap2.append(b'0')
                    elif cut_genos[m][j] == b'2':
                        hap1.append(b'1')
                        hap2.append(b'1')
                    else:
                        if random.randint(0, 1) == 0:
                            hap1.append(b'1')
                            hap2.append(b'0')
                        else:
                            hap1.append(b'0')
                            hap2.append(b'1')
                known.append(hap1)
                known.append(hap2)
                result.append(hap1)
                result.append(hap2)
            else:
                unknown.append(m)
                hap1 = []
                hap2 = []
                for ch in cut_genos[m]:
                    if ch == b'0':
                        hap1.append(b'0')
                        hap2.append(b'0')
                    elif ch == b'2':
                        hap1.append(b'1')
                        hap2.append(b'2')
                    else:
                        if random.randint(0,1) == 0:
                            hap1.append(b'0')
                            hap2.append(b'1')
                        else:
                            hap1.append(b'1')
                            hap2.append(b'0')
                result.append(hap1)
                result.append(hap2)
        if len(known) > 0:
            known = np.unique(known, axis=0)
            known = list(known)
        loopCount = 0
        while (len(unknown) != 0 and loopCount < 3):
            flag = False
            for n in unknown:
                match_hap = findSumMatch(known, cut_genos[n])
                if len(match_hap) > 0:
                    known.append(match_hap[0])
                    known.append(match_hap[1])
                    result[n*2] = match_hap[0]
                    result[n*2 + 1] = match_hap[1]
                    flag = True
                    known = np.unique(known, axis=0)
                    known = list(known)
                    unknown.remove(n)
            if flag == True:
                loopCount = 0
                continue
            for n in unknown:
                match_hap = singleMatch(known, cut_genos[n])
                if len(match_hap) > 0:
                    known.append(match_hap[1])
                    result[n*2] = match_hap[0]
                    result[n*2 + 1] = match_hap[1]
                    flag = True
                    known = np.unique(known, axis=0)
                    known = list(known)
                    unknown.remove(n)
            if flag == True:
                loopCount = 0
                continue
            loopCount += 1
        if i == 0:
            for geno in result:
                final_sol.append(geno)
        else:
            for z in range(len(result)):
                final_sol[z] = np.append(final_sol[z], result[z])
    return final_sol


def singleMatch(knowns, geno):
    geno_num = byteToInt(geno)
    knowns_num = []
    for known in knowns:
        knowns_num.append(byteToInt(known))
    for known in knowns_num:
        temp = np.subtract(geno_num, known)
        flag = True
        for n in temp:
            if n < 0:
                flag = False
                break
        if flag == True:
            ret = []
            ret.append(intToByte(known))
            ret.append(intToByte(temp))
            return ret
    return []
       

def byteToInt(data):
    new_data = []
    for d in data:
        new_data.append(int(d))
    return new_data


def intToByte(data):
    new_data = []
    for d in data:
        new_data.append(str(d).encode('ascii'))
    return new_data


def findSumMatch(knowns, geno):
    geno_num = byteToInt(geno)
    knowns_num = []
    for known in knowns:
        knowns_num.append(byteToInt(known))
    for known in knowns_num:
        temp = np.subtract(geno_num, known)
        for n in temp:
            if n < 0:
                knowns_num.remove(known)
                break
    for i in range(len(knowns_num)):
        for j in range(i, len(knowns_num)):
            temp = np.add(knowns_num[i], knowns_num[j])
            if np.array_equal(temp, geno_num):
                ret = []
                ret.append(intToByte(knowns_num[i]))
                ret.append(intToByte(knowns_num[j]))
                return ret
    return []


def writeGenoToFile(data, fname):
    with open(fname, 'w') as f:
        for row in data:
            for i in range(len(row)):
                if row[i] == b'0':
                    f.write('0')
                elif row[i] == b'1':
                    f.write('1')
                elif row[i] == b'2':
                    f.write('2')
                if i != len(row) - 1:
                    f.write(' ')
            f.write('\n')


def writeHaploToFile(data, fname):
    with open(fname, 'w') as f:
        for row in data:
            for i in range(len(row)):
                if row[i] == b'0':
                    f.write('0')
                elif row[i] == b'1':
                    f.write('1')
                else:
                    f.write('0')
                if i != len(row) - 1:
                    f.write(' ')
            f.write('\n')


def main():
    fname = sys.argv[1]
    sol_name = sys.argv[2]
    start = time.time()
    geno = np.genfromtxt(fname, dtype=bytes, delimiter=' ')
    fill_in_obvious(geno)
    geno = np.transpose(geno)
    fill_in_non_obvious(geno, 3)
    geno = np.transpose(geno)
    end = time.time()
    print('Duration For Geno Unmasking: ' + str(end - start))
    print('')

    start = time.time()
    print('size of haplo: %d' % 20)
    print('geno size: %s x %s' % (len(geno), len(geno[0])))
    geno_t = np.transpose(geno)
    print('geno_t size: %s x %s' % (len(geno_t), len(geno_t[0])))
    my_haplo_sol = realParse(geno_t, 20)
    print('my_haplo_sol size: %s x %s' % (len(my_haplo_sol), len(my_haplo_sol[0])))

    my_haplo_sol_t = np.transpose(my_haplo_sol)
    print('my_haplo_sol_t size: %s x %s' % (len(my_haplo_sol_t), len(my_haplo_sol_t[0])))
    # fname = 'test_data_sol.txt'
    writeHaploToFile(my_haplo_sol_t, sol_name)
    end = time.time()
    print('Duration: ' + str(end - start))
    print('')


if __name__ == '__main__':
    main()
