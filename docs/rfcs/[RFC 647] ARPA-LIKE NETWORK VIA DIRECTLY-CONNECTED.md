---
rfc: 647
title: "ARPA-LIKE NETWORK VIA DIRECTLY-CONNECTED"
date: November 1974
---

# 1. BEGIN INDEX HOST SOCKET TRANSLATION-TYPE CONNECTION-TYPE

The begin command establishes a "connection" between the Host and the
FE.  Regardless of internal representation, the duplex data stream
the connection represents will be referred to by the value specified
in the next (INDEX) field that is, for example, the FE will send
input from and receive output for a given Telnet connection "on" a
given INDEX, even though it is actually managing two "sockets" for
the purpose in its dealings with the Network.

a) INDEX is a two-byte field.  Both the Host and the FE may choose
arbitrary values for it when opening connection with a BEGIN command
(H-FP implementations will probably simply increment INDEX by 1
whenever they need a new connection); however, the value of 0 is
reserved to apply to the "global" connection between the Host and the
FE -- thus, when either machine "come up" the first thing it does is
send a BEGIN for INDEX=0.  (The END and ACKNOWLEDGE commands also
follow this convention; for that matter, there is no reason why the
MESSAGE command could not also, should it be desired to extend the
FE's functions in the future.  At present, however, this is merely a
potential extension.)  Note that all other fields should be set to 0
for INDEX 0 BEGINS.

b) HOST is a two-byte field.  It specifies the Host number associated
with the socket in the next field.  On FE to Host BEGINS this is
purely informational.  However, on Host to FE BEGINS it is necessary
to enable the FE to identify the foreign Host with which to
communicate at the NCP level.

c) SOCKET is a four-byte field.  If SOCKET=1, a Telnet connection is
to be established.  If SOCKET=3, an FTP connection is to be
established.  If SOCKET=5, an ARPANET RJE Protocol connection is to
be established (no known current utility).  If SOCKET=77, a Host-
specific connection is to be established for RJE/batch.  All other
values are for connections for unspecified purposes, to be opened at
the NCP level according to the CONNECTION-TYPE field.  Note that
sockets 1, 3, 5 and 77 are "known about" and special-cased by the FE.

d) TRANSLATION-TYPE is a one-byte field.  From FE Host, it is
informational.  From Host to FE, it specifies character set mapping
if desired, or characterizes the data to be transmitted over the
connection.  0 request / specifies ASCII data 1; binary data (note
that this value will not be sent from FE to Host under current
assumptions, and that word size is to be a per-installation
parameter); 2, mapping of ASCII to/from local character set.  Other
types will be defined if needs are identified.

e) CONNECTION-TYPE is a one-byte field.  For FE to Host BEGINS it is
informational.  For Host to FE BEGINS it instructs the FE as to which
kind of NCP connection discipline to follow.  1 requests a duplex
connection (i.e., that the Initial Connection Protocol of the ARPANET
be employed) 2, a simplex connection (i.e., that the appropriate
ARPANET "request for connection" Host-Host Protocol commmand be
employed for the gender of the socket at hand).  Note that this
extended use of the H-FP will be of interest when (and if) User-level
programs on the Host begin to use the Network.  (The FE will open 8-
bit connections at the Network level unless otherwise directed.)

# 2. ACKNOLEDGE INDEX CODE

The ACKNOWLDEGE command is multi-purpose.  It must be sent in
response to all commands from the other machine (other than
ACKNOWLEDGES, of course), and is primarily used to indicate the
success or failure of the command just received on INDEX.  Note that
this implies that each MESSAGE on a given INDEX must be ACKNOWLEDGEd
before the next can be sent.

a) INDEX is as above.

b) CODE is a two-byte field.  CODE=0 indicates success / acceptance
of the command most recently received for INDEX.  CODE=1 indicates
failure /rejection of the most recent command.  (E.g., if a MESSAGE,
buffering was unavailable so the other machine must retransmit; if a
BEGIN, the indicated protocol / socket cannot be serviced.)  CODE=3
indicates an invalid or inactive INDEX has been used.  CODE=4
indicates (HOST to FE) that no mapping is to be performed on the
connection just opened.  Other values (for such meanings as "foreign
Host down", "undefined type requested" and the like) will be assigned
as identified.

# 3. MESSAGE INDEX COUNT PAD TEXT

The MESSAGE command is employed for the transmission of data.

a) INDEX is as above.

b) COUNT is a two-byte field which specifies the number of bits of
data in the TEXT field.

