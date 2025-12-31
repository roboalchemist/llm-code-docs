# Source: https://firebase.google.com/docs/reference/js/ai.segment.md.txt

# Segment interface

Represents a specific segment within a [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) object, often used to pinpoint the exact location of text or data that grounding information refers to.

**Signature:**  

    export interface Segment 

## Properties

|                                          Property                                           |  Type  |                                                                                                                                                  Description                                                                                                                                                  |
|---------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [endIndex](https://firebase.google.com/docs/reference/js/ai.segment.md#segmentendindex)     | number | The zero-based end index of the segment within the specified `Part`, measured in UTF-8 bytes. This offset is exclusive, meaning the character at this index is not included in the segment.                                                                                                                   |
| [partIndex](https://firebase.google.com/docs/reference/js/ai.segment.md#segmentpartindex)   | number | The zero-based index of the [Part](https://firebase.google.com/docs/reference/js/ai.md#part) object within the `parts` array of its parent [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) object. This identifies which part of the content the segment belongs to. |
| [startIndex](https://firebase.google.com/docs/reference/js/ai.segment.md#segmentstartindex) | number | The zero-based start index of the segment within the specified `Part`, measured in UTF-8 bytes. This offset is inclusive, starting from 0 at the beginning of the part's content (e.g., `Part.text`).                                                                                                         |
| [text](https://firebase.google.com/docs/reference/js/ai.segment.md#segmenttext)             | string | The text corresponding to the segment from the response.                                                                                                                                                                                                                                                      |

## Segment.endIndex

The zero-based end index of the segment within the specified `Part`, measured in UTF-8 bytes. This offset is exclusive, meaning the character at this index is not included in the segment.

**Signature:**  

    endIndex: number;

## Segment.partIndex

The zero-based index of the [Part](https://firebase.google.com/docs/reference/js/ai.md#part) object within the `parts` array of its parent [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) object. This identifies which part of the content the segment belongs to.

**Signature:**  

    partIndex: number;

## Segment.startIndex

The zero-based start index of the segment within the specified `Part`, measured in UTF-8 bytes. This offset is inclusive, starting from 0 at the beginning of the part's content (e.g., `Part.text`).

**Signature:**  

    startIndex: number;

## Segment.text

The text corresponding to the segment from the response.

**Signature:**  

    text: string;