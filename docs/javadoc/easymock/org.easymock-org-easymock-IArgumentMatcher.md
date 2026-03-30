Module org.easymock
Package org.easymock

## Interface IArgumentMatcher

- 

All Known Implementing Classes:
`And`, `Any`, `ArrayEquals`, `Captures`, `Compare`, `CompareEqual`, `CompareTo`, `Contains`, `EndsWith`, `Equals`, `EqualsWithDelta`, `Find`, `GreaterOrEqual`, `GreaterThan`, `InstanceOf`, `LessOrEqual`, `LessThan`, `Matches`, `Not`, `NotNull`, `Null`, `Or`, `Same`, `StartsWith`

---

```
public interface IArgumentMatcher
```

Decides whether an actual argument is accepted.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description

`void`
`appendTo​(StringBuffer buffer)`

Appends a string representation of this matcher to the given buffer.

`boolean`
`matches​(Object argument)`

Returns whether this matcher accepts the given argument.

- 

  - 

### Method Detail

    - 

#### matches

```
boolean matches​(Object argument)
```

Returns whether this matcher accepts the given argument.
 

 Like Object.equals(), it should be aware that the argument passed might
 be null and of any type. So you will usually start the method with an
 instanceof and/or null check.
 

 The method should **never** assert if the argument doesn't match. It
 should only return false. EasyMock will take care of asserting if the
 call is really unexpected.

Parameters:
`argument` - the argument
Returns:
whether this matcher accepts the given argument.

    - 

#### appendTo

```
void appendTo​(StringBuffer buffer)
```

Appends a string representation of this matcher to the given buffer. In
 case of failure, the printed message will show this string to allow to
 know which matcher was used for the failing call.

Parameters:
`buffer` - the buffer to which the string representation is appended.