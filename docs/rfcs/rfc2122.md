---
rfc: 2122
title: "Telecommunication+Multimedia"
date: March 1997
category: Standards
---
...starting VEMMI session...

7)  Procedure to use when a VEMMI URL is encountered in a HTML document
without VEMMI support:

The VEMMI URL support may be built-in in some Web browsers, or
offered by an associated software or plug-in interworking with the
user browser, for example using the WWW_RegisterProtocol API command
to register the new VEMMI protocol.

When a Web browser encounters a VEMMI URL without having VEMMI support,
two cases may occur:
- some browsers will detect an unrecognized scheme and signal an
unrecoverable error directly.

- others will manage it as a relative URL [4] and will build a
complete URL including the VEMMI URL and will request it from the
host having sent the current document. In this case the host will
usually return the error "not found".

Among the mechanisms that could be used in order to offer a friendly
interface to both users with and without VEMMI support:
- when the second case occurs and the relative URL including the
vemmi:// string is transmitted to the server, the HTTPD server may
be modified in order to recognize such URL and to propose the
downloading of a VEMMI client software.
- the HTML document including the vemmi URL allowing to start the
VEMMI session may propose both options, for example:
If your browser supports VEMMI, directly
<A HREF="vemmi://ares.mctel.fr/TEST">start the interactive
multimedia service</A>, otherwise
<A HREF="ftp://ftp.mctel.fr/vemmi.exe">download first a VEMMI
client software</A>.
- the application/vemmi MIME type is defined below (to allow for
example exchange of vemmi objects). A possible way is for the
server to look in the HTTP Accept header field and to deduce that if
application/vemmi is supported, then the VEMMI support exists (in
this case, application/vemmi is to be defined in the browser and
associated with the vemmi decoder).

8) Security Considerations:

The VEMMI URL scheme is subject to the same security implications as
the general URL scheme [5] [14], so the usual precautions outlined in
[5] [14] apply (for example, it is not allowed to store the username
and password in the URLs).

Furthermore, among VEMMI objects that could be used during the
interactive session, metacode objects (representing a sequence of
VEMMI commands) and operative objects (they are executable programs
to be run on the client platform) may be downloaded and/or started.

In order to protect the user against the activation of an harmful
operative object, it is strongly recommended that the users use the
configuration menu of their VEMMI software to disable the option of
running operative objects when receiving potentially unsafe VEMMI
objects, or at least enable the option to request first user approval
before starting the execution of an operative object.

The VEMMI remote interactive services may vary widely in their access
control policies; in practice, when a prompt for username or password
is received, the VEMMI terminal should request them from the user.
The VEMMI terminal implementation could support additional features,

for example proposing by default "anonymous" as username and the user
Internet e-mail address as password, or looking in an encrypted local
database for user identification on this service.

Such an identification mechanism using the username/password scheme
is unsecure and is provided for backwards compatibility only. The
VEMMI services requiring a safe identification procedure must rely on
other alternative mechanisms (e.g. S/KEY or other). In numerous
cases, the user identification procedure will be performed by the
VEMMI service.

9) application/vemmi MIME type

VEMMI is a multimedia interactive service and VEMMI objects are
usually exchanged through a continuous VEMMI multimedia session.
However, VEMMI objects could also be transmitted and exchanged using
other mechanisms, for example using HTTP, through e-mail, and so
on... The assignment of a MIME media type application/vemmi will
allow this transport and exchange of VEMMI objects, and this
paragraph describes this MIME type.

Furthermore, for Web browsers not supporting the addition of new URL
protocol scheme, the VEMMI MIME type may also be used to transmit,
instead of a VEMMI object, a text file containing the VEMMI URL to
activate to connect to a VEMMI server.

9A) DESCRIPTION:

MIME media type name: "application"

MIME subtype name: "vemmi"

Required parameters: none

Optional parameters:
- version:
an optional version number may be specified, in the format:

version=<integer>

The version number is a numeric integer whose is encoded as the

```
     <version> parameter defined in ETS 300 709 (e.g. version=100), and
     whose the first digit represents the major VEMMI version number.
```

It must be pointed out that the VEMMI objects includes the VEMMI
version and a timestamp.

9B) ENCODING CONSIDERATIONS:

The "base64" mechanism is preferred because VEMMI use a native 8-bit
binary file format. However, as VEMMI includes its own 7-bits
encoding mechanisms, VEMMI data could also be transmitted in 7-bit
mode.

