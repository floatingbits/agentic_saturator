import soundfile as sf
import sounddevice as sd

from audio.factory import build_saturator
from audio.processing.saturator import Saturator
from scipy.signal import fftconvolve

from util.performance import timer

with timer("Total Processing"):
    audio, sr = sf.read("data/input/demo/dry_riff_long.wav")
    ir, sr_ir = sf.read("data/convolution/IR.wav")

    assert sr == sr_ir

    if len(audio.shape) > 1:
        audio = audio[:,0]
    processor = build_saturator(sr)
    # Processing
    processed = processor.process_mono(audio*70)
    processed /= abs(processed).max()
    out = fftconvolve(processed, ir)
    out /= abs(out).max()
    sf.write("data/output/1.wav",processed,sr)
    sf.write("data/output/with_cabinet.wav",out,sr)
sd.play(out, sr)
sd.wait()