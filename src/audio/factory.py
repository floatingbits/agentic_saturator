from audio.processing.agent.core import SimpleAgent
from audio.processing.saturator import Saturator
import numpy as np

def build_saturator(sr):
    num_agents = 15
    capacity = 3/num_agents
    refill = 0.2/num_agents
    rng = np.random.default_rng(12345)

    agents = [
        SimpleAgent(capacity + 10*rng.random()/num_agents,refill + 0.6*rng.random()/num_agents, is_bipolar=rng.random() > 0.2)
        for _ in range(0,num_agents)
    ]
    return Saturator(sr, agents)