c) PAD is a 1-to-n-byte field.  Its width is a per-installation
parameter used to enable the TEXT field to start on a word boundary
if the local H-FP implementers so desire.  (This is not only a
kindness, but it's also a placeholder if we decide to go to a flow
control mechanism involving sequence numbers.)

d) TEXT is a field wherein byte structure is coincidental.  It
consists of COUNT bits of data to be sent to the process implicitly
associated with INDEX by a BEGIN command (which has not been ENDed.)

# 4. INTERRUPT INDEX

The INTERRUPT command, when sent from the FE to the Host, indicates
that an FCP interrupt command (INS or INR) has been received for the
process associated with INDEX; the Host should interrupt the
associated process and whatever fashion is "normal" to it.  (The most
common use of the NCP is in Telnet, where it is defined as being the
functional equivalent of having struck a terminal's ATTN, INT, of
BREAK key, or input a "control-c" on certain character-at-a-time
systems; essentially, it requests a "quit button" push.  Note that
the FE will take care of the associated Telnet control code in the
input stream.)  When sent from the Host to the FE (in process to
process applications), it will indicate that an appropriate NCP
interrupt be sent, according to the gender of the socket associated
with INDEX.

# 5. END INDEX CODE

The END command is used to terminate a connection.  It may be sent
either because one system or the other is about to go down, or
because the FE have received an NCP "CLS" command or because the
destination system or IMP has gone down, or at the behest of a Host
user process.

a) INDEX is as above.  Note that if INDEX=0 the END refer to the
"global" connection between the Host and the FE in such case, the
high-order bit of CODE will be set to 1 and the low-order bits will
specify the number of the minutes to shutdown if this information is
available.  (Furnished because the associated IMP often informs the
FE of such a condition.)

b) CODE is a two-byte field.  CODE=1 indicates the general "close"
case (either received or ordered) 2, foreign systems has gone down;
3, foreign IMP has gone down; 4, local IMP has gone down.  Other
values will be assigned as identified.

EXTENSIBILITY

Simplicity and compactness being major goals of the protocol, the
small repertoire of commands just presented represent "all there is".
Recall that we are specifically omitting from consideration such
issues as error and flow control, which could turn the H-FP into
another Host-Host Protocol.  (should error and flow control prove

desirable in practice, we have, of course, thought of some suitable
mechanism within the H-FP framework; but they are not considered
germane in the present context.) The primary intention here is to
specify a protocol, which lends itself to minimal initial
implementations in the Hosts, on the same time scale as would have
otherwise been required for known-device simulations -- but which
offers great flexibility in the use of the network than would be
achieved through known-device simulation.

