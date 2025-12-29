---
rfc: 7079
title: "The Pseudowire (PW) and Virtual Circuit Connectivity Verification (VCCV)"
date: November 2013
category: Informational
---

# Abstract

The IETF Pseudowire Emulation Edge-to-Edge (PWE3) working group has
defined many encapsulations of various layer 1 and layer 2 service-
specific PDUs and circuit data.  In most of these encapsulations, use
of the Pseudowire (PW) Control Word is required.  However, there are
several encapsulations for which the Control Word is optional, and
this optionality has been seen in practice to possibly introduce
interoperability concerns between multiple implementations of those
encapsulations.  This survey of the Pseudowire / Virtual Circuit
Connectivity Verification (VCCV) user community was conducted to
determine implementation trends and the possibility of always
mandating the Control Word.

# Status of This Memo

This document is not an Internet Standards Track specification; it is
published for informational purposes.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Not all documents
approved by the IESG are a candidate for any level of Internet
Standard; see Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc7079.

# Copyright Notice

Copyright (c) 2013 IETF Trust and the persons identified as the
document authors.  All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(http://trustee.ietf.org/license-info) in effect on the date of
publication of this document.  Please review these documents
carefully, as they describe your rights and restrictions with respect
to this document.  Code Components extracted from this document must
include Simplified BSD License text as described in Section 4.e of
the Trust Legal Provisions and are provided without warranty as
described in the Simplified BSD License.

# Table of Contents

  - [1. Introduction](#1-introduction)
    - [1.1. PW/VCCV Survey Overview](#11-pwvccv-survey-overview)
    - [1.2. PW/VCCV Survey Form](#12-pwvccv-survey-form)
    - [1.3. PW/VCCV Survey Highlights](#13-pwvccv-survey-highlights)
  - [2. Survey Results](#2-survey-results)
    - [2.1. Summary of Results](#21-summary-of-results)
    - [2.2. Respondents](#22-respondents)
    - [2.3. Pseudowire Encapsulations Implemented](#23-pseudowire-encapsulations-implemented)
    - [2.4. Number of Pseudowires Deployed](#24-number-of-pseudowires-deployed)
    - [2.5. VCCV Control Channel in Use](#25-vccv-control-channel-in-use)
    - [2.6. VCCV Connectivity Verification Types in Use](#26-vccv-connectivity-verification-types-in-use)
      - [CW Is Optional](#cw-is-optional)
    - [2.8. Open-Ended Question](#28-open-ended-question)
  - [3. Security Considerations](#3-security-considerations)
  - [4. Acknowledgements](#4-acknowledgements)
  - [5. Informative References](#5-informative-references)
  - [Appendix A. Survey Responses](#appendix-a-survey-responses)
  - [A.1. Respondent 1](#a1-respondent-1)
  - [A.2. Respondent 2](#a2-respondent-2)
  - [A.3. Respondent 3](#a3-respondent-3)
  - [A.4. Respondent 4](#a4-respondent-4)
  - [A.5. Respondent 5](#a5-respondent-5)
  - [A.6. Respondent 6](#a6-respondent-6)
  - [A.7. Respondent 7](#a7-respondent-7)
  - [A.8. Respondent 8](#a8-respondent-8)
  - [A.9. Respondent 9](#a9-respondent-9)
  - [A.10. Respondent 10](#a10-respondent-10)
  - [A.11. Respondent 11](#a11-respondent-11)
  - [A.12. Respondent 12](#a12-respondent-12)
  - [A.13. Respondent 13](#a13-respondent-13)
  - [A.14. Respondent 14](#a14-respondent-14)
  - [A.15. Respondent 15](#a15-respondent-15)
  - [A.16. Respondent 16](#a16-respondent-16)
  - [A.17. Respondent 17](#a17-respondent-17)

# 1. Introduction

Most Pseudowire Emulation Edge-to-Edge (PWE3) encapsulations mandate
the use of the Control Word (CW) to carry information essential to
the emulation, to inhibit Equal-Cost Multipath (ECMP) behavior, and
to discriminate Operations, Administration, and Maintenance (OAM)
from Pseudowire (PW) packets.  However, some encapsulations treat the
Control Word as optional.  As a result, implementations of the CW,
for encapsulations for which it is optional, vary by equipment
manufacturer, equipment model, and service provider network.
Similarly, Virtual Circuit Connectivity Verification (VCCV) supports
three Control Channel (CC) types and multiple Connectivity
Verification (CV) types.  This flexibility has led to reports of
interoperability issues within deployed networks and associated
documents to attempt to remedy the situation.

The encapsulations and modes for which the Control Word is currently
optional are:

o  Ethernet Tagged Mode [RFC4448]

o  Ethernet Raw Mode [RFC4448]

o  Point-to-Point Protocol (PPP) [RFC4618]

o  High-Level Data Link Control (HDLC) [RFC4618]

o  Frame Relay Port Mode [RFC4618]

o  ATM (N:1 Cell Mode) [RFC4717]

Virtual Circuit Connectivity Verification (VCCV) [RFC5085] defines
three Control Channel types for MPLS PWs: Type 1, using the PW
Control Word; Type 2, using the Router Alert (RA) Label; and Type 3,
using Time to Live (TTL) Expiration (e.g., MPLS PW Label with TTL ==
1).  While Type 2 (RA Label) is indicated as being "the preferred
mode of VCCV operation when the Control Word is not present", RFC
5085 does not indicate a mandatory Control Channel to ensure
interoperable implementations.  The closest it comes to mandating a
control channel is the requirement to support Type 1 (Control Word)
whenever the CW is present.  As such, the three options yield seven
implementation permutations (assuming you have to support at least
one Control Channel type to provide VCCV).  Due to these
permutations, interoperability challenges have been identified by
several VCCV users.

In order to assess the best approach to address the observed
interoperability issues, the PWE3 working group decided to solicit
feedback from the PW and VCCV user community regarding
implementation.  This document presents the survey questionnaire and
the information returned by those in the user community who
participated.

## 1.1. PW/VCCV Survey Overview

Per the direction of the PWE3 working group chairs, a survey was
created to sample the nature of implementations of PWs, with specific
emphasis on Control Word usage, and VCCV, with emphasis on Control
Channel and Control Type usage.  The survey consisted of a series of
questions based on direction of the WG chairs and the survey opened
to the public on November 4, 2010.  The survey was conducted using
the SurveyMonkey tool, http://www.surveymonkey.com.  The survey ran
from November 4, 2010 until February 25, 2011 and was repeatedly
publicized on the PWE3 email list over that period.

The editors took precautions to ensure the validity of the sample and
the data.  Specifically, only responses with recognizable non-vendor
company-affiliated email addresses were accepted.  Unrecognizable or
personal email addresses would have been contacted to determine their
validity, but none were received.  Only one response was received
from each responding company.  If multiple responses from a company
had been received, they would have been contacted to determine
whether the responses were duplicative or additive.  This, however,
did not occur.

## 1.2. PW/VCCV Survey Form

The PW/VCCV Implementation Survey requested the following information
about user implementations (the lists of implementation choices were
taken verbatim from the survey):

-  Responding Organization.  No provisions were made for anonymous
responses, as all responses required a valid email address in
order to validate the survey response.  However, the results
herein are reported anonymously, except for an alphabetic list of
participating organizations in Section 2.2.

-  Of the various encapsulations (and options therein) known at the
time, including the WG document, "Encapsulation Methods for
Transport of Fibre Channel" (now [RFC6307]), which were
implemented by the respondent.  These included:

o  Ethernet Tagged Mode - RFC 4448

o  Ethernet Raw Mode - RFC 4448

o  Structure-Agnostic Time Division Multiplexing (TDM) over Packet
(SAToP) - RFC 4553

o  PPP - RFC 4618

o  HDLC - RFC 4618

o  Frame Relay (Port Mode) - RFC 4619

o  Frame Relay (1:1 Mode) - RFC 4619

o  ATM (N:1 Mode) - RFC 4717

o  ATM (1:1 Mode) - RFC 4717

o  ATM (AAL5 Service Data Unit (SDU) Mode) - RFC 4717

o  ATM (AAL5 PDU Mode) - RFC 4717

o  Circuit Emulation over Packet (CEP) - RFC 4842

o  Circuit Emulation Service over Packet Switched Network
(CESoPSN) - RFC 5086

o  Time Division Multiplexing over IP (TDMoIP) - RFC 5087

o  Fiber Channel (Port Mode) - "Encapsulation Methods for
Transport of Fibre Channel" (now RFC 6307)

-  Approximately how many PWs of each type were deployed.
Respondents could list a number, or for the sake of privacy, could
just respond "In-Use" instead.

-  For each encapsulation listed above, the respondent could indicate
which Control Channel [RFC5085] was in use.  (See Section 1 for a
discussion of these Control Channels.)  The options listed were:

o  Control Word (Type 1)

o  Router Alert Label (Type 2)

o  TTL Expiry (Type 3)

-  For each encapsulation listed above, the respondent could indicate
which Connectivity Verification types [RFC5085] were in use.  The
options were:

o  Internet Control Message Protocol (ICMP) Ping

o  Label Switched Path (LSP) Ping

-  For each encapsulation type for which the Control Word is
optional, the respondents could indicate the encapsulation(s) for
which Control Word was supported by the equipment vendor, and
whether the CW was also in use in the network.  The encapsulations
listed were:

o  Ethernet (Tagged Mode)

o  Ethernet (Raw Mode)

o  PPP

o  HDLC

o  Frame Relay (Port Mode)

o  ATM (N:1 Cell Mode)

-  Finally, a free-form entry was provided for the respondent to
provide feedback regarding PW and VCCV deployments, VCCV
interoperability challenges, or the survey or any other network/
vendor details they wished to share.

## 1.3. PW/VCCV Survey Highlights

There were seventeen responses to the survey that met the validity
requirements in Section 1.1.  The responding companies are listed
below in Section 2.2.

# 2. Survey Results

## 2.1. Summary of Results

Prior to this survey, there was considerable speculation about
whether the Control Word could always be mandated, with several
proposals to do so.  However, the survey showed that there was
considerable deployment of PWs that did not use the CW.  The
publication of this survey serves as a reminder of the extent of PWs
without the CW in use, and hence a reminder that the CW-less modes
cannot be deprecated in the near future.

## 2.2. Respondents

The following companies, listed here alphabetically as received in
the survey responses, participated in the PW/VCCV Implementation
Survey.  Responses were only solicited from non-vendors (users and
service providers), and no vendors responded (although if they had,
their response would not have been included).  The data provided has
been aggregated.  No specific company's response will be detailed
herein.

o  AboveNet

o  AMS-IX

o  Bright House Networks

o  Cox Communications

o  Deutsche Telekom AG

o  Easynet Global Services

o  France Telecom Orange

o  Internet Solution

o  MTN South Africa

o  OJSC MegaFon

o  Superonline

o  Telecom New Zealand

o  Telstra Corporation

o  Time Warner Cable

o  Tinet

o  Verizon

o  Wipro Technologies

## 2.3. Pseudowire Encapsulations Implemented

The following request was made: "In your network in general, across
all products, please indicate which pseudowire encapsulations your
company has implemented."  Of all responses, the following list shows
the percentage of responses for each encapsulation:

o  Ethernet Tagged Mode - RFC 4448 = 76.5%

o  Ethernet Raw Mode - RFC 4448 = 82.4%

o  SAToP - RFC 4553 = 11.8%

o  PPP - RFC 4618 = 11.8%

o  HDLC - RFC 4618 = 5.9%

o  Frame Relay (Port Mode) - RFC 4619 = 17.6%

o  Frame Relay (1:1 Mode) - RFC 4619 = 41.2%

o  ATM (N:1 Mode) - RFC 4717 = 5.9%

o  ATM (1:1 Mode) - RFC 4717 = 17.6%

o  ATM (AAL5 SDU Mode) - RFC 4717 = 5.9%

o  ATM (AAL5 PDU Mode) - RFC 4717 = 0.0%

o  CEP - RFC 4842 = 0.0%

o  CESoPSN - RFC 5086 = 11.8%

o  TDMoIP - RFC 5087 = 11.8%

o  Fiber Channel (Port Mode) - "Encapsulation Methods for Transport
of Fibre Channel" (now RFC 6307) = 5.9%

## 2.4. Number of Pseudowires Deployed

The following question was asked: "Approximately how many pseudowires
are deployed of each encapsulation type.  Note, this should be the
number of pseudowires in service, carrying traffic, or pre-positioned
to do so."  The following list shows the number of pseudowires in use
for each encapsulation:

o  Ethernet Tagged Mode = 93,861

o  Ethernet Raw Mode = 94,231

o  SAToP - RFC 4553 = 20,050

o  PPP - RFC 4618 = 500

o  HDLC - RFC 4618 = 0

o  Frame Relay (Port Mode) - RFC 4619 = 5,002

o  Frame Relay (1:1 Mode) - RFC 4619 = 50,959

o  ATM (N:1 Mode) - RFC 4717 = 50,000

o  ATM (1:1 Mode) - RFC 4717 = 70,103

o  ATM (AAL5 SDU Mode) - RFC 4717 = 0

o  ATM (AAL5 PDU Mode) - RFC 4717 = 0

o  CEP - RFC 4842 = 0

o  CESoPSN - RFC 5086 = 21,600

o  TDMoIP - RFC 5087 = 20,000

o  Fiber Channel (Port Mode) - "Encapsulation Methods for Transport
of Fibre Channel" (now RFC 6307) = 0

In the above responses (on several occasions), the response was in
the form of "> XXXXX" where the response indicated a number greater
than the one provided.  Where applicable, the number itself was used
in the sums above.  For example, ">20K" and "20K+" yielded 20K.

Additionally, the following encapsulations were listed as "In-Use"
with no quantity provided:

o  Ethernet Raw Mode: 2 Responses

o  ATM (AAL5 SDU Mode): 1 Response

o  TDMoIP: 1 Response

## 2.5. VCCV Control Channel in Use

The following instructions were given: "Please indicate which VCCV
Control Channel is used for each encapsulation type.  Understanding
that users may have different networks with varying implementations,
for your network in general, please select all which apply."  The
numbers below indicate the number of responses.  The responses were:

o  Ethernet Tagged Mode - RFC 4448

*  Control Word (Type 1) = 7

*  Router Alert Label (Type 2) = 3

*  TTL Expiry (Type 3) = 3

o  Ethernet Raw Mode - RFC 4448

*  Control Word (Type 1) = 8

*  Router Alert Label (Type 2) = 4

*  TTL Expiry (Type 3) = 4

o  SAToP - RFC 4553

*  Control Word (Type 1) = 1

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  PPP - RFC 4618

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  HDLC - RFC 4618

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  Frame Relay (Port Mode) - RFC 4619

*  Control Word (Type 1) = 1

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  Frame Relay (1:1 Mode) - RFC 4619

*  Control Word (Type 1) = 3

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 2

o  ATM (N:1 Mode) - RFC 4717

*  Control Word (Type 1) = 1

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  ATM (1:1 Mode) - RFC 4717

*  Control Word (Type 1) = 1

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 1

o  ATM (AAL5 SDU Mode) - RFC 4717

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 1

*  TTL Expiry (Type 3) = 0

o  ATM (AAL5 PDU Mode) - RFC 4717

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  CEP - RFC 4842

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  CESoPSN - RFC 5086

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 1

o  TDMoIP - RFC 5087

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

o  Fiber Channel (Port Mode) - "Encapsulation Methods for Transport
of Fibre Channel" (now RFC 6307)

*  Control Word (Type 1) = 0

*  Router Alert Label (Type 2) = 0

*  TTL Expiry (Type 3) = 0

## 2.6. VCCV Connectivity Verification Types in Use

The following instructions were given: "Please indicate which VCCV
Connectivity Verification types are used in your networks for each
encapsulation type."  Note that Bidirectional Forwarding Detection
(BFD) was not one of the choices.  The responses were as follows:

o  Ethernet Tagged Mode - RFC 4448

*  ICMP Ping = 5

*  LSP Ping = 11

o  Ethernet Raw Mode - RFC 4448

*  ICMP Ping = 6

*  LSP Ping = 11

o  SAToP - RFC 4553

*  ICMP Ping = 0

*  LSP Ping = 2

o  PPP - RFC 4618

*  ICMP Ping = 0

*  LSP Ping = 0

o  HDLC - RFC 4618

*  ICMP Ping = 0

*  LSP Ping = 0

o  Frame Relay (Port Mode) - RFC 4619

*  ICMP Ping = 0

*  LSP Ping = 1

o  Frame Relay (1:1 Mode) - RFC 4619

*  ICMP Ping = 2

*  LSP Ping = 5

o  ATM (N:1 Mode) - RFC 4717

*  ICMP Ping = 0

*  LSP Ping = 1

o  ATM (1:1 Mode) - RFC 4717

*  ICMP Ping = 0

*  LSP Ping = 3

o  ATM (AAL5 SDU Mode) - RFC 4717

*  ICMP Ping = 0

*  LSP Ping = 1

o  ATM (AAL5 PDU Mode) - RFC 4717

*  ICMP Ping = 0

*  LSP Ping = 0

o  CEP - RFC 4842

*  ICMP Ping = 0

*  LSP Ping = 0

o  CESoPSN - RFC 5086

*  ICMP Ping = 0

*  LSP Ping = 1

o  TDMoIP - RFC 5087

*  ICMP Ping = 0

*  LSP Ping = 1

o  Fiber Channel (Port Mode) - "Encapsulation Methods for Transport
of Fibre Channel" (now RFC 6307)

*  ICMP Ping = 0

*  LSP Ping = 0

## 2.7. Control Word Support for Encapsulations for Which CW Is Optional

The following instructions were given: "Please indicate your
network's support of and use of the Control Word for encapsulations
for which the Control Word is optional."  The responses were:

o  Ethernet (Tagged Mode)

*  Supported by Network/Equipment = 13

*  Used in Network = 6

o  Ethernet (Raw Mode)

*  Supported by Network/Equipment = 14

*  Used in Network = 7

o  PPP

*  Supported by Network/Equipment = 5

*  Used in Network = 0

o  HDLC

*  Supported by Network/Equipment = 4

*  Used in Network = 0

o  Frame Relay (Port Mode)

*  Supported by Network/Equipment = 3

*  Used in Network = 1

o  ATM (N:1 Cell Mode)

*  Supported by Network/Equipment = 5

*  Used in Network = 1

## 2.8. Open-Ended Question

Space was provided for user feedback.  The following instructions
were given: "Please use this space to provide any feedback regarding
PW and VCCV deployments, VCCV interoperability challenges, this
survey or any network/vendor details you wish to share."  Below are
the responses, made anonymous.  The responses are otherwise provided
here verbatim.

1.  BFD VCCV Control Channel is not indicated in the survey (may be
required for PW redundancy purpose)

2.  Using CV is not required at the moment

3.  COMPANY has deployed several MPLS network elements, from multiple
vendors.  COMPANY is seeking a uniform implementation of VCCV
Control Channel (CC) capabilities across its various vendor
platforms.  This will provide COMPANY with significant advantages
in reduced operational overheads when handling cross-domain
faults.  Having a uniform VCCV feature implementation in COMPANY
multi-vendor network leads to:

o  Reduced operational cost and complexity

o  Reduced OSS development to coordinate incompatible VCCV
implementations.

o  Increased end-end service availability when handing faults.

In addition, currently some of COMPANY deployed VCCV traffic
flows (on some vendor platforms) are not guaranteed to follow
those of the customer's application traffic (a key operational
requirement).  As a result, the response from the circuit ping
cannot faithfully reflect the status of the circuit.  This leads
to ambiguity regarding the operational status of our networks.
An in-band method is highly preferred, with COMPANY having a
clear preference for VCCV Circuit Ping using PWE Control Word.
This preference is being pursued with each of COMPANY vendors.

4.  PW VCCV is very useful tool for finding faults in each PW
channel.  Without this we can not find fault on a PW channel.  PW
VCCV using BFD is another better option.  Interoperability
challenges are with Ethernet OAM mechanism.

5.  We are using L2PVPN AToM like-to-like models - ATMoMPLS - EoMPLS
ATMoMPLS : This service offered for transporting ATM cells over
IP/MPLS core with Edge ATM CE devices including BPX, Ericsson
Media Gateway etc.  This is purely a Port mode with cell-packing
configuration on it to have best performance.  QoS marking is
done for getting LLQ treatment in the core for these MPLS
encapsulated ATM packets.  EoMPLS: This service offered for
transporting 2G/3G traffic from network such as Node-B to RNC's
over IP/MPLS backbone core network.  QoS marking is done for
getting guaranteed bandwidth treatment in the core for these MPLS
encapsulated ATM packets.  In addition to basic L2VPN service
configuration, these traffic are routed via MPLS TE tunnels with
dedicated path and bandwidth defined to avoid bandwidth related
congestion.

6.  EQUIPMENT MANUFACTURER does not provide options to configure VCCV
control-channel and its sub options for LDP based L2Circuits.
How can we achieve end-to-end management and fault detection of
PW without VCCV in such cases?

7.  I'm very interested in this work as we continue to experience
interop challenges particularly with newer vendors to the space
who are only implementing VCCV via control word.  Vendors who
have tailed their MPLS OAM set specifically to the cell backhaul
space and mandatory CW have been known to fall into this space.
That's all I've got.

# 3. Security Considerations

As this document is an informational report of the PW/VCCV User
Implementation Survey results, no protocol security considerations
are introduced.

# 4. Acknowledgements

We would like to thank the chairs of the PWE3 working group for their
guidance and review of the survey questions.  We would also like to
sincerely thank those listed in Section 2.2. who took the time and
effort to participate.

# 5. Informative References

[RFC4448]  Martini, L., Rosen, E., El-Aawar, N., and G. Heron,
"Encapsulation Methods for Transport of Ethernet over MPLS
Networks", RFC 4448, April 2006.

[RFC4618]  Martini, L., Rosen, E., Heron, G., and A. Malis,
"Encapsulation Methods for Transport of PPP/High-Level
Data Link Control (HDLC) over MPLS Networks", RFC 4618,
September 2006.

[RFC4717]  Martini, L., Jayakumar, J., Bocci, M., El-Aawar, N.,
Brayley, J., and G. Koleyni, "Encapsulation Methods for
Transport of Asynchronous Transfer Mode (ATM) over MPLS
Networks", RFC 4717, December 2006.

[RFC5085]  Nadeau, T., Ed. and C. Pignataro, Ed., "Pseudowire Virtual
Circuit Connectivity Verification (VCCV): A Control
Channel for Pseudowires", December 2007.

[RFC6307]  Black, D., Dunbar, L., Roth, M., and R. Solomon,
"Encapsulation Methods for Transport of Fibre Channel
Traffic over MPLS Networks", RFC 6307, April 2012.

# Appendix A. Survey Responses

The detailed responses are included in this appendix.  The respondent
contact info has been removed.

A.1.  Respondent 1

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 423

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: Control Word (Type 1)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: Ethernet (Tagged Mode), Ethernet (Raw Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.2.  Respondent 2

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

SAToP - RFC 4553

CESoPSN - RFC 5086

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 5000

Ethernet Raw Mode - RFC 4448 - 1000

SAToP - RFC 4553 - 50

CESoPSN - RFC 5086 - 1600

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: Control Word (Type 1), Router
Alert Label (Type 2), TTL Expiry (Type 3)

Ethernet Raw Mode - RFC 4448: Control Word (Type 1), Router Alert
Label (Type 2), TTL Expiry (Type 3)

CESoPSN - RFC 5086: TTL Expiry (Type 3)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: ICMP Ping, LSP Ping

Ethernet Raw Mode - RFC 4448: ICMP Ping, LSP Ping

SAToP - RFC 4553: LSP Ping

CESoPSN - RFC 5086: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

I'm very interested in this work as we continue to experience
interop challenges particularly with newer vendors to the space
who are only implementing VCCV via control word.  Vendors who
have tailed their MPLS OAM set specifically to the cell backhaul
space and mandatory CW have been known to fall into this space.
That's all I've got.

A.3.  Respondent 3

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

Frame Relay (Port Mode) - RFC 4619

Frame Relay (1:1 Mode) - RFC 4619

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 800

Ethernet Raw Mode - RFC 4448 - 50

Frame Relay (Port Mode) - RFC 4619 - 2

Frame Relay (1:1 Mode) - RFC 4619 - 2

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

No Response

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

No Response

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.4.  Respondent 4

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 1000

Ethernet Raw Mode - RFC 4448 - 200

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

No Response

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: LSP Ping

Ethernet Raw Mode - RFC 4448: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

EQUIPMENT MANUFACTURER does not provide options to configure VCCV
control-channel and its sub options for LDP based L2Circuits.
How can we achieve end-to-end management and fault detection of
PW without VCCV in such cases?

A.5.  Respondent 5

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

PPP - RFC 4618

Frame Relay (Port Mode) - RFC 4619

Frame Relay (1:1 Mode) - RFC 4619

Fiber Channel (Port Mode) - "Encapsulation Methods for Transport
of Fibre Channel" (now RFC 6307)

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 4000

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: Control Word (Type 1), Router
Alert Label (Type 2)

Ethernet Raw Mode - RFC 4448: Control Word (Type 1), Router Alert
Label (Type 2)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: Ethernet (Tagged Mode), Ethernet (Raw Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.6.  Respondent 6

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 1000+

Ethernet Raw Mode - RFC 4448 - 500

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: Control Word (Type 1)

Ethernet Raw Mode - RFC 4448: Control Word (Type 1)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: ICMP Ping, LSP Ping

Ethernet Raw Mode - RFC 4448: ICMP Ping, LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: Ethernet (Tagged Mode), Ethernet (Raw Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.7.  Respondent 7

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Raw Mode - RFC 4448

ATM (1:1 Mode) - RFC 4717

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Raw Mode - RFC 4448 - 20

ATM (1:1 Mode) - RFC 4717 - 100

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

No Response

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Raw Mode - RFC 4448: LSP Ping

ATM (1:1 Mode) - RFC 4717: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode), PPP, HDLC, Frame Relay (Port Mode), ATM (N:1 Cell
Mode)

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

We are using L2PVPN AToM like-to-like models - ATMoMPLS - EoMPLS
ATMoMPLS : This service offered for transporting ATM cells over
IP/MPLS core with Edge ATM CE devices including BPX, Ericsson
Media Gateway etc.  This is purely a Port mode with cell-packing
configuration on it to have best performance.  QoS marking is
done for getting LLQ treatment in the core for these MPLS
encapsulated ATM packets.  EoMPLS: This service offered for
transporting 2G/3G traffic from network such as Node-B to RNC's
over IP/MPLS backbone core network.  QoS marking is done for
getting guaranteed bandwidth treatment in the core for these MPLS
encapsulated ATM packets.  In addition to basic L2VPN service
configuration, these traffic are routed via MPLS TE tunnels with
dedicated path and bandwidth defined to avoid bandwidth related
congestion.

A.8.  Respondent 8

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Raw Mode - RFC 4448

ATM (AAL5 SDU Mode) - RFC 4717

TDMoIP - RFC 5087

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Raw Mode - RFC 4448 - In-Use

ATM (AAL5 SDU Mode) - RFC 4717 - In-Use

TDMoIP - RFC 5087 - In-Use

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Raw Mode - RFC 4448: Control Word (Type 1)

ATM (AAL5 SDU Mode) - RFC 4717: Router Alert Label (Type 2)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Raw Mode - RFC 4448: LSP Ping

ATM (AAL5 SDU Mode) - RFC 4717: LSP Ping

TDMoIP - RFC 5087: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Raw Mode), ATM (N:1
Cell Mode)

Used in Network: Ethernet (Raw Mode), ATM (N:1 Cell Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

PW VCCV is very useful tool for finding faults in each PW
channel.  Without this we can not find fault on a PW channel.  PW
VCCV using BFD is another better option.  Interoperability
challenges are with Ethernet OAM mechanism.

A.9.  Respondent 9

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Frame Relay (1:1 Mode) - RFC 4619

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 19385

Frame Relay (1:1 Mode) - RFC 4619 - 15757

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Frame Relay (1:1 Mode) - RFC 4619: Control Word (Type 1)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Frame Relay (1:1 Mode) - RFC 4619: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode), PPP, HDLC, Frame Relay (Port Mode), ATM (N:1 Cell
Mode)

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.10.  Respondent 10

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Raw Mode - RFC 4448

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Raw Mode - RFC 4448 - 325

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Raw Mode - RFC 4448: Control Word (Type 1)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Raw Mode - RFC 4448: ICMP Ping, LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: No Response

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.11.  Respondent 11

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

PPP - RFC 4618 HDLC - RFC 4618

Frame Relay (1:1 Mode) - RFC 4619

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 2000

Ethernet Raw Mode - RFC 4448 - 100

PPP - RFC 4618 - 500

Frame Relay (1:1 Mode) - RFC 4619 - 200

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

No Response

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: ICMP Ping, LSP Ping

Ethernet Raw Mode - RFC 4448: ICMP Ping, LSP Ping

Frame Relay (1:1 Mode) - RFC 4619: ICMP Ping, LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode), PPP, HDLC

Used in Network: Ethernet (Tagged Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.12.  Respondent 12

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Raw Mode - RFC 4448

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Raw Mode - RFC 4448 - 50000

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Raw Mode - RFC 4448: Control Word (Type 1), Router Alert
Label (Type 2), TTL Expiry (Type 3)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

No Response

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: Ethernet (Tagged Mode), Ethernet (Raw Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.13.  Respondent 13

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

Frame Relay (1:1 Mode) - RFC 4619

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 3

Ethernet Raw Mode - RFC 4448 - 10-20

ATM (1:1 Mode) - RFC 4717 - 3

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: Control Word (Type 1), TTL
Expiry (Type 3)

Ethernet Raw Mode - RFC 4448: Control Word (Type 1), TTL Expiry
(Type 3)

Frame Relay (1:1 Mode) - RFC 4619: Control Word (Type 1), TTL
Expiry (Type 3)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: ICMP Ping, LSP Ping

Ethernet Raw Mode - RFC 4448: ICMP Ping, LSP Ping

Frame Relay (1:1 Mode) - RFC 4619: ICMP Ping, LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode), PPP, HDLC, Frame Relay (Port Mode), ATM (N:1 Cell
Mode)

Used in Network: Ethernet (Tagged Mode), Ethernet (Raw Mode),
Frame Relay (Port Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.14.  Respondent 14

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 150

Ethernet Raw Mode - RFC 4448 - 100

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: Control Word (Type 1), Router
Alert Label (Type 2)

Ethernet Raw Mode - RFC 4448: Control Word (Type 1), Router Alert
Label (Type 2)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: LSP Ping

Ethernet Raw Mode - RFC 4448: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode), PPP, HDLC, Frame Relay (Port Mode)

Used in Network: Ethernet (Tagged Mode), Ethernet (Raw Mode)

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

No Response

A.15.  Respondent 15

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

Frame Relay (1:1 Mode) - RFC 4619

ATM (1:1 Mode) - RFC 4717

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 20,000

Ethernet Raw Mode - RFC 4448 - 1000

Frame Relay (1:1 Mode) - RFC 4619 - 30,000

ATM (1:1 Mode) - RFC 4717 - 20,000

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: TTL Expiry (Type 3)

Ethernet Raw Mode - RFC 4448: TTL Expiry (Type 3)

Frame Relay (1:1 Mode) - RFC 4619: TTL Expiry (Type 3)

ATM (1:1 Mode) - RFC 4717: TTL Expiry (Type 3)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: LSP Ping

Ethernet Raw Mode - RFC 4448: LSP Ping

Frame Relay (1:1 Mode) - RFC 4619: LSP Ping

ATM (1:1 Mode) - RFC 4717: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: No Response

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

COMPANY has deployed several MPLS network elements, from multiple
vendors.  COMPANY is seeking a uniform implementation of VCCV
Control Channel (CC) capabilities across its various vendor
platforms.  This will provide COMPANY with significant advantages
in reduced operational overheads when handling cross-domain
faults.  Having a uniform VCCV feature implementation in COMPANY
multi-vendor network leads to:

o   Reduced operational cost and complexity

o   Reduced OSS development to coordinate incompatible VCCV
implementations.

o   Increased end-end service availability when handing faults.

In addition, currently some of COMPANY deployed VCCV traffic
flows (on some vendor platforms) are not guaranteed to follow
those of the customer's application traffic (a key operational
requirement).  As a result, the response from the circuit ping
cannot faithfully reflect the status of the circuit.  This leads
to ambiguity regarding the operational status of our networks.
An in-band method is highly preferred, with COMPANY having a
clear preference for VCCV Circuit Ping using PWE Control Word.
This preference is being pursued with each of COMPANY vendors.

A.16.  Respondent 16

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

Ethernet Raw Mode - RFC 4448

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - 100

Ethernet Raw Mode - RFC 4448 - 100

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

No Response

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: ICMP Ping, LSP Ping

Ethernet Raw Mode - RFC 4448: ICMP Ping, LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: Ethernet (Tagged Mode), Ethernet
(Raw Mode)

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

Using CV is not required at the moment

A.17.  Respondent 17

2.  In your network in general, across all products, please indicate
which pseudowire encapsulations your company has implemented.

Ethernet Tagged Mode - RFC 4448

SAToP - RFC 4553

Frame Relay (Port Mode) - RFC 4619

Frame Relay (1:1 Mode) - RFC 4619

ATM (N:1 Mode) - RFC 4717

ATM (1:1 Mode) - RFC 4717

CESoPSN - RFC 5086

TDMoIP - RFC 5087

3.  Approximately how many pseudowires are deployed of each
encapsulation type.  Note, this should be the number of
pseudowires in service, carrying traffic, or pre-positioned to do
so. ***Note, please indicate "In-Use" for any PW Encap Types
which you are using but cannot provide a number.

Ethernet Tagged Mode - RFC 4448 - >40k

Ethernet Raw Mode - RFC 4448 - In-Use

SAToP - RFC 4553 - >20k

Frame Relay (Port Mode) - RFC 4619 - >5k

Frame Relay (1:1 Mode) - RFC 4619 - >5k

ATM (N:1 Mode) - RFC 4717 - >50k

ATM (1:1 Mode) - RFC 4717 - >50k

CESoPSN - RFC 5086 - >20k

TDMoIP - RFC 5087 - >20k

4.  Please indicate which VCCV Control Channel is used for each
encapsulation type.  Understanding that users may have different
networks with varying implementations, for your network in
general, please select all which apply.

Ethernet Tagged Mode - RFC 4448: Control Word (Type 1)

SAToP - RFC 4553: Control Word (Type 1)

Frame Relay (Port Mode) - RFC 4619: Control Word (Type 1)

Frame Relay (1:1 Mode) - RFC 4619: Control Word (Type 1)

ATM (N:1 Mode) - RFC 4717: Control Word (Type 1)

ATM (1:1 Mode) - RFC 4717: Control Word (Type 1)

5.  Please indicate which VCCV Connectivity Verification types are
used in your networks for each encapsulation type.

Ethernet Tagged Mode - RFC 4448: LSP Ping

SAToP - RFC 4553: LSP Ping

Frame Relay (Port Mode) - RFC 4619: LSP Ping

Frame Relay (1:1 Mode) - RFC 4619: LSP Ping

ATM (N:1 Mode) - RFC 4717: LSP Ping

ATM (1:1 Mode) - RFC 4717: LSP Ping

6.  Please indicate your network's support of and use of the Control
Word for encapsulations for which the Control Word is optional.

Supported by Network/Equipment: ATM (N:1 Cell Mode)

Used in Network: No Response

7.  Please use this space to provide any feedback regarding PW and
VCCV deployments, VCCV interoperability challenges, this survey
or any network/vendor details you wish to share.

BFD VCCV Control Channel is not indicated in the survey (may be
required for PW redundancy purpose)

# Authors' Addresses

Christopher N. "Nick" Del Regno (editor)
Verizon Communications, Inc.
400 International Pkwy
Richardson, TX  75081
US

EMail: nick.delregno@verizon.com

Andrew G. Malis (editor)
Consultant

EMail: agmalis@gmail.com
