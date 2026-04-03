# RDAttachmentFormat in English

# RDAttachmentFormat
Inherits:RefCounted<Object
Attachment format (used byRenderingDevice).

## Description
This object is used byRenderingDevice.

## Properties

| DataFormat | format | 36 |
|---|---|---|
| TextureSamples | samples | 0 |
| int | usage_flags | 0 |

DataFormat
format
TextureSamples
samples
usage_flags

## Property Descriptions
DataFormatformat=36🔗
- voidset_format(value:DataFormat)
voidset_format(value:DataFormat)
- DataFormatget_format()
DataFormatget_format()
The attachment's data format.
TextureSamplessamples=0🔗
- voidset_samples(value:TextureSamples)
voidset_samples(value:TextureSamples)
- TextureSamplesget_samples()
TextureSamplesget_samples()
The number of samples used when sampling the attachment.
intusage_flags=0🔗
- voidset_usage_flags(value:int)
voidset_usage_flags(value:int)
- intget_usage_flags()
intget_usage_flags()
The attachment's usage flags, which determine what can be done with it.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.