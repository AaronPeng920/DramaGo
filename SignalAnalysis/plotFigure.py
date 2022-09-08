# - * - coding: utf-8 - * -
from spectrumFigure import *
from spectrogramFigure import *
from waveformFigure import *

if __name__ == "__main__":
    songpath = "/Users/aaronpeng/Desktop/Adobe/音频材料/bensound-allthewayup.mp3"
    wavformpath = "./figures/waveform.jpg"
    specpath = "./figures/spec.jpg"
    spectpath = "./figures/spect.jpg"
    displayWaveform(songpath, wavformpath)
    displaySpectrum(songpath, specpath)
    displaySpectrogram(songpath, spectpath)
    