The astute reader will have noticed that most of the commands have
been specified with an eye toward the future.  Because the same
protocol, which allows the Host and the FE to communicate can easily
allow user processes on the Host to use the Network, we have tried to
encourage this desirable end by furnishing all the necessary hoods
and handholds for it in the FE's H-FP module through the broad
definitions of the commands.  A Hosts's H-FP module can furnish a
trivial interface for user programs in terms of a very few entry
points (open, read, write, and close appear to be the minimal set)
and allow the user program considerable flexibility in its use of the
net.  For example, a "User" FTP program could be straightforwardly
created even for a Host, which did not choose to field the BEGINs on
socket 3 (necessary for "Server" FTP capability), and files could
still be "pulled" to the Host even if they could not be "pushed" to
it.  (the FE will be required to recognize and special-case BEGINs on
socket 3, but that's a small price to pay).  So, if the specification
of the h-FP command repertoire seems somewhat more complex than it
need be, remember that not all of it has to coped with on any given
Host -- and that any give host ca take advantage of more functions as
it desires.  (Although it's not really within the present scope, we
stand willing to invent per-Host H-FP to user program interfaces on
request.)

FTP

To amplify a bit on the problem of file transfer, it must be observed
that in general only a file system can manage its files.  This
borders on tautology and is difficult to deny.  Therefore, although
the FE can shield the Host from a great deal of the mechanism
included in the FTP for functions not directly germane to the
transferring of files, Host's operating system and place or extract a
given file, even though it "has" the file's name available to it.
There is no in-principle reason why the H-FP module on the Host can't
invoke an appropriate routine when it receives a BEGIN on socket 3,
though.  (The FE will handle all the type and mode negotiations, pass
the "stor" or "retr" line along, and be ready to transmit or receive
on the appropriate socket but "somebody" in the Host has to receive
or transmit the MESSAGE to or from the right place.)  But if that
seems hard to do on any particular Host, its H-FP module can merely

negatively ACKNOWLEDGE any BEGINs for socket 3.  The real point to be
noted is that the H-FP still allows in principle for User  FTP, as
explained above, even so -- and that the simulation of known device
offers neither (User nor Server FTP) function.

(Files could, of course, be transferred into the FE, then somehow
gotten into the Host "later" -- perhaps by faxing up a batch job --
but that route requires either an awful lot of buffering in the mini
or a very sophisticated file system there, or both.  It also requires
an awful lot of per-Host information in each FE -- or perhaps human
intervention.  We're not saying it can't be done... eventually.  But
it's not going to be clean, or quick, or easy, or cheap.)

SUMMATION

Several important themes have unavoidably been dealt with piecemeal
in the foreign attempt to specify the H-FP in the abstract.  To
gather the threads together, it might be useful to consider the
various ways in which the protocol can be employed, in the context of
their ARPANET counterparts.  A. "SERVER" FUNCTIONS: There are, in
essence, three levels on which a Host can use the H-FP to fulfill
ARPANET "Server" functions.  1) For Hosts which choose to take FULL
advantage of the flexibility of the H-FP, all "fourth level" (user
process to user process)  protocols can be managed by the Host.  The
FE will perform NCP (Host-Host protocol) and IMP-Host protocol
functions (the associated IMP will, of course, perform IMP-IMP
protocol functions), thus shielding the Host from the necessity of
implementing a full-blown NCP with the attendant complexity of being
aware of the 11 to 14 "states" of a socket, flow control,
retransmission, and the like (as well as shielding it from the IMP-
Host protocol, with the attendant complexity of mapping "links"
to/from "sockets", dealing with message types forming and parsing
"leaders", and the like).  This mode of use is effected by giving the
"no mapping" code when the Host acknowledge a BEGIN on socket 1 and 3
(and by simply accepting BEGINs on all other sockets).  2) For Hosts
which choose to take PARTIAL advantage of the flexibility of the H-
FP, many aspects of the fourth level protocols (in particular Telnet
and FTP) can be managed by the FE on the Host's behalf, by virtue of
making assumptions about which Telnet and/or FTP "commands" are to be
permitted and only referring search matter as the association of data
which processes and/or file names to the Host.  (Note that the CODE
field of the ACKNOWLEDGE command furnishes the mechanism for
conveying such error information as "file not found" from the Host to
the FE, which in turn will send out appropriate FTP error messages.)
This mode of use is effected by simply accepting (with code 0) BEGINs
on sockets 1 and/or 3 (and doing as one chooses for all other
sockets); that is, fourth level shielding is anticipated to be
commonplace, and is the FE's default case.  3) For Hosts which choose

to take NO advantage of the flexibility of the H-FP, the "private"
RJE/batch connection type will still provide for the desirable
functions of load sharing and transferring files even though other
fourth level protocols were to be rejected by a given Host (by
refusing BEGINs on all sockets other than 77).  Even in this most
restricted case, the ability to upgrade to either of the broader base
is additively implicit in the H-FP, with no changes required to the
FE's own H-FP module -- whereas it would entail considerable
alteration of the Host's operating system had the first step been a
known-device simulation.  B. "USER" FUNCTIONS: 1) On the "User" side,
a Host could again elect to handle such fourth level protocols as
Telnet and FTP itself.  However, particularly in the Telnet case,
there is no real need for this, as a User Telnet "comes with" the FE
and it is unnecessary to burden the Host with such use unless so many
of its local terminals are hardwired that it would be expensive to
access the FE directly.  (Note that for a User FTP, the Host's H-FP
module would, as discussed above, in all likelihood require a user
program callable interface.) 2) On a less ambitious level, the FE
could be induced to perform the same shielding as it offers the
Server FTP (cf. case A2, above), given an "FTP mapping" TRANSLATION-
TYPE on the BEGIN command or the previously suggested special casting
by the FE on socket 3.  3) Finally, "User" functions could be
completely finessed, as per case A3.C. PROCESS TO PROCESS FUNCTIONS:
Irrespective of the positions taken in A and B, given only a user
program callable interface to the Host's H-FP module, all other
fourth level protocols which might evolve -- or, simply, general use
of sockets as interprocess communication ports -- can be achieved
directly.  Again, this would fundamentally be an "add-on" to the
system, not an alteration of existing software.

APPENDIX 2 - SOME NOTES ON IMPLEMENTERS

INTRODUCTORY DISCLAIMER

