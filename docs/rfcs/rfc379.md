---
title: "IBM's Time Sharing Option (\"TSO\") is now available at CCN for use via"
---
1.  To obtain a list of TSO commands enter:  "help commands"

2.  To get detailed information on syntax and function of a particular
command, enter: "help <command name> <qualifiers>"
Type "help help" for details.

3.  The SEND command may be useful for on-line help from PCN (Pete Nielsen)
or WDD (Bill Drain), when they are signed on.  You can find out if PCN
or WDD is on by sending them a trial message.

EXAMPLE:
-------

User:  send 'hello' user(wdd)

TSO:   USER WDD NOT LOGGED ON

TSO:   READY

user:  send 'hello' user(pcn)

TSO:   READY

user:  send 'edit is acting funny' user(pcn)

TSO:   READY

Here "PCN" was logged on and got your message.  You can, therefore,
converse with him through SEND.  The text in one SEND is limited to
115 characters.

4.  You can also leave a message for wdd to receive when he logs on by
typing:  send '<message>' user(wdd) logon.

5.  To send a message to the CCN operator, enter simply:  send '<message>'

6.  You can call the CCN Telephone Consultant at (213) 825-7452, Monday
through Friday during the hours 10-12 A.M. PDT and 1-4 P.M. (except
3-4 P.M. on Thursday).  If the consultant does not know the answer,
he/she will investigate and call you back.

7.  You can call the general contact for Network user problems, Barbara
Noble, at (213) 825-7438.  Barbara is also one of the Telephone
consultants.

8.  If all else fails, call Bill Drain, the CCN Systems Programmer in
charge of TSO installation.  His telephone is (213) 825-7474 (if no
answer, call my secretary at (213) 825-7518 and leave a message for
Bill).

9.  You can also send a message to someone at CCN by submitting the
following pseudo-job through RJS at TSO:

//<charge number>  JOB 'BIN=9906',MSGLASS=C
//*  <message>
//*
//*
//*
//*
etc.

[ This RFC was put into machine readable form for entry ]

```
       [ into the online RFC archives by BBN Corp. under the   ]
       [ direction of Alex McKenzie.                      1/97 ]

```