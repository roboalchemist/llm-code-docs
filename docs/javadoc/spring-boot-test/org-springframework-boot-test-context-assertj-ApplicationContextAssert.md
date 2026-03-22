# Class ApplicationContextAssert<C extends org.springframework.context.ApplicationContext>

java.lang.Object
org.assertj.core.api.AbstractAssert<ApplicationContextAssert<C>, C>
org.springframework.boot.test.context.assertj.ApplicationContextAssert<C>

Type Parameters:
`C` - the application context type

All Implemented Interfaces:
`org.assertj.core.api.Assert<ApplicationContextAssert<C>, C>, org.assertj.core.api.Descriptable<ApplicationContextAssert<C>>, org.assertj.core.api.ExtensionPoints<ApplicationContextAssert<C>, C>`

---

public class ApplicationContextAssert<C extends org.springframework.context.ApplicationContext>
extends org.assertj.core.api.AbstractAssert<ApplicationContextAssert<C>, C>
AssertJ `assertions` that can be applied to an
`ApplicationContext`.

Since:
2.0.0
See Also:

- `ApplicationContextRunner`

- `AssertableApplicationContext`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`ApplicationContextAssert.Scope`

The scope of an assertion.

- 

## Field Summary

### Fields inherited from class org.assertj.core.api.AbstractAssert

`actual, info, myself, objects, throwUnsupportedExceptionOnEquals`

- 

## Method Summary

Modifier and Type
Method
Description
`ApplicationContextAssert<C>`
`doesNotHaveBean(Class<?> type)`

Verifies that the application context (or ancestors) does not contain any beans of
the given type.

`ApplicationContextAssert<C>`
`doesNotHaveBean(Class<?> type,
 ApplicationContextAssert.Scope scope)`

Verifies that the application context does not contain any beans of the given type.

`ApplicationContextAssert<C>`
`doesNotHaveBean(String name)`

Verifies that the application context does not contain a beans of the given name.

`protected final C`
`getApplicationContext()`
 
`<T> org.assertj.core.api.AbstractObjectAssert<?,T>`
`getBean(Class<T> type)`

Obtain a single bean of the given type from the application context (or ancestors),
the bean becoming the object under test.

`<T> org.assertj.core.api.AbstractObjectAssert<?,T>`
`getBean(Class<T> type,
 ApplicationContextAssert.Scope scope)`

Obtain a single bean of the given type from the application context, the bean
becoming the object under test.

`org.assertj.core.api.AbstractObjectAssert<?,Object>`
`getBean(String name)`

Obtain a single bean of the given name from the application context, the bean
becoming the object under test.

`<T> org.assertj.core.api.AbstractObjectAssert<?,T>`
`getBean(String name,
 Class<T> type)`

Obtain a single bean of the given name and type from the application context, the
bean becoming the object under test.

`<T> org.assertj.core.api.AbstractObjectArrayAssert<?,String>`
`getBeanNames(Class<T> type)`

Obtain the beans names of the given type from the application context, the names
becoming the object array under test.

`<T> org.assertj.core.api.MapAssert<String,T>`
`getBeans(Class<T> type)`

Obtain a map bean names and instances of the given type from the application
context (or ancestors), the map becoming the object under test.

`<T> org.assertj.core.api.MapAssert<String,T>`
`getBeans(Class<T> type,
 ApplicationContextAssert.Scope scope)`

Obtain a map bean names and instances of the given type from the application
context, the map becoming the object under test.

`org.assertj.core.api.AbstractThrowableAssert<?, ? extends Throwable>`
`getFailure()`

Obtain the failure that stopped the application context from running, the failure
becoming the object under test.

`protected final @Nullable Throwable`
`getStartupFailure()`
 
`ApplicationContextAssert<C>`
`hasBean(String name)`

Verifies that the application context contains a bean with the given name.

`ApplicationContextAssert<C>`
`hasFailed()`

Verifies that the application has failed to start.

`ApplicationContextAssert<C>`
`hasNotFailed()`

Verifies that the application has not failed to start.

`ApplicationContextAssert<C>`
`hasSingleBean(Class<?> type)`

Verifies that the application context (or ancestors) contains a single bean with
the given type.

`ApplicationContextAssert<C>`
`hasSingleBean(Class<?> type,
 ApplicationContextAssert.Scope scope)`

Verifies that the application context contains a single bean with the given type.

### Methods inherited from class org.assertj.core.api.AbstractAssert

