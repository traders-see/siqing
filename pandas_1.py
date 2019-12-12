import pandas as pd
print(pd.__version__)  # 查pandas版本
import os
#打印当前目录
current_dir = os.path.dirname(os.path.dirname(__file__))
print(current_dir)
#打印当前目录下其他目录
path = current_dir + '/siqig/'
print(path)