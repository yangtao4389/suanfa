'''
想象一个乡村诊所。村民有着非常理想化的特性，要么健康要么发烧。他们只有问诊所的医生的才能知道是否发烧。 聪明的医生通过询问病人的感觉诊断他们是否发烧。村民只回答他们感觉正常、头晕或冷。

假设一个病人每天来到诊所并告诉医生他的感觉。医生相信病人的健康状况如同一个离散马尔可夫链。病人的状态有两种“健康”和“发烧”，但医生不能直接观察到，这意味着状态对他是“隐含”的。每天病人会告诉医生自己有以下几种由他的健康状态决定的感觉的一种：正常、冷或头晕。这些是观察结果。 整个系统为一个隐马尔可夫模型(HMM)。

医生知道村民的总体健康状况，还知道发烧和没发烧的病人通常会抱怨什么症状。 换句话说，医生知道隐马尔可夫模型的参数。 这可以用Python语言表示如下:
'''
states = ('Healthy', 'Fever')
observations = ('normal', 'cold', 'dizzy', 'dizzy')
#  起始概率start_probability 表示病人第一次到访时医生认为其所处的HMM状态，他唯一知道的是病人倾向于是健康的
start_probability = {'Healthy': 0.6, 'Fever': 0.4}


# 转移概率transition_probability表示潜在的马尔可夫链中健康状态的变化。在这个例子中，当天健康的病人仅有30%的机会第二天会发烧
transition_probability = {
   'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.6},
   }

# 放射概率emission_probability表示每天病人感觉的可能性。假如他是健康的，50%会感觉正常。如果他发烧了，有60%的可能感觉到头晕。
emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
   }

# Helps visualize the steps of Viterbi.
def print_dptable(V):
    print("    "),
    for i in range(len(V)): print("%7d" % i,)
    print()

    for y in V[0].keys():
        print( "%.5s: " % y,)
        for t in range(len(V)):
            print("%.7s" % ("%f" % V[t][y]),)
        print()



def viterbi(obs, states, start_p, trans_p, emit_p):
    '''
    函数viterbi 具有以下参数:
    obs 为观察结果序列, 例如 ['normal', 'cold', 'dizzy']；
     states 为一组隐含状态； ('Healthy', 'Fever')
     start_p 为起始状态概率;{'Healthy': 0.6, 'Fever': 0.4}
     trans_p 为转移概率;transition_probability
     而 emit_p 为放射概率。 emission_probability
    '''
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    # 先初始化第一步
    for y in states: # ('Healthy', 'Fever')
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
        print(path,'ppppppppppp')
        print(V,'VVVVVVVVVVVVVVV')

    # Run Viterbi for t > 0
    for t in range(1,len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            print(y,'yyyyyyyyy')
            print([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states],'llllllllllll')
            (prob, state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        # Don't need to remember the old paths
        path = newpath

    # print_dptable(V)
    print(V,'22222vvvvvvvvvvvvv')
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])

def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
print(example())