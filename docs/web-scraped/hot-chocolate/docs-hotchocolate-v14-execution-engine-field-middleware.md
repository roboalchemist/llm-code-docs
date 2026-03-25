# Source: https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware

Title: Field middleware - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware

Markdown Content:
The field middleware is one of the fundamental components in Hot Chocolate. It allows you to create reuseable logic that can be run before or after a field resolver. Field middleware is composable, so you can specify multiple middleware and they will be executed in order. The field resolver is always the last element in this middleware chain.

Each field middleware only knows about the next element in the chain and can choose to

*   execute logic before it
*   execute logic after all later components (including the field resolver) have been run
*   not execute the next component

Each field middleware also has access to an `IMiddlewareContext`. It implements the `IResolverContext` interface so you can use all of the `IResolverContext` APIs in your middleware, similarly to how you would use them in your resolver. There are also some special properties like the `Result`, which holds the resolver or middleware computed result.

[](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#middleware-order)Middleware order
--------------------------------------------------------------------------------------------------------------------

If you have used Hot Chocolate's data middleware before you might have encountered warnings about the order of middleware. The order is important, since it determines in which order the middleware are executed, e.g. in which order the resolver result is being processed.

Take the `UsePagination` and `UseFiltering` middleware for example: Does it make sense to first paginate and then filter? No. It should first be filtered and then paginated. That's why the correct order is `UsePagination`>`UseFiltering`.

C#

descriptor

.UsePagination()

.UseFiltering()

.Resolve(context =>

{

});

But hold up, isn't this the opposite order of what we've just described?

Lets visualize the middleware chain to understand why it is indeed the correct order.

As you can see the result of the resolver flows backwards through the middleware. So the middleware is first invoked in the order they were defined, but the result produced by the last middleware, the field resolver, is sent back to first middleware in reverse order.

[](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#definition)Definition
--------------------------------------------------------------------------------------------------------

Field middleware can be defined either as a delegate or as a separate type. In both cases we gain access to a `FieldDelegate`, which allows us to invoke the next middleware, and the `IMiddlewareContext`.

By awaiting the `FieldDelegate` we are waiting for the completion of all of the middleware that might come after the current middleware, including the actual field resolver.

[](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#field-middleware-delegate)Field middleware delegate
--------------------------------------------------------------------------------------------------------------------------------------

A field middleware delegate can be defined using code-first APIs.

C#

public class QueryType : ObjectType

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor

.Field("example")

.Use(next => async context =>

{

await next(context);

})

.Resolve(context =>

{

});

}

}

### [](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#reusing-the-middleware-delegate)Reusing the middleware delegate

As it's shown above the middleware is only applied to the `example` field on the `Query` type, but what if you want to use this middleware in multiple places?

You can simply create an extension method for the `IObjectFieldDescriptor`.

C#

public static class MyMiddlewareObjectFieldDescriptorExtension

{

public static IObjectFieldDescriptor UseMyMiddleware(

this IObjectFieldDescriptor descriptor)

{

descriptor

.Use(next => async context =>

{

await next(context);

});

}

}

> Note: We recommend sticking to the convention of prepending `Use` to your extension method to indicate that it is applying a middleware.

You can now use this middleware in different places throughout your schema definition.

C#

public class QueryType : ObjectType

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor

.Field("example")

.UseMyMiddleware()

.Resolve(context =>

{

});

}

}

