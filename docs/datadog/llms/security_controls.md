# Source: https://docs.datadoghq.com/security/code_security/iast/security_controls.md

---
title: Security Controls
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Runtime Code Analysis (IAST) >
  Security Controls
---

# Security Controls

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Security Controls prevent false positives reporting in vulnerability detection using escaping and sanitization functions. Security functions refine how data is processed, ensuring that legitimate transformations do not trigger unnecessary security alerts.

## Input validators vs. sanitizers{% #input-validators-vs-sanitizers %}

Security Controls differentiate between **Input Validators** and **Sanitizers**, depending on how a function is used in security validation:

- **Input Validators**: Used when the function validates the parameters passed to it. Validators ensure that user inputs comply with expected formats before they are processed.
- **Sanitizers**: Used when the function validates or modifies the return value before it is used further in the application. Sanitizers help clean data to ensure it does not contain potentially harmful content.

## Configuring security controls{% #configuring-security-controls %}

The Security Controls definition must be placed in the configuration variable `DD_IAST_SECURITY_CONTROLS_CONFIGURATION`. To configure a list of security controls, follow the format and field specifications below. This format uses specific separators to structure each security control entry.

### Format{% #format %}

`<TYPE>:<SECURE_MARKS>:<CLASS/FILE>:<METHOD>:<PARAMETERS (Optional)>:<PARAMETERS TO VALIDATE (Optional)>`

### Field specifications{% #field-specifications %}

| **Field**                             | **Description**                                                                                                                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                              | Defines the type of control. **Accepted values:** `INPUT_VALIDATOR` or `SANITIZER`.                                                                                                                     |
| **Secure Marks**                      | List of vulnerability types to apply. Possible values are defined in Secure marks. Optionally, use `*` to indicate applicability to all types.                                                          |
| **Class/File**                        | Fully qualified class or file implementing the security control.                                                                                                                                        |
| **Method**                            | Name of the method implementing the security control.                                                                                                                                                   |
| **Parameters (Optional)**             | Fully qualified class parameters. Used to distinguish between overloaded methods. If omitted and overloading exists, the security control applies to all overloaded methods.                            |
| **Parameters to Validate (Optional)** | Zero-based list of parameter positions to validate. The first parameter is position **0**. This field applies **only** to `INPUT_VALIDATOR` types. Used when **not all parameters require validation**. |

### Separators{% #separators %}

- `;` (semicolon): Separates each security control.
- `:` (colon): Separates each field within a security control.
- `,` (comma): Separates items within a field that accepts a list.

### Secure marks{% #secure-marks %}

