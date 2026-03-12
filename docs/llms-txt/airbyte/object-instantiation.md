# Source: https://docs.airbyte.com/platform/connector-development/config-based/advanced-topics/object-instantiation.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/config-based/advanced-topics/object-instantiation.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/config-based/advanced-topics/object-instantiation.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/config-based/advanced-topics/object-instantiation.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/config-based/advanced-topics/object-instantiation.md

# Object Instantiation

Copy Page

If the component is a literal, then it is returned as is:

```
3
```

will result in

```
3
```

If the component definition is a mapping with a "type" field, the factory will lookup the [CLASS\_TYPES\_REGISTRY](https://github.com/airbytehq/airbyte-python-cdk/blob/main//airbyte_cdk/sources/declarative/parsers/class_types_registry.py) and replace the "type" field by "class\_name" -> CLASS\_TYPES\_REGISTRY\[type] and instantiate the object from the resulting mapping

If the component definition is a mapping with neither a "class\_name" nor a "type" field, the factory will do a best-effort attempt at inferring the component type by looking up the parent object's constructor type hints. If the type hint is an interface present in [DEFAULT\_IMPLEMENTATIONS\_REGISTRY](https://github.com/airbytehq/airbyte-python-cdk/blob/main//airbyte_cdk/sources/declarative/parsers/default_implementation_registry.py), then the factory will create an object of its default implementation.

If the component definition is a list, then the factory will iterate over the elements of the list, instantiate its subcomponents, and return a list of instantiated objects.

If the component has subcomponents, the factory will create the subcomponents before instantiating the top level object

```
{
  "type": TopLevel
  "param":
    {
      "type": "ParamType"
      "k": "v"
    }
}
```

will result in

```
TopLevel(param=ParamType(k="v"))
```

More details on object instantiation can be found [here](https://airbyte-cdk.readthedocs.io/en/latest/api/airbyte_cdk.sources.declarative.parsers.html?highlight=factory#airbyte_cdk.sources.declarative.parsers.factory.DeclarativeComponentFactory).
