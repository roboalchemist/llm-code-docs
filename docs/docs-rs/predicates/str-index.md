predicates

# Module str

Source

## Structs§

ContainsPredicatePredicate that checks for patterns.DifferencePredicate`diff`Predicate that diffs two strings.EndsWithPredicatePredicate checks end of strIsEmptyPredicatePredicate that checks for empty strings.MatchesPredicatePredicate that checks for repeated patterns.NormalizedPredicate`normalize-line-endings`Predicate adapter that normalizes the newlines contained in the variable being tested.RegexMatchesPredicate`regex`Predicate that checks for repeated patterns.RegexPredicate`regex`Predicate that uses regex matchingStartsWithPredicatePredicate checks start of strTrimPredicatePredicate adapter that trims the variable being tested.Utf8PredicatePredicate adapter that converts a `str` predicate to byte predicate.

## Traits§

PredicateStrExt`Predicate` extension adapting a `str` Predicate.

## Functions§

containsCreates a new `Predicate` that ensures a str contains `pattern`diff`diff`Creates a new `Predicate` that diffs two strings.ends_withCreates a new `Predicate` that ensures a str ends with `pattern`is_emptyCreates a new `Predicate` that ensures a str is emptyis_match`regex`Creates a new `Predicate` that uses a regular expression to match the string.starts_withCreates a new `Predicate` that ensures a str starts with `pattern`

## Type Aliases§

RegexError`regex`An error that occurred during parsing or compiling a regular expression.
