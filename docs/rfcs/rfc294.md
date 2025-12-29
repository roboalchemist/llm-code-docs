---
title: "The Use of 'Set Data Type' Transaction in File Transfer Protocol"
date: January 1972
---
1.        USER                                             SERVER
----                                             ------
Set data type '02' (Network ASCII)
------------------------------------->
Store File X
------------------------------------->
File X (in Network ASCII)
------------------------------------->
End of File
------------------------------------->
Acknowledge
<-------------------------------------

Retrieve File X
------------------------------------->
File X in Network ASCII
<-------------------------------------
End of File
<-------------------------------------

2.        USER                                             SERVER
----                                             ------
Set data type'03' (EBCDIC)
------------------------------------->
Retrieve File Y
------------------------------------->
Set data type '00' ("bit-stream")
<-------------------------------------
File Y as stored (no conversion)
<-------------------------------------
End of File
<-------------------------------------

Set data type '02' (Network ASCII)
------------------------------------->
Retrieve File Z
------------------------------------->
File Z in Network ASCII
<-------------------------------------
End of File
<-------------------------------------
