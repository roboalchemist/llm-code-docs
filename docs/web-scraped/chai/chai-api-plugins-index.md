# Source: https://devdocs.io/chai/api/plugins/index

Title: Plugin Utilities — DevDocs

URL Source: https://devdocs.io/chai/api/plugins/index

Markdown Content:
The plugin utilities are for those who want to extend Chai with their own set of assertions. The [Code Plugin Concepts](https://devdocs.io/chai/guide/plugins/index) and [Building a Helper](https://devdocs.io/chai/guide/helpers/index) guide tutorials are a great reference on how to get started with your own assertions.

API Reference
-------------

### .addChainableMethod(ctx, name, method, chainingBehavior)

Adds a method to an object, such that the method can also be chained.

utils.addChainableMethod(chai.Assertion.prototype, 'foo', function (str) {
  var obj = utils.flag(this, 'object');
  new chai.Assertion(obj).to.be.equal(str);
});

Can also be accessed directly from `chai.Assertion`.

chai.Assertion.addChainableMethod('foo', fn, chainingBehavior);

The result can then be used as both a method assertion, executing both `method` and `chainingBehavior`, or as a language chain, which only executes `chainingBehavior`.

expect(fooStr).to.be.foo('bar');
expect(fooStr).to.be.foo.equal('foo');

### .addLengthGuard(fn, assertionName, isChainable)

Define `length` as a getter on the given uninvoked method assertion. The getter acts as a guard against chaining `length` directly off of an uninvoked method assertion, which is a problem because it references `function`’s built-in `length` property instead of Chai’s `length` assertion. When the getter catches the user making this mistake, it throws an error with a helpful message.

There are two ways in which this mistake can be made. The first way is by chaining the `length` assertion directly off of an uninvoked chainable method. In this case, Chai suggests that the user use `lengthOf` instead. The second way is by chaining the `length` assertion directly off of an uninvoked non-chainable method. Non-chainable methods must be invoked prior to chaining. In this case, Chai suggests that the user consult the docs for the given assertion.

If the `length` property of functions is unconfigurable, then return `fn` without modification.

Note that in ES6, the function’s `length` property is configurable, so once support for legacy environments is dropped, Chai’s `length` property can replace the built-in function’s `length` property, and this length guard will no longer be necessary. In the mean time, maintaining consistency across all environments is the priority.

### .addMethod(ctx, name, method)

Adds a method to the prototype of an object.

utils.addMethod(chai.Assertion.prototype, 'foo', function (str) {
  var obj = utils.flag(this, 'object');
  new chai.Assertion(obj).to.be.equal(str);
});

Can also be accessed directly from `chai.Assertion`.

chai.Assertion.addMethod('foo', fn);

Then can be used as any other assertion.

expect(fooStr).to.be.foo('bar');

### .addProperty(ctx, name, getter)

Adds a property to the prototype of an object.

utils.addProperty(chai.Assertion.prototype, 'foo', function () {
  var obj = utils.flag(this, 'object');
  new chai.Assertion(obj).to.be.instanceof(Foo);
});

Can also be accessed directly from `chai.Assertion`.

chai.Assertion.addProperty('foo', fn);

Then can be used as any other assertion.

expect(myFoo).to.be.foo;

### .compareByInspect(mixed, mixed)

To be used as a compareFunction with Array.prototype.sort. Compares elements using inspect instead of default behavior of using toString so that Symbols and objects with irregular/missing toString can still be sorted without a TypeError.

### .expectTypes(obj, types)

Ensures that the object being tested against is of a valid type.

utils.expectTypes(this, ['array', 'object', 'string']);

### .flag(object, key, [value])

Get or set a flag value on an object. If a value is provided it will be set, else it will return the currently set value or `undefined` if the value is not set.

utils.flag(this, 'foo', 'bar'); 
utils.flag(this, 'foo'); 

### .getActual(object, [actual])

Returns the `actual` value for an Assertion.

### .getEnumerableProperties(object)

This allows the retrieval of enumerable property names of an object, inherited or not.

### .getMessage(object, message, negateMessage)

Construct the error message based on flags and template tags. Template tags will return a stringified inspection of the object referenced.

Message template tags:

*   `#{this}` current asserted object
*   `#{act}` actual value
*   `#{exp}` expected value

### .getOperator(message)

Extract the operator from error message. Operator defined is based on below link https://nodejs.org/api/assert.html#assert_assert.

Returns the `operator` or `undefined` value for an Assertion.

### .getOwnEnumerableProperties(object)

This allows the retrieval of directly-owned enumerable property names and symbols of an object. This function is necessary because Object.keys only returns enumerable property names, not enumerable property symbols.

### .getOwnEnumerablePropertySymbols(object)

This allows the retrieval of directly-owned enumerable property symbols of an object. This function is necessary because Object.getOwnPropertySymbols returns both enumerable and non-enumerable property symbols.

### .getProperties(object)

This allows the retrieval of property names of an object, enumerable or not, inherited or not.

### .inspect(obj, [showHidden], [depth], [colors])

Echoes the value of a value. Tries to print the value out in the best way possible given the different types.

### .isProxyEnabled()

Helper function to check if Chai’s proxy protection feature is enabled. If proxies are unsupported or disabled via the user’s Chai config, then return false. Otherwise, return true.

### .objDisplay(object)

Determines if an object or an array matches criteria to be inspected in-line for error messages or should be truncated.

### .overwriteChainableMethod(ctx, name, method, chainingBehavior)

Overwrites an already existing chainable method and provides access to the previous function or property. Must return functions to be used for name.

utils.overwriteChainableMethod(chai.Assertion.prototype, 'lengthOf',
  function (_super) {
  }
, function (_super) {
  }
);

Can also be accessed directly from `chai.Assertion`.

chai.Assertion.overwriteChainableMethod('foo', fn, fn);

Then can be used as any other assertion.

expect(myFoo).to.have.lengthOf(3);
expect(myFoo).to.have.lengthOf.above(3);

### .overwriteMethod(ctx, name, fn)

Overwrites an already existing method and provides access to previous function. Must return function to be used for name.

utils.overwriteMethod(chai.Assertion.prototype, 'equal', function (_super) {
  return function (str) {
    var obj = utils.flag(this, 'object');
    if (obj instanceof Foo) {
      new chai.Assertion(obj.value).to.equal(str);
    } else {
      _super.apply(this, arguments);
    }
  }
});

Can also be accessed directly from `chai.Assertion`.

chai.Assertion.overwriteMethod('foo', fn);

Then can be used as any other assertion.

expect(myFoo).to.equal('bar');

### .overwriteProperty(ctx, name, fn)

Overwrites an already existing property getter and provides access to previous value. Must return function to use as getter.

utils.overwriteProperty(chai.Assertion.prototype, 'ok', function (_super) {
  return function () {
    var obj = utils.flag(this, 'object');
    if (obj instanceof Foo) {
      new chai.Assertion(obj.name).to.equal('bar');
    } else {
      _super.call(this);
    }
  }
});

Can also be accessed directly from `chai.Assertion`.

chai.Assertion.overwriteProperty('foo', fn);

Then can be used as any other assertion.

expect(myFoo).to.be.ok;

### .proxify(object)

Return a proxy of given object that throws an error when a non-existent property is read. By default, the root cause is assumed to be a misspelled property, and thus an attempt is made to offer a reasonable suggestion from the list of existing properties. However, if a nonChainableMethodName is provided, then the root cause is instead a failure to invoke a non-chainable method prior to reading the non-existent property.

If proxies are unsupported or disabled via the user’s Chai config, then return object without modification.

### .test(object, expression)

Test and object for expression.

### .transferFlags(assertion, object, includeAll = true)

Transfer all the flags for `assertion` to `object`. If `includeAll` is set to `false`, then the base Chai assertion flags (namely `object`, `ssfi`, `lockSsfi`, and `message`) will not be transferred.

var newAssertion = new Assertion();
utils.transferFlags(assertion, newAssertion);

var anotherAssertion = new Assertion(myObj);
utils.transferFlags(assertion, anotherAssertion, false);

### .compatibleInstance(thrown, errorLike)

Checks if two instances are compatible (strict equal). Returns false if errorLike is not an instance of Error, because instances can only be compatible if they’re both error instances.

### .compatibleConstructor(thrown, errorLike)

Checks if two constructors are compatible. This function can receive either an error constructor or an error instance as the `errorLike` argument. Constructors are compatible if they’re the same or if one is an instance of another.

### .compatibleMessage(thrown, errMatcher)

Checks if an error’s message is compatible with a matcher (String or RegExp). If the message contains the String or passes the RegExp test, it is considered compatible.

### .getFunctionName(constructorFn)

Returns the name of a function. This also includes a polyfill function if `constructorFn.name` is not defined.

### .getConstructorName(errorLike)

Gets the constructor name for an Error instance or constructor itself.

### .getMessage(errorLike)

Gets the error message from an error. If `err` is a String itself, we return it. If the error has no message, we return an empty string.

### .getFuncName(constructorFn)

Returns the name of a function. When a non-function instance is passed, returns `null`. This also includes a polyfill function if `aFunc.name` is not defined.

### .hasProperty(object, name)

This allows checking whether an object has own or inherited from prototype chain named property.

Basically does the same thing as the `in` operator but works properly with null/undefined values and other primitives.

var obj = {
    arr: ['a', 'b', 'c']
  , str: 'Hello'
}

The following would be the results.

hasProperty(obj, 'str');  
hasProperty(obj, 'constructor');  
hasProperty(obj, 'bar');  

hasProperty(obj.str, 'length'); 
hasProperty(obj.str, 1);  
hasProperty(obj.str, 5);  

hasProperty(obj.arr, 'length');  
hasProperty(obj.arr, 2);  
hasProperty(obj.arr, 3);  

### .getPathInfo(object, path)

This allows the retrieval of property info in an object given a string path.

The path info consists of an object with the following properties:

*   parent - The parent object of the property referenced by `path`
*   name - The name of the final property, a number if it was an array indexer
*   value - The value of the property, if it exists, otherwise `undefined`
*   exists - Whether the property exists or not

### .getPathValue(object, path)

This allows the retrieval of values in an object given a string path.

var obj = {
    prop1: {
        arr: ['a', 'b', 'c']
      , str: 'Hello'
    }
  , prop2: {
        arr: [ { nested: 'Universe' } ]
      , str: 'Hello again!'
    }
}

The following would be the results.

getPathValue(obj, 'prop1.str'); 
getPathValue(obj, 'prop1.att[2]'); 
getPathValue(obj, 'prop2.arr[0].nested');
