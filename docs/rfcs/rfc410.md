---
title: "Removal of the 30-Second Delay When Hosts Come Up"
date: November 1972
---
1.  Hosts should not have to wait the worst-case time
of 30 seconds to send to Hosts at their IMP or
nearby in the network.

2.  The operation of half-duplex interfaces is made
even more complicated because of the startup delay.

3.  The timeout period of 30 seconds is really a
function of network topology and we would like to
be able to change it when necessary as the network
expands.

We propose to eliminate the 30-second delay altogether.
The IMP subnetwork will detect messages for a dead Host at the
destination IMP instead of at the source IMP.  There is no delay

involved for an IMP to sense when its own Hosts come up, so
that it can always make the correct decision about whether to
give a message to one of its Hosts or to return a destination
dead message to the source Host.  Under this new scheme, when-
ever the IMP's ready line is up it is ready to accept input
from its Hosts without delay.  Several comments on this change
should be noted:

1.  No change to Host software should be necessitated
by this change.  The Host may attempt to send a
message to the IMP as soon as it brings its
ready line up, or it may delay for a long time.  In
either case, the IMP will take the message.  As
before, as soon as the Host has brought up its
ready line, it must accept messages from the IMP.

2.  The Hosts may wish to remove any delays _they_ have
programmed into their startup routines, since
such delays are no longer necessary.

3.  Destination dead messages will be returned as
before with two differences.  There will be more
delay between the receipt of the message at the
IMP and the return of the dead destination message
because it must travel through the network.  For
the same reason, if many messages are sent to
dead Hosts, the dead destination messages may come
back out of order.

The Host personnel responsible for the IMP software at
each site should check that this proposed change will not ad-
versely affect them.  If no adverse comments are received,
this change will go into effect on Tuesday morning, December
12 at the regular IMP software release time.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by BBN Corp. under the   ]
[ direction of Alex McKenzie.                      1/97 ]
