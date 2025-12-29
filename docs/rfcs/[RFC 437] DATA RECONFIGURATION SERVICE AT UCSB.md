---
rfc: 437
title: "Data Reconfiguration Service at UCSB"
date: June 1973
---
1. (Note that without this socket switching, processes would be
connected to themselves when 'SICP' or 'UICP' is specified.)

The user is notified when his requests for connections are initiated
and when the interpreter begins applying a form to a connection.
When execution of a form terminates, the user is supplied with a
diagnostic message provided by the interpreter as well as the actual
run time of the interpreter.

'SELECT' (<tty list>|<CA>) <CA>

Requests DRS to establish unidirectional links between the user's
terminal and the terminals specified in <tty list>.  If <tty list> is
omitted, DRS attempts to link the user's terminal to all other active

terminals.  While the user's terminal has another terminal selected,
all output to the user'S terminal will also be routed to the selected
terminal.

';' <text> <CA>

Allows the user to enter any comments he chooses. <text> may include
the characters '?', and '.'.  Note that <CA> must be CR-LF, rather
than period.

[This RFC was put into machine readable form for entry]

```
    [into the online RFC archives by Helene Morin, Via Genie, 12/1999]

```