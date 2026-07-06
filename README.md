# Agentic Saturator
## What is it?
Agentic Saturator is an experiment or proof of concept. It tries to approach the topic of (guitar) distortion from a 
different direction than modeling existing amps or non-linear charcteristic curves.  
The idea behind agentic saturator is that a signal to process has to be "re-built" or "copied" by a set of "agents", 
but with limited resources. These limited resources are responsible for the saturation, once the input signal gets
too loud. The reason why I think that this approach could be promising is that it models in a rather abstract way the way
real saturation happens in an amplifier: Components reach the limits of their resources.

## What is agentic about it?
Not very much yet. At the moment, we have just components that try to add their contribution to add up to the signal and once
their storage is used up, the can only output the amount they are re-filled at each sample. But the approach could be
enhanced to make complex interactions between complex strategies possible. In my experience, the complex, non-linear interaction between many components
is where it really gets interesting, natural and organic.
In the future, I may even decide to implement some kind of re-inforcement learning, just for the fun of it, because it would
make the behavior of the agents more complex. 

## Demo files
Find some demo files in [./data/demo](./data/demo).

## Usage
After installing the dependencies from requirements.txt, use the following script to generate your saturated signal:
(Yet to be parametrised)
`(.venv) agentic_saturator$ python -m scripts.simple_io`
