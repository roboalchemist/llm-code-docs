---
title: "The first section of this paper describes the prevailing ARPANET"
---
8.

The presence of a transaction identifier in a command
implies the necessity of a response echoing the identifier;
and no two concurrently outstanding commands may bear the same
identifier.

-9-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
A Command/Response Protocol, the Basis for an Alternative Approach

Requirements 3 and 4--the ability to transmit an arbitrary number
of parameters of various types with each command or response--are
most economically and effectively met by defining a small set of
primitive "data types" (for example, booleans, integers, character
strings) from which concrete parameters can be modeled, and a
"transmission format" in which such parameters can be encoded.
Appendix A suggests a set of data types suitable for a large class
of applications; Appendix B defines some possible transmission
formats.                                                             3c5

The protocol description given above is, of course, purely
symbolic.  Appendix C explores one possible encoding of the Protocol
in detail.                                                           3c6

Summarizing the Arguments Advanced So Far                             3d

The author trusts that little of what has been presented thus far
will be considered controversial by the reader.  The following
principal arguments have been made:                                  3d1

(1) The more effective forms of resource sharing depend upon
remote resources being usefully accessible to other programs,
not just to human users.

(2) Application-dependent protocols providing such access using
the current approach leave to the applications programmer the
task of constructing the additional layer of software (above
the IPC facility provided by the system) required to make
remote resources accessible at the functional level, thus
discouraging their use.

(3) A single, resource-independent protocol providing flexible
and efficient access at the functional level to arbitrary
remote resources can be devised.

(4) This protocol would make possible the construction at each
installation of an application-independent, network run-time
environment making remote resources accessible at the
functional level and thus encouraging their use by the
applications programmer.

A protocol as simple as that suggested here has great potential
for stimulating the sharing of resources within a computer network.
First, it would reduce the cost of adapting existing resources for
network use by eliminating the need for the design, documentation,
and implementation of specialized delivery protocols.  Second, it

-10-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
A Command/Response Protocol, the Basis for an Alternative Approach

would encourage the use of remote resources by eliminating the need
for application-specific interface software.  And finally, it would
encourage the construction of new resources built expressly for
remote access, because of the ease with which they could be offered
and used within the network software marketplace.                    3d2

-11-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
A High-Level Model of the Network Environment

A HIGH-LEVEL MODEL OF THE NETWORK ENVIRONMENT                          4

The Importance of the Model Imposed by the Protocol                   4a

The Protocol proposed above imposes upon the applications
programmer a particular model of the network environment.  In a
heterogeneous computer network, nearly every protocol intended for
general implementation has this effect, since it idealizes a class
of operations that have concrete but slightly different equivalents
in each system.  Thus the ARPANET's TELNET Protocol alluded to
earlier, for example, specifies a Network Virtual Terminal that
attempts to provide a best fit to the many real terminals in use
around the Network.                                                  4a1

As now formulated, the Protocol models a remote resource as an
interactive program with a simple, rigidly specified command
language.  This model follows naturally from the fact that the
function-oriented protocols from which the Protocol was extracted
were necessitated by the complexity and diversity of user-oriented
command languages.  The Protocol may thus legitimately be viewed as
a vehicle for providing, as an adjunct to the sophisticated command
languages already available to users, a family of simple command
languages that can readily be employed by programs.                  4a2

While the command/response model is a natural one, others are
possible.  A remote resource might also be modeled as a process that
services and replies to requests it receives from other computer
processes.  This request/reply model would emphasize the fact that
the Protocol is a vehicle for inter-process communication and that
no human user is directly involved.                                  4a3

Substituting the request/reply model for the command/response
model requires only cosmetic changes to the Protocol:                4a4

message-type=REQUEST [tid] op-code arguments
message-type=REPLY    tid  outcome results

In the formulation above, the terms "REQUEST", "REPLY", and
"op-code" have simply been substituted for "COMMAND", "RESPONSE",
and "command-name", respectively.                                    4a5

The choice of model need affect neither the content of the
Protocol nor the behavior of the processes whose dialog it governs.
Use of the word "command" in the command/response model, for
example, is not meant to imply that the remote process can be
coerced into action.  Whatever model is adopted, a process has

