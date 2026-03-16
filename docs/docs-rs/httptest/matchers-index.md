httptest
# Module matchers 
Source 
## Modules§
requestMatchers that extract information from HTTP requests.
## Macros§
all_oftrue if all the provided matchers return true.any_oftrue if any of the provided matchers return true.
## Structs§
AllOfThe `AllOf` mapper returned by all_of()AnyThe `Any` mapper returned by any()AnyOfThe `AnyOf` mapper returned by any_of()ContainsThe `Contains` mapper returned by contains()EqThe `Eq` mapper returned by eq()ExecutionContextAn ExecutionContext tracks how Matchers are chained together. There is a
single public method called chain that when used to chain input from one
matcher to another will allow tracking the flow of data across composable
matchers.JsonDecodedThe `JsonDecoded` mapper returned by json_decoded()KVA key-value pair.KeyThe `Key` mapper returned by key()LenThe `Len` mapper returned by len()LowercaseThe `Lowercase` mapper returned by lowercase()MatchesThe `Matches` mapper returned by matches()NotThe `Not` mapper returned by not()UrlDecodedThe `UrlDecoded` mapper returned by url_decoded()ValueThe `Value` mapper returned by value()
## Traits§
IntoRegexCreate a regex.MatcherThe core trait. Defines how an input value should be turned into an output
value. This allows for a flexible pattern of composition where two or more
matchers are chained together to form a readable and flexible manipulation.
## Functions§
all_oftrue if all the provided matchers return true. See the `all_of!` macro for
convenient usage.anyAlways true.any_oftrue if any of the provided matchers returns true. See the `any_of!` macro
for convenient usage.containstrue if any input element matches the provided mapper.eqtrue if the input is equal to value.json_decodedjson decode the input and pass the resulting value to the inner mapper. If
the input cannot be decoded a false value is returned.keyextract the key from a key-value pair.lenextract the length of the input.lowercaselowercase the input and pass it to the next mapper.matchestrue if the input matches the regex provided.notinvert the result of the inner mapper.url_decodedurl decode the input and pass the resulting slice of key-value pairs to the next mapper.valueextract the value from a key-value pair.