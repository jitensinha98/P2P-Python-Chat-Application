# P2P-Python-Chat-Application
P2P Chat application written in python with tkinter GUI framework.

## Programming Language used
- python 3

## Modules used
- Socket
- Tkinter

## Module installation guidelines
Execute the following bash commands on terminal.
```
sudo apt-get install python3-tk
sudo apt-get update
sudo apt-get upgrade
```
###### Socket is a default module present in python

## Description
Python socket programming is done to initialize and connect the server and the client portion of the application.
Tkinter module is used to design the GUI and ease the usability of the users.

This chat apllication is able to communicate with the client over a LAN network.
In order to support users outside the LAN network,the users are required to enable DMZ and set DMZ Host IP Address to be the internal IP address of their computer , assuming the user to be the host.

## Steps to use the application
- Before using ,the users are adviced to change **HOST and PORT** variables in **server.py** program with their device HOST name and desirable port number.

- In order to execute the application,run server.py script first and then execute client.py.The Server should automatically connect to the client and dislay **MESSAGE FACILITY ACTIVE** upon successfull connection.

## Author
- ***Jiten Sinha***-initial work-[LinkedIn](https://www.linkedin.com/in/jiten-sinha-131043159/)

## Licesnse
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/jitensinha98/P2P-Python-Chat-Application/blob/master/LICENSE) file for details.
