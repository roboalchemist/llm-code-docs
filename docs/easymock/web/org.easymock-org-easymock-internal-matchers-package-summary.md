Module org.easymock

# Package org.easymock.internal.matchers

- 

Class Summary 

Class
Description

And

Matches if all given argument matchers match.

Any

Matches any argument.

ArrayEquals

Matches if the argument is an array where the elements are equal to the given array.

Captures<T>

Captures the argument to retrieve it later and matches anything.

Compare<T>

Matches if the argument, when compared (`Comparator.compare()`), agrees with the logical operator.

CompareEqual<T extends Comparable<T>>

Matches if the argument is equal when compared (as in `Comparable.compareTo() == 0`) to the given value.

CompareTo<T extends Comparable<T>>

Base class for matchers that are comparing a value to another.

Contains

Matches if the argument is a string containing a given substring.

EndsWith

Matches if the argument is a string ending with a given suffix.

Equals

Matches if the argument is equal to the given value.

EqualsWithDelta

Matches if the argument is a number equal to the given value with some tolerance equal to delta.

Find

Matches if the argument is a string in which a regex can be found.

GreaterOrEqual<T extends Comparable<T>>

Matches if the argument is greater or equal to the given value.

GreaterThan<T extends Comparable<T>>

Matches if the argument is strictly greater than the given value.

InstanceOf

Matches if the argument is an instance of the given class.

LessOrEqual<T extends Comparable<T>>

Matches if the argument is less or equal to the given value.

LessThan<T extends Comparable<T>>

Match if the argument is less than the given value.

Matches

Matches if the argument is a string matching a given regex.

Not

Matches if the argument DOESN'T match another.

NotNull

Matches if the argument is not null.

Null

Matches if the argument is null.

Or

Matches if any given argument matcher matches.

Same

Matches if the argument is the same instance as the given value.

StartsWith

Matches if the argument is a string starting with the given prefix.