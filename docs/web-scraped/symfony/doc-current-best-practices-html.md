# Source: https://symfony.com/doc/current/best_practices.html

Title: The Symfony Framework Best Practices (Symfony Docs)

URL Source: https://symfony.com/doc/current/best_practices.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/best_practices.rst)

This article describes the **best practices for developing web applications with Symfony** that fit the philosophy envisioned by the original Symfony creators.

If you don't agree with some of these recommendations, they might be a good **starting point** that you can then **extend and fit to your specific needs**. You can even ignore them completely and continue using your own best practices and methodologies. Symfony is flexible enough to adapt to your needs.

This article assumes that you already have experience developing Symfony applications. If you don't, first read the [Getting Started](https://symfony.com/doc/current/setup.html) section of the documentation.

Tip

Symfony provides a sample application called [Symfony Demo](https://github.com/symfony/demo) that follows all these best practices, so you can experience them in practice.

[Creating the Project](https://symfony.com/doc/current/best_practices.html#creating-the-project "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

### [Use the Symfony Binary to Create Symfony Applications](https://symfony.com/doc/current/best_practices.html#use-the-symfony-binary-to-create-symfony-applications "Permalink to this headline")

The Symfony binary is an executable command created in your machine when you [download Symfony](https://symfony.com/download). It provides multiple utilities, including the simplest way to create new Symfony applications:

Internally, this Symfony binary command executes the needed [Composer](https://getcomposer.org/) command to [create a new Symfony application](https://symfony.com/doc/current/setup.html#creating-symfony-applications) based on the current stable version.

### [Use the Default Directory Structure](https://symfony.com/doc/current/best_practices.html#use-the-default-directory-structure "Permalink to this headline")

Unless your project follows a development practice that imposes a certain directory structure, follow the default Symfony directory structure. It's flat, self-explanatory and not coupled to Symfony:

[Configuration](https://symfony.com/doc/current/best_practices.html#configuration "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

### [Use Parameters for Application Configuration](https://symfony.com/doc/current/best_practices.html#use-parameters-for-application-configuration "Permalink to this headline")

These are the options used to modify the application behavior, such as the sender of email notifications, or the enabled [feature toggles](https://en.wikipedia.org/wiki/Feature_toggle). Their value doesn't change per machine, so don't define them as environment variables.

Define these options as [parameters](https://symfony.com/doc/current/configuration.html#configuration-parameters) in the `config/services.yaml` file. You can override these options per [environment](https://symfony.com/doc/current/configuration.html#configuration-environments) in the `config/services_dev.yaml` and `config/services_prod.yaml` files.

Unless the application configuration is reused multiple times and needs rigid validation, do _not_ use the [Config component](https://symfony.com/doc/current/components/config.html) to define the options.

### [Use Short and Prefixed Parameter Names](https://symfony.com/doc/current/best_practices.html#use-short-and-prefixed-parameter-names "Permalink to this headline")

Consider using `app.` as the prefix of your [parameters](https://symfony.com/doc/current/configuration.html#configuration-parameters) to avoid collisions with Symfony and third-party bundles/libraries parameters. Then, use only one or two words to describe the purpose of the parameter:

### [Use Constants to Define Options that Rarely Change](https://symfony.com/doc/current/best_practices.html#use-constants-to-define-options-that-rarely-change "Permalink to this headline")

Configuration options like the number of items to display in some listing rarely change. Instead of defining them as [configuration parameters](https://symfony.com/doc/current/configuration.html#configuration-parameters), define them as PHP constants in the related classes. Example:

The main advantage of constants is that you can use them everywhere, including Twig templates and Doctrine entities, whereas parameters are only available from places with access to the [service container](https://symfony.com/doc/current/service_container.html).

The only notable disadvantage of using constants for this kind of configuration values is that it's complicated to redefine their values in your tests.

[Business Logic](https://symfony.com/doc/current/best_practices.html#business-logic "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

### [Don't Create any Bundle to Organize your Application Logic](https://symfony.com/doc/current/best_practices.html#don-t-create-any-bundle-to-organize-your-application-logic "Permalink to this headline")

When Symfony 2.0 was released, applications used [bundles](https://symfony.com/doc/current/bundles.html) to divide their code into logical features: UserBundle, ProductBundle, InvoiceBundle, etc. However, a bundle is meant to be something that can be reused as a stand-alone piece of software.

If you need to reuse some feature in your projects, create a bundle for it (in a private repository, do not make it publicly available). For the rest of your application code, use PHP namespaces to organize code instead of bundles.

### [Use Autowiring to Automate the Configuration of Application Services](https://symfony.com/doc/current/best_practices.html#use-autowiring-to-automate-the-configuration-of-application-services "Permalink to this headline")

[Service autowiring](https://symfony.com/doc/current/service_container/autowiring.html) is a feature that reads the type-hints on your constructor (or other methods) and automatically passes the correct services to each method, making it unnecessary to configure services explicitly and simplifying the application maintenance.

Use it in combination with [service autoconfiguration](https://symfony.com/doc/current/service_container.html#services-autoconfigure) to also add [service tags](https://symfony.com/doc/current/service_container/tags.html) to the services needing them, such as Twig extensions, event subscribers, etc.

### [Services Should be Private Whenever Possible](https://symfony.com/doc/current/best_practices.html#services-should-be-private-whenever-possible "Permalink to this headline")

[Make services private](https://symfony.com/doc/current/service_container.html#container-public) to prevent you from accessing those services via `$container->get()`. Instead, you will need to use proper dependency injection.

### [Use the YAML Format to Configure your own Services](https://symfony.com/doc/current/best_practices.html#use-the-yaml-format-to-configure-your-own-services "Permalink to this headline")

If you use the [default services.yaml configuration](https://symfony.com/doc/current/service_container.html#service-container-services-load-example), most services will be configured automatically. However, in some edge cases you'll need to configure services (or parts of them) manually.

YAML is the format recommended for configuring services because it's friendly to newcomers and concise, but Symfony also supports PHP configuration.

### [Use Attributes to Define the Doctrine Entity Mapping](https://symfony.com/doc/current/best_practices.html#use-attributes-to-define-the-doctrine-entity-mapping "Permalink to this headline")

Doctrine entities are plain PHP objects that you store in some "database". Doctrine only knows about your entities through the mapping metadata configured for your model classes.

Doctrine supports several metadata formats, but it's recommended to use PHP attributes because they are by far the most convenient and agile way of setting up and looking for mapping information.

[Controllers](https://symfony.com/doc/current/best_practices.html#controllers "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------

### [Make your Controller Extend the `AbstractController` Base Controller](https://symfony.com/doc/current/best_practices.html#make-your-controller-extend-the-abstractcontroller-base-controller "Permalink to this headline")

Symfony provides a [base controller](https://symfony.com/doc/current/controller.html#the-base-controller-classes-services) which includes shortcuts for the most common needs such as rendering templates or checking security permissions.

Extending your controllers from this base controller couples your application to Symfony. Coupling is generally wrong, but it may be OK in this case because controllers shouldn't contain any business logic. Controllers should contain nothing more than a few lines of _glue-code_, so you are not coupling the important parts of your application.

### [Use Attributes to Configure Routing, Caching, and Security](https://symfony.com/doc/current/best_practices.html#use-attributes-to-configure-routing-caching-and-security "Permalink to this headline")

Using attributes for routing, caching, and security simplifies configuration. You don't need to browse several files created with different formats (YAML, PHP): all the configuration is just where you require it, and it only uses one format.

### [Use Dependency Injection to Get Services](https://symfony.com/doc/current/best_practices.html#use-dependency-injection-to-get-services "Permalink to this headline")

If you extend the base `AbstractController`, you can only get access to the most common services (e.g `twig`, `router`, `doctrine`, etc.), directly from the container via `$this->container->get()`. Instead, you must use dependency injection to fetch services by [type-hinting action method arguments](https://symfony.com/doc/current/controller.html#controller-accessing-services) or constructor arguments.

### [Use Entity Value Resolvers If They Are Convenient](https://symfony.com/doc/current/best_practices.html#use-entity-value-resolvers-if-they-are-convenient "Permalink to this headline")

If you're using [Doctrine](https://symfony.com/doc/current/doctrine.html), then you can _optionally_ use the [EntityValueResolver](https://symfony.com/doc/current/doctrine.html#doctrine-entity-value-resolver) to automatically query for an entity and pass it as an argument to your controller. It will also show a 404 page if no entity can be found.

If the logic to get an entity from a route variable is more complex, instead of configuring the EntityValueResolver, it's better to make the Doctrine query inside the controller (e.g. by calling to a [Doctrine repository method](https://symfony.com/doc/current/doctrine.html)).

[Templates](https://symfony.com/doc/current/best_practices.html#templates "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

### [Use Snake Case for Template Names and Variables](https://symfony.com/doc/current/best_practices.html#use-snake-case-for-template-names-and-variables "Permalink to this headline")

Use lowercase snake_case for template names, directories, and variables (e.g. `user_profile` instead of `userProfile` and `product/edit_form.html.twig` instead of `Product/EditForm.html.twig`).

### [Prefix Template Fragments with an Underscore](https://symfony.com/doc/current/best_practices.html#prefix-template-fragments-with-an-underscore "Permalink to this headline")

Template fragments, also called _"partial templates"_, allow you to [reuse template contents](https://symfony.com/doc/current/templates.html#templates-reuse-contents). Prefix their names with an underscore to better differentiate them from complete templates (e.g. `_user_metadata.html.twig` or `_caution_message.html.twig`).

[Forms](https://symfony.com/doc/current/best_practices.html#forms "Permalink to this headline")
-----------------------------------------------------------------------------------------------

### [Define your Forms as PHP Classes](https://symfony.com/doc/current/best_practices.html#define-your-forms-as-php-classes "Permalink to this headline")

Creating [forms in classes](https://symfony.com/doc/current/forms.html#creating-forms-in-classes) allows reusing them in different parts of the application. Besides, not creating forms in controllers simplifies the code and maintenance of the controllers.

### [Add Form Buttons in Templates](https://symfony.com/doc/current/best_practices.html#add-form-buttons-in-templates "Permalink to this headline")

Form classes should be agnostic to where they will be used. For example, the button of a form used to both create and edit items should change from "Add new" to "Save changes" depending on where it's used.

Instead of adding buttons in form classes or the controllers, it's recommended to add buttons in the templates. This also improves the separation of concerns because the button styling (CSS class and other attributes) is defined in the template instead of in a PHP class.

However, if you create a [form with multiple submit buttons](https://symfony.com/doc/current/forms.html#processing-forms-multiple-buttons) you should define them in the controller instead of the template. Otherwise, you won't be able to check which button was clicked when handling the form in the controller.

### [Define Validation Constraints on the Underlying Object](https://symfony.com/doc/current/best_practices.html#define-validation-constraints-on-the-underlying-object "Permalink to this headline")

Attaching [validation constraints](https://symfony.com/doc/current/reference/constraints.html) to form fields instead of to the mapped object prevents the validation from being reused in other forms or other places where the object is used.

### [Use a Single Action to Render and Process the Form](https://symfony.com/doc/current/best_practices.html#use-a-single-action-to-render-and-process-the-form "Permalink to this headline")

[Rendering forms](https://symfony.com/doc/current/forms.html#rendering-forms) and [processing forms](https://symfony.com/doc/current/forms.html#processing-forms) are two of the main tasks when handling forms. Both are too similar (most of the time, almost identical), so it's much simpler to let a single controller action handle both.

[Internationalization](https://symfony.com/doc/current/best_practices.html#internationalization "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

### [Use the XLIFF Format for Your Translation Files](https://symfony.com/doc/current/best_practices.html#use-the-xliff-format-for-your-translation-files "Permalink to this headline")

Of all the translation formats supported by Symfony (PHP, Qt, `.po`, `.mo`, JSON, CSV, INI, etc.), `XLIFF` and `gettext` have the best support in the tools used by professional translators. And since it's based on XML, you can validate `XLIFF` file contents as you write them.

Symfony also supports notes in XLIFF files, making them more user-friendly for translators. At the end, good translations are all about context, and these XLIFF notes allow you to define that context.

### [Use Keys for Translations Instead of Content Strings](https://symfony.com/doc/current/best_practices.html#use-keys-for-translations-instead-of-content-strings "Permalink to this headline")

Using keys simplifies the management of the translation files because you can change the original contents in templates, controllers, and services without having to update all the translation files.

Keys should always describe their _purpose_ and _not_ their location. For example, if a form has a field with the label "Username", then a nice key would be `label.username`, _not_`edit_form.label.username`.

[Security](https://symfony.com/doc/current/best_practices.html#security "Permalink to this headline")
-----------------------------------------------------------------------------------------------------

### [Define a Single Firewall](https://symfony.com/doc/current/best_practices.html#define-a-single-firewall "Permalink to this headline")

Unless you have two legitimately different authentication systems and users (e.g. form login for the main site and a token system for your API only), it's recommended to have only one firewall to keep things simple.

### [Use the `auto` Password Hasher](https://symfony.com/doc/current/best_practices.html#use-the-auto-password-hasher "Permalink to this headline")

The [auto password hasher](https://symfony.com/doc/current/security/passwords.html#reference-security-encoder-auto) automatically selects the best possible encoder/hasher depending on your PHP installation. Currently, the default auto hasher is `bcrypt`.

### [Use Voters to Implement Fine-grained Security Restrictions](https://symfony.com/doc/current/best_practices.html#use-voters-to-implement-fine-grained-security-restrictions "Permalink to this headline")

If your security logic is complex, you should create custom [security voters](https://symfony.com/doc/current/security/voters.html) instead of defining long expressions inside the `#[Security]` attribute.

[Web Assets](https://symfony.com/doc/current/best_practices.html#web-assets "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

### [Use AssetMapper to Manage Web Assets](https://symfony.com/doc/current/best_practices.html#use-assetmapper-to-manage-web-assets "Permalink to this headline")

Web assets are the CSS, JavaScript, and image files that make the frontend of your site look and work great. [AssetMapper](https://symfony.com/doc/current/frontend/asset_mapper.html) lets you write modern JavaScript and CSS without the complexity of using a bundler such as [Webpack](https://webpack.js.org/) (directly or via [Webpack Encore](https://symfony.com/doc/current/frontend/encore/index.html)).

[Tests](https://symfony.com/doc/current/best_practices.html#tests "Permalink to this headline")
-----------------------------------------------------------------------------------------------

### [Smoke Test your URLs](https://symfony.com/doc/current/best_practices.html#smoke-test-your-urls "Permalink to this headline")

In software engineering, [smoke testing](https://en.wikipedia.org/wiki/Smoke_testing_(software)) consists of _"preliminary testing to reveal simple failures severe enough to reject a prospective software release"_. Using [PHPUnit data providers](https://docs.phpunit.de/en/9.6/writing-tests-for-phpunit.html#data-providers) you can define a functional test that checks that all application URLs load successfully:

Add this test while creating your application because it requires little effort and checks that none of your pages returns an error. Later, you'll add more specific tests for each page.

### [Hard-code URLs in a Functional Test](https://symfony.com/doc/current/best_practices.html#hard-code-urls-in-a-functional-test "Permalink to this headline")

In Symfony applications, it's recommended to [generate URLs](https://symfony.com/doc/current/routing.html#routing-generating-urls) using routes to automatically update all links when a URL changes. However, if a public URL changes, users won't be able to browse it unless you set up a redirection to the new URL.

That's why it's recommended to use raw URLs in tests instead of generating them from routes. Whenever a route changes, tests will fail, and you'll know that you must set up a redirection.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
