spdx
# Module lexer 
Source 
## Structs§
LexerAllows iteration through an SPDX license expression, yielding
a token or a `ParseError`.LexerTokenA wrapper around a particular token that includes the span of the characters
in the original string, for diagnostic purposesParseModeParsing configuration for SPDX expression
## Enums§
TokenA single token in an SPDX license expression