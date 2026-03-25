# Source: https://symfony.com/doc/current/validation.html

Title: Validation (Symfony Docs)

URL Source: https://symfony.com/doc/current/validation.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/validation.rst)

Validation is a very common task in web applications. Data entered in forms needs to be validated. Data also needs to be validated before it is written into a database or passed to a web service.

Symfony provides a [Validator](https://github.com/symfony/validator) component to handle this for you. This component is based on the [JSR303 Bean Validation specification](https://jcp.org/en/jsr/detail?id=303).

[Installation](https://symfony.com/doc/current/validation.html#installation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

In applications using [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex), run this command to install the validator before using it:

[The Basics of Validation](https://symfony.com/doc/current/validation.html#the-basics-of-validation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------

The best way to understand validation is to see it in action. To start, suppose you've created a plain-old-PHP object that you need to use somewhere in your application:

So far, this is an ordinary class that serves some purpose inside your application. The goal of validation is to tell you if the data of an object is valid. For this to work, you'll configure a list of rules (called [constraints](https://symfony.com/doc/current/validation.html#validation-constraints)) that the object must follow in order to be valid. These rules are usually defined using PHP code or attributes but they can also be defined as `.yaml` or `.xml` files inside the `config/validator/` directory.

For example, to indicate that the `$name` property must not be empty, add the following:

Adding this configuration by itself does not yet guarantee that the value will not be blank; you can still set it to a blank value if you want. To actually guarantee that the value adheres to the constraint, the object must be passed to the validator service to be checked.

Tip

Symfony's validator uses PHP reflection, as well as _"getter"_ methods, to get the value of any property, so they can be public, private or protected (see [Validation](https://symfony.com/doc/current/validation.html#validator-constraint-targets)).

Tip

Symfony provides a JSON schema for validation mapping files that enables autocompletion and validation in IDEs like PhpStorm. Add the following `$schema` key at the beginning of your YAML files to enable this feature:

### [Using the Validator Service](https://symfony.com/doc/current/validation.html#using-the-validator-service "Permalink to this headline")

Next, to actually validate an `Author` object, use the `validate()` method on the `validator` service (which implements [ValidatorInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Validator/ValidatorInterface.php "Symfony\Component\Validator\Validator\ValidatorInterface")). The job of the `validator` is to read the constraints (i.e. rules) of a class and verify if the data on the object satisfies those constraints. If validation fails, a non-empty list of errors ([ConstraintViolationList](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/ConstraintViolationList.php "Symfony\Component\Validator\ConstraintViolationList") class) is returned. Take this simple example from inside a controller:

If the `$name` property is empty, you will see the following error message:

If you insert a value into the `name` property, the happy success message will appear.

Tip

Most of the time, you won't interact directly with the `validator` service or need to worry about printing out the errors. Most of the time, you'll use validation indirectly when handling submitted form data. For more information, see [how to validate Symfony forms](https://symfony.com/doc/current/forms.html#validating-forms).

You could also pass the collection of errors into a template:

Inside the template, you can output the list of errors exactly as needed:

Note

Each validation error (called a "constraint violation"), is represented by a [ConstraintViolation](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/ConstraintViolation.php "Symfony\Component\Validator\ConstraintViolation") object. This object allows you, among other things, to get the constraint that caused this violation thanks to the `ConstraintViolation::getConstraint()` method.

[Constraints](https://symfony.com/doc/current/validation.html#constraints "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

The `validator` is designed to validate objects against _constraints_ (i.e. rules). In order to validate an object, simply map one or more constraints to its class and then pass it to the `validator` service.

Internally, a constraint is a PHP object that makes an assertive statement. In real life, a constraint could be: `'The cake must not be burned'`. In Symfony, constraints are similar: they are assertions that a condition is true. Given a value, a constraint will tell you if that value adheres to the rules of the constraint.

### [Supported Constraints](https://symfony.com/doc/current/validation.html#supported-constraints "Permalink to this headline")

Symfony packages many of the most commonly-needed constraints:

### [String Constraints](https://symfony.com/doc/current/validation.html#string-constraints "Permalink to this headline")

*   [Charset](https://symfony.com/doc/current/reference/constraints/Charset.html)
*   [Cidr](https://symfony.com/doc/current/reference/constraints/Cidr.html)
*   [CssColor](https://symfony.com/doc/current/reference/constraints/CssColor.html)
*   [Email](https://symfony.com/doc/current/reference/constraints/Email.html)
*   [ExpressionSyntax](https://symfony.com/doc/current/reference/constraints/ExpressionSyntax.html)
*   [Hostname](https://symfony.com/doc/current/reference/constraints/Hostname.html)
*   [Ip](https://symfony.com/doc/current/reference/constraints/Ip.html)
*   [Json](https://symfony.com/doc/current/reference/constraints/Json.html)
*   [Length](https://symfony.com/doc/current/reference/constraints/Length.html)
*   [MacAddress](https://symfony.com/doc/current/reference/constraints/MacAddress.html)
*   [NoSuspiciousCharacters](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html)
*   [NotCompromisedPassword](https://symfony.com/doc/current/reference/constraints/NotCompromisedPassword.html)
*   [PasswordStrength](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html)
*   [Regex](https://symfony.com/doc/current/reference/constraints/Regex.html)
*   [Twig](https://symfony.com/doc/current/reference/constraints/Twig.html)
*   [Ulid](https://symfony.com/doc/current/reference/constraints/Ulid.html)
*   [Url](https://symfony.com/doc/current/reference/constraints/Url.html)
*   [UserPassword](https://symfony.com/doc/current/reference/constraints/UserPassword.html)
*   [Uuid](https://symfony.com/doc/current/reference/constraints/Uuid.html)
*   [WordCount](https://symfony.com/doc/current/reference/constraints/WordCount.html)
*   [Yaml](https://symfony.com/doc/current/reference/constraints/Yaml.html)

### [Constraint Configuration](https://symfony.com/doc/current/validation.html#constraint-configuration "Permalink to this headline")

Some constraints, like [NotBlank](https://symfony.com/doc/current/reference/constraints/NotBlank.html), are simple whereas others, like the [Choice](https://symfony.com/doc/current/reference/constraints/Choice.html) constraint, have several configuration options available. Suppose that the `Author` class has another property called `genre` that defines the literature genre mostly associated with the author, which can be set to either "fiction" or "non-fiction":

[Constraints in Form Classes](https://symfony.com/doc/current/validation.html#constraints-in-form-classes "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------

Constraints can be defined while building the form via the `constraints` option of the form fields:

[Constraint Targets](https://symfony.com/doc/current/validation.html#constraint-targets "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------

Constraints can be applied to a class property (e.g. `name`), a getter method (e.g. `getFullName()`) or an entire class. Property constraints are the most common and easy to use. Getter constraints allow you to specify more complex validation rules. Finally, class constraints are intended for scenarios where you want to validate a class as a whole.

### [Properties](https://symfony.com/doc/current/validation.html#properties "Permalink to this headline")

Validating class properties is the most basic validation technique. Symfony allows you to validate private, protected or public properties. The next listing shows you how to configure the `$firstName` property of an `Author` class to have at least 3 characters.

Warning

The validator will use a value `null` if a typed property is uninitialized. This can cause unexpected behavior if the property holds a value when initialized. In order to avoid this, make sure all properties are initialized before validating them.

### [Getters](https://symfony.com/doc/current/validation.html#getters "Permalink to this headline")

Constraints can also be applied to the return value of a method. Symfony allows you to add a constraint to any private, protected or public method whose name starts with "get", "is" or "has". In this guide, these types of methods are referred to as "getters".

The benefit of this technique is that it allows you to validate your object dynamically. For example, suppose you want to make sure that a password field doesn't match the first name of the user (for security reasons). You can do this by creating an `isPasswordSafe()` method, and then asserting that this method must return `true`:

Now, create the `isPasswordSafe()` method and include the logic you need:

Note

The keen-eyed among you will have noticed that the prefix of the getter ("get", "is" or "has") is omitted in the mappings for the YAML, XML and PHP formats. This allows you to move the constraint to a property with the same name later (or vice versa) without changing your validation logic.

### [Classes](https://symfony.com/doc/current/validation.html#classes "Permalink to this headline")

Some constraints apply to the entire class being validated. For example, the [Callback](https://symfony.com/doc/current/reference/constraints/Callback.html) constraint is a generic constraint that's applied to the class itself. When that class is validated, methods specified by that constraint are simply executed so that each can provide more custom validation.

[Validating Object With Inheritance](https://symfony.com/doc/current/validation.html#validating-object-with-inheritance "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------

When you validate an object that extends another class, the validator automatically validates constraints defined in the parent class as well.

**The constraints defined in the parent properties will be applied to the child properties even if the child properties override those constraints**. Symfony will always merge the parent constraints for each property.

You can't change this behavior, but you can overcome it by defining the parent and the child constraints in different [validation groups](https://symfony.com/doc/current/validation/groups.html) and then select the appropriate group when validating each object.

[Extending Validation for a Class](https://symfony.com/doc/current/validation.html#extending-validation-for-a-class "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may want to add or override validation constraints on a class you cannot modify (for example, a model coming from a third party library or a bundle).

Suppose you use a third party `Product` class that validates the `name` property with a minimum length of 2, but in your application you want to enforce a minimum of 10 characters.

To do this, create a separate class and use the `#[ExtendsValidationFor]` attribute to tell the Validator which class should receive these constraints. Your new class name is irrelevant and the class is typically made `abstract` to make it clear it is never instantiated:

The constraints defined in this class are applied to the target class (`Product`) as if they were defined there.

You can only define constraints for properties that exist on the target class. Otherwise, a `MappingException` is thrown.

[Debugging the Constraints](https://symfony.com/doc/current/validation.html#debugging-the-constraints "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------

Use the `debug:validator` command to list the validation constraints of a given class:

You can also validate all the classes stored in a given directory:

[Final Thoughts](https://symfony.com/doc/current/validation.html#final-thoughts "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------

The Symfony `validator` is a powerful tool that can be leveraged to guarantee that the data of any object is "valid". The power behind validation lies in "constraints", which are rules that you can apply to properties or getter methods of your object. And while you'll most commonly use the validation framework indirectly when using forms, remember that it can be used anywhere to validate any object.

[Learn more](https://symfony.com/doc/current/validation.html#learn-more "Permalink to this headline")
-----------------------------------------------------------------------------------------------------

*   [How to Create a Custom Validation Constraint](https://symfony.com/doc/current/validation/custom_constraint.html)
*   [How to Apply only a Subset of all Your Validation Constraints (Validation Groups)](https://symfony.com/doc/current/validation/groups.html)
*   [How to Validate Raw Values (Scalar Values and Arrays)](https://symfony.com/doc/current/validation/raw_values.html)
*   [How to Sequentially Apply Validation Groups](https://symfony.com/doc/current/validation/sequence_provider.html)
*   [How to Handle Different Error Levels](https://symfony.com/doc/current/validation/severity.html)
*   [How to Translate Validation Constraint Messages](https://symfony.com/doc/current/validation/translations.html)

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
