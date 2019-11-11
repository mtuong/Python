import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.style.use('ggplot') # optional: for ggplot-like style

#df = pd.read_excel('D:\Python\Visualizing Data\data.xlsx')
#print(df)


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    print (df)
    
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()


obj = list(df['INSTANCE'])
y_pos = np.arange(len(obj))

df.plot(kind='barh', 
             stacked=False,
             figsize=(20, 10), # pass a tuple (x, y) size
             )
plt.title('Cluster Resources')
plt.xlabel('Usage of CPU-RAM-HDD')
plt.yticks(y_pos, obj)

plt.show()