-12-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
A High-Level Model of the Network Environment

complete freedom to reject an incoming remote request that it is
incapable of or unwilling to fulfill.                                4a6

But even though it has no substantive effect upon the Protocol,
the selection of a model--command/response, request/reply, and so
on--is an important task because it determines the way in which both
applications and systems programmers perceive the network
environment.  If the network environment is made to appear foreign
to him, the applications programmer may be discouraged from using
it.  The choice of model also constrains the kind and range of
protocol extensions that are likely to occur to the systems
programmer; one model may suggest a rich set of useful extensions,
another lead nowhere (or worse still, in the wrong direction).       4a7

In this final section of the paper, the author suggests a network
model (hereafter termed the Model) that he believes will both
encourage the use of remote resources by the applications programmer
and suggest to the systems programmer a wide variety of useful
Protocol extensions.  Unlike the substance of the Protocol, however,
the Model has already proven quite controversial within the ARPANET
community.                                                           4a8

Modeling Resources As Collections of Procedures                       4b

Ideally, the goal of both the Protocol and its accompanying RTE
is to make remote resources as easy to use as local ones.  Since
local resources usually take the form of resident and/or library
subroutines, the possibility of modeling remote commands as
"procedures" immediately suggests itself.  The Model is further
confirmed by the similarity that exists between local procedures and
the remote commands to which the Protocol provides access.  Both
carry out arbitrarily complex, named operations on behalf of the
requesting program (the caller); are governed by arguments supplied
by the caller; and return to it results that reflect the outcome of
the operation.  The procedure call model thus acknowledges that, in
a network environment, programs must sometimes call subroutines in
machines other than their own.                                       4b1

Like the request/reply model already described, the procedure
call model requires only cosmetic changes to the Protocol:           4b2

message-type=CALL   [tid] procedure-name arguments
message-type=RETURN  tid  outcome        results

In this third formulation, the terms "CALL", "RETURN", and
"procedure-name" have been substituted for "COMMAND, "RESPONSE", and

-13-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
A High-Level Model of the Network Environment

"command-name", respectively.  And in this form, the Protocol might
aptly be designated a "procedure call protocol (PCP)".               4b3

"The procedure call model would elevate the task of creating
applications protocols to that of defining procedures and their
calling sequences.  It would also provide the foundation for a true
distributed programming system (DPS) that encourages and facilitates
the work of the applications programmer by gracefully extending the
local programming environment, via the RTE, to embrace modules on
other machines."  This integration of local and network programming
environments can even be carried as far as modifying compilers to
provide minor variants of their normal procedure-calling constructs
for addressing remote procedures (for which calls to the appropriate
RTE primitives would be dropped out).                                4b4

Finally, the Model is one that can be naturally extended in a
variety of ways (for example, coroutine linkages and signals) to
further enhance the distributed programming environment.             4b5

Clarifying the Procedure Call Model                                   4c

Although in many ways it accurately portrays the class of network
interactions with which this paper deals, the Model suggested above
may in other respects tend to mislead the applications programmer.
The Model must therefore be clarified:                               4c1

(1) Local procedure calls are cheap; remote procedure calls are
not.

Local procedure calls are often effected by means of a
single machine instruction and are therefore relatively
inexpensive.  Remote procedure calls, on the other hand, would
be effected by means of a primitive provided by the local RTE
and require an exchange of messages via IPC.

Because of this cost differential, the applications
programmer must exercise discretion in his use of remote
resources, even though the mechanics of their use will have
been greatly simplified by the RTE.  Like virtual memory, the
procedure call model offers great convenience, and therefore
power, in exchange for reasonable alertness to the
possibilities of abuse.

(2) Conventional programs usually have a single locus of control;
distributed programs need not.

-14-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
A High-Level Model of the Network Environment

Conventional programs are usually implemented as a single
process with exactly one locus of control.  A procedure call,
therefore, traditionally implies a transfer of control from
caller to callee.  Distributed systems, on the other hand, are
implemented as two or more processes, each of which is capable
of independent execution.  In this new environment, a remote
procedure call need not suspend the caller, which is capable
of continuing execution in parallel with the called procedure.

