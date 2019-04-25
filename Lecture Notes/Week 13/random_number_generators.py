#!/usr/bin/env python

import numpy as np
import pandas as pd

def generator1(num_samples):
    return pd.Series(np.random.rand(num_samples) * 20)

def generator2(num_samples):
    return pd.Series(np.random.normal(10, 2, num_samples))

def generator3(num_samples):
    return pd.Series(np.random.normal(10, 5, num_samples))

def generator4(num_samples):
    nums1 = np.random.normal(15, 2, int(num_samples/2))
    nums2 = np.random.normal(5, 2, int(num_samples/2))
    nums = np.concatenate([nums1, nums2])
    return pd.Series(nums)

def generator5(num_samples):
    nums1 = np.random.normal(15, 3, int(num_samples * .75))
    nums2 = np.random.normal(-5, 3, int(num_samples * .25))
    nums = np.concatenate([nums1, nums2])
    return pd.Series(nums)

def confidence_interval_definition():
    print("If we used the same sampling method to select different samples and computed an interval estimate for each sample, we would expect the true population parameter to fall within the interval estimates 95% of the time.")