[](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#field-middleware-as-a-class)Field middleware as a class
------------------------------------------------------------------------------------------------------------------------------------------

If you do not like using a delegate, you can also create a dedicated class for your middleware.

C#

public class MyMiddleware

{

private readonly FieldDelegate _next;

public MyMiddleware(FieldDelegate next)

{

_next = next;

}

public async Task InvokeAsync(IMiddlewareContext context)

{

await _next(context);

}

}

If you need to access services you can either inject them via the constructor, if they are singleton, or as an argument of the `InvokeAsync` method, if they have a scoped or transient lifetime.

C#

public class MyMiddleware

{

private readonly FieldDelegate _next;

private readonly IMySingletonService _singletonService;

public MyMiddleware(FieldDelegate next, IMySingletonService singletonService)

{

_next = next;

_singletonService = singletonService;

}

public async Task InvokeAsync(IMiddlewareContext context,

IMyScopedService scopedService)

{

}

}

The ability to add additional arguments to the `InvokeAsync` method is the reason why there isn't a contract like an interface or a base class for field middleware.

### [](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#usage)Usage

Now that you've defined the middleware as a class we need to still apply it to a field.

C#

public class QueryType : ObjectType

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor

.Field("example")

.Use<MyMiddleware>()

.Resolve(context =>

{

});

}

}

While an extension method like `UseMyMiddleware` on the `IObjectFieldDescriptor` doesn't make as much sense for `Use<MyMiddleware>` in contrast to the middleware delegate, we still recommend creating one as shown [here](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#reusing-the-middleware-delegate). The reason being that you can make changes to this middleware more easily in the future without potentially having to change all places this middleware is being used in.

If you need to pass an additional custom argument to the middleware you can do so using the factory overload of the `Use` method.

C#

descriptor

.Field("example")

.Use((provider, next) => new MyMiddleware(next, "custom",

provider.GetRequiredService<FooBar>()));

[](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#usage-as-an-attribute)Usage as an attribute
------------------------------------------------------------------------------------------------------------------------------

Up until now we have only worked with code-first APIs to create the field middleware. What if you want to apply your middleware to a field resolver defined using the implementation-first approach?

You can create a new attribute inheriting from `ObjectFieldDescriptorAttribute` and call or create your middleware inside of the `OnConfigure` method.

> Note: Attribute order is not guaranteed in C#, so we, in the case of middleware attributes, use the `CallerLineNumberAttribute` to inject the C# line number at compile time. The line number is used as an order. We do not recommend inheriting middleware attributes from a base method or property since this can lead to confusion about ordering. Look at the example below to see how we infer the order. When inheriting from middleware, attributes always pass through the order argument. Further, indicate with the `Use` verb that your attribute is a middleware attribute.

C#

public class UseMyMiddlewareAttribute : ObjectFieldDescriptorAttribute

{

public UseMyMiddlewareAttribute([CallerLineNumber] int order = 0)

{

Order = order;

}

protected override void OnConfigure(IDescriptorContext context,

IObjectFieldDescriptor descriptor, MemberInfo member)

{

descriptor.UseMyMiddleware();

}

}

The attribute can then be used like the following.

C#

public class Query

{

[UseMyMiddleware]

public string MyResolver()

{

}

}

[](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#accessing-the-resolver-result)Accessing the resolver result
----------------------------------------------------------------------------------------------------------------------------------------------

The `IMiddlewareContext` conveniently contains a `Result` property that can be used to access the field resolver result.

C#

descriptor

.Use(next => async context =>

{

await next(context);

object? result = context.Result;

if (result is string stringResult)

{

}

});

A middleware can also set or override the result by assigning the `context.Result` property.

> Note: The field resolver will only execute if no result has been produced by one of the preceding field middleware. If any middleware has set the `Result` property on the `IMiddlewareContext`, the field resolver will be skipped.

[](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware#short-circuiting)Short-circuiting
--------------------------------------------------------------------------------------------------------------------

In some cases we might want to short-circuit the execution of field middleware / the field resolver. For this we can simply not call the `FieldDelegate` (`next`).

C#

descriptor

.Use(next => context =>

{

if(context.Parent<object>() is IDictionary<string, object> dict)

{

context.Result = dict[context.Field.Name];

return Task.CompletedTask;

}

else

{

return next(context);

}

})

Last updated on **2026-02-17** by**Tobias Tengler**