The RTE can therefore be expected to provide, for
convenience, two modes of remote procedure invocation:  a
blocking mode that suspends the caller until the procedure
returns; and a non-blocking mode that releases the caller as
soon as the CALL message has been sent or queued.  Most
conventional operating systems already provide such a mode
choice for I/O operations.  For non-blocking calls, the RTE
must also, of course, either arrange to asynchronously notify
the program when the call is complete, or provide an
additional primitive by which the applications program can
periodically test for that condition.

Finally, the applications programmer must recognize that by no
means all useful forms of network communication are effectively
modeled as procedure calls.  The lower level IPC facility that
remains directly accessible to him must therefore be employed in
those applications for which the procedure call model is
inappropriate and RTE-provided primitives simply will not do.        4c2

-15-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Some Expectations

SOME EXPECTATIONS                                                      5

Both the Procedure Call Protocol and its associated Run-Time
Environment have great potential for facilitating the work of the
network programmer; only a small percentage of that potential has
been discussed in the present paper.  Upon the foundation provided
by PCP can be erected higher level application-independent protocol
layers that further enhance the distributed programming environment
by providing even more powerful capabilities (see Appendix D).        5a

As the importance of the RTE becomes fully evident, additional
tasks will gradually be assigned to it, including perhaps those of:   5b

(1) Converting parameters between the format employed internally
by the applications program, and that imposed by the
Protocol.                                                     5b1

(2) Automatically selecting the most appropriate inter-process
transmission format on the basis of the two machines' word
sizes.                                                        5b2

(3) Automatically substituting for network IPC a more efficient
form of communication when both processes reside on the same
machine.                                                      5b3

The RTE will eventually offer the programmer a wide variety of
application-independent, network-programming conveniences, and so,
by means of the Protocol, become an increasingly powerful
distributed-system-building tool.                                     5c

-16-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing

# Acknowledgments

ACKNOWLEDGMENTS                                                        6

Many individuals within both SRI's Augmentation Research Center
(ARC) and the larger ARPANET community have contributed their time
and ideas to the development of the Protocol and Model described in
this paper.  The contributions of the following individuals are
expressly acknowledged:  Dick Watson, Jon Postel, Charles Irby, Ken
Victor, Dave Maynard, and Larry Garlick of ARC; and Bob Thomas and
Rick Schantz of Bolt, Beranek and Newman, Inc.                        6a

ARC has been working toward a high-level framework for
network-based distributed systems for a number of years now [14].
The particular Protocol and Model described here result from
research begun by ARC in July of 1974.  This research included
developing the Model; designing and documenting the Protocol
required to support it [15]; and designing, documenting, and
implementing a prototype run-time environment for a particular
machine [16, 17], specifically a PDP-10 running the Tenex operating
system developed by Bolt, Beranek and Newman, Inc [18].  Three
design iterations were carried out during a 12-month period, and the
resulting specification implemented for Tenex.  The Tenex RTE
provides a superset of the capabilities presented in the body of
this paper and Appendices A through C as well as those alluded to in

# Appendix D. 6b

The work reported here was supported by the Advanced Research
Projects Agency of the Department of Defense, and by the Rome Air
Development Center of the Air Force.                                  6c

-17-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Appendix A:  Suggested Data Types

APPENDIX A:  SUGGESTED DATA TYPES                                      7

The Protocol requires that every parameter or "data object" be
represented by one of several primitive data types defined by the
Model.  The set of data types below is sufficient to conveniently
model a large class of data objects, but since the need for
additional data types (for example, floating-point numbers) will
surely arise, the set must remain open-ended.  Throughout the
descriptions below, N is confined to the range [0, 2**15-1]:          7a

LIST:  A list is an ordered sequence of N data objects called
"elements".  A LIST may contain other LISTs as elements, and can
therefore be employed to construct arbitrarily complex composite
data objects.                                                     7a1

CHARSTR:  A character string is an ordered sequence of N ASCII
characters, and conveniently models a variety of textual
entities, from short user names to whole paragraphs of text.      7a2

BITSTR:  A bit string is an ordered sequence of N bits and,
therefore, provides a means for representing arbitrary binary
data (for example, the contents of a word of memory).             7a3

INTEGER:  An integer is a fixed-point number in the range

