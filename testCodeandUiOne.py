##from future import *
from tkinter import *
import multiprocessing
import time
import sys
import linphone
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication

#from PythonLinphone import chatmessage
class chatmessage:
    def __init__():
         print ("Inside constructor")

    #logging.basicConfig(level=logging.INFO)
    app = QApplication(sys.argv)

    #def log_handler(level, msg):
        #method = getattr(logging, level)
        #method(msg)

    def global_state_changed(*args, **kwargs):
        print ("inside global_state_changed")
        #logging.warning("global_state_changed: %r %r" % (args, kwargs))

    def registration_state_changed(core, call, state, message):
        print ("inside registration_state_changed")
        #logging.warning("registration_state_changed: " + str(state) + ", " + message)
        
    def call_state_changed(core, call, state, message):
        print ('below code will receive call')
        if state == linphone.CallState.IncomingReceived:
            params = core.create_call_params(call)
            core.accept_call_with_params(call, params)
            core.video_display_enabled = True
    def message_received(core, room, message):
        print ('below code will receive message')
        global chatmessa
        chatmessa = message.text
        print (chatmessa)
           
        
    callbacks = {
        'call_state_changed': call_state_changed,
        'message_received':message_received,
        'global_state_changed': global_state_changed,
        'registration_state_changed': registration_state_changed,
       }

    
    #linphone.set_log_handler(log_handler)
    core1 = linphone.Core.new(callbacks, None, None)
    proxy_cfg = core1.create_proxy_config()
    proxy_cfg.identity_address = core1.create_address('sip:dillip_12@sip.linphone.org'.format(username='dillip_12'))
    proxy_cfg.server_addr = 'sip:sip.linphone.org'
    proxy_cfg.register_enabled = True
    core1.add_proxy_config(proxy_cfg)
    auth_info = core1.create_auth_info('dillip_12', None, '12dillip', None, None, 'sip.linphone.org')
    core1.add_auth_info(auth_info)
    
  
  
    core1.iterate
    #initiate call to divyam5
    call = core1.invite('sip:meghav@sip.linphone.org')
    #send chat message to divyam5
    chat_room = core1.get_chat_room_from_uri('sip:meghav@sip.linphone.org') 
    msg1 = chat_room.create_message('hello phanin')
    #chat_room.send_chat_message(msg1)
    

    
    iterate_timer = QTimer()
    iterate_timer.timeout.connect(core1.iterate)
    stop_timer = QTimer()
    stop_timer.timeout.connect(app.quit)
    iterate_timer.start(20)
    stop_timer.start(5000)

    exitcode = app.exec_()
    #sys.exit(exitcode)

