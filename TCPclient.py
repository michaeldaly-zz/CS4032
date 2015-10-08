# CS4032 Lab01 Submission
# Michael Daly/McAndrew #10380775
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:  
    # Send get request including message 'test'
    message = 'GET /echo.php?message=test HTTP/1.1\r\n\r\n'
    print >>sys.stderr, 'sending "%s"' % message
    #Sendd the data to server
    sock.sendall(message)

    # Look for the response
    received = 0
    expected = len(message)
    
    #To ensure both strings are same length
    while received < expected:
    	#Accept response from server
        data = sock.recv(1024)
        received += len(data)
        #Recieve and print the response from server
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
