---
rfc: 1023
title: "HEMS Monitoring and Control Language"
date: October 1987
---
10.0.0.51.

interfaces BEGIN                    -- get dictionary
interface{ ip-addr(10.0.0.51) }     -- value to match
interface{ in-pkts out-pkts }       -- data template to get
GET-MATCH
END                                 -- finished with dict

The exact meaning of a "match" is dependent upon the characteristics
of the entities being compared.  In almost all cases, it is a
comparison for exact equality.  However, it is quite reasonable to
define values that allow matches to do interesting things.  For
example, one might define three different flavors of "ip-addr":  one
that has only the IP net number, one with the IP net+subnet, and the
whole IP address.  Another possibility is to allow for wildcards in
IP addresses (e.g., if the "host" part of an IP address was all ones,
then that would match against any IP address with the same net
number).

So, for all data items defined, the behavior of the match operation
must be defined if it is not simple equality.

Implementations don't have to provide the ability to use all items in
an object to match against.  It is expected that some data structures
that provide for efficient lookup for one item may be very
inefficient for matching against others.  (For instance, routing
tables are designed for lookup with IP addresses.  It may be very
difficult to search the routing table, matching against costs.)

NOTE:  It would be desirable to provide a general-purpose filtering
capability, rather than just "equality" as provided by GET-MATCH.
However, because of the potential complexity of such a facility, lack
of a widely-accepted representation for filter expressions, and time
pressure, we are not defining this mechanism now.

However, if a generalized filtering mechanism is devised, the GET-
MATCH operator will disappear.

Data Attributes

Although ASN.1 data is self-describing as far as the structure goes,
it gives no information about what the data means (e.g., By looking
at the raw data, it is possible to tell that an item is of type
[context 5] and 4 octets long).  That does not tell how to interpret
the data (is this an integer, an IP address, or a 4-character
string?), or what the data means (IP address of what?).

Most of the time, this information will come from RFC-1024, which
defines all of the ASN.1 tags and their precise meaning.  When
extensions have been made, it may not be possible to get

documentation on the extensions.  (See the section about extensions,
page 15.)

The query language provides a set of operators parallel to the GET
and GET-MATCH operators that return a set of attributes describing
the data.  This information should be sufficient to let a human
understand the meaning of the data and to let a sophisticated
application treat the data appropriately.  The information is
sufficient to let an application format the information on a display
and decide whether or not to subtract one sample from another.

Some of the attributes are textual descriptions to help a human
understand the nature of the data and provide meaningful labels for
it.  Extensive descriptions of standard data are optional, since they
are defined in RFC-1024.  Complete descriptions of extensions must be
available, even if they are documented in a user's manual.  Network
firefighters may not have the manual handy when the network is
broken.

The format of the attributes is not as simple as the format of the
data itself.  It isn't possible to use the data's tag, since that
would just look exactly like the data itself.  The format is:

Attributes ::= [APPLICATION 2] IMPLICIT SEQUENCE {
tagASN1       [0] IMPLICIT INTEGER,
valueFormat   [1] IMPLICIT INTEGER,
longDesc      [2] IMPLICIT IA5String OPTIONAL,
shortDesc     [3] IMPLICIT IA5String OPTIONAL,
unitsDesc     [4] IMPLICIT IA5String OPTIONAL,
precision     [5] IMPLICIT INTEGER OPTIONAL,
properties    [6] IMPLICIT BITSTRING OPTIONAL,
}

