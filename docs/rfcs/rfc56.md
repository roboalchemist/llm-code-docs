---
rfc: 56
title: "Third Level Protocol"
date: June 1970
---
1. Stable state: receive-logger at foreign host listening to User 0,
Socket 0.

2. Local user calls send-logger.

3. Send-logger calls CONNECT (port, 2N+1, <foreign host#,0,0>).

4. Send-logger calls LISTEN (port, <local host#, user#, 2N>).

5. Foreign logger's LISTEN is answered, and he is told local user
number, host and #2N+1.

6. Foreign logger looks for available sockets (2M and 2M+1).  If they
exist and it is able to establish connection, it accepts and then
immediately closes the link.

7. Foreign logger calls CONNECT (port, 2M+1, <local host#, user#,
2N>).

8. Foreign logger calls LISTEN (port, <local host#, user#, 2M>).

9. Send-logger has listened to 2N and accepts link, then calls
CONNECT (port, 2N+1, <foreign host#, user#,2M>).

10. Receive-logger, which is listening on 2M, accepts link.

11. Loggers activate appropriate handlers.

12. When the user is finished, sender closes down both links.

This basic method of establishing a full duplex connection should be
standard throughout the network. The particular way each installation
handles the implementation of the sender, receiver, and the two loggers
is of no consequence to the network and is highly machine dependent.
(Even the fact of needing a sender and receiver is machine dependent in
that some members of the network might be able to handle their functions
in other ways.) However, some conventions must be established regarding
communication between the sender and receiver, or their equivalents.

Network Standard Code

In order to facilitate use of the network, we propose the convention
that all teletype-to-foreign-monitor communication be done using 128
character USASCII. (This is the code used by the IMP's and is in the
appendix to the IMP operating manual.) It makes sense to require
machines to make only one conversion to a standard code, than to have to
make conversions to every code on the net.

In addition, since most of the network machines use ASCII as their
internal character code, it will be no trouble for them. Even those
machines that use a different code must translate to and from ASCII in
order to communicate with local teletypes. Extending this translation to
the network should cause very little trouble. We envision this
translation as taking place in the sender and receiver, but again that
is implementation dependent.

If ASCII is adopted as a standard, we would suggest that all non-ASCII
machines create a monitor to the machine's internal code. This would
make the complete character set available to those who wished to use it
(and were willing to write a simple conversion routine for the local
machine.) In this way, those users who wanted to could use any machine
on the net from their teletype, without requiring their machines to have
records of all the network codes, and yet could use the full power of
the foreign machine if they wanted.

Again, this standard applies only for teletype-to-foreign-monitor
communication.

Break Characters

A standard way of handling the break character has to be established for
the network and be included in the protocol. Problems with the break
character arise in several contexts. First, there are two distinct
purposes served by the break character. One is as a panic button. This
says, "I do not care what is happening, stop and get me out to monitor
level now." This command is executed immediately upon receipt, and is
most commonly used to get out of a program that one does not want to be
in (e.g., one that is in an infinite loop, etc.)

The other purpose that is served is that of an exit from a subsystem, or
on a machine with a forking structure as a method to get back to the
next higher level fork. This second purpose is not an immediate one in
that the user wants the system to finish all that he has told it to do
before exiting.

We assume that there does not exist in every system 1) a way of
performing each of these functions, or 2) a clear cut distinction
between the calling and operation of the two. Furthermore, there are
subtle distinctions as to how each system treats the commands.

The panic button function can easily be performed by the proposed
control command <INT>. This function must be accomplished by using a
control command, since a program can enter a state where it is accepting
no input: hence, the program cannot be aborted by sending it a message
down the teletype link. There is no reason to worry about the race
condition caused by sending this command down the control link since its

whole purpose is to force the machine to disregard everything else the
user has sent.

In our implementation of this, we would ask the user to specify to the
logger a seldom used character that he wants to be his foreign panic
button. Then, it would be a simple task for the sender to map this
character into an <INT> command, which the foreign machine must
interpret properly. This scheme would work well for most machines, but
some may lend themselves to different ways of generating the <INT>.

The other problem that presents itself is what to do if the foreign
machine's "exit" character is the same as the local machine's.  The
problem is that while a user is talking to a foreign machine, he would
want to be in a transparent mode, where everything he types is sent
directly to the other machine. The way he would get himself out of this
mode is to type either his machine's "exit" character or its panic
button. Thus, if the foreign machine has the same one, there would be no
way to send it. The way out of this is the same as above--merely a
mapping of another seldom used character into the foreign machine's
"exit" character. This type of mapping can be carried as far as each
installation deems necessary. Giving the user complete control over
translation is helpful in that it allows him to user characters that his
teletype cannot generate.

Command Message Formats

Each site should establish its now conventions about when to send a
monitor command string, and in what size chunks. When performing a
routine operation, one might want to send several command lines as a
single message. If working with the monitor as usual, a reasonable break
point might be at every carriage return. When using a highly interactive
language such as QED, one might decide character-by-character
transmission was a necessity. We feel that each user should have the
choice between these three methods (and possible more). Furthermore, the
user should be able to change between each mode at will. The differences
in syntax of the send-message commands mentioned above should be noted.
For the first, a special send-message command character must be defined,
and it should not be sent along with the message. For the second, the
carriage return acts dually as the send-message command and as a command
delimiter. Therefore it must be sent with the message. Finally, the case
of character-by-character transmission with its implicit send command
should pose no significant problems.

The preceding discussion is meant to imply also that the receiver must
be able to buffer up each of the above types of transmission into a form
acceptable to its own monitor interface.

In addition, all echoing should be done in the local host, with the
foreign machine suppressing its echoes (if it can.)

We would like to thank Carl Ellison (of Utah) for his valuable
suggestions and criticisms of this work, and Jim Curry (of Utah) for his
encouragement and support of the effort.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Jon Ribbens 7/97 ]
