inquire
# Module type_aliases 
Source 
## Type Aliases§
CompleterType alias to represent the function used to retrieve an optional autocompletion suggestion.
The function receives the current input and should return the suggestion (if any)
that will replace the current input.ScorerType alias to represent the function used to Score and filter options.SorterType alias to represent the function used to sort a slice of (index, score) tuples.SuggesterType alias to represent the function used to retrieve text input suggestions.
The function receives the current input and should return a collection of strings
containing the suggestions to be made to the user.