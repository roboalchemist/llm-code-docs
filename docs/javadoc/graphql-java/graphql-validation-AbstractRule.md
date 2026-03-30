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

graphql.validation

## Class AbstractRule

- java.lang.Object

- 

  - graphql.validation.AbstractRule

- 

Direct Known Subclasses:
ArgumentsOfCorrectType, ExecutableDefinitions, FieldsOnCorrectType, FragmentsOnCompositeType, KnownArgumentNames, KnownDirectives, KnownFragmentNames, KnownTypeNames, LoneAnonymousOperation, NoFragmentCycles, NoUndefinedVariables, NoUnusedFragments, NoUnusedVariables, OverlappingFieldsCanBeMerged, PossibleFragmentSpreads, ProvidedNonNullArguments, ScalarLeafs, UniqueArgumentNamesRule, UniqueDirectiveNamesPerLocation, UniqueFragmentNames, UniqueOperationNames, UniqueVariableNamesRule, VariableDefaultValuesOfCorrectType, VariablesAreInputTypes, VariableTypesMatchRule

---

```
public class AbstractRule
extends java.lang.Object
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AbstractRule(ValidationContext validationContext,
            ValidationErrorCollector validationErrorCollector)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`addError(ValidationError.Builder validationError)` 

`void`
`addError(ValidationErrorType validationErrorType,
        java.util.List<? extends Node<?>> locations,
        java.lang.String description)` 

`void`
`addError(ValidationErrorType validationErrorType,
        SourceLocation location,
        java.lang.String description)` 

`void`
`checkArgument(Argument argument)` 

`void`
`checkDirective(Directive directive,
              java.util.List<Node> ancestors)` 

`void`
`checkDocument(Document document)` 

`void`
`checkField(Field field)` 

`void`
`checkFragmentDefinition(FragmentDefinition fragmentDefinition)` 

`void`
`checkFragmentSpread(FragmentSpread fragmentSpread)` 

`void`
`checkInlineFragment(InlineFragment inlineFragment)` 

`void`
`checkOperationDefinition(OperationDefinition operationDefinition)` 

`void`
`checkSelectionSet(SelectionSet selectionSet)` 

`void`
`checkTypeName(TypeName typeName)` 

`void`
`checkVariable(VariableReference variableReference)` 

`void`
`checkVariableDefinition(VariableDefinition variableDefinition)` 

`void`
`documentFinished(Document document)` 

`java.util.List<ValidationError>`
`getErrors()` 

`protected java.util.List<java.lang.String>`
`getQueryPath()` 

`ValidationContext`
`getValidationContext()` 

`ValidationErrorCollector`
`getValidationErrorCollector()` 

`ValidationUtil`
`getValidationUtil()` 

`boolean`
`isVisitFragmentSpreads()` 

`void`
`leaveOperationDefinition(OperationDefinition operationDefinition)` 

`void`
`leaveSelectionSet(SelectionSet selectionSet)` 

`void`
`setVisitFragmentSpreads(boolean visitFragmentSpreads)` 

`java.lang.String`
`toString()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AbstractRule

```
public AbstractRule(ValidationContext validationContext,
                    ValidationErrorCollector validationErrorCollector)
```

  - 

### Method Detail

    - 

#### isVisitFragmentSpreads

```
public boolean isVisitFragmentSpreads()
```

    - 

#### setVisitFragmentSpreads

```
public void setVisitFragmentSpreads(boolean visitFragmentSpreads)
```

    - 

#### getValidationUtil

```
public ValidationUtil getValidationUtil()
```

    - 

#### addError

```
public void addError(ValidationErrorType validationErrorType,
                     java.util.List<? extends Node<?>> locations,
                     java.lang.String description)
```

    - 

#### addError

```
public void addError(ValidationErrorType validationErrorType,
                     SourceLocation location,
                     java.lang.String description)
```

    - 

#### addError

```
public void addError(ValidationError.Builder validationError)
```

    - 

#### getErrors

```
public java.util.List<ValidationError> getErrors()
```

    - 

#### getValidationContext

```
public ValidationContext getValidationContext()
```

    - 

#### getValidationErrorCollector

```
public ValidationErrorCollector getValidationErrorCollector()
```

    - 

#### getQueryPath

```
protected java.util.List<java.lang.String> getQueryPath()
```

    - 

#### checkDocument

```
public void checkDocument(Document document)
```

    - 

#### checkArgument

```
public void checkArgument(Argument argument)
```

    - 

#### checkTypeName

```
public void checkTypeName(TypeName typeName)
```

    - 

#### checkVariableDefinition

```
public void checkVariableDefinition(VariableDefinition variableDefinition)
```

    - 

#### checkField

```
public void checkField(Field field)
```

    - 

#### checkInlineFragment

```
public void checkInlineFragment(InlineFragment inlineFragment)
```

    - 

#### checkDirective

```
public void checkDirective(Directive directive,
                           java.util.List<Node> ancestors)
```

    - 

#### checkFragmentSpread

```
public void checkFragmentSpread(FragmentSpread fragmentSpread)
```

    - 

#### checkFragmentDefinition

```
public void checkFragmentDefinition(FragmentDefinition fragmentDefinition)
```

    - 

#### checkOperationDefinition

```
public void checkOperationDefinition(OperationDefinition operationDefinition)
```

    - 

#### leaveOperationDefinition

```
public void leaveOperationDefinition(OperationDefinition operationDefinition)
```

    - 

#### checkSelectionSet

```
public void checkSelectionSet(SelectionSet selectionSet)
```

    - 

#### leaveSelectionSet

```
public void leaveSelectionSet(SelectionSet selectionSet)
```

    - 

#### checkVariable

```
public void checkVariable(VariableReference variableReference)
```

    - 

#### documentFinished

```
public void documentFinished(Document document)
```

    - 

#### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`

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