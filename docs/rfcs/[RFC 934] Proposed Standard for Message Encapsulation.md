---
rfc: 934
title: "Proposed Standard for Message Encapsulation"
date: January 1985
---
1. The Header Portion

This memo makes no restriction on the header portion of the draft,
although it should conform to the RFC-822 standard.

2. The Text Portion

The text of the draft forwarding message consists of three parts: an
initial text section, the encapsulated messages, and the final text
section.

2.1. The Initial Text Section

All text (if any) up to the first EB comprises the initial text
section of the draft.  This memo makes no restrictions on the

Message Encapsulation

format of the initial text section of the draft.  In the case of a
digest, this initial text is usually the "table of contents" of
the digest.

2.2. The Final Text Section

All text (if any) after the last EB composes the final text
section of the draft.  This memo makes no restrictions on the
format of the final text section of the draft.  In the case of a
digest, this final text usually contains the sign-off banner for
the digest (e.g., "End of FOO Digest").

2.3. Encapsulated Messages

Each encapsulated message is bounded by two EBs: a pre-EB, which
occurs before the message; and, a post-EB, which occurs after the
message.  For two adjacent encapsulated messages, the post-EB of
the first message is also the pre-EB of the second message.
Consistent with this, two adjacent EBs with nothing between them
should be treated as enclosing a null message, and thus two or
more adjacent EBs are equivalent to one EB.

Each encapsulated message consists of two parts: a headers portion
and a text portion.  If the text portion is present, it is
separated from the header portion by a blank line.

2.3.1. The Header Portion

Minimally, there must be two header items in each message being
forwarded, a "Date:" field and a "From:" field. This differs
from RFC-822, which requires at least one destination address
(in a "To:" or "cc:" field) or a possibly empty "Bcc:" field.
Any addresses occuring in the header items for a message being
forwarded must be fully qualified.

2.3.2. The Text Portion

This memo makes no restrictions on the format of the text
portion of each encapsulated message.  (Actually, this memo
does restrict the format of the text portion of each
encapsulated message, but these restrictions are discussed
later.)

Before summarizing the generation/parsing rules for message
encapsulation, two issues are addressed.

Message Encapsulation

Compatibility with Existing User Agents

The above encapsulation protocol is presently used by many user
agents in the ARPA-Internet, and was specifically designed to
minimize the amount of changes to existing implementations of
forwarding agents in the ARPA-Internet.

However, the protocol is not exactly like the pseudo-standard used by
those forwarding agents that compose digests.  In particular, the
post-EB of all messages encapsulated in a digest is preceeded and
followed by by a blank line.  In addition, the first message
encapsulated in a digest has a pre-EB that is followed by a blank
line, but usually isn't preceeded by a blank line (wonderful).

This memo recommends that implementors of forwarding agents wishing
to remain compatible with existing bursting agents consider
surrounding each EB with a blank line.  It should be noted that blank
lines following a pre-EB for an encapsulated message must be ignored
by bursting agents.  Further, this memo suggests that blank lines
preceeding a post-EB also be ignored by bursting agents.

NOTE: This recommendation is made in the interest of
backwards-compatibility.  A forwarding agent wishing to strictly
adhere to this memo, should not generate blank lines surrounding
EBs.

Character-Stuffing the Encapsulation Boundary

It should be noted that the protocol is general enough to support
both general forwarding of messages and the specific case of digests.
Unfortunately, there is one issue of message encapsulation which
apparently is not addressed by any forwarding agent (to the authors'
knowledge) in the ARPA-Internet: what action does the forwarding
agent take when the encapsulation boundary occurs within a the text
portion of a message being forwarded?  Without exception, this
circumstance is ignored by existing forwarding agents.

To address this issue, this memo proposes the following
character-stuffing scheme: the encapsulation boundary is defined as a
line which starts with a dash.  A special case is made for those
boundaries which start with a dash and are followed by a space
(decimal code 32, " ").

During forwarding, if the forwarding agent detects a line in the
text portion of a message being forwarded which starts with the
encapsulation boundary, the forwarding agent outputs a dash
followed by a space prior to outputting the line.

Message Encapsulation

During bursting, if the bursting agent detects an encapsulation
boundary which starts with a dash followed by a space, then the
bursting agent does not treat the line as an encapsulation
boundary, and outputs the remainder of the line instead.

This simple character-stuffing scheme permits recursive forwardings.

Generation/Parsing Rules for Message Encapsulation

The rules for forwarding/bursting are described in terms of regular
expressions.  The first author originally derived simple finite-state
automata for the rules, but was unable to legibly represent them in
this memo.  It is suggested that the implementors sketch the automata
to understand the grammar.

The conventions used for the grammar are simple.  Each state is
followed by one or more alternatives, which are separated by the "|"
character.  Each alternative starts with a character that is received
as input. (CRLF, although two characters is treated as one character
herein.)  The last alternative for a state is the character "c",
which represents any character not specified in the preceeding
alternatives.  Optionally following the input character is an output
string enclosed by curly-braces.  Following this is the state that
the automata enters.  The reader should note that these grammars are
extremely simple to implement (and, in most cases, can be implemented
quite efficiently).

When the forwarding agent encapsulates a message, it should apply the
following finite-state automaton.  The initial state is S1.

S1 ::   CRLF {CRLF} S1
| "-" {"- -"} S2
| c {c} S2

