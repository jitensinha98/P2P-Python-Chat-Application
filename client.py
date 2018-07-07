"""This is the Client portion GUI of the P2P Chat Application.
   The client is capable of receiving and sending messages to the server application."""

import socket
import sys
import os
import time
import threading
from tkinter import *

#This function is used to receive messages from the server
def receive_message():
	while True:
		incoming_message=client.recv(4096)
		if not incoming_message: 
			message_list.insert(END, ' ')	
			message_list.insert(END, 'DISCONNECTED FROM SERVER')
			message_list.insert(END, ' ')
			sys.out()
		else:
			incoming_message=incoming_message.decode()
			incoming_message='<'+host+'('+host_ip+')'+'> : '+incoming_message
			message_list.insert(END, incoming_message)

#This function is used to send messages to the server				
def send_message():
	message=send_entry.get()
	encoded_message=message.encode()
	client.send(encoded_message)
	message='<You> : '+message
	message_list.insert(END, message)
	send_entry.delete(0,END)

#used for multithreading
thread_send = []
thread_rcv = []
num_threads = 2

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

#initializing socket
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#server host-name and port number
#change it to your desirable host and port of the server
host = 'jiten-Vostro1310'
port = 8080

#getting server host IP address 
host_ip=socket.gethostbyname(host)

#connectiing the client to the server
client.connect((host,port))

#obtaining client information
client_info=client.getsockname();

#storing the messages to be displayed
info_1='Connected to chat server : '+str(host_ip)
info_2='USING PORT 8080'
info_3='CLIENT IP AND PORT : '+str(client_info)
info_4='MESSAGE FACILITY: ACTIVE'

#displaying the messages in the listbox
message_list.insert(END, info_1)
message_list.insert(END, info_2)
message_list.insert(END, info_3)
message_list.insert(END, ' ')
message_list.insert(END, info_4)
message_list.insert(END, ' ')

#enabling multi-threading for receive_message() 
for loop_1 in range(num_threads):
    thread_rcv.append(threading.Thread(target = receive_message))
    thread_rcv[-1].start()

#changing name of the application
root.title('CLIENT CHATBOX')

#infinite loop to be executed to display the GUI
root.mainloop()
