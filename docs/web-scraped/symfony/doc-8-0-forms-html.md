# Source: https://symfony.com/doc/8.0/forms.html

Title: Forms (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/forms.html

Markdown Content:
Forms (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/forms.html#main-content)

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
3. Forms

 Search Symfony Docs

Version:

Table of Contents

* [Installation](https://symfony.com/doc/8.0/forms.html#installation)
* [Understanding How Forms Work](https://symfony.com/doc/8.0/forms.html#understanding-how-forms-work)
  * [The Data Transformation Lifecycle](https://symfony.com/doc/8.0/forms.html#the-data-transformation-lifecycle)

* [Usage](https://symfony.com/doc/8.0/forms.html#usage)
  * [Form Types](https://symfony.com/doc/8.0/forms.html#form-types)

* [Building Forms](https://symfony.com/doc/8.0/forms.html#building-forms)
  * [Creating Forms in Controllers](https://symfony.com/doc/8.0/forms.html#creating-forms-in-controllers)
  * [Creating Form Classes](https://symfony.com/doc/8.0/forms.html#creating-form-classes)
  * [Mapping Fields to Object Properties](https://symfony.com/doc/8.0/forms.html#mapping-fields-to-object-properties)

* [Rendering Forms](https://symfony.com/doc/8.0/forms.html#rendering-forms)
* [Processing Forms](https://symfony.com/doc/8.0/forms.html#processing-forms)
  * [Accessing Form Data](https://symfony.com/doc/8.0/forms.html#accessing-form-data)
  * [Using the submit() Method](https://symfony.com/doc/8.0/forms.html#using-the-submit-method)
  * [Handling Multiple Submit Buttons](https://symfony.com/doc/8.0/forms.html#handling-multiple-submit-buttons)

* [Validating Forms](https://symfony.com/doc/8.0/forms.html#validating-forms)
  * [Disabling Validation](https://symfony.com/doc/8.0/forms.html#disabling-validation)

* [Other Common Form Features](https://symfony.com/doc/8.0/forms.html#other-common-form-features)
  * [Passing Options to Forms](https://symfony.com/doc/8.0/forms.html#passing-options-to-forms)
  * [Form Type Options](https://symfony.com/doc/8.0/forms.html#form-type-options)
  * [Changing the Action and HTTP Method](https://symfony.com/doc/8.0/forms.html#changing-the-action-and-http-method)
  * [Changing the Form Field Names and Ids](https://symfony.com/doc/8.0/forms.html#changing-the-form-field-names-and-ids)
  * [Client-Side HTML Validation](https://symfony.com/doc/8.0/forms.html#client-side-html-validation)
  * [Form Type Guessing](https://symfony.com/doc/8.0/forms.html#form-type-guessing)
  * [Unmapped Fields](https://symfony.com/doc/8.0/forms.html#unmapped-fields)
  * [Extra fields](https://symfony.com/doc/8.0/forms.html#extra-fields)

* [Using a Form without a Data Class](https://symfony.com/doc/8.0/forms.html#using-a-form-without-a-data-class)
  * [Adding Validation](https://symfony.com/doc/8.0/forms.html#adding-validation)

* [Troubleshooting](https://symfony.com/doc/8.0/forms.html#troubleshooting)
  * [Why Doesn't My Field Value Display?](https://symfony.com/doc/8.0/forms.html#why-doesn-t-my-field-value-display)
  * [Why Doesn't My Submitted Data Save to the Object?](https://symfony.com/doc/8.0/forms.html#why-doesn-t-my-submitted-data-save-to-the-object)
  * [Why Does getData() Return null After Submission?](https://symfony.com/doc/8.0/forms.html#why-does-getdata-return-null-after-submission)

* [Learn more](https://symfony.com/doc/8.0/forms.html#learn-more)

Forms
=====

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/forms.rst)

Screencast

Do you prefer video tutorials? Check out the [Symfony Forms screencast series](https://symfonycasts.com/screencast/symfony-forms).

Creating and processing HTML forms is hard and repetitive. You need to deal with rendering HTML form fields, validating submitted data, mapping the form data into objects and a lot more. Symfony includes a powerful form feature that provides all these features and many more for truly complex scenarios.

[Installation](https://symfony.com/doc/8.0/forms.html#installation "Permalink to this headline")
------------------------------------------------------------------------------------------------

In applications using [Symfony Flex](https://symfony.com/doc/8.0/setup.html#symfony-flex), run this command to install the form feature before using it:

1`$ composer require symfony/form`

[Understanding How Forms Work](https://symfony.com/doc/8.0/forms.html#understanding-how-forms-work "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

Before diving into the code, it's helpful to understand the mental model behind Symfony forms. Think of a form as a **bidirectional mapping layer** between your PHP objects (or arrays) and HTML forms.

This mapping works in two directions:

1. **Object to HTML**: When rendering a form, Symfony reads data from your object and turns it into HTML fields that users can edit;
2. **HTML to Object**: When processing a submission, Symfony takes the raw values from the HTTP request (typically strings) and converts them back into the appropriate PHP types on your object.

This flow is the core of the Form component. From simple text fields to complex nested collections, everything follows the same pattern.

### [The Data Transformation Lifecycle](https://symfony.com/doc/8.0/forms.html#the-data-transformation-lifecycle "Permalink to this headline")

Data in a form goes through three representations, often called **data layers**:

**Model Data** The data in the format your application uses. For example, a `DateTime` object, a Doctrine entity, or a custom value object. This is what you pass to `createForm()` and what you get back after a successful submission via `getData()`. **Normalized Data** An intermediate representation that normalizes the model data. For most field types, this is identical to the model data. However, for some types it's different. For example, `DateType` is normalized as an array with `year`, `month`, and `day` keys. **View Data** The format used to populate HTML form fields and received from user submissions. In most cases, this is string-based (or arrays of strings), because browsers submit text. Some fields may use other representations or remain empty for security reasons (for example, file inputs).
High-level flow:

**Form Rendering**

1. Start with model data from your object.
2. Model transformers convert it to normalized data.
3. View transformers convert it to view data (typically strings).
4. Symfony renders the corresponding HTML widgets.

**Form Submission**

1. Symfony reads raw values from the HTTP request (typically strings).
2. View transformers reverse the data into normalized data.
3. Model transformers reverse the data into model data.
4. The data is written back to the underlying object or array.

For a `DateType` field configured to render as three `<select>` elements:

* **Model data**: a `DateTime` object;
* **Norm data**: an array like `['year' => 2026, 'month' => 10, 'day' => 18]`; (values are integers)
* **View data**: an array like `['year' => '2026', 'month' => '10', 'day' => '18']` (values are strings, as submitted by the browser).

Most of the time you don't need to think about these layers. They become relevant when debugging why a field doesn't display or submit correctly, or when creating custom [data transformers](https://symfony.com/doc/8.0/form/data_transformers.html).

[Usage](https://symfony.com/doc/8.0/forms.html#usage "Permalink to this headline")
----------------------------------------------------------------------------------

The recommended workflow when working with Symfony forms is the following:

1. **Build the form** in a Symfony controller or using a dedicated form class;
2. **Render the form** in a template so the user can edit and submit it;
3. **Process the form** to validate the submitted data, transform it into PHP data and do something with it (e.g. persist it in a database).

Each of these steps is explained in detail in the next sections. To make examples easier to follow, all of them assume that you're building a small Todo list application that displays "tasks".

Users create and edit tasks using Symfony forms. Each task is an instance of the following `Task` class:

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
// src/Entity/Task.php
namespace App\Entity;

class Task
{
    protected string $task;

    protected ?\DateTimeInterface $dueDate;

    public function getTask(): string
    {
        return $this->task;
    }

    public function setTask(string $task): void
    {
        $this->task = $task;
    }

    public function getDueDate(): ?\DateTimeInterface
    {
        return $this->dueDate;
    }

    public function setDueDate(?\DateTimeInterface $dueDate): void
    {
        $this->dueDate = $dueDate;
    }
}
```

This class is a "plain-old-PHP-object" because, so far, it has nothing to do with Symfony or any other library. It's a normal PHP object that directly solves a problem inside _your_ application (i.e. the need to represent a task in your application). But you can also edit [Doctrine entities](https://symfony.com/doc/8.0/doctrine.html) in the same way.

### [Form Types](https://symfony.com/doc/8.0/forms.html#form-types "Permalink to this headline")

Before creating your first Symfony form, it's important to understand the concept of "form type". In other projects, it's common to differentiate between "forms" and "form fields". In Symfony, all of them are "form types":

* a single `<input type="text">` form field is a "form type" (e.g. `TextType`);
* a group of several HTML fields used to input a postal address is a "form type" (e.g. `PostalAddressType`);
* an entire `<form>` with multiple fields to edit a user profile is a "form type" (e.g. `UserProfileType`).

This unified concept makes the Form component more **flexible**. You can compose complex forms from simpler types, embed forms within forms, and reuse the same type definition across your application.

**The Form Type Hierarchy**

Every form type has a parent type. The parent determines the base behavior, options, and rendering that your type inherits. Here's a simplified view:

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
FormType        (the root parent of all types)
├─ TextType    (renders a text input)
│  ├─ EmailType
│  ├─ PasswordType
│  ├─ ...
│  └─ UrlType
├─ ChoiceType  (renders select, radio, or checkboxes)
│  ├─ CountryType
│  ├─ EntityType
│  └─ ...
├─ DateType    (renders single or multiple fields for date input)
│  └─ ...
└─ ...
```

When you create a custom form type and specify a parent (via `getParent()`), your type inherits options, template blocks, and behavior from that parent. This is why `EmailType` reuses the rendering and options from `TextType`.

There are tens of [form types provided by Symfony](https://symfony.com/doc/8.0/reference/forms/types.html) and you can also [create your own form types](https://symfony.com/doc/8.0/form/create_custom_field_type.html).

Tip

You can use the `debug:form` to list all the available types, type extensions and type guessers in your application:

1
2
3
4
5
6
7
8

```
$ php bin/console debug:form

# pass the form type FQCN to only show the options for that type, its parents and extensions
# For built-in types, you can pass the short classname instead of the FQCN
$ php bin/console debug:form BirthdayType

# pass also an option name to only display the full definition of that option
$ php bin/console debug:form BirthdayType label_attr
```

[Building Forms](https://symfony.com/doc/8.0/forms.html#building-forms "Permalink to this headline")
----------------------------------------------------------------------------------------------------

Symfony provides a "form builder" object which allows you to describe the form fields using a fluent interface. Later, this builder creates the actual form object used to render and process contents.

### [Creating Forms in Controllers](https://symfony.com/doc/8.0/forms.html#creating-forms-in-controllers "Permalink to this headline")

If your controller extends from the [AbstractController](https://symfony.com/doc/8.0/controller.html#the-base-controller-class-services), use the `createFormBuilder()` helper:

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
// src/Controller/TaskController.php
namespace App\Controller;

use App\Entity\Task;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

class TaskController extends AbstractController
{
    public function new(Request $request): Response
    {
        // creates a task object and initializes some data for this example
        $task = new Task();
        $task->setTask('Write a blog post');
        $task->setDueDate(new \DateTimeImmutable('tomorrow'));

        $form = $this->createFormBuilder($task)
            ->add('task', TextType::class)
            ->add('dueDate', DateType::class)
            ->add('save', SubmitType::class, ['label' => 'Create Task'])
            ->getForm();

        // ...
    }
}
```

If your controller does not extend from `AbstractController`, you'll need to [fetch services in your controller](https://symfony.com/doc/8.0/controller.html#controller-accessing-services) and use the `createBuilder()` method of the `form.factory` service.

In this example, you've added two fields to your form - `task` and `dueDate` - corresponding to the `task` and `dueDate` properties of the `Task` class. You've also assigned each a [form type](https://symfony.com/doc/8.0/forms.html#form-types) (e.g. `TextType` and `DateType`), represented by its fully qualified class name. Finally, you added a submit button with a custom label for submitting the form to the server.

### [Creating Form Classes](https://symfony.com/doc/8.0/forms.html#creating-form-classes "Permalink to this headline")

Symfony recommends putting as little logic as possible in controllers. That's why it's better to move complex forms to dedicated classes instead of defining them in controller actions. Besides, forms defined in classes can be reused in multiple actions and services.

Form classes are [form types](https://symfony.com/doc/8.0/forms.html#form-types) that implement [FormTypeInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormTypeInterface.php "Symfony\Component\Form\FormTypeInterface"). However, it's better to extend from [AbstractType](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/AbstractType.php "Symfony\Component\Form\AbstractType"), which already implements the interface and provides some utilities:

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
// src/Form/Type/TaskType.php
namespace App\Form\Type;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;

class TaskType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('task', TextType::class)
            ->add('dueDate', DateType::class)
            ->add('save', SubmitType::class)
        ;
    }
}
```

Tip

Install the [MakerBundle](https://symfony.com/doc/current/bundles/SymfonyMakerBundle/index.html) in your project to generate form classes using the `make:form` and `make:registration-form` commands.

The form class contains all the directions needed to create the task form. In controllers extending from the [AbstractController](https://symfony.com/doc/8.0/controller.html#the-base-controller-class-services), use the `createForm()` helper (otherwise, use the `create()` method of the `form.factory` service):

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
// src/Controller/TaskController.php
namespace App\Controller;

use App\Form\Type\TaskType;
// ...

class TaskController extends AbstractController
{
    public function new(): Response
    {
        // creates a task object and initializes some data for this example
        $task = new Task();
        $task->setTask('Write a blog post');
        $task->setDueDate(new \DateTimeImmutable('tomorrow'));

        $form = $this->createForm(TaskType::class, $task);

        // ...
    }
}
```

Every form needs to know the name of the class that holds the underlying data (e.g. `App\Entity\Task`). Usually, this is guessed based on the object passed to the second argument to `createForm()` (i.e. `$task`). Later, when you begin [embedding forms](https://symfony.com/doc/8.0/form/embedded.html), this will no longer be sufficient.

So, while not always necessary, it's generally a good idea to explicitly specify the `data_class` option by adding the following to your form type class:

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
// src/Form/Type/TaskType.php
namespace App\Form\Type;

use App\Entity\Task;
use Symfony\Component\OptionsResolver\OptionsResolver;
// ...

class TaskType extends AbstractType
{
    // ...

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => Task::class,
        ]);
    }
}
```

### [Mapping Fields to Object Properties](https://symfony.com/doc/8.0/forms.html#mapping-fields-to-object-properties "Permalink to this headline")

By default, a form field named `dueDate` reads and writes the `dueDate` property on your object. This uses the [PropertyAccess component](https://symfony.com/doc/8.0/components/property_access.html), which can work with public properties and common accessor names (`get*()`, `is*()`, `has*()`, `set*()`).

The `property_path` option lets you customize this mapping.

**Mapping to a Different Property**

If your form field name doesn't match the object property:

1
2
3
4

```
$builder->add('deadline', DateType::class, [
    // this field will read/write the 'dueDate' property
    'property_path' => 'dueDate',
]);
```

**Mapping to Nested Properties**

You can access nested object properties using dot notation:

1
2
3
4

```
// assuming Task::getCategory() returns a Category object with getName()/setName()
$builder->add('categoryName', TextType::class, [
    'property_path' => 'category.name',
]);
```

For fields that shouldn't be written back to the underlying data, use [unampped fields](https://symfony.com/doc/8.0/forms.html#form-unmapped-fields).

#### [Injecting Services in Form Classes](https://symfony.com/doc/8.0/forms.html#injecting-services-in-form-classes "Permalink to this headline")

Form classes are regular services, which means you can inject other services using [autowiring](https://symfony.com/doc/8.0/service_container/autowiring.html):

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
// src/Form/Type/TaskType.php
namespace App\Form\Type;

use App\Repository\CategoryRepository;
use Symfony\Component\Form\AbstractType;
// ...

class TaskType extends AbstractType
{
    public function __construct(
        private CategoryRepository $categoryRepository,
    ) {
    }

    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        // use $this->categoryRepository to access the repository
    }
}
```

If you're using the [default services.yaml configuration](https://symfony.com/doc/8.0/service_container.html#service-container-services-load-example), this works automatically. See [How to Create a Custom Form Field Type](https://symfony.com/doc/8.0/form/create_custom_field_type.html) for more information about injecting services in custom form types.

[Rendering Forms](https://symfony.com/doc/8.0/forms.html#rendering-forms "Permalink to this headline")
------------------------------------------------------------------------------------------------------

Now that the form has been created, the next step is to render it:

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
// src/Controller/TaskController.php
namespace App\Controller;

use App\Entity\Task;
use App\Form\Type\TaskType;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

class TaskController extends AbstractController
{
    public function new(Request $request): Response
    {
        $task = new Task();
        // ...

        $form = $this->createForm(TaskType::class, $task);

        return $this->render('task/new.html.twig', [
            'form' => $form,
        ]);
    }
}
```

Internally, the `render()` method calls `$form->createView()` to transform the form into a _form view_ instance.

Then, use some [form helper functions](https://symfony.com/doc/8.0/form/form_customization.html#reference-form-twig-functions) to render the form contents:

1
2

```
{# templates/task/new.html.twig #}
{{ form(form) }}
```

That's it! The [form() function](https://symfony.com/doc/8.0/form/form_customization.html#reference-forms-twig-form) renders all fields _and_ the `<form>` start and end tags. By default, the form method is `POST` and the target URL is the same that displayed the form, but [you can change both](https://symfony.com/doc/8.0/forms.html#forms-change-action-method).

Notice how the rendered `task` input field has the value of the `task` property from the `$task` object (i.e. "Write a blog post"). This is the first job of a form: to take data from an object and translate it into a format that's suitable for being rendered in an HTML form.

Tip

The form system is smart enough to access the value of the protected `task` property via the `getTask()` and `setTask()` methods on the `Task` class. Unless a property is public, it _must_ have a "getter" and "setter" method so that Symfony can get and put data onto the property. For a boolean property, you can use an "isser" or "hasser" method (e.g. `isPublished()` or `hasReminder()`) instead of a getter (e.g. `getPublished()` or `getReminder()`).

As short as this rendering is, it's not very flexible. Usually, you'll need more control about how the entire form or some of its fields look. For example, thanks to the [Bootstrap 5 integration with Symfony forms](https://symfony.com/doc/8.0/form/bootstrap5.html) you can set this option to generate forms compatible with the Bootstrap 5 CSS framework:

YAML PHP

1
2
3

```
# config/packages/twig.yaml
twig:
    form_themes: ['bootstrap_5_layout.html.twig']
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
// config/packages/twig.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'twig' => [
        'form_themes' => ['bootstrap_5_layout.html.twig'],
    ],
]);
```

The [built-in Symfony form themes](https://symfony.com/doc/8.0/form/form_themes.html#symfony-builtin-forms) include Bootstrap 3, 4 and 5, Foundation 5 and 6, as well as Tailwind 2. You can also [create your own Symfony form theme](https://symfony.com/doc/8.0/form/form_themes.html#create-your-own-form-theme).

In addition to form themes, Symfony allows you to [customize the way fields are rendered](https://symfony.com/doc/8.0/form/form_customization.html) with multiple functions to render each field part separately (widgets, labels, errors, help messages, etc.)

[Processing Forms](https://symfony.com/doc/8.0/forms.html#processing-forms "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

The [recommended way of processing forms](https://symfony.com/doc/8.0/best_practices.html#best-practice-handle-form) is to use a single action for both rendering the form and handling the form submit. You can use separate actions, but using one action simplifies everything while keeping the code concise and maintainable.

Processing a form means to translate user-submitted data back to the properties of an object. To make this happen, the submitted data from the user must be written into the form object:

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

```
// src/Controller/TaskController.php

// ...
use Symfony\Component\HttpFoundation\Request;

class TaskController extends AbstractController
{
    public function new(Request $request): Response
    {
        // set up a fresh $task object (remove the example data)
        $task = new Task();

        $form = $this->createForm(TaskType::class, $task);

        $form->handleRequest($request);
        if ($form->isSubmitted() && $form->isValid()) {
            // $form->getData() holds the submitted values
            // but, the original `$task` variable has also been updated
            $task = $form->getData();

            // ... perform some action, such as saving the task to the database

            return $this->redirectToRoute('task_success');
        }

        return $this->render('task/new.html.twig', [
            'form' => $form,
        ]);
    }
}
```

This controller follows a common pattern for handling forms and has three possible paths:

1. When initially loading the page in a browser, the form hasn't been submitted yet and `$form->isSubmitted()` returns `false`. So, the form is created and rendered;
2. When the user submits the form, [handleRequest()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20handleRequest "Symfony\Component\Form\FormInterface::handleRequest()") recognizes this and immediately writes the submitted data back into the `task` and `dueDate` properties of the `$task` object. Then this object is validated (validation is explained in the next section). If it is invalid, [isValid()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20isValid "Symfony\Component\Form\FormInterface::isValid()") returns `false` and the form is rendered again, but now with validation errors.

By passing `$form` to the `render()` method (instead of `$form->createView()`), the response code is automatically set to [HTTP 422 Unprocessable Content](https://www.rfc-editor.org/rfc/rfc9110.html#name-422-unprocessable-content). This ensures compatibility with tools relying on the HTTP specification, like [Symfony UX Turbo](https://ux.symfony.com/turbo);

1. When the user submits the form with valid data, the submitted data is again written into the form, but this time [isValid()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20isValid "Symfony\Component\Form\FormInterface::isValid()") returns `true`. Now you have the opportunity to perform some actions using the `$task` object (e.g. persisting it to the database) before redirecting the user to some other page (e.g. a "thank you" or "success" page);

Note

Redirecting a user after a successful form submission is a best practice that prevents the user from being able to hit the "Refresh" button of their browser and re-post the data.

### [Accessing Form Data](https://symfony.com/doc/8.0/forms.html#accessing-form-data "Permalink to this headline")

You'll use the `getData()` method most often to access the form's data, but Symfony forms also provide methods to access data at [each layer](https://symfony.com/doc/8.0/forms.html#form-data-lifecycle):

`getData()` Returns the **model data**. This is the method you'll use most often. After submission, it returns the populated object (or array) with all the submitted values transformed into their proper PHP types. `getNormData()` Returns the **normalized data**. Useful when debugging transformer issues or when you need the intermediate representation. `getViewData()` Returns the **view data**. This is what gets rendered into HTML fields and what comes back from user submissions (before transformation).

See also

When adding [extra fields](https://symfony.com/doc/8.0/forms.html#form-extra-fields) to the form, you can also use the `getExtraData()` method to get any submitted data that doesn't correspond to a form field.

Example showing these methods in action:

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
// after form submission
$form->handleRequest($request);

if ($form->isSubmitted()) {
    // the populated Task object
    $task = $form->getData();

    // for a DateType field, this might be ['year' => 2024, 'month' => 6, ...]
    $normData = $form->get('dueDate')->getNormData();

    // the raw submitted values (usually strings): ['year' => '2024', 'month' => '6', ...]
    $viewData = $form->get('dueDate')->getViewData();
}
```

If a transformer fails, the form (or the affected field) may be marked as not synchronized. Check `isSynchronized()` and inspect field errors to understand what went wrong.

### [Using the submit() Method](https://symfony.com/doc/8.0/forms.html#using-the-submit-method "Permalink to this headline")

The [handleRequest()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20handleRequest "Symfony\Component\Form\FormInterface::handleRequest()") method is the recommended way to process forms. However, you can also use the [submit()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20submit "Symfony\Component\Form\FormInterface::submit()") method for finer control over when exactly your form is submitted and what data is passed to it:

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
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
// ...

public function new(Request $request): Response
{
    $task = new Task();
    $form = $this->createForm(TaskType::class, $task);

    if ($request->isMethod('POST')) {
        $form->submit($request->getPayload()->get($form->getName()));

        if ($form->isSubmitted() && $form->isValid()) {
            // perform some action...

            return $this->redirectToRoute('task_success');
        }
    }

    return $this->render('task/new.html.twig', [
        'form' => $form,
    ]);
}
```

The list of fields submitted with the `submit()` method must be the same as the fields defined by the form class. Otherwise, you'll see a form validation error:

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
public function new(Request $request): Response
{
    // ...

    if ($request->isMethod('POST')) {
        // '$json' represents payload data sent by React/Angular/Vue
        // the merge of parameters is needed to submit all form fields
        $form->submit(array_merge($json, $request->getPayload()->all()));

        // ...
    }

    // ...
}
```

Tip

Forms consisting of nested fields expect an array in [submit()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20submit "Symfony\Component\Form\FormInterface::submit()"). You can also submit individual fields by calling [submit()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20submit "Symfony\Component\Form\FormInterface::submit()") directly on the field:

1`$form->get('firstName')->submit('Fabien');`

Tip

When submitting a form via a "PATCH" request, you may want to update only a few submitted fields. To achieve this, you may pass an optional second boolean argument to `submit()`. Passing `false` will remove any missing fields within the form object. Otherwise, the missing fields will be set to `null`.

Warning

When the second parameter `$clearMissing` is `false`, like with the "PATCH" method, the validation will only apply to the submitted fields. If you need to validate all the underlying data, add the required fields manually so that they are validated:

1
2
3
4
5

```
// 'email' and 'username' are added manually to force their validation
$form->submit(array_merge(
    ['email' => null, 'username' => null],
    $request->getPayload()->all()
), false);
```

### [Handling Multiple Submit Buttons](https://symfony.com/doc/8.0/forms.html#handling-multiple-submit-buttons "Permalink to this headline")

When your form contains more than one submit button, you'll want to check which of the buttons was clicked to adapt the program flow in your controller. For example, if you add a second button with the caption "Save and Add" to your form:

1
2
3
4
5
6

```
$form = $this->createFormBuilder($task)
    ->add('task', TextType::class)
    ->add('dueDate', DateType::class)
    ->add('save', SubmitType::class, ['label' => 'Create Task'])
    ->add('saveAndAdd', SubmitType::class, ['label' => 'Save and Add'])
    ->getForm();
```

In your controller, use the button's [isClicked()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/ClickableInterface.php#:~:text=function%20isClicked "Symfony\Component\Form\ClickableInterface::isClicked()") method for querying if the "Save and Add" button was clicked:

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
if ($form->isSubmitted() && $form->isValid()) {
    // ... perform some action, such as saving the task to the database

    $nextAction = $form->get('saveAndAdd')->isClicked()
        ? 'task_new'
        : 'task_success';

    return $this->redirectToRoute($nextAction);
}
```

Alternatively you can use the [getClickedButton()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/Form.php#:~:text=function%20getClickedButton "Symfony\Component\Form\Form::getClickedButton()") method to get the clicked button's name:

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
if ($form->getClickedButton() && 'saveAndAdd' === $form->getClickedButton()->getName()) {
    // ...
}

// when using nested forms, two or more buttons can have the same name;
// in those cases, compare the button objects instead of the button names
if ($form->getClickedButton() === $form->get('saveAndAdd')) {
    // ...
}
```

[Validating Forms](https://symfony.com/doc/8.0/forms.html#validating-forms "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

In the previous section, you learned how a form can be submitted with valid or invalid data. In Symfony, the question isn't whether the "form" is valid, but whether or not the underlying object (`$task` in this example) is valid after the form has applied the submitted data to it. Calling `$form->isValid()` is a shortcut that asks the `$task` object whether or not it has valid data.

Before using validation, add support for it in your application:

1`$ composer require symfony/validator`

Validation is done by adding a set of rules, called (validation) constraints, to a class. You can add them either to the entity class or by using the [constraints option](https://symfony.com/doc/8.0/reference/forms/types/form.html#reference-form-option-constraints) of form types.

To see the first approach - adding constraints to the entity - in action, add the validation constraints, so that the `task` field cannot be empty, and the `dueDate` field cannot be empty, and must be a valid `DateTimeImmutable` object.

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

```
// src/Entity/Task.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;

class Task
{
    #[Assert\NotBlank]
    public string $task;

    #[Assert\NotBlank]
    #[Assert\Type(\DateTimeInterface::class)]
    protected \DateTimeInterface $dueDate;
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
# config/validator/validation.yaml
App\Entity\Task:
    properties:
        task:
            - NotBlank: ~
        dueDate:
            - NotBlank: ~
            - Type:
                type: \DateTimeInterface
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
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping
        https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Entity\Task">
        <property name="task">
            <constraint name="NotBlank"/>
        </property>
        <property name="dueDate">
            <constraint name="NotBlank"/>
            <constraint name="Type">
                <option name="type">\DateTimeInterface</option>
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
21

```
// src/Entity/Task.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class Task
{
    // ...

    public static function loadValidatorMetadata(ClassMetadata $metadata): void
    {
        $metadata->addPropertyConstraint('task', new Assert\NotBlank());

        $metadata->addPropertyConstraint('dueDate', new Assert\NotBlank());
        $metadata->addPropertyConstraint(
            'dueDate',
            new Assert\Type(\DateTimeInterface::class)
        );
    }
}
```

That's it! If you re-submit the form with invalid data, you'll see the corresponding errors printed out with the form.

To see the second approach - adding constraints to the form - refer to [this section](https://symfony.com/doc/8.0/forms.html#form-option-constraints). Both approaches can be used together.

### [Disabling Validation](https://symfony.com/doc/8.0/forms.html#disabling-validation "Permalink to this headline")

Sometimes it's useful to suppress the validation of a form altogether. For these cases, set the `validation_groups` option to `false`:

1
2
3
4
5
6
7
8

```
use Symfony\Component\OptionsResolver\OptionsResolver;

public function configureOptions(OptionsResolver $resolver): void
{
    $resolver->setDefaults([
        'validation_groups' => false,
    ]);
}
```

Note that when you do that, the form will still run basic integrity checks, for example whether an uploaded file was too large or whether non-existing fields were submitted.

The submission of extra form fields can be controlled with the [allow_extra_fields config option](https://symfony.com/doc/8.0/reference/forms/types/form.html#form-option-allow-extra-fields) and the maximum upload file size should be handled via your PHP and web server configuration.

You can also disable validation for specific submit buttons using `'validation_groups' => false`. This is useful in multi-step forms when you want a "Previous" button to save data without running validation:

1
2
3
4
5
6
7

```
$form = $this->createFormBuilder($task)
    // ...
    ->add('nextStep', SubmitType::class)
    ->add('previousStep', SubmitType::class, [
        'validation_groups' => false,
    ])
    ->getForm();
```

The form will still validate basic integrity constraints even when clicking "previousStep".

[Other Common Form Features](https://symfony.com/doc/8.0/forms.html#other-common-form-features "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------

### [Passing Options to Forms](https://symfony.com/doc/8.0/forms.html#passing-options-to-forms "Permalink to this headline")

If you [create forms in classes](https://symfony.com/doc/8.0/forms.html#creating-forms-in-classes), when building the form in the controller you can pass custom options to it as the third optional argument of `createForm()`:

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
// src/Controller/TaskController.php
namespace App\Controller;

use App\Form\Type\TaskType;
// ...

class TaskController extends AbstractController
{
    public function new(): Response
    {
        $task = new Task();
        // use some PHP logic to decide if this form field is required or not
        $dueDateIsRequired = ...;

        $form = $this->createForm(TaskType::class, $task, [
            'require_due_date' => $dueDateIsRequired,
        ]);

        // ...
    }
}
```

If you try to use the form now, you'll see an error message: _The option "require\_due\_date" does not exist._ That's because forms must declare all the options they accept using the `configureOptions()` method:

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
// src/Form/Type/TaskType.php
namespace App\Form\Type;

use Symfony\Component\OptionsResolver\OptionsResolver;
// ...

class TaskType extends AbstractType
{
    // ...

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            // ...,
            'require_due_date' => false,
        ]);

        // you can also define the allowed types, allowed values and
        // any other feature supported by the OptionsResolver component
        $resolver->setAllowedTypes('require_due_date', 'bool');
    }
}
```

Now you can use this new form option inside the `buildForm()` method:

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
// src/Form/Type/TaskType.php
namespace App\Form\Type;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\FormBuilderInterface;

class TaskType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            // ...
            ->add('dueDate', DateType::class, [
                'required' => $options['require_due_date'],
            ])
        ;
    }

    // ...
}
```

### [Form Type Options](https://symfony.com/doc/8.0/forms.html#form-type-options "Permalink to this headline")

Each [form type](https://symfony.com/doc/8.0/forms.html#form-types) has a number of options to configure it, as explained in the [Symfony form types reference](https://symfony.com/doc/8.0/reference/forms/types.html). Two commonly used options are `required` and `label`.

#### [The `required` Option](https://symfony.com/doc/8.0/forms.html#the-required-option "Permalink to this headline")

The most common option is the `required` option, which can be applied to any field. By default, this option is set to `true`, meaning that HTML5-ready browsers will require you to fill in all fields before submitting the form.

If you don't want this behavior, either [disable client-side validation](https://symfony.com/doc/8.0/forms.html#forms-html5-validation-disable) for the entire form or set the `required` option to `false` on one or more fields:

1
2
3

```
->add('dueDate', DateType::class, [
    'required' => false,
])
```

The `required` option does not perform any server-side validation. If a user submits a blank value for the field (either with an old browser or a web service, for example), it will be accepted as a valid value unless you also use Symfony's `NotBlank` or `NotNull` validation constraints.

#### [The `label` Option](https://symfony.com/doc/8.0/forms.html#the-label-option "Permalink to this headline")

By default, the label of form fields are the _humanized_ version of the property name (`user` ->`User`; `postalAddress` ->`Postal Address`). Set the `label` option on fields to define their labels explicitly:

1
2
3
4

```
->add('dueDate', DateType::class, [
    // set it to FALSE to not display the label for this field
    'label' => 'To Be Completed Before',
])
```

Tip

By default, `<label>` tags of required fields are rendered with a `required` CSS class, so you can display an asterisk by applying a CSS style:

1
2
3

```
label.required:before {
    content: "*";
}
```

### [Changing the Action and HTTP Method](https://symfony.com/doc/8.0/forms.html#changing-the-action-and-http-method "Permalink to this headline")

By default, the `<form>` tag is rendered with a `method="post"` attribute, and no `action` attribute. This means that the form is submitted via an HTTP POST request to the same URL under which it was rendered. When building the form, use the `setAction()` and `setMethod()` methods to change this:

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
// src/Controller/TaskController.php
namespace App\Controller;

// ...
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\Extension\Core\Type\TextType;

class TaskController extends AbstractController
{
    public function new(): Response
    {
        // ...

        $form = $this->createFormBuilder($task)
            ->setAction($this->generateUrl('target_route'))
            ->setMethod('GET')
            // ...
            ->getForm();

        // ...
    }
}
```

When building the form in a class, pass the action and method as form options:

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
// src/Controller/TaskController.php
namespace App\Controller;

use App\Form\TaskType;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
// ...

class TaskController extends AbstractController
{
    public function new(): Response
    {
        // ...

        $form = $this->createForm(TaskType::class, $task, [
            'action' => $this->generateUrl('target_route'),
            'method' => 'GET',
        ]);

        // ...
    }
}
```

Finally, you can override the action and method in the template by passing them to the `form()` or the `form_start()` helper functions:

1
2

```
{# templates/task/new.html.twig #}
{{ form_start(form, {'action': path('target_route'), 'method': 'GET'}) }}
```

Note

If the form's method is not `GET` or `POST`, but `PUT`, `PATCH` or `DELETE`, Symfony will insert a hidden field with the name `_method` that stores this method. The form will be submitted in a normal `POST` request, but [Symfony's routing](https://symfony.com/doc/8.0/routing.html) is capable of detecting the `_method` parameter and will interpret it as a `PUT`, `PATCH` or `DELETE` request. The [http_method_override](https://symfony.com/doc/8.0/reference/configuration/framework.html#configuration-framework-http_method_override) option must be enabled for this to work.

For security, you can restrict which HTTP methods can be overridden using the [allowed_http_method_override](https://symfony.com/doc/8.0/reference/configuration/framework.html#configuration-framework-allowed_http_method_override) option.

### [Changing the Form Field Names and Ids](https://symfony.com/doc/8.0/forms.html#changing-the-form-field-names-and-ids "Permalink to this headline")

When Symfony renders a form, it generates HTML `name` and `id` attributes for each field following specific conventions. Understanding these conventions helps when writing JavaScript, CSS selectors, or custom form themes.

In Twig templates, prefer `form.vars.full_name` and `form.vars.id` as the source of truth, instead of reconstructing names manually.

**The `name` Attribute**

Field names follow the pattern: `formName[fieldName]`. For nested forms, names are further nested: `formName[childForm][fieldName]`.

Given a `TaskType` form with a `dueDate` field:

1`$form = $this->createForm(TaskType::class, $task);`

The rendered HTML will have:

1`<input name="task[dueDate]" ...>`

For a `DateType` field that renders as three separate `<select>` elements:

1
2
3

```
<select name="task[dueDate][month]">...</select>
<select name="task[dueDate][day]">...</select>
<select name="task[dueDate][year]">...</select>
```

**The `id` Attribute**

The `id` attribute follows a similar pattern but uses underscores instead of brackets: `formName_fieldName`. For the examples above:

1
2
3
4
5
6

```
<input id="task_dueDate" ...>

<!-- or for DateType with multiple fields: -->
<select id="task_dueDate_month">...</select>
<select id="task_dueDate_day">...</select>
<select id="task_dueDate_year">...</select>
```

**Customizing the Form Name**

The default form name is derived from the form type class (for example, `TaskType` becomes `task` and `FooBarType` becomes `foo_bar`). You can customize this by returning a different value from the `getBlockPrefix()` method of your form type class.

You can also customize this by creating the form with the [createNamed()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormFactoryInterface.php#:~:text=function%20createNamed "Symfony\Component\Form\FormFactoryInterface::createNamed()") method:

1
2
3
4

```
// using FormFactory
$form = $formFactory->createNamed('my_task', TaskType::class, $task);

// this generates: <input name="my_task[dueDate]" id="my_task_dueDate">
```

To create a form without any name prefix (fields named directly like `dueDate` instead of `task[dueDate]`):

1`$form = $formFactory->createNamed('', TaskType::class, $task);`

### [Client-Side HTML Validation](https://symfony.com/doc/8.0/forms.html#client-side-html-validation "Permalink to this headline")

Thanks to HTML5, many browsers can natively enforce certain validation constraints on the client side. The most common validation is activated by adding a `required` attribute on fields that are required. For browsers that support HTML5, this will result in a native browser message being displayed if the user tries to submit the form with that field blank.

Generated forms take full advantage of this new feature by adding sensible HTML attributes that trigger the validation. The client-side validation, however, can be disabled by adding the `novalidate` attribute to the `<form>` tag or `formnovalidate` to the submit tag. This is especially useful when you want to test your server-side validation constraints, but are being prevented by your browser from, for example, submitting blank fields.

1
2
3
4

```
{# templates/task/new.html.twig #}
{{ form_start(form, {'attr': {'novalidate': 'novalidate'}}) }}
    {{ form_widget(form) }}
{{ form_end(form) }}
```

### [Form Type Guessing](https://symfony.com/doc/8.0/forms.html#form-type-guessing "Permalink to this headline")

If the object handled by the form includes validation constraints, Symfony can introspect that metadata to guess the type of your field. In the above example, Symfony can guess from the validation rules that the `task` field is a normal `TextType` field and the `dueDate` field is a `DateType` field.

To enable Symfony's "guessing mechanism", omit the second argument to the `add()` method, or pass `null` to it:

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
// src/Form/Type/TaskType.php
namespace App\Form\Type;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;

class TaskType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            // if you don't define field options, you can omit the second argument
            ->add('task')
            // if you define field options, pass NULL as second argument
            ->add('dueDate', null, ['required' => false])
            ->add('save', SubmitType::class)
        ;
    }
}
```

Warning

When using a specific [form validation group](https://symfony.com/doc/8.0/form/validation_groups.html), the field type guesser will still consider _all_ validation constraints when guessing your field types (including constraints that are not part of the validation group(s) being used).

#### [Form Type Options Guessing](https://symfony.com/doc/8.0/forms.html#form-type-options-guessing "Permalink to this headline")

When the guessing mechanism is enabled for some field, in addition to its form type, the following options will be guessed too:

`required` The `required` option is guessed based on the validation rules (i.e. is the field `NotBlank` or `NotNull`) or the Doctrine metadata (i.e. is the field `nullable`). This is very useful, as your client-side validation will automatically match your validation rules. `maxlength` If the field is some sort of text field, then the `maxlength` option attribute is guessed from the validation constraints (if `Length` or `Range` is used) or from the [Doctrine](https://symfony.com/doc/8.0/doctrine.html) metadata (via the field's length).
If you'd like to change one of the guessed values, override it in the options field array:

1`->add('task', null, ['attr' => ['maxlength' => 4]])`

See also

Besides guessing the form type, Symfony also guesses [validation constraints](https://symfony.com/doc/8.0/forms.html#validating-forms) if you're using a Doctrine entity. Read [Databases and the Doctrine ORM](https://symfony.com/doc/8.0/doctrine.html#automatic_object_validation) guide for more information.

### [Unmapped Fields](https://symfony.com/doc/8.0/forms.html#unmapped-fields "Permalink to this headline")

When editing an object via a form, all form fields are considered properties of the object. Any fields on the form that do not exist on the object will cause an exception to be thrown.

If you need extra fields in the form that won't be stored in the object (for example to add an _"I agree with these terms"_ checkbox), set the `mapped` option to `false` in those fields:

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
// ...
use Symfony\Component\Form\Extension\Core\Type\CheckboxType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\FormBuilderInterface;

class TaskType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('task')
            ->add('dueDate')
            ->add('agreeTerms', CheckboxType::class, ['mapped' => false])
            ->add('save', SubmitType::class)
        ;
    }
}
```

These "unmapped fields" can be set and accessed in a controller with:

1
2

```
$form->get('agreeTerms')->getData();
$form->get('agreeTerms')->setData(true);
```

Additionally, if there are any fields on the form that aren't included in the submitted data, those fields will be explicitly set to `null`.

### [Extra fields](https://symfony.com/doc/8.0/forms.html#extra-fields "Permalink to this headline")

By default, Symfony expects every submitted field to be defined in the form. Any additional submitted fields are treated as "extra fields". You can access them via the [FormInterface::getExtraData()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20getExtraData "Symfony\Component\Form\FormInterface::getExtraData()") method.

For example, consider a user creation form:

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
use App\User;
use Symfony\Component\Form\Extension\Core\Type\CheckboxType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\FormBuilderInterface;

class UserCreateType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('username', TextType::class)
            ->add('email', EmailType::class)
        ;
    }

    public function configureOptions(OptionsResolver $resolver)
    {
        $resolver->setDefaults([
            'data_class' => User::class,
        ]);
    }
}
```

You can render an additional input in the template without adding it to the form definition:

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
{# templates/user/create.html.twig #}
{{ form_start(form) }}
    {{ form_row(form.username) }}
    {{ form_row(form.email) }}

    {# hidden field to send an additional referral code #}
    <input type="hidden" name="{{ form.vars.full_name ~ '[referralCode]' }}" value="{{ referralCode }}"/>

    <button type="submit">Submit</button>
{{ form_end(form) }}
```

In this example, `referralCode` is submitted as an extra field and you can read it like this:

1
2

```
$extraData = $form->getExtraData();
$referralCode = $extraData['referralCode'] ?? null;
```

Note

To accept extra fields, set the [allow_extra_fields](https://symfony.com/doc/8.0/reference/forms/types/form.html#form-option-allow-extra-fields) option to `true`. Otherwise, the form will be invalid.

[Using a Form without a Data Class](https://symfony.com/doc/8.0/forms.html#using-a-form-without-a-data-class "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

In most applications, a form is tied to an object, and the fields of the form get and store their data on the properties of that object. This is what you've seen so far in this article with the `Task` class.

However, by default, a form actually assumes that you want to work with arrays of data, instead of an object. There are exactly two ways that you can change this behavior and tie the form to an object instead:

1. Pass an object when creating the form (as the first argument to `createFormBuilder()` or the second argument to `createForm()`);
2. Declare the `data_class` option on your form.

If you _don't_ do either of these, then the form will return the data as an array. In this example, since `$defaultData` is not an object (and no `data_class` option is set), `$form->getData()` ultimately returns an array:

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

```
// src/Controller/ContactController.php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
// ...

class ContactController extends AbstractController
{
    public function contact(Request $request): Response
    {
        $defaultData = ['message' => 'Type your message here'];
        $form = $this->createFormBuilder($defaultData)
            ->add('name', TextType::class)
            ->add('email', EmailType::class)
            ->add('message', TextareaType::class)
            ->add('send', SubmitType::class)
            ->getForm();

        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            // data is an array with "name", "email", and "message" keys
            $data = $form->getData();
        }

        // ... render the form
    }
}
```

Tip

You can also access POST values (in this case "name") directly through the request object, like so:

1`$request->getPayload()->get('name');`

Be advised, however, that in most cases using the `getData()` method is a better choice, since it returns the data (usually an object) after it's been transformed by the Form component.

### [Adding Validation](https://symfony.com/doc/8.0/forms.html#adding-validation "Permalink to this headline")

Usually, when you call `$form->handleRequest($request)`, the object is validated by reading the constraints that you applied to that class. If your form is mapped to an object, this is almost always the approach you want to use. See [Validation](https://symfony.com/doc/8.0/validation.html) for more details.

But if the form is not mapped to an object and you instead want to retrieve an array of your submitted data, there are two ways to add constraints to the form data.

#### [Constraints At Field Level](https://symfony.com/doc/8.0/forms.html#constraints-at-field-level "Permalink to this headline")

You can attach constraints to the individual fields. The overall approach is covered a bit more in [this validation article](https://symfony.com/doc/8.0/validation/raw_values.html), but here's a short example:

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
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\Validator\Constraints as Assert;

public function buildForm(FormBuilderInterface $builder, array $options): void
{
    $builder
        ->add('firstName', TextType::class, [
            'constraints' => new Assert\Length(['min' => 3]),
        ])
        ->add('lastName', TextType::class, [
            'constraints' => [
                new Assert\NotBlank(),
                new Assert\Length(['min' => 3]),
            ],
        ])
    ;
}
```

Tip

If you are using validation groups, you need to either reference the `Default` group when creating the form, or set the correct group on the constraint you are adding:

1`new NotBlank(['groups' => ['create', 'update']]);`

Tip

If the form is not mapped to an object, every object in your array of submitted data is validated using the `Symfony\Component\Validator\Constraints\Valid` constraint, unless you [disable validation](https://symfony.com/doc/8.0/forms.html#disabling-validation).

Warning

When a form is only partially submitted (for example, in an HTTP PATCH request), only the constraints from the submitted form fields will be evaluated.

#### [Constraints At Class Level](https://symfony.com/doc/8.0/forms.html#constraints-at-class-level "Permalink to this headline")

You can also add the constraints at the class level. This can be done by setting the `constraints` option in the `configureOptions()` method:

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
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;
use Symfony\Component\Validator\Constraints as Assert;

public function buildForm(FormBuilderInterface $builder, array $options): void
{
    $builder
        ->add('firstName', TextType::class)
        ->add('lastName', TextType::class);
}

public function configureOptions(OptionsResolver $resolver): void
{
    $resolver->setDefaults([
        'data_class' => null,
        'constraints' => new Assert\Collection([
            'firstName' => new Assert\Length(['min' => 3]),
            'lastName' => [
                new Assert\NotBlank(),
                new Assert\Length(['min' => 3]),
            ],
        ]),
    ]);
}
```

This means you can also do this when using the `createFormBuilder()` method in your controller:

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
use Symfony\Component\Validator\Constraints as Assert;

$form = $this->createFormBuilder($defaultData, [
        'constraints' => [
            'firstName' => new Assert\Length(['min' => 3]),
            'lastName' => [
                new Assert\NotBlank(),
                new Assert\Length(['min' => 3]),
            ],
        ],
    ])
    ->add('firstName', TextType::class)
    ->add('lastName', TextType::class)
    ->getForm();
```

#### [Conditional Constraints](https://symfony.com/doc/8.0/forms.html#conditional-constraints "Permalink to this headline")

It's possible to define field constraints that depend on the value of other fields (e.g. a field must not be blank when another field has a certain value). To achieve this, use the `expression` option of the [When constraint](https://symfony.com/doc/8.0/reference/constraints/When.html) to reference the other field:

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

```
use Symfony\Component\Validator\Constraints as Assert;

$builder
    ->add('how_did_you_hear', ChoiceType::class, [
        'required' => true,
        'label' => 'How did you hear about us?',
        'choices' => [
            'Search engine' => 'search_engine',
            'Friends' => 'friends',
            'Other' => 'other',
        ],
        'expanded' => true,
        'constraints' => [
            new Assert\NotBlank(),
        ]
    ])

    // this field is only required when 'how_did_you_hear' is 'other'
    ->add('other_text', TextType::class, [
        'required' => false,
        'label' => 'Please specify',
        'constraints' => [
            new Assert\When(
                expression: 'this.getParent().get("how_did_you_hear").getData() == "other"',
                constraints: [
                    new Assert\NotBlank(),
                ],
            )
        ],
    ])
;
```

See also

Another way to implement conditional constraints is to configure the `validation_groups` form option with a callable. See [Configuring Validation Groups in Forms](https://symfony.com/doc/8.0/form/validation_groups.html).

[Troubleshooting](https://symfony.com/doc/8.0/forms.html#troubleshooting "Permalink to this headline")
------------------------------------------------------------------------------------------------------

### [Why Doesn't My Field Value Display?](https://symfony.com/doc/8.0/forms.html#why-doesn-t-my-field-value-display "Permalink to this headline")

**Problem**: The form renders, but a field is empty even though the underlying data has a value.

**Common causes**:

1. The property is not readable (missing accessor, wrong name, or not public). For booleans, Symfony also looks for `is*()` and `has*()` accessors.
2. The field name doesn't match the property name. Use [property_path](https://symfony.com/doc/8.0/forms.html#form-property-path) if you need to map to a different property.
3. The data is set after creating the form. Populate your object _before_ passing it to `createForm()`:

1
2
3
4
5
6
7

```
// wrong: object populated after form creation
$form = $this->createForm(TaskType::class, $task);
$task->setTask('My task');

// correct: object populated before form creation
$task->setTask('My task');
$form = $this->createForm(TaskType::class, $task);
```  

### [Why Doesn't My Submitted Data Save to the Object?](https://symfony.com/doc/8.0/forms.html#why-doesn-t-my-submitted-data-save-to-the-object "Permalink to this headline")

**Problem**: The form submits, but the object properties remain unchanged.

**Common causes**:

1. The property is not writable (missing setter, wrong name, or not public).
2. It is an [unmapped field](https://symfony.com/doc/8.0/forms.html#form-unmapped-fields).
3. The form is not synchronized due to a transformation failure. Check `isSynchronized()` and inspect field errors.

### [Why Does `getData()` Return `null` After Submission?](https://symfony.com/doc/8.0/forms.html#why-does-getdata-return-null-after-submission "Permalink to this headline")

**Problem**: `$form->getData()` is `null` after handling the request.

**Common causes**:

1. No initial object (or default data) was provided and the form doesn't create one. Review the form's `data_class` and `empty_data` options.
2. A transformation failed and the form is not synchronized. Check `isSynchronized()` and field errors.
3. The form is not submitted or is invalid. Check `isSubmitted()` and `isValid()` before using the data.

[Learn more](https://symfony.com/doc/8.0/forms.html#learn-more "Permalink to this headline")
--------------------------------------------------------------------------------------------

When building forms, remember that the first goal of a form is to translate data from an object (`Task`) to an HTML form so that the user can modify that data. The second goal of a form is to take the data submitted by the user and to re-apply it to the object.

There's a lot more to learn and a lot of _powerful_ tricks in the Symfony forms:

Reference:

* [Form Types Reference](https://symfony.com/doc/8.0/reference/forms/types.html)

Advanced Features:

* [How to Upload Files](https://symfony.com/doc/8.0/controller/upload_file.html)
* [How to Implement CSRF Protection](https://symfony.com/doc/8.0/security/csrf.html)
* [How to Create a Custom Form Field Type](https://symfony.com/doc/8.0/form/create_custom_field_type.html)
* [How to Use Data Transformers](https://symfony.com/doc/8.0/form/data_transformers.html)
* [When and How to Use Data Mappers](https://symfony.com/doc/8.0/form/data_mappers.html)
* [How to Create a Form Type Extension](https://symfony.com/doc/8.0/form/create_form_type_extension.html)
* [Creating a custom Type Guesser](https://symfony.com/doc/8.0/form/type_guesser.html)

Form Themes and Customization:

* [Bootstrap 4 Form Theme](https://symfony.com/doc/8.0/form/bootstrap4.html)
* [Bootstrap 5 Form Theme](https://symfony.com/doc/8.0/form/bootstrap5.html)
* [Tailwind CSS Form Theme](https://symfony.com/doc/8.0/form/tailwindcss.html)
* [How to Customize Form Rendering](https://symfony.com/doc/8.0/form/form_customization.html)
* [How to Work with Form Themes](https://symfony.com/doc/8.0/form/form_themes.html)

Events:

* [Form Events](https://symfony.com/doc/8.0/form/events.html)
* [How to Dynamically Modify Forms Using Form Events](https://symfony.com/doc/8.0/form/dynamic_form_modification.html)

Validation:

* [Configuring Validation Groups in Forms](https://symfony.com/doc/8.0/form/validation_groups.html)

Misc.:

* [How to Embed Forms](https://symfony.com/doc/8.0/form/embedded.html)
* [How to Embed a Collection of Forms](https://symfony.com/doc/8.0/form/form_collections.html)
* [How to Reduce Code Duplication with "inherit_data"](https://symfony.com/doc/8.0/form/inherit_data_option.html)
* [How to Unit Test your Forms](https://symfony.com/doc/8.0/form/unit_testing.html)
* [How to Configure empty Data for a Form Class](https://symfony.com/doc/8.0/form/use_empty_data.html)

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 1: Show your Symfony expertise](https://symfony.com/images/network/sf7certif_01.webp)](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=symfonyexpertise)
[Show your Symfony expertise](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=symfonyexpertise)

[![Image 2: Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://symfony.com/images/network/slsolutions_01.webp)](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)
[Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 3: Avatar of Maxime PINEAU, a Symfony contributor](https://www.gravatar.com/avatar/ec8a5dcd68f010293146df742710ee5a?size=48&rating=g&default=retro)

Thanks **Maxime PINEAU** for being a Symfony contributor

**1** commit • **115** lines changed

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
