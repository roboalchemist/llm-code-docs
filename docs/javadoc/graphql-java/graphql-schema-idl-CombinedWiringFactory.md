JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.schema.idl

## Class CombinedWiringFactory

- java.lang.Object

- 

  - graphql.schema.idl.CombinedWiringFactory

- 

All Implemented Interfaces:
WiringFactory

---

```
@PublicApi
public class CombinedWiringFactory
extends java.lang.Object
implements WiringFactory
```

This combines a number of `WiringFactory`s together to act as one.  It asks each one
 whether it handles a type and delegates to the first one to answer yes.

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CombinedWiringFactory(java.util.List<WiringFactory> factories)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`DataFetcher`
`getDataFetcher(FieldWiringEnvironment environment)`
Returns a `DataFetcher` given the type definition

`<T> DataFetcherFactory<T>`
`getDataFetcherFactory(FieldWiringEnvironment environment)`
Returns a `DataFetcherFactory` given the type definition

`DataFetcher`
`getDefaultDataFetcher(FieldWiringEnvironment environment)`
All fields need a data fetcher of some sort and this method is called to provide the data fetcher
 that will be used if no specific one has been provided

`GraphQLScalarType`
`getScalar(ScalarWiringEnvironment environment)`
Returns a `GraphQLScalarType` given scalar defined in IDL

`SchemaDirectiveWiring`
`getSchemaDirectiveWiring(SchemaDirectiveWiringEnvironment environment)`
Returns a `SchemaDirectiveWiring` given the environment

`TypeResolver`
`getTypeResolver(InterfaceWiringEnvironment environment)`
Returns a `TypeResolver` given the type interface

`TypeResolver`
`getTypeResolver(UnionWiringEnvironment environment)`
Returns a `TypeResolver` given the type union

`boolean`
`providesDataFetcher(FieldWiringEnvironment environment)`
This is called to ask if this factory can provide a data fetcher for the definition

`boolean`
`providesDataFetcherFactory(FieldWiringEnvironment environment)`
This is called to ask if this factory can provide a `DataFetcherFactory` for the definition

`boolean`
`providesScalar(ScalarWiringEnvironment environment)`
This is called to ask if this factory can provide a custom scalar

`boolean`
`providesSchemaDirectiveWiring(SchemaDirectiveWiringEnvironment environment)`
This is called to ask if this factory can provide a schema directive wiring.

`boolean`
`providesTypeResolver(InterfaceWiringEnvironment environment)`
This is called to ask if this factory can provide a type resolver for the interface

`boolean`
`providesTypeResolver(UnionWiringEnvironment environment)`
This is called to ask if this factory can provide a type resolver for the union

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### CombinedWiringFactory

```
public CombinedWiringFactory(java.util.List<WiringFactory> factories)
```

  - 

### Method Detail

    - 

#### providesTypeResolver

```
public boolean providesTypeResolver(InterfaceWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
This is called to ask if this factory can provide a type resolver for the interface

Specified by:
`providesTypeResolver` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
true if the factory can give out a type resolver

    - 

#### getTypeResolver

```
public TypeResolver getTypeResolver(InterfaceWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
Returns a `TypeResolver` given the type interface

Specified by:
`getTypeResolver` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
a `TypeResolver`

    - 

#### providesTypeResolver

```
public boolean providesTypeResolver(UnionWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
This is called to ask if this factory can provide a type resolver for the union

Specified by:
`providesTypeResolver` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
true if the factory can give out a type resolver

    - 

#### getTypeResolver

```
public TypeResolver getTypeResolver(UnionWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
Returns a `TypeResolver` given the type union

Specified by:
`getTypeResolver` in interface `WiringFactory`
Parameters:
`environment` - the union wiring environment
Returns:
a `TypeResolver`

    - 

#### providesDataFetcherFactory

```
public boolean providesDataFetcherFactory(FieldWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
This is called to ask if this factory can provide a `DataFetcherFactory` for the definition

Specified by:
`providesDataFetcherFactory` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
true if the factory can give out a data fetcher factory

    - 

#### getDataFetcherFactory

```
public <T> DataFetcherFactory<T> getDataFetcherFactory(FieldWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
Returns a `DataFetcherFactory` given the type definition

Specified by:
`getDataFetcherFactory` in interface `WiringFactory`
Type Parameters:
`T` - the type of the data fetcher
Parameters:
`environment` - the wiring environment
Returns:
a `DataFetcherFactory`

    - 

#### providesDataFetcher

```
public boolean providesDataFetcher(FieldWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
This is called to ask if this factory can provide a data fetcher for the definition

Specified by:
`providesDataFetcher` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
true if the factory can give out a data fetcher

    - 

#### getDataFetcher

```
public DataFetcher getDataFetcher(FieldWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
Returns a `DataFetcher` given the type definition

Specified by:
`getDataFetcher` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
a `DataFetcher`

    - 

#### providesScalar

```
public boolean providesScalar(ScalarWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
This is called to ask if this factory can provide a custom scalar

Specified by:
`providesScalar` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
true if the factory can give out a type resolver

    - 

#### getScalar

```
public GraphQLScalarType getScalar(ScalarWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
Returns a `GraphQLScalarType` given scalar defined in IDL

Specified by:
`getScalar` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
a `GraphQLScalarType`

    - 

#### providesSchemaDirectiveWiring

```
public boolean providesSchemaDirectiveWiring(SchemaDirectiveWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
This is called to ask if this factory can provide a schema directive wiring.
 

 `SchemaDirectiveWiringEnvironment.getDirectives()` contains all the directives
 available which may in fact be an empty list.

Specified by:
`providesSchemaDirectiveWiring` in interface `WiringFactory`
Parameters:
`environment` - the calling environment
Returns:
true if the factory can give out a schema directive wiring.

    - 

#### getSchemaDirectiveWiring

```
public SchemaDirectiveWiring getSchemaDirectiveWiring(SchemaDirectiveWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
Returns a `SchemaDirectiveWiring` given the environment

Specified by:
`getSchemaDirectiveWiring` in interface `WiringFactory`
Parameters:
`environment` - the calling environment
Returns:
a `SchemaDirectiveWiring`

    - 

#### getDefaultDataFetcher

```
public DataFetcher getDefaultDataFetcher(FieldWiringEnvironment environment)
```

Description copied from interface: `WiringFactory`
All fields need a data fetcher of some sort and this method is called to provide the data fetcher
 that will be used if no specific one has been provided

Specified by:
`getDefaultDataFetcher` in interface `WiringFactory`
Parameters:
`environment` - the wiring environment
Returns:
a `DataFetcher`

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method