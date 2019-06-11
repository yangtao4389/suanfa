'''
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''


def combinationSum( candidates, target) :
    n = len(candidates)
    candidates.sort()
    res = []

    def dfs(t, ind, path):
        if t == 0:
            res.append(path)
            return
        for i in range(ind, n):
            if candidates[i] > t:
                break
            dfs(t - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return res

if __name__ == '__main__':
    candidates = [ 2,3,6,7 ]
    target = 7

    res = combinationSum(candidates,target)
    print(res)