```
   [-2**31, 2**31-1], and conveniently models various kinds of
   numerical data, including time intervals, distances, and so on.   7a4

      INDEX:  An index is an integer in the range [1, 2**15-1].  As
   its name and value range suggest, an INDEX can be used to address
   a particular bit or character within a string, or element within
   a list.  INDEXes have other uses as well, including the modeling
   of handles or identifiers for open files, created processes, and
   the like.  Also, because of their restricted range, INDEXes are
   more compact in transmission than INTEGERs (see Appendix B).      7a5

      BOOLEAN:  A boolean represents a single bit of information,
   and has either the value true or false.                           7a6

      EMPTY:  An empty is a valueless place holder within a LIST or
   parameter list.                                                   7a7

                                  -18-

```

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Appendix B:  Suggested Transmission Formats

APPENDIX B:  SUGGESTED TRANSMISSION FORMATS                            8

Parameters must be encoded in a standard transmission format
before they can be sent from one process to another via the
Protocol.  An effective strategy is to define several formats and
select the most appropriate one at run-time, adding to the Protocol
a mechanism for format negotiation.  Format negotiation would be
another responsibility of the RTE and could thus be made completely
invisible to the applications program.                                8a

Suggested below are two transmission formats.  The first is a
36-bit binary format for use between 36-bit machines, the second an
8-bit binary, "universal" format for use between dissimilar
machines.  Data objects are fully typed in each format to enable the
RTE to automatically decode and internalize incoming parameters
should it be desired to provide this service to the applications
program.                                                              8b

PCPB36, For Use Between 36-Bit Machines                               8c

Bits  0-13 Unused (zero)                                          8c1
Bits 14-17 Data type                                              8c2
EMPTY  =1  INTEGER=4  LIST=7

```
      BOOLEAN=2  BITSTR =5
      INDEX  =3  CHARSTR=6
   Bits 18-20 Unused (zero)                                          8c3
   Bits 21-35 Value or length N                                      8c4
      EMPTY    unused (zero)
      BOOLEAN  14 zero-bits + 1-bit value (TRUE=1/FALSE=0)
      INDEX    unsigned value
      INTEGER  unused (zero)
      BITSTR   unsigned bit count N
      CHARSTR  unsigned character count N
      LIST     unsigned element count N
   Bits 36-   Value                                                  8c5
      EMPTY    unused (nonexistent)
      BOOLEAN  unused (nonexistent)
      INDEX    unused (nonexistent)
      INTEGER  two's complement full-word value
      BITSTR   bit string + zero padding to word boundary
      CHARSTR  ASCII string + zero padding to word boundary
      LIST     element data objects

                                  -19-

```

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Appendix B:  Suggested Transmission Formats

PCPB8, For Use Between Dissimilar Machines                            8d

Byte    0  Data type                                              8d1
EMPTY  =1  INTEGER=4  LIST=7

```
      BOOLEAN=2  BITSTR =5
      INDEX  =3  CHARSTR=6
   Bytes 1-   Value                                                  8d2
      EMPTY     unused (nonexistent)
      BOOLEAN   7 zero-bits + 1-bit value (TRUE=1/FALSE=0)
      INDEX     2-byte unsigned value
      INTEGER   4-byte two's complement value
      BITSTR    2-byte unsigned bit count N + bit string
                 + zero padding to byte boundary
      CHARSTR   2-byte unsigned character count N + ASCII string
      LIST      2-byte element count N + element data objects

                                  -20-

```

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Appendix C:  A Detailed Encoding of the Procedure Call Protocol

APPENDIX C:  A DETAILED ENCODING OF THE PROCEDURE CALL PROTOCOL        9

Although the data types and transmission formats detailed in the
previous appendixes serve primarily as vehicles for representing the
arguments and results of remote procedures, they can just as readily
and effectively be employed to represent the commands and responses
by which those parameters are transmitted.                            9a

Taking this approach, one might model each of the two Protocol
messages as a PCP data object, specifically a LIST whose first
element is an INDEX message type.  The following concise statement
of the Protocol then results:                                         9b

LIST (CALL,   tid,        procedure, arguments)

```
         INDEX=1 INDEX/EMPTY CHARSTR    LIST                         9b1
   LIST (RETURN, tid,        outcome,   results)
         INDEX=2 INDEX       BOOLEAN    LIST                         9b2

```

