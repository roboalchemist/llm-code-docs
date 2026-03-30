# Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums

Title: Enums - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums

Markdown Content:
This is documentation for **v14**, which is no longer actively maintained.

For up-to-date documentation, see the

[latest stable version](https://chillicream.com/docs/hotchocolate/v15/defining-a-schema/enums).

An Enum is a special kind of [scalar](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/scalars) that is restricted to a particular set of allowed values. It can be used as both an input and an output type.

SDL

enum UserRole {

GUEST,

DEFAULT,

ADMINISTRATOR

}

type Query {

role: UserRole

usersByRole(role: UserRole): [User]

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums#usage)Usage
------------------------------------------------------------------------------------

Given is the schema from above.

When querying a field returning an enum type, the enum value will be serialized as a string.

**Request**

GraphQL

{

role

}

**Response**

JSON

{

"data": {

"role": "STANDARD"

}

}

When using an enum value as an argument, it is represented as a literal and **not** a string.

**Request**

GraphQL

{

usersByRole(role: ADMINISTRATOR) {

id

}

}

When used as a type for a variable, it is represented as a string in the variables object, since JSON does not offer support for literals.

**Request**

Operation:

GraphQL

query ($role: UserRole) {

usersByRole(role: $role) {

id

}

}

Variables:

JSON

{

"role": "ADMINISTRATOR"

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums#definition)Definition
----------------------------------------------------------------------------------------------

We can define enums like the following.

C#

public enum UserRole

{

Guest,

Standard,

Administrator

}

public class Query

{

public User[] GetUsers(UserRole role)

{

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums#non-enum-values)Non-enum values
--------------------------------------------------------------------------------------------------------

In code-first we can also bind the enum type to any other .NET type, for example a `string`.

C#

public class UserRoleType : EnumType<string>

{

protected override void Configure(IEnumTypeDescriptor<string> descriptor)

{

descriptor.Name("UserRole");

descriptor

.Value("Default")

.Name("STANDARD");

}

}

public class QueryType : ObjectType

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor.Name(OperationTypeNames.Query);

descriptor

.Field("users")

.Argument("role", a => a.Type<UserRoleType>())

.Resolve(context =>

{

var role = context.ArgumentValue<string>("role");

});

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums#binding-behavior)Binding behavior
----------------------------------------------------------------------------------------------------------

In the implementation-first approach all enum values are implicitly included on the schema enum type. The same is true for `T` of `EnumType<T>` when using the code-first approach.

In the code-first approach we can also enable explicit binding, where we have to opt-in enum values we want to include instead of them being implicitly included.

We can configure our preferred binding behavior globally like the following.

C#

builder.Services

.AddGraphQLServer()

.ModifyOptions(options =>

{

options.DefaultBindingBehavior = BindingBehavior.Explicit;

});

Warning

This changes the binding behavior for all types, not only enum types.

We can also override it on a per type basis:

C#

public class UserRoleType : EnumType<UserRole>

{

protected override void Configure(IEnumTypeDescriptor<UserRole> descriptor)

{

descriptor.BindValues(BindingBehavior.Implicit);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums#ignoring-values)Ignoring values
--------------------------------------------------------------------------------------------------------

In the implementation-first approach we can ignore values using the `[GraphQLIgnore]` attribute.

C#

public enum UserRole

{

[GraphQLIgnore]

Guest,

Standard,

Administrator

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums#including-values)Including values
----------------------------------------------------------------------------------------------------------

In the code-first approach we can explicitly include values using the `Value` method on the `IEnumTypeDescriptor`. This is only necessary, if the binding behavior of the enum type is explicit.

C#

public class UserRoleType : EnumType<UserRole>

{

protected override void Configure(IEnumTypeDescriptor<UserRole> descriptor)

{

descriptor.BindValuesExplicitly();

descriptor.Value(UserRole.Guest);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums#naming)Naming
--------------------------------------------------------------------------------------

Unless specified explicitly, Hot Chocolate automatically infers the names of enums and their values. Per default the name of the enum becomes the name of the enum type. When using `EnumType<T>` in code-first, the name of `T` is chosen as the name for the enum type.

Enum values are automatically formatted to the UPPER_SNAKE_CASE according to the GraphQL specification:

*   `Guest` becomes `GUEST`
*   `HeadOfDepartment` becomes `HEAD_OF_DEPARTMENT`

If we need to we can override these inferred names.

The `[GraphQLName]` attribute allows us to specify an explicit name.

C#

[GraphQLName("Role")]

public enum UserRole

{

[GraphQLName("VISITOR")]

Guest,

Standard,

Administrator

}

This would produce the following `Role` schema enum type:

SDL

enum Role {

VISITOR,

STANDARD,

ADMINISTRATOR

}

Last updated on **2026-02-17** by**Tobias Tengler**
