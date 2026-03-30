Package jakarta.faces.application

# Class ApplicationFactory

java.lang.Object
jakarta.faces.application.ApplicationFactory

All Implemented Interfaces:
`FacesWrapper<ApplicationFactory>`

---

public abstract class ApplicationFactory
extends Object
implements FacesWrapper<ApplicationFactory>

 **ApplicationFactory** is a factory object that
 creates (if needed) and returns `Application` instances. Implementations of Jakarta Faces must provide
 at least a default implementation of `Application`.

 There must be one `ApplicationFactory` instance per web application that is utilizing Jakarta Faces.
 This instance can be acquired, in a portable manner, by calling:

```

 ApplicationFactory factory = (ApplicationFactory) FactoryFinder.getFactory(FactoryFinder.APPLICATION_FACTORY);
 
```

 Usage: extend this class and push the implementation being wrapped to the constructor and use `getWrapped()` to
 access the instance being wrapped.

-

## Constructor Summary

Constructors

Constructor
Description
`ApplicationFactory()`

Deprecated.
Use the other constructor taking the implementation being wrapped.

`ApplicationFactory(ApplicationFactory wrapped)`

 If this factory has been decorated, the implementation doing the decorating should push the implementation being
 wrapped to this constructor.

-

## Method Summary

Modifier and Type
Method
Description
`abstract Application`
`getApplication()`

 Create (if needed) and return an `Application` instance for this web application.

`ApplicationFactory`
`getWrapped()`

 If this factory has been decorated, the implementation doing the decorating may override this method to provide
 access to the implementation being wrapped.

`abstract void`
`setApplication(Application application)`

 Replace the `Application` instance that will be returned for this web application.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ApplicationFactory

@Deprecated
public ApplicationFactory()
Deprecated.
Use the other constructor taking the implementation being wrapped.

-

### ApplicationFactory

public ApplicationFactory(ApplicationFactory wrapped)

 If this factory has been decorated, the implementation doing the decorating should push the implementation being
 wrapped to this constructor. The `getWrapped()` will then return the implementation being wrapped.

Parameters:
`wrapped` - The implementation being wrapped.

-

## Method Details

-

### getWrapped

public ApplicationFactory getWrapped()

 If this factory has been decorated, the implementation doing the decorating may override this method to provide
 access to the implementation being wrapped.

Specified by:
`getWrapped` in interface `FacesWrapper<ApplicationFactory>`
Returns:
the wrapped instance.
Since:
2.0

-

### getApplication

public abstract Application getApplication()

 Create (if needed) and return an `Application` instance for this web application.

Returns:
the application.

-

### setApplication

public abstract void setApplication(Application application)

 Replace the `Application` instance that will be returned for this web application.

Parameters:
`application` - The replacement `Application` instance
Throws:
`NullPointerException` - if `application` is `null`.