The RESULTS of an unsuccessful procedure would be represented as
follows:                                                              9c

LIST (error, diagnostic)
INDEX  CHARSTR                                              9c1

-21-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Appendix D:  A Look at Some Possible Extensions to the Model

APPENDIX D:  A LOOK AT SOME POSSIBLE EXTENSIONS TO THE MODEL          10

The result of the distributed-system-building strategy proposed
in the body of this paper and the preceeding appendices is depicted
in Figure D-1.  At the core of each process is the inter-process
communication facility provided by the operating system, which
effects the transmission of arbitrary binary data between distant
processes.  Surrounding this core are conventions regarding first
the format in which a few, primitive types of data objects are
encoded in binary for IPC, and then the formats of several composite
data objects (that is, messages) whose transmission either invokes
or acknowledges the previous invocation of a remote procedure.
Immediately above lies an open-ended protocol layer in which an
arbitrary number of enhancements to the distributed programming
environment can be implemented.  Encapsulating these various
protocol layers is the installation-provided run-time environment,
which delivers DPS services to the applications program according to
machine- and possibly programming-language-dependent conventions.    10a

The Protocol proposed in the present paper recognizes only the
most fundamental aspects of remote procedure calling.  It permits
the caller to identify the procedure to be called, supply the
necessary arguments, determine the outcome of the procedure, and
recover its results.  In a second paper [19], the author proposes
some extensions to this simple procedure call model, and attempts to
identify other common forms of inter-process interaction whose
standardization would enhance the distributed programming
environment.  Included among the topics discussed are:               10b

(1) Coroutine linkages and other forms of communication between
the caller and callee.                                       10b1

(2) Propagation of notices and requests up the thread of control
that results from nested procedure calls.                    10b2

(3) Standard mechanisms for remotely reading or writing
system-global data objects within another program.           10b3

(4) Access controls for collections of related procedures.       10b4

(5) A standard means for creating and initializing processes,
that is, for establishing contact with and logging into a
remote machine, identifying the program to be executed, and
so forth.  This facility would permit arbitrarily complex
process hierarchies to be created.                           10b5

-22-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Appendix D:  A Look at Some Possible Extensions to the Model

(6) A mechanism for introducing processes to one another, that
is, for superimposing more general communication paths upon
the process hierarchy.                                       10b6

These and other extensions can all find a place in the open-ended
protocol layer of Figure D-1.  The particular extensions explored in
[19] are offered not as dogma but rather as a means of suggesting
the possibilities and stimulating further research.                  10c

-23-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing

# References

REFERENCES                                                            11

# 1. Kahn, R. E., "Resource-Sharing Computer Communications

Networks," Proceedings of the IEEE, Vol. 60, No. 11, pp.
1397-1407, November 1972.                                        11a

# 2. Crocker, S. D., Heafner, J. F., Metcalfe, R. M., Postel, J. B.,

"Function-oriented Protocols for the ARPA Computer Network,"
AFIPS Proceedings, Spring Joint Computer Conference, Vol. 40,
pp. 271-279, 1972.                                               11b

# 3. Carr, C. S., Crocker, S. D., Cerf, V. G., "Host-Host

Communication Protocol in the ARPA Network," AFIPS Proceedings,
Spring Joint Computer Conference, Vol. 36, pp. 589-597, 1970.    11c

# 4. Mc Kenzie, A. A., Host/Host Protocol for the ARPA Network, Bolt

Beranek and Newman Inc., Cambridge, Massachusetts, January 1972
(SRI-ARC Catalog Item 8246).                                     11d

# 5. Walden, D. C., "A System for Interprocess Communication in a

Resource Sharing Computer Network," Communications of the ACM,
Vol. 15, No. 4, pp. 221-230, April 1972.                         11e

# 6. Cerf, V. G., Kahn, R. E., "A Protocol for Packet Network

Intercommunication," IEEE Transactions on Communications, Vol.
Com-22, No. 5, pp. 637-648, May 1974.                            11f

# 7. Thomas, R. H., "A Resource-Sharing Executive for the ARPANET,"

