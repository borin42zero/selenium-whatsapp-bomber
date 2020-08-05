# -*- coding: utf-8 -*-
"""
Created on Thu May 03 20:23:51 2018

@author: Robin
"""

import Tkinter as tk

root = tk.Tk()


label_victim =  tk.Label(root, text="Contact Name: ") 
label_msg = tk.Label(root, text="Message: ")
  
victim = tk.Entry(root)
msg = tk.Entry(root)

label_msg_style = tk.Label(root, text="Message Style: ") 
bottomFrame = tk.Frame(root)
choose1 = tk.Button(bottomFrame,text="Regular")
choose2 = tk.Button(bottomFrame,text="Nerf-Mode")



label_victim.grid(row=0,column=0)
label_msg.grid(row=1,column=0)
victim.grid(row=0,column=1)
msg.grid(row=1,column=1)
label_msg_style.pack()
bottomFrame.pack(side=tk.BOTTOM)









root.mainloop()