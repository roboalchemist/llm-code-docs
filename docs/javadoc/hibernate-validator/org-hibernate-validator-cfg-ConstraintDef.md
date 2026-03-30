# Class ConstraintDef<C extends ConstraintDef<C,A>, A extends Annotation>

java.lang.Object
org.hibernate.validator.cfg.AnnotationDef<C,A>
org.hibernate.validator.cfg.ConstraintDef<C,A>

Type Parameters:
`C` - The type of a concrete sub type. Following to the
"self referencing generic type" pattern each sub type has to be
parametrized with itself.
`A` - The constraint annotation type represented by a concrete sub type.

Direct Known Subclasses:
`AssertFalseDef, AssertTrueDef, BitcoinAddressDef, CNPJDef, CodePointLengthDef, CPFDef, CreditCardNumberDef, CurrencyDef, DecimalMaxDef, DecimalMinDef, DigitsDef, DurationMaxDef, DurationMinDef, EANDef, EmailDef, FutureDef, FutureOrPresentDef, GenericConstraintDef, INNDef, IpAddressDef, ISBNDef, KorRRNDef, LengthDef, LuhnCheckDef, MaxDef, MinDef, Mod10CheckDef, Mod11CheckDef, NegativeDef, NegativeOrZeroDef, NIPDef, NormalizedDef, NotBlankDef, NotEmptyDef, NotNullDef, NullDef, ParameterScriptAssertDef, PastDef, PastOrPresentDef, PatternDef, PESELDef, PositiveDef, PositiveOrZeroDef, RangeDef, REGONDef, ScriptAssertDef, SizeDef, TituloEleitoralDef, UniqueElementsDef, URLDef, UUIDDef`

---

public abstract class ConstraintDef<C extends ConstraintDef<C,A>, A extends Annotation>
extends AnnotationDef<C,A>
Base class for all constraint definition types. Each sub type represents a
single constraint annotation type and allows to add this constraint to a bean
class in a programmatic type-safe way with help of the
`ConstraintMapping` API.

Author:
Hardy Ferentschik, Gunnar Morling

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`ConstraintDef(Class<A> constraintType)`
 
`protected `
`ConstraintDef(ConstraintDef<?,A> original)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`C`
`groups(Class<?>... groups)`
 
`C`
`message(String message)`
 
`C`
`payload(Class<? extends Payload>... payload)`
 

### Methods inherited from class AnnotationDef

`addAnnotationAsParameter, addParameter, toString`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### ConstraintDef

protected ConstraintDef(Class<A> constraintType)

  - 

### ConstraintDef

protected ConstraintDef(ConstraintDef<?,A> original)

- 

## Method Details

  - 

### message

public C message(String message)

  - 

### groups

public C groups(Class<?>... groups)

  - 

### payload

public C payload(Class<? extends Payload>... payload)

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved