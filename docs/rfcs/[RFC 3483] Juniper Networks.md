---
rfc: 3483
title: "Juniper Networks"
date: March 2003
category: Informational
---

# Abstract

Common Open Policy Services (COPS) Protocol (RFC 2748), defines the
capability of reporting information to the Policy Decision Point
(PDP).  The types of report information are success, failure and
accounting of an installed state.  This document focuses on the COPS
Report Type of Accounting and the necessary framework for the
monitoring and reporting of usage feedback for an installed state.

Conventions used in this document

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119].

# Table of Contents

  - [Glossary](#glossary)
  - [1  Introduction](#1-introduction)
  - [2  Overview](#2-overview)
  - [3  Requirements for Normal Operations](#3-requirements-for-normal-operations)
  - [4  Periodic Nature of Policy Usage Feedback](#4-periodic-nature-of-policy-usage-feedback)
    - [4.1 Reporting Intervals](#41-reporting-intervals)
    - [Reporting](#reporting)
  - [6  Solicited Feedback](#6-solicited-feedback)
  - [7  Usage reports on shared objects](#7-usage-reports-on-shared-objects)
  - [8  Context](#8-context)
  - [9  Delete Request States](#9-delete-request-states)
  - [10 Failover](#10-failover)
  - [11 Security Considerations](#11-security-considerations)
  - [12 References](#12-references)
    - [12.1 Normative References](#121-normative-references)
    - [12.2 Informative References](#122-informative-references)
  - [13 Authors' Addresses](#13-authors-addresses)
  - [14 Full Copyright Statement](#14-full-copyright-statement)

QoS policy decisions.  Furthermore, the PDP may coordinate this usage
information with other external systems to determine the future
policy such as the case with the PDP coordinating multimedia session
QoS and clearinghouse authorizations [SIP-AAA-QOS].

The scope of this document is to describe the framework for policy
usage monitored and reported by the PEP and collected at the PDP.
The charging, rating and billing models, as well as other accounting
or statistics gathering events, detectable by the PDP are beyond the
scope of this framework.

# 2. Overview

There are three main aspects to define policies for usage feedback:

-  which objects are monitored
-  the metrics to be monitored and reported for these objects
-  when the reports are delivered

In the framework, a selection criteria policy specifies one or more
objects that should be monitored (e.g., a dropper or the instances of
an IP Filter for all its interfaces).

A usage feedback class is used to specify which metrics are to be
collected for a set of objects - instances of the specified class
carry the usage information when it is reported.  The valid
combinations of monitored object classes and usage feedback classes
are reported by the PEP as capabilities.

Finally, selection criteria policy and usage feedback class are bound
together in a linkage policy, which also contains the information of
when reports are generated.  Reports are usually sent periodically,
but more restrictions can be placed on the generation of reports,
like thresholds or a change in the data.

# 3. Requirements for Normal Operations

Per COPS [RFC2748], the PDP specifies the minimum feedback interval
in the Accounting Timer object that is included in the Client Accept
message during connection establishment.  This specifies the maximum
frequency with which the PEP issues unsolicited accounting type
report messages.  The purpose of this interval is to pace the number
of report messages sent to the PDP.  It is not the goal of the
interval defined by the ACCT Timer value to provide precision
synchronization or timing.

The selection and the associated usage criteria and intervals for
feedback reporting are defined by the PDP.  Feedback policies, which
define the necessary selection and linkages to usage feedback
criteria, are included by the PDP in a Decision message to the PEP.
The usage feedback is then periodically reported by the PEP, at
intervals defined in the linkage policies at a rate no more
frequently than specified in the Accounting Timer object.  Note that

there are exceptions where reports containing feedback are provided
prior to the Accounting Timer interval (see section 6).  The PDP may
also solicit usage feedback which is to be reported back immediately
by the PEP.  Usage information may be cleared upon reporting.  This
is specified in the usage policy criteria.

The PEP monitors and tracks the usage feedback information.  The PDP
is the collection point for the policy usage feedback information
reported by the PEP clients within the administrative domain.  The
PDP may also collect other accounting event information that is
outside the scope of this document.

# 4. Periodic Nature of Policy Usage Feedback

Generally the policy usage feedback is periodic in nature and the
reporting is unsolicited.  The unsolicited reports are supplied per
the interval defined by the PDP.  The periodic unsolicited reports
are dictated by timer intervals and use a deterministic amount of
network resources.

The PDP informs the PEP of the minimal feedback interval during
client connection establishment with the Accounting Timer object.
The PDP may specify feedback intervals in the specific usage feedback
policies as well.  The unsolicited monitoring and reporting by the
PEP may be suspended and resumed at the direction of the PDP.

## 4.1. Reporting Intervals

The generation of usage feedback by the PEP to the PDP is done under
different conditions that include feedback on demand, periodic
feedback or feedback when a defined threshold is reached.

The periodic feedback for a usage policy can be further defined in
terms of providing feedback if there is a change or providing
feedback periodically regardless of a change in value.

The periodic interval is defined in terms of the Accounting Object,
ACCT Timer value.  A single interval is equal to the number of
seconds specified by the ACCT Timer value.  The PDP may define a
specific number of intervals, which are to pass before the PEP
provides the usage feedback for a specific policy in a report.  When
the ACCT Timer value is equal to zero there is no unsolicited usage
feedback provided by the PEP.  However, the PEP still monitors and
tracks the usage per the PDP policy and reports it when the PDP
solicits the feedback.

Reporting may be based on reaching a defined threshold value in the
usage PRC.

The PDP may solicit usage feedback in the middle of an interval by
sending a COPS decision message.  The exact contents of the message
are out of the scope of this framework document and need to be
defined in a document that actually implements usage feedback using
this framework.

The PEP, upon receiving a solicit decision from the PDP, shall
provide the requested usage information and clear the usage
information if the usage policy requires that the attribute be
cleared after reporting.  The PEP should continue to maintain the
same interval schedule as defined by the PDP in the Accounting Timer
object and established at client connection acceptance.

# 5. Suspension, Resumption and Halting of Usage Monitoring and Reporting

The PDP may direct the PEP to suspend usage feedback report messages
and then at a later time instruct the PEP to resume the reporting of
feedback.  The PDP may also instruct the PEP to suspend the
monitoring and tracking of usage which also results in the
suppression of the feedback reports until the PDP later tells the PEP
to resume the monitoring (and reporting).  When the PDP suspends
monitoring or suspends reporting, it also specifies whether the PEP
is to provide an unsolicited feedback report of the current monitored
usage of the affected usage policy.  The PDP may suspend and resume
monitoring and reporting for specific usage policies or for all of
the usage feedback policies.

# 6. Solicited Feedback

There may be instances when it is useful for the PDP to control the
feedback per an on-demand basis rather than a periodic basis.  The
PDP may solicit the PEP for usage feedback with a Decision.  The PDP
may solicit usage feedback at any time during the accounting interval
defined by the ACCT Timer.  The PEP responds immediately and reports
the appropriate usage policies and should continue to follow the
usage feedback interval schedule established during connection
acceptance.

# 7. Usage reports on shared objects

While some objects in a context's namespace directly represent unique
objects of the PEP's configuration, other COPS objects can be shared
between multiple actual assignments in the PEP.

Whenever the PEP creates multiple actual configuration instances from
the same COPS objects, these assignments can potentially collect
their own statistics independently.  Since the individual assignments
do not have a direct representation as COPS objects, additional
information must be provided to uniquely identify the assignment that
generates the usage information.  As an example, if the PEP needs to
create multiple usage objects for an IP address, it may use the port
number to uniquely identify each object, i.e., the (IP address, port
number) combination is now the unique identifier of the object.

The feedback framework allows this information to be distributed
between a selection criteria PRC and the corresponding usage feedback
PRC, however both PRCs together always must contain sufficient
information for the finest granularity of usage collection supported
by the PEP.

If all the additional information is not part of the selection
criteria PRC, all matching assignments are selected to collect usage
information.  The necessary data to differentiate these assignments
is part of the usage feedback PRC.

Implementations based on the feedback framework should always provide
a selection criteria PRC that contains a complete set of information
to select a unique assignment, while underspecified selection
criteria PRCs (together with extended usage feedback PRCs) are
optional.

# 8. Context

COPS-PR [RFC3084] allows multiple, independent, disjoint instances of
policies to be configured on the PEP.  Each instance is known as a
context, and only one context can be active at any given moment.  The
PDP directs the PEP to switch between contexts using a single
decision message.

The monitoring and recording of usage policies is subject to context
switches in a manner similar to that of the enforcement policy.
Usage policy is monitored, recorded and reported while the associated
policy information context is active.  When the context is
deactivated, a report message containing the usage feedback policies
for that context is provided to the PDP.  The PEP does not perform
any monitoring, tracking or reporting of policy usage for a given
context while the context is inactive.

# 9. Delete Request States

The PEP MUST send any outstanding usage feedback data monitored
during the feedback interval to the PDP via an unsolicited report
message immediately prior to issuing a Delete Request State.  This is
also the case when the PDP initiates the Delete Request State.

# 10. Failover

In the event the connection is lost between the PEP and PDP, the PEP
continues to track usage feedback information as long as it continues
to enforce installed (cached) policy.  When the locally installed
policy at the PEP expires, the usage feedback policy data also
expires and is no longer monitored.

Upon successful reconnection, where the PEP is still caching policy,
the PDP indicates deterministically to the PEP that the PEP may
resume usage feedback reporting.  The PEP reports all cached usage
and resumes periodic reporting, making any needed adjustment to the
interval schedule as specified in the reconnection acceptance ACCT
Timer.

# 11. Security Considerations

This document provides a framework for policy usage feedback, using
COPS-PR as the transport mechanism.  As feedback information is
sensitive, it MUST be transported in a secured manner.  COPS
[RFC2748] and COPS-PR [RFC3084] provide for such secured transport,
with mandatory and suggested security mechanisms.

The usage feedback information themselves MUST be secured, with their
security requirement specified in their respective documents.

# 12. References

## 12.1. Normative References

[RFC2119]     Bradner, S., "Key words to use in the RFCs", BCP 14,
RFC 2119, March 1997.

[RFC2748]     Boyle, J., Cohen, R., Durham, D., Herzog, S., Rajan, R.
and A. Sastry, "The COPS (Common Open Policy Service)
Protocol", RFC 2748, January 2000.

[RFC2753]     Yavatkar, R., Pendarakis, D. and R. Guerin, "A
Framework for Policy-based Admission Control", RFC
2753, January 2000.

[RFC3084]     Chan, K., Durham, D., Gai, S., Herzog, S., McCloghrie,
K., Reichmeyer, F., Seligson, J., Smith, A. and R.
Yavatkar, "COPS Usage for Policy Provisioning (COPS-
PR)", RFC 3084, March 2001.

## 12.2. Informative References

[SIP-AAA-QOS] Gross, G., Sinnreich, H. Rawlins D. and T. Havinis,
"QoS and AAA Usage with SIP Based IP Communications",
Work in Progress.

# 13. Authors' Addresses

Diana Rawlins
WorldCom
901 International Parkway
Richardson, Texas 75081

Phone: 972-729-4071
EMail: Diana.Rawlins@wcom.com

Amol Kulkarni
JF3-206
2111 NE 25th Ave
Hillsboro, Oregon 97124

Phone: 503-712-1168
EMail: amol.kulkarni@intel.com

Kwok Ho Chan
Nortel Networks, Inc.
600 Technology Park Drive
Billerica, MA 01821 USA

Phone: 978-288-8175
EMail: khchan@nortelnetworks.com

Martin Bokaemper
Juniper Networks
700 Silver Seven Road
Kanata, ON, K2V 1C3, Canada

Phone: 613-591-2735
EMail: mbokaemper@juniper.net

# 14. Full Copyright Statement

Copyright (C) The Internet Society (2003).  All Rights Reserved.

This document and translations of it may be copied and furnished to
others, and derivative works that comment on or otherwise explain it
or assist in its implementation may be prepared, copied, published
and distributed, in whole or in part, without restriction of any
kind, provided that the above copyright notice and this paragraph are
included on all such copies and derivative works.  However, this
document itself may not be modified in any way, such as by removing
the copyright notice or references to the Internet Society or other
Internet organizations, except as needed for the purpose of
developing Internet standards in which case the procedures for
copyrights defined in the Internet Standards process must be
followed, or as required to translate it into languages other than
English.

The limited permissions granted above are perpetual and will not be
revoked by the Internet Society or its successors or assigns.

This document and the information contained herein is provided on an
"AS IS" basis and THE INTERNET SOCIETY AND THE INTERNET ENGINEERING
TASK FORCE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION
HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF
MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