This appendix represents strictly the personal views of one of the
authors; I (now that I can admit to being Mike Padlipsky) have not
even permitted the other authors to agree with the views expressed
here, much less disagree with them, for they are insights which I've
gained the hard way during nearly four years of involvement with the
ARPANET and I feel they need saying -- regardless of the polite
fiction of refraining from finger pointing.  Please note at the
outset, however, that I am motivated not by a sense of vindictiveness
-- nor even of righteous indignation -- but rather by a desire to
present some history in the hope that the reader will not be
condemned to repeat it.  Note also that even though it makes the
prose more convoluted than it might otherwise have been, the
convention will be observed of "naming no names".  I am not, I

repeat, out to get these guys; merely to get away from them and their
like in the future.  (The reader can stop here with no loss to the
main argument of the paper.)

SEVERAL HORROR STORIES FROM THE WONDERFUL WORLD OF NETWORKING

Consider first the tale already told of the PDP 15/PDP 10 front
ending effort.  Having been involved in the writing of both the "old"
(1971) and the "new" (1973) Telnet Protocols, I feel a certain sense
of shame by the association that they were not so compellingly clear
that the power of the Network Virtual Terminal / common intermediate
representation approach could not have been missed, ever by system
programmers operating in pretty much of a vacuum with respect to
contact with knowledgeable ARPANET workers.  Having said that -- and
meant it -- I still feel we did a good enough job for average-plus
system types to cope with.  (The fact that numerous Hosts are on the
Net is evidence of this.) Unfortunately, however, average-minus
system types do exist and must also be contended with.  Therefore, if
we do not make a concerted effort to "idiot proof" our protocols, we
may anticipate further repetitions of the sad state the site under
discussion found itself in before it happened upon them.  (And, it
must regretfully be observed, support of the "real" ARPANET has
deteriorated to the point that the massive effort required to over-
explain ourselves probably could not be launched in the prevailing
climate.  More on this point later.)

Case in point number two is potentially far graver than a mere
"philosophical" muddle over bringing one site aboard.  It involves an
attempt by one of the Armed Services to network a large number of
large machines using the ARPANET as a model.  The implementation of
the software house with no known ARPANET expertise.  The
communications subnet and the hardware interfacing to the Hosts was
subcontracted to a well-known hardware manufacturer with no known
ARPANET expertise.  (As an aside, but because it's so startling I
can't forbear, the "system architect" for the target network is still
another well-known hardware manucfacturer (!), with, of course, no
known ARPANET expertise.) To make a long, continuing story short, it
is currently the case that the "real" ARPANET system whose hardware
corresponds most closely to the machines being netted here (even
though it is benchmarked at a rather lower "mips" (million
instructions per second) rate than the target net's machines) can
transfer files at rates in excess of 28,000 bits per second
(following the rather cumbersome full ARPANET FTP) from a small
configuration developement machine to a lightly loaded (but still
running in excess of 20 users) service machine one Network "hop"
away, while the new system achieves rates which I am apparently not
permitted to quantify but are very considerably lower even though
only one process is being run on each machine -- also one "hop" away

--  and the protocol for file transfer is nowhere near so general as
in the ARPANET.  Given a year or two, the situation can presumably be
rectified, but at present it is fair --  if somewhat fanciful -- to
say that if the Japanese were capable of only like level of
technology transfer they'd still be trying to make up their balance
of trade with those cute little parasols on matchsticks.

Yet what has gone amiss here in Horror Story 2? I submit that the
choice of subcontractors was based upon a misapprehension of the
level of technological sophistication associated with the ARPANET,
and that what was (is?) needed is a subcontract to a knowledgeable
ARPANET source (and I don't mean to the usual, profit-marking place
-- though I guess I trust them for the subnet), rather than to
"outsiders".  (I don't even mean to any particular place on the Net;
maybe what's needed is to form a meta-place out of the whole Net.
More on this, too, later.)  The real point is that the model was
essentially ignored by the putative model-followers, and --
demonstrably -- it shouldn't have been.

Case three should go a long way toward dispelling any impressions
that might be building in the reader's mind that I'm some sort of
hardcore ARPANET chauvinist.  For even "insiders" have blown some.
This is actually a dual case, for it involves two unsuccessful
attempts to furnish terminal support mini-Hosts for the Net.  In one
case, the choice of machine was faulty; even with additional core
memory field retrofitted, buffers cannot be furnished to support
reasonable data rates without imposing considerable unnecessary Host
overhead in the processing of too frequent Host-Host Allocation
commands.  Nor is there enough room to furnish more than a
rudimentary command language in the mini.  Now these were
knowledgeable, reasonably well managed "insiders" -- but they were
contractually not in a position to heed the technical intuitions of
several of themselves and the technical intuitions of many of their
colleagues throughout the Network Working Group that they'd been
painted into a corner.

In the second sub-case, the hardware and contractual obligations
appear to have been right, but ill-considered choice of
implementation language and inadequate management have prevented the
project's full completion to this time (some two years after its
inception).  Again, there was forewarnings from the NWG, in that we
had tried to alert them quite early about the language issue.  (On
the management level, we could only sympathize -- and in some cases
empathize -- but it is at least a tentacle position to take that the
ARPANET as a whole happened despite, not because of, management.)  (I
guess I am an ace system programmer chauvinist.)

