from abc import ABC, abstractmethod
from audio.core import MonoFrame

class Agent(ABC):

    @abstractmethod
    def rebuild_audio(self, original:MonoFrame, current_state: MonoFrame ) -> MonoFrame:
        pass


class SimpleAgent(Agent):
    def __init__(self, capacity: float, refill_per_sample: float, is_bipolar:bool = False):
        # initialize with zero storage
        self.storage = 0
        self.neg_storage = 0
        # max storage
        self.capacity = capacity
        self.refill_per_sample = refill_per_sample
        self.is_bipolar = is_bipolar
    def rebuild_audio(self, original:MonoFrame, current_state: MonoFrame ) -> MonoFrame:
        for i, orig_sample in enumerate(original):
            residual = orig_sample - current_state[i]
            is_negative = orig_sample < 0
            if is_negative:
                residual = -residual
            use_negative_storage =  not is_negative or not self.is_bipolar
            storage_level = self.neg_storage if use_negative_storage else self.storage
            # prevent hard running out of resources
            contribution = min(residual, storage_level/1.5, self.capacity/4, self.refill_per_sample*20)
            # residual and storage are positive

            # take out of storage
            if not use_negative_storage:
                self.storage -= contribution
            else:
                self.neg_storage -= contribution
            # handle negative values
            if is_negative:
                contribution = -contribution
            # agents contribution to mimic the input signal
            current_state[i] += contribution
            # refill after each sample
            self.storage = min(self.capacity, self.refill_per_sample + self.storage)
            if self.is_bipolar:
                self.neg_storage = min(self.capacity, self.refill_per_sample + self.neg_storage)
        return current_state


