Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ServiceConfigurationError

java.lang.Object
java.lang.Throwable
java.lang.Error
org.glassfish.tyrus.core.ServiceConfigurationError

All Implemented Interfaces:
`Serializable`

---

public class ServiceConfigurationError
extends Error
Taken from Jersey 2. Error thrown when something goes wrong while looking up service providers.
 In particular, this error will be thrown in the following situations:

- A concrete provider class cannot be found,

- A concrete provider class cannot be instantiated,

- The format of a provider-configuration file is illegal, or

- An IOException occurs while reading a provider-configuration file.

Author:
Mark Reinhold, Marek Potociar
See Also:

- Serialized Form

-

## Constructor Summary

Constructors

Constructor
Description
`ServiceConfigurationError(String msg)`

Constructs a new instance with the specified detail string.

`ServiceConfigurationError(Throwable x)`

Constructs a new instance that wraps the specified throwable.

-

## Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### ServiceConfigurationError

public ServiceConfigurationError(String msg)
Constructs a new instance with the specified detail string.

Parameters:
`msg` - the detail string

-

### ServiceConfigurationError

public ServiceConfigurationError(Throwable x)
Constructs a new instance that wraps the specified throwable.

Parameters:
`x` - the throwable to be wrapped
