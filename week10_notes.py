#!\usr\bin\python

''' WEEK 10

CONNECTING TO A ROUTER VIA SSH

Create a program that connects to a router over ssh and then retrieves a show version output. 

How to use ParamikoSSH to connecto to a router.

Paramiko is a python library.

There can be some nuances depending on how you connect to (some hp switches you have to hit continue to login)

Step 1. INstall paramiko
    sudo pip install paramiko

Step 2.
    import paramiko
    ip = '10.0.0.1'
    username = 'user'
    password = 'pass'


Step 3.

THen create a variable that is an instance of the SSHClient() class.

remote_conn_pre = paramiko.SSHClient()

Step 4.
Blindly accepting the ssh host key is not reccommended, but you can set it so it auto add.

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

Step 5.
So now lets start the connection
remote_conn_pre.connect(ip, username=username, password=password)

Step 6. Assign a new variable and invoke the shell
remote_conn = remote_conn_pre.invoke_shell()

dir(remote_conn) will show you what's availiable to you.

Step 7. Read in the content from the router in bytes
output = remote_conn.recv(5000) --- bytes
print(output)

Step 8. Let's send a command down the channel. 
So now we have an ssh connection established to a router, and a way of reading in text.
Let's send in a new line
remote_conn.send("\n")
output = remote_conn.recv(5000) 
print(output)

remote_conn.send("show version\n")
remote_conn.recv(65535) <- That's the max that can be read)


Step 9. Let's turn this into a script:


'''
import time
import paramiko

def disable_paging(remote_conn, command="terminal length 0\n", delay=1):
    # the reason the delay is a variable, is because that delay expectation might
    # change based on the model. 
    remote_conn.send("\n")
    remote_conn.send(command)
    time.sleep(delay)
    output = remote_conn.recv(65535)
    return output

if __name__ == "__main__":
    ip = '10.5.0.1'
    username = 'borr'
    password = 'test'
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip, username=username, password=password)
    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(5000)
    # DIsable pagaing, you have to pass remote_conn into the function because 
    # you're using remote_conn in the function.
    disable_paging(remote_conn)
    remote_conn.send("\n")
    remote_conn.send("show version\n")
    # wait for 1 second to mimic human interaction
    time.sleep(1)
    output = remote_conn.recv(65535)
    # Always remember to close your SSH connection. In this case we need to
    # close the pre
    remote_conn_pre.close()
