# Source: https://symfony.com/doc/current/validation/custom_constraint.html

Title: How to Create a Custom Validation Constraint (Symfony Docs)

URL Source: https://symfony.com/doc/current/validation/custom_constraint.html

Markdown Content:
How to Create a Custom Validation Constraint (Symfony Docs)
===============
[Skip to content](https://symfony.com/doc/current/validation/custom_constraint.html#main-content)

[Symfony Hub](https://symfony.com/doc/current/validation/custom_constraint.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/current/validation/custom_constraint.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight](https://insight.symfony.com/)[![Image 2](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight: The life jacket for your projects](https://insight.symfony.com/)[![Image 3](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight helps you protect your projects against security issues and technical debt.](https://insight.symfony.com/)

[](https://symfony.com/doc/current/validation/custom_constraint.html# "Search")

[](https://symfony.com/doc/current/validation/custom_constraint.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/validation/custom_constraint.html)

![Image 4: SensioLabs](https://connect.symfony.com/assets/images/sln-v2/sensiolabs-9Agct9D.png)
SensioLabs is the creator of Symfony and plays a pivotal role in supporting its growth. With a passionate team pushing the boundaries of PHP, SensioLabs helps organizations get the most out of Symfony through quality, high-performance, software vendor-level training and consulting services.

*   [International](https://sensiolabs.com/en)
*   [France](https://sensiolabs.com/fr)

In the Spotlight
----------------

[![Image 5: SymfonyInsight](https://connect.symfony.com/assets/images/sln-v2/symfonyinsight-HwpmiQ3.png)](https://insight.symfony.com/)

[![Image 6: Blackfire](https://connect.symfony.com/assets/images/sln-v2/blackfire-ca6NfRp.png)](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)

Open Source
-----------

*   [Symfony - Web framework](https://symfony.com/)
*   [Twig - Templating](https://twig.symfony.com/)
*   [PHP Polyfills](https://github.com/symfony/polyfill)

Products
--------

*   [Insight: PHP Quality](https://insight.symfony.com/)
*   [Blackfire: Web App performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)
*   [SymfonyCloud powered by Upsun](https://symfony.com/cloud)

Solutions & Services
--------------------

*   [Training](https://training.sensiolabs.com/)
*   [Certification](https://certification.symfony.com/)
*   [Technical Solutions](https://sensiolabs.com/solutions)
*   [SensioLabs University](https://university.sensiolabs.com/)
*   [Experts](https://expert.sensiolabs.com/)

Community
---------

*   [Community](https://connect.symfony.com/)
*   [Conferences](https://live.symfony.com/)
*   [Videos](https://www.youtube.com/symfonytv)
*   [Partners](https://network.sensiolabs.com/en/partenaires)

Blogs
-----

[Symfony](https://symfony.com/blog/), [SensioLabs](https://blog.sensiolabs.com/), [Insight](https://blog.insight.symfony.com/), and [Blackfire](https://blog.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler). 

[](https://symfony.com/)

Close

*   About

    *   [What is Symfony?](https://symfony.com/what-is-symfony)
    *   [Community](https://symfony.com/community)
    *   [News](https://symfony.com/blog/)
    *   [Contributing](https://symfony.com/doc/current/contributing/index.html)
    *   [Support](https://symfony.com/support)

*   Documentation

    *   [Symfony Docs](https://symfony.com/doc)
    *   [Symfony Book](https://symfony.com/book)
    *   [Screencasts](https://symfonycasts.com/)
    *   [Symfony Bundles](https://symfony.com/bundles)
    *   [Symfony Cloud](https://symfony.com/doc/cloud/)
    *   [Training](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)

*   Services

    *   [Upsun for Symfony](https://symfony.com/cloud/)Best platform to deploy Symfony apps
    *   [SymfonyInsight](https://insight.symfony.com/)Automatic quality checks for your apps
    *   [Symfony Certification](https://certification.symfony.com/)Prove your knowledge and boost your career
    *   [SensioLabs](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)Professional services to help you with Symfony
    *   [Blackfire](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)Profile and monitor performance of your apps

*   Other
*   [Blog](https://symfony.com/blog/)
*   [Download](https://symfony.com/download)

sponsored by[](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_sponsoredby&utm_campaign=permanent_referral "SensioLabs, PHP services and software solutions for enterprise and community.")

[SymfonyOnline June 2026](https://live.symfony.com/2026-online-june)

June 11 – 12, 2026

100% Online

+20 talks and workshops

1.   [Home](https://symfony.com/)
2.   [Documentation](https://symfony.com/doc)
3.   [Validation](https://symfony.com/doc/current/validation.html)
4.    How to Create a Custom Validation Constraint 

 Search Symfony Docs 

Version:

Table of Contents

*   [Creating the Constraint Class](https://symfony.com/doc/current/validation/custom_constraint.html#creating-the-constraint-class)
*   [Creating the Validator itself](https://symfony.com/doc/current/validation/custom_constraint.html#creating-the-validator-itself)
*   [Using the new Validator](https://symfony.com/doc/current/validation/custom_constraint.html#using-the-new-validator)
    *   [Constraint Validators with Dependencies](https://symfony.com/doc/current/validation/custom_constraint.html#constraint-validators-with-dependencies)
    *   [Constraint Validators with Custom Options](https://symfony.com/doc/current/validation/custom_constraint.html#constraint-validators-with-custom-options)
    *   [Create a Reusable Set of Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#create-a-reusable-set-of-constraints)
    *   [Class Constraint Validator](https://symfony.com/doc/current/validation/custom_constraint.html#class-constraint-validator)

*   [Testing Custom Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#testing-custom-constraints)
    *   [Atomic Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#atomic-constraints)
    *   [Compound Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#compound-constraints)

How to Create a Custom Validation Constraint
============================================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/validation/custom_constraint.rst)

You can create a custom constraint by extending the base constraint class, [Constraint](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Constraint.php "Symfony\Component\Validator\Constraint"). As an example you're going to create a basic validator that checks if a string contains only alphanumeric characters.

[Creating the Constraint Class](https://symfony.com/doc/current/validation/custom_constraint.html#creating-the-constraint-class "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

First you need to create a Constraint class and extend [Constraint](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Constraint.php "Symfony\Component\Validator\Constraint"):

Attributes

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```
// src/Validator/ContainsAlphanumeric.php
namespace App\Validator;

use Symfony\Component\Validator\Constraint;

#[\Attribute]
class ContainsAlphanumeric extends Constraint
{
    public string $message = 'The string "{{ string }}" contains an illegal character: it can only contain letters or numbers.';
    public string $mode = 'strict';

    // all configurable options must be passed to the constructor
    public function __construct(?string $mode = null, ?string $message = null, ?array $groups = null, $payload = null)
    {
        $this->mode = $mode ?? $this->mode;
        $this->message = $message ?? $this->message;

        parent::__construct(null, $groups, $payload);
    }
}
```

Add `#[\Attribute]` to the constraint class if you want to use it as an attribute in other classes.

You can use `#[HasNamedArguments]` to make some constraint options required:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```
// src/Validator/ContainsAlphanumeric.php
namespace App\Validator;

use Symfony\Component\Validator\Attribute\HasNamedArguments;
use Symfony\Component\Validator\Constraint;

#[\Attribute]
class ContainsAlphanumeric extends Constraint
{
    public string $message = 'The string "{{ string }}" contains an illegal character: it can only contain letters or numbers.';

    #[HasNamedArguments]
    public function __construct(
        public string $mode,
        ?array $groups = null,
        mixed $payload = null,
    ) {
        parent::__construct(null, $groups, $payload);
    }
}
```

Note

Constraints are cached for performance reasons. The base `Constraint` class implements `__serialize()`_, which automatically handles all properties, including private ones defined in child classes. This means you can use private properties in your custom constraints without any extra configuration.

[Creating the Validator itself](https://symfony.com/doc/current/validation/custom_constraint.html#creating-the-validator-itself "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

As you can see, a constraint class is fairly minimal. The actual validation is performed by another "constraint validator" class. The constraint validator class is specified by the constraint's `validatedBy()` method, which has this default logic:

1
2
3
4
5
```
// in the base Symfony\Component\Validator\Constraint class
public function validatedBy(): string
{
    return static::class.'Validator';
}
```

In other words, if you create a custom `Constraint` (e.g. `MyConstraint`), Symfony will automatically look for another class, `MyConstraintValidator` when actually performing the validation.

The validator class only has one required method `validate()`:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
```
// src/Validator/ContainsAlphanumericValidator.php
namespace App\Validator;

use Symfony\Component\Validator\Constraint;
use Symfony\Component\Validator\ConstraintValidator;
use Symfony\Component\Validator\Exception\UnexpectedTypeException;
use Symfony\Component\Validator\Exception\UnexpectedValueException;

class ContainsAlphanumericValidator extends ConstraintValidator
{
    public function validate(mixed $value, Constraint $constraint): void
    {
        if (!$constraint instanceof ContainsAlphanumeric) {
            throw new UnexpectedTypeException($constraint, ContainsAlphanumeric::class);
        }

        // custom constraints should ignore null and empty values to allow
        // other constraints (NotBlank, NotNull, etc.) to take care of that
        if (null === $value || '' === $value) {
            return;
        }

        if (!is_string($value)) {
            // throw this exception if your validator cannot handle the passed type so that it can be marked as invalid
            throw new UnexpectedValueException($value, 'string');

            // separate multiple types using pipes
            // throw new UnexpectedValueException($value, 'string|int');
        }

        // access your configuration options like this:
        if ('strict' === $constraint->mode) {
            // ...
        }

        if (preg_match('/^[a-zA-Z0-9]+$/', $value, $matches)) {
            return;
        }

        // the argument must be a string or an object implementing __toString()
        $this->context->buildViolation($constraint->message)
            ->setParameter('{{ string }}', $value)
            ->addViolation();
    }
}
```

Inside `validate()`, you don't need to return a value. Instead, you add violations to the validator's `context` property and a value will be considered valid if it causes no violations. The `buildViolation()` method takes the error message as its argument and returns an instance of [ConstraintViolationBuilderInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Violation/ConstraintViolationBuilderInterface.php "Symfony\Component\Validator\Violation\ConstraintViolationBuilderInterface"). The `addViolation()` method call finally adds the violation to the context.

Tip

Validation error messages are automatically translated to the current application locale. If your application doesn't use translations, you can disable this behavior by calling the `disableTranslation()` method of `ConstraintViolationBuilderInterface`. See also the [framework.validation.disable_translation option](https://symfony.com/doc/current/reference/configuration/framework.html#reference-validation-disable_translation).

[Using the new Validator](https://symfony.com/doc/current/validation/custom_constraint.html#using-the-new-validator "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------

You can use custom validators like the ones provided by Symfony itself:

Attributes YAML XML PHP

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```
// src/Entity/AcmeEntity.php
namespace App\Entity;

use App\Validator as AcmeAssert;
use Symfony\Component\Validator\Constraints as Assert;

class AcmeEntity
{
    // ...

    #[Assert\NotBlank]
    #[AcmeAssert\ContainsAlphanumeric(mode: 'loose')]
    protected string $name;

    // ...
}
```

1
2
3
4
5
6
7
```
# config/validator/validation.yaml
App\Entity\User:
    properties:
        name:
            - NotBlank: ~
            - App\Validator\ContainsAlphanumeric:
                mode: 'loose'
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Entity\User">
        <property name="name">
            <constraint name="NotBlank"/>
            <constraint name="App\Validator\ContainsAlphanumeric">
                <option name="mode">loose</option>
            </constraint>
        </property>
    </class>
</constraint-mapping>
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
```
// src/Entity/User.php
namespace App\Entity;

use App\Validator\ContainsAlphanumeric;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class User
{
    protected string $name = '';

    // ...

    public static function loadValidatorMetadata(ClassMetadata $metadata): void
    {
        $metadata->addPropertyConstraint('name', new Assert\NotBlank());
        $metadata->addPropertyConstraint('name', new ContainsAlphanumeric(mode: 'loose'));
    }
}
```

If your constraint contains options, then they must be public properties on the custom Constraint class you created earlier. These options can be configured like options on core Symfony constraints.

### [Constraint Validators with Dependencies](https://symfony.com/doc/current/validation/custom_constraint.html#constraint-validators-with-dependencies "Permalink to this headline")

If you're using the [default services.yaml configuration](https://symfony.com/doc/current/service_container.html#service-container-services-load-example), then your validator is already registered as a service and [tagged](https://symfony.com/doc/current/service_container/tags.html) with the necessary `validator.constraint_validator`. This means you can [inject services or configuration](https://symfony.com/doc/current/service_container.html#services-constructor-injection) like any other service.

### [Constraint Validators with Custom Options](https://symfony.com/doc/current/validation/custom_constraint.html#constraint-validators-with-custom-options "Permalink to this headline")

If your custom constraint defines configuration options, declare them as public properties on the constraint class, add them as mandatory constructor arguments, and apply the `#[HasNamedArguments]` attribute to the constructor:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
```
// src/Validator/Foo.php
namespace App\Validator;

use Symfony\Component\Validator\Attribute\HasNamedArguments;
use Symfony\Component\Validator\Constraint;

#[\Attribute]
class Foo extends Constraint
{
    public string $message = 'This value is invalid';
    public bool $optionalBarOption = false;

    #[HasNamedArguments]
    public function __construct(
        public string $mandatoryFooOption,
        ?string $message = null,
        ?bool $optionalBarOption = null,
        ?array $groups = null,
        mixed $payload = null,
    ) {
        parent::__construct(null, $groups, $payload);

        $this->message = $message ?? $this->message;
        $this->optionalBarOption = $optionalBarOption ?? $this->optionalBarOption;
    }
}
```

Then, inside the validator class you can access these options directly via the constraint class passed to the `validate()` method:

1
2
3
4
5
6
7
8
9
10
11
12
```
class FooValidator extends ConstraintValidator
{
    public function validate($value, Constraint $constraint)
    {
        // access any option of the constraint
        if ($constraint->optionalBarOption) {
            // ...
        }

        // ...
    }
}
```

When using this constraint in your own application, you can pass the value of the custom options like you pass any other option in built-in constraints:

Attributes YAML XML PHP

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
```
// src/Entity/AcmeEntity.php
namespace App\Entity;

use App\Validator as AcmeAssert;
use Symfony\Component\Validator\Constraints as Assert;

class AcmeEntity
{
    // ...

    #[Assert\NotBlank]
    #[AcmeAssert\Foo(
        mandatoryFooOption: 'bar',
        optionalBarOption: true
    )]
    protected $name;

    // ...
}
```

1
2
3
4
5
6
7
8
```
# config/validator/validation.yaml
App\Entity\AcmeEntity:
    properties:
        name:
            - NotBlank: ~
            - App\Validator\Foo:
                mandatoryFooOption: bar
                optionalBarOption: true
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Entity\AcmeEntity">
        <property name="name">
            <constraint name="NotBlank"/>
            <constraint name="App\Validator\Foo">
                <option name="mandatoryFooOption">bar</option>
                <option name="optionalBarOption">true</option>
            </constraint>
        </property>
    </class>
</constraint-mapping>
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```
// src/Entity/AcmeEntity.php
namespace App\Entity;

use App\Validator\ContainsAlphanumeric;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class AcmeEntity
{
    public $name;

    public static function loadValidatorMetadata(ClassMetadata $metadata)
    {
        $metadata->addPropertyConstraint('name', new Assert\NotBlank());
        $metadata->addPropertyConstraint('name', new Foo(
            mandatoryFooOption: 'bar',
            optionalBarOption: true,
        ));
    }
}
```

### [Create a Reusable Set of Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#create-a-reusable-set-of-constraints "Permalink to this headline")

In case you need to consistently apply a common set of constraints across your application, you can extend the [Compound constraint](https://symfony.com/doc/current/reference/constraints/Compound.html).

### [Class Constraint Validator](https://symfony.com/doc/current/validation/custom_constraint.html#class-constraint-validator "Permalink to this headline")

Besides validating a single property, a constraint can have an entire class as its scope.

For instance, imagine you also have a `PaymentReceipt` entity and you need to make sure the email of the receipt payload matches the user's email. First, create a constraint and override the `getTargets()` method:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```
// src/Validator/ConfirmedPaymentReceipt.php
namespace App\Validator;

use Symfony\Component\Validator\Constraint;

#[\Attribute]
class ConfirmedPaymentReceipt extends Constraint
{
    public string $userDoesNotMatchMessage = 'User\'s e-mail address does not match that of the receipt';

    public function getTargets(): string
    {
        return self::CLASS_CONSTRAINT;
    }
}
```

Now, the constraint validator will get an object as the first argument to `validate()`:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
```
// src/Validator/ConfirmedPaymentReceiptValidator.php
namespace App\Validator;

use Symfony\Component\Validator\Constraint;
use Symfony\Component\Validator\ConstraintValidator;
use Symfony\Component\Validator\Exception\UnexpectedTypeException;
use Symfony\Component\Validator\Exception\UnexpectedValueException;

class ConfirmedPaymentReceiptValidator extends ConstraintValidator
{
    /**
     * @param PaymentReceipt $receipt
     */
    public function validate($receipt, Constraint $constraint): void
    {
        if (!$receipt instanceof PaymentReceipt) {
            throw new UnexpectedValueException($receipt, PaymentReceipt::class);
        }

        if (!$constraint instanceof ConfirmedPaymentReceipt) {
            throw new UnexpectedTypeException($constraint, ConfirmedPaymentReceipt::class);
        }

        $receiptEmail = $receipt->getPayload()['email'] ?? null;
        $userEmail = $receipt->getUser()->getEmail();

        if ($userEmail !== $receiptEmail) {
            $this->context
                ->buildViolation($constraint->userDoesNotMatchMessage)
                ->atPath('user.email')
                ->addViolation();
        }
    }
}
```

Tip

The `atPath()` method defines the property with which the validation error is associated. Use any [valid PropertyAccess syntax](https://symfony.com/doc/current/components/property_access.html) to define that property.

A class constraint validator must be applied to the class itself:

Attributes YAML XML PHP

1
2
3
4
5
6
7
8
9
10
```
// src/Entity/AcmeEntity.php
namespace App\Entity;

use App\Validator as AcmeAssert;

#[AcmeAssert\ConfirmedPaymentReceipt]
class AcmeEntity
{
    // ...
}
```

1
2
3
4
```
# config/validator/validation.yaml
App\Entity\PaymentReceipt:
    constraints:
        - App\Validator\ConfirmedPaymentReceipt: ~
```

1
2
3
4
5
6
7
8
9
10
11
```
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping
        https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Entity\PaymentReceipt">
        <constraint name="App\Validator\ConfirmedPaymentReceipt"/>
    </class>
</constraint-mapping>
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```
// src/Entity/PaymentReceipt.php
namespace App\Entity;

use App\Validator\ConfirmedPaymentReceipt;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class PaymentReceipt
{
    // ...

    public static function loadValidatorMetadata(ClassMetadata $metadata): void
    {
        $metadata->addConstraint(new ConfirmedPaymentReceipt());
    }
}
```

[Testing Custom Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#testing-custom-constraints "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### [Atomic Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#atomic-constraints "Permalink to this headline")

Use the [ConstraintValidatorTestCase](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Test/ConstraintValidatorTestCase.php "Symfony\Component\Validator\Test\ConstraintValidatorTestCase") class to simplify writing unit tests for your custom constraints:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
```
// tests/Validator/ContainsAlphanumericValidatorTest.php
namespace App\Tests\Validator;

use App\Validator\ContainsAlphanumeric;
use App\Validator\ContainsAlphanumericValidator;
use PHPUnit\Framework\Attributes\DataProvider;
use Symfony\Component\Validator\ConstraintValidatorInterface;
use Symfony\Component\Validator\Test\ConstraintValidatorTestCase;

class ContainsAlphanumericValidatorTest extends ConstraintValidatorTestCase
{
    protected function createValidator(): ConstraintValidatorInterface
    {
        return new ContainsAlphanumericValidator();
    }

    public function testNullIsValid(): void
    {
        $this->validator->validate(null, new ContainsAlphanumeric());

        $this->assertNoViolation();
    }

    #[DataProvider('provideInvalidConstraints')]
    public function testTrueIsInvalid(ContainsAlphanumeric $constraint): void
    {
        $this->validator->validate('...', $constraint);

        $this->buildViolation('myMessage')
            ->setParameter('{{ string }}', '...')
            ->assertRaised();
    }

    public static function provideInvalidConstraints(): \Generator
    {
        yield [new ContainsAlphanumeric(message: 'myMessage')];
        // ...
    }
}
```

### [Compound Constraints](https://symfony.com/doc/current/validation/custom_constraint.html#compound-constraints "Permalink to this headline")

Consider the following compound constraint that checks if a string meets the minimum requirements for your password policy:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
```
// src/Validator/PasswordRequirements.php
namespace App\Validator;

use Symfony\Component\Validator\Constraints as Assert;

#[\Attribute]
class PasswordRequirements extends Assert\Compound
{
    protected function getConstraints(array $options): array
    {
        return [
            new Assert\NotBlank(allowNull: false),
            new Assert\Length(min: 8, max: 255),
            new Assert\NotCompromisedPassword(),
            new Assert\Type('string'),
            new Assert\Regex('/[A-Z]+/'),
        ];
    }
}
```

You can use the [CompoundConstraintTestCase](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Test/CompoundConstraintTestCase.php "Symfony\Component\Validator\Test\CompoundConstraintTestCase") class to check precisely which of the constraints failed to pass:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
```
// tests/Validator/PasswordRequirementsTest.php
namespace App\Tests\Validator;

use App\Validator\PasswordRequirements;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Test\CompoundConstraintTestCase;

/**
 * @extends CompoundConstraintTestCase<PasswordRequirements>
 */
class PasswordRequirementsTest extends CompoundConstraintTestCase
{
    public function createCompound(): Assert\Compound
    {
        return new PasswordRequirements();
    }

    public function testInvalidPassword(): void
    {
        $this->validateValue('azerty123');

        // check all constraints pass except for the
        // password leak and the uppercase letter checks
        $this->assertViolationsRaisedByCompound([
            new Assert\NotCompromisedPassword(),
            new Assert\Regex('/[A-Z]+/'),
        ]);
    }

    public function testValid(): void
    {
        $this->validateValue('VERYSTR0NGP4$$WORD#%!');

        $this->assertNoViolation();
    }
}
```

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. 

 TOC 

 Search 

 Version 

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: Check Code Performance in Dev, Test, Staging & Production](https://symfony.com/images/network/blackfire_03.png)](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)
[Check Code Performance in Dev, Test, Staging & Production](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)

[![Image 8: Be safe against critical risks to your projects and businesses](https://symfony.com/images/network/sfinsight_02.png)](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=safe)
[Be safe against critical risks to your projects and businesses](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=safe)

Symfony footer
--------------

![Image 9: Avatar of Matthias Gutjahr, a Symfony contributor](https://connect.symfony.com/api/images/6b057ac1-ec57-4117-9d30-3ec4d069d1d1.png?format=48x48)

Thanks **[Matthias Gutjahr](https://connect.symfony.com/profile/mattsches)** (**@mattsches**) for being a Symfony contributor

[**1** commit](https://github.com/symfony/symfony/commits?author=mattsches) • **2** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 10](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
[Celebrating 20 years of Symfony](https://symfony.com/20years)

**Symfony**™ is a trademark of Symfony SAS. [All rights reserved](https://symfony.com/trademark).

*   [What is Symfony?](https://symfony.com/what-is-symfony)

    *   [What is Symfony?](https://symfony.com/what-is-symfony)
    *   [Symfony at a Glance](https://symfony.com/at-a-glance)
    *   [Symfony Packages](https://symfony.com/packages)
    *   [Symfony Releases](https://symfony.com/releases)
    *   [Security Policy](https://symfony.com/doc/current/contributing/code/security.html)
    *   [Logo & Screenshots](https://symfony.com/logo)
    *   [Trademark & Licenses](https://symfony.com/license)
    *   [symfony1 Legacy](https://symfony.com/legacy)

*   [Learn Symfony](https://symfony.com/doc)

    *   [Symfony Docs](https://symfony.com/doc)
    *   [Symfony Book](https://symfony.com/book)
    *   [Reference](https://symfony.com/doc/current/reference/index.html)
    *   [Bundles](https://symfony.com/bundles)
    *   [Best Practices](https://symfony.com/doc/current/best_practices.html)
    *   [Training](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [eLearning Platform](https://university.sensiolabs.com/e-learning-platform?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [Certification](https://certification.symfony.com/)

*   [Screencasts](https://symfonycasts.com/)

    *   [Learn Symfony](https://symfonycasts.com/tracks/symfony)
    *   [Learn PHP](https://symfonycasts.com/tracks/php)
    *   [Learn JavaScript](https://symfonycasts.com/tracks/javascript)
    *   [Learn Drupal](https://symfonycasts.com/tracks/drupal)
    *   [Learn RESTful APIs](https://symfonycasts.com/tracks/rest)

*   [Community](https://symfony.com/community)

    *   [Symfony Community](https://symfony.com/community)
    *   [SymfonyConnect](https://connect.symfony.com/)
    *   [Events & Meetups](https://symfony.com/events/)
    *   [Projects using Symfony](https://symfony.com/projects)
    *   [Contributors](https://symfony.com/contributors)
    *   [Symfony Jobs](https://symfony.com/jobs)
    *   [Backers](https://symfony.com/backers)
    *   [Code of Conduct](https://symfony.com/doc/current/contributing/code_of_conduct/code_of_conduct.html)
    *   [Downloads Stats](https://symfony.com/stats/downloads)
    *   [Support](https://symfony.com/support)

*   [Blog](https://symfony.com/blog/)

    *   [All Blog Posts](https://symfony.com/blog/)
    *   [A Week of Symfony](https://symfony.com/blog/category/a-week-of-symfony)
    *   [Case Studies](https://symfony.com/blog/category/case-studies)
    *   [Cloud](https://symfony.com/blog/category/cloud)
    *   [Community](https://symfony.com/blog/category/community)
    *   [Conferences](https://symfony.com/blog/category/conferences)
    *   [Diversity](https://symfony.com/blog/category/diversity)
    *   [Living on the edge](https://symfony.com/blog/category/living-on-the-edge)
    *   [Releases](https://symfony.com/blog/category/releases)
    *   [Security Advisories](https://symfony.com/blog/category/security-advisories)
    *   [Symfony Insight](https://symfony.com/blog/category/symfony-insight)
    *   [Twig](https://symfony.com/blog/category/twig)
    *   [SensioLabs Blog](https://sensiolabs.com/blog?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

*   [Services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

    *   [SensioLabs services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [Train developers](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [Manage your project quality](https://insight.symfony.com/)
    *   [Improve your project performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)
    *   [Host Symfony projects](https://symfony.com/cloud/)

[Powered by](https://symfony.com/cloud/)

[](https://symfony.com/cloud/ "Upsun, a Platform-as-a-Service optimized for Symfony developers")

### Follow Symfony

[](https://github.com/symfony "Symfony on GitHub")[](https://symfony.com/slack "Symfony on Slack")[](https://twitter.com/symfony "Symfony on Twitter")[](https://mastodon.social/@symfony "Symfony on Mastodon")[](https://www.linkedin.com/company/symfony-sas/ "Symfony on LinkedIn")[](https://www.facebook.com/SymfonyFramework "Symfony on Facebook")[](https://www.youtube.com/symfonytv "Symfony on YouTube")[](https://bsky.app/profile/symfony.com "Symfony on BlueSky")[](https://www.threads.net/@symfony "Symfony on Threads")[](https://symfonycasts.com/ "Symfony Screencasts")[](https://feeds.feedburner.com/symfony/blog "Symfony Blog RSS")

Site appearance: 

CLOSE

Search Symfony Docs 

Search
