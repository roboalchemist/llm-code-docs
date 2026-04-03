# Source: https://firebase.google.com/docs/reference/js/vertexai.groundingattribution.md.txt

# GroundingAttribution interface

> | **Warning:** This API is now obsolete.

**Signature:**  

    export interface GroundingAttribution 

## Properties

|                                                                Property                                                                 |                                                                            Type                                                                            | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [confidenceScore](https://firebase.google.com/docs/reference/js/vertexai.groundingattribution.md#groundingattributionconfidencescore)   | number                                                                                                                                                     |             |
| [retrievedContext](https://firebase.google.com/docs/reference/js/vertexai.groundingattribution.md#groundingattributionretrievedcontext) | [RetrievedContextAttribution](https://firebase.google.com/docs/reference/js/vertexai.retrievedcontextattribution.md#retrievedcontextattribution_interface) |             |
| [segment](https://firebase.google.com/docs/reference/js/vertexai.groundingattribution.md#groundingattributionsegment)                   | [Segment](https://firebase.google.com/docs/reference/js/vertexai.segment.md#segment_interface)                                                             |             |
| [web](https://firebase.google.com/docs/reference/js/vertexai.groundingattribution.md#groundingattributionweb)                           | [WebAttribution](https://firebase.google.com/docs/reference/js/vertexai.webattribution.md#webattribution_interface)                                        |             |

## GroundingAttribution.confidenceScore

**Signature:**  

    confidenceScore?: number;

## GroundingAttribution.retrievedContext

**Signature:**  

    retrievedContext?: RetrievedContextAttribution;

## GroundingAttribution.segment

**Signature:**  

    segment: Segment;

## GroundingAttribution.web

**Signature:**  

    web?: WebAttribution;