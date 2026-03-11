# Source: https://symfony.com/doc/8.0/page_creation.html

Title: Create your First Page in Symfony (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/page_creation.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/page_creation.rst)

Creating a new page - whether it's an HTML page or a JSON endpoint - is a two-step process:

1. **Create a controller**: A controller is the PHP function you write that builds the page. You take the incoming request information and use it to create a Symfony `Response` object, which can hold HTML content, a JSON string or even a binary file like an image or PDF;
2. **Create a route**: A route is the URL (e.g. `/about`) to your page and points to a controller.

[Creating a Page: Route and Controller](https://symfony.com/doc/8.0/page_creation.html#creating-a-page-route-and-controller "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Tip

Before continuing, make sure you've read the [Setup](https://symfony.com/doc/current/setup.html) article and can access your new Symfony app in the browser.

Suppose you want to create a page - `/lucky/number` - that generates a lucky (well, random) number and prints it. To do that, create a "Controller" class and a "number" method inside of it:

Now you need to associate this controller function with a public URL (e.g. `/lucky/number`) so that the `number()` method is called when a user browses to it. This association is defined with the `#[Route]` attribute (in PHP, [attributes](https://www.php.net/manual/en/language.attributes.overview.php) are used to add metadata to code):

That's it! If you are using [the Symfony web server](https://symfony.com/doc/current/setup/symfony_cli.html#symfony-cli-server), try it out by going to: [http://localhost:8000/lucky/number](http://localhost:8000/lucky/number)

Tip

Symfony recommends defining routes as attributes to have the controller code and its route configuration at the same location. However, if you prefer, you can [define routes in separate files](https://symfony.com/doc/current/routing.html) using the YAML or PHP formats.

If you see a lucky number being printed back to you, congratulations! But before you run off to play the lottery, check out how this works. Remember the two steps to create a page?

1. _Create a controller and a method_: This is a function where _you_ build the page and ultimately return a `Response` object. You'll learn more about [controllers](https://symfony.com/doc/current/controller.html) in their own section, including how to return JSON responses;
2. _Create a route_: In `config/routes.yaml`, the route defines the URL to your page (`path`) and what `controller` to call. You'll learn more about [routing](https://symfony.com/doc/current/routing.html) in its own section, including how to make _variable_ URLs.

[The bin/console Command](https://symfony.com/doc/8.0/page_creation.html#the-bin-console-command "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------

Your project already has a powerful debugging tool inside: the `bin/console` command. Try running it:

You should see a list of commands that can give you debugging information, help generate code, generate database migrations and a lot more. As you install more packages, you'll see more commands.

To get a list of _all_ of the routes in your system, use the `debug:router` command:

You should see your `app_lucky_number` route in the list:

You will also see debugging routes besides `app_lucky_number` -- more on the debugging routes in the next section.

You'll learn about many more commands as you continue!

Tip

If your shell is supported, you can also set up console completion support. This autocompletes commands and other input when using `bin/console`. See [the Console document](https://symfony.com/doc/current/console.html#console-completion-setup) for more information on how to set up completion.

[The Web Debug Toolbar: Debugging Dream](https://symfony.com/doc/8.0/page_creation.html#the-web-debug-toolbar-debugging-dream "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

One of Symfony's _amazing_ features is the Web Debug Toolbar: a bar that displays a _huge_ amount of debugging information along the bottom of your page while developing. This is all included by default when using a [Symfony pack](https://symfony.com/doc/current/setup.html#symfony-packs) called `symfony/profiler-pack`.

You will see a dark bar along the bottom of the page. You'll learn more about all the information it holds along the way, but feel free to experiment: hover over and click the different icons to get information about routing, performance, logging and more.

[Rendering a Template](https://symfony.com/doc/8.0/page_creation.html#rendering-a-template "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------

If you're returning HTML from your controller, you'll probably want to render a template. Fortunately, Symfony comes with [Twig](https://twig.symfony.com/): a templating language that's minimal, powerful and actually quite fun.

Install the twig package with:

Make sure that `LuckyController` extends Symfony's base [AbstractController](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php "Symfony\Bundle\FrameworkBundle\Controller\AbstractController") class:

Now, use the handy `render()` method to render a template. Pass it a `number` variable so you can use it in Twig:

Template files live in the `templates/` directory, which was created for you automatically when you installed Twig. Create a new `templates/lucky` directory with a new `number.html.twig` file inside:

The `{{ number }}` syntax is used to _print_ variables in Twig. Refresh your browser to get your _new_ lucky number!

> [http://localhost:8000/lucky/number](http://localhost:8000/lucky/number)

Now you may wonder where the Web Debug Toolbar has gone: that's because there is no `</body>` tag in the current template. You can add the body element yourself, or extend `base.html.twig`, which contains all default HTML elements.

In the [templates](https://symfony.com/doc/current/templates.html) article, you'll learn all about Twig: how to loop, render other templates and leverage its powerful layout inheritance system.

[Checking out the Project Structure](https://symfony.com/doc/8.0/page_creation.html#checking-out-the-project-structure "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------

Great news! You've already worked inside the most important directories in your project:

`config/` Contains configuration. You will configure routes, [services](https://symfony.com/doc/current/service_container.html) and packages. `src/` All your PHP code lives here. `templates/` All your Twig templates live here.
Most of the time, you'll be working in `src/`, `templates/` or `config/`. As you keep reading, you'll learn what can be done inside each of these.

So what about the other directories in the project?

`bin/` The famous `bin/console` file lives here (and other, less important executable files). `var/` This is where automatically-created files are stored, like cache files (`var/cache/`) and logs (`var/log/`). `vendor/` Third-party (i.e. "vendor") libraries live here! These are downloaded via the [Composer](https://getcomposer.org/) package manager. `public/` This is the document root for your project: you put any publicly accessible files here.
And when you install new packages, new directories will be created automatically when needed.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
