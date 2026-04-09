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

graphql.validation.rules

## Class ArgumentsOfCorrectType

- java.lang.Object

- 

  - graphql.validation.AbstractRule

  - 

    - graphql.validation.rules.ArgumentsOfCorrectType

- 

---

```
public class ArgumentsOfCorrectType
extends AbstractRule
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ArgumentsOfCorrectType(ValidationContext validationContext,
                      ValidationErrorCollector validationErrorCollector)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`checkArgument(Argument argument)` 

    - 

### Methods inherited from class graphql.validation.AbstractRule

`addError, addError, addError, checkDirective, checkDocument, checkField, checkFragmentDefinition, checkFragmentSpread, checkInlineFragment, checkOperationDefinition, checkSelectionSet, checkTypeName, checkVariable, checkVariableDefinition, documentFinished, getErrors, getQueryPath, getValidationContext, getValidationErrorCollector, getValidationUtil, isVisitFragmentSpreads, leaveOperationDefinition, leaveSelectionSet, setVisitFragmentSpreads, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ArgumentsOfCorrectType

```
public ArgumentsOfCorrectType(ValidationContext validationContext,
                              ValidationErrorCollector validationErrorCollector)
```

  - 

### Method Detail

    - 

#### checkArgument

```
public void checkArgument(Argument argument)
```

Overrides:
`checkArgument` in class `AbstractRule`

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