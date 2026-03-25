Module org.easymock
Package org.easymock

## Class Capture<T>

- java.lang.Object

- 

  - org.easymock.Capture<T>

- 

Type Parameters:
`T` - Type of the captured element

All Implemented Interfaces:
`Serializable`

---

```
public class Capture<T>
extends Object
implements Serializable
```

Will contain what was captured by the `capture()` matcher. Knows
 if something was captured or not (allows to capture a null value).

 **Implementation note:**
 If the capture is serialized, it is the user duty to make sure the transformation used also is serializable.

Author:
Henri Tremblay
See Also:
Serialized Form

- 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`T`
`getValue()`

Return captured value.

`List<T>`
`getValues()`

Return all captured values.

`boolean`
`hasCaptured()`
 

`static <T> Capture<T>`
`newInstance()`

Create a new capture instance that will keep only the last captured value.

`static <T> Capture<T>`
`newInstance​(UnaryOperator<T> transform)`

Create a new capture instance with a specific transformation
 function to change the values into a different value.

`static <T> Capture<T>`
`newInstance​(CaptureType type)`

Create a new capture instance with a specific `CaptureType`.

`static <T> Capture<T>`
`newInstance​(CaptureType type,
           UnaryOperator<T> transform)`

Create a new capture instance with a specific `CaptureType`
 and a specific transformation function to change the values
 into a different value.

`void`
`reset()`

Will reset capture to a "nothing captured yet" state

`void`
`setValue​(T value)`

Used internally by the EasyMock framework to add a new captured value.

`String`
`toString()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### newInstance

```
public static <T> Capture<T> newInstance()
```

Create a new capture instance that will keep only the last captured value.

Type Parameters:
`T` - type of the class to be captured
Returns:
the new capture object

    - 

#### newInstance

```
public static <T> Capture<T> newInstance​(CaptureType type)
```

Create a new capture instance with a specific `CaptureType`.

Type Parameters:
`T` - type of the class to be captured
Parameters:
`type` - capture type wanted
Returns:
the new capture object

    - 

#### newInstance

```
public static <T> Capture<T> newInstance​(CaptureType type,
                                         UnaryOperator<T> transform)
```

Create a new capture instance with a specific `CaptureType`
 and a specific transformation function to change the values
 into a different value.

Type Parameters:
`T` - type of the class to be captured
Parameters:
`type` - capture type wanted
`transform` - the transform function
Returns:
the new capture object

    - 

#### newInstance

```
public static <T> Capture<T> newInstance​(UnaryOperator<T> transform)
```

Create a new capture instance with a specific transformation
 function to change the values into a different value.

Type Parameters:
`T` - type of the class to be captured
Parameters:
`transform` - the transform function
Returns:
the new capture object

    - 

#### reset

```
public void reset()
```

Will reset capture to a "nothing captured yet" state

    - 

#### hasCaptured

```
public boolean hasCaptured()
```

Returns:
true if something was captured

    - 

#### getValue

```
public T getValue()
```

Return captured value.

Returns:
The last captured value
Throws:
`AssertionError` - if nothing was captured yet or if more than one value was
             captured

    - 

#### getValues

```
public List<T> getValues()
```

Return all captured values. It returns the actual list so you can modify
 its content if needed.

Returns:
The currently captured values

    - 

#### setValue

```
public void setValue​(T value)
```

Used internally by the EasyMock framework to add a new captured value.

Parameters:
`value` - Value captured

    - 

#### toString

```
public String toString()
```

Overrides:
`toString` in class `Object`