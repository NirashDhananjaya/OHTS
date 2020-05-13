# **IT17113946 N.D Perera**

LAB Structure

1 Windows Machine

FTP Server Planted(Exploiting this ftp server)

1 Kali Machine

A Simple Server is coded in order to send and receive instructions and deliver payloads

![image](https://user-images.githubusercontent.com/36559509/81834166-3c56b000-955e-11ea-816c-86c95d0ea90f.png)


We will be using immunity Debugger(In order to debug and find EIP ESP)

Like I described in the video I have divided my attack into four steps. Step by step I have shown how I developed the program to attack.

1st I installed an ftp server in the windows machine (we will then exploit this ftp server in order gain access to the windows machine) then in the kali linux side I have created a simple server in order to send and receive Data. (this is the server that we are using to send the payload and attack the windows)

![image](https://user-images.githubusercontent.com/36559509/81834485-9bb4c000-955e-11ea-8c32-22e356c6806f.png)

In the left hand side is the basic code that I started developing in there 1st im sending 1000 As to check the Attack is happening


![image](https://user-images.githubusercontent.com/36559509/81834501-a1120a80-955e-11ea-85f0-d82118b3a1e1.png)

Here you can see the 1000 A.


![image](https://user-images.githubusercontent.com/36559509/81834522-a8391880-955e-11ea-9154-526bc56198dd.png)


Here You can see the Error message. Because of the 1st part of the exploit.

In the second step instead of the 1000A we are using a character set we developed this character set from the ./patern\_create.rb -l 1000 ()(we are creating 1000 random characters)

![image](https://user-images.githubusercontent.com/36559509/81834767-0c5bdc80-955f-11ea-83ec-def0412be173.png)

The Code




![image](https://user-images.githubusercontent.com/36559509/81834786-12ea5400-955f-11ea-8dd2-23c728767596.png)


After the exploit memory slots are filled with different different characters .

The main thing we understood from here is the EIP address. ![](RackMultipart20200513-4-14g5mzo_html_79f7cd8c4ea96438.png)

After finding the eip address we are using a module called ./patern\_offset.rb -q \*YOU Must Enter The EIP Address found in immunity debugger this space\* -l 1000

We need 247 characters to get 247 bytes to get to the eip and theres 4 bytes for eip rest is 1000-247



![image](https://user-images.githubusercontent.com/36559509/81834804-1bdb2580-955f-11ea-8e89-5982b5e698eb.png)

IN the 3rd part of the development

payload = &quot;A&quot;\*247 + B\*4&quot; + shellcode + &quot;C&quot;\*(749-len(shellcode))

we are using B\*4 to find the memory address

now our next step is to tell EIP to jump to the next register



![image](https://user-images.githubusercontent.com/36559509/81834820-1f6eac80-955f-11ea-87dd-a65b4482a37d.png)


Now we found the memory address and then we are binding it to our payload

payload = &quot;A&quot;\*247 + &quot;\x53\x93\x42\x7E&quot; + shellcode + &quot;C&quot;\*(749-len(shellcode))

&quot;\x53\x93\x42\x7E ------- memory address in little Indian format 





![image](https://user-images.githubusercontent.com/36559509/81834863-2e555f00-955f-11ea-8647-bc04defb531e.png)


![image](https://user-images.githubusercontent.com/36559509/81834874-33b2a980-955f-11ea-84a1-db9cf3f66368.png)


Finally we are inside windows.
