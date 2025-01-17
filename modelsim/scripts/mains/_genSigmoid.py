# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:15:25 2022

Engineer: Michele Pio Fragasso


Description:
    
    Contains a set of functions to generate the binary Sigmoid values to load into the LUT.
    
    The output file SigmoidContent.mif contains the Sigmoid output value y for different values of
    x. The number of outputs will be 2^(inputSize). 
    
    Notes:
    --"Base" 10 fixed-point representation" is the fixed-point representation but converted from
    binary to base 10.
    
    This file is deprecated.
"""

import sys
sys.path.insert(0,"../functions/")

import Sigmoid


outputdataWidth=32
outputdataIntWidth=6
inputSize=5
inputIntWidth=2
        
if __name__ == "__main__":
    Sigmoid.genSigContent(dest_path="../files/sigmoid/",outputdataWidth=32,outputdataIntWidth=6,inputSize=5,inputIntWidth=2)