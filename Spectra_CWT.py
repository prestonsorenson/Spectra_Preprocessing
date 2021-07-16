#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:22:14 2021

@author: preston
"""

import pywt
import pandas as pd
import matplotlib.pyplot as plt

#import data
spectra=pd.read_csv('<file location>')

#subset data to only the spectra columns
spectra=spectra.iloc[:,6:1874]


#define wavelet transform functions. This example calculates a second order gaussian wavelet
#Scales 2, 3, and 4 are calculated and summed
def calculate_wavelet(data):
    wav2, freq = pywt.cwt(data, 2, "gaus2")
    wav3, freq = pywt.cwt(data, 3, "gaus2")
    wav4, freq = pywt.cwt(data, 4, "gaus2")
    result_wavelet = wav2 + wav3 + wav4
    return result_wavelet[0]

#This function applies the wavelet transform specified previously to each row the the imported data
def create_cwt(input_data):
    output = input_data.apply(lambda x: calculate_wavelet(x), axis=1)
    output = output.apply(lambda x: pd.Series(list(x)))
    return pd.DataFrame(output)

#process spectra with continuous wavelet transforms
spectra_cwt=create_cwt(spectra)

#plot results
plt.plot(spectra_cwt.iloc[100,:])
