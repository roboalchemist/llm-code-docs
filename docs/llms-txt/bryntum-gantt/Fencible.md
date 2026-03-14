# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Fencible.md

# [Fencible](https://bryntum.com/docs/gantt/api/Core/mixin/Fencible)

This mixin is used to apply reentrancy barriers to instance methods. For details, see [fenced](https://bryntum.com/docs/gantt/api/#Core/mixin/Fencible#property-fenced-static).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFencible](https://bryntum.com/docs/gantt/api/Core/mixin/Fencible#property-isFencible)
Identifies an object as an instance of [Fencible](https://bryntum.com/docs/gantt/api/#Core/mixin/Fencible) class, or subclass thereof.

[isFencible](https://bryntum.com/docs/gantt/api/Core/mixin/Fencible#property-isFencible-static)
Identifies an object as an instance of [Fencible](https://bryntum.com/docs/gantt/api/#Core/mixin/Fencible) class, or subclass thereof.

[fenced](https://bryntum.com/docs/gantt/api/Core/mixin/Fencible#property-fenced-static)
This class property returns an object that specifies the instance methods which need reentrancy protection.

It is used like so:

```
 class Foo extends Base.mixin(Fencible) {
     static fenced = {
         reentrantMethod : true
     };

     reentrantMethod() {
         // things() may cause reentrantMethod() to be called...
         // but we won't be allowed to reenter this method since we are already inside it
         this.things();
     }
 }
```

This can also be used to protect mutually reentrant method groups:

```
 class Foo extends Base.mixin(Fencible) {
     static fenced = {
         foo : 'foobar'
         bar : 'foobar'
     };

     foo() {
         console.log('foo');
         this.bar();
     }

     bar() {
         console.log('bar');
         this.foo();
     }
 }

 instance = new Foo();
 instance.foo();
 >> foo
 instance.bar();
 >> bar
```

The value for a fenced method value can be `true`, a string, an array of strings, or a [MethodFence](https://bryntum.com/docs/gantt/api/#Core/mixin/Fencible#typedef-MethodFence) options object.

Internally these methods are protected by defining a wrapper function on the instance. The class methods remain on the class prototype and are guarded by the instance-level method. This allows these methods to use `super` calls, just like other methods.

## Typedefs

Typedefs are type definitions for the class

[MethodFence](https://bryntum.com/docs/gantt/api/Core/mixin/Fencible#typedef-MethodFence)
A description of how to protect a method from reentry.

A value of `true` is transformed using the key as the `all` value. For example, this:

```
 class Foo extends Base.mixin(Fencible) {
     static fenced = {
         foo : true
     };
```

Is equivalent to this:

```
 class Foo extends Base.mixin(Fencible) {
     static fenced = {
         foo : {
             all : ['foo']
         }
     };
```

Strings are split on spaces to produce the `all` array. For example, this:

```
 class Foo extends Base.mixin(Fencible) {
     static fenced = {
         foo : 'foo bar'
     };
```

Is equivalent to this:

```
 class Foo extends Base.mixin(Fencible) {
     static fenced = {
         foo : {
             all : ['foo', 'bar']
         }
     };
```

This indicates that `foo()` cannot be reentered if `foo()` or `bar()` are already executing. On entry to `foo()`, both `foo()` and `bar()` will be fenced (prevented from entering).
