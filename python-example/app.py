### This is python example file ###

import numpy as np
import pandas as pd
import os
from pathlib import Path

localDir = Path(os.path.dirname(os.path.realpath(__file__))) # This files absolute path

df = pd.read_csv(localDir/'dataTarget'/'data.csv', header=None) 

df.apply(np.sum, axis=1).to_csv(localDir/'dataOut'/'data.csv')
