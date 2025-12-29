---
rfc: 6534
title: "Colgate University"
date: May 2012
category: Standards
---

# Abstract

The IETF has developed a one-way packet loss metric that measures the
loss rate on a Poisson and Periodic probe streams between two hosts.
However, the impact of packet loss on applications is, in general,
sensitive not just to the average loss rate but also to the way in
which packet losses are distributed in loss episodes (i.e., maximal
sets of consecutively lost probe packets).  This document defines
one-way packet loss episode metrics, specifically, the frequency and
average duration of loss episodes and a probing methodology under
which the loss episode metrics are to be measured.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc6534.

# Copyright Notice

Copyright (c) 2012 IETF Trust and the persons identified as the
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

This document may contain material from IETF Documents or IETF
Contributions published or made publicly available before November
10, 2008.  The person(s) controlling the copyright in some of this
material may not have granted the IETF Trust the right to allow
modifications of such material outside the IETF Standards Process.
Without obtaining an adequate license from the person(s) controlling
the copyright in such materials, this document may not be modified
outside the IETF Standards Process, and derivative works of it may
not be created outside the IETF Standards Process, except to format
it for publication as an RFC or to translate it into languages other
than English.

# Table of Contents

  - [1. Introduction](#1-introduction)
    - [1.1. Background and Motivation](#11-background-and-motivation)
      - [1.1.1. Requirements Language](#111-requirements-language)
    - [1.2. Loss Episode Metrics and Bi-Packet Probes](#12-loss-episode-metrics-and-bi-packet-probes)
    - [1.3. Outline and Contents](#13-outline-and-contents)
  - [2. Singleton Definition for Type-P-One-way Bi-Packet Loss](#2-singleton-definition-for-type-p-one-way-bi-packet-loss)
    - [2.1. Metric Name](#21-metric-name)
    - [2.2. Metric Parameters](#22-metric-parameters)
    - [2.3. Metric Units](#23-metric-units)
    - [2.4. Metric Definition](#24-metric-definition)
    - [2.5. Discussion](#25-discussion)
    - [2.6. Methodologies](#26-methodologies)
    - [2.7. Errors and Uncertainties](#27-errors-and-uncertainties)
    - [2.8. Reporting the Metric](#28-reporting-the-metric)
    - [Type-P-One-way-Bi-Packet-Loss](#type-p-one-way-bi-packet-loss)
    - [3.1. Metric Name](#31-metric-name)
    - [3.2. Metric Parameters](#32-metric-parameters)
    - [3.3. Metric Units](#33-metric-units)
    - [3.4. Metric Definition](#34-metric-definition)
    - [3.5. Discussion](#35-discussion)
    - [3.6. Methodologies](#36-methodologies)
    - [3.7. Errors and Uncertainties](#37-errors-and-uncertainties)
    - [3.8. Reporting the Metric](#38-reporting-the-metric)
  - [4. An Active Probing Methodology for Bi-Packet Loss](#4-an-active-probing-methodology-for-bi-packet-loss)
    - [4.1. Metric Name](#41-metric-name)
    - [4.2. Metric Parameters](#42-metric-parameters)
    - [4.3. Metric Units](#43-metric-units)
    - [4.4. Metric Definition](#44-metric-definition)
    - [4.5. Discussion](#45-discussion)
    - [4.6. Methodologies](#46-methodologies)
    - [4.7. Errors and Uncertainties](#47-errors-and-uncertainties)
    - [4.8. Reporting the Metric](#48-reporting-the-metric)
  - [5. Loss Episode Proto-Metrics](#5-loss-episode-proto-metrics)
    - [5.1. Loss-Pair-Counts](#51-loss-pair-counts)
    - [5.2. Bi-Packet-Loss-Ratio](#52-bi-packet-loss-ratio)
    - [5.3. Bi-Packet-Loss-Episode-Duration-Number](#53-bi-packet-loss-episode-duration-number)
    - [5.4. Bi-Packet-Loss-Episode-Frequency-Number](#54-bi-packet-loss-episode-frequency-number)
  - [6. Loss Episode Metrics Derived from Bi-Packet Loss Probing](#6-loss-episode-metrics-derived-from-bi-packet-loss-probing)
    - [6.1. Geometric Stream: Loss Ratio](#61-geometric-stream-loss-ratio)
      - [6.1.1. Metric Name](#611-metric-name)
      - [6.1.2. Metric Parameters](#612-metric-parameters)
      - [6.1.3. Metric Units](#613-metric-units)
      - [6.1.4. Metric Definition](#614-metric-definition)
      - [6.1.5. Discussion](#615-discussion)
      - [6.1.6. Methodologies](#616-methodologies)
      - [6.1.7. Errors and Uncertainties](#617-errors-and-uncertainties)
      - [6.1.8. Reporting the Metric](#618-reporting-the-metric)
    - [6.2. Geometric Stream: Loss Episode Duration](#62-geometric-stream-loss-episode-duration)
      - [6.2.1. Metric Name](#621-metric-name)
      - [6.2.2. Metric Parameters](#622-metric-parameters)
      - [6.2.3. Metric Units](#623-metric-units)
      - [6.2.4. Metric Definition](#624-metric-definition)
      - [6.2.5. Discussion](#625-discussion)
      - [6.2.6. Methodologies](#626-methodologies)
      - [6.2.7. Errors and Uncertainties](#627-errors-and-uncertainties)
      - [6.2.8. Reporting the Metric](#628-reporting-the-metric)
    - [6.3. Geometric Stream: Loss Episode Frequency](#63-geometric-stream-loss-episode-frequency)
      - [6.3.1. Metric Name](#631-metric-name)
      - [6.3.2. Metric Parameters](#632-metric-parameters)
      - [6.3.3. Metric Units](#633-metric-units)
      - [6.3.4. Metric Definition](#634-metric-definition)
      - [6.3.5. Discussion](#635-discussion)
      - [6.3.6. Methodologies](#636-methodologies)
      - [6.3.7. Errors and Uncertainties](#637-errors-and-uncertainties)
      - [6.3.8. Reporting the Metric](#638-reporting-the-metric)
  - [7. Applicability of Loss Episode Metrics](#7-applicability-of-loss-episode-metrics)
    - [7.1. Relation to Gilbert Model](#71-relation-to-gilbert-model)
  - [8. Security Considerations](#8-security-considerations)
  - [9. References](#9-references)
    - [9.1. Normative References](#91-normative-references)
    - [9.2. Informative References](#92-informative-references)

# 1. Introduction

## 1.1. Background and Motivation

Packet loss in the Internet is a complex phenomenon due to the bursty
nature of traffic and congestion processes, influenced by both end-
users and applications and the operation of transport protocols such
as TCP.  For these reasons, the simplest model of packet loss -- the
single parameter Bernoulli (independent) loss model -- does not
represent the complexity of packet loss over periods of time.
Correspondingly, a single loss metric -- the average packet loss
ratio over some period of time -- arising, e.g., from a stream of
Poisson probes as in [RFC2680] is not sufficient to determine the
effect of packet loss on traffic in general.

Moving beyond single parameter loss models, Markovian and Markov-
modulated loss models involving transitions between a good and bad
state, each with an associated loss rate, have been proposed by
Gilbert [Gilbert] and more generally by Elliot [Elliot].  In
principle, Markovian models can be formulated over state spaces
involving patterns of loss of any desired number of packets.
However, further increase in the size of the state space makes such
models cumbersome both for parameter estimation (accuracy decreases)
and prediction in practice (due to computational complexity and
sensitivity to parameter inaccuracy).  In general, the relevance and
importance of particular models can change in time, e.g., in response
to the advent of new applications and services.  For this reason, we
are drawn to empirical metrics that do not depend on a particular
model for their interpretation.

An empirical measure of packet loss complexity, the index of
dispersion of counts (IDC), comprise, for each t >0, the ratio v(t) /
a(t) of the variance v(t) and average a(t) of the number of losses
over successive measurement windows of a duration t.  However, a full
characterization of packet loss over time requires specification of
the IDC for each window size t>0.

In the standards arena, loss pattern sample metrics are defined in
[RFC3357].  Following the Gilbert-Elliot model, burst metrics
specific for Voice over IP (VoIP) that characterize complete episodes
of lost, transmitted, and discarded packets are defined in [RFC3611].

The above considerations motivate the formulation of empirical
metrics of one-way packet loss that provide the simplest
generalization of [RFC2680] (which is widely adopted but only defines
a single loss-to-total ratio metric).  The metrics defined here

capture deviations from independent packet loss in a robust model-
independent manner.  The document also defines efficient measurement
methodologies for these metrics.

### 1.1.1. Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in RFC 2119 [RFC2119].

## 1.2. Loss Episode Metrics and Bi-Packet Probes

The losses experienced by the packet stream can be viewed as
occurring in loss episodes, i.e., a maximal set of consecutively lost
packets.  This memo describes one-way loss episode metrics: their
frequency and average duration.  Although the average loss ratio can
be expressed in terms of these quantities, they go further in
characterizing the statistics of the patterns of packet loss within
the stream of probes.  This is useful information in understanding
the effect of packet losses on application performance, since
different applications can have different sensitivities to patterns
of loss, being sensitive not only to the long-term average loss rate,
but how losses are distributed in time.  As an example, MPEG video
traffic may be sensitive to loss involving the I-frame in a group of
pictures, but further losses within an episode of sufficiently short
duration have no further impact; the damage is already done.

The loss episode metrics presented here have the following useful
properties:

1.  the metrics are empirical and do not depend on an underlying
model; e.g., the loss process is not assumed to be Markovian.  On
the other hand, it turns out that the metrics of this memo can be
related to the special case of the Gilbert Model parameters; see
Section 7.

2.  the metric units can be directly compared with applications or
user requirements or tolerance for network loss performance, in
the frequency and duration of loss episodes, as well as the usual
packet loss ratio, which can be recovered from the loss episode
metrics upon dividing the average loss episode duration by the
loss episode frequency.

3.  the metrics provide the smallest possible increment in complexity
beyond, but in the spirit of, the IP Performance Metrics (IPPM)
average packet loss ratio metrics [RFC2680], i.e., moving from a
single metric (average packet loss ratio) to a pair of metrics
(loss episode frequency and average loss episode duration).

The document also describes a probing methodology under which loss
episode metrics are to be measured.  The methodology comprises
sending probe packets in pairs, where packets within each probe pair
have a fixed separation, and the time between pairs takes the form of
a geometric distributed number multiplied by the same separation.
This can be regarded a generalization of Poisson probing where the
probes are pairs rather than single packets as in [RFC2680], and also
of geometric probing described in [RFC2330].  However, it should be
distinguished from back-to-back packet pairs whose change in
separation on traversing a link is used to probe bandwidth.  In this
document, the separation between the packets in a pair is the
temporal resolution at which different loss episodes are to be
distinguished.  The methodology does not measure episodes of loss of
consecutive background packets on the measured path.  One key feature
of this methodology is its efficiency: it estimates the average
length of loss episodes without directly measuring the complete
episodes themselves.  Instead, this information is encoded in the
observed relative frequencies of the four possible outcomes arising
from the loss or successful transmission of each of the two packets
of the probe pairs.  This is distinct from the approach of [RFC3611],
which reports on directly measured episodes.

The metrics defined in this memo are "derived metrics", according to
Section 6.1 of [RFC2330] (the IPPM framework).  They are based on the
singleton loss metric defined in Section 2 of [RFC2680] .

## 1.3. Outline and Contents

o  Section 2 defines the fundamental singleton metric for the
possible outcomes of a probe pair: Type-P-One-way-Bi-Packet-Loss.

o  Section 3 defines sample sets of this metric derived from a
general probe stream: Type-P-One-way-Bi-Packet-Loss-Stream.

o  Section 4 defines the prime example of the Bi-Packet-Loss-Stream
metrics, specifically Type-P-One-way-Bi-Packet-Loss-Geometric-
Stream arising from the geometric stream of packet-pair probes
that was described informally in Section 1.

o  Section 5 defines loss episode proto-metrics that summarize the
outcomes from a stream metrics as an intermediate step to forming
the loss episode metrics; they need not be reported in general.

o  Section 6 defines the final loss episode metrics that are the
focus of this memo, the new metrics:

*  Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Episode-
Duration, the average duration, in seconds, of a loss episode.

*  Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Episode-
Frequency, the average frequency, per second, at which loss
episodes start.

*  Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Ratio, which is
the average packet loss ratio metric arising from the geometric
stream probing methodology

o  Section 7 details applications and relations to existing loss
models.

# 2. Singleton Definition for Type-P-One-way Bi-Packet Loss

## 2.1. Metric Name

Type-P-One-way-Bi-Packet-Loss

## 2.2. Metric Parameters

o  Src, the IP address of a source host

o  Dst, the IP address of a destination host

o  T1, a sending time of the first packet

o  T2, a sending time of the second packet, with T2>T1

o  F, a selection function defining unambiguously the two packets
from the stream selected for the metric

o  P, the specification of the packet type, over and above the source
and destination addresses

## 2.3. Metric Units

A Loss Pair is pair (l1, l2) where each of l1 and l2 is a binary
value 0 or 1, where 0 signifies successful transmission of a packet
and 1 signifies loss.

The metric unit of Type-P-One-way-Bi-Packet-Loss is a Loss Pair.

## 2.4. Metric Definition

1.  "The Type-P-One-way-Bi-Packet-Loss with parameters (Src, Dst, T1,
T2, F, P) is (1,1)" means that Src sent the first bit of a Type-P
packet to Dst at wire-time T1 and the first bit of a Type-P
packet to Dst at wire-time T2>T1 and that neither packet was
received at Dst.

2.  "The Type-P-One-way-Bi-Packet-Loss with parameters (Src, Dst, T1,
T2, F, P) is (1,0)" means that Src sent the first bit of a Type-P
packet to Dst at wire-time T1 and the first bit of a Type-P
packet to Dst at wire-time T2>T1 and that the first packet was
not received at Dst, and the second packet was received at Dst

3.  "The Type-P-One-way-Bi-Packet-Loss with parameters (Src, Dst, T1,
T2, F, P) is (0,1)" means that Src sent the first bit of a Type-P
packet to Dst at wire-time T1 and the first bit of a Type-P
packet to Dst at wire-time T2>T1 and that the first packet was
received at Dst, and the second packet was not received at Dst

4.  "The Type-P-One-way-Bi-Packet-Loss with parameters (Src, Dst, T1,
T2, F, P) is (0,0)" means that Src sent the first bit of a Type-P
packet to Dst at wire-time T1 and the first bit of a Type-P
packet to Dst at wire-time T2>T1 and that both packets were
received at Dst.

## 2.5. Discussion

The purpose of the selection function is to specify exactly which
packets are to be used for measurement.  The notion is taken from
Section 2.5 of [RFC3393], where examples are discussed.

## 2.6. Methodologies

The methodologies related to the Type-P-One-way-Packet-Loss metric in
Section 2.6 of [RFC2680] are similar for the Type-P-One-way-Bi-
Packet-Loss metric described above.  In particular, the methodologies
described in RFC 2680 apply to both packets of the pair.

## 2.7. Errors and Uncertainties

Sources of error for the Type-P-One-way-Packet-Loss metric in Section
2.7 of [RFC2680] apply to each packet of the pair for the Type-P-One-
way-Bi-Packet-Loss metric.

## 2.8. Reporting the Metric

Refer to Section 2.8 of [RFC2680].

# 3. General Definition of Samples for Type-P-One-way-Bi-Packet-Loss

Given the singleton metric for Type-P-One-way-Bi-Packet-Loss, we now
define examples of samples of singletons.  The basic idea is as
follows.  We first specify a set of times T1 < T2 <...<Tn, each of

which acts as the first time of a packet pair for a single Type-P-
One-way-Bi-Packet-Loss measurement.  This results is a set of n
metric values of Type-P-One-way-Bi-Packet-Loss.

## 3.1. Metric Name

Type-P-One-way-Bi-Packet-Loss-Stream

## 3.2. Metric Parameters

o  Src, the IP address of a source host

o  Dst, the IP address of a destination host

o  (T11,T12), (T21,T22)....,(Tn1,Tn2) a set of n times of sending
times for packet pairs, with T11 < T12 <= T21 < T22 <=...<= Tn1 <
Tn2

o  F, a selection function defining unambiguously the two packets
from the stream selected for the metric

o  P, the specification of the packet type, over and above the source
and destination address

## 3.3. Metric Units

A set L1,L2,...,Ln of Loss Pairs

## 3.4. Metric Definition

Each Loss Pair Li for i = 1,....n is the Type-P-One-way-Bi-Packet-
Loss with parameters (Src, Dst, Ti1, Ti2, Fi, P) where Fi is the
restriction of the selection function F to the packet pair at time
Ti1, Ti2.

## 3.5. Discussion

The metric definition of Type-P-One-way-Bi-Packet-Loss-Stream is
sufficiently general to describe the case where packets are sampled
from a preexisting stream.  This is useful in the case in which there
is a general purpose measurement stream set up between two hosts, and
we wish to select a substream from it for the purposes of loss
episode measurement.  Packet pairs selected as bi-packet loss probes
need not be consecutive within such a stream.  In the next section,
we specialize this somewhat to more concretely describe a purpose
built packet stream for loss episode measurement.

## 3.6. Methodologies

The methodologies related to the Type-P-One-way-Packet-Loss metric in
Section 2.6 of [RFC2680] are similar for the Type-P-One-way-Bi-
Packet-Loss-Stream metric described above.  In particular, the
methodologies described in RFC 2680 apply to both packets of each
pair.

## 3.7. Errors and Uncertainties

Sources of error for the Type-P-One-way-Packet-Loss metric in Section
2.7 of [RFC2680] apply to each packet of each pair for the Type-P-
One-way-Bi-Packet-Loss-Stream metric.

## 3.8. Reporting the Metric

Refer to Section 2.8 of [RFC2680].

# 4. An Active Probing Methodology for Bi-Packet Loss

This section specializes the preceding section for an active probing
methodology.  The basic idea is a follows.  We set up a sequence of
evenly spaced times T1 < T2 < ... < Tn.  Each time Ti is potentially
the first packet time for a packet pair measurement.  We make an
independent random decision at each time, whether to initiate such a
measurement.  Hence, the interval count between successive times at
which a pair is initiated follows a geometric distribution.  We also
specify that the spacing between successive times Ti is the same as
the spacing between packets in a given pair.  Thus, if pairs happen
to be launched at the successive times Ti and T(i+1), the second
packet of the first pair is actually used as the first packet of the
second pair.

## 4.1. Metric Name

Type-P-One-way-Bi-Packet-Loss-Geometric-Stream

## 4.2. Metric Parameters

o  Src, the IP address of a source host

o  Dst, the IP address of a destination host

o  T0, the randomly selected starting time [RFC3432] for periodic
launch opportunities

o  d, the time spacing between potential launch times, Ti and T(i+1)

o  n, a count of potential measurement instants

o  q, a launch probability

o  F, a selection function defining unambiguously the two packets
from the stream selected for the metric

o  P, the specification of the packet type, over and above the source
and destination address

## 4.3. Metric Units

A set of Loss Pairs L1, L2, ..., Lm for some m <= n

## 4.4. Metric Definition

For each i = 0, 1, ..., n-1 we form the potential measurement time Ti
= T0 + i*d.  With probability q, a packet pair measurement is
launched at Ti, resulting in a Type-P-One-way-Bi-Packet-Loss with
parameters (Src, Dst, Ti, T(i+1), Fi, P) where Fi is the restriction
of the selection function F to the packet pair at times Ti, T(i+1).
L1, L2,...Lm are the resulting Loss Pairs; m can be less than n since
not all times Ti have an associated measurement.

## 4.5. Discussion

The above definition of Type-P-One-way-Bi-Packet-Loss-Geometric-
Stream is equivalent to using Type-P-One-way-Bi-Packet-Loss-Stream
with an appropriate statistical definition of the selection function
F.

The number m of Loss Pairs in the metric can be less than the number
of potential measurement instants because not all instants may
generate a probe when the launch probability q is strictly less than
1.

## 4.6. Methodologies

The methodologies follow from:

o  the specific time T0, from which all successive Ti follow, and

o  the specific time spacing, and

o  the methodologies discussion given above for the singleton Type-P-
One-way-Bi-Packet-Loss metric.

The issue of choosing an appropriate time spacing (e.g., one that is
matched to expected characteristics of loss episodes) is outside the
scope of this document.

Note that as with any active measurement methodology, consideration
must be made to handle out-of-order arrival of packets; see also
Section 3.6. of [RFC2680].

## 4.7. Errors and Uncertainties

In addition to sources of errors and uncertainties related to
methodologies for measuring the singleton Type-P-One-way-Bi-Packet-
Loss metric, a key source of error when emitting packets for Bi-
Packet Loss relates to resource limits on the host used to send the
packets.  In particular, the choice of T0, the choice of the time
spacing, and the choice of the launch probability results in a
schedule for sending packets.  Insufficient CPU resources on the
sending host may result in an inability to send packets according to
schedule.  Note that the choice of time spacing directly affects the
ability of the host CPU to meet the required schedule (e.g., consider
a 100 microsecond spacing versus a 100 millisecond spacing).

For other considerations, refer to Section 3.7 of [RFC2680].

## 4.8. Reporting the Metric

Refer to Section 3.8. of [RFC2680].

# 5. Loss Episode Proto-Metrics

This section describes four generic proto-metric quantities
associated with an arbitrary set of Loss Pairs.  These are the Loss-
Pair-Counts, Bi-Packet-Loss-Ratio, Bi-Packet-Loss-Episode-Duration-
Number, Bi-Packet-Loss-Episode-Frequency-Number.  Specific loss
episode metrics can then be constructed when these proto-metrics
take, as their input, sets of Loss Pairs samples generated by the
Type-P-One-way-Bi-Packet-Loss-Stream and Type-P-One-way-Bi-Packet-
Loss-Geometric-Stream.  The second of these is described in
Section 4.  It is not expected that these proto-metrics would be
reported themselves.  Rather, they are intermediate quantities in the
production of the final metrics of Section 6 below, and could be
rolled up into metrics in implementations.  The metrics report loss
episode durations and frequencies in terms of packet counts, since
they do not depend on the actual time between probe packets.  The
final metrics of Section 6 incorporate timescales and yield durations
in seconds and frequencies as per second.

## 5.1. Loss-Pair-Counts

Loss-Pair-Counts are the absolute frequencies of the four types of
Loss Pair outcome in a sample.  More precisely, the Loss-Pair-Counts
associated with a set of Loss Pairs L1,,,,Ln are the numbers N(i,j)
of such Loss Pairs that take each possible value (i,j) in the set (
(0,0), (0,1), (1,0), (1,1)).

## 5.2. Bi-Packet-Loss-Ratio

The Bi-Packet-Loss-Ratio associated with a set of n Loss Pairs
L1,,,,Ln is defined in terms of their Loss-Pair-Counts by the
quantity (N(1,0) + N(1,1))/n.

Note this is formally equivalent to the loss metric Type-P-One-way-
Packet-Loss-Average from [RFC2680], since it averages single packet
losses.

## 5.3. Bi-Packet-Loss-Episode-Duration-Number

The Bi-Packet-Loss-Episode-Duration-Number associated with a set of n
Loss Pairs L1,,,,Ln is defined in terms of their Loss-Pair-Counts in
the following cases:

o  (2*N(1,1) + N(0,1) + N(1,0)) / (N(0,1) + N(1,0)) if N(0,1) +
N(1,0) > 0

o  0 if N(0,1) + N(1,0) + N(1,1) = 0 (no probe packets lost)

o  Undefined if N(0,1) + N(1,0) + N(0,0) = 0 (all probe packets lost)

Note N(0,1) + N(1,0) is zero if there are no transitions between loss
and no-loss outcomes.

## 5.4. Bi-Packet-Loss-Episode-Frequency-Number

The Bi-Packet-Loss-Episode-Frequency-Number associated with a set of
n Loss Pairs L1,,,,Ln is defined in terms of their Loss-Pair-Counts
as Bi-Packet-Loss-Ratio / Bi-Packet-Loss-Episode-Duration-Number,
when this can be defined, specifically, it is as follows:

o  (N(1,0) + N(1,1)) * (N(0,1) + N(1,0)) / (2*N(1,1) + N(0,1) +
N(1,0) ) / n if N(0,1) + N(1,0) > 0

o  0 if N(0,1) + N(1,0) + N(1,1) = 0 (no probe packets lost)

o  1 if N(0,1) + N(1,0) + N(0,0) = 0 (all probe packets lost)

# 6. Loss Episode Metrics Derived from Bi-Packet Loss Probing

Metrics for the time frequency and time duration of loss episodes are
now defined as functions of the set of n Loss Pairs L1,....,Ln.
Although a loss episode is defined as a maximal set of successive
lost packets, the loss episode metrics are not defined directly in
terms of the sequential patterns of packet loss exhibited by Loss
Pairs.  This is because samples, including Type-P-One-way-Bi-Packet-
Loss-Geometric-Stream, generally do not report all lost packets in
each episode.  Instead, the metrics are defined as functions of the
Loss-Pair-Counts of the sample, for reasons that are now described.

Consider an idealized Type-P-One-way-Bi-Packet-Loss-Geometric-Stream
sample in which the launch probability q =1.  It is shown in [SBDR08]
that the average number of packets in a loss episode of this ideal
sample is exactly the Bi-Packet-Loss-Episode-Duration derived from
its set of Loss Pairs.  Note this computation makes no reference to
the position of lost packet in the sequence of probes.

A general Type-P-One-way-Bi-Packet-Loss-Geometric-Stream sample with
launch probability q < 1, independently samples, with probability q,
each Loss Pair of an idealized sample.  On average, the Loss-Pair-
Counts (if normalized by the total number of pairs) will be the same
as in the idealized sample.  The loss episode metrics in the general
case are thus estimators of those for the idealized case; the
statistical properties of this estimation, including a derivation of
the estimation variance, is provided in [SBDR08].

## 6.1. Geometric Stream: Loss Ratio

### 6.1.1. Metric Name

Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Ratio

### 6.1.2. Metric Parameters

o  Src, the IP address of a source host

o  Dst, the IP address of a destination host

o  T0, the randomly selected starting time [RFC3432] for periodic
launch opportunities

o  d, the time spacing between potential launch times, Ti and T(i+1)

o  n, a count of potential measurement instants

o  q, a launch probability

o  F, a selection function defining unambiguously the two packets
from the stream selected for the metric

o  P, the specification of the packet type, over and above the source
and destination address

### 6.1.3. Metric Units

A decimal number in the interval [0,1]

### 6.1.4. Metric Definition

The result obtained by computing the Bi-Packet-Loss-Ratio over a
Type-P-One-way-Bi-Packet-Loss-Geometric-Stream sample with the metric
parameters.

### 6.1.5. Discussion

Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Ratio estimates the
fraction of packets lost from the geometric stream of Bi-Packet
probes.

### 6.1.6. Methodologies

Refer to Section 4.6.

### 6.1.7. Errors and Uncertainties

Because Type-P-One-way-Bi-Packet-Loss-Geometric-Stream is sampled in
general (when the launch probability q <1), the metrics described in
this section can be regarded as statistical estimators of the
corresponding idealized version corresponding to q = 1.  Estimation
variance as it applies to Type-P-One-way-Bi-Packet-Loss-Geometric-
Stream-Loss-Ratio is described in [SBDR08].

For other issues, refer to Section 4.7

### 6.1.8. Reporting the Metric

Refer to Section 4.8.

## 6.2. Geometric Stream: Loss Episode Duration

### 6.2.1. Metric Name

Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Episode-Duration

### 6.2.2. Metric Parameters

o  Src, the IP address of a source host

o  Dst, the IP address of a destination host

o  T0, the randomly selected starting time [RFC3432] for periodic
launch opportunities

o  d, the time spacing between potential launch times, Ti and T(i+1)

o  n, a count of potential measurement instants

o  q, a launch probability

o  F, a selection function defining unambiguously the two packets
from the stream selected for the metric

o  P, the specification of the packet type, over and above the source
and destination address

### 6.2.3. Metric Units

A non-negative number of seconds

### 6.2.4. Metric Definition

The result obtained by computing the Bi-Packet-Loss-Episode-Duration-
Number over a Type-P-One-way-Bi-Packet-Loss-Geometric-Stream sample
with the metric parameters, then multiplying the result by the launch
spacing parameter d.

### 6.2.5. Discussion

Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Episode-Duration
estimates the average duration of a loss episode, measured in
seconds.  The duration measured in packets is obtained by dividing
the metric value by the packet launch spacing parameter d.

### 6.2.6. Methodologies

Refer to Section 4.6.

### 6.2.7. Errors and Uncertainties

Because Type-P-One-way-Bi-Packet-Loss-Geometric-Stream is sampled in
general (when the launch probability q <1), the metrics described in
this section can be regarded as statistical estimators of the
corresponding idealized version corresponding to q = 1.  Estimation
variance as it applies to Type-P-One-way-Bi-Packet-Loss-Geometric-
Stream-Episode-Duration is described in [SBDR08].

For other issues, refer to Section 4.7

### 6.2.8. Reporting the Metric

Refer to Section 4.8.

## 6.3. Geometric Stream: Loss Episode Frequency

### 6.3.1. Metric Name

Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Episode-Frequency

### 6.3.2. Metric Parameters

o  Src, the IP address of a source host

o  Dst, the IP address of a destination host

o  T0, the randomly selected starting time [RFC3432] for periodic
launch opportunities

o  d, the time spacing between potential launch times, Ti and T(i+1)

o  n, a count of potential measurement instants

o  q, a launch probability

o  F, a selection function defining unambiguously the two packets
from the stream selected for the metric

o  P, the specification of the packet type, over and above the source
and destination address

### 6.3.3. Metric Units

A positive number

### 6.3.4. Metric Definition

The result obtained by computing the Bi-Packet-Loss-Episode-
Frequency-Number over a Type-P-One-way-Bi-Packet-Loss-Geometric-
Stream sample with the metric parameters, then dividing the result by
the launch spacing parameter d.

### 6.3.5. Discussion

Type-P-One-way-Bi-Packet-Loss-Geometric-Stream-Episode-Frequency
estimates the average frequency per unit time with which loss
episodes start (or finish).  The frequency relative to the count of
potential probe launches is obtained by multiplying the metric value
by the packet launch spacing parameter d.

### 6.3.6. Methodologies

Refer to Section 4.6.

### 6.3.7. Errors and Uncertainties

Because Type-P-One-way-Bi-Packet-Loss-Geometric-Stream is sampled in
general (when the launch probability q <1), the metrics described in
this section can be regarded as statistical estimators of the
corresponding idealized version corresponding to q = 1.  Estimation
variance as it applies to Type-P-One-way-Bi-Packet-Loss-Geometric-
Stream-Episode-Frequency is described in [SBDR08].

For other issues, refer to Section 4.7

### 6.3.8. Reporting the Metric

Refer to Section 4.8.

# 7. Applicability of Loss Episode Metrics

## 7.1. Relation to Gilbert Model

The general Gilbert-Elliot model is a discrete time Markov chain over
two states, Good (g) and Bad (b), each with its own independent
packet loss ratio.  In the simplest case, the Good loss ratio is 0,
while the Bad loss ratio is 1.  Correspondingly, there are two
independent parameters, the Markov transition probabilities P(g|b) =
1- P(b|b) and P(b|g) = 1- P(g|g), where P(i|j) is the probability to
transition from state j and step n to state i at step n+1.  With
these parameters, the fraction of steps spent in the bad state is
P(b|g)/(P(b|g) + P(g|b)), while the average duration of a sojourn in
the bad state is 1/P(g|b) steps.

Now identify the steps of the Markov chain with the possible sending
times of packets for a Type-P-One-way-Bi-Packet-Loss-Geometric-Stream
with launch spacing d.  Suppose the loss episode metrics Type-P-One-
way-Bi-Packet-Loss-Geometric-Stream-Ratio and Type-P-One-way-Bi-
Packet-Loss-Geometric-Stream-Episode-Duration take the values r and
m, respectively.  Then, from the discussion in Section 6.1.5, the
following can be equated:

r = P(b|g)/(P(b|g) + P(g|b)) and m/d = 1/P(g|b).

These relationships can be inverted in order to recover the Gilbert
model parameters:

P(g|b) = d/m and P(b|g)=d/m/(1/r - 1)

# 8. Security Considerations

Conducting Internet measurements raises both security and privacy
concerns.  This memo does not specify an implementation of the
metrics, so it does not directly affect the security of the Internet
or of applications that run on the Internet.  However,implementations
of these metrics must be mindful of security and privacy concerns.

There are two types of security concerns: potential harm caused by
the measurements and potential harm to the measurements.  The
measurements could cause harm because they are active and inject
packets into the network.  The measurement parameters MUST be
carefully selected so that the measurements inject trivial amounts of
additional traffic into the networks they measure.  If they inject
"too much" traffic, they can skew the results of the measurement and,
in extreme cases, cause congestion and denial of service.  The
measurements themselves could be harmed by routers giving measurement
traffic a different priority than "normal" traffic, or by an attacker
injecting artificial measurement traffic.  If routers can recognize
measurement traffic and treat it separately, the measurements may not
reflect actual user traffic.  If an attacker injects artificial
traffic that is accepted as legitimate, the loss rate will be
artificially lowered.  Therefore, the measurement methodologies
SHOULD include appropriate techniques to reduce the probability that
measurement traffic can be distinguished from "normal" traffic.
Authentication techniques, such as digital signatures, may be used
where appropriate to guard against injected traffic attacks.  The
privacy concerns of network measurement are limited by the active
measurements described in this memo: they involve no release of user
data.

# 9. References

## 9.1. Normative References

[RFC2680]  Almes, G., Kalidindi, S., and M. Zekauskas, "A One-way
Packet Loss Metric for IPPM", RFC 2680, September 1999.

[RFC3393]  Demichelis, C. and P. Chimento, "IP Packet Delay Variation
Metric for IP Performance Metrics (IPPM)", RFC 3393,
November 2002.

[RFC3611]  Friedman, T., Caceres, R., and A. Clark, "RTP Control
Protocol Extended Reports (RTCP XR)", RFC 3611,
November 2003.

[RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[RFC3432]  Raisanen, V., Grotefeld, G., and A. Morton, "Network
performance measurement with periodic streams", RFC 3432,
November 2002.

## 9.2. Informative References

[RFC2330]  Paxson, V., Almes, G., Mahdavi, J., and M. Mathis,
"Framework for IP Performance Metrics", RFC 2330,
May 1998.

[RFC3357]  Koodli, R. and R. Ravikanth, "One-way Loss Pattern Sample
Metrics", RFC 3357, August 2002.

[SBDR08]   IEEE/ACM Transactions on Networking, 16(2): 307-320, "A
Geometric Approach to Improving Active Packet Loss
Measurement", 2008.

[Gilbert]  Gilbert, E.N., "Capacity of a Burst-Noise Channel. Bell
System Technical Journal 39 pp 1253-1265", 1960.

[Elliot]   Elliott, E.O., "Estimates of Error Rates for Codes on
Burst-Noise Channels. Bell System Technical Journal 42 pp
1977-1997", 1963.

# Authors' Addresses

Nick Duffield
AT&T Labs-Research
180 Park Avenue
Florham Park, NJ  07932
USA

Phone: +1 973 360 8726
Fax:   +1 973 360 8871
EMail: duffield@research.att.com
URI:   http://www.research.att.com/people/Duffield_Nicholas_G

Al Morton
AT&T Labs
200 Laurel Avenue South
Middletown,, NJ  07748
USA

Phone: +1 732 420 1571
Fax:   +1 732 368 1192
EMail: acmorton@att.com
URI:   http://home.comcast.net/~acmacm/

Joel Sommers
Colgate University
304 McGregory Hall
Hamilton, NY  13346
USA

Phone: +1 315 228 7587
Fax:
EMail: jsommers@colgate.edu
URI:   http://cs.colgate.edu/faculty/jsommers
