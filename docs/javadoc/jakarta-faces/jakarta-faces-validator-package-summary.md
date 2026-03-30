# Package jakarta.faces.validator

---

package jakarta.faces.validator

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
BeanValidator

 A Validator that delegates validation of the
 bean property to the Bean Validation API.

DoubleRangeValidator

 **DoubleRangeValidator** is a `Validator`
 that checks the value of the corresponding component against specified minimum and maximum values.

FacesValidator

 The presence of this annotation on a class automatically registers the
 class with the runtime as a `Validator`.

FacesValidator.Literal

 Supports inline instantiation of the `FacesValidator` qualifier.

LengthValidator

 **LengthValidator** is a `Validator` that checks the number of
 characters in the String representation of the value of the associated component.

LongRangeValidator

 **LongRangeValidator** is a `Validator` that checks the value
 of the corresponding component against specified minimum and maximum values.

MethodExpressionValidator

 **MethodExpressionValidator** is a `Validator` that wraps a
 `MethodExpression`, and it performs validation by executing a method on an object identified by the
 `MethodExpression`.

RegexValidator

 A Validator that checks against a Regular Expression (which is the
 pattern property).

RequiredValidator

 A Validator that checks for an empty value in the same way that UIInput checks for a value.

Validator<T>

 A **Validator** implementation is a class that can perform validation
 (correctness checks) on a `EditableValueHolder`.

ValidatorException

 A **ValidatorException** is an exception thrown by the
 `validate()` method of a `Validator` to indicate that validation failed.
