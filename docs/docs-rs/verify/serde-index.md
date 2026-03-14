verify
# Module serde 
Source Available on **crate feature `serde`** only.
## Structs§
KeySpansKeySpans associates nested values with their
full path from the first value as a Vec of Strings.SpannedSpanned allows validation of any value that implements Serde Serialize with
a given Spans.
## Enums§
NewSpanType returned by Spans, it dictates
how the newly returned spans should be used.
## Traits§
SpansSpans is used to provide spans for values that implement Serde Serialize.