# Source: https://symfony.com/doc/8.0/controller.html

Title: Controller (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/controller.html

Markdown Content:
Controller (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/controller.html#main-content)

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
3. Controller

 Search Symfony Docs

Version:

Table of Contents

* [A Basic Controller](https://symfony.com/doc/8.0/controller.html#a-basic-controller)
  * [Mapping a URL to a Controller](https://symfony.com/doc/8.0/controller.html#mapping-a-url-to-a-controller)

* [The Base Controller Class & Services](https://symfony.com/doc/8.0/controller.html#the-base-controller-class-services)
  * [Generating URLs](https://symfony.com/doc/8.0/controller.html#generating-urls)
  * [Redirecting](https://symfony.com/doc/8.0/controller.html#redirecting)
  * [Rendering Templates](https://symfony.com/doc/8.0/controller.html#rendering-templates)
  * [Fetching Services](https://symfony.com/doc/8.0/controller.html#fetching-services)

* [Generating Controllers](https://symfony.com/doc/8.0/controller.html#generating-controllers)
* [Managing Errors and 404 Pages](https://symfony.com/doc/8.0/controller.html#managing-errors-and-404-pages)
* [The Request object as a Controller Argument](https://symfony.com/doc/8.0/controller.html#the-request-object-as-a-controller-argument)
* [Automatic Mapping Of The Request](https://symfony.com/doc/8.0/controller.html#automatic-mapping-of-the-request)
  * [Mapping Query Parameters Individually](https://symfony.com/doc/8.0/controller.html#mapping-query-parameters-individually)
  * [Mapping The Whole Query String](https://symfony.com/doc/8.0/controller.html#mapping-the-whole-query-string)
  * [Mapping Request Payload](https://symfony.com/doc/8.0/controller.html#mapping-request-payload)
  * [Mapping Uploaded Files](https://symfony.com/doc/8.0/controller.html#mapping-uploaded-files)

* [Managing the Session](https://symfony.com/doc/8.0/controller.html#managing-the-session)
  * [Flash Messages](https://symfony.com/doc/8.0/controller.html#flash-messages)

* [The Request and Response Object](https://symfony.com/doc/8.0/controller.html#the-request-and-response-object)
  * [Accessing Configuration Values](https://symfony.com/doc/8.0/controller.html#accessing-configuration-values)
  * [Returning JSON Response](https://symfony.com/doc/8.0/controller.html#returning-json-response)
  * [Streaming File Responses](https://symfony.com/doc/8.0/controller.html#streaming-file-responses)
  * [Sending Early Hints](https://symfony.com/doc/8.0/controller.html#sending-early-hints)
  * [Streaming Server-Sent Events](https://symfony.com/doc/8.0/controller.html#streaming-server-sent-events)

* [Decoupling Controllers from Symfony](https://symfony.com/doc/8.0/controller.html#decoupling-controllers-from-symfony)
* [Final Thoughts](https://symfony.com/doc/8.0/controller.html#final-thoughts)
* [Keep Going!](https://symfony.com/doc/8.0/controller.html#keep-going)
* [Learn more about Controllers](https://symfony.com/doc/8.0/controller.html#learn-more-about-controllers)

Controller
==========

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/controller.rst)

A controller is a PHP function you create that reads information from the `Request` object and creates and returns a `Response` object. The response could be an HTML page, JSON, XML, a file download, a redirect, a 404 error or anything else. The controller runs whatever arbitrary logic _your application_ needs to render the content of a page.

Tip

If you haven't already created your first working page, check out [Create your First Page in Symfony](https://symfony.com/doc/8.0/page_creation.html) and then come back!

[A Basic Controller](https://symfony.com/doc/8.0/controller.html#a-basic-controller "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

While a controller can be any PHP callable (function, method on an object, or a `Closure`), a controller is usually a method inside a controller class:

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

```
// src/Controller/LuckyController.php
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class LuckyController
{
    #[Route('/lucky/number/{max}', name: 'app_lucky_number')]
    public function number(int $max): Response
    {
        $number = random_int(0, $max);

        return new Response(
            '<html><body>Lucky number: '.$number.'</body></html>'
        );
    }
}
```

The controller is the `number()` method, which lives inside the controller class `LuckyController`.

This controller is quite simple:

* _line 2_: Symfony takes advantage of PHP's namespace functionality to namespace the entire controller class.
* _line 4_: Symfony again takes advantage of PHP's namespace functionality: the `use` keyword imports the `Response` class, which the controller must return.
* _line 7_: The class can technically be called anything, but it's suffixed with `Controller` by convention.
* _line 10_: The action method is allowed to have a `$max` argument thanks to the `{max}`[wildcard in the route](https://symfony.com/doc/8.0/routing.html).
* _line 14_: The controller creates and returns a `Response` object.

### [Mapping a URL to a Controller](https://symfony.com/doc/8.0/controller.html#mapping-a-url-to-a-controller "Permalink to this headline")

In order to _view_ the result of this controller, you need to map a URL to it via a route. This was done above with the `#[Route('/lucky/number/{max}')]`[route attribute](https://symfony.com/doc/8.0/page_creation.html#attribute-routes).

To see your page, go to this URL in your browser: [http://localhost:8000/lucky/number/100](http://localhost:8000/lucky/number/100)

For more information on routing, see [Routing](https://symfony.com/doc/8.0/routing.html).

[The Base Controller Class & Services](https://symfony.com/doc/8.0/controller.html#the-base-controller-class-services "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------

To aid development, Symfony comes with an optional base controller class called [AbstractController](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php "Symfony\Bundle\FrameworkBundle\Controller\AbstractController"). It can be extended to gain access to helper methods.

Add the `use` statement atop your controller class and then modify `LuckyController` to extend it:

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
// src/Controller/LuckyController.php
  namespace App\Controller;

+ use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;

- class LuckyController
+ class LuckyController extends AbstractController
  {
      // ...
  }
```

That's it! You now have access to methods like [$this->render()](https://symfony.com/doc/8.0/controller.html#controller-rendering-templates) and many others that you'll learn about next.

### [Generating URLs](https://symfony.com/doc/8.0/controller.html#generating-urls "Permalink to this headline")

The [generateUrl()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20generateUrl "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::generateUrl()") method is just a helper method that generates the URL for a given route:

1`$url = $this->generateUrl('app_lucky_number', ['max' => 10]);`

### [Redirecting](https://symfony.com/doc/8.0/controller.html#redirecting "Permalink to this headline")

If you want to redirect the user to another page, use the `redirectToRoute()` and `redirect()` methods:

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
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\HttpFoundation\Response;

// ...
public function index(): RedirectResponse
{
    // redirects to the "homepage" route
    return $this->redirectToRoute('homepage');

    // redirectToRoute is a shortcut for:
    // return new RedirectResponse($this->generateUrl('homepage'));

    // does a permanent HTTP 301 redirect
    return $this->redirectToRoute('homepage', [], 301);
    // if you prefer, you can use PHP constants instead of hardcoded numbers
    return $this->redirectToRoute('homepage', [], Response::HTTP_MOVED_PERMANENTLY);

    // redirect to a route with parameters
    return $this->redirectToRoute('app_lucky_number', ['max' => 10]);

    // redirects to a route and maintains the original query string parameters
    return $this->redirectToRoute('blog_show', $request->query->all());

    // redirects to the current route (e.g. for Post/Redirect/Get pattern):
    return $this->redirectToRoute($request->attributes->get('_route'));

    // redirects externally
    return $this->redirect('http://symfony.com/doc');
}
```

Danger

The `redirect()` method does not check its destination in any way. If you redirect to a URL provided by end-users, your application may be open to the [unvalidated redirects security vulnerability](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html).

### [Rendering Templates](https://symfony.com/doc/8.0/controller.html#rendering-templates "Permalink to this headline")

If you're serving HTML, you'll want to render a template. The `render()` method renders a template **and** puts that content into a `Response` object for you:

1
2

```
// renders templates/lucky/number.html.twig
return $this->render('lucky/number.html.twig', ['number' => $number]);
```

Templating and Twig are explained more in the [Creating and Using Templates article](https://symfony.com/doc/8.0/templates.html).

### [Fetching Services](https://symfony.com/doc/8.0/controller.html#fetching-services "Permalink to this headline")

Symfony comes _packed_ with a lot of useful classes and functionalities, called [services](https://symfony.com/doc/8.0/service_container.html). These are used for rendering templates, sending emails, querying the database and any other "work" you can think of.

If you need a service in a controller, type-hint an argument with its class (or interface) name and Symfony will inject it automatically. This requires your [controller to be registered as a service](https://symfony.com/doc/8.0/controller/service.html):

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
use Psr\Log\LoggerInterface;
use Symfony\Component\HttpFoundation\Response;
// ...

#[Route('/lucky/number/{max}')]
public function number(int $max, LoggerInterface $logger): Response
{
    $logger->info('We are logging!');
    // ...
}
```

Awesome!

What other services can you type-hint? To see them, use the `debug:autowiring` console command:

1`$ php bin/console debug:autowiring`

Tip

If you need control over the _exact_ value of an argument, or require a parameter, you can use the `#[Autowire]` attribute:

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
// ...
use Psr\Log\LoggerInterface;
use Symfony\Component\DependencyInjection\Attribute\Autowire;
use Symfony\Component\HttpFoundation\Response;

class LuckyController extends AbstractController
{
    public function number(
        int $max,

        // inject a specific logger service
        #[Autowire(service: 'monolog.logger.request')]
        LoggerInterface $logger,

        // or inject parameter values
        #[Autowire('%kernel.project_dir%')]
        string $projectDir
    ): Response
    {
        $logger->info('We are logging!');
        // ...
    }
}
```

You can read more about this attribute in [Defining Services Dependencies Automatically (Autowiring)](https://symfony.com/doc/8.0/service_container/autowiring.html#autowire-attribute).

Like with all services, you can also use regular [constructor injection](https://symfony.com/doc/8.0/service_container.html#services-constructor-injection) in your controllers.

For more information about services, see the [Service Container](https://symfony.com/doc/8.0/service_container.html) article.

[Generating Controllers](https://symfony.com/doc/8.0/controller.html#generating-controllers "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

To save time, you can install [Symfony Maker](https://symfony.com/doc/current/bundles/SymfonyMakerBundle/index.html) and tell Symfony to generate a new controller class:

1
2
3
4

```
$ php bin/console make:controller BrandNewController

created: src/Controller/BrandNewController.php
created: templates/brandnew/index.html.twig
```

If you want to generate an entire CRUD from a Doctrine [entity](https://symfony.com/doc/8.0/doctrine.html), use:

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
$ php bin/console make:crud Product

created: src/Controller/ProductController.php
created: src/Form/ProductType.php
created: templates/product/_delete_form.html.twig
created: templates/product/_form.html.twig
created: templates/product/edit.html.twig
created: templates/product/index.html.twig
created: templates/product/new.html.twig
created: templates/product/show.html.twig
```

[Managing Errors and 404 Pages](https://symfony.com/doc/8.0/controller.html#managing-errors-and-404-pages "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------

When things are not found, you should return a 404 response. To do this, throw a special type of exception:

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

```
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

// ...
public function index(): Response
{
    // retrieve the object from database
    $product = ...;
    if (!$product) {
        throw $this->createNotFoundException('The product does not exist');

        // the above is just a shortcut for:
        // throw new NotFoundHttpException('The product does not exist');
    }

    return $this->render(/* ... */);
}
```

The [createNotFoundException()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20createNotFoundException "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::createNotFoundException()") method is just a shortcut to create a special [NotFoundHttpException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Exception/NotFoundHttpException.php "Symfony\Component\HttpKernel\Exception\NotFoundHttpException") object, which ultimately triggers a 404 HTTP response inside Symfony.

If you throw an exception that extends or is an instance of [HttpException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Exception/HttpException.php "Symfony\Component\HttpKernel\Exception\HttpException"), Symfony will use the appropriate HTTP status code. Otherwise, the response will have a 500 HTTP status code:

1
2

```
// this exception ultimately generates a 500 status error
throw new \Exception('Something went wrong!');
```

In every case, an error page is shown to the end user and a full debug error page is shown to the developer (i.e. when you're in "Debug" mode - see [Configuring Symfony](https://symfony.com/doc/8.0/configuration.html#page-creation-environments)).

To customize the error page that's shown to the user, see the [How to Customize Error Pages](https://symfony.com/doc/8.0/controller/error_pages.html) article.

[The Request object as a Controller Argument](https://symfony.com/doc/8.0/controller.html#the-request-object-as-a-controller-argument "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

What if you need to read query parameters, grab a request header or get access to an uploaded file? That information is stored in Symfony's `Request` object. To access it in your controller, add it as an argument and **type-hint it with the Request class**:

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
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
// ...

public function index(Request $request): Response
{
    $page = $request->query->get('page', 1);

    // ...
}
```

[Keep reading](https://symfony.com/doc/8.0/controller.html#request-object-info) for more information about using the Request object.

[Automatic Mapping Of The Request](https://symfony.com/doc/8.0/controller.html#automatic-mapping-of-the-request "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------

It is possible to automatically map request's payload and/or query parameters to your controller's action arguments with attributes.

### [Mapping Query Parameters Individually](https://symfony.com/doc/8.0/controller.html#mapping-query-parameters-individually "Permalink to this headline")

Let's say a user sends you a request with the following query string: `https://example.com/dashboard?firstName=John&lastName=Smith&age=27`. Thanks to the [MapQueryParameter](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Attribute/MapQueryParameter.php "Symfony\Component\HttpKernel\Attribute\MapQueryParameter") attribute, arguments of your controller's action can be automatically fulfilled:

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
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapQueryParameter;

// ...

public function dashboard(
    #[MapQueryParameter] string $firstName,
    #[MapQueryParameter] string $lastName,
    #[MapQueryParameter] int $age,
): Response
{
    // ...
}
```

The `MapQueryParameter` attribute supports the following argument types:

* `\BackedEnum`
* `array`
* `bool`
* `float`
* `int`
* `string`
* Objects that extend [AbstractUid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/AbstractUid.php "Symfony\Component\Uid\AbstractUid")

`#[MapQueryParameter]` can take an optional argument called `filter`. You can use the [Validate Filters](https://www.php.net/manual/en/filter.constants.php) constants defined in PHP:

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
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapQueryParameter;

// ...

public function dashboard(
    #[MapQueryParameter(filter: \FILTER_VALIDATE_REGEXP, options: ['regexp' => '/^\w+$/'])] string $firstName,
    #[MapQueryParameter] string $lastName,
    #[MapQueryParameter(filter: \FILTER_VALIDATE_INT)] int $age,
): Response
{
    // ...
}
```

### [Mapping The Whole Query String](https://symfony.com/doc/8.0/controller.html#mapping-the-whole-query-string "Permalink to this headline")

Another possibility is to map the entire query string into an object that will hold available query parameters. Let's say you declare the following DTO with its optional validation constraints:

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

```
namespace App\Model;

use Symfony\Component\Validator\Constraints as Assert;

class UserDto
{
    public function __construct(
        #[Assert\NotBlank]
        public string $firstName,

        #[Assert\NotBlank]
        public string $lastName,

        #[Assert\GreaterThan(18)]
        public int $age,
    ) {
    }
}
```

You can then use the [MapQueryString](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Attribute/MapQueryString.php "Symfony\Component\HttpKernel\Attribute\MapQueryString") attribute in your controller:

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
use App\Model\UserDto;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapQueryString;

// ...

public function dashboard(
    #[MapQueryString] UserDto $userDto
): Response
{
    // ...
}
```

You can customize the validation groups used during the mapping and also the HTTP status to return if the validation fails:

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
use Symfony\Component\HttpFoundation\Response;

// ...

public function dashboard(
    #[MapQueryString(
        validationGroups: ['strict', 'edit'],
        validationFailedStatusCode: Response::HTTP_UNPROCESSABLE_ENTITY
    )] UserDto $userDto
): Response
{
    // ...
}
```

The default status code returned if the validation fails is 404.

If you want to map your object to a nested array in your query using a specific key, set the `key` option in the `#[MapQueryString]` attribute:

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
use App\Model\SearchDto;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapQueryString;

// ...

public function dashboard(
    #[MapQueryString(key: 'search')] SearchDto $searchDto
): Response
{
    // ...
}
```

If you need a valid DTO even when the request query string is empty, set a default value for your controller arguments:

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
use App\Model\UserDto;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapQueryString;

// ...

public function dashboard(
    #[MapQueryString] UserDto $userDto = new UserDto()
): Response
{
    // ...
}
```

### [Mapping Request Payload](https://symfony.com/doc/8.0/controller.html#mapping-request-payload "Permalink to this headline")

When creating an API and dealing with other HTTP methods than `GET` (like `POST` or `PUT`), user's data are not stored in the query string but directly in the request payload, like this:

1
2
3
4
5

```
{
    "firstName": "John",
    "lastName": "Smith",
    "age": 28
}
```

In this case, it is also possible to directly map this payload to your DTO by using the [MapRequestPayload](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Attribute/MapRequestPayload.php "Symfony\Component\HttpKernel\Attribute\MapRequestPayload") attribute:

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
use App\Model\UserDto;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;

// ...

public function dashboard(
    #[MapRequestPayload] UserDto $userDto
): Response
{
    // ...
}
```

This attribute allows you to customize the serialization context as well as the class responsible of doing the mapping between the request and your DTO:

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
public function dashboard(
    #[MapRequestPayload(
        serializationContext: ['...'],
        resolver: App\Resolver\UserDtoResolver
    )]
    UserDto $userDto
): Response
{
    // ...
}
```

You can also customize the validation groups used, the status code to return if the validation fails as well as supported payload formats:

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
use Symfony\Component\HttpFoundation\Response;

// ...

public function dashboard(
    #[MapRequestPayload(
        acceptFormat: 'json',
        validationGroups: ['strict', 'read'],
        validationFailedStatusCode: Response::HTTP_NOT_FOUND
    )] UserDto $userDto
): Response
{
    // ...
}
```

The default status code returned if the validation fails is 422.

Tip

If you build a JSON API, make sure to declare your route as using the JSON [format](https://symfony.com/doc/8.0/routing.html#routing-format-parameter). This will make the error handling output a JSON response in case of validation errors, rather than an HTML page:

1`#[Route('/dashboard', name: 'dashboard', format: 'json')]`

Make sure to install [phpstan/phpdoc-parser](https://packagist.org/packages/phpstan/phpdoc-parser) and [phpdocumentor/type-resolver](https://packagist.org/packages/phpdocumentor/type-resolver) if you want to map a nested array of specific DTOs:

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
public function dashboard(
    #[MapRequestPayload] EmployeesDto $employeesDto
): Response
{
    // ...
}

final class EmployeesDto
{
    /**
     * @param UserDto[] $users
     */
    public function __construct(
        public readonly array $users = []
    ) {}
}
```

Instead of returning an array of DTO objects, you can tell Symfony to transform each DTO object into an array and return something like this:

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
[
    {
        "firstName": "John",
        "lastName": "Smith",
        "age": 28
    },
    {
        "firstName": "Jane",
        "lastName": "Doe",
        "age": 30
    }
]
```

To do so, map the parameter as an array and configure the type of each element using the `type` option of the attribute:

1
2
3
4
5
6

```
public function dashboard(
    #[MapRequestPayload(type: UserDto::class)] array $users
): Response
{
    // ...
}
```

Warning

When using custom types (e.g. enums) in your DTO properties, denormalization errors may expose internal class names to the end user. This was fixed in Symfony 8.1. In earlier versions, to avoid leaking implementation details, use built-in PHP types (`string`, `int`, etc.) and validate the values with constraints:

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
use Symfony\Component\Validator\Constraints as Assert;

final class OrderDto
{
    public function __construct(
        #[Assert\Choice(callback: [OrderStatus::class, 'values'])]
        public readonly string $status,
    ) {}
}
```

### [Mapping Uploaded Files](https://symfony.com/doc/8.0/controller.html#mapping-uploaded-files "Permalink to this headline")

Symfony provides an attribute called `#[MapUploadedFile]` to map one or more `UploadedFile` objects to controller arguments:

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

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\File\UploadedFile;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapUploadedFile;
use Symfony\Component\Routing\Attribute\Route;

class UserController extends AbstractController
{
    #[Route('/user/picture', methods: ['PUT'])]
    public function changePicture(
        #[MapUploadedFile] UploadedFile $picture,
    ): Response {
        // ...
    }
}
```

In this example, the associated [argument resolver](https://symfony.com/doc/8.0/controller/value_resolver.html) fetches the `UploadedFile` based on the argument name (`$picture`). If no file is submitted, an `HttpException` is thrown. You can change this by making the controller argument nullable:

1
2

```
#[MapUploadedFile]
?UploadedFile $document
```

The `#[MapUploadedFile]` attribute also allows you to pass a list of constraints to apply to the uploaded file:

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
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\File\UploadedFile;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapUploadedFile;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Validator\Constraints as Assert;

class UserController extends AbstractController
{
    #[Route('/user/picture', methods: ['PUT'])]
    public function changePicture(
        #[MapUploadedFile([
            new Assert\File(mimeTypes: ['image/png', 'image/jpeg']),
            new Assert\Image(maxWidth: 3840, maxHeight: 2160),
        ])]
        UploadedFile $picture,
    ): Response {
        // ...
    }
}
```

The validation constraints are checked before injecting the `UploadedFile` into the controller argument. If there's a constraint violation, an `HttpException` is thrown and the controller's action is not executed.

If you need to upload a collection of files, map them to an array or a variadic argument. The given constraint will be applied to all files and if any of them fails, an `HttpException` is thrown:

1
2
3
4
5

```
#[MapUploadedFile(new Assert\File(mimeTypes: ['application/pdf']))]
array $documents

#[MapUploadedFile(new Assert\File(mimeTypes: ['application/pdf']))]
UploadedFile ...$documents
```

Use the `name` option to rename the uploaded file to a custom value:

1
2

```
#[MapUploadedFile(name: 'something-else')]
UploadedFile $document
```

In addition, you can change the status code of the HTTP exception thrown when there are constraint violations:

1
2
3
4
5

```
#[MapUploadedFile(
    constraints: new Assert\File(maxSize: '2M'),
    validationFailedStatusCode: Response::HTTP_REQUEST_ENTITY_TOO_LARGE
)]
UploadedFile $document
```

[Managing the Session](https://symfony.com/doc/8.0/controller.html#managing-the-session "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------

Symfony provides a session service to store information about the user between requests. You can access the session through the `Request` object (in services, [inject the RequestStack service](https://symfony.com/doc/8.0/service_container/request.html)):

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
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

public function index(Request $request): Response
{
    $session = $request->getSession();

    // store an attribute for reuse during a later user request
    $session->set('user_id', 42);

    // retrieve an attribute with an optional default value
    $userId = $session->get('user_id', 0);

    // ...
}
```

Read the [session documentation](https://symfony.com/doc/8.0/session.html) for more details about configuring and using sessions.

### [Flash Messages](https://symfony.com/doc/8.0/controller.html#flash-messages "Permalink to this headline")

Flash messages are special session messages meant to be used exactly once: they vanish from the session automatically as soon as you retrieve them. This makes them ideal for storing user notifications:

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
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
// ...

public function update(Request $request): Response
{
    // ... do some data processing

    $this->addFlash('notice', 'Your changes were saved!');
    // $this->addFlash() is equivalent to $request->getSession()->getFlashBag()->add()

    return $this->redirectToRoute(/* ... */);
}
```

[The Request and Response Object](https://symfony.com/doc/8.0/controller.html#the-request-and-response-object "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------

As mentioned [earlier](https://symfony.com/doc/8.0/controller.html#controller-request-argument), Symfony will pass the `Request` object to any controller argument that is type-hinted with the `Request` class:

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
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

public function index(Request $request): Response
{
    $request->isXmlHttpRequest(); // is it an Ajax request?

    $request->getPreferredLanguage(['en', 'fr']);

    // retrieves GET and POST variables respectively
    $request->query->get('page');
    $request->getPayload()->get('page');

    // retrieves SERVER variables
    $request->server->get('HTTP_HOST');

    // retrieves an instance of UploadedFile identified by foo
    $request->files->get('foo');

    // retrieves a COOKIE value
    $request->cookies->get('PHPSESSID');

    // retrieves an HTTP request header, with normalized, lowercase keys
    $request->headers->get('host');
    $request->headers->get('content-type');
}
```

The `Request` class has several public properties and methods that return any information you need about the request.

Like the `Request`, the `Response` object has a public `headers` property. This object is of the type [ResponseHeaderBag](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/ResponseHeaderBag.php "Symfony\Component\HttpFoundation\ResponseHeaderBag") and provides methods for getting and setting response headers. The header names are normalized. As a result, the name `Content-Type` is equivalent to the name `content-type` or `content_type`.

In Symfony, a controller is required to return a `Response` object:

1
2
3
4
5
6
7
8

```
use Symfony\Component\HttpFoundation\Response;

// creates a simple Response with a 200 status code (the default)
$response = new Response('Hello '.$name, Response::HTTP_OK);

// creates a CSS-response with a 200 status code
$response = new Response('<style> ... </style>');
$response->headers->set('Content-Type', 'text/css');
```

To facilitate this, different response objects are included to address different response types. Some of these are mentioned below. To learn more about the `Request` and `Response` (and different `Response` classes), see the [HttpFoundation component documentation](https://symfony.com/doc/8.0/components/http_foundation.html#component-http-foundation-request).

Note

Technically, a controller can return a value other than a `Response`. However, your application is responsible for transforming that value into a `Response` object. This is handled using [events](https://symfony.com/doc/8.0/event_dispatcher.html) (specifically the [kernel.view event](https://symfony.com/doc/8.0/components/http_kernel.html#component-http-kernel-kernel-view)), an advanced feature you'll learn about later.

### [Accessing Configuration Values](https://symfony.com/doc/8.0/controller.html#accessing-configuration-values "Permalink to this headline")

To get the value of any [configuration parameter](https://symfony.com/doc/8.0/configuration.html#configuration-parameters) from a controller, use the `getParameter()` helper method:

1
2
3
4
5
6

```
// ...
public function index(): Response
{
    $contentsDir = $this->getParameter('kernel.project_dir').'/contents';
    // ...
}
```

### [Returning JSON Response](https://symfony.com/doc/8.0/controller.html#returning-json-response "Permalink to this headline")

To return JSON from a controller, use the `json()` helper method. This returns a `JsonResponse` object that encodes the data automatically:

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
use Symfony\Component\HttpFoundation\JsonResponse;
// ...

public function index(): JsonResponse
{
    // returns '{"username":"jane.doe"}' and sets the proper Content-Type header
    return $this->json(['username' => 'jane.doe']);

    // the shortcut defines three optional arguments
    // return $this->json($data, $status = 200, $headers = [], $context = []);
}
```

If the [serializer service](https://symfony.com/doc/8.0/serializer.html) is enabled in your application, it will be used to serialize the data to JSON. Otherwise, the [json_encode](https://secure.php.net/manual/en/function.json-encode.php "json_encode") function is used.

### [Streaming File Responses](https://symfony.com/doc/8.0/controller.html#streaming-file-responses "Permalink to this headline")

You can use the [file()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20file "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::file()") helper to serve a file from inside a controller:

1
2
3
4
5
6
7
8

```
use Symfony\Component\HttpFoundation\BinaryFileResponse;
// ...

public function download(): BinaryFileResponse
{
    // send the file contents and force the browser to download it
    return $this->file('/path/to/some_file.pdf');
}
```

The `file()` helper provides some arguments to configure its behavior:

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

```
use Symfony\Component\HttpFoundation\File\File;
use Symfony\Component\HttpFoundation\ResponseHeaderBag;
// ...

public function download(): BinaryFileResponse
{
    // load the file from the filesystem
    $file = new File('/path/to/some_file.pdf');

    return $this->file($file);

    // rename the downloaded file
    return $this->file($file, 'custom_name.pdf');

    // display the file contents in the browser instead of downloading it
    return $this->file('invoice_3241.pdf', 'my_invoice.pdf', ResponseHeaderBag::DISPOSITION_INLINE);
}
```

### [Sending Early Hints](https://symfony.com/doc/8.0/controller.html#sending-early-hints "Permalink to this headline")

You can improve performance by sending `103` Early Hints responses to ask the browser to start downloading assets before the full response is ready. See [Asset Preloading and Resource Hints with WebLink](https://symfony.com/doc/8.0/web_link.html#early-hints) for details.

### [Streaming Server-Sent Events](https://symfony.com/doc/8.0/controller.html#streaming-server-sent-events "Permalink to this headline")

[Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) is a standard that allows a server to push updates to the client over a single HTTP connection. It provides an efficient way to send real-time updates from the server to the browser, such as live notifications, progress updates, or data feeds.

The [EventStreamResponse](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/EventStreamResponse.php "Symfony\Component\HttpFoundation\EventStreamResponse") class allows you to stream events to the client using the SSE protocol. It automatically sets the required headers (`Content-Type: text/event-stream`, `Cache-Control: no-cache`, `Connection: keep-alive`) and provides an API to send events:

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
use Symfony\Component\HttpFoundation\EventStreamResponse;
use Symfony\Component\HttpFoundation\ServerEvent;

// ...

public function liveNotifications(): EventStreamResponse
{
    return new EventStreamResponse(function (): iterable {
        foreach ($this->getNotifications() as $notification) {
            yield new ServerEvent($notification->toJson());

            sleep(1); // simulate a delay between events
        }
    });
}
```

The [ServerEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/ServerEvent.php "Symfony\Component\HttpFoundation\ServerEvent") class is a DTO that represents an SSE event following [the WHATWG SSE specification](https://html.spec.whatwg.org/multipage/server-sent-events.html). You can customize each event using its constructor arguments:

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
// basic event with only data
yield new ServerEvent('Some message');

// event with a custom type (clients listen via addEventListener('my-event', ...))
yield new ServerEvent(
    data: json_encode(['status' => 'completed']),
    type: 'my-event'
);

// event with an ID (useful for resuming streams with the Last-Event-ID header)
yield new ServerEvent(
    data: 'Update content',
    id: 'event-123'
);

// event that tells the client to retry after a specific time (in milliseconds)
yield new ServerEvent(
    data: 'Retry info',
    retry: 5000
);

// event with a comment (can be used for keep-alive)
yield new ServerEvent(comment: 'keep-alive');
```

For use cases where generators are not practical, you can use the [sendEvent()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/EventStreamResponse.php#:~:text=function%20sendEvent "Symfony\Component\HttpFoundation\EventStreamResponse::sendEvent()") method for manual control:

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
use Symfony\Component\HttpFoundation\EventStreamResponse;
use Symfony\Component\HttpFoundation\ServerEvent;

// ...

public function liveProgress(): EventStreamResponse
{
    return new EventStreamResponse(function (EventStreamResponse $response): void {
        $redis = new \Redis();
        $redis->connect('127.0.0.1');
        $redis->subscribe(['message'], function (/* ... */, string $message) use ($response): void {
            $response->sendEvent(new ServerEvent($message));
        });
    });
}
```

On the client side, you can listen to events using the native `EventSource` API:

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

```
const eventSource = new EventSource('/live-notifications');

// listen to all events (without a specific type)
eventSource.onmessage = (event) => {
    console.log('Received:', event.data);
};

// listen to events with a specific type
eventSource.addEventListener('my-event', (event) => {
    console.log('My event:', JSON.parse(event.data));
});

// handle connection errors
eventSource.onerror = (error) => {
    console.error('SSE error:', error);
    eventSource.close();
};
```

Warning

`EventStreamResponse` is designed for applications with limited concurrent connections. Because SSE keeps HTTP connections open, it consumes server resources (memory and connection limits) for each connected client.

For high-traffic applications that need to broadcast updates to many clients simultaneously, consider using [Mercure](https://symfony.com/doc/8.0/mercure.html), which is built on top of SSE but uses a dedicated hub to manage connections efficiently.

[Decoupling Controllers from Symfony](https://symfony.com/doc/8.0/controller.html#decoupling-controllers-from-symfony "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------

Extending the [AbstractController base class](https://symfony.com/doc/8.0/controller.html#the-base-controller-class-services) simplifies controller development and is **recommended for most applications**. However, some advanced users prefer to fully decouple your controllers from Symfony (for example, to improve testability or to follow a more framework-agnostic design) Symfony provides tools to help you do that.

To decouple controllers, Symfony exposes all the helpers from `AbstractController` through another class called [ControllerHelper](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/ControllerHelper.php "Symfony\Bundle\FrameworkBundle\Controller\ControllerHelper"), where each helper is available as a public method:

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
use Symfony\Bundle\FrameworkBundle\Controller\ControllerHelper;
use Symfony\Component\DependencyInjection\Attribute\AutowireMethodOf;
use Symfony\Component\HttpFoundation\Response;

class MyController
{
    public function __construct(
        #[AutowireMethodOf(ControllerHelper::class)]
        private \Closure $render,
        #[AutowireMethodOf(ControllerHelper::class)]
        private \Closure $redirectToRoute,
    ) {
    }

    public function showProduct(int $id): Response
    {
        if (!$id) {
            return ($this->redirectToRoute)('product_list');
        }

        return ($this->render)('product/show.html.twig', ['product_id' => $id]);
    }
}
```

You can inject the entire `ControllerHelper` class if you prefer, but using the [AutowireMethodOf](https://symfony.com/doc/8.0/service_container/autowiring.html#autowiring_closures) attribute as in the previous example, lets you inject only the exact helpers you need, making your code more efficient.

Since `#[AutowireMethodOf]` also works with interfaces, you can define interfaces for these helper methods:

1
2
3
4
5

```
interface RenderInterface
{
    // this is the signature of the render() helper
    public function __invoke(string $view, array $parameters = [], ?Response $response = null): Response;
}
```

Then, update your controller to use the interface instead of a closure:

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
use Symfony\Bundle\FrameworkBundle\Controller\ControllerHelper;
use Symfony\Component\DependencyInjection\Attribute\AutowireMethodOf;

class MyController
{
    public function __construct(
        #[AutowireMethodOf(ControllerHelper::class)]
        private RenderInterface $render,
    ) {
    }

    // ...
}
```

Using interfaces like in the previous example provides full static analysis and autocompletion benefits with no extra boilerplate code.

[Final Thoughts](https://symfony.com/doc/8.0/controller.html#final-thoughts "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

In Symfony, a controller is usually a class method which is used to accept requests, and return a `Response` object. When mapped with a URL, a controller becomes accessible and its response can be viewed.

To facilitate the development of controllers, Symfony provides an `AbstractController`. It can be used to extend the controller class allowing access to some frequently used utilities such as `render()` and `redirectToRoute()`. The `AbstractController` also provides the `createNotFoundException()` utility which is used to return a page not found response.

In other articles, you'll learn how to use specific services from inside your controller that will help you persist and fetch objects from a database, process form submissions, handle caching and more.

[Keep Going!](https://symfony.com/doc/8.0/controller.html#keep-going "Permalink to this headline")
--------------------------------------------------------------------------------------------------

Next, learn all about [rendering templates with Twig](https://symfony.com/doc/8.0/templates.html).

[Learn more about Controllers](https://symfony.com/doc/8.0/controller.html#learn-more-about-controllers "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------

* [How to Customize Error Pages](https://symfony.com/doc/8.0/controller/error_pages.html)
* [How to Forward Requests to another Controller](https://symfony.com/doc/8.0/controller/forwarding.html)
* [How to Define Controllers as Services](https://symfony.com/doc/8.0/controller/service.html)
* [How to Upload Files](https://symfony.com/doc/8.0/controller/upload_file.html)
* [Extending Action Argument Resolving](https://symfony.com/doc/8.0/controller/value_resolver.html)

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 1: Become certified from home](https://symfony.com/images/network/sf7certif_02.webp)](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=certifiedathome)
[Become certified from home](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=certifiedathome)

[![Image 2: Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://symfony.com/images/network/sltraining_01.webp)](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)
[Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 3: Avatar of Zoran Makrevski, a Symfony contributor](https://connect.symfony.com/api/images/b72af2e5-f602-4912-b952-6e2df5429378.png?format=48x48)

Thanks **[Zoran Makrevski](https://connect.symfony.com/profile/zmakrevski)** (**@zmakrevski**) for being a Symfony contributor

[**1** commit](https://github.com/symfony/symfony/commits?author=zmakrevski) • **653** lines changed

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