9C) SECURITY CONSIDERATIONS:

Refer to paragraph 8.

9D) INTEROPERABILITY CONSIDERATIONS:

VEMMI is designed to be fully platform independent, and the VEMMI
objects and contents could interoperate between any platform. The
only exception are the VEMMI operative objects that could be binary
programs specific to a given hardware platform and operating system.

10) Liaison address:

For all technical questions regarding this request, please contact:

Daniel Mavrakis
Monaco Telematique MC-TEL
P.O. Box 225
MC 98004 Monte-Carlo Cedex
PRINCIPALITY OF MONACO
EMail: Mavrakis@mctel.fr
Tel: (+377) 9216 8860
Fax: (+377) 9330 4545

Comments may also be addressed to:

Mr. Herve Layec,
ETSI STC TE1
06921 SOPHIA ANTIPOLIS Cedex
FRANCE
EMail: herve.layec@dri.france-telecom.fr
Tel: (+33) 2 99 12 73 01
Fax: (+33) 2 99 38 49 61

Mr. Kurt Kartmann
Consulting
Telecommunication+Multimedia
Gabelsbergerstr. 2
D-64807 DIEBURG
GERMANY
EMail: k.kartmann@t-online.de
Tel: (+49) 6071 1528
c/o Deutsche Telekom AG
Tel. (+49)6151 834965, Fax (+49) 6151 834284

The authors thank the other members of the ETSI TE1 VEMMI Working
Group for their comments:

- Michael Blaschitz (michael.blaschitz@etsi.fr)
- Agnelo Fernandes (agnelo@telepac.pt)
- Daniel Allonsius (daniel.allonsius@is.belgacom.be)
- Stefaan Herrebout (Stefaan.Herrebout@mail.interpac.be)
- Francisca Oliva (oliva@tid.es)
- Herwart Wermescher (Herwart.Wermescher@infonova.telecom.at)

11) References:

[1] "Enhanced Man-Machine Interface for Videotex and
Multimedia/Hypermedia Information Retrieval Services (VEMMI
revision 1)", ETS 300 709 standard (European Telecommunications
Standards Institute), September 1996.
This document is available on the Web in HTML format: see
http://www.etsi.fr/ecs/projects/vemmi/vemmi.htm

[2] "Enhanced Man-Machine Interface for Videotex and Other
Information Retrieval Services (VEMMI)", ITU-T T.107 standard
(International Telecommunications Union), March 1995.

[3] "Videotex Enhanced Man-Machine Interface service (VEMMI)",
ETS 300 382 standard (European Telecommunications Standards
Institute), February 1995.

[4] Fielding, R., "Relative Uniform Resource Locators", RFC 1808, UC
Irvine, June 1995.

[5] Berners-Lee, T., Masinter, L., and M. McCahill, "Uniform Resource
Locators (URL)", RFC 1738, December 1994.

[6] Reynolds, J., and J. Postel, "Assigned Numbers", STD 2, RFC 1700,
October 1994.

[7] Mavrakis, D., "VEMMI and Internet", TD 44, ETSI TE1 plenary
meeting in Brussels, October 20, 1995.

[8] Berners-Lee, T., Fielding, R., and H. Frystyk: "Hypertext Transfer
Protocol - HTTP/1.0", RFC 1945, MIT/LCS, UC Irvine, May 1996.

[9] Fielding, R., Gettys, J., Mogul, J., Frystyk, H., and T.
Berners-Lee, Transfer Protocol - HTTP/1.1", RFC 2068, UC Irvine,
January 1997.

[10] Freed, N., Klensin, J., and J. Postel, "Multipurpose Internet
Mail Extensions (MIME) Part Four Registration Procedures", BCP
13, RFC 2048, November 1996.

[11] Masinter, L., Zigmond, D., and H. Alvestrand, "Guidelines and
Process for new URL Schemes", Work in Progress.

[12] Berners-Lee, T., and D. Connolly, "Hypertext Markup Language
Specification - 2.0", RFC 1866, MIT/LCS, November 1995.

[13] "Port Numbers",
ftp://venera.isi.edu/in-notes/iana/assignments/port-numbers

[14] T. Berners-Lee, R. Fielding, L. Masinter, "Uniform Resource
Locators (URL)", Work in Progress.