The available secure marks correspond to the codes associated with each injection-related vulnerability. These codes and their availability for each language can be found in [supported vulnerabilities](https://docs.datadoghq.com/security/code_security/iast/#overview).

The injection-related vulnerabilities are:

- Code Injection
- Command Injection
- Email HTML Injection
- Header Injection
- LDAP Injection
- NoSQL Injection
- Path Traversal
- Reflection Injection
- Server-Side Request Forgery (SSRF)
- SQL Injection
- Trust Boundary Violation
- Untrusted Deserialization
- Unvalidated Redirect
- XPath Injection
- Cross-Site Scripting (XSS)

## Compatibility requirements{% #compatibility-requirements %}

This feature is available starting from the following versions of each language's tracing library:

- **Java**: 1.45.0+
- **.NET**: 3.10.0+
- **Node.js**: 5.37.0+
- **Python**: 3.10.0+

## Examples{% #examples %}

{% collapsible-section %}
#### Java

### Input validator{% #input-validator %}

#### Method that validates all input parameters to avoid command injection vulnerabilities{% #method-that-validates-all-input-parameters-to-avoid-command-injection-vulnerabilities %}

##### Method{% #method %}

`bar.foo.CustomInputValidator#validate(String input1, String input2)`

##### Config{% #config %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar.foo.CustomInputValidator:validate`

#### Method that validates one input parameter to avoid command injection vulnerabilities{% #method-that-validates-one-input-parameter-to-avoid-command-injection-vulnerabilities %}

##### Method{% #method-1 %}

`bar.foo.CustomInputValidator#validate(String input1, String inputToValidate)`

##### Config{% #config-1 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar.foo.CustomInputValidator:validate:1`

#### Method that validates two input parameters to avoid command injection vulnerabilities{% #method-that-validates-two-input-parameters-to-avoid-command-injection-vulnerabilities %}

##### Method{% #method-2 %}

`bar.foo.CustomInputValidator#validate(String input1, String firstInputToValidate, String secondInputToValidate, Object anotherInput)`

##### Config{% #config-2 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar.foo.CustomInputValidator:validate:1,2`

#### Method that validates the input parameter to avoid command injection and code injection vulnerabilities{% #method-that-validates-the-input-parameter-to-avoid-command-injection-and-code-injection-vulnerabilities %}

##### Method{% #method-3 %}

`bar.foo.CustomInputValidator#validate(String input)`

##### Config{% #config-3 %}

`INPUT_VALIDATOR:COMMAND_INJECTION,CODE_INJECTION:bar.foo.CustomInputValidator:validate`

#### Method that validates the input parameter to avoid any vulnerabilities{% #method-that-validates-the-input-parameter-to-avoid-any-vulnerabilities %}

##### Method{% #method-4 %}

`bar.foo.CustomInputValidator#validate(String input)`

##### Config{% #config-4 %}

`INPUT_VALIDATOR:*:bar.foo.CustomInputValidator:validate`

#### Overloaded method that validates the input parameter to avoid command injection vulnerabilities{% #overloaded-method-that-validates-the-input-parameter-to-avoid-command-injection-vulnerabilities %}

##### Methods{% #methods %}

`bar.foo.CustomInputValidator#validate(String input)`

`bar.foo.CustomInputValidator#validate(String input, String input2)`

##### Config{% #config-5 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar.foo.CustomInputValidator:validate:java.lang.String`

##### Note{% #note %}

Applies for the first method.

#### Overloaded methods that validate the input parameter to avoid command injection vulnerabilities{% #overloaded-methods-that-validate-the-input-parameter-to-avoid-command-injection-vulnerabilities %}

##### Methods{% #methods-1 %}

`bar.foo.CustomInputValidator#validate(String input)`

`bar.foo.CustomInputValidator#validate(String input, String input2)`

##### Config{% #config-6 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar.foo.CustomInputValidator:validate`

##### Note{% #note-1 %}

Applies for both methods.

### Sanitizer{% #sanitizer %}

#### Sanitizer to avoid command injection vulnerabilities{% #sanitizer-to-avoid-command-injection-vulnerabilities %}

##### Method{% #method-5 %}

`bar.foo.CustomSanitizer#sanitize(String input)`

##### Config{% #config-7 %}

`SANITIZER:COMMAND_INJECTION:bar.foo.CustomSanitizer:sanitize`

#### Sanitizer to avoid command injection and code injection vulnerabilities{% #sanitizer-to-avoid-command-injection-and-code-injection-vulnerabilities %}

##### Method{% #method-6 %}

`bar.foo.CustomSanitizer#sanitize(String input)`

##### Config{% #config-8 %}

`SANITIZER:COMMAND_INJECTION,CODE_INJECTION:bar.foo.CustomSanitizer:sanitize`

#### Sanitizer to avoid any vulnerabilities{% #sanitizer-to-avoid-any-vulnerabilities %}

##### Method{% #method-7 %}

`bar.foo.CustomSanitizer#sanitize(String input)`

##### Config{% #config-9 %}

`SANITIZER:*:bar.foo.CustomSanitizer:sanitize`

#### Overloaded sanitizer to avoid command injection vulnerabilities{% #overloaded-sanitizer-to-avoid-command-injection-vulnerabilities %}

##### Methods{% #methods-2 %}

`bar.foo.CustomSanitizer#sanitize(String input)`

`bar.foo.CustomSanitizer#sanitize(String input, String input2)`

##### Config{% #config-10 %}

`SANITIZER:COMMAND_INJECTION:bar.foo.CustomSanitizer:sanitize:java.lang.String`

##### Note{% #note-2 %}

applies for the first method

#### Overloaded sanitizers to avoid command injection vulnerabilities{% #overloaded-sanitizers-to-avoid-command-injection-vulnerabilities %}

##### Methods{% #methods-3 %}

`bar.foo.CustomSanitizer#sanitize(String input)`

`bar.foo.CustomSanitizer#sanitize(String input, String input2)`

##### Config{% #config-11 %}

`SANITIZER:COMMAND_INJECTION:bar.foo.CustomSanitizer:sanitize`

##### Note{% #note-3 %}

applies for both methods
{% /collapsible-section %}

{% collapsible-section %}
#### Node.js

### Input validator{% #input-validator-1 %}

#### Method that validates all input parameters to avoid command injection vulnerabilities{% #method-that-validates-all-input-parameters-to-avoid-command-injection-vulnerabilities-1 %}

##### Method{% #method-8 %}

`bar/foo/custom_input_validator.js#validate(input1, input2)`

##### Config{% #config-12 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar/foo/custom_input_validator.js:validate`

#### Method that validates one input parameter to avoid command injection vulnerabilities{% #method-that-validates-one-input-parameter-to-avoid-command-injection-vulnerabilities-1 %}

##### Method{% #method-9 %}

`bar/foo/custom_input_validator.js#validate(input1, inputToValidate)`

##### Config{% #config-13 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar/foo/custom_input_validator.js:validate:1`

#### Method that validates two input parameters to avoid command injection vulnerabilities{% #method-that-validates-two-input-parameters-to-avoid-command-injection-vulnerabilities-1 %}

##### Method{% #method-10 %}

`bar/foo/custom_input_validator.js#validate(input1, firstInputToValidate, secondInputToValidate, anotherInput)`

##### Config{% #config-14 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar/foo/custom_input_validator.js:validate:1,2`

#### Method that validates the input parameter to avoid command injection and code injection vulnerabilities{% #method-that-validates-the-input-parameter-to-avoid-command-injection-and-code-injection-vulnerabilities-1 %}

##### Method{% #method-11 %}

`bar/foo/custom_input_validator.js#validate(input)`

##### Config{% #config-15 %}

`INPUT_VALIDATOR:COMMAND_INJECTION,CODE_INJECTION:bar/foo/custom_input_validator.js:validate`

#### Method that validates the input parameter to avoid any vulnerabilities{% #method-that-validates-the-input-parameter-to-avoid-any-vulnerabilities-1 %}

##### Method{% #method-12 %}

`bar/foo/custom_input_validator.js#validate(input)`

##### Config{% #config-16 %}

`INPUT_VALIDATOR:*:bar/foo/custom_input_validator.js:validate`

### Sanitizer{% #sanitizer-1 %}

#### Sanitizer to avoid command injection vulnerabilities{% #sanitizer-to-avoid-command-injection-vulnerabilities-1 %}

##### Method{% #method-13 %}

`bar/foo/custom_input_sanitizer.js#sanitize(input)`

##### Config{% #config-17 %}

`SANITIZER:COMMAND_INJECTION:bar/foo/custom_input_sanitizer.js:sanitize`

#### Sanitizer to avoid command injection and code injection vulnerabilities{% #sanitizer-to-avoid-command-injection-and-code-injection-vulnerabilities-1 %}

##### Method{% #method-14 %}

`bar/foo/custom_input_sanitizer.js#sanitize(input)`

##### Config{% #config-18 %}

`SANITIZER:COMMAND_INJECTION,CODE_INJECTION:bar/foo/custom_input_sanitizer.js:sanitize`

#### Sanitizer to avoid any vulnerabilities{% #sanitizer-to-avoid-any-vulnerabilities-1 %}

##### Method{% #method-15 %}

`bar/foo/custom_input_sanitizer.js#sanitize(input)`

##### Config{% #config-19 %}

`SANITIZER:*:bar/foo/custom_input_sanitizer.js:sanitize`

### Special cases{% #special-cases %}

#### Security control method inside an exported object{% #security-control-method-inside-an-exported-object %}

Method `validate`, which is exported inside an object `validators`, that validates the input parameter to avoid command injection vulnerabilities.

```javascript
// bar/foo/custom_input_validator.js
module.exports = {
  validators: {
    validate: (input) => {
      /* validation process */
    }
  }
}
```

#### Config{% #config-20 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:bar/foo/custom_input_validator.js:validators.validate`

#### Security control method from a transitive dependency{% #security-control-method-from-a-transitive-dependency %}

Because of `npm`'s flat dependency structure, it is not possible to differentiate between a direct dependency and a transitive dependency. This means if a security control is defined inside a dependency, all instances of that dependency (direct or transitive), are affected.

The following security control definition affects every `sql-sanitizer` package found in the dependency tree.

#### Config{% #config-21 %}

`SANITIZER:SQL_INJECTION:node_modules/sql-sanitizer/index.js:sanitize`
{% /collapsible-section %}

{% collapsible-section %}
#### .NET

### General syntax{% #general-syntax %}

`TYPE:SECURE_MARKS:Assembly:Class:Method(ParameterTypes)[:ParameterIndexes]`

{% alert level="info" %}
Parameter types must be fully qualified with their namespace. Example: `System.String`Parameter indexes are comma-separated. If no parameter index is provided, the value of the first parameter defaults to 0.
{% /alert %}

### Input validator{% #input-validator-2 %}

#### Method that validates all input parameters to avoid command injection vulnerabilities{% #method-that-validates-all-input-parameters-to-avoid-command-injection-vulnerabilities-2 %}

##### Method{% #method-16 %}

`[FooAssembly]CustomInputValidatorClass::ValidateMethod(string input1, string input2)`

##### Config{% #config-22 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:FooAssembly:CustomInputValidatorClass:ValidateMethod(System.String,System.String):0,1`

#### Method that validates one input parameter to avoid command injection vulnerabilities{% #method-that-validates-one-input-parameter-to-avoid-command-injection-vulnerabilities-2 %}

##### Method{% #method-17 %}

`[FooAssembly]CustomInputValidatorClass::ValidateMethod(string input1, string inputToValidate)`

##### Config{% #config-23 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:FooAssembly:CustomInputValidatorClass:ValidateMethod(System.String,System.String):1`

#### Method that validates two input parameters to avoid command injection vulnerabilities{% #method-that-validates-two-input-parameters-to-avoid-command-injection-vulnerabilities-2 %}

##### Method{% #method-18 %}

`[FooAssembly]CustomInputValidatorClass::ValidateMethod(string input1, string firstInputToValidate, string secondInputToValidate, object anotherInput)`

##### Config{% #config-24 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:FooAssembly:CustomInputValidatorClass:ValidateMethod(System.String,System.String,System.String,System.Object):1,2`

#### Method that validates the input parameter to avoid command injection and code injection vulnerabilities{% #method-that-validates-the-input-parameter-to-avoid-command-injection-and-code-injection-vulnerabilities-2 %}

##### Method{% #method-19 %}

`[FooAssembly]CustomInputValidatorClass::ValidateMethod(string input)`

##### Config{% #config-25 %}

`INPUT_VALIDATOR:COMMAND_INJECTION,CODE_INJECTION:FooAssembly:CustomInputValidatorClass:ValidateMethod(System.String)`

### Sanitizer{% #sanitizer-2 %}

#### Sanitizer to avoid command injection vulnerabilities{% #sanitizer-to-avoid-command-injection-vulnerabilities-2 %}

##### Method{% #method-20 %}

`[FooAssembly]CustomInputValidatorClass::SanitizerMethod(string input)`

##### Config{% #config-26 %}

`SANITIZER:COMMAND_INJECTION:FooAssembly:CustomInputValidatorClass:SanitizerMethod(System.String)`
{% /collapsible-section %}

{% collapsible-section %}
#### Python

### Input validator{% #input-validator-3 %}

#### Method that validates all input parameters to avoid command injection vulnerabilities{% #method-that-validates-all-input-parameters-to-avoid-command-injection-vulnerabilities-3 %}

##### Method{% #method-21 %}

`python_project.security.validators.validate(input1, input2)`

##### Config{% #config-27 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:python_project.security.validators:validate`

#### Method that validates one input parameter to avoid command injection vulnerabilities{% #method-that-validates-one-input-parameter-to-avoid-command-injection-vulnerabilities-3 %}

##### Method{% #method-22 %}

`python_project.security.validators.validate(input1, input_to_validate)`

##### Config{% #config-28 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:python_project.security.validators:validate:1`

#### Method that validates two input parameters to avoid command injection vulnerabilities{% #method-that-validates-two-input-parameters-to-avoid-command-injection-vulnerabilities-3 %}

##### Method{% #method-23 %}

`python_project.security.validators.validate(input1, first_input_to_validate, second_input_to_validate, another_input)`

##### Config{% #config-29 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:python_project.security.validators:validate:1,2`

#### Method that validates the input parameter to avoid command injection and code injection vulnerabilities{% #method-that-validates-the-input-parameter-to-avoid-command-injection-and-code-injection-vulnerabilities-3 %}

##### Method{% #method-24 %}

`python_project.security.validators.validate(input)`

##### Config{% #config-30 %}

`INPUT_VALIDATOR:COMMAND_INJECTION,CODE_INJECTION:python_project.security.validators:validate`

#### Method that validates the input parameter to avoid any vulnerabilities{% #method-that-validates-the-input-parameter-to-avoid-any-vulnerabilities-2 %}

##### Method{% #method-25 %}

`python_project.security.validators.validate(input)`

##### Config{% #config-31 %}

`INPUT_VALIDATOR:*:python_project.security.validators:validate`

### Sanitizer{% #sanitizer-3 %}

#### Sanitizer to avoid command injection vulnerabilities{% #sanitizer-to-avoid-command-injection-vulnerabilities-3 %}

##### Method{% #method-26 %}

`python_project.sql_sanitizer.SQLSanitizer.sanitize(input)`

##### Config{% #config-32 %}

`SANITIZER:COMMAND_INJECTION:python_project.sql_sanitizer:SQLSanitizer.sanitize`

#### Sanitizer to avoid command injection and code injection vulnerabilities{% #sanitizer-to-avoid-command-injection-and-code-injection-vulnerabilities-2 %}

##### Method{% #method-27 %}

`python_project.security.sanitizers.DataSanitizer.sanitize(input)`

##### Config{% #config-33 %}

`SANITIZER:COMMAND_INJECTION,CODE_INJECTION:python_project.security.sanitizers:DataSanitizer.sanitize`

#### Sanitizer to avoid any vulnerabilities{% #sanitizer-to-avoid-any-vulnerabilities-2 %}

##### Method{% #method-28 %}

`python_project.security.sanitizers.UniversalSanitizer.sanitize(input)`

##### Config{% #config-34 %}

`SANITIZER:*:python_project.security.sanitizers:UniversalSanitizer.sanitize`

### Special cases{% #special-cases-1 %}

#### Function-level security control{% #function-level-security-control %}

Function `validate_user_input` that validates the input parameter to avoid command injection vulnerabilities.

```python
# python_project/utils/validators.py
def validate_user_input(input_data):
    """Validation process"""
    pass
```

##### Config{% #config-35 %}

`INPUT_VALIDATOR:COMMAND_INJECTION:python_project.utils.validators:validate_user_input`

#### Security control method from a third-party package{% #security-control-method-from-a-third-party-package %}

The following security control definition affects the `sanitize_sql` method from the `secure_db` package.

##### Config{% #config-36 %}

`SANITIZER:SQL_INJECTION:secure_db.sanitizers:SQLSanitizer.sanitize_sql`
{% /collapsible-section %}
