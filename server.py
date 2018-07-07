import socket
import threading
import os
import sys
from tkinter import *
      
def receive_message():
	global conn
	#obtaining client host name and port
	conn, addr = server.accept()
	info_5=str(addr) + ' has joined the server.'
	message_list.insert(END,info_5)
	message_list.insert(END,' ')
	message_list.insert(END,'MESSAGE FACILITY ACTIVE')
	message_list.insert(END,' ')
	while True:
		#receiving messages from the client
		incoming_message=conn.recv(4096)
		if not incoming_message:
			message_list.insert(END,' ')
			message_list.insert(END,'Client Disconnected')
			message_list.insert(END,' ')
			sys.out()
		else:
			incoming_message=incoming_message.decode()
			incoming_message='<'+str(addr)+'>' + ' : ' + incoming_message
			message_list.insert(END,incoming_message) 
	
def send_message():
	global conn
	#getting entry from the entry box input
	message = send_entry.get()
	#encoding message
	encoded_message = message.encode()
	conn.send(encoded_message)
	message='<You> : '+message
	#displaying message on listbox widget
	message_list.insert(END,message)
	#clearing entrybox field
	send_entry.delete(0,END)

#builds the GUI window
root=Tk()

#setting the resolution of the GUI window
root.geometry("520x410")

#Creating two frames to accomodate widgets
topframe=Frame(root)
bottomframe=Frame(root)

#Creating widgets to be used in the application
message_scrollbar=Scrollbar(topframe)
labelheading=Label(topframe,text="----------------Message History----------------")
message_list=Listbox(topframe,width=62,height=20)
send_button=Button(bottomframe,text="SEND",width=10,height=1,bg="grey",fg="white",command=send_message)
send_entry=Entry(bottomframe,width=50)

#Assigning frame location in the GUI window
topframe.pack(side=TOP)
bottomframe.pack(side=BOTTOM)

#inserting message in listbox
send_entry.insert(END,'Type your message here...')
#Assigning position to the label widget in the topframe
labelheading.pack(side=TOP)

#Assigning position to the lisbox and scrollbar widget in the topframe
message_list.pack(side=LEFT,fill=Y)
message_scrollbar.pack(side=LEFT,fill=Y)

#Assigning position to the entrybox and button widget in the bottomframe
send_entry.pack(side=LEFT)
send_button.pack(side=LEFT)

#linking scrollbar and lisbox widget
message_scrollbar.config(command=message_list.yview)
message_list.config(yscrollcommand=message_scrollbar.set)

#creating socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#server host name
host = 'jiten-Vostro1310'

#server host IP
host_ip=socket.gethostbyname(host)

#port number
port = 8080

#messages to be displayed
info_1='Server will start on host : '+ '< '+str(host)+': '+ str(host_ip)+'> : '
info_2='Using Port : '+str(port)

#displaying messages on the listbox widget
message_list.insert(END,info_1)
message_list.insert(END,info_2)

#binding socket to host and port of the server
server.bind((host,port))

#messages to be dispalyed
info_3= 'Server done binding to host and port successfully.'
info_4= 'Server is waiting for incoming connections.'

#displaying messages
message_list.insert(END,info_3)
message_list.insert(END,info_4)

#server will be listening to one client
server.listen(1)

#used for threading
thread_send = []
thread_rcv = []
num_threads = 3

#threading
for loop_1 in range(num_threads):
	thread_rcv.append(threading.Thread(target = receive_message))
	thread_rcv[-1].start()

#setting application name
root.title('SERVER CHATBOX')
#infinite loop to run display the window continuosly
root.mainloop()