AFIPS Proceedings, National Computer Conference, Vol. 42, pp.
155-163, 1973.                                                   11g

# 8. TELNET Protocol Specification, Stanford Research Institute,

Menlo Park, California, August 1973 (SRI-ARC Catalog Item
18639).                                                          11h

# 9. Engelbart, D. C., Watson, R. W., Norton, J. C., "The Augmented

Knowledge Workshop," AFIPS Proceedings, National Computer
Conference, Vol. 42, pp. 9-21, 1973.                             11i

# 10. Engelbart, D. C., English, W. K., "A Research Center for

Augmenting Human Intellect," AFIPS Proceedings, Fall Joint
Computer Conference, Vol. 33, pp. 395-410, 1968.                 11j

# 11. Irby, C. H., Dornbush, C. F., Victor, K. E., Wallace, D. C., "A

Command Meta Language for NLS," Final Report, Contract

-24-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing

# References

RADC-TR-75-304, SRI Project 1868, Stanford Research Institute,
Menlo Park, California, December, 1975.                          11k

# 12. Neigus, N. J., File Transfer Protocol, ARPA Network Working

Group Request for Comments 542, Bolt Beranek and Newman Inc.,
Cambridge, Massachusetts, July 1973 (SRI-ARC Catalog Item
17759).                                                          11l

# 13. Bressler, R. D., Guida, R., Mc Kenzie, A. A., Remote Job Entry

Protocol, ARPA Network Working Group Request for Comments 360,
Dynamic Modeling Group, Massachusetts Institute of Technology,
Cambridge, Massachusetts, (undated) (SRI-ARC Catalog Item
12112).                                                          11m

# 14. Watson, R. W., Some Thoughts on System Design to Facilitate

Resource Sharing, ARPA Network Working Group Request for
Comments 592, Augmentation Research Center, Stanford Research
Institute, Menlo Park, California, November 20, 1973 (SRI-ARC
Catalog Item 20391).                                             11n

# 15. White, J. E., DPS-10 Version 2.5 Implementer's Guide,

Augmentation Research Center, Stanford Research Institute, Menlo
Park, California, August 15, 1975 (SRI-ARC Catalog Item 26282).  11o

# 16. White, J. E., DPS-10 Version 2.5 Programmer's Guide,

Augmentation Research Center, Stanford Research Institute, Menlo
Park, California, August 13, 1975 (SRI-ARC Catalog Item 26271).  11p

# 17. White, J. E., DPS-10 Version 2.5 Source Code, Augmentation

Research Center, Stanford Research Institute, Menlo Park,
California, August 13, 1975 (SRI-ARC Catalog Item 26267).        11q

18. Bobrow, D. G., Burchfiel, J. D., Murphy, D. L., Tomlinson, R.
S., "TENEX, a Paged Time Sharing System for the PDP-10,"
Communications of the ACM, Vol. 15, No. 3, pp. 135-143, March
1972.                                                            11r

# 19. White, J. E., "Elements of a Distributed Programming System,"

Submitted for publication in the Journal of Computer Languages,
1976.                                                            11s

-25-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263
NCC 76         A High-Level Framework for Network-Based Resource Sharing
Figure List

FIGURE LIST                                                           12

Figure   1.  Interfacing a remote terminal to a local time-sharing
system via the TELNET Protocol.                         12a

Figure   2.  Interfacing distant applications programs via their
run-time environments.                                  12b

Figure D-1.  Software and protocol layers comprising a process
within the distributed programming system.              12c

-26-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263

-27-

NWG/RFC# 707                                  JEW 14-JAN-76 19:51  34263

A High-Level Framework for Network-Based Resource Sharing

23-DEC-75

James E. White
Augmentation Research Center

Stanford Research Institute
Menlo Park, California  94025

(415) 326-6200 x2960

This paper proposes a high-level, application-independent
protocol and software framework that would extend the local
programming environment to embrace modules in other computers
within a resource sharing computer network, and thereby
facilitate the construction of distributed systems and encourage
the sharing of resources.

The work reported here was supported by the Advanced Research
Projects Agency of the Department of Defense, and by the Rome Air
Development Center of the Air Force.

This paper has been submitted for publication in the
Proceedings of the 1976 National Computer Conference.