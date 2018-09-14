import numpy as np

dic = {}
rev_dic = {}


def get_probability_matrix():
    p = np.zeros([25, 25])
    global dic, rev_dic

    #interior probabilities
    for i in range(1, 4):
        for j in range(1, 4):
            curr_index = dic[(i, j)]
            neighbours = [dic[(i - 1, j)], dic[(i + 1, j)], dic[(i, j + 1)], dic[(i, j - 1)]]
            for n in neighbours:
                p[curr_index][n] = 0.25

    #top
    for i in range(1, 4):
        curr_index = dic[(0,i)]
        neighbours = [ dic[(1,i)], dic[0, i+1], dic[0, i - 1] ]
        p[curr_index][curr_index] = 0.25
        for n in neighbours:
            p[curr_index][n] = 0.25

    # bottom
    for i in range(1,4):
        curr_index = dic[(4, i)]
        neighbours = [dic[(3, i)], dic[(4, i + 1)], dic[(4, i-1)] ]
        p[curr_index][curr_index] = 0.25
        for n in neighbours:
            p[curr_index][n] = 0.25

    # left
    for i in range(1,4):
        curr_index = dic[(i, 0)]
        neighbours = [dic[(i, 1)], dic[(i-1,0)], dic[(i+1, 0)] ]
        p[curr_index][curr_index] = 0.25
        for n in neighbours:
            p[curr_index][n] = 0.25

    # left
    for i in range(1, 4):
        curr_index = dic[(i, 4)]
        neighbours = [dic[(i, 4)], dic[(i - 1, 4)], dic[(i + 1, 4)]]
        p[curr_index][curr_index] = 0.25
        for n in neighbours:
            p[curr_index][n] = 0.25

    corner = [ dic[(0,0)], dic[(4,4)], dic[(0,4)], dic[(4,0)]]
    for i in corner:
        p[i][i] = 0.5

    #hardcoding the rest
    curr = dic[(0,0)]
    p[curr][dic[(0,1)]] = p[curr][dic[(1,0)]] = 0.25

    curr = dic[(4, 4)]
    p[curr][dic[(4, 3)]] = p[curr][dic[(3, 4)]] = 0.25

    curr = dic[(0, 4)]
    p[curr][dic[(0, 3)]] = p[curr][dic[(1, 4)]] = 0.25

    curr = dic[(4, 0)]
    p[curr][dic[(3, 0)]] = p[curr][dic[(4, 1)]] = 0.25

    #special states
    curr = dic[(0,1)]
    for i in range(25):
        p[curr][i] = 0
    p[curr][dic[(4,1)]] = 1

    curr = dic[(0,3)]
    for i in range(25):
        p[curr][i] = 0
    p[curr][dic[(2,1)]] = 1

    return p


def get_hash():
    global dic, rev_dic
    counter = 0
    for i in range(5):
        for j in range(5):
            dic[(i, j)] = counter
            rev_dic[counter] = (i, j)
            counter += 1

    # print(dic)
    return dic


def get_expected_reward_vector(p):
    r = np.zeros(25)
    for s in range(25):
        reward = 0
        for i in range(25):
            if i == s:
                reward += p[s][i]*(-1)
        r[s] = reward
        if s == dic[(0,1)]:
            r[s] = 10
        if s == dic[(0, 3)]:
            r[s] = 5
    return r


def solve():
    get_hash()
    p = get_probability_matrix()
    print(p)
    r = get_expected_reward_vector(p)
    for i in range(25):
        print(rev_dic[i], " ", r[i])
    discount = 0.9
    i = np.identity(25)
    temp = np.multiply(discount, p)
    temp = i - temp

    inverse = np.linalg.inv(temp)

    x = np.dot(temp,inverse)
    v = np.dot(inverse, r)
    return v


def main():
    final = [ [0 for i in range(5)] for j in range(5) ]
    v = solve()
    for i in range(25):
        index = rev_dic[i]
        # print(index)
        final[index[0]][index[1]] = v[i]
    for rows in final:
        for e in rows:
            print(e,"\t\t", end = "")
        print()

main()