`actual, areEqual, asInstanceOf, asList, assertionError, asString, describedAs, descriptionText, doesNotHave, doesNotHaveSameClassAs, doesNotHaveSameHashCodeAs, doesNotHaveToString, doesNotHaveToString, doesNotMatch, doesNotMatch, equals, extracting, extracting, failure, failureWithActualExpected, failWithActualExpectedAndMessage, failWithMessage, getWritableAssertionInfo, has, hashCode, hasSameClassAs, hasSameHashCodeAs, hasToString, hasToString, inBinary, inHexadecimal, is, isElementOfCustomAssert, isEqualTo, isExactlyInstanceOf, isIn, isIn, isInstanceOf, isInstanceOfAny, isInstanceOfSatisfying, isNot, isNotEqualTo, isNotExactlyInstanceOf, isNotIn, isNotIn, isNotInstanceOf, isNotInstanceOfAny, isNotNull, isNotOfAnyClassIn, isNotSameAs, isNull, isOfAnyClassIn, isSameAs, matches, matches, newListAssertInstance, overridingErrorMessage, overridingErrorMessage, satisfies, satisfies, satisfies, satisfiesAnyOf, satisfiesAnyOf, satisfiesAnyOfForProxy, satisfiesForProxy, setCustomRepresentation, setDescriptionConsumer, setPrintAssertionsDescription, throwAssertionError, usingComparator, usingComparator, usingDefaultComparator, usingEquals, usingEquals, usingRecursiveAssertion, usingRecursiveAssertion, usingRecursiveComparison, usingRecursiveComparison, withFailMessage, withFailMessage, withRepresentation, withThreadDumpOnError`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.assertj.core.api.Descriptable

`as, as, as, describedAs, describedAs`

- 

## Method Details

  - 

### hasBean

public ApplicationContextAssert<C> hasBean(String name)
Verifies that the application context contains a bean with the given name.

Example: 

```

assertThat(context).hasBean("fooBean"); 
```

Parameters:
`name` - the name of the bean
Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context does not contain a bean with the
given name

  - 

### hasSingleBean

public ApplicationContextAssert<C> hasSingleBean(Class<?> type)
Verifies that the application context (or ancestors) contains a single bean with
the given type.

Example: 

```

assertThat(context).hasSingleBean(Foo.class); 
```

Parameters:
`type` - the bean type
Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context does no beans of the given type
`AssertionError` - if the application context contains multiple beans of the
given type

  - 

### hasSingleBean

public ApplicationContextAssert<C> hasSingleBean(Class<?> type,
 ApplicationContextAssert.Scope scope)
Verifies that the application context contains a single bean with the given type.

Example: 

```

assertThat(context).hasSingleBean(Foo.class, Scope.NO_ANCESTORS); 
```

Parameters:
`type` - the bean type
`scope` - the scope of the assertion
Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context does no beans of the given type
`AssertionError` - if the application context contains multiple beans of the
given type

  - 

### doesNotHaveBean

public ApplicationContextAssert<C> doesNotHaveBean(Class<?> type)
Verifies that the application context (or ancestors) does not contain any beans of
the given type.

Example: 

```

assertThat(context).doesNotHaveBean(Foo.class); 
```

Parameters:
`type` - the bean type
Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context contains any beans of the given
type

  - 

### doesNotHaveBean

public ApplicationContextAssert<C> doesNotHaveBean(Class<?> type,
 ApplicationContextAssert.Scope scope)
Verifies that the application context does not contain any beans of the given type.

Example: 

```

assertThat(context).doesNotHaveBean(Foo.class, Scope.NO_ANCESTORS); 
```

Parameters:
`type` - the bean type
`scope` - the scope of the assertion
Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context contains any beans of the given
type

  - 

### doesNotHaveBean

public ApplicationContextAssert<C> doesNotHaveBean(String name)
Verifies that the application context does not contain a beans of the given name.

Example: 

```

assertThat(context).doesNotHaveBean("fooBean"); 
```

Parameters:
`name` - the name of the bean
Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context contains a beans of the given
name

  - 

### getBeanNames

@CheckReturnValue
public <T>
org.assertj.core.api.AbstractObjectArrayAssert<?,String> getBeanNames(Class<T> type)
Obtain the beans names of the given type from the application context, the names
becoming the object array under test.

Example: 

```

assertThat(context).getBeanNames(Foo.class).containsOnly("fooBean"); 
```

Type Parameters:
`T` - the bean type
Parameters:
`type` - the bean type
Returns:
array assertions for the bean names
Throws:
`AssertionError` - if the application context did not start

  - 

### getBean

@CheckReturnValue
public <T>
org.assertj.core.api.AbstractObjectAssert<?,T> getBean(Class<T> type)
Obtain a single bean of the given type from the application context (or ancestors),
the bean becoming the object under test. If no beans of the specified type can be
found an assert on `null` is returned.

Example: 

```

assertThat(context).getBean(Foo.class).isInstanceOf(DefaultFoo.class);
assertThat(context).getBean(Bar.class).isNull();
```

