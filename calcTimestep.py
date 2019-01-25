import tkinter 

allFont = ('Arial',12)

window = tkinter.Tk()
window.title('calcTimestep')
window.geometry('400x300')

rpmText = tkinter.Label(window, text='RPM', font=allFont, padx=10, pady=5)
rpmText.grid(row=0, sticky='w')
rpmEntry = tkinter.Entry(window, width=10, font=allFont)
rpmEntry.insert(0,'600')
rpmEntry.grid(row=0, column=1)

degText = tkinter.Label(window, text='Deg / timestep', font=allFont, padx=10, pady=5)
degText.grid(row=1, sticky='w')
degEntry = tkinter.Entry(window, width=10, font=allFont)
degEntry.insert(0,'5')
degEntry.grid(row=1, column=1)

nrevText = tkinter.Label(window, text='Revolutions', font=allFont, padx=10, pady=5)
nrevText.grid(column=0, row=2, sticky='w')
nrevEntry = tkinter.Entry(window, width=10, font=allFont)
nrevEntry.insert(0,'40')
nrevEntry.grid(row=2, column=1)

def clicked():
    res = float(rpmEntry.get()) + float(degEntry.get())
    omegaText.configure(text=res)

btn = tkinter.Button(window, text='Calculate', command=clicked, font=allFont)
btn.grid(row=3, column=1)

omegaText = tkinter.Label(window, text='Omega (rad/s)', font=allFont, padx=10, pady=5)
omegaText.grid(row=4)
omegaEntry = tkinter.Entry(window, width=10, font=allFont)
omegaEntry.insert(0, '62.83')
omegaEntry.grid(row=4, column=1)
omegaEntry.config(state='disabled')

timestepText = tkinter.Label(window, text='Timestep length (s)', font=allFont, padx=10, pady=5)
timestepText.grid(row=5)
timestepEntry = tkinter.Entry(window, width=10, font=allFont)
timestepEntry.insert(0, '0.0028')
timestepEntry.grid(row=5, column=1)
timestepEntry.config(state='disabled')

ntimestepsText = tkinter.Label(window, text='No. of timesteps', font=allFont, padx=10, pady=5)
ntimestepsText.grid(row=6)
ntimestepsEntry = tkinter.Entry(window, width=10, font=allFont)
ntimestepsEntry.insert(0, '2880')
ntimestepsEntry.grid(row=6, column=1)
ntimestepsEntry.config(state='disabled')

window.mainloop()

