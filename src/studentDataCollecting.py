import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
#pd.set_option('max_columns', 200)

student_data = pd.read_csv('/Users/tjohm/Coding/PYTHON/Student_data_pipeline/Student_Data/student_performance_dataset.csv')

#print(student_data.shape) #(3000, 32)

