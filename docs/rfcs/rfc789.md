---
title: "Vulnerabilities of Network Control Protocols: An Example"
date: January 1981
---

# 29. Although we did not yet understand how it was  possible  for

so  many updates from one IMP to be extant simultaneously, we did

understand enough to be able to get the network to recover.   All

that was necessary was to patch the IMPs to disregard any updates

from  IMP  50, which after all was down anyway.  When the network

is operating normally, broadcasting a patch to all  IMPs  can  be

done  in  a  matter of minutes.  With the network operating as it

was during the period of the outage, this can take as much  as  3

or  4 hours.  (Remember that the IMPs are generally unmanned, and

that the only way of controlling them from the  NCC  is  via  the

network  itself.   This  is perfectly satisfactory when an outage

affects only a small group of IMPs, but  is  an  obvious  problem

when  the  outage  has network-wide effects.)  This procedure was

fully successful in bringing the network back up.

When we looked closely at the dumps, we saw  that  not  only

were  all  the updates on the queue from IMP 50, but they all had

one of three sequence numbers (either 8, 40,  or  44),  and  were

ordered        in        the        queue       as       follows:

8, 40, 44, 8, 40, 44, 8, 40, 44, ...  Note that by the definition

of LATER, 44 is LATER than 40 (44 > 40 and 44 - 40 <= 32), 40  is

LATER  than  8  (40 > 8 and 40 - 8 <= 32), and 8 is LATER than 44

(8 < 44 and 44 - 8 > 32).  Given the presence  of  three  updates

from the same IMP with these three sequence numbers, this is what

would  be  expected.   Since each update is LATER than one of the

others, a cycle is formed which keeps the three updates  floating

- 9 -

Eric C. Rosen

around  the  network  indefinitely.   Thus the IMPs spend most of

their CPU time and buffer space in processing these updates.  The

problem was to figure out how these three updates could  possibly

have  existed at the same time.  After all, getting from update 8

to update 40  should  require  2  or  3  full  minutes,  plus  31

intervening  sequence  numbers.   So  how could 8 still be around

when  40  was  generated,  especially  since  no   updates   with

intervening sequence numbers were present?

Our  first thought was that maybe the real-time clock in IMP

# 50. was running one or two orders of magnitude faster than normal,

invalidating our assumptions about the maximum number of  updates

which  could  be  generated  in  a  given  time.   An alternative

hypothesis suggested itself however when we looked at the  binary

representations of the three sequence numbers:

8 - 001000

40 - 101000

44 - 101100

Note  that  44  has only one more bit than 40, which has only one

more bit than 8.  Furthermore, the three different  updates  were

completely  identical,  except  for their sequence numbers.  This

suggests that  there  was  really  only  one  update,  44,  whose

sequence number was twice corrupted by dropped bits.  (Of course,

it's  also  possible  that  the  "real"  update  was  8,  and was

corrupted by added bits.  However, bit-dropping has proven itself

- 10 -

Eric C. Rosen

to be a much  more  common  sort  of  hardware  malfunction  than

bit-adding,  although  spontaneously  dropped  bits may sometimes

come back on spontaneously.)

Surely, the reader will object,  there  must  be  protection

against  dropped  bits.   Yes there is protection, but apparently

not enough.  The update packets themselves are checksummed, so  a

dropped  bit  in  an update packet is readily detected.  Remember

though that if  an  update  needs  to  be  retransmitted,  it  is

recreated  from tabled information.  For maximal reliability, the

tables must  be  checksummed  also,  and  the  checksum  must  be

recomputed every time the table is accessed.  However, this would

require  either  a  large  number  of  CPU  cycles  (for frequent

checksumming of a large area of memory)  or  a  large  amount  of

memory  (to store the checksums for a lot of small areas).  Since

CPU cycles and memory are both potentially scarce resources, this

did not seem to us to  be  a  cost-effective  way  to  deal  with

problems  that  arise, say, once per year (this is the first such

problem encountered in a year and a half of running this  routing

algorithm).   Time  and  space  can  be  saved by recomputing the

checksum at  a  somewhat  slower  frequency,  but  this  is  less

reliable,  in  that it allows a certain number of dropped bits to

"fall between the cracks."  It seems likely then that one of  the

malfunctioning  IMPs  had to retransmit update 44 at least twice,

(recreating it each time from tabled information), retransmitting

it at least once with the corrupted sequence number  40,  and  at

- 11 -

Eric C. Rosen

least  once  with  the  corrupted  sequence number 8.  This would

