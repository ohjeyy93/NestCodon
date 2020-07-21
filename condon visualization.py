import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

condons = sns.load_dataset("codondepth2.csv")
sns.relplot(x="sample", y="gene", data=condons);