Type Parameters:
`T` - the bean type
Parameters:
`type` - the bean type
Returns:
bean assertions for the bean, or an assert on `null` if the no bean
is found
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context contains multiple beans of the
given type

  - 

### getBean

@CheckReturnValue
public <T>
org.assertj.core.api.AbstractObjectAssert<?,T> getBean(Class<T> type,
 ApplicationContextAssert.Scope scope)
Obtain a single bean of the given type from the application context, the bean
becoming the object under test. If no beans of the specified type can be found an
assert on `null` is returned.

Example: 

```

assertThat(context).getBean(Foo.class, Scope.NO_ANCESTORS).isInstanceOf(DefaultFoo.class);
assertThat(context).getBean(Bar.class, Scope.NO_ANCESTORS).isNull();
```

Type Parameters:
`T` - the bean type
Parameters:
`type` - the bean type
`scope` - the scope of the assertion
Returns:
bean assertions for the bean, or an assert on `null` if the no bean
is found
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context contains multiple beans of the
given type

  - 

### getBean

@CheckReturnValue
public org.assertj.core.api.AbstractObjectAssert<?,Object> getBean(String name)
Obtain a single bean of the given name from the application context, the bean
becoming the object under test. If no bean of the specified name can be found an
assert on `null` is returned.

Example: 

```

assertThat(context).getBean("foo").isInstanceOf(Foo.class);
assertThat(context).getBean("foo").isNull();
```

Parameters:
`name` - the name of the bean
Returns:
bean assertions for the bean, or an assert on `null` if the no bean
is found
Throws:
`AssertionError` - if the application context did not start

  - 

### getBean

@CheckReturnValue
public <T>
org.assertj.core.api.AbstractObjectAssert<?,T> getBean(String name,
 Class<T> type)
Obtain a single bean of the given name and type from the application context, the
bean becoming the object under test. If no bean of the specified name can be found
an assert on `null` is returned.

Example: 

```

assertThat(context).getBean("foo", Foo.class).isInstanceOf(DefaultFoo.class);
assertThat(context).getBean("foo", Foo.class).isNull();
```

Type Parameters:
`T` - the bean type
Parameters:
`name` - the name of the bean
`type` - the bean type
Returns:
bean assertions for the bean, or an assert on `null` if the no bean
is found
Throws:
`AssertionError` - if the application context did not start
`AssertionError` - if the application context contains a bean with the given
name but a different type

  - 

### getBeans

@CheckReturnValue
public <T> org.assertj.core.api.MapAssert<String,T> getBeans(Class<T> type)
Obtain a map bean names and instances of the given type from the application
context (or ancestors), the map becoming the object under test. If no bean of the
specified type can be found an assert on an empty `map` is returned.

Example: 

```

assertThat(context).getBeans(Foo.class).containsKey("foo");

```

Type Parameters:
`T` - the bean type
Parameters:
`type` - the bean type
Returns:
bean assertions for the beans, or an assert on an empty `map` if the
no beans are found
Throws:
`AssertionError` - if the application context did not start

  - 

### getBeans

@CheckReturnValue
public <T> org.assertj.core.api.MapAssert<String,T> getBeans(Class<T> type,
 ApplicationContextAssert.Scope scope)
Obtain a map bean names and instances of the given type from the application
context, the map becoming the object under test. If no bean of the specified type
can be found an assert on an empty `map` is returned.

Example: 

```

assertThat(context).getBeans(Foo.class, Scope.NO_ANCESTORS).containsKey("foo");

```

Type Parameters:
`T` - the bean type
Parameters:
`type` - the bean type
`scope` - the scope of the assertion
Returns:
bean assertions for the beans, or an assert on an empty `map` if the
no beans are found
Throws:
`AssertionError` - if the application context did not start

  - 

### getFailure

@CheckReturnValue
public org.assertj.core.api.AbstractThrowableAssert<?, ? extends Throwable> getFailure()
Obtain the failure that stopped the application context from running, the failure
becoming the object under test.

Example: 

```

assertThat(context).getFailure().hasMessageContaining("missing bean");

```

Returns:
assertions on the cause of the failure
Throws:
`AssertionError` - if the application context started without a failure

  - 

### hasFailed

public ApplicationContextAssert<C> hasFailed()
Verifies that the application has failed to start.

Example: 

```
 assertThat(context).hasFailed();

```

Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context started without a failure

  - 

### hasNotFailed

public ApplicationContextAssert<C> hasNotFailed()
Verifies that the application has not failed to start.

Example: 

```
 assertThat(context).hasNotFailed();

```

Returns:
`this` assertion object.
Throws:
`AssertionError` - if the application context failed to start

  - 

### getApplicationContext

protected final C getApplicationContext()

  - 

### getStartupFailure

protected final @Nullable Throwable getStartupFailure()