# Source: https://symfony.com/doc/8.0/serializer.html

Title: How to Use the Serializer (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/serializer.html

Markdown Content:
How to Use the Serializer (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/serializer.html#main-content)

[](https://symfony.com/)

Close

* About

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Community](https://symfony.com/community)
  * [News](https://symfony.com/blog/)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Support](https://symfony.com/support)

* Documentation

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Screencasts](https://symfonycasts.com/)
  * [Symfony Bundles](https://symfony.com/bundles)
  * [Symfony Cloud](https://symfony.com/doc/cloud/)
  * [Training](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)

* Services

  * [Upsun for Symfony](https://symfony.com/cloud/)Best platform to deploy Symfony apps
  * [SymfonyInsight](https://insight.symfony.com/)Automatic quality checks for your apps
  * [Symfony Certification](https://certification.symfony.com/)Prove your knowledge and boost your career
  * [SensioLabs](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)Professional services to help you with Symfony
  * [Blackfire](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)Profile and monitor performance of your apps

* Other
* [Blog](https://symfony.com/blog/)
* [Download](https://symfony.com/download)

sponsored by[](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_sponsoredby&utm_campaign=permanent_referral "SensioLabs, PHP services and software solutions for enterprise and community.")

1. [Home](https://symfony.com/)
2. [Documentation](https://symfony.com/doc)
3. How to Use the Serializer

 Search Symfony Docs

Version:

Table of Contents

* [Installation](https://symfony.com/doc/8.0/serializer.html#installation)
* [Serializing an Object](https://symfony.com/doc/8.0/serializer.html#serializing-an-object)
  * [Using the Serializer in Twig Templates](https://symfony.com/doc/8.0/serializer.html#using-the-serializer-in-twig-templates)

* [Deserializing an Object](https://symfony.com/doc/8.0/serializer.html#deserializing-an-object)
* [The Serialization Process: Normalizers and Encoders](https://symfony.com/doc/8.0/serializer.html#the-serialization-process-normalizers-and-encoders)
  * [Serializer Context](https://symfony.com/doc/8.0/serializer.html#serializer-context)

* [Serializing JSON Using Streams](https://symfony.com/doc/8.0/serializer.html#serializing-json-using-streams)
* [Serializing to or from PHP Arrays](https://symfony.com/doc/8.0/serializer.html#serializing-to-or-from-php-arrays)
* [Ignoring Properties](https://symfony.com/doc/8.0/serializer.html#ignoring-properties)
  * [Ignoring Attributes Using the Context](https://symfony.com/doc/8.0/serializer.html#ignoring-attributes-using-the-context)

* [Selecting Specific Properties](https://symfony.com/doc/8.0/serializer.html#selecting-specific-properties)
  * [Using the Serialization Context](https://symfony.com/doc/8.0/serializer.html#using-the-serialization-context)

* [Handling Arrays](https://symfony.com/doc/8.0/serializer.html#handling-arrays)
* [Deserializing Nested Structures](https://symfony.com/doc/8.0/serializer.html#deserializing-nested-structures)
* [Converting Property Names when Serializing and Deserializing](https://symfony.com/doc/8.0/serializer.html#converting-property-names-when-serializing-and-deserializing)
  * [CamelCase to snake_case](https://symfony.com/doc/8.0/serializer.html#camelcase-to-snake-case)
  * [snake_case to CamelCase](https://symfony.com/doc/8.0/serializer.html#snake-case-to-camelcase)

* [Serializer Normalizers](https://symfony.com/doc/8.0/serializer.html#serializer-normalizers)
  * [Built-in Normalizers](https://symfony.com/doc/8.0/serializer.html#built-in-normalizers)

* [Named Serializers](https://symfony.com/doc/8.0/serializer.html#named-serializers)
* [Debugging the Serializer](https://symfony.com/doc/8.0/serializer.html#debugging-the-serializer)
* [Advanced Serialization](https://symfony.com/doc/8.0/serializer.html#advanced-serialization)
  * [Skipping null Values](https://symfony.com/doc/8.0/serializer.html#skipping-null-values)
  * [Preserving Empty Objects](https://symfony.com/doc/8.0/serializer.html#preserving-empty-objects)
  * [Handling Uninitialized Properties](https://symfony.com/doc/8.0/serializer.html#handling-uninitialized-properties)
  * [Handling Circular References](https://symfony.com/doc/8.0/serializer.html#handling-circular-references)
  * [Handling Serialization Depth](https://symfony.com/doc/8.0/serializer.html#handling-serialization-depth)
  * [Using Callbacks to Serialize Properties with Object Instances](https://symfony.com/doc/8.0/serializer.html#using-callbacks-to-serialize-properties-with-object-instances)

* [Advanced Deserialization](https://symfony.com/doc/8.0/serializer.html#advanced-deserialization)
  * [Require all Properties](https://symfony.com/doc/8.0/serializer.html#require-all-properties)
  * [Collecting Type Errors While Denormalizing](https://symfony.com/doc/8.0/serializer.html#collecting-type-errors-while-denormalizing)
  * [Deserializing in an Existing Object](https://symfony.com/doc/8.0/serializer.html#deserializing-in-an-existing-object)
  * [Deserializing Interfaces and Abstract Classes](https://symfony.com/doc/8.0/serializer.html#deserializing-interfaces-and-abstract-classes)
  * [Deserializing Input Partially (Unwrapping)](https://symfony.com/doc/8.0/serializer.html#deserializing-input-partially-unwrapping)
  * [Handling Constructor Arguments](https://symfony.com/doc/8.0/serializer.html#handling-constructor-arguments)
  * [Recursive Denormalization and Type Safety](https://symfony.com/doc/8.0/serializer.html#recursive-denormalization-and-type-safety)
  * [Handling Boolean Values](https://symfony.com/doc/8.0/serializer.html#handling-boolean-values)

* [Extending Serialization for a Class](https://symfony.com/doc/8.0/serializer.html#extending-serialization-for-a-class)
* [Configuring the Metadata Cache](https://symfony.com/doc/8.0/serializer.html#configuring-the-metadata-cache)
* [Going Further with the Serializer](https://symfony.com/doc/8.0/serializer.html#going-further-with-the-serializer)

How to Use the Serializer
=========================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/serializer.rst)

Symfony provides a serializer to transform data structures from one format to PHP objects and the other way around.

This is most commonly used when building an API or communicating with third party APIs. The serializer can transform an incoming JSON request payload to a PHP object that is consumed by your application. Then, when generating the response, you can use the serializer to transform the PHP objects back to a JSON response.

It can also be used to, for instance, load CSV configuration data as PHP objects, or even to transform between formats (e.g. YAML to XML).

[Installation](https://symfony.com/doc/8.0/serializer.html#installation "Permalink to this headline")
-----------------------------------------------------------------------------------------------------

In applications using [Symfony Flex](https://symfony.com/doc/8.0/setup.html#symfony-flex), run this command to install the serializer [Symfony pack](https://symfony.com/doc/8.0/setup.html#symfony-packs) before using it:

1`$ composer require symfony/serializer-pack`

Note

The serializer pack also installs some commonly used optional dependencies of the Serializer component. When using this component outside the Symfony framework, you might want to start with the `symfony/serializer` package and install optional dependencies if you need them.

See also

A popular alternative to the Symfony Serializer component is the third-party library, [JMS serializer](https://github.com/schmittjoh/serializer).

[Serializing an Object](https://symfony.com/doc/8.0/serializer.html#serializing-an-object "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------

For this example, assume the following class exists in your project:

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

```
// src/Model/Person.php
namespace App\Model;

class Person
{
    public function __construct(
        private int $age,
        private string $name,
        private bool $sportsperson
    ) {
    }

    public function getAge(): int
    {
        return $this->age;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function isSportsperson(): bool
    {
        return $this->sportsperson;
    }
}
```

If you want to transform objects of this type into a JSON structure (e.g. to send them via an API response), get the `serializer` service by using the [SerializerInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/SerializerInterface.php "Symfony\Component\Serializer\SerializerInterface") parameter type:

Framework Use Standalone Use

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

```
// src/Controller/PersonController.php
namespace App\Controller;

use App\Model\Person;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Serializer\SerializerInterface;

class PersonController extends AbstractController
{
    public function index(SerializerInterface $serializer): Response
    {
        $person = new Person('Jane Doe', 39, false);

        $jsonContent = $serializer->serialize($person, 'json');
        // $jsonContent contains {"name":"Jane Doe","age":39,"sportsperson":false}

        return JsonResponse::fromJsonString($jsonContent);
    }
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
9
10
11
12
13

```
use App\Model\Person;
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

$encoders = [new JsonEncoder()];
$normalizers = [new ObjectNormalizer()];
$serializer = new Serializer($normalizers, $encoders);

$person = new Person('Jane Done', 39, false);

$jsonContent = $serializer->serialize($person, 'json');
// $jsonContent contains {"name":"Jane Doe","age":39,"sportsperson":false}
```

The first parameter of the [serialize()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Serializer.php#:~:text=function%20serialize "Symfony\Component\Serializer\Serializer::serialize()") is the object to be serialized and the second is used to choose the proper encoder (i.e. format), in this case the [JsonEncoder](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Encoder/JsonEncoder.php "Symfony\Component\Serializer\Encoder\JsonEncoder").

Tip

When your controller class extends `AbstractController` (like in the example above), you can simplify your controller by using the [json()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20json "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::json()") method to create a JSON response from an object using the Serializer:

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
class PersonController extends AbstractController
{
    public function index(): Response
    {
        $person = new Person('Jane Doe', 39, false);

        // when the Serializer is not available, this will use json_encode()
        return $this->json($person);
    }
}
```

### [Using the Serializer in Twig Templates](https://symfony.com/doc/8.0/serializer.html#using-the-serializer-in-twig-templates "Permalink to this headline")

You can also serialize objects in any Twig template using the `serialize` filter:

1`{{ person|serialize(format = 'json') }}`

See the [twig reference](https://symfony.com/doc/8.0/reference/twig_reference.html#reference-twig-filter-serialize) for more information.

[Deserializing an Object](https://symfony.com/doc/8.0/serializer.html#deserializing-an-object "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

APIs often also need to convert a formatted request body (e.g. JSON) to a PHP object. This process is called _deserialization_ (also known as "hydration"):

Framework Use Standalone Use

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

```
// src/Controller/PersonController.php
namespace App\Controller;

// ...
use Symfony\Component\HttpFoundation\Exception\BadRequestException;
use Symfony\Component\HttpFoundation\Request;

class PersonController extends AbstractController
{
    // ...

    public function create(Request $request, SerializerInterface $serializer): Response
    {
        if ('json' !== $request->getContentTypeFormat()) {
            throw new BadRequestException('Unsupported content format');
        }

        $jsonData = $request->getContent();
        $person = $serializer->deserialize($jsonData, Person::class, 'json');

        // ... do something with $person and return a response
    }
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
use App\Model\Person;
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

// ...
$jsonData = ...; // fetch JSON from the request
$person = $serializer->deserialize($jsonData, Person::class, 'json');
```

In this case, [deserialize()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Serializer.php#:~:text=function%20deserialize "Symfony\Component\Serializer\Serializer::deserialize()") needs three parameters:

1. The data to be decoded
2. The name of the class this information will be decoded to
3. The name of the encoder used to convert the data to an array (i.e. the input format)

When sending a request to this controller (e.g. `{"first_name":"John Doe","age":54,"sportsperson":true}`), the serializer will create a new instance of `Person` and sets the properties to the values from the given JSON.

Note

By default, additional attributes that are not mapped to the denormalized object will be ignored by the Serializer component. For instance, if a request to the above controller contains `{..., "city": "Paris"}`, the `city` field will be ignored. You can also throw an exception in these cases using the [serializer context](https://symfony.com/doc/8.0/serializer.html#serializer-context) you'll learn about later.

See also

You can also deserialize data into an existing object instance (e.g. when updating data). See [Deserializing in an Existing Object](https://symfony.com/doc/8.0/serializer.html#serializer-populate-existing-object).

[The Serialization Process: Normalizers and Encoders](https://symfony.com/doc/8.0/serializer.html#the-serialization-process-normalizers-and-encoders "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The serializer uses a two-step process when (de)serializing objects:

In both directions, data is always first converted to an array. This splits the process in two separate responsibilities:

Normalizers These classes convert **objects** into **arrays** and vice versa. They do the heavy lifting of finding out which class properties to serialize, what value they hold and what name they should have. Encoders Encoders convert **arrays** into a specific **format** and the other way around. Each encoder knows exactly how to parse and generate a specific format, for instance JSON or XML.
Internally, the `Serializer` class uses a sorted list of normalizers and one encoder for the specific format when (de)serializing an object.

There are several normalizers configured in the default `serializer` service. The most important normalizer is the [ObjectNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/ObjectNormalizer.php "Symfony\Component\Serializer\Normalizer\ObjectNormalizer"). This normalizer uses reflection and the [PropertyAccess component](https://symfony.com/doc/8.0/components/property_access.html) to transform between any object and an array. You'll learn more about [this and other normalizers](https://symfony.com/doc/8.0/serializer.html#serializer-normalizers) later.

The default serializer is also configured with some encoders, covering the common formats used by HTTP applications:

* [JsonEncoder](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Encoder/JsonEncoder.php "Symfony\Component\Serializer\Encoder\JsonEncoder")
* [XmlEncoder](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Encoder/XmlEncoder.php "Symfony\Component\Serializer\Encoder\XmlEncoder")
* [CsvEncoder](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Encoder/CsvEncoder.php "Symfony\Component\Serializer\Encoder\CsvEncoder")
* [YamlEncoder](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Encoder/YamlEncoder.php "Symfony\Component\Serializer\Encoder\YamlEncoder")

Read more about these encoders and their configuration in [Serializer Encoders](https://symfony.com/doc/8.0/serializer/encoders.html).

Tip

The [API Platform](https://api-platform.com/) project provides encoders for more advanced formats:

* [JSON-LD](https://json-ld.org/) along with the [Hydra Core Vocabulary](https://www.hydra-cg.com/)
* [OpenAPI](https://www.openapis.org/) v2 (formerly Swagger) and v3
* [GraphQL](https://graphql.org/)
* [JSON:API](https://jsonapi.org/)
* [HAL](https://stateless.group/hal_specification.html)

### [Serializer Context](https://symfony.com/doc/8.0/serializer.html#serializer-context "Permalink to this headline")

The serializer, and its normalizers and encoders, are configured through the _serializer context_. This context can be configured in multiple places:

* [Globally through the framework configuration](https://symfony.com/doc/8.0/serializer.html#serializer-default-context)
* [While serializing/deserializing](https://symfony.com/doc/8.0/serializer.html#serializer-context-while-serializing-deserializing)
* [For a specific property](https://symfony.com/doc/8.0/serializer.html#serializer-using-context-builders)

You can use all three options at the same time. When the same setting is configured in multiple places, the latter in the list above will override the previous one (e.g. the setting on a specific property overrides the one configured globally).

#### [Configure a Default Context](https://symfony.com/doc/8.0/serializer.html#configure-a-default-context "Permalink to this headline")

You can configure a default context in the framework configuration, for instance to disallow extra fields while deserializing:

YAML PHP Standalone Use

1
2
3
4
5

```
# config/packages/serializer.yaml
framework:
    serializer:
        default_context:
            allow_extra_attributes: false
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

```
// config/packages/serializer.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'serializer' => [
            'default_context' => [
                'allow_extra_attributes' => false,
            ],
        ],
    ],
]);
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

```
use Symfony\Component\Serializer\NameConverter\CamelCaseToSnakeCaseNameConverter;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;

// ...
$normalizers = [
    new ObjectNormalizer(null, null, null, null, null, null, [
        'allow_extra_attributes' => false,
    ]),
];
$serializer = new Serializer($normalizers, $encoders);
```

#### [Pass Context while Serializing/Deserializing](https://symfony.com/doc/8.0/serializer.html#pass-context-while-serializing-deserializing "Permalink to this headline")

You can also configure the context for a single call to `serialize()`/`deserialize()`. For instance, you can skip properties with a `null` value only for one serialize call:

1
2
3
4
5
6
7
8

```
use Symfony\Component\Serializer\Normalizer\AbstractObjectNormalizer;

// ...
$serializer->serialize($person, 'json', [
    AbstractObjectNormalizer::SKIP_NULL_VALUES => true
]);

// next calls to serialize() will NOT skip null values
```

##### [Using Context Builders](https://symfony.com/doc/8.0/serializer.html#using-context-builders "Permalink to this headline")

You can use "context builders" to help define the (de)serialization context. Context builders are PHP objects that provide autocompletion, validation, and documentation of context options:

1
2
3
4
5

```
use Symfony\Component\Serializer\Context\Normalizer\DateTimeNormalizerContextBuilder;

$contextBuilder = (new DateTimeNormalizerContextBuilder())
    ->withFormat('Y-m-d H:i:s');
$serializer->serialize($something, 'json', $contextBuilder->toArray());
```

Each normalizer/encoder has its related context builder. To create a more complex (de)serialization context, you can chain them using the `withContext()` method:

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
use Symfony\Component\Serializer\Context\Encoder\CsvEncoderContextBuilder;
use Symfony\Component\Serializer\Context\Normalizer\ObjectNormalizerContextBuilder;

$initialContext = [
    'custom_key' => 'custom_value',
];

$contextBuilder = (new ObjectNormalizerContextBuilder())
    ->withContext($initialContext)
    ->withGroups(['group1', 'group2']);

$contextBuilder = (new CsvEncoderContextBuilder())
    ->withContext($contextBuilder)
    ->withDelimiter(';');

$serializer->serialize($something, 'csv', $contextBuilder->toArray());
```

See also

You can also [create your context builders](https://symfony.com/doc/8.0/serializer/custom_context_builders.html) to have autocompletion, validation, and documentation for your custom context values.

#### [Configure Context on a Specific Property](https://symfony.com/doc/8.0/serializer.html#configure-context-on-a-specific-property "Permalink to this headline")

At last, you can also configure context values on a specific object property. For instance, to configure the datetime format:

Attributes YAML XML

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

```
// src/Model/Person.php

// ...
use Symfony\Component\Serializer\Attribute\Context;
use Symfony\Component\Serializer\Normalizer\DateTimeNormalizer;

class Person
{
    #[Context([DateTimeNormalizer::FORMAT_KEY => 'Y-m-d'])]
    public \DateTimeImmutable $createdAt;

    // ...
}
```

1
2
3
4
5
6

```
# config/serializer/person.yaml
App\Model\Person:
    attributes:
        createdAt:
            contexts:
                - context: { datetime_format: 'Y-m-d' }
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
<!-- config/serializer/person.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\Person">
        <attribute name="createdAt">
            <context>
                <entry name="datetime_format">Y-m-d</entry>
            </context>
        </attribute>
    </class>
</serializer>
```

Note

When using YAML or XML, the mapping files must be placed in one of these locations:

* All `*.yaml` and `*.xml` files in the `config/serializer/` directory.
* The `serialization.yaml` or `serialization.xml` file in the `Resources/config/` directory of a bundle;
* All `*.yaml` and `*.xml` files in the `Resources/config/serialization/` directory of a bundle.

Tip

Symfony provides a JSON schema for serializer mapping files that enables autocompletion and validation in IDEs like PhpStorm. Add the following `$schema` key at the beginning of your YAML files to enable this feature:

1
2
3
4
5

```
# config/serializer/person.yaml
'$schema': https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.json
App\Model\Person:
    attributes:
        # your IDE will now provide autocompletion here...
```

You can also specify a context specific to normalization or denormalization:

Attributes YAML XML

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
// src/Model/Person.php

// ...
use Symfony\Component\Serializer\Attribute\Context;
use Symfony\Component\Serializer\Normalizer\DateTimeNormalizer;

class Person
{
    #[Context(
        normalizationContext: [DateTimeNormalizer::FORMAT_KEY => 'Y-m-d'],
        denormalizationContext: [DateTimeNormalizer::FORMAT_KEY => \DateTime::RFC3339],
    )]
    public \DateTimeImmutable $createdAt;

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
# config/serializer/person.yaml
App\Model\Person:
    attributes:
        createdAt:
            contexts:
                - normalization_context: { datetime_format: 'Y-m-d' }
                  denormalization_context: { datetime_format: !php/const \DateTime::RFC3339 }
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
<!-- config/serializer/person.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\Person">
        <attribute name="createdAt">
            <normalization-context>
                <entry name="datetime_format">Y-m-d</entry>
            </normalization-context>

            <denormalization-context>
                <entry name="datetime_format">Y-m-d\TH:i:sP</entry>
            </denormalization-context>
        </attribute>
    </class>
</serializer>
```

You can also restrict the usage of a context to some [groups](https://symfony.com/doc/8.0/serializer.html#serializer-groups-attribute):

Attributes YAML XML

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
// src/Model/Person.php

// ...
use Symfony\Component\Serializer\Attribute\Context;
use Symfony\Component\Serializer\Attribute\Groups;
use Symfony\Component\Serializer\Normalizer\DateTimeNormalizer;

class Person
{
    #[Groups(['extended'])]
    #[Context([DateTimeNormalizer::FORMAT_KEY => \DateTime::RFC3339])]
    #[Context(
        context: [DateTimeNormalizer::FORMAT_KEY => \DateTime::RFC3339_EXTENDED],
        groups: ['extended'],
    )]
    public \DateTimeImmutable $createdAt;

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
9

```
# config/serializer/person.yaml
App\Model\Person:
    attributes:
        createdAt:
            groups: [extended]
            contexts:
                - context: { datetime_format: !php/const \DateTime::RFC3339 }
                - context: { datetime_format: !php/const \DateTime::RFC3339_EXTENDED }
                  groups: [extended]
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
21

```
<!-- config/serializer/person.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\Person">
        <attribute name="createdAt">
            <group>extended</group>

            <context>
                <entry name="datetime_format">Y-m-d\TH:i:sP</entry>
            </context>
            <context>
                <entry name="datetime_format">Y-m-d\TH:i:s.vP</entry>
                <group>extended</group>
            </context>
        </attribute>
    </class>
</serializer>
```

The attribute can be repeated as much as needed on a single property. Context without group is always applied first. Then context for the matching groups are merged in the provided order.

If you repeat the same context in multiple properties, consider using the `#[Context]` attribute on your class to apply that context configuration to all the properties of the class:

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

```
namespace App\Model;

use Symfony\Component\Serializer\Attribute\Context;
use Symfony\Component\Serializer\Normalizer\DateTimeNormalizer;

#[Context([DateTimeNormalizer::FORMAT_KEY => \DateTime::RFC3339])]
#[Context(
    context: [DateTimeNormalizer::FORMAT_KEY => \DateTime::RFC3339_EXTENDED],
    groups: ['extended'],
)]
class Person
{
    // ...
}
```

[Serializing JSON Using Streams](https://symfony.com/doc/8.0/serializer.html#serializing-json-using-streams "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------

Symfony can encode PHP data structures to JSON streams and decode JSON streams back into PHP data structures.

To do this, it relies on the [JsonStreamer component](https://symfony.com/doc/8.0/serializer/streaming_json.html), which is designed for high efficiency and can process large JSON data incrementally, without needing to load the entire content into memory.

When deciding between the Serializer component and the JsonStreamer component, consider the following:

* **Serializer Component**: Best suited for use cases that require flexibility, such as dynamically manipulating object structures using normalizers and denormalizers, or handling complex objects with multiple serialization formats. It also supports output formats beyond JSON (including your own custom ones).
* **JsonStreamer Component**: Best suited for simple objects and scenarios that demand high performance and low memory usage. It's particularly effective for processing very large JSON datasets or when streaming JSON in real-time without loading the entire dataset into memory.

The choice depends on your specific use case. The JsonStreamer component is tailored for performance and memory efficiency, whereas the Serializer component provides greater flexibility and broader format support.

Read more about [streaming JSON](https://symfony.com/doc/8.0/serializer/streaming_json.html).

[Serializing to or from PHP Arrays](https://symfony.com/doc/8.0/serializer.html#serializing-to-or-from-php-arrays "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------

The default [Serializer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Serializer.php "Symfony\Component\Serializer\Serializer") can also be used to only perform one step of the [two step serialization process](https://symfony.com/doc/8.0/serializer.html#serializer-process) by using the respective interface:

Framework Use Standalone Use

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

```
use Symfony\Component\Serializer\Encoder\DecoderInterface;
use Symfony\Component\Serializer\Encoder\EncoderInterface;
use Symfony\Component\Serializer\Normalizer\DenormalizerInterface;
use Symfony\Component\Serializer\Normalizer\NormalizerInterface;
// ...

class PersonController extends AbstractController
{
    public function index(DenormalizerInterface&NormalizerInterface $serializer): Response
    {
        $person = new Person('Jane Doe', 39, false);

        // use normalize() to convert a PHP object to an array
        $personArray = $serializer->normalize($person, 'json');

        // ...and denormalize() to convert an array back to a PHP object
        $personCopy = $serializer->denormalize($personArray, Person::class);

        // ...
    }

    public function json(DecoderInterface&EncoderInterface $serializer): Response
    {
        $data = ['name' => 'Jane Doe'];

        // use encode() to transform PHP arrays into another format
        $json = $serializer->encode($data, 'json');

        // ...and decode() to transform any format to just PHP arrays (instead of objects)
        $data = $serializer->decode('{"name":"Charlie Doe"}', 'json');
        // $data contains ['name' => 'Charlie Doe']
    }
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

```
use App\Model\Person;
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

$encoders = [new JsonEncoder()];
$normalizers = [new ObjectNormalizer()];
$serializer = new Serializer($normalizers, $encoders);

// use normalize() to convert a PHP object to an array
$personArray = $serializer->normalize($person, 'json');

// ...and denormalize() to convert an array back to a PHP object
$personCopy = $serializer->denormalize($personArray, Person::class);

$data = ['name' => 'Jane Doe'];

// use encode() to transform PHP arrays into another format
$json = $serializer->encode($data, 'json');

// ...and decode() to transform any format to just PHP arrays (instead of objects)
$data = $serializer->decode('{"name":"Charlie Doe"}', 'json');
// $data contains ['name' => 'Charlie Doe']
```

[Ignoring Properties](https://symfony.com/doc/8.0/serializer.html#ignoring-properties "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------

The `ObjectNormalizer` normalizes _all_ properties of an object and all methods starting with `get*()`, `has*()`, `is*()` and `can*()`. Some properties or methods should never be serialized. You can exclude them using the `#[Ignore]` attribute:

Attributes YAML XML

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
// src/Model/Person.php
namespace App\Model;

use Symfony\Component\Serializer\Attribute\Ignore;

class Person
{
    // ...

    #[Ignore]
    public function isPotentiallySpamUser(): bool
    {
        // ...
    }
}
```

1
2
3
4

```
App\Model\Person:
    attributes:
        potentiallySpamUser:
            ignore: true
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

```
<?xml version="1.0" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\Person">
        <attribute name="potentiallySpamUser" ignore="true"/>
    </class>
</serializer>
```

The `potentiallySpamUser` property will now never be serialized:

Framework Use Standalone Use

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

```
use App\Model\Person;

// ...
$person = new Person('Jane Doe', 32, false);
$json = $serializer->serialize($person, 'json');
// $json contains {"name":"Jane Doe","age":32,"sportsperson":false}

$person1 = $serializer->deserialize(
    '{"name":"Jane Doe","age":32,"sportsperson":false","potentiallySpamUser":false}',
    Person::class,
    'json'
);
// the "potentiallySpamUser" value is ignored
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
21
22
23
24
25
26

```
use App\Model\Person;
use Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactory;
use Symfony\Component\Serializer\Mapping\Loader\AttributeLoader;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

// ...

// you need to pass a class metadata factory with a loader to the
// ObjectNormalizer when reading mapping information like Ignore or Groups.
// E.g. when using PHP attributes:
$classMetadataFactory = new ClassMetadataFactory(new AttributeLoader());
$normalizers = [new ObjectNormalizer($classMetadataFactory)];

$serializer = new Serializer($normalizers, $encoders);

$person = new Person('Jane Doe', 32, false);
$json = $serializer->serialize($person, 'json');
// $json contains {"name":"Jane Doe","age":32,"sportsperson":false}

$person1 = $serializer->deserialize(
    '{"name":"Jane Doe","age":32,"sportsperson":false","potentiallySpamUser":false}',
    Person::class,
    'json'
);
// the "potentiallySpamUser" value is ignored
```

### [Ignoring Attributes Using the Context](https://symfony.com/doc/8.0/serializer.html#ignoring-attributes-using-the-context "Permalink to this headline")

You can also pass an array of attribute names to ignore at runtime using the `ignored_attributes` context options:

1
2
3
4
5
6
7
8
9

```
use Symfony\Component\Serializer\Normalizer\AbstractNormalizer;

// ...
$person = new Person('Jane Doe', 32, false);
$json = $serializer->serialize($person, 'json',
[
    AbstractNormalizer::IGNORED_ATTRIBUTES => ['age'],
]);
// $json contains {"name":"Jane Doe","sportsperson":false}
```

However, this can quickly become unmaintainable if used excessively. See the next section about _serialization groups_ for a better solution.

[Selecting Specific Properties](https://symfony.com/doc/8.0/serializer.html#selecting-specific-properties "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------

Instead of excluding a property or method in all situations, you might need to exclude some properties in one place, but serialize them in another. Groups are a handy way to achieve this.

You can add the `#[Groups]` attribute to your class:

Attributes YAML XML

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
// src/Model/Person.php
namespace App\Model;

use Symfony\Component\Serializer\Attribute\Groups;

class Person
{
    #[Groups(["admin-view"])]
    private int $age;

    #[Groups(["public-view"])]
    private string $name;

    #[Groups(["public-view"])]
    private bool $sportsperson;

    private string $email;

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
9
10

```
# config/serializer/person.yaml
App\Model\Person:
    attributes:
        age:
            groups: ['admin-view']
        name:
            groups: ['public-view']
        sportsperson:
            groups: ['public-view']
        # email has no groups defined
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
<!-- config/serializer/person.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\Person">
        <attribute name="age">
            <group>admin-view</group>
        </attribute>
        <attribute name="name">
            <group>public-view</group>
        </attribute>
        <attribute name="sportsperson">
            <group>public-view</group>
        </attribute>
        <!-- email has no groups defined -->
    </class>
</serializer>
```

You can now choose which groups to use when serializing:

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

```
$json = $serializer->serialize(
    $person,
    'json',
    ['groups' => 'public-view']
);
// $json contains {"name":"Jane Doe","sportsperson":false}

// you can also pass an array of groups
$json = $serializer->serialize(
    $person,
    'json',
    ['groups' => ['public-view', 'admin-view']]
);
// $json contains {"name":"Jane Doe","age":32,"sportsperson":false}

// or use the special "*" value to serialize all properties
// (including those without any groups)
$json = $serializer->serialize(
    $person,
    'json',
    ['groups' => '*']
);
// $json contains {"name":"Jane Doe","age":32,"sportsperson":false,"email":"jane.doe@exemple.com"}
```

### [Using the Serialization Context](https://symfony.com/doc/8.0/serializer.html#using-the-serialization-context "Permalink to this headline")

At last, you can also use the `attributes` context option to select properties at runtime:

1
2
3
4
5
6
7

```
use Symfony\Component\Serializer\Normalizer\AbstractNormalizer;
// ...

$json = $serializer->serialize($person, 'json', [
    AbstractNormalizer::ATTRIBUTES => ['name', 'company' => ['name']]
]);
// $json contains {"name":"Dunglas","company":{"name":"Les-Tilleuls.coop"}}
```

Only attributes that are [not ignored](https://symfony.com/doc/8.0/serializer.html#serializer_ignoring-attributes) are available. If serialization groups are set, only attributes allowed by those groups can be used.

[Handling Arrays](https://symfony.com/doc/8.0/serializer.html#handling-arrays "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------

The serializer is capable of handling arrays of objects. Serializing arrays works just like serializing a single object:

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
use App\Model\Person;

// ...
$person1 = new Person('Jane Doe', 39, false);
$person2 = new Person('John Smith', 52, true);

$persons = [$person1, $person2];
$jsonContent = $serializer->serialize($persons, 'json');

// $jsonContent contains [{"name":"Jane Doe","age":39,"sportsman":false},{"name":"John Smith","age":52,"sportsman":true}]
```

To deserialize a list of objects, you have to append `[]` to the type parameter:

1
2
3
4

```
// ...

$jsonData = ...; // the serialized JSON data from the previous example
$persons = $serializer->deserialize($JsonData, Person::class.'[]', 'json');
```

For nested classes, you have to add a PHPDoc type to the property, constructor or setter:

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

```
// src/Model/UserGroup.php
namespace App\Model;

class UserGroup
{
    /**
     * @param Person[] $members
     */
    public function __construct(
        private array $members,
    ) {
    }

    // or if you're using a setter

    /**
     * @param Person[] $members
     */
    public function setMembers(array $members): void
    {
        $this->members = $members;
    }

    // ...
}
```

Tip

The Serializer also supports array types used in static analysis, like `list<Person>` and `array<Person>`. Make sure the `phpstan/phpdoc-parser` and `phpdocumentor/reflection-docblock` packages are installed (these are part of the `symfony/serializer-pack`).

[Deserializing Nested Structures](https://symfony.com/doc/8.0/serializer.html#deserializing-nested-structures "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------

Some APIs might provide verbose nested structures that you want to flatten in the PHP object. For instance, imagine a JSON response like this:

1
2
3
4
5
6
7
8
9

```
{
    "id": "123",
    "profile": {
        "username": "jdoe",
        "personal_information": {
            "full_name": "Jane Doe"
        }
    }
}
```

You may wish to serialize this information to a single PHP object like:

1
2
3
4
5
6

```
class Person
{
    private int $id;
    private string $username;
    private string $fullName;
}
```

Use the `#[SerializedPath]` to specify the path of the nested property using [valid PropertyAccess syntax](https://symfony.com/doc/8.0/components/property_access.html):

Attributes YAML XML

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

```
namespace App\Model;

use Symfony\Component\Serializer\Attribute\SerializedPath;

class Person
{
    private int $id;

    #[SerializedPath('[profile][username]')]
    private string $username;

    #[SerializedPath('[profile][personal_information][full_name]')]
    private string $fullName;
}
```

1
2
3
4
5
6

```
App\Model\Person:
    attributes:
        username:
            serialized_path: '[profile][username]'
        fullName:
            serialized_path: '[profile][personal_information][full_name]'
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
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\Person">
        <attribute name="username" serialized-path="[profile][username]"/>
        <attribute name="fullName" serialized-path="[profile][personal_information][full_name]"/>
    </class>
</serializer>
```

Warning

The `SerializedPath` cannot be used in combination with a `SerializedName` for the same property.

The `#[SerializedPath]` attribute also applies to the serialization of a PHP object:

1
2
3
4
5
6

```
use App\Model\Person;
// ...

$person = new Person(123, 'jdoe', 'Jane Doe');
$jsonContent = $serializer->serialize($person, 'json');
// $jsonContent contains {"id":123,"profile":{"username":"jdoe","personal_information":{"full_name":"Jane Doe"}}}
```

[Converting Property Names when Serializing and Deserializing](https://symfony.com/doc/8.0/serializer.html#converting-property-names-when-serializing-and-deserializing "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes serialized attributes must be named differently than properties or getter/setter methods of PHP classes. This can be achieved using name converters.

The serializer service uses the [MetadataAwareNameConverter](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/NameConverter/MetadataAwareNameConverter.php "Symfony\Component\Serializer\NameConverter\MetadataAwareNameConverter"). With this name converter, you can change the name of an attribute using the `#[SerializedName]` attribute:

Attributes YAML XML

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
// src/Model/Person.php
namespace App\Model;

use Symfony\Component\Serializer\Attribute\SerializedName;

class Person
{
    #[SerializedName('customer_name')]
    private string $name;

    // ...
}
```

1
2
3
4
5

```
# config/serializer/person.yaml
App\Entity\Person:
    attributes:
        name:
            serialized_name: customer_name
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
<!-- config/serializer/person.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Entity\Person">
        <attribute name="name" serialized-name="customer_name"/>
    </class>
</serializer>
```

This custom mapping is used to convert property names when serializing and deserializing objects:

Framework Use Standalone Use

1
2
3
4

```
// ...

$json = $serializer->serialize($person, 'json');
// $json contains {"customer_name":"Jane Doe", ...}
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
21
22

```
use App\Model\Person;
use Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactory;
use Symfony\Component\Serializer\Mapping\Loader\AttributeLoader;
use Symfony\Component\Serializer\NameConverter\MetadataAwareNameConverter;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

// ...

// Configure a loader to retrieve mapping information like SerializedName.
// E.g. when using PHP attributes:
$classMetadataFactory = new ClassMetadataFactory(new AttributeLoader());
$nameConverter = new MetadataAwareNameConverter($classMetadataFactory);
$normalizers = [
    new ObjectNormalizer($classMetadataFactory, $nameConverter),
];

$serializer = new Serializer($normalizers, $encoders);

$person = new Person('Jane Doe', 32, false);
$json = $serializer->serialize($person, 'json');
// $json contains {"customer_name":"Jane Doe", ...}
```

See also

You can also create a custom name converter class. Read more about this in [How to Create your Custom Name Converter](https://symfony.com/doc/8.0/serializer/custom_name_converter.html).

### [CamelCase to snake_case](https://symfony.com/doc/8.0/serializer.html#camelcase-to-snake-case "Permalink to this headline")

In many formats, it's common to use underscores to separate words (also known as snake_case). However, in Symfony applications is common to use camelCase to name properties.

Symfony provides a built-in name converter designed to transform between snake_case and CamelCased styles during serialization and deserialization processes. You can use it instead of the metadata aware name converter by setting the `name_converter` setting to `serializer.name_converter.camel_case_to_snake_case`:

YAML PHP Standalone Use

1
2
3
4

```
# config/packages/serializer.yaml
framework:
    serializer:
        name_converter: 'serializer.name_converter.camel_case_to_snake_case'
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

```
// config/packages/serializer.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'serializer' => [
            'name_converter' => 'serializer.name_converter.camel_case_to_snake_case',
        ],
    ],
]);
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
use Symfony\Component\Serializer\NameConverter\CamelCaseToSnakeCaseNameConverter;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;

// ...
$normalizers = [
    new ObjectNormalizer(null, new CamelCaseToSnakeCaseNameConverter()),
];
$serializer = new Serializer($normalizers, $encoders);
```

### [snake_case to CamelCase](https://symfony.com/doc/8.0/serializer.html#snake-case-to-camelcase "Permalink to this headline")

In Symfony applications, it is common to use camelCase for naming properties. However some packages may follow a snake_case convention.

Symfony provides a built-in name converter designed to transform between CamelCase and snake_case styles during serialization and deserialization processes. You can use it instead of the metadata-aware name converter by setting the `name_converter` setting to `serializer.name_converter.snake_case_to_camel_case`:

YAML PHP Standalone Use

1
2
3
4

```
# config/packages/serializer.yaml
framework:
    serializer:
        name_converter: 'serializer.name_converter.snake_case_to_camel_case'
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

```
// config/packages/serializer.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'serializer' => [
            'name_converter' => 'serializer.name_converter.snake_case_to_camel_case',
        ],
    ],
]);
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
use Symfony\Component\Serializer\NameConverter\SnakeCaseToCamelCaseNameConverter;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;

// ...
$normalizers = [
    new ObjectNormalizer(null, new SnakeCaseToCamelCaseNameConverter()),
];
$serializer = new Serializer($normalizers, $encoders);
```

[Serializer Normalizers](https://symfony.com/doc/8.0/serializer.html#serializer-normalizers "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

By default, the serializer service is configured with the following normalizers (in order of priority):

[UnwrappingDenormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/UnwrappingDenormalizer.php "Symfony\Component\Serializer\Normalizer\UnwrappingDenormalizer") Can be used to only denormalize a part of the input, read more about this [later in this article](https://symfony.com/doc/8.0/serializer.html#serializer-unwrapping-denormalizer). [ProblemNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/ProblemNormalizer.php "Symfony\Component\Serializer\Normalizer\ProblemNormalizer") Normalizes [FlattenException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ErrorHandler/Exception/FlattenException.php "Symfony\Component\ErrorHandler\Exception\FlattenException") errors according to the API Problem spec [RFC 7807](https://tools.ietf.org/html/rfc7807). [UidNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/UidNormalizer.php "Symfony\Component\Serializer\Normalizer\UidNormalizer")
Normalizes objects that extend [AbstractUid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/AbstractUid.php "Symfony\Component\Uid\AbstractUid").

The default normalization format for objects that implement [Uuid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/Uuid.php "Symfony\Component\Uid\Uuid") is the [RFC 4122](https://tools.ietf.org/html/rfc4122) format (example: `d9e7a184-5d5b-11ea-a62a-3499710062d0`). The default normalization format for objects that implement [Ulid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/Ulid.php "Symfony\Component\Uid\Ulid") is the Base 32 format (example: `01E439TP9XJZ9RPFH3T1PYBCR8`). You can change the string format by setting the serializer context option `UidNormalizer::NORMALIZATION_FORMAT_KEY` to `UidNormalizer::NORMALIZATION_FORMAT_BASE58`, `UidNormalizer::NORMALIZATION_FORMAT_BASE32` or `UidNormalizer::NORMALIZATION_FORMAT_RFC4122`.

Also it can denormalize `uuid` or `ulid` strings to [Uuid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/Uuid.php "Symfony\Component\Uid\Uuid") or [Ulid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/Ulid.php "Symfony\Component\Uid\Ulid"). The format does not matter.

[DateTimeNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/DateTimeNormalizer.php "Symfony\Component\Serializer\Normalizer\DateTimeNormalizer")
This normalizes between [DateTimeInterface](https://secure.php.net/manual/en/class.datetimeinterface.php "DateTimeInterface") objects (e.g. [DateTime](https://secure.php.net/manual/en/class.datetime.php "DateTime") and [DateTimeImmutable](https://secure.php.net/manual/en/class.datetimeimmutable.php "DateTimeImmutable")) and strings, integers or floats.

[DateTime](https://secure.php.net/manual/en/class.datetime.php "DateTime") and [DateTimeImmutable](https://secure.php.net/manual/en/class.datetimeimmutable.php "DateTimeImmutable")) into strings, integers or floats. By default, it converts them to strings using the [RFC 3339](https://tools.ietf.org/html/rfc3339#section-5.8) format. Use `DateTimeNormalizer::FORMAT_KEY` and `DateTimeNormalizer::TIMEZONE_KEY` to change the format.

To always create [DateTime](https://secure.php.net/manual/en/class.datetime.php "DateTime") and [DateTimeImmutable](https://secure.php.net/manual/en/class.datetimeimmutable.php "DateTimeImmutable") objects using the time zone specified in the context, set the `DateTimeNormalizer::FORCE_TIMEZONE_KEY` context option to `true`. This forces the context time zone and ignores any time zone provided in the input.

To convert the objects to integers or floats, set the serializer context option `DateTimeNormalizer::CAST_KEY` to `int` or `float`.

[ConstraintViolationListNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/ConstraintViolationListNormalizer.php "Symfony\Component\Serializer\Normalizer\ConstraintViolationListNormalizer") This normalizer converts objects that implement [ConstraintViolationListInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/ConstraintViolationListInterface.php "Symfony\Component\Validator\ConstraintViolationListInterface") into a list of errors according to the [RFC 7807](https://tools.ietf.org/html/rfc7807) standard. [DateTimeZoneNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/DateTimeZoneNormalizer.php "Symfony\Component\Serializer\Normalizer\DateTimeZoneNormalizer") This normalizer converts between [DateTimeZone](https://secure.php.net/manual/en/class.datetimezone.php "DateTimeZone") objects and strings that represent the name of the timezone according to the [list of PHP timezones](https://www.php.net/manual/en/timezones.php). [DateIntervalNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/DateIntervalNormalizer.php "Symfony\Component\Serializer\Normalizer\DateIntervalNormalizer") This normalizes between [DateInterval](https://secure.php.net/manual/en/class.dateinterval.php "DateInterval") objects and strings. By default, the `P%yY%mM%dDT%hH%iM%sS` format is used. Use the `DateIntervalNormalizer::FORMAT_KEY` option to change this. [FormErrorNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/FormErrorNormalizer.php "Symfony\Component\Serializer\Normalizer\FormErrorNormalizer")
This normalizer works with classes that implement [FormInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php "Symfony\Component\Form\FormInterface").

It will get errors from the form and normalize them according to the API Problem spec [RFC 7807](https://tools.ietf.org/html/rfc7807).

[TranslatableNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/TranslatableNormalizer.php "Symfony\Component\Serializer\Normalizer\TranslatableNormalizer")
This normalizer converts objects implementing [TranslatableInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Contracts/Translation/TranslatableInterface.php "Symfony\Contracts\Translation\TranslatableInterface") to a translated string using the [translator](https://symfony.com/doc/8.0/translation.html).

You can define the locale to use to translate the object by setting the `TranslatableNormalizer::NORMALIZATION_LOCALE_KEY` context option.

[BackedEnumNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/BackedEnumNormalizer.php "Symfony\Component\Serializer\Normalizer\BackedEnumNormalizer")
This normalizer converts between [BackedEnum](https://secure.php.net/manual/en/class.backedenum.php "BackedEnum") enums and strings or integers.

By default, an exception is thrown when data is not a valid backed enumeration. If you want `null` instead, you can set the `BackedEnumNormalizer::ALLOW_INVALID_VALUES` option.

[NumberNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/NumberNormalizer.php "Symfony\Component\Serializer\Normalizer\NumberNormalizer") This normalizer converts between [Number](https://secure.php.net/manual/en/class.bcmath-number.php "BcMath\Number") or [GMP](https://secure.php.net/manual/en/class.gmp.php "GMP") objects and strings or integers. [DataUriNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/DataUriNormalizer.php "Symfony\Component\Serializer\Normalizer\DataUriNormalizer") This normalizer converts between [SplFileInfo](https://secure.php.net/manual/en/class.splfileinfo.php "SplFileInfo") objects and a [data URI](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) string (`data:...`) such that files can be embedded into serialized data. [JsonSerializableNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/JsonSerializableNormalizer.php "Symfony\Component\Serializer\Normalizer\JsonSerializableNormalizer")
This normalizer works with classes that implement [JsonSerializable](https://secure.php.net/manual/en/class.jsonserializable.php "JsonSerializable").

It will call the [jsonSerialize()](https://secure.php.net/manual/en/jsonserializable.jsonserialize.php "JsonSerializable::jsonSerialize()") method and then further normalize the result. This means that nested [JsonSerializable](https://secure.php.net/manual/en/class.jsonserializable.php "JsonSerializable") classes will also be normalized.

This normalizer is particularly helpful when you want to gradually migrate from an existing codebase using simple [json_encode](https://secure.php.net/manual/en/function.json-encode.php "json_encode") to the Symfony Serializer by allowing you to mix which normalizers are used for which classes.

Unlike with [json_encode](https://secure.php.net/manual/en/function.json-encode.php "json_encode") circular references can be handled.

[ArrayDenormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/ArrayDenormalizer.php "Symfony\Component\Serializer\Normalizer\ArrayDenormalizer")
This denormalizer converts an array of arrays to an array of objects (with the given type). See [Handling Arrays](https://symfony.com/doc/8.0/serializer.html#serializer-handling-arrays).

Use [PropertyInfoExtractor](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/PropertyInfo/PropertyInfoExtractor.php "Symfony\Component\PropertyInfo\PropertyInfoExtractor") to provide hints with annotations like `@var Person[]`:

Standalone Use

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

```
use Symfony\Component\PropertyInfo\Extractor\PhpDocExtractor;
use Symfony\Component\PropertyInfo\Extractor\ReflectionExtractor;
use Symfony\Component\PropertyInfo\PropertyInfoExtractor;
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactory;
use Symfony\Component\Serializer\Mapping\Loader\AttributeLoader;
use Symfony\Component\Serializer\Normalizer\ArrayDenormalizer;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

$propertyInfo = new PropertyInfoExtractor([], [new PhpDocExtractor(), new ReflectionExtractor()]);
$normalizers = [new ObjectNormalizer(new ClassMetadataFactory(new AttributeLoader()), null, null, $propertyInfo), new ArrayDenormalizer()];

$this->serializer = new Serializer($normalizers, [new JsonEncoder()]);
```

[ObjectNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/ObjectNormalizer.php "Symfony\Component\Serializer\Normalizer\ObjectNormalizer")
This is the most powerful default normalizer and used for any object that could not be normalized by the other normalizers.

It leverages the [PropertyAccess Component](https://symfony.com/doc/8.0/components/property_access.html) to read and write in the object. This allows it to access properties directly or using getters, setters, hassers, issers, canners, adders and removers. Names are generated by removing the `get`, `set`, `has`, `is`, `can`, `add` or `remove` prefix from the method name and transforming the first letter to lowercase (e.g. `getFirstName()` ->`firstName`).

During denormalization, it supports using the constructor as well as the discovered methods.

Danger

Always make sure the `DateTimeNormalizer` is registered when serializing the `DateTime` or `DateTimeImmutable` classes to avoid excessive memory usage and exposing internal details.

### [Built-in Normalizers](https://symfony.com/doc/8.0/serializer.html#built-in-normalizers "Permalink to this headline")

Besides the normalizers registered by default (see previous section), the serializer component also provides some extra normalizers. You can register these by defining a service and tag it with [serializer.normalizer](https://symfony.com/doc/8.0/reference/dic_tags.html#reference-dic-tags-serializer-normalizer). For instance, to use the `CustomNormalizer` you have to define a service like:

YAML PHP

1
2
3
4
5
6
7
8
9

```
# config/services.yaml
services:
    # ...

    # if you're using autoconfigure, the tag will be automatically applied
    Symfony\Component\Serializer\Normalizer\CustomNormalizer:
        tags:
            # register the normalizer with a high priority (called earlier)
            - { name: 'serializer.normalizer', priority: 500 }
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
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\Serializer\Normalizer\CustomNormalizer;

return App::config([
    'services' => [
        // if you're using autoconfigure, the tag will be automatically applied
        CustomNormalizer::class => [
            'tags' => [
                // register the normalizer with a high priority (called earlier)
                ['serializer.normalizer' => ['priority' => 500]],
            ],
        ],
    ],
]);
```

[CustomNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/CustomNormalizer.php "Symfony\Component\Serializer\Normalizer\CustomNormalizer") This normalizer calls a method on the PHP object when normalizing. The PHP object must implement [NormalizableInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/NormalizableInterface.php "Symfony\Component\Serializer\Normalizer\NormalizableInterface") and/or [DenormalizableInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/DenormalizableInterface.php "Symfony\Component\Serializer\Normalizer\DenormalizableInterface"). [GetSetMethodNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/GetSetMethodNormalizer.php "Symfony\Component\Serializer\Normalizer\GetSetMethodNormalizer")
This normalizer is an alternative to the default `ObjectNormalizer`. It reads the content of the class by calling the "getters" (public methods starting with `get`, `has`, `is` or `can`). It will denormalize data by calling the constructor and the "setters" (public methods starting with `set`).

Objects are normalized to a map of property names and values (names are generated by removing the `get` prefix from the method name and transforming the first letter to lowercase; e.g. `getFirstName()` ->`firstName`).

[PropertyNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/PropertyNormalizer.php "Symfony\Component\Serializer\Normalizer\PropertyNormalizer")
This is yet another alternative to the `ObjectNormalizer`. This normalizer directly reads and writes public properties as well as **private and protected** properties (from both the class and all of its parent classes) by using [PHP reflection](https://php.net/manual/en/book.reflection.php). It supports calling the constructor during the denormalization process.

Objects are normalized to a map of property names to property values.

You can also limit the normalizer to only use properties with a specific visibility (e.g. only public properties) using the `PropertyNormalizer::NORMALIZE_VISIBILITY` context option. You can set it to any combination of the `PropertyNormalizer::NORMALIZE_PUBLIC`, `PropertyNormalizer::NORMALIZE_PROTECTED` and `PropertyNormalizer::NORMALIZE_PRIVATE` constants:

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
use Symfony\Component\Serializer\Normalizer\PropertyNormalizer;
// ...

$json = $serializer->serialize($person, 'json', [
    // only serialize public properties
    PropertyNormalizer::NORMALIZE_VISIBILITY => PropertyNormalizer::NORMALIZE_PUBLIC,

    // serialize public and protected properties
    PropertyNormalizer::NORMALIZE_VISIBILITY => PropertyNormalizer::NORMALIZE_PUBLIC | PropertyNormalizer::NORMALIZE_PROTECTED,
]);
```

[Named Serializers](https://symfony.com/doc/8.0/serializer.html#named-serializers "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

Sometimes, you may need multiple configurations for the serializer, such as different default contexts, name converters, or sets of normalizers and encoders, depending on the use case. For example, when your application communicates with multiple APIs, each of which follows its own set of serialization rules.

You can achieve this by configuring multiple serializer instances using the `named_serializers` option:

YAML PHP

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
# config/packages/serializer.yaml
framework:
    serializer:
        named_serializers:
            api_client1:
                name_converter: 'serializer.name_converter.camel_case_to_snake_case'
                default_context:
                    enable_max_depth: true
            api_client2:
                default_context:
                    enable_max_depth: false
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
21
22

```
// config/packages/serializer.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'serializer' => [
            'named_serializers' => [
                'api_client1' => [
                    'name_converter' => 'serializer.name_converter.camel_case_to_snake_case',
                    'default_context' => [
                        'enable_max_depth' => true,
                    ],
                ],
                'api_client2' => [
                    'default_context' => [
                        'enable_max_depth' => false,
                    ],
                ],
            ],
        ],
    ],
]);
```

You can inject these different serializer instances using [named aliases](https://symfony.com/doc/8.0/service_container/autowiring.html#autowiring-multiple-implementations-same-type):

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
namespace App\Controller;

// ...
use Symfony\Component\DependencyInjection\Attribute\Target;

class PersonController extends AbstractController
{
    public function index(
        SerializerInterface $serializer,           // default serializer
        SerializerInterface $apiClient1Serializer, // api_client1 serializer
        #[Target('apiClient2.serializer')]         // api_client2 serializer
        SerializerInterface $customName,
    ) {
        // ...
    }
}
```

By default, named serializers use the built-in set of normalizers and encoders, just like the main serializer service. However, you can customize them by registering additional normalizers or encoders for a specific named serializer. To do that, add a `serializer` attribute to the [serializer.normalizer](https://symfony.com/doc/8.0/reference/dic_tags.html#reference-dic-tags-serializer-normalizer) or [serializer.encoder](https://symfony.com/doc/8.0/reference/dic_tags.html#reference-dic-tags-serializer-encoder) tags:

YAML PHP

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
# config/services.yaml
services:
    # ...

    Symfony\Component\Serializer\Normalizer\CustomNormalizer:
        tags:
            # add this normalizer only to a specific named serializer
            - serializer.normalizer: { serializer: 'api_client1' }
            # add this normalizer to several named serializers
            - serializer.normalizer: { serializer: [ 'api_client1', 'api_client2' ] }
            # add this normalizer to all serializers, including the default one
            - serializer.normalizer: { serializer: '*' }
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
21

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\Serializer\Normalizer\CustomNormalizer;

return App::config([
    'services' => [
        CustomNormalizer::class => [
            // prevent this normalizer from being automatically added to the default serializer
            'autoconfigure' => false,
            'tags' => [
                // add this normalizer only to a specific named serializer
                ['serializer.normalizer' => ['serializer' => 'api_client1']],
                // add this normalizer to several named serializers
                ['serializer.normalizer' => ['serializer' => ['api_client1', 'api_client2']]],
                // add this normalizer to all serializers, including the default one
                ['serializer.normalizer' => ['serializer' => '*']],
            ],
        ],
    ],
]);
```

When the `serializer` attribute is not set, the service is registered only with the default serializer.

Each normalizer or encoder used in a named serializer is tagged with a `serializer.normalizer.<name>` or `serializer.encoder.<name>` tag. You can inspect their priorities using the following command:

1`$ php bin/console debug:container --tag serializer.<normalizer|encoder>.<name>`

Additionally, you can exclude the default set of normalizers and encoders from a named serializer by setting the `include_built_in_normalizers` and `include_built_in_encoders` options to `false`:

YAML PHP

1
2
3
4
5
6
7

```
# config/packages/serializer.yaml
framework:
    serializer:
        named_serializers:
            api_client1:
                include_built_in_normalizers: false
                include_built_in_encoders: true
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
// config/packages/serializer.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'serializer' => [
            'named_serializers' => [
                'api_client1' => [
                    'include_built_in_normalizers' => false,
                    'include_built_in_encoders' => true,
                ],
            ],
        ],
    ],
]);
```

[Debugging the Serializer](https://symfony.com/doc/8.0/serializer.html#debugging-the-serializer "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

Use the `debug:serializer` command to dump the serializer metadata of a given class:

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

```
$ php bin/console debug:serializer 'App\Entity\Book'

    App\Entity\Book
    ---------------

    +----------+------------------------------------------------------------+
    | Property | Options                                                    |
    +----------+------------------------------------------------------------+
    | name     | [                                                          |
    |          |   "groups" => [                                            |
    |          |       "book:read",                                         |
    |          |       "book:write",                                        |
    |          |   ],                                                       |
    |          |   "maxDepth" => 1,                                         |
    |          |   "serializedName" => "book_name",                         |
    |          |   "serializedPath" => null,                                |
    |          |   "ignore" => false,                                       |
    |          |   "normalizationContexts" => [],                           |
    |          |   "denormalizationContexts" => []                          |
    |          | ]                                                          |
    | isbn     | [                                                          |
    |          |   "groups" => [                                            |
    |          |       "book:read",                                         |
    |          |   ],                                                       |
    |          |   "maxDepth" => null,                                      |
    |          |   "serializedName" => null,                                |
    |          |   "serializedPath" => "[data][isbn]",                      |
    |          |   "ignore" => false,                                       |
    |          |   "normalizationContexts" => [],                           |
    |          |   "denormalizationContexts" => []                          |
    |          | ]                                                          |
    +----------+------------------------------------------------------------+
```

[Advanced Serialization](https://symfony.com/doc/8.0/serializer.html#advanced-serialization "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

### [Skipping `null` Values](https://symfony.com/doc/8.0/serializer.html#skipping-null-values "Permalink to this headline")

By default, the Serializer will preserve properties containing a `null` value. You can change this behavior by setting the `AbstractObjectNormalizer::SKIP_NULL_VALUES` context option to `true`:

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
class Person
{
    public string $name = 'Jane Doe';
    public ?string $gender = null;
}

$jsonContent = $serializer->serialize(new Person(), 'json', [
    AbstractObjectNormalizer::SKIP_NULL_VALUES => true,
]);
// $jsonContent contains {"name":"Jane Doe"}
```

### [Preserving Empty Objects](https://symfony.com/doc/8.0/serializer.html#preserving-empty-objects "Permalink to this headline")

By default, the Serializer transforms an empty array to `[]`. You can change this behavior by setting the `AbstractObjectNormalizer::PRESERVE_EMPTY_OBJECTS` context option to `true`. When the value is an instance of `\ArrayObject()`, the serialized data will be `{}`.

### [Handling Uninitialized Properties](https://symfony.com/doc/8.0/serializer.html#handling-uninitialized-properties "Permalink to this headline")

In PHP, typed properties have an `uninitialized` state which is different from the default `null` of untyped properties. When you try to access a typed property before giving it an explicit value, you get an error.

To avoid the serializer throwing an error when serializing or normalizing an object with uninitialized properties, by default the `ObjectNormalizer` catches these errors and ignores such properties.

You can disable this behavior by setting the `AbstractObjectNormalizer::SKIP_UNINITIALIZED_VALUES` context option to `false`:

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
class Person {
    public string $name = 'Jane Doe';
    public string $phoneNumber; // uninitialized
}

$jsonContent = $normalizer->serialize(new Dummy(), 'json', [
    AbstractObjectNormalizer::SKIP_UNINITIALIZED_VALUES => false,
]);
// throws Symfony\Component\PropertyAccess\Exception\UninitializedPropertyException
// as the ObjectNormalizer cannot read uninitialized properties
```

Note

Using [PropertyNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/PropertyNormalizer.php "Symfony\Component\Serializer\Normalizer\PropertyNormalizer") or [GetSetMethodNormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/GetSetMethodNormalizer.php "Symfony\Component\Serializer\Normalizer\GetSetMethodNormalizer") with `AbstractObjectNormalizer::SKIP_UNINITIALIZED_VALUES` context option set to `false` will throw an `\Error` instance if the given object has uninitialized properties as the normalizers cannot read them (directly or via getter/isser methods).

### [Handling Circular References](https://symfony.com/doc/8.0/serializer.html#handling-circular-references "Permalink to this headline")

Circular references are common when dealing with associated objects:

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
46
47
48

```
class Organization
{
    public function __construct(
        private string $name,
        private array $members = []
    ) {
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function addMember(Member $member): void
    {
        $this->members[] = $member;
    }

    public function getMembers(): array
    {
        return $this->members;
    }
}

class Member
{
    private Organization $organization;

    public function __construct(
        private string $name
    ) {
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function setOrganization(Organization $organization): void
    {
        $this->organization = $organization;
    }

    public function getOrganization(): Organization
    {
        return $this->organization;
    }
}
```

To avoid infinite loops, the normalizers throw a [CircularReferenceException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Exception/CircularReferenceException.php "Symfony\Component\Serializer\Exception\CircularReferenceException") when such a case is encountered:

1
2
3
4
5
6
7
8

```
$organization = new Organization('Les-Tilleuls.coop');
$member = new Member('Kévin');

$organization->addMember($member);
$member->setOrganization($organization);

$jsonContent = $serializer->serialize($organization, 'json');
// throws a CircularReferenceException
```

The key `circular_reference_limit` in the context sets the number of times it will serialize the same object before considering it a circular reference. The default value is `1`.

Instead of throwing an exception, circular references can also be handled by custom callables. This is especially useful when serializing entities having unique identifiers:

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
use Symfony\Component\Serializer\Exception\CircularReferenceException;
use Symfony\Component\Serializer\Normalizer\AbstractNormalizer;

$context = [
    AbstractNormalizer::CIRCULAR_REFERENCE_HANDLER => function (object $object, ?string $format, array $context): string {
        if (!$object instanceof Organization) {
            throw new CircularReferenceException('A circular reference has been detected when serializing the object of class "'.get_debug_type($object).'".');
        }

        // serialize the nested Organization with only the name (and not the members)
        return $object->getName();
    },
];

$jsonContent = $serializer->serialize($organization, 'json', $context);
// $jsonContent contains {"name":"Les-Tilleuls.coop","members":[{"name":"K\u00e9vin", organization: "Les-Tilleuls.coop"}]}
```

### [Handling Serialization Depth](https://symfony.com/doc/8.0/serializer.html#handling-serialization-depth "Permalink to this headline")

The serializer can also detect nested objects of the same class and limit the serialization depth. This is useful for tree structures, where the same object is nested multiple times.

For instance, assume a data structure of a family tree:

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

```
// ...
class Person
{
    // ...

    public function __construct(
        private string $name,
        private ?self $mother
    ) {
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function getMother(): ?self
    {
        return $this->mother;
    }

    // ...
}

// ...
$greatGrandmother = new Person('Elizabeth', null);
$grandmother = new Person('Jane', $greatGrandmother);
$mother = new Person('Sophie', $grandmother);
$child = new Person('Joe', $mother);
```

You can specify the maximum depth for a given property. For instance, you can set the max depth to `1` to always only serialize someone's mother (and not their grandmother, etc.):

Attributes YAML XML

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
// src/Model/Person.php
namespace App\Model;

use Symfony\Component\Serializer\Attribute\MaxDepth;

class Person
{
    #[MaxDepth(1)]
    private ?self $mother;

    // ...
}
```

1
2
3
4
5

```
# config/serializer/person.yaml
App\Model\Person:
    attributes:
        mother:
            max_depth: 1
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
<!-- config/serializer/person.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\Person">
        <attribute name="mother" max-depth="1"/>
    </class>
</serializer>
```

To limit the serialization depth, you must set the `AbstractObjectNormalizer::ENABLE_MAX_DEPTH` key to `true` in the context (or the default context specified in `framework.yaml`):

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
// ...
$greatGrandmother = new Person('Elizabeth', null);
$grandmother = new Person('Jane', $greatGrandmother);
$mother = new Person('Sophie', $grandmother);
$child = new Person('Joe', $mother);

$jsonContent = $serializer->serialize($child, null, [
    AbstractObjectNormalizer::ENABLE_MAX_DEPTH => true
]);
// $jsonContent contains {"name":"Joe","mother":{"name":"Sophie"}}
```

You can also configure a custom callable that is used when the maximum depth is reached. This can be used to for instance return the unique identifier of the next nested object, instead of omitting the property:

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
use Symfony\Component\Serializer\Normalizer\AbstractObjectNormalizer;
// ...

$greatGrandmother = new Person('Elizabeth', null);
$grandmother = new Person('Jane', $greatGrandmother);
$mother = new Person('Sophie', $grandmother);
$child = new Person('Joe', $mother);

// all callback parameters are optional (you can omit the ones you don't use)
$maxDepthHandler = function (object $innerObject, object $outerObject, string $attributeName, ?string $format = null, array $context = []): ?string {
    // return only the name of the next person in the tree
    return $innerObject instanceof Person ? $innerObject->getName() : null;
};

$jsonContent = $serializer->serialize($child, null, [
    AbstractObjectNormalizer::ENABLE_MAX_DEPTH => true,
    AbstractObjectNormalizer::MAX_DEPTH_HANDLER => $maxDepthHandler,
]);
// $jsonContent contains {"name":"Joe","mother":{"name":"Sophie","mother":"Jane"}}
```

### [Using Callbacks to Serialize Properties with Object Instances](https://symfony.com/doc/8.0/serializer.html#using-callbacks-to-serialize-properties-with-object-instances "Permalink to this headline")

When serializing, you can set a callback to format a specific object property. This can be used instead of [defining the context for a group](https://symfony.com/doc/8.0/serializer.html#serializer-context-group):

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

```
$person = new Person('cordoval', 34);
$person->setCreatedAt(new \DateTime('now'));

$context = [
    AbstractNormalizer::CALLBACKS => [
        // all callback parameters are optional (you can omit the ones you don't use)
        'createdAt' => function (object $attributeValue, object $object, string $attributeName, ?string $format = null, array $context = []) {
            return $attributeValue instanceof \DateTime ? $attributeValue->format(\DateTime::ATOM) : '';
        },
    ],
];
$jsonContent = $serializer->serialize($person, 'json', $context);
// $jsonContent contains {"name":"cordoval","age":34,"createdAt":"2014-03-22T09:43:12-0500"}
```

[Advanced Deserialization](https://symfony.com/doc/8.0/serializer.html#advanced-deserialization "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

### [Require all Properties](https://symfony.com/doc/8.0/serializer.html#require-all-properties "Permalink to this headline")

By default, the Serializer will add `null` to nullable properties when the parameters for those are not provided. You can change this behavior by setting the `AbstractNormalizer::REQUIRE_ALL_PROPERTIES` context option to `true`:

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
class Person
{
    public function __construct(
        public string $firstName,
        public ?string $lastName,
    ) {
    }
}

// ...
$data = ['firstName' => 'John'];
$person = $serializer->deserialize($data, Person::class, 'json', [
    AbstractNormalizer::REQUIRE_ALL_PROPERTIES => true,
]);
// throws Symfony\Component\Serializer\Exception\MissingConstructorArgumentException
```

### [Collecting Type Errors While Denormalizing](https://symfony.com/doc/8.0/serializer.html#collecting-type-errors-while-denormalizing "Permalink to this headline")

When denormalizing a payload to an object with typed properties, you'll get an exception if the payload contains properties that don't have the same type as the object.

Use the `COLLECT_DENORMALIZATION_ERRORS` option to collect all exceptions at once, and to get the object partially denormalized:

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
try {
    $person = $serializer->deserialize($jsonString, Person::class, 'json', [
        DenormalizerInterface::COLLECT_DENORMALIZATION_ERRORS => true,
    ]);
} catch (PartialDenormalizationException $e) {
    $violations = new ConstraintViolationList();

    /** @var NotNormalizableValueException $exception */
    foreach ($e->getErrors() as $exception) {
        $message = sprintf('The type must be one of "%s" ("%s" given).', implode(', ', $exception->getExpectedTypes()), $exception->getCurrentType());
        $parameters = [];
        if ($exception->canUseMessageForUser()) {
            $parameters['hint'] = $exception->getMessage();
        }
        $violations->add(new ConstraintViolation($message, '', $parameters, null, $exception->getPath(), null));
    }

    // ... return violation list to the user
}
```

### [Deserializing in an Existing Object](https://symfony.com/doc/8.0/serializer.html#deserializing-in-an-existing-object "Permalink to this headline")

The serializer can also be used to update an existing object. You can do this by configuring the `object_to_populate` serializer context option:

1
2
3
4
5
6
7
8
9

```
use Symfony\Component\Serializer\Normalizer\AbstractNormalizer;

// ...
$person = new Person('Jane Doe', 59);

$serializer->deserialize($jsonData, Person::class, 'json', [
    AbstractNormalizer::OBJECT_TO_POPULATE => $person,
]);
// instead of returning a new object, $person is updated instead
```

Note

The `AbstractNormalizer::OBJECT_TO_POPULATE` option is only used for the top level object. If that object is the root of a tree structure, all child elements that exist in the normalized data will be re-created with new instances.

When the `AbstractObjectNormalizer::DEEP_OBJECT_TO_POPULATE` context option is set to `true`, existing children of the root `OBJECT_TO_POPULATE` are updated from the normalized data, instead of the denormalizer re-creating them. This only works for single child objects, not for arrays of objects. Those will still be replaced when present in the normalized data.

### [Deserializing Interfaces and Abstract Classes](https://symfony.com/doc/8.0/serializer.html#deserializing-interfaces-and-abstract-classes "Permalink to this headline")

When working with associated objects, a property sometimes reference an interface or abstract class. When deserializing these properties, the Serializer has to know which concrete class to initialize. This is done using a _discriminator class mapping_.

Imagine there is an `InvoiceItemInterface` that is implemented by the `Product` and `Shipping` objects. When serializing an object, the serializer will add an extra "discriminator attribute". This contains either `product` or `shipping`. The discriminator class map maps these type names to the real PHP class name when deserializing:

Attributes YAML XML

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
namespace App\Model;

use Symfony\Component\Serializer\Attribute\DiscriminatorMap;

#[DiscriminatorMap(
    typeProperty: 'type',
    mapping: [
        'product' => Product::class,
        'shipping' => Shipping::class,
    ]
)]
interface InvoiceItemInterface
{
    // ...
}
```

1
2
3
4
5
6

```
App\Model\InvoiceItemInterface:
    discriminator_map:
        type_property: type
        mapping:
            product: 'App\Model\Product'
            shipping: 'App\Model\Shipping'
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

```
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\InvoiceItemInterface">
        <discriminator-map type-property="type">
            <mapping type="product" class="App\Model\Product"/>
            <mapping type="shipping" class="App\Model\Shipping"/>
        </discriminator-map>
    </class>
</serializer>
```

With the discriminator map configured, the serializer can now pick the correct class for properties typed as `InvoiceItemInterface`:

Framework Use Standalone Use

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

```
class InvoiceLine
{
    public function __construct(
        private InvoiceItemInterface $invoiceItem
    ) {
        $this->invoiceItem = $invoiceItem;
    }

    public function getInvoiceItem(): InvoiceItemInterface
    {
        return $this->invoiceItem;
    }

    // ...
}

// ...
$invoiceLine = new InvoiceLine(new Product());

$jsonString = $serializer->serialize($invoiceLine, 'json');
// $jsonString contains {"type":"product",...}

$invoiceLine = $serializer->deserialize($jsonString, InvoiceLine::class, 'json');
// $invoiceLine contains new InvoiceLine(new Product(...))
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

```
// ...
use Symfony\Component\Serializer\Mapping\ClassDiscriminatorFromClassMetadata;
use Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactory;
use Symfony\Component\Serializer\Mapping\Loader\AttributeLoader;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

class InvoiceLine
{
    public function __construct(
        private InvoiceItemInterface $invoiceItem
    ) {
        $this->invoiceItem = $invoiceItem;
    }

    public function getInvoiceItem(): InvoiceItemInterface
    {
        return $this->invoiceItem;
    }

    // ...
}

// ...

// Configure a loader to retrieve mapping information like DiscriminatorMap.
// E.g. when using PHP attributes:
$classMetadataFactory = new ClassMetadataFactory(new AttributeLoader());
$discriminator = new ClassDiscriminatorFromClassMetadata($classMetadataFactory);
$normalizers = [
    new ObjectNormalizer($classMetadataFactory, null, null, null, $discriminator),
];

$serializer = new Serializer($normalizers, $encoders);

$invoiceLine = new InvoiceLine(new Product());

$jsonString = $serializer->serialize($invoiceLine, 'json');
// $jsonString contains {"type":"product",...}

$invoiceLine = $serializer->deserialize($jsonString, InvoiceLine::class, 'json');
// $invoiceLine contains new InvoiceLine(new Product(...))
```

You can add a default type to avoid the need to add the type property when deserializing:

Attributes YAML XML

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
namespace App\Model;

use Symfony\Component\Serializer\Attribute\DiscriminatorMap;

#[DiscriminatorMap(
    typeProperty: 'type',
    mapping: [
        'product' => Product::class,
        'shipping' => Shipping::class,
    ],
    defaultType: 'product',
)]
interface InvoiceItemInterface
{
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
App\Model\InvoiceItemInterface:
    discriminator_map:
        type_property: type
        mapping:
            product: 'App\Model\Product'
            shipping: 'App\Model\Shipping'
        default_type: product
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

```
<?xml version="1.0" encoding="UTF-8" ?>
<serializer xmlns="http://symfony.com/schema/dic/serializer-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/serializer-mapping
        https://symfony.com/schema/dic/serializer-mapping/serializer-mapping-1.0.xsd"
>
    <class name="App\Model\InvoiceItemInterface">
        <discriminator-map type-property="type" default-type="product">
            <mapping type="product" class="App\Model\Product"/>
            <mapping type="shipping" class="App\Model\Shipping"/>
        </discriminator-map>
    </class>
</serializer>
```

Now it deserializes like this:

PHP

1
2
3

```
// $jsonString does NOT contain "type" in "invoiceItem"
$invoiceLine = $serializer->deserialize('{"invoiceItem":{...},...}', InvoiceLine::class, 'json');
// $invoiceLine contains new InvoiceLine(new Product(...))
```

### [Deserializing Input Partially (Unwrapping)](https://symfony.com/doc/8.0/serializer.html#deserializing-input-partially-unwrapping "Permalink to this headline")

The serializer will always deserialize the complete input string into PHP values. When connecting with third party APIs, you often only need a specific part of the returned response.

To avoid deserializing the whole response, you can use the [UnwrappingDenormalizer](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Normalizer/UnwrappingDenormalizer.php "Symfony\Component\Serializer\Normalizer\UnwrappingDenormalizer") and "unwrap" the input data:

1
2
3
4
5

```
$jsonData = '{"result":"success","data":{"person":{"name": "Jane Doe","age":57}}}';
$data = $serialiser->deserialize($jsonData, Object::class, 'json', [
    UnwrappingDenormalizer::UNWRAP_PATH => '[data][person]',
]);
// $data is Person(name: 'Jane Doe', age: 57)
```

The `unwrap_path` is a [property path](https://symfony.com/doc/8.0/components/property_access.html#property-access-reading-arrays) of the PropertyAccess component, applied on the denormalized array.

### [Handling Constructor Arguments](https://symfony.com/doc/8.0/serializer.html#handling-constructor-arguments "Permalink to this headline")

If the class constructor defines arguments, as usually happens with [Value Objects](https://en.wikipedia.org/wiki/Value_object), the serializer will match the parameter names with the deserialized attributes. If some parameters are missing, a [MissingConstructorArgumentsException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Exception/MissingConstructorArgumentsException.php "Symfony\Component\Serializer\Exception\MissingConstructorArgumentsException") is thrown.

In these cases, use the `default_constructor_arguments` context option to define default values for the missing parameters:

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
use App\Model\Person;
use Symfony\Component\Serializer\Normalizer\AbstractNormalizer;
// ...

$jsonData = '{"age":39,"name":"Jane Doe"}';
$person = $serializer->deserialize($jsonData, Person::class, 'json', [
    AbstractNormalizer::DEFAULT_CONSTRUCTOR_ARGUMENTS => [
        Person::class => ['sportsperson' => true],
    ],
]);
// $person is Person(name: 'Jane Doe', age: 39, sportsperson: true);
```

### [Recursive Denormalization and Type Safety](https://symfony.com/doc/8.0/serializer.html#recursive-denormalization-and-type-safety "Permalink to this headline")

When a `PropertyTypeExtractor` is available, the normalizer will also check that the data to denormalize matches the type of the property (even for primitive types). For instance, if a `string` is provided, but the type of the property is `int`, an [UnexpectedValueException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Serializer/Exception/UnexpectedValueException.php "Symfony\Component\Serializer\Exception\UnexpectedValueException") will be thrown. The type enforcement of the properties can be disabled by setting the serializer context option `ObjectNormalizer::DISABLE_TYPE_ENFORCEMENT` to `true`.

### [Handling Boolean Values](https://symfony.com/doc/8.0/serializer.html#handling-boolean-values "Permalink to this headline")

PHP considers many different values as true or false. For example, the strings `true`, `1`, and `yes` are considered true, while `false`, `0`, and `no` are considered false.

When deserializing, the Serializer component can take care of this automatically. This can be done by using the `AbstractNormalizer::FILTER_BOOL` context option:

1
2
3
4
5
6
7

```
use Symfony\Component\Serializer\Normalizer\AbstractNormalizer;
// ...

$person = $serializer->denormalize(['sportsperson' => 'yes'], Person::class, context: [
    AbstractNormalizer::FILTER_BOOL => true
]);
// $person contains a Person instance with sportsperson set to true
```

This context makes the deserialization process behave like the [filter_var](https://secure.php.net/manual/en/function.filter-var.php "filter_var") function with the `FILTER_VALIDATE_BOOL` flag.

[Extending Serialization for a Class](https://symfony.com/doc/8.0/serializer.html#extending-serialization-for-a-class "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may want to add or override serialization metadata on a class you cannot modify, for example a model coming from a third party library or a vendor package. Traditionally, you would have to create YAML or XML mapping files to configure serialization for these classes. The `#[ExtendsSerializationFor]` attribute provides a more convenient alternative.

Suppose you use a third party `Product` class and you want to expose different serialized field names or groups without modifying the original class.

To do this, create a separate class and use the `#[ExtendsSerializationFor]` attribute to tell the Serializer which class should receive this metadata. Your new class name is irrelevant and the class is typically made `abstract` to make it clear it is never instantiated:

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

```
// src/Serializer/VendorProductExtension.php
namespace App\Serializer;

use Symfony\Component\Serializer\Attribute\ExtendsSerializationFor;
use Symfony\Component\Serializer\Attribute\Groups;
use Symfony\Component\Serializer\Attribute\MaxDepth;
use Symfony\Component\Serializer\Attribute\SerializedName;
use Vendor\Library\Product;

#[ExtendsSerializationFor(Product::class)]
abstract class MyProductSerialization
{
    #[Groups(['api'])]
    #[SerializedName('product_name')]
    public string $name = '';

    #[Groups(['api', 'admin'])]
    public float $price = 0;

    #[Groups(['admin'])]
    #[MaxDepth(1)]
    public $category;
}
```

The serialization metadata defined in this class is applied to the target class (`Product`) as if it were defined directly on it.

You can only define metadata for properties that exist on the target class. Otherwise, a `MappingException` is thrown during container compilation.

You can use any serialization attribute on the source class properties, including `#[Groups]`, `#[SerializedName]`, `#[MaxDepth]`, `#[Ignore]`, and others.

#### [Compile-Time Attribute Metadata](https://symfony.com/doc/8.0/serializer.html#compile-time-attribute-metadata "Permalink to this headline")

When using the Symfony framework with [autoconfiguration](https://symfony.com/doc/8.0/service_container.html#services-autoconfigure), classes that use serializer attributes (such as `#[Groups]`, `#[SerializedName]`, `#[MaxDepth]`, `#[Ignore]`, `#[Context]`, `#[SerializedPath]` or `#[DiscriminatorMap]`) are automatically discovered at compile time. This allows the attribute loader to only process the classes that are known to have serializer attributes, improving performance in production.

If you need to explicitly register a class that uses serializer attributes (e.g. from a third-party library that is not part of your service definitions), tag it with `serializer.attribute_metadata` and `container.excluded`:

1
2
3
4
5
6

```
# config/services.yaml
services:
    Vendor\Library\SomeModel:
        tags:
            - { name: container.excluded }
            - { name: serializer.attribute_metadata }
```

[Configuring the Metadata Cache](https://symfony.com/doc/8.0/serializer.html#configuring-the-metadata-cache "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------

The metadata for the serializer is automatically cached to enhance application performance. By default, the serializer uses the `cache.system` cache pool which is configured using the [cache.system](https://symfony.com/doc/8.0/reference/configuration/framework.html#reference-cache-system) option.

[Going Further with the Serializer](https://symfony.com/doc/8.0/serializer.html#going-further-with-the-serializer "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------

* [How to Create your Custom Context Builder](https://symfony.com/doc/8.0/serializer/custom_context_builders.html)
* [How to Create your Custom Name Converter](https://symfony.com/doc/8.0/serializer/custom_name_converter.html)
* [How to Create your Custom Normalizer](https://symfony.com/doc/8.0/serializer/custom_normalizer.html)
* [Serializer Encoders](https://symfony.com/doc/8.0/serializer/encoders.html)
* [Streaming JSON](https://symfony.com/doc/8.0/serializer/streaming_json.html)

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 1: Check Code Performance in Dev, Test, Staging & Production](https://symfony.com/images/network/blackfire_03.png)](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)
[Check Code Performance in Dev, Test, Staging & Production](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)

[![Image 2: Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://symfony.com/images/network/slsolutions_01.webp)](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)
[Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 3: Avatar of Anton A. Sumin, a Symfony contributor](https://www.gravatar.com/avatar/8c5113d3f81d7f422f6e63d2058203a6?size=48&rating=g&default=retro)

Thanks **Anton A. Sumin** for being a Symfony contributor

**2** commits • **140** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 4](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
[Celebrating 20 years of Symfony](https://symfony.com/20years)

**Symfony**™ is a trademark of Symfony SAS. [All rights reserved](https://symfony.com/trademark).

* [What is Symfony?](https://symfony.com/what-is-symfony)

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Symfony at a Glance](https://symfony.com/at-a-glance)
  * [Symfony Packages](https://symfony.com/packages)
  * [Symfony Releases](https://symfony.com/releases)
  * [Security Policy](https://symfony.com/doc/current/contributing/code/security.html)
  * [Logo & Screenshots](https://symfony.com/logo)
  * [Trademark & Licenses](https://symfony.com/license)
  * [symfony1 Legacy](https://symfony.com/legacy)

* [Learn Symfony](https://symfony.com/doc)

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Reference](https://symfony.com/doc/current/reference/index.html)
  * [Bundles](https://symfony.com/bundles)
  * [Best Practices](https://symfony.com/doc/current/best_practices.html)
  * [Training](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [eLearning Platform](https://university.sensiolabs.com/e-learning-platform?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Certification](https://certification.symfony.com/)

* [Screencasts](https://symfonycasts.com/)

  * [Learn Symfony](https://symfonycasts.com/tracks/symfony)
  * [Learn PHP](https://symfonycasts.com/tracks/php)
  * [Learn JavaScript](https://symfonycasts.com/tracks/javascript)
  * [Learn Drupal](https://symfonycasts.com/tracks/drupal)
  * [Learn RESTful APIs](https://symfonycasts.com/tracks/rest)

* [Community](https://symfony.com/community)

  * [Symfony Community](https://symfony.com/community)
  * [SymfonyConnect](https://connect.symfony.com/)
  * [Events & Meetups](https://symfony.com/events/)
  * [Projects using Symfony](https://symfony.com/projects)
  * [Contributors](https://symfony.com/contributors)
  * [Symfony Jobs](https://symfony.com/jobs)
  * [Backers](https://symfony.com/backers)
  * [Code of Conduct](https://symfony.com/doc/current/contributing/code_of_conduct/code_of_conduct.html)
  * [Downloads Stats](https://symfony.com/stats/downloads)
  * [Support](https://symfony.com/support)

* [Blog](https://symfony.com/blog/)

  * [All Blog Posts](https://symfony.com/blog/)
  * [A Week of Symfony](https://symfony.com/blog/category/a-week-of-symfony)
  * [Case Studies](https://symfony.com/blog/category/case-studies)
  * [Cloud](https://symfony.com/blog/category/cloud)
  * [Community](https://symfony.com/blog/category/community)
  * [Conferences](https://symfony.com/blog/category/conferences)
  * [Diversity](https://symfony.com/blog/category/diversity)
  * [Living on the edge](https://symfony.com/blog/category/living-on-the-edge)
  * [Releases](https://symfony.com/blog/category/releases)
  * [Security Advisories](https://symfony.com/blog/category/security-advisories)
  * [Symfony Insight](https://symfony.com/blog/category/symfony-insight)
  * [Twig](https://symfony.com/blog/category/twig)
  * [SensioLabs Blog](https://sensiolabs.com/blog?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

* [Services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

  * [SensioLabs services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Train developers](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Manage your project quality](https://insight.symfony.com/)
  * [Improve your project performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)
  * [Host Symfony projects](https://symfony.com/cloud/)

[Powered by](https://symfony.com/cloud/)

[](https://symfony.com/cloud/ "Upsun, a Platform-as-a-Service optimized for Symfony developers")

### Follow Symfony

[](https://github.com/symfony "Symfony on GitHub")[](https://symfony.com/slack "Symfony on Slack")[](https://twitter.com/symfony "Symfony on Twitter")[](https://mastodon.social/@symfony "Symfony on Mastodon")[](https://www.linkedin.com/company/symfony-sas/ "Symfony on LinkedIn")[](https://www.facebook.com/SymfonyFramework "Symfony on Facebook")[](https://www.youtube.com/symfonytv "Symfony on YouTube")[](https://bsky.app/profile/symfony.com "Symfony on BlueSky")[](https://www.threads.net/@symfony "Symfony on Threads")[](https://symfonycasts.com/ "Symfony Screencasts")[](https://feeds.feedburner.com/symfony/blog "Symfony Blog RSS")

Site appearance:

CLOSE

Search Symfony Docs

Search
