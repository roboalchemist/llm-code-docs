Module org.easymock
Package org.easymock

## Interface IAnswer<T>

- 

Type Parameters:
`T` - the type to return.

All Known Implementing Classes:
`Result`

---

```
public interface IAnswer<T>
```

Used to answer expected calls.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description

`T`
`answer()`

Is called by EasyMock to answer an expected call.

- 

  - 

### Method Detail

    - 

#### answer

```
T answer()
  throws Throwable
```

Is called by EasyMock to answer an expected call. The answer may be to
 return a value, or to throw an exception. The arguments of the call for
 which the answer is generated are available via
 `EasyMock.getCurrentArgument(int)` or `EasyMock.getCurrentArguments()`.
 The former method is preferred since it will infer the argument type.

Returns:
the value to be returned
Throws:
`Throwable` - the throwable to be thrown