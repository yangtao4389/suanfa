'''
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0

'''

class Solution:
    def imageSmoother(self, M):
        '''
        暴力法看起来可以求解的样子
        但比较麻烦。。
        :param M:
        :return:
        '''
        hang = len(M)
        lie = len(M[0])
        for i in range(hang):
            for j in range(lie):
                pass
    def imageSmoother2(self, M):
        '''
        卷积神经网络里的平均池
        :param M:
        :return:
        '''
        # 以00为原点来定义其余8个点,顺时针12点开始遍历一遍
        # dirs = []
        # for i in [-1,0,1]:
        #     for j in [-1,0,1]:
        #         if i == 0 and j== 0:
        #             continue
        #         dirs.append([i,j])

        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        height = len(M)
        width = len(M[0])
        res = []
        for i in range(height):
            cache = []
            for j in range(width):
                sum = M[i][j]
                count = 1
                for _dir in dirs:
                    #todo 遍历所有的关于当前点围绕的8个数的x,y.当满足x,y依旧落在该取值区间，就进行加和
                    x = _dir[0]+i
                    y = _dir[1]+j
                    if x>=0 and x<height and y>=0 and y<width:
                        sum += M[x][y]
                        count += 1
                cache.append(sum//count)
            res.append(cache)

        return res


if __name__ == '__main__':
    print(Solution().imageSmoother2([[1,1,1],[1,0,1],[1,1,1]]))
    print(Solution().imageSmoother2([[]]))