class Application(Frame,chatmessage):
    def say_hi(self):
        print ("Hello GUI Development!")

    def createWidgets(self):

        labelframe = LabelFrame(root, text="KPIT Technologies Limited")
        labelframe.pack(fill="both", expand="yes")

        labelframe1 = LabelFrame(root, text="KPIT Technologies Limited")
        labelframe1.pack(fill="both", expand="yes")
    
        LeftFrame1 = Canvas(labelframe, bg="white",bd = 4,relief = GROOVE, height=400, width=200)
        LeftFrame1.pack({"side":"left"})
        LeftFrame1.pack(fill = "both", expand = "yes")
    
        RightFrame1 = Canvas(labelframe, bg="white",bd = 4,relief = GROOVE, height=400, width= 200)
        RightFrame1.pack({"side":"right"})
        RightFrame1.pack(fill = "both", expand = "yes")

        LeftFrame11 = Canvas(labelframe1, bg="grey", height=200, width=60)
        LeftFrame11.pack({"side":"left"})
        LeftFrame11.pack(fill = "both", expand = "yes")

        LeftFrame14 = Canvas(labelframe1, bg="grey", height=100, width=100)
        LeftFrame14.pack({"side":"right"})
        LeftFrame14.pack(fill = "both", expand = "yes")
    
        RightFrame12 = Canvas(labelframe1, bg="grey", height=400, width= 300)
        RightFrame12.pack({"side":"right"})
        RightFrame12.pack(fill = "both", expand = "yes")
        
        LeftFrame13 = Canvas(labelframe1, bg="grey", height=400, width=300)
        LeftFrame13.pack({"side":"right"})
        LeftFrame13.pack(fill = "both", expand = "yes")

       
        
        ReceivedButton=Button(LeftFrame11, text="Receive Call",justify = LEFT)
        ReceivedButton.place(x= 120, y = 100)
        #img = PhotoImage(Image.Open(r"C:\Python27\callButton.bmp"))
        #recimage = Label(ReceivedButton, image = img)
        #recimage.pack()
        
        DisconnectButton=Button(LeftFrame11, text="Diconnect Call",justify = LEFT)
        #photo=PhotoImage(file="mine32.gif")
        #b.config(image=photo,width="10",height="10")
        DisconnectButton.place(x= 10, y = 100)
       
        
       
        
        HonkButton=Button(LeftFrame14,width=30, bg="#d65826" ,relief=GROOVE,text="Honk",justify = LEFT)
        HonkButton.place(x= 15, y = 50)
        
        LightOnButton=Button(LeftFrame14, width=30,text="Light On",relief=GROOVE,justify = LEFT)
        LightOnButton.place(x= 15, y = 80)
        
        UnlockDoorsButton=Button(LeftFrame14, width=30,text="Unlock Doors",relief=GROOVE,justify = LEFT)
        UnlockDoorsButton.place(x= 15, y = 110)

        TurnOffIginitionButton=Button(LeftFrame14, width=30,text="TurnOff Ignition",relief=GROOVE,justify = LEFT)
        TurnOffIginitionButton.place(x= 15, y = 140)

        
		#frame first
        L1 = Label(LeftFrame13, text="Location", bg="grey", height = 4)
        L1.place(x=20, y = 30)
        E1 = Entry(LeftFrame13, bd =2, width = 50)
        E1.place(x= 120, y = 52)

        L2 = Label(LeftFrame13, text="ID", bg="grey")
        L2.place(x=20, y = 100)
        E2 = Entry(LeftFrame13, bd =2, width = 50)
        E2.place(x= 120, y = 100)

        L3 = Label(LeftFrame13, text="Vehicle number", bg="grey")
        L3.place(x=20, y = 160)
        E3 = Entry(LeftFrame13, bd =2, width = 50)
        E3.place(x=120, y = 160)

        L4 = Label(LeftFrame13, text="Vehicle no", bg="grey")
        L4.place(x=20, y = 220)
        E4 = Entry(LeftFrame13, bd =2, width = 50)
        E4.place(x=120, y = 220)

        #frame change
        L5 = Label(RightFrame12, text="Direction", bg="grey", height = 4)
        L5.place(x=20, y = 30)
        E5 = Entry(RightFrame12, bd =2, width = 50)
        E5.place(x= 120, y = 50)

        L6 = Label(RightFrame12, text="Passengers", bg="grey")
        L6.place(x=20, y = 100)
        E6 = Entry(RightFrame12, bd =2, width = 50)
        E6.place(x= 120, y = 100)

        L7 = Label(RightFrame12, text="Time", bg="grey")
        L7.place(x=20, y = 160)
        E7 = Entry(RightFrame12, bd =2, width = 50)
        E7.place(x=120, y = 160)

        L8 = Label(RightFrame12, text="TIME", bg="grey")
        L8.place(x=20, y = 220)
        E8 = Entry(RightFrame12, bd =2, width = 50)
        E8.place(x=120, y = 220)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
print (app.message_received())
root.title("Welcome to app")
root.geometry('2000x1000')

app.mainloop()
ch = chatmessage()
print (ch.chatmessage)
root.destroy()
root.quit()
