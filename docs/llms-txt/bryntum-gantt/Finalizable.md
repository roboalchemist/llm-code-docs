# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Finalizable.md

# [Finalizable](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable)

This mixin provides an asynchronous completion mechanism. This allows a process to coordinate its async actions (such as Ajax requests or user interaction) with cleanup.

Consider a context tracking helper class, for example:

```
 class Context extends Base.mixin(Finalizable) {
     // ...

     async finish() {
         this.owner.trigger('finish', {
             context : this
         });

         // Wait for any scheduled finalizer to run...
         await this.finalize();
     }

     doFinalize() {
         this.destroy();
     }
 }
```

When the `finish` event is processed, the receiver can register a promise for whatever processing it would like to perform:

```
 class Foo {
     onFinish({ context }) {
         context.finalizer = this.askUser(context);
     }

     async askUser(context) {
         //
     }
 }
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFinalizable](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#property-isFinalizable)
Identifies an object as an instance of [Finalizable](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable) class, or subclass thereof.

[isFinalizable](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#property-isFinalizable-static)
Identifies an object as an instance of [Finalizable](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable) class, or subclass thereof.

[finalizer](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#property-finalizer)
This property can be set any time prior to calling [finalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-finalize) (i.e., when the [isFinalizing](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#property-isFinalizing) property goes to `true`). When set, this instance will `await` this promise before completing the finalization process by calling [doFinalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-doFinalize).

[finalizing](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#property-finalizing)
This property holds the `Promise` that will resolve when [finalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-finalize) has completed. It is set when [finalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-finalize) is called and cleared on return.

[isFinalized](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#property-isFinalized)
This property is `true` once the instance completes the [finalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-finalize) method.

[isFinalizing](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#property-isFinalizing)
This property is set to `true` when [finalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-finalize) is called.

## Functions

Functions are methods available for calling on the class

[doFinalize](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#function-doFinalize)
This template method is called at the end of [finalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-finalize). By default it calls `destroy()`, but can be replaced by the derived class. This can be useful if it is not the `Finalizable` instance that awaits the [finalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-finalize) method.

[finalize](https://bryntum.com/docs/gantt/api/Core/mixin/Finalizable#function-finalize)
This method is called (typically by this instance or its owner) to cleanup this instance while possibly first waiting for the [finalizer](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#property-finalizer) promise to settle. Once settled, the [doFinalize](https://bryntum.com/docs/gantt/api/#Core/mixin/Finalizable#function-doFinalize) method is called.