The final case to be cited here involves another military effort.

This one I'm not even sure I'm supposed to know about, much less talk
about.  But I can say that it involves a subcontractor's attempt to
attach several special purpose machines to a major ARPANET server by
means of an internally invented set of machines and protocols.  My
information suggests that when asked why they failed to follow the
apparently obvious course of using ARPANET technology (facilities for
which do, of course, already exist on the target server), the
subcontractors essentially replied that they hadn't felt like it.
They also made their approach work yet, and it's been something like
a couple of years they've been trying.

Then three's the fad to simulate RJE terminals... but to use that as
Horror Story 5 would be begging the question -- for now.

SOME MORALS

Rather than search out any more dirty linen, let's pause and look for
the lessons to be learned.  In the first place, it borders on the
obvious that for any technical project the "right" technicians must
be found and empowered to perform it.  Despite the generation of
over-sell on the "power of computers", they still absolutely require
intelligent, competent programming -- which in turn requires
intelligent, competent programmers.  And, at the risk of gilding the
ragweed, not all self-professed programmers are intelligent and/or
competent.

In the second, and more interesting, place, all unknowing the ARPANET
has attracted or engendered an "in-group" of extremely good system
types -- who have learned through some sort of natural selection
process to work well together despite the immense handicap of the
heterogeneity of our various "nome" systems' assumptions.  We not
only have developed a common tongue, but some of us even like each
other.  (It should be noted that Appendix 1 was specified on a
Wednesday afternoon and a little bit of a Thursday morning.  Jon and
Jim and I had been there before.)  It seems quite clear to me that
the organizations for whom this report is intended should avail
themselves of the expertise which exists in the NWG; we've got a
reasonable track record, after all, especially in comparison to
others who have attempting networking.  Many of us also feel quite
strongly that we didn't get a chance to finish the job on the
ARPANET, and would like to be given the chance to "do it right" --
especially in view of the errors which have been committed in our
name.  (This is particularly important because the old gang is
beginning to scatter.  For myself, I expect this will be my last RFC.
Well, at least I've tried to make the most of it.)  The ARPANET is no
more a finished product than ANTS or ELF -- but all of them could and
should be.

In the final place now, a rather trite moral must be drawn: Technical
competence is extremely difficult to assess a priori.  (I'm
inordinately fond of saying "Don't ask me what I'm going to say, I
haven't said it yet" myself.)  But "track records" ARE important, and
competence CAN be demonstrated -- to a suitable jury of technical
peers.  Therefore, beware of plausible sounding subcontractors who
tell you "It's easy".  In our field, and particularly in getting all
those strange machines which were developed by people who by and
large didn't talk to each other to "talk" to each other, it's NOT
easy.  I'm willing to claim that it will be easier letting some NWG
types do it with the H-FP approach, but it might never be really easy
-- where "never" means for the next 10 years or so, until "real"
networking comes off the shelf with the operating system (which
itself scarcely comes off the shelf today) -- but don't get me
started on The Manufacturers.

BEYOND THE PAIN PRINCIPLE

So it's not easy.  It's also not impossible.  Indeed, the time
appears to be ripe right now avoiding generating a whole new
generation of horror stories, by sensitizing decision makers to
technical realities and "doing things right" this time around.
Having seized this occasion to say some things to that end which I
think are important, I must in good conscience stand ready to defend
the assertions I've made of error in some camps and of correctness in
what I might loosely call "our" camp.  I do so stand, with a right
good will.  If any reader desires more corroborative detail -- or
merely to see if I rant like this in contexts other than RFCs (or
even to have a go at my explanation of the common intermediate
representation principle), well, I'm still in the ARPANET Directory
-- even though the phone number's different (try 703-790-6375).  The
mailbox remains accurate (even though there is no "ARPANET mail
protocol" it's marvelous how stopgaps endure).

[This RFC was put into machine readable form for entry]

```
          [into the online RFC by Helene Morin, Viagenie,12/1999]

```