For example, the attributes for
system{ name, clock-msec }
might be:
system{
Attributes{
tagASN1(name), valueFormat(IA5String),
longDesc("The name of the host"),
shortDesc("hostname")
},
Attributes{
tagASN1(clock-msec), valueFormat(Integer),
longDesc("milliseconds since boot"),
shortDesc("uptime"), unitsDesc("ms")
precision(4294967296),
properties(1)

}
Note that in this example <name> and <clock-msec> are integer values
for the ASN.1 tags for the two data items.  A complete definition of
the contents of the Attributes type is in RFC-1024.

Note that there will be exactly as many Attributes items in the
result as there are objects in the template.  Attributes objects for
items which do not exist in the entity will have a valueFormat of
NULL and none of the optional elements will appear.

GET-ATTRIBUTES
dict template    GET-ATTRIBUTES    dict
Emit ASN.1 Attributes objects that for the objects named
in <template>.  Any items in the template that are not
in <dictionary> (or its components), elicit an
Attributes object with no.

or          dict    GET-ATTRIBUTES    dict
If there is no template, emit Attribute objects for all
of the items in the dictionary.  This is equivalent to
providing a template that lists all of the items in the
dictionary.  This allows a complete list of a
dictionary's contents to be obtained.

GET-ATTRIBUTES-MATCH
dict value template GET-ATTRIBUTES-MATCH dict <array>
should be an array (dictionary containing only one
type of item).  The first tag in <value> and

```
               <template> must match this type.  For each entry in
               <array>, match the <value> against the contents of the
               entry.  If there is a match, emit the atributes based
               upon <template>, just as in a GET-ATTRIBUTES operation.

   GET-ATTRIBUTES-MATCH is necessary because there will be situations
```

where the contents of the elements of an array may differ, even
though the array elements themselves are of the same type.  The most
obvious example of this is the situation where several network
interfaces exist and are of different types, with different data
collected for each type.

NOTE:  The GET-ATTRIBUTES-MATCH operator will disappear if a
generalized filtering mechanism is devised.

ADDITIONAL NOTE:  A much cleaner method would be to store the
attributes as sub-components of the data item of interest.  For
example, requesting:
system{ clock-msec() }  GET
would normally just get the value of the data.  Asking for an

additional layer down the tree would now get its attributes:
system{ clock-msec{ shortDesc, unitsDesc }  GET
would get the named attributes.  (The attributes would be named with
application-specific tags.)  Unfortunately, ASN.1 doesn't provide an
obvious notation to describe this type of organization.  So, we're
stuck with the GET-ATTRIBUTES operator.  However, if this cleaner
organization becomes possible, this decision may be re-thought.

Examining Memory

Even with the ability to symbolically access all of this information
in an entity, there will still be times when it is necessary to get
to very low levels and examine memory, as in remote debugging
operations.  The building blocks outlined so far can easily be
extended to allow memory to be examined.

Memory is modeled as an array, with an ASN.1 representation of
OctetString.  Because of the variety of addressing architectures in
existence, the conversion between the OctetString and "memory" is
very machine-dependent.  The only simple case is for byte-addressed
machines with 8 bits per byte.

Each address space in an entity is represented by one dictionary.  In
a one-address-space situation, this dictionary will be at the top
level.  If each process has its own address space, then one "memory"
dictionary may exist for each process.

The GET-RANGE operator is provided for the primary purpose of
retrieving the contents of memory, but can be used on any array.  It
is only useful in these other contexts if the array index is
meaningful.

GET-RANGE   array start length    GET-RANGE    dict
Get <length> elements of <array> starting at <start>.

```
               <start> and <length> are both ASN.1 INTEGER type.

```

The returned data may not be <length> octets long, since it may take
more than one octet to represent one memory location.

Memory is special in that it will not automatically be returned as
part of a request for an entire dictionary (e.g., If memory is part
of the "system" dictionary, then requesting:
system{}
will emit the entire contents of the system dictionary, but not the
memory item).

NOTE:  The GET-RANGE operator may disappear if a generalized
filtering mechanism is devised.

Controlling Things

All of the operators defined so far only allow data in an entity to
be retrieved.  By replacing the "template" arguments used in the GET
operators with values, data in the entity can be changed.

There are many control operations that do not correspond to simply
changing the value of a piece of data, such as bringing an interface
"down" or "up".  In these cases, a special data item associated with
the component being controlled (e.g., each interface), would be
defined.  Control operations then consist of "setting" this item to
an appropriate command code.

SET         dict value    SET    dict
Set the value(s) of data in the entity to the value(s)
given in <value>.

SET-MATCH   array mvalue svalue    SET-MATCH    dict

```
               <array> should be a array (dictionary containing only one
               type of item).  The first tag in <mvalue> and <svalue>
               must match this type.  For each entry in <array>, match
               the <mvalue> against the contents of the entry.  If there
               is a match, set value(s) in the entity to the value(s) in
               <svalue>, just as in SET.

   CREATE      array value    SET    dict
```

Insert a new entry into <array>.  Depending upon the
context, there may be severe restrictions about what
constitutes a valid <value>.

DELETE      array value    SET    dict
Delete the entry(s) in <array> that have values that
match <value>.

If there are several leaf items in the matched value, as in
route-entry{ interface(1), cost(3) }
all of them must match an array entry for any values to be changed.

Here is an example of how this operator would be used to shut down
the interface with ip-address 10.0.0.51 changing its status to
"down".

interfaces BEGIN                    -- get dictionary
interface{ ip-addr(10.0.0.51) }     -- value to match
interface{ status(down) }           -- value to set
SET-MATCH
END                                 -- finished with dict

Delete the routing table entry for 36.0.0.0.

route-table BEGIN                   -- get dictionary
route-entry{ ip-addr(36.0.0.0) }    -- value to match
DELETE
END                                 -- finished with dict

Note that this BEGIN/END pair ends up sending an empty ASN.1 item.
We don't regard this as a problem, as it is likely that there will be
some get operations executed in the same context.  In addition, the
"open" ASN.1 item provides the correct context for reporting errors.
(See page 14.)

NOTE:  The SET-MATCH operator will disappear and the DELETE operator
will change if a generalized filtering mechanism is devised.

Atomic Operations

Atomic operations can be provided if desired by allowing the stack to
contain a fragment of a query.  A new operation would take a query
fragment and verify its executability and execute it, atomically.

This is mentioned as a possibility, but it may be difficult to
implement.  More study is needed.

ERRORS

If some particular information is requested but is not available for
any reason (e.g., it doesn't apply to this implementation, isn't
collected, etc.), it can ALWAYS be returned as "no-value" by giving
the ASN.1 length as 0.

When there is any other kind of error, such as having improper
arguments on the top of the stack or trying to execute BEGIN when the
tag doesn't refer to a dictionary, an ERROR object be emitted.  The
contents of this object identify the exact nature of the error and
are discussed in RFC-1024.

Since there may be several unterminated ASN.1 objects in progress at
the time the error occurs, each one must be terminated.  Each
unterminated object will be closed with a copy of the ERROR object.
Depending upon the type of length encoding used for this object, this
will involve filling the value for the length (definite length form)
or emitting two zero octets (indefinite length form).  After all
objects are terminated, a final copy of the ERROR object will be
emitted.  This structure guarantees that the error will be noticed at
every level of interpretation on the receiving end.

If there was an error before any ASN.1 objects were generated, then
the result would simply be:
error(details)

If a couple of ASN.1 objects were unterminated, the result might look
like:

interfaces{
interface { name(...) type(...) error(details) }
error(details)
}
error{details}

EXTENDING THE SET OF VALUES

There are two ways to extend the set of values understood by the
query language.  The first is to register the data and its meaning
and get an ASN.1 tag assigned for it.  This is the preferred method
because it makes that data specification available for everyone to
use.

The second method is to use the VendorSpecific application type to
"wrap" the vendor-specific data.  Wherever an implementation defines
data that is not in RFC-1024, the "VendorSpecific" tag should be used
to label a dictionary containing the vendor-specific data.  For
example, if a vendor had some data associated with interfaces that
was too strange to get standard numbers assigned for, they could,
instead represent the data like this:

interfaces {
interface {
in-pkts, out-pkts, ...
VendorSpecific { ephemeris, declination }
}
}

In this case, ephemeris and declination are two context-dependent
tags assigned by the vendor for its non-standard data.

If the vendor-specific method is chosen, the private data MUST have
descriptions available through the GET-ATTRIBUTES and GET-
ATTRIBUTESMATCH operators.  Even with this descriptive ability, the
preferred method is to get standard numbers assigned if possible.

IMPLEMENTATION

Although it is not normally in the spirit of RFCs to define an
implementation, the authors feel that some suggestions will be useful

to early implementors of the query language.  This list is not meant
to be complete, but merely to give some hints about how the authors
imagine that the query processor might be implemented efficiently.

- The stack is an abstraction -- it should be implemented
with pointers, not by copying dictionaries, etc.

- An object-oriented approach should make initial
implementation fairly easy.  Changes to the "shape" if the
data items (which will certainly occur, early on) will also
be easier to make.

- Only a few "messages" need to be understood by objects.

- Most interesting objects are dictionaries, each of which
can be implemented using pointers to the data and procedure
"hooks" to perform specific operations such as GET, MATCH,
SET, etc.

- The hardest part is actually extracting the data from an
existing TCP/IP implementions that weren't designed with
detailed monitoring in mind.  This should be less of a
problem if a system is designed with easy monitoring as a
goal.

OBTAINING A COPY OF THE ASN.1 SPECIFICATION

Copies of ISO Standard ASN.1 (Abstract Syntax Notation 1) are
available from the following source.  It comes in two parts; both are
needed:

IS 8824 -- Specification (meaning, notation)
IS 8825 -- Encoding Rules (representation)

They are available from:

Omnicom Inc.
115 Park St, S.E.          (new address as of March, 1987)
Vienna, VA  22180
(703) 281-1135
