from tkinter import *

def gui(pre):
	w = Tk()
	sec=Label(w,text=pre,fg="red",bg="black",font=("Helvetica", 32))
	sec.pack()
	w.after(1000, lambda: w.destroy())
	w.mainloop()

def output(pred):
    if pred==0:
        gui("SPEED LIMIT-20Km/Hr")
    elif pred==1:
        gui("SPEED LIMIT-30Km/Hr")
    elif pred==2:
        gui("SPEED LIMIT-50Km/Hr")
    elif pred==3:
        gui("SPEED LIMIT-60Km/Hr")
    elif pred==4:
        gui("SPEED LIMIT-70Km/Hr")
    elif pred==5:
        gui("SPEED LIMIT-80Km/Hr")
    elif pred==6:
        gui("END OF SPEED LIMIT ZONE!")
    elif pred==7:
        gui("SPEED LIMIT-100Km/Hr")
    elif pred==8:
        gui("SPEED LIMIT-120Km/Hr")
    elif pred==9:
        gui("NO OVERTAKING!")
    elif pred==10:
        gui("NO PASSING FOR VEHICLES OVER 3.5TONS!")
    elif pred==11:
        gui("CROSSROADS!")
    elif pred==12:
        gui("PRIORITY ROADS!")
    elif pred==13:
        gui("DISTANCE TO 'GIVE-WAY' LINE!")
    elif pred==14:
        gui("STOP!")
    elif pred==15:
        gui("NO VEHICLES!")
    elif pred==16:
        gui("TRUCK CROSSING!")
    elif pred==17:
        gui("NO ENTRY FOR VEHICULAR TRAFFIC!")
    elif pred==18:
        gui("HIDDEN DIP!")
    elif pred==19:
        gui("BEND TO LEFT!")
    elif pred==20:
        gui("BEND TO RIGHT!")
    elif pred==21:
        gui("DOUBLE BEND FIRST TO LEFT!")
    elif pred==22:
        gui("UNEVEN ROAD!")
    elif pred==23:
        gui("SLIPPERY ROAD!")
    elif pred==24:
        gui("ROAD NARROWS ON RIGHT!")
    elif pred==25:
        gui("MEN AT WORK!")
    elif pred==26:
        gui("TRAFFIC SIGNALS!")
    elif pred==27:
        gui("PEDESTRIANS PROHIBITED!")
    elif pred==28:
        gui("PEDESTRIAN CROSSING!")
    elif pred==29:
        gui("CYCLE ROUTE AHEAD!")
    elif pred==30:
        gui("RISK OF ICE!")
    elif pred==31:
        gui("WILD ANIMALS!")
    elif pred==32:
        gui("NATIONAL SPEED LIMIT APPLIES!")
    elif pred==33:
        gui("TURN RIGHT AHEAD!")
    elif pred==34:
        gui("TURN LEFT AHEAD!")
    elif pred==35:
        gui("AHEAD ONLY!")
    elif pred==36:
        gui("JUNCTION AHEAD-RIGHT!")
    elif pred==37:
        gui("JUNCTION AHEAD-LEFT!")
    elif pred==38:
        gui("KEEP RIGHT!")
    elif pred==39:
        gui("KEEP LEFT!")
    elif pred==40:
        gui("MINI ROUNDABOUT!")
    elif pred==41:
        gui("NO CARS ALLOWED!")
    elif pred==42:
        gui("HEAVY VEHICLES NOT ALLOWED!")
    else:
        print("")


output(1)
