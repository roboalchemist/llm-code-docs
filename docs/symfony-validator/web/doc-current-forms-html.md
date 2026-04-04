# Source: https://symfony.com/doc/current/forms.html

Title: Forms (Symfony Docs)

URL Source: https://symfony.com/doc/current/forms.html

Markdown Content:
Creating and processing HTML forms is hard and repetitive. You need to deal with rendering HTML form fields, validating submitted data, mapping the form data into objects and a lot more. Symfony includes a powerful form feature that provides all these features and many more for truly complex scenarios.

[Installation](https://symfony.com/doc/current/forms.html#installation "Permalink to this headline")
----------------------------------------------------------------------------------------------------

In applications using [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex), run this command to install the form feature before using it:

[Understanding How Forms Work](https://symfony.com/doc/current/forms.html#understanding-how-forms-work "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------

Before diving into the code, it's helpful to understand the mental model behind Symfony forms. Think of a form as a **bidirectional mapping layer** between your PHP objects (or arrays) and HTML forms.

This mapping works in two directions:

1.   **Object to HTML**: When rendering a form, Symfony reads data from your object and turns it into HTML fields that users can edit;
2.   **HTML to Object**: When processing a submission, Symfony takes the raw values from the HTTP request (typically strings) and converts them back into the appropriate PHP types on your object.

This flow is the core of the Form component. From simple text fields to complex nested collections, everything follows the same pattern.

### [The Data Transformation Lifecycle](https://symfony.com/doc/current/forms.html#the-data-transformation-lifecycle "Permalink to this headline")

Data in a form goes through three representations, often called **data layers**:

**Model Data** The data in the format your application uses. For example, a `DateTime` object, a Doctrine entity, or a custom value object. This is what you pass to `createForm()` and what you get back after a successful submission via `getData()`. **Normalized Data** An intermediate representation that normalizes the model data. For most field types, this is identical to the model data. However, for some types it's different. For example, `DateType` is normalized as an array with `year`, `month`, and `day` keys. **View Data** The format used to populate HTML form fields and received from user submissions. In most cases, this is string-based (or arrays of strings), because browsers submit text. Some fields may use other representations or remain empty for security reasons (for example, file inputs). 
High-level flow:

**Form Rendering**

1.   Start with model data from your object.
2.   Model transformers convert it to normalized data.
3.   View transformers convert it to view data (typically strings).
4.   Symfony renders the corresponding HTML widgets.

**Form Submission**

1.   Symfony reads raw values from the HTTP request (typically strings).
2.   View transformers reverse the data into normalized data.
3.   Model transformers reverse the data into model data.
4.   The data is written back to the underlying object or array.

For a `DateType` field configured to render as three `<select>` elements:

*   **Model data**: a `DateTime` object;
*   **Norm data**: an array like `['year' => 2026, 'month' => 10, 'day' => 18]`; (values are integers)
*   **View data**: an array like `['year' => '2026', 'month' => '10', 'day' => '18']` (values are strings, as submitted by the browser).

Most of the time you don't need to think about these layers. They become relevant when debugging why a field doesn't display or submit correctly, or when creating custom [data transformers](https://symfony.com/doc/current/form/data_transformers.html).

[Usage](https://symfony.com/doc/current/forms.html#usage "Permalink to this headline")
--------------------------------------------------------------------------------------

The recommended workflow when working with Symfony forms is the following:

1.   **Build the form** in a Symfony controller or using a dedicated form class;
2.   **Render the form** in a template so the user can edit and submit it;
3.   **Process the form** to validate the submitted data, transform it into PHP data and do something with it (e.g. persist it in a database).

Each of these steps is explained in detail in the next sections. To make examples easier to follow, all of them assume that you're building a small Todo list application that displays "tasks".

Users create and edit tasks using Symfony forms. Each task is an instance of the following `Task` class:

This class is a "plain-old-PHP-object" because, so far, it has nothing to do with Symfony or any other library. It's a normal PHP object that directly solves a problem inside _your_ application (i.e. the need to represent a task in your application). But you can also edit [Doctrine entities](https://symfony.com/doc/current/doctrine.html) in the same way.

### [Form Types](https://symfony.com/doc/current/forms.html#form-types "Permalink to this headline")

Before creating your first Symfony form, it's important to understand the concept of "form type". In other projects, it's common to differentiate between "forms" and "form fields". In Symfony, all of them are "form types":

*   a single `<input type="text">` form field is a "form type" (e.g. `TextType`);
*   a group of several HTML fields used to input a postal address is a "form type" (e.g. `PostalAddressType`);
*   an entire `<form>` with multiple fields to edit a user profile is a "form type" (e.g. `UserProfileType`).

This unified concept makes the Form component more **flexible**. You can compose complex forms from simpler types, embed forms within forms, and reuse the same type definition across your application.

**The Form Type Hierarchy**

Every form type has a parent type. The parent determines the base behavior, options, and rendering that your type inherits. Here's a simplified view:

When you create a custom form type and specify a parent (via `getParent()`), your type inherits options, template blocks, and behavior from that parent. This is why `EmailType` reuses the rendering and options from `TextType`.

There are tens of [form types provided by Symfony](https://symfony.com/doc/current/reference/forms/types.html) and you can also [create your own form types](https://symfony.com/doc/current/form/create_custom_field_type.html).

Tip

You can use the `debug:form` to list all the available types, type extensions and type guessers in your application:

[Building Forms](https://symfony.com/doc/current/forms.html#building-forms "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

Symfony provides a "form builder" object which allows you to describe the form fields using a fluent interface. Later, this builder creates the actual form object used to render and process contents.

### [Creating Forms in Controllers](https://symfony.com/doc/current/forms.html#creating-forms-in-controllers "Permalink to this headline")

If your controller extends from the [AbstractController](https://symfony.com/doc/current/controller.html#the-base-controller-class-services), use the `createFormBuilder()` helper:

If your controller does not extend from `AbstractController`, you'll need to [fetch services in your controller](https://symfony.com/doc/current/controller.html#controller-accessing-services) and use the `createBuilder()` method of the `form.factory` service.

In this example, you've added two fields to your form - `task` and `dueDate` - corresponding to the `task` and `dueDate` properties of the `Task` class. You've also assigned each a [form type](https://symfony.com/doc/current/forms.html#form-types) (e.g. `TextType` and `DateType`), represented by its fully qualified class name. Finally, you added a submit button with a custom label for submitting the form to the server.

### [Creating Form Classes](https://symfony.com/doc/current/forms.html#creating-form-classes "Permalink to this headline")

Symfony recommends putting as little logic as possible in controllers. That's why it's better to move complex forms to dedicated classes instead of defining them in controller actions. Besides, forms defined in classes can be reused in multiple actions and services.

Form classes are [form types](https://symfony.com/doc/current/forms.html#form-types) that implement [FormTypeInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormTypeInterface.php "Symfony\Component\Form\FormTypeInterface"). However, it's better to extend from [AbstractType](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/AbstractType.php "Symfony\Component\Form\AbstractType"), which already implements the interface and provides some utilities:

Tip

Install the [MakerBundle](https://symfony.com/doc/current/bundles/SymfonyMakerBundle/index.html) in your project to generate form classes using the `make:form` and `make:registration-form` commands.

The form class contains all the directions needed to create the task form. In controllers extending from the [AbstractController](https://symfony.com/doc/current/controller.html#the-base-controller-class-services), use the `createForm()` helper (otherwise, use the `create()` method of the `form.factory` service):

Every form needs to know the name of the class that holds the underlying data (e.g. `App\Entity\Task`). Usually, this is guessed based on the object passed to the second argument to `createForm()` (i.e. `$task`). Later, when you begin [embedding forms](https://symfony.com/doc/current/form/embedded.html), this will no longer be sufficient.

So, while not always necessary, it's generally a good idea to explicitly specify the `data_class` option by adding the following to your form type class:

### [Mapping Fields to Object Properties](https://symfony.com/doc/current/forms.html#mapping-fields-to-object-properties "Permalink to this headline")

By default, a form field named `dueDate` reads and writes the `dueDate` property on your object. This uses the [PropertyAccess component](https://symfony.com/doc/current/components/property_access.html), which can work with public properties and common accessor names (`get*()`, `is*()`, `has*()`, `set*()`).

The `property_path` option lets you customize this mapping.

**Mapping to a Different Property**

If your form field name doesn't match the object property:

**Mapping to Nested Properties**

You can access nested object properties using dot notation:

For fields that shouldn't be written back to the underlying data, use [unampped fields](https://symfony.com/doc/current/forms.html#form-unmapped-fields).

[Rendering Forms](https://symfony.com/doc/current/forms.html#rendering-forms "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

Now that the form has been created, the next step is to render it:

Internally, the `render()` method calls `$form->createView()` to transform the form into a _form view_ instance.

Then, use some [form helper functions](https://symfony.com/doc/current/form/form_customization.html#reference-form-twig-functions) to render the form contents:

That's it! The [form() function](https://symfony.com/doc/current/form/form_customization.html#reference-forms-twig-form) renders all fields _and_ the `<form>` start and end tags. By default, the form method is `POST` and the target URL is the same that displayed the form, but [you can change both](https://symfony.com/doc/current/forms.html#forms-change-action-method).

Notice how the rendered `task` input field has the value of the `task` property from the `$task` object (i.e. "Write a blog post"). This is the first job of a form: to take data from an object and translate it into a format that's suitable for being rendered in an HTML form.

Tip

The form system is smart enough to access the value of the protected `task` property via the `getTask()` and `setTask()` methods on the `Task` class. Unless a property is public, it _must_ have a "getter" and "setter" method so that Symfony can get and put data onto the property. For a boolean property, you can use an "isser" or "hasser" method (e.g. `isPublished()` or `hasReminder()`) instead of a getter (e.g. `getPublished()` or `getReminder()`).

As short as this rendering is, it's not very flexible. Usually, you'll need more control about how the entire form or some of its fields look. For example, thanks to the [Bootstrap 5 integration with Symfony forms](https://symfony.com/doc/current/form/bootstrap5.html) you can set this option to generate forms compatible with the Bootstrap 5 CSS framework:

The [built-in Symfony form themes](https://symfony.com/doc/current/form/form_themes.html#symfony-builtin-forms) include Bootstrap 3, 4 and 5, Foundation 5 and 6, as well as Tailwind 2. You can also [create your own Symfony form theme](https://symfony.com/doc/current/form/form_themes.html#create-your-own-form-theme).

In addition to form themes, Symfony allows you to [customize the way fields are rendered](https://symfony.com/doc/current/form/form_customization.html) with multiple functions to render each field part separately (widgets, labels, errors, help messages, etc.)

[Processing Forms](https://symfony.com/doc/current/forms.html#processing-forms "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

The [recommended way of processing forms](https://symfony.com/doc/current/best_practices.html#best-practice-handle-form) is to use a single action for both rendering the form and handling the form submit. You can use separate actions, but using one action simplifies everything while keeping the code concise and maintainable.

Processing a form means to translate user-submitted data back to the properties of an object. To make this happen, the submitted data from the user must be written into the form object:

This controller follows a common pattern for handling forms and has three possible paths:

1.   When initially loading the page in a browser, the form hasn't been submitted yet and `$form->isSubmitted()` returns `false`. So, the form is created and rendered;
2.   When the user submits the form, [handleRequest()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20handleRequest "Symfony\Component\Form\FormInterface::handleRequest()") recognizes this and immediately writes the submitted data back into the `task` and `dueDate` properties of the `$task` object. Then this object is validated (validation is explained in the next section). If it is invalid, [isValid()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20isValid "Symfony\Component\Form\FormInterface::isValid()") returns `false` and the form is rendered again, but now with validation errors.

By passing `$form` to the `render()` method (instead of `$form->createView()`), the response code is automatically set to [HTTP 422 Unprocessable Content](https://www.rfc-editor.org/rfc/rfc9110.html#name-422-unprocessable-content). This ensures compatibility with tools relying on the HTTP specification, like [Symfony UX Turbo](https://ux.symfony.com/turbo);

3.   When the user submits the form with valid data, the submitted data is again written into the form, but this time [isValid()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20isValid "Symfony\Component\Form\FormInterface::isValid()") returns `true`. Now you have the opportunity to perform some actions using the `$task` object (e.g. persisting it to the database) before redirecting the user to some other page (e.g. a "thank you" or "success" page);

Note

Redirecting a user after a successful form submission is a best practice that prevents the user from being able to hit the "Refresh" button of their browser and re-post the data.

### [Accessing Form Data](https://symfony.com/doc/current/forms.html#accessing-form-data "Permalink to this headline")

You'll use the `getData()` method most often to access the form's data, but Symfony forms also provide methods to access data at [each layer](https://symfony.com/doc/current/forms.html#form-data-lifecycle):

`getData()` Returns the **model data**. This is the method you'll use most often. After submission, it returns the populated object (or array) with all the submitted values transformed into their proper PHP types. `getNormData()` Returns the **normalized data**. Useful when debugging transformer issues or when you need the intermediate representation. `getViewData()` Returns the **view data**. This is what gets rendered into HTML fields and what comes back from user submissions (before transformation). 

See also

When adding [extra fields](https://symfony.com/doc/current/forms.html#form-extra-fields) to the form, you can also use the `getExtraData()` method to get any submitted data that doesn't correspond to a form field.

Example showing these methods in action:

If a transformer fails, the form (or the affected field) may be marked as not synchronized. Check `isSynchronized()` and inspect field errors to understand what went wrong.

### [Using the submit() Method](https://symfony.com/doc/current/forms.html#using-the-submit-method "Permalink to this headline")

The [handleRequest()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20handleRequest "Symfony\Component\Form\FormInterface::handleRequest()") method is the recommended way to process forms. However, you can also use the [submit()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20submit "Symfony\Component\Form\FormInterface::submit()") method for finer control over when exactly your form is submitted and what data is passed to it:

The list of fields submitted with the `submit()` method must be the same as the fields defined by the form class. Otherwise, you'll see a form validation error:

Tip

Forms consisting of nested fields expect an array in [submit()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20submit "Symfony\Component\Form\FormInterface::submit()"). You can also submit individual fields by calling [submit()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20submit "Symfony\Component\Form\FormInterface::submit()") directly on the field:

Tip

When submitting a form via a "PATCH" request, you may want to update only a few submitted fields. To achieve this, you may pass an optional second boolean argument to `submit()`. Passing `false` will remove any missing fields within the form object. Otherwise, the missing fields will be set to `null`.

Warning

When the second parameter `$clearMissing` is `false`, like with the "PATCH" method, the validation will only apply to the submitted fields. If you need to validate all the underlying data, add the required fields manually so that they are validated:

### [Handling Multiple Submit Buttons](https://symfony.com/doc/current/forms.html#handling-multiple-submit-buttons "Permalink to this headline")

When your form contains more than one submit button, you'll want to check which of the buttons was clicked to adapt the program flow in your controller. For example, if you add a second button with the caption "Save and Add" to your form:

In your controller, use the button's [isClicked()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/ClickableInterface.php#:~:text=function%20isClicked "Symfony\Component\Form\ClickableInterface::isClicked()") method for querying if the "Save and Add" button was clicked:

Alternatively you can use the [getClickedButton()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/Form.php#:~:text=function%20getClickedButton "Symfony\Component\Form\Form::getClickedButton()") method to get the clicked button's name:

[Validating Forms](https://symfony.com/doc/current/forms.html#validating-forms "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

In the previous section, you learned how a form can be submitted with valid or invalid data. In Symfony, the question isn't whether the "form" is valid, but whether or not the underlying object (`$task` in this example) is valid after the form has applied the submitted data to it. Calling `$form->isValid()` is a shortcut that asks the `$task` object whether or not it has valid data.

Before using validation, add support for it in your application:

Validation is done by adding a set of rules, called (validation) constraints, to a class. You can add them either to the entity class or by using the [constraints option](https://symfony.com/doc/current/reference/forms/types/form.html#reference-form-option-constraints) of form types.

To see the first approach - adding constraints to the entity - in action, add the validation constraints, so that the `task` field cannot be empty, and the `dueDate` field cannot be empty, and must be a valid `DateTimeImmutable` object.

That's it! If you re-submit the form with invalid data, you'll see the corresponding errors printed out with the form.

To see the second approach - adding constraints to the form - refer to [this section](https://symfony.com/doc/current/forms.html#form-option-constraints). Both approaches can be used together.

### [Disabling Validation](https://symfony.com/doc/current/forms.html#disabling-validation "Permalink to this headline")

Sometimes it's useful to suppress the validation of a form altogether. For these cases, set the `validation_groups` option to `false`:

Note that when you do that, the form will still run basic integrity checks, for example whether an uploaded file was too large or whether non-existing fields were submitted.

The submission of extra form fields can be controlled with the [allow_extra_fields config option](https://symfony.com/doc/current/reference/forms/types/form.html#form-option-allow-extra-fields) and the maximum upload file size should be handled via your PHP and web server configuration.

You can also disable validation for specific submit buttons using `'validation_groups' => false`. This is useful in multi-step forms when you want a "Previous" button to save data without running validation:

The form will still validate basic integrity constraints even when clicking "previousStep".

[Other Common Form Features](https://symfony.com/doc/current/forms.html#other-common-form-features "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

### [Passing Options to Forms](https://symfony.com/doc/current/forms.html#passing-options-to-forms "Permalink to this headline")

If you [create forms in classes](https://symfony.com/doc/current/forms.html#creating-forms-in-classes), when building the form in the controller you can pass custom options to it as the third optional argument of `createForm()`:

If you try to use the form now, you'll see an error message: _The option "require\_due\_date" does not exist._ That's because forms must declare all the options they accept using the `configureOptions()` method:

Now you can use this new form option inside the `buildForm()` method:

### [Form Type Options](https://symfony.com/doc/current/forms.html#form-type-options "Permalink to this headline")

Each [form type](https://symfony.com/doc/current/forms.html#form-types) has a number of options to configure it, as explained in the [Symfony form types reference](https://symfony.com/doc/current/reference/forms/types.html). Two commonly used options are `required` and `label`.

#### [The `required` Option](https://symfony.com/doc/current/forms.html#the-required-option "Permalink to this headline")

The most common option is the `required` option, which can be applied to any field. By default, this option is set to `true`, meaning that HTML5-ready browsers will require you to fill in all fields before submitting the form.

If you don't want this behavior, either [disable client-side validation](https://symfony.com/doc/current/forms.html#forms-html5-validation-disable) for the entire form or set the `required` option to `false` on one or more fields:

The `required` option does not perform any server-side validation. If a user submits a blank value for the field (either with an old browser or a web service, for example), it will be accepted as a valid value unless you also use Symfony's `NotBlank` or `NotNull` validation constraints.

#### [The `label` Option](https://symfony.com/doc/current/forms.html#the-label-option "Permalink to this headline")

By default, the label of form fields are the _humanized_ version of the property name (`user` ->`User`; `postalAddress` ->`Postal Address`). Set the `label` option on fields to define their labels explicitly:

Tip

By default, `<label>` tags of required fields are rendered with a `required` CSS class, so you can display an asterisk by applying a CSS style:

### [Changing the Action and HTTP Method](https://symfony.com/doc/current/forms.html#changing-the-action-and-http-method "Permalink to this headline")

By default, the `<form>` tag is rendered with a `method="post"` attribute, and no `action` attribute. This means that the form is submitted via an HTTP POST request to the same URL under which it was rendered. When building the form, use the `setAction()` and `setMethod()` methods to change this:

When building the form in a class, pass the action and method as form options:

Finally, you can override the action and method in the template by passing them to the `form()` or the `form_start()` helper functions:

Note

If the form's method is not `GET` or `POST`, but `PUT`, `PATCH` or `DELETE`, Symfony will insert a hidden field with the name `_method` that stores this method. The form will be submitted in a normal `POST` request, but [Symfony's routing](https://symfony.com/doc/current/routing.html) is capable of detecting the `_method` parameter and will interpret it as a `PUT`, `PATCH` or `DELETE` request. The [http_method_override](https://symfony.com/doc/current/reference/configuration/framework.html#configuration-framework-http_method_override) option must be enabled for this to work.

For security, you can restrict which HTTP methods can be overridden using the [allowed_http_method_override](https://symfony.com/doc/current/reference/configuration/framework.html#configuration-framework-allowed_http_method_override) option.

### [Changing the Form Field Names and Ids](https://symfony.com/doc/current/forms.html#changing-the-form-field-names-and-ids "Permalink to this headline")

When Symfony renders a form, it generates HTML `name` and `id` attributes for each field following specific conventions. Understanding these conventions helps when writing JavaScript, CSS selectors, or custom form themes.

In Twig templates, prefer `form.vars.full_name` and `form.vars.id` as the source of truth, instead of reconstructing names manually.

**The `name` Attribute**

Field names follow the pattern: `formName[fieldName]`. For nested forms, names are further nested: `formName[childForm][fieldName]`.

Given a `TaskType` form with a `dueDate` field:

The rendered HTML will have:

For a `DateType` field that renders as three separate `<select>` elements:

**The `id` Attribute**

The `id` attribute follows a similar pattern but uses underscores instead of brackets: `formName_fieldName`. For the examples above:

**Customizing the Form Name**

The default form name is derived from the form type class (for example, `TaskType` becomes `task` and `FooBarType` becomes `foo_bar`). You can customize this by returning a different value from the `getBlockPrefix()` method of your form type class.

You can also customize this by creating the form with the [createNamed()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormFactoryInterface.php#:~:text=function%20createNamed "Symfony\Component\Form\FormFactoryInterface::createNamed()") method:

To create a form without any name prefix (fields named directly like `dueDate` instead of `task[dueDate]`):

### [Client-Side HTML Validation](https://symfony.com/doc/current/forms.html#client-side-html-validation "Permalink to this headline")

Thanks to HTML5, many browsers can natively enforce certain validation constraints on the client side. The most common validation is activated by adding a `required` attribute on fields that are required. For browsers that support HTML5, this will result in a native browser message being displayed if the user tries to submit the form with that field blank.

Generated forms take full advantage of this new feature by adding sensible HTML attributes that trigger the validation. The client-side validation, however, can be disabled by adding the `novalidate` attribute to the `<form>` tag or `formnovalidate` to the submit tag. This is especially useful when you want to test your server-side validation constraints, but are being prevented by your browser from, for example, submitting blank fields.

### [Form Type Guessing](https://symfony.com/doc/current/forms.html#form-type-guessing "Permalink to this headline")

If the object handled by the form includes validation constraints, Symfony can introspect that metadata to guess the type of your field. In the above example, Symfony can guess from the validation rules that the `task` field is a normal `TextType` field and the `dueDate` field is a `DateType` field.

To enable Symfony's "guessing mechanism", omit the second argument to the `add()` method, or pass `null` to it:

Warning

When using a specific [form validation group](https://symfony.com/doc/current/form/validation_groups.html), the field type guesser will still consider _all_ validation constraints when guessing your field types (including constraints that are not part of the validation group(s) being used).

#### [Form Type Options Guessing](https://symfony.com/doc/current/forms.html#form-type-options-guessing "Permalink to this headline")

When the guessing mechanism is enabled for some field, in addition to its form type, the following options will be guessed too:

`required` The `required` option is guessed based on the validation rules (i.e. is the field `NotBlank` or `NotNull`) or the Doctrine metadata (i.e. is the field `nullable`). This is very useful, as your client-side validation will automatically match your validation rules. `maxlength` If the field is some sort of text field, then the `maxlength` option attribute is guessed from the validation constraints (if `Length` or `Range` is used) or from the [Doctrine](https://symfony.com/doc/current/doctrine.html) metadata (via the field's length). 
If you'd like to change one of the guessed values, override it in the options field array:

### [Unmapped Fields](https://symfony.com/doc/current/forms.html#unmapped-fields "Permalink to this headline")

When editing an object via a form, all form fields are considered properties of the object. Any fields on the form that do not exist on the object will cause an exception to be thrown.

If you need extra fields in the form that won't be stored in the object (for example to add an _"I agree with these terms"_ checkbox), set the `mapped` option to `false` in those fields:

These "unmapped fields" can be set and accessed in a controller with:

Additionally, if there are any fields on the form that aren't included in the submitted data, those fields will be explicitly set to `null`.

By default, Symfony expects every submitted field to be defined in the form. Any additional submitted fields are treated as "extra fields". You can access them via the [FormInterface::getExtraData()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Form/FormInterface.php#:~:text=function%20getExtraData "Symfony\Component\Form\FormInterface::getExtraData()") method.

For example, consider a user creation form:

You can render an additional input in the template without adding it to the form definition:

In this example, `referralCode` is submitted as an extra field and you can read it like this:

Note

To accept extra fields, set the [allow_extra_fields](https://symfony.com/doc/current/reference/forms/types/form.html#form-option-allow-extra-fields) option to `true`. Otherwise, the form will be invalid.

[Using a Form without a Data Class](https://symfony.com/doc/current/forms.html#using-a-form-without-a-data-class "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------

In most applications, a form is tied to an object, and the fields of the form get and store their data on the properties of that object. This is what you've seen so far in this article with the `Task` class.

However, by default, a form actually assumes that you want to work with arrays of data, instead of an object. There are exactly two ways that you can change this behavior and tie the form to an object instead:

1.   Pass an object when creating the form (as the first argument to `createFormBuilder()` or the second argument to `createForm()`);
2.   Declare the `data_class` option on your form.

If you _don't_ do either of these, then the form will return the data as an array. In this example, since `$defaultData` is not an object (and no `data_class` option is set), `$form->getData()` ultimately returns an array:

Tip

You can also access POST values (in this case "name") directly through the request object, like so:

Be advised, however, that in most cases using the `getData()` method is a better choice, since it returns the data (usually an object) after it's been transformed by the Form component.

### [Adding Validation](https://symfony.com/doc/current/forms.html#adding-validation "Permalink to this headline")

Usually, when you call `$form->handleRequest($request)`, the object is validated by reading the constraints that you applied to that class. If your form is mapped to an object, this is almost always the approach you want to use. See [Validation](https://symfony.com/doc/current/validation.html) for more details.

But if the form is not mapped to an object and you instead want to retrieve an array of your submitted data, there are two ways to add constraints to the form data.

#### [Constraints At Field Level](https://symfony.com/doc/current/forms.html#constraints-at-field-level "Permalink to this headline")

You can attach constraints to the individual fields. The overall approach is covered a bit more in [this validation article](https://symfony.com/doc/current/validation/raw_values.html), but here's a short example:

Tip

If you are using validation groups, you need to either reference the `Default` group when creating the form, or set the correct group on the constraint you are adding:

Tip

If the form is not mapped to an object, every object in your array of submitted data is validated using the `Symfony\Component\Validator\Constraints\Valid` constraint, unless you [disable validation](https://symfony.com/doc/current/forms.html#disabling-validation).

Warning

When a form is only partially submitted (for example, in an HTTP PATCH request), only the constraints from the submitted form fields will be evaluated.

#### [Constraints At Class Level](https://symfony.com/doc/current/forms.html#constraints-at-class-level "Permalink to this headline")

You can also add the constraints at the class level. This can be done by setting the `constraints` option in the `configureOptions()` method:

This means you can also do this when using the `createFormBuilder()` method in your controller:

#### [Conditional Constraints](https://symfony.com/doc/current/forms.html#conditional-constraints "Permalink to this headline")

It's possible to define field constraints that depend on the value of other fields (e.g. a field must not be blank when another field has a certain value). To achieve this, use the `expression` option of the [When constraint](https://symfony.com/doc/current/reference/constraints/When.html) to reference the other field:

[Troubleshooting](https://symfony.com/doc/current/forms.html#troubleshooting "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

### [Why Doesn't My Field Value Display?](https://symfony.com/doc/current/forms.html#why-doesn-t-my-field-value-display "Permalink to this headline")

**Problem**: The form renders, but a field is empty even though the underlying data has a value.

**Common causes**:

1.   The property is not readable (missing accessor, wrong name, or not public). For booleans, Symfony also looks for `is*()` and `has*()` accessors.
2.   The field name doesn't match the property name. Use [property_path](https://symfony.com/doc/current/forms.html#form-property-path) if you need to map to a different property.
3.   The data is set after creating the form. Populate your object _before_ passing it to `createForm()`:

### [Why Doesn't My Submitted Data Save to the Object?](https://symfony.com/doc/current/forms.html#why-doesn-t-my-submitted-data-save-to-the-object "Permalink to this headline")

**Problem**: The form submits, but the object properties remain unchanged.

**Common causes**:

1.   The property is not writable (missing setter, wrong name, or not public).
2.   It is an [unmapped field](https://symfony.com/doc/current/forms.html#form-unmapped-fields).
3.   The form is not synchronized due to a transformation failure. Check `isSynchronized()` and inspect field errors.

### [Why Does `getData()` Return `null` After Submission?](https://symfony.com/doc/current/forms.html#why-does-getdata-return-null-after-submission "Permalink to this headline")

**Problem**: `$form->getData()` is `null` after handling the request.

**Common causes**:

1.   No initial object (or default data) was provided and the form doesn't create one. Review the form's `data_class` and `empty_data` options.
2.   A transformation failed and the form is not synchronized. Check `isSynchronized()` and field errors.
3.   The form is not submitted or is invalid. Check `isSubmitted()` and `isValid()` before using the data.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
