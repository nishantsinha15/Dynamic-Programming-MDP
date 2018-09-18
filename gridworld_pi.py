import numpy as np

n_state = 15


def init():
    v = np.zeros(n_state)
    pi = np.zeros((n_state, n_state))
    return v, pi


def policy_evaluation(v, pi):
    threshhold = 0.01
    delta = 0
    return v,pi


def policy_improvement(v, pi):
    optimal = False
    return v,pi, optimal


def show(v,pi):
    x = 0
    print("Printing Value Functions")
    for i in range(4):
        for j in range(4):
            print("%5.5f" %(v[x]), end="\t")
            x += 1
            if x == 15:
                print("%5.5f" % (v[0]), end="\t")
                break
        print()


def main():
    v, pi = init()
    show(v,pi)
    condition = True
    # while condition:
    #     v, pi = policy_evaluation(v,pi)
    #     v, pi, condition = policy_improvement(v, pi)

main()