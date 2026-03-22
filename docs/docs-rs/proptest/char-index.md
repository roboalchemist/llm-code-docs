proptest
# Module char 
Source 
## Structs§
CharStrategyStrategy for generating `char`s.CharValueTreeThe `ValueTree` corresponding to `CharStrategy`.
## Constants§
DEFAULT_PREFERRED_RANGESA default sequence of ranges used preferentially when generating random
characters.DEFAULT_SPECIAL_CHARSA default set of characters to consider as “special” during character
generation.
## Functions§
anyCreates a `CharStrategy` which picks from literally any character, with the
default biases.rangeCreates a `CharStrategy` which selects characters within the given
endpoints, inclusive, using the default biases.rangesCreates a `CharStrategy` which selects characters within the given ranges,
all inclusive, using the default biases.select_charSelects a random character the way `CharStrategy` does.