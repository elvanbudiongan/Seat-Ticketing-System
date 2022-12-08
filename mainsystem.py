from tkinter import *


root = Tk()
root.geometry("500x300")
root.title("SEAT TICKETING SYSTEM")


root2 = Tk()
root2.geometry("530x445")
root2.title("SEAT TICKETING SYSTEM")


label1 = Label(root, text= "SEAT TICKETING SYSTEM", font = ( 'arial',20,'bold'), fg = "#000000", justify= "center")
label1.pack(pady=40)

label2 = Label(root, text= "Enter room code",justify= "left")
label2.pack()
inputentry = Entry(root)
inputentry.pack()

B1= Button(root, text ="apply",command = lambda: [msg_pop(),update_color()])
B1.pack()
B2= Button(root, text ="reset",command=lambda :[reset_color()])
B2.pack()


list = []
index=0
varr=0
for i in range(1,9):
    var = 0
    charr=65
    for j in range(8):
        box=Label(root2, text = chr(charr)+str(i), bg='green', width=8, height=3)
        box.grid(row =varr, column=var,padx=2,pady=2)
        list.insert(index,str(chr(charr)+str(i)))
        charr+=1
        index+=1
        var=var+1
    varr=varr+1

def msg_pop():
    global pop
    pop = Toplevel(root)
    pop.geometry("200x100")
    pop.title("SEAT TICKETING SYSTEM")
    my_dict=list
    string_inp = str(inputentry.get())
    if string_inp in my_dict:
        pop_label = Label(pop, text=string_inp + " is occupied!", justify="center")
        pop_label.pack()
        pb = Button(pop, text="ok", command=pop.destroy)
        pb.pack(pady=20)
    else:
        pop_label3 = Label(pop, text= "ERROR:: INPUT IS NOT IN THE LIST!", justify="center")
        pop_label3.pack()
        pb = Button(pop, text="ok", command=pop.destroy)
        pb.pack(pady=20)




def update_color():
    for wgd in root2.winfo_children():
        if wgd['text'] == inputentry.get():
            wgd['bg']='red'

def reset_color():
    for wgd in root2.winfo_children():
            wgd['bg']='green'


root.mainloop()
root2.mainloop()