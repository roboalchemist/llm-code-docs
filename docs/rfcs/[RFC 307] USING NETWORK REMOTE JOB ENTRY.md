---
title: "Using Network Remote Job Entry"
date: February 1972
---
1. Help

If the user types "?" RJSAP will echo the "?" and list the
valid set of commands (see below).

2. Message to RJS

If the first character of a command is a "/" all subsequent
characters up to a "return" are transmitted to RJS on the
operator input connection.  See RFC 189 for the syntax and
semantics of these commands.

An operator input message can be cancelled with the RUB OUT key
or backspaced using BACKSPACE.

3. Send a Job

When the user types "S" RJSAP echoes "SEND SOURCE DECK FROM
FILE".  The user then enters the file name containing his job
followed by a "return."  Obviously the file must already exist.
If the file is ok and is transmitted successfully, both RJSAP
and RJS will print an acknowledgement on the user's terminal
(see example below).

4. Retrieve Job Output-Printer

The user can retrieve printed output by entering "PR".  RJSAP
will echo "PRINT OUTPUT TO FILE".  The user then enters the
files name where he wants the output.  This can be a new file
or even a device such as the printer or teletype.  When the
print output is completely received, the RJSAP will print an
acknowledgment (see example).

5. Retrieve Job Output-Punch

This function is currently not implemented, pending a decision
on the use of this channel between a PDP-10 and a 360.

6. Transmission Status

For long transmissions of job input or output it may be
desirable to check on the progress of the transmission.  Typing
"R" will cause RJSAP to echo "REPORT ON TRANSMISSIONS--",
followed by a record count for the job input and printer output
channels.

7. Termination

If the user types a "Q" at the start of a command, RJSAP will
echo "QUIT IN PROGRESS" and terminate.  This is the preferred
way of terminating the program.  (Rather than just ^C).

NOTE: Since RJSAP has not been extensively used, we expect it to be
improved and modified in the future.  Thus, the last section of this
RFC -- the explanation of the use of RJSAP -- will be kept in file

```
   <HARSLEM>RJSACCESSPROGRAM.EXPLANATION on the Rand PDP-10 and be
   updated appropriately.

```

Sample Session

The follows is a sample session using RJS from RJSAP on the Rand
PDP-10.  All user inputs have been underlined (shown as _text_ ).

TENEX 1.28,RAND EXEC 1.33.1                          Rand Exec Prompt
@_LOGIN_                                        \
(USER) _HARSLEM_                                 \   User Logs In
(PASSWORD)______                                 /
(ACCOUNT #)_1__                                 /
JOB 12 ON TTY10 25-FEB-72 11:12                      System Acknowledges
@_RJS_                                               User Starts RJS
Access Program

RJS REMOTE ACCESS PROGRAM

HELLO ERIC

YOU ARE CONNECTED TO RJS                          \
NRJ876I NETWORK REMOTE JOB SERVICE READY           \
RJS750I TERMINAL NETRAND HAS SIGNED ONTO RJS        \ RJS Recognizes
RJS652I INFORMATION ALERT -                         / Terminal ID and
RJS250I OS COLDSTARTED 4:30 PM 24 FEB ALL JOBS     /  Prints System
**IN SYS LOST AND MUST BE RESUBMITTED             /   News Messages
RJS650I OS COLDSTARTED 11:07 FEB 25, ALL JOBS LOST MUST RESUBMIT_
_?_
VALID COMMANDS ARE:                                User asks for
SEND A SOURCE FILE                                 Valid Commands
PRINT OUTPUT RETRIEVAL
PUNCH OUTPUT RETRIEVAL
REPORT ON STATUS OF TRANSMISSIONS
PRECEDE RJS OPERATOR COMMANDS WITH A SLASH
QUIT TO TERMINATE THE PROGRAM
_/STATUS JOBS_
RJS804I TERMINAL NETRAND HAS NO JOBS ACTIVE        User Sends Message to
_/STATUS LINES_                                    RJS asking Job Status
RJS800I TERMINAL GSM     ACTIVE ON LINE 1          User asks RJS to
RJS809I PUNCH REROUTE = ENGR                       show Active Users
RJS800I TERMINAL ENGR    ACTIVE ON LINE2
RJS800I TERMINAL CSCSRC  ACTIVE ON LINE7
RJS800I TERMINAL NETRAND ACTIVE ON LINE8
_S_END SOURCE DECK FROM FILE _TESTA.;1_
TESTA.; TRANSMITTED TO RJS                         User Sends Job to RJS
26 CARDS  SENT                                     Both Access
RJS534I JOB MES727DS ACCEPTED BY RJS - 0000027     Program and RJS Ack
**CARDS READ                                       Job Submission

_/STATUS JOBS_
RJS810I TERMINAL NETRAND HAS THE FOLLOWING JOBS IN RJS
RJS812I MES272DS SPL(A) 001                        User Asks Job Status
\                                     And Sees his job
/                                     being Spooled.
\
/
(SOMETIME LATER)
/
\
_/STATUS JOBS_
RJS810I TERMINAL NETRAND HAS THE FOLLOWING JOBS     User Checks and
**IN RJS
RJS812I MES727DS XEQ   000                          Finds his job ready
/
\
(SOMETIME LATER)
/
\
/
\
_/STATUS JOBS_                                      User sees job
RJS810I TERMINAL NETRAND HAS THE FOLLOWING JOBS     has been run
**IN RJS
RJS812I MES727DS PPT 060                            Print output ready
_PR_INT OUTPUT TO FILE _LPT_:[CONFIRM]              User asks for output
directly to printer

_R_EPORT ON TRANSMISSIONS--
NO SEND IN PROGRESS                                User checks to see
PRINT TO FILE LPT: RECORD COUNT=88                  the print retrieval
LPT:RECEIVED 197 PRINT LINES                        running
_Q_UIT IN PROGRESS                                  User Terminates
BYE, BYE BANANA                                     Access Program

@_LOGOUT_                                           User Logs Out
KILLED JOB 3, USER HARSLEM, ACC 1, TTY 10, AT 2/25/72 1300
USED 0:0:21 IN 1:12:52

[This RFC was put into machine readable form for entry]

```
    [into the online RFC archives by H�l�ne Morin, Viag�nie, 12/99]

```