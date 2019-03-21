import gym
env = gym.make('CartPole-v0')
env.reset()  #重置环境
for _ in range(100000):  #1000帧
    env.render()  #每一帧重新渲染环境
    env.step(env.action_space.sample()) # take a random action