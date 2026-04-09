proptest
# Module string 
Source Available on **crate feature `std`** only.
## Structs§
RegexGeneratorStrategyStrategy which generates values (i.e., `String` or `Vec<u8>`) matching
a regular expression.RegexGeneratorValueTree`ValueTree` corresponding to `RegexGeneratorStrategy`.StringParamWraps the regex that forms the `Strategy` for `String` so that a sensible
`Default` can be given. The default is a string of non-control characters.
## Enums§
ErrorErrors which may occur when preparing a regular expression for use with
string generation.
## Functions§
bytes_regexCreates a strategy which generates byte strings matching the given regular
expression.bytes_regex_parsedLike `bytes_regex()`, but allows providing a pre-parsed expression.string_regexCreates a strategy which generates strings matching the given regular
expression.string_regex_parsedLike `string_regex()`, but allows providing a pre-parsed expression.