S2 ::   CRLF {CRLF} S1
| c {c} S2

This simply says that anytime a "-" is found at the beginning of a
line, a "- " is output prior to outputting the line.

Message Encapsulation

When the bursting agent decapsulates the text portion of a draft, it
should apply the following finite-state automaton.  The initial state
is S1.

S1 ::   "-" S3
| CRLF {CRLF} S1
| c {c} S2

S2 ::   CRLF {CRLF} S1
| c {c} S2

S3 ::   " " S2
| c S4

S4 ::   CRLF S5
| c S4

S5 ::   CRLF S5
| c {c} S2

Although more complicated than the grammar used by the forwarding
agent to encapsulate a single message, this grammer is still quite
simple.  Let us make the simplifying assumption that both the initial
and final text sections of the draft are messages in addition to the
encapsulated messages.

To begin, the current message being burst is scanned at state S1. All
characters are output until the EB is found (state S3).  If "- " is
found, the automaton enters state S2 and characters from the current
message are continued to be output.  Finally, a true EB is found
(state S4).  As the automaton traverses from state S3 to S4, the
bursting agent should consider the current message ended.  The
remainder of the EB is discarded (states S4 and S5).  As the
automaton traverses from state S5 to S2, the bursting agent should
consider a new message started and output the first character.  In
state S2, all characters are output until the EB is found.

Blind Carbon Copies

Many user agents support a blind-carbon-copy facility.  With this
facility a draft has two types of addressees: visible and blind
recipients.  The visible recipients are listed as addresses in the
"To:" and "cc:" fields of the draft, and the blind recipients are
listed as addresses in the "Bcc:" fields of the draft.  The basis of
this facility is that copies of the draft which are delivered to the
recipients list the visible recipients only.

Message Encapsulation

One method of achieving this is to post a single draft, which lacks
any "Bcc:" fields, and, during posting, to interact with the MTS in
such a way that copies are sent to both the visible and blind
recipients.

Unfortunately, a key problem with this arrangement is that the blind
recipients can accidently reply to the draft in such a way that the
visible recipients are included as addressees in the reply. This is
socially unacceptable!  To avoid this problem, the message which the
visible recipients receive must be different than the message which
the blind recipients receive.

A second method is to post two drafts.  The first, which goes to the
visible recipients, is simply the draft without any "Bcc:" fields.
The second, which goes to the blind recipients, is simply the draft
with some string prepended to any "To:" and "cc:" field. For example,
the user agent might prepend "BCC-" to these fields, so that the
blind recipients get a draft with "BCC-To:" and "Bcc-cc:" fields and
no "To:" or "cc:" fields. Unfortunately, this is often very confusing
to the blind recipients.  Although accidental replies are not
possible, it is often difficult to tell that the draft received is
the result of a blind-carbon-copy.

The method which this memo suggests is to post two drafts, a visible
draft for the visible recipients, and a blind draft for the blind
recipients.  The visible draft consists of the original draft without
any "Bcc:" fields.  The blind draft contains the visible message as a
forwarded message.  The headers for the blind draft contain the
minimal RFC-822 headers and, if the original draft had a "Subject:"
field, then this header field is also included.  In addition, the
user agent might explicitly show that the blind draft is the result
of a blind-carbon-copy, with a "Bcc" header or prior to the first
encapsulating boundary in the body.

Message Distribution

The main purpose of message distribution (often called redistribution
or resending) is to provide to a secondary recipient, perhaps not
included among the original addressees, with a "true original" copy
that can be treated like an original in every respect.

Such distribution is most often done by discussion group moderators
who use automated agents to simply repost received messages to a
distribution list.  The better automatic distribution agents insert a
new "Return-Path" header field to direct address failure notices to
the discussion group address list maintainer, rather than to the
original author.  This form of distribution is encouraged because it

Message Encapsulation

most simply serves to deliver messages to discussion group recipients
as processable originals.  It is performed by trusted pseudo-MTS
agents.

A second kind of distribution is that done by individuals who wish to
transfer a processable copy of a received message to another
recipient. This second form is discouraged in various new standards
for message transfer.  These include the NBS Standard for Mail
Interchange [FIPS-98], and the recent CCITT draft MHS (Mail Handling
Systems) X.400 standards [X.400]. In place of direct reposting of
received messages as though they are new drafts, the recommendation
is to forward the received message in the body of a new draft from
which is can be extracted by its secondary recipient for further
processing.

It is in support of this recommendation that this standard for
encapsulation/decapsulation is proposed.

Message Encapsulation

# References

[RFC-822]    D.H. Crocker.  "Standard for the Format of ARPA-Internet
Text Messages", University of Delaware.  (August, 1982)

[RFC-821]    J.B. Postel.  "Simple Mail Transfer Protocol",
USC/Information Sciences Institute.  (August, 1982).

[FIPS-98]    National Bureau of Standards.  "Specification for
Message Format for Computer Based Message Systems."
(January, 1983).

```
   [X.400]      Consultative Committee on International Telephone and
```

Telegraph.  "DRAFT Recommendation X.400.  Message
Handling Systems: System Model-Service Elements."

# Authors' Addresses

Marshall T. Rose

Department of Computer and Information Sciences
University of Delaware
Newark, DE 19716

MRose@UDel.ARPA

Einar A. Stefferud

Network Management Associates, Inc.
17301 Drey Lane
Huntington Beach, CA 92647

Stef@UCI.ARPA
