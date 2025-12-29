---
title: "Regarding Proferred Official ICP"
date: May 1971
updates: [123, 145                                            3]
---

# 1. The user can inquire or is notified of the fact that one of his

connections has been closed.

# 2. The server can inquire or is notified that a connection for which

he has done an Init (or Listen) is now open.

Both of the above seem basic to any NCP - user interface.

This race condition problem would not exist had the dynamic reconnection
features of RFC #36 been included in the NCP protocol and had dynamic
reconnection been used in this ICP.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Walter Pienciak 1/98 ]