cause those three sequence numbers to be extant  in  the  network

simultaneously,  even  though protocol is supposed to ensure that

this is impossible.

Actually, the detection of dropped bits is most  properly  a

hardware function.  The next generation of IMP hardware (the "C30

IMP")  will  be able to detect and correct all single-bit errors,

and will detect all other bit errors.  Uncorrectable  bit  errors

will  cause  the  IMP to go into its "loader/dumper."  (An IMP in

its loader/dumper is not usable for  transferring  data,  and  is

officially   in  the  "down"  state.   However,  an  IMP  in  its

loader/dumper is easily controllable from the  NCC,  and  can  be

restarted  or  reloaded  without  on-site intervention.)  Current

hardware does have parity checking (which  should  detect  single

dropped  bits),  but  this feature has had to be turned off since

(a) there are too many spurious parity "errors,"  i.e.,  most  of

the  time when the machines complain of parity errors there don't

really seem to be any, and (b) parity errors cause  the  machines

to  simply  halt, rather than go into their loader/dumpers, which

means that on-site intervention is required to restart them.

Pending the introduction of improved hardware, what  can  be

done  to prevent problems like this from recurring in the future?

It is easy to think of many  ways  of  avoiding  this  particular

problem,  especially  if  one does not consider the problems that

may arise from the "fixes."  For example, we  might  be  able  to

- 12 -

Eric C. Rosen

avoid  this  sort of problem by spending a lot more CPU cycles on

checksumming, but this may be too expensive because of  the  side

effects  it  would  introduce.   (Also,  it is not clear that any

memory checksumming strategy can be totally free of "cracks.")  A

very  simple  and  conservative  fix  to  prevent this particular

problem from recurring is to modify clause (a) of the  definition

of  LATER  so  that  the  "<="  is replaced by "<" (strictly less

than).  We will implement this fix, but it cannot  be  guaranteed

that no related problems will ever arise.

What  is  really  needed  is  not some particular fix to the

routing algorithm, but a more general fix.  In  some  sense,  the

problem  we  saw  was  not really a routing problem.  The routing

code was working correctly, and the routes  that  were  generated

were correct and consistent.  The real problem is that a freakish

hardware  malfunction caused a high priority process to run wild,

devouring resources needed by other processes, thereby making the

network unusable.  The fact that the wild process was the routing

process is incidental.  In  designing  the  routing  process,  we

carefully  considered the amount of resource utilization it would

require.  By strictly controlling and limiting the rate at  which

updates  can  be  generated, we tried to prevent any situation in

which the routing process would make  excessive  demands  on  the

system.   As  we  have  seen  though, even our carefully designed

mechanisms were unable to protect against every possible sort  of

hardware  failure.  We need a better means of detecting that some

- 13 -

Eric C. Rosen

high priority process in the IMP, despite all the  safeguards  we

have  built in, is still consuming too many resources.  Once this

is  detected,  the  IMP  can  be  automatically  placed  in   its

loader/dumper.  In the case under discussion, we would have liked

to  have  all  the  IMPs  go  into  their loader/dumpers when the

problem arose.  This would have enabled us to  re-initialize  and

restart  all  the  IMPs  much more quickly.  (Although restarting

individual  IMPs  did  little  good,  restarting  all  the   IMPs

simultaneously would have cleared up the problem instantly, since

all  routing  tables  in  all  IMPs  would  have been initialized

simultaneously.)  It took us no more than an hour to  figure  out

how  to  restore  the  network;  several  additional  hours  were

required because it took so long for us to gain  control  of  the

misbehaving  IMPs  and  get  them  back  to  normal.   A built-in

software alarm system (assuming,  of  course,  that  it  was  not

subject  to  false  alarms)  might have enabled us to restore the

network more quickly, significantly reducing the duration of  the

outage.   This  is  not  to  say  that a better alarm and control

system could ever be a replacement for careful study  and  design

which   attempts   to  properly  distribute  the  utilization  of

important resources, but only that it is a necessary adjunct,  to

handle  the cases that will inevitably fall between the cracks of

even the most careful design.

- 14 -

Eric C. Rosen

# REFERENCES

"The New Routing Algorithm for the ARPANET," IEEE TRANSACTIONS ON

COMMUNICATIONS, May 1980, J.M. McQuillan, I. Richer, E.C.  Rosen.

"The  Updating  Protocol  of  ARPANET's  New  Routing Algorithm,"

COMPUTER NETWORKS, February 1980, E.C. Rosen.

- 15 -
