import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as ttk
import sys
import time



HOST = '127.1.0.1'
PORT = 9999

LISTENER_LIMIT = 5
active_clients = []

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
FONT = ("Helvetica", 17)
FONT1 = ("Helvetica",25)
WHITE= 'white'
SMALL_FONT = ("Helvetica", 13)
BUTTON_FONT = ("Helvetica", 13)

root = tk.Tk()
root.geometry("500x250")
root.title("Secure chat App")
root.resizable(False, False)


def connect():
    print("Yeah bro!! its working")

# client, address = server.accept()
# Main function
def main():
    root.mainloop()

    # Creating the socket class object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        # Provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:
        client, address = server.accept()
        message = input(str("You:>>"))

        message = message.encode()
        client.send(message)
        incoming_message = client.recv(1024)

        incoming_message = incoming_message.decode()
        print("Clienr:>>", incoming_message)

        # client, address = server.accept()
        # print(f"Successfully connected to client {address[0]} {address[1]}")

        # threading.Thread(target=client_handler, args=(client, )).start()


def send():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client, address = server.accept()
    message = input(str("You:>>"))
    message = message.encode()
    client.send(message)


top_frame = tk.Frame(root, width=500, height=80, bg= DARK_GREY)
top_frame.grid(row=0, column=0, sticky= tk.NSEW) #north,south, east,west

middle_frame = tk.Frame(root, width=500, height=550, bg=MEDIUM_GREY)
middle_frame.grid(row=1, column=0, sticky= tk.NSEW)

# bottom_frame = tk.Frame(root, width=500, height=80, bg=DARK_GREY)
# bottom_frame.grid(row=2, column=0, sticky= tk.NSEW)

username_lable = tk.Label(top_frame, text="Sender", font=FONT1, bg= DARK_GREY, fg ='white')
username_lable.grid(sticky= tk.NSEW, padx=200)

plaintext = tk.Label(middle_frame, text= "Plaintext:", font= FONT,bg= MEDIUM_GREY, fg ='white', anchor='w')
plaintext.grid(row=2, column=0,sticky= tk.NSEW, pady=10)

plaintextbox = tk.Entry(middle_frame, font= FONT,bg= MEDIUM_GREY, fg ='white',)
plaintextbox.grid(row=2, column=1,sticky= tk.NSEW, pady=10)

key_lable = tk.Label(middle_frame,text= "Key:",font= FONT,bg= MEDIUM_GREY, fg ='white', anchor="w")
key_lable.grid(row=3, column=0,sticky= tk.NSEW, pady=10)

keybox = tk.Entry(middle_frame, font= FONT,bg= MEDIUM_GREY, fg ='white',)
keybox.grid(row=3, column=1,sticky= tk.NSEW, pady=10)

technique_label = tk.Label(middle_frame,text= "Technique:",font= FONT,bg= MEDIUM_GREY, fg ='white', anchor="w")
technique_label.grid(row=4, column=0,sticky= tk.NSEW, pady=10)

options = ["Caesar cipher", "Monoalphabetic", "Polyalphabetic", "Hill cipher"
           , "Playfair", "OTP", "Rail fence", "Columnar"
           , "DES", "AES", "RC4", "RSA", "ECC"
           , "DH for key exchange", "Hashing (SHA) for integrity checking", "DSA for signature"]


clicked = StringVar()
clicked.set(options[0])

techniquetype = tk.OptionMenu( middle_frame, root, clicked, *options) #command = select and write select function sepreately
techniquetype.grid(row=4, column=1, pady=10 )

techniquebutton = (tk.Button(middle_frame,text = "Encypt", font= BUTTON_FONT  , bg = OCEAN_BLUE, fg =WHITE, command= encrypt))
techniquebutton.grid(row=4, column=2, pady=10)

cipherlabel = tk.Label(middle_frame,text= "Ciphertext:",font= FONT,bg= MEDIUM_GREY, fg ='white', anchor="w" )
cipherlabel.grid(row=5, column=0,sticky= tk.NSEW, pady=10)

ciphertextbox = tk.Entry(middle_frame, font= FONT,bg= MEDIUM_GREY, fg ='white',)
ciphertextbox.grid(row=5, column=1,sticky= tk.NSEW, pady=10)

sendbutton = (tk.Button(middle_frame,text = "Send", font= BUTTON_FONT  , bg = OCEAN_BLUE, fg =WHITE, command= send))
sendbutton.grid(row=5, column=2, padx=20, pady=10)




if __name__ == '__main__':
    main()