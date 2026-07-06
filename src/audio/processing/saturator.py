import numpy as np

from audio.core import MonoProcessor, MonoFrame
from audio.processing.agent.core import Agent


class Saturator(MonoProcessor):
    def __init__(self, sr,agents: list[Agent]):
        super().__init__(sr)
        self.agents = agents
    def process_mono(self, samples: MonoFrame) -> MonoFrame:
        current_state = np.zeros_like(samples)
        for agent in self.agents:
            current_state = agent.rebuild_audio(samples, current_state)
        return current_state

