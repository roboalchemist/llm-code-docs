# Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/portable-object-localization?view=aspnetcore-10.0

Title: Configure portable object localization in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/portable-object-localization?view=aspnetcore-10.0

Markdown Content:
By [Hisham Bin Ateya](https://github.com/hishamco) and [Sébastien Ros](https://github.com/sebastienros).

This article walks through the steps for using Portable Object (PO) files in an ASP.NET Core application with the [Orchard Core](https://github.com/OrchardCMS/OrchardCore) framework.

**Note:** Orchard Core isn't a Microsoft product. Microsoft provides no support for this feature.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/localization/sample/6.x/POLocalization) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

PO files are distributed as text files containing the translated strings for a given language. Some advantages of using PO files instead of _.resx_ files include:

*   PO files support pluralization; _.resx_ files don't support pluralization.
*   PO files aren't compiled like _.resx_ files. As such, specialized tooling and build steps aren't required.
*   PO files work well with collaborative online editing tools.

The following sample PO file contains the translation for two strings in French, including one with its plural form:

_fr.po_

```
#: Pages/Index.cshtml:13
msgid "Hello world!"
msgstr "Bonjour le monde!"

msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Il y a un élément."
msgstr[1] "Il y a {0} éléments."
```

This example uses the following syntax:

*   `#:`: A comment indicating the context of the string to be translated. The same string might be translated differently depending on where it's being used.
*   `msgid`: The untranslated string.
*   `msgstr`: The translated string.

For pluralization support, more entries can be defined.

*   `msgid_plural`: The untranslated plural string.
*   `msgstr[0]`: The translated string for the case 0.
*   `msgstr[N]`: The translated string for the case N.

The PO file specification can be found [here](https://www.gnu.org/savannah-checkouts/gnu/gettext/manual/html_node/PO-Files.html).

This example is based on an ASP.NET Core Web application generated from a Visual Studio 2022 project template.

Add a reference to the `OrchardCore.Localization.Core` NuGet package.

The `.csproj` file now contains a line similar to the following (version number may vary):

```
<PackageReference Include="OrchardCore.Localization.Core" Version="1.5.0" />
```

Add the required services to `Program.cs`:

```
builder.Services.AddPortableObjectLocalization();

builder.Services
    .Configure<RequestLocalizationOptions>(options => options
        .AddSupportedCultures("fr", "cs")
        .AddSupportedUICultures("fr", "cs"));

builder.Services
    .AddRazorPages()
    .AddViewLocalization();
```

Add the following code to your Razor page of choice. `Index.cshtml` is used in this example.

```
@page
@using Microsoft.AspNetCore.Mvc.Localization
@inject IViewLocalizer Localizer
@{
    ViewData["Title"] = "Home";
}

<div class="text-center">
    <h1 class="display-4">Welcome</h1>
    <p>Learn about <a href="https://docs.microsoft.com/aspnet/core">building Web apps with ASP.NET Core</a>.</p>
</div>

<p>@Localizer["Hello world!"]</p>
```

An `IViewLocalizer` instance is injected and used to translate the text "Hello world!".

Create a file named _<culture code>.po_ in your application root folder. In this example, the file name is _fr.po_ because the French language is used:

```
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

This file stores both the string to translate and the French-translated string. Translations revert to their parent culture, if necessary. In this example, the _fr.po_ file is used if the requested culture is `fr-FR` or `fr-CA`.

Run your application, the text **Hello world!** is displayed.

Navigate to the URL `/Index?culture=fr-FR`. The text **Bonjour le monde!** is displayed.

PO files support pluralization forms, which is useful when the same string needs to be translated differently based on a cardinality. This task is made complicated by the fact that each language defines custom rules to select which string to use based on the cardinality.

The Orchard Localization package provides an API to invoke these different plural forms automatically.

Add the following content to the previously mentioned _fr.po_ file:

```
msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Il y a un élément."
msgstr[1] "Il y a {0} éléments."
```

See [What is a PO file?](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/portable-object-localization?view=aspnetcore-10.0#what-is-a-po-file) for an explanation of what each entry in this example represents.

English and French strings were used in the previous example. English and French have only two pluralization forms and share the same form rules, which is that a cardinality of one is mapped to the first plural form. Any other cardinality is mapped to the second plural form.

Not all languages share the same rules. This is illustrated with the Czech language, which has three plural forms.

Create the `cs.po` file as follows, and note how the pluralization needs three different translations:

```
msgid "Hello world!"
msgstr "Ahoj světe!!"

msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Existuje jedna položka."
msgstr[1] "Existují {0} položky."
msgstr[2] "Existuje {0} položek."
```

To accept Czech localizations, add `"cs"` to the list of supported cultures in the `Configure` method:

```
builder.Services
    .Configure<RequestLocalizationOptions>(options => options
        .AddSupportedCultures("fr", "cs")
        .AddSupportedUICultures("fr", "cs"));
```

Edit the `Pages/Index.cshtml` file to render localized, plural strings for several cardinalities:

```
<p>@Localizer.Plural(1, "There is one item.", "There are {0} items.")</p>
<p>@Localizer.Plural(2, "There is one item.", "There are {0} items.")</p>
<p>@Localizer.Plural(5, "There is one item.", "There are {0} items.")</p>
```

**Note:** In a real world scenario, a variable would be used to represent the count. Here, we repeat the same code with three different values to expose a specific case.

Upon switching cultures, you see the following:

For `/Index`:

```
There is one item.
There are 2 items.
There are 5 items.
```

For `/Index?culture=fr`:

```
Il y a un élément.
Il y a 2 éléments.
Il y a 5 éléments.
```

For `/Index?culture=cs`:

```
Existuje jedna položka.
Existují 2 položky.
Existuje 5 položek.
```

For the Czech culture, the three translations are different. The French and English cultures share the same construction for the two last translated strings.

The argument at index zero `{0}` always represents the count value. When invoking the `Plural` method it is possible to add additional arguments and their index will then start at one (`1`).

```
<p>@Localizer.Plural(count, "There is one item with the color {1}.", "There are {0} items. The main color is {1}.", color)</p>
```

Applications often contain the strings to be translated in several places. The same string may have a different translation in certain locations within an app (Razor views or class files). A PO file supports the notion of a file context, which can be used to categorize the string being represented. Using a file context, a string can be translated differently, depending on the file context (or lack of a file context).

The PO localization services use the name of the full class or the view that's used when translating a string. This is accomplished by setting the value on the `msgctxt` entry.

Consider a minor addition to the previous _fr.po_ example. A Razor page located at `Pages/Index.cshtml` can be defined as the file context by setting the reserved `msgctxt` entry's value:

```
msgctxt "Views.Home.About"
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

With the `msgctxt` set as such, text translation occurs when navigating to `/Index?culture=fr-FR`. The translation doesn't occur when navigating to `/Privacy?culture=fr-FR`.

When no specific entry is matched with a given file context, Orchard Core's fallback mechanism looks for an appropriate PO file without a context. Assuming there's no specific file context defined for `Pages/Privacy.cshtml`, navigating to `/Privacy?culture=fr-FR` loads a PO file such as:

```
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

The default location of PO files can be changed in `Programs.cs`:

```
services.AddPortableObjectLocalization(options => options.ResourcesPath = "Localization");
```

In this example, the PO files are loaded from the _Localization_ folder.

When more complex logic is needed to locate PO files, the `OrchardCore.Localization.PortableObject.ILocalizationFileLocationProvider` interface can be implemented and registered as a service. This is useful when PO files can be stored in varying locations or when the files have to be found within a hierarchy of folders.

The package includes a `Plural` extension method that's specific to two plural forms. For languages requiring more plural forms, create an extension method. With an extension method, you won't need to provide any localization file for the default language — the original strings are already available directly in the code.

You can use the more generic `Plural(int count, string[] pluralForms, params object[] arguments)` overload which accepts a string array of translations.

By [Sébastien Ros](https://github.com/sebastienros), [Scott Addie](https://twitter.com/Scott_Addie) and [Hisham Bin Ateya](https://github.com/hishamco)

This article walks through the steps for using Portable Object (PO) files in an ASP.NET Core application with the [Orchard Core](https://github.com/OrchardCMS/OrchardCore) framework.

**Note:** Orchard Core isn't a Microsoft product. Consequently, Microsoft provides no support for this feature.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/localization/sample/5.x/POLocalization) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

PO files are distributed as text files containing the translated strings for a given language. Some advantages of using PO files instead of _.resx_ files include:

*   PO files support pluralization; _.resx_ files don't support pluralization.
*   PO files aren't compiled like _.resx_ files. As such, specialized tooling and build steps aren't required.
*   PO files work well with collaborative online editing tools.

Here is a sample PO file containing the translation for two strings in French, including one with its plural form:

_fr.po_

```
#: Pages/Index.cshtml:13
msgid "Hello world!"
msgstr "Bonjour le monde!"

msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Il y a un élément."
msgstr[1] "Il y a {0} éléments."
```

This example uses the following syntax:

*   `#:`: A comment indicating the context of the string to be translated. The same string might be translated differently depending on where it's being used.
*   `msgid`: The untranslated string.
*   `msgstr`: The translated string.

In the case of pluralization support, more entries can be defined.

*   `msgid_plural`: The untranslated plural string.
*   `msgstr[0]`: The translated string for the case 0.
*   `msgstr[N]`: The translated string for the case N.

The PO file specification can be found [here](https://www.gnu.org/savannah-checkouts/gnu/gettext/manual/html_node/PO-Files.html).

This example is based on an ASP.NET Core MVC application generated from a Visual Studio 2019 project template.

Add a reference to the `OrchardCore.Localization.Core` NuGet package.

The `.csproj` file now contains a line similar to the following (version number may vary):

```
<PackageReference Include="OrchardCore.Localization.Core" Version="1.2.0" />
```

Add the required services to the `ConfigureServices` method of `Startup.cs`:

```
public void ConfigureServices(IServiceCollection services)
{
    services.AddRazorPages()
        .AddViewLocalization(LanguageViewLocationExpanderFormat.Suffix);

    services.AddPortableObjectLocalization();

    services.Configure<RequestLocalizationOptions>(options => options
        .AddSupportedCultures("fr", "cs")
        .AddSupportedUICultures("fr", "cs")
    );
}
```

Add the required middleware to the `Configure` method of `Startup.cs`:

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/Home/Error");
    }

    app.UseRouting();
    app.UseStaticFiles();

    app.UseRequestLocalization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllerRoute(name: "default", pattern: "{controller=Home}/{action=Index}/{id?}");
    });
}
```

Add the following code to your Razor page of choice. `Index.cshtml` is used in this example.

```
@page
@using Microsoft.AspNetCore.Mvc.Localization
@inject IViewLocalizer Localizer
@{
    ViewData["Title"] = "Home";
}

<div class="text-center">
    <h1 class="display-4">Welcome</h1>
    <p>Learn about <a href="https://docs.microsoft.com/aspnet/core">building Web apps with ASP.NET Core</a>.</p>
</div>

<p>@Localizer["Hello world!"]</p>
```

An `IViewLocalizer` instance is injected and used to translate the text "Hello world!".

Create a file named _<culture code>.po_ in your application root folder. In this example, the file name is _fr.po_ because the French language is used:

```
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

This file stores both the string to translate and the French-translated string. Translations revert to their parent culture, if necessary. In this example, the _fr.po_ file is used if the requested culture is `fr-FR` or `fr-CA`.

Run your application, and navigate to the URL `/Index`. The text **Hello world!** is displayed.

Navigate to the URL `/Index?culture=fr-FR`. The text **Bonjour le monde!** is displayed.

PO files support pluralization forms, which is useful when the same string needs to be translated differently based on a cardinality. This task is made complicated by the fact that each language defines custom rules to select which string to use based on the cardinality.

The Orchard Localization package provides an API to invoke these different plural forms automatically.

Add the following content to the previously mentioned _fr.po_ file:

```
msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Il y a un élément."
msgstr[1] "Il y a {0} éléments."
```

See [What is a PO file?](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/portable-object-localization?view=aspnetcore-10.0#what-is-a-po-file) for an explanation of what each entry in this example represents.

English and French strings were used in the previous example. English and French have only two pluralization forms and share the same form rules, which is that a cardinality of one is mapped to the first plural form. Any other cardinality is mapped to the second plural form.

Not all languages share the same rules. This is illustrated with the Czech language, which has three plural forms.

Create the `cs.po` file as follows, and note how the pluralization needs three different translations:

```
msgid "Hello world!"
msgstr "Ahoj světe!!"

msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Existuje jedna položka."
msgstr[1] "Existují {0} položky."
msgstr[2] "Existuje {0} položek."
```

To accept Czech localizations, add `"cs"` to the list of supported cultures in the `ConfigureServices` method:

```
services.Configure<RequestLocalizationOptions>(options => options
                .AddSupportedCultures("fr", "cs")
                .AddSupportedUICultures("fr", "cs")
            );
```

Edit the `Pages/Index.cshtml` file to render localized, plural strings for several cardinalities:

```
<p>@Localizer.Plural(1, "There is one item.", "There are {0} items.")</p>
<p>@Localizer.Plural(2, "There is one item.", "There are {0} items.")</p>
<p>@Localizer.Plural(5, "There is one item.", "There are {0} items.")</p>
```

**Note:** In a real world scenario, a variable would be used to represent the count. Here, we repeat the same code with three different values to expose a very specific case.

Upon switching cultures, you see the following:

For `/Index`:

```
There is one item.
There are 2 items.
There are 5 items.
```

For `/Index?culture=fr`:

```
Il y a un élément.
Il y a 2 éléments.
Il y a 5 éléments.
```

For `/Index?culture=cs`:

```
Existuje jedna položka.
Existují 2 položky.
Existuje 5 položek.
```

Note that for the Czech culture, the three translations are different. The French and English cultures share the same construction for the two last translated strings.

Applications often contain the strings to be translated in several places. The same string may have a different translation in certain locations within an app (Razor views or class files). A PO file supports the notion of a file context, which can be used to categorize the string being represented. Using a file context, a string can be translated differently, depending on the file context (or lack of a file context).

The PO localization services use the name of the full class or the view that's used when translating a string. This is accomplished by setting the value on the `msgctxt` entry.

Consider a minor addition to the previous _fr.po_ example. A Razor view located at `Pages/Index.cshtml` can be defined as the file context by setting the reserved `msgctxt` entry's value:

```
msgctxt "Pages.Index"
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

With the `msgctxt` set as such, text translation occurs when navigating to `/Index?culture=fr-FR`. The translation won't occur when navigating to `/Privacy?culture=fr-FR`.

When no specific entry is matched with a given file context, Orchard Core's fallback mechanism looks for an appropriate PO file without a context. Assuming there's no specific file context defined for `Pages/Privacy.cshtml`, navigating to `/Privacy?culture=fr-FR` loads a PO file such as:

```
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

The default location of PO files can be changed in `ConfigureServices`:

```
services.AddPortableObjectLocalization(options => options.ResourcesPath = "Localization");
```

In this example, the PO files are loaded from the _Localization_ folder.

When more complex logic is needed to locate PO files, the `OrchardCore.Localization.PortableObject.ILocalizationFileLocationProvider` interface can be implemented and registered as a service. This is useful when PO files can be stored in varying locations or when the files have to be found within a hierarchy of folders.

The package includes a `Plural` extension method that's specific to two plural forms. For languages requiring more plural forms, create an extension method. With an extension method, you won't need to provide any localization file for the default language — the original strings are already available directly in the code.

You can use the more generic `Plural(int count, string[] pluralForms, params object[] arguments)` overload which accepts a string array of translations.

By [Sébastien Ros](https://github.com/sebastienros), [Scott Addie](https://twitter.com/Scott_Addie) and [Hisham Bin Ateya](https://github.com/hishamco)

This article walks through the steps for using Portable Object (PO) files in an ASP.NET Core application with the [Orchard Core](https://github.com/OrchardCMS/OrchardCore) framework.

**Note:** Orchard Core isn't a Microsoft product. Consequently, Microsoft provides no support for this feature.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/localization/sample/3.x/POLocalization) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

PO files are distributed as text files containing the translated strings for a given language. Some advantages of using PO files instead of _.resx_ files include:

*   PO files support pluralization; _.resx_ files don't support pluralization.
*   PO files aren't compiled like _.resx_ files. As such, specialized tooling and build steps aren't required.
*   PO files work well with collaborative online editing tools.

Here is a sample PO file containing the translation for two strings in French, including one with its plural form:

_fr.po_

```
#: Services/EmailService.cs:29
msgid "Enter a comma separated list of email addresses."
msgstr "Entrez une liste d'emails séparés par une virgule."

#: Views/Email.cshtml:112
msgid "The email address is \"{0}\"."
msgid_plural "The email addresses are \"{0}\"."
msgstr[0] "L'adresse email est \"{0}\"."
msgstr[1] "Les adresses email sont \"{0}\""
```

This example uses the following syntax:

*   `#:`: A comment indicating the context of the string to be translated. The same string might be translated differently depending on where it's being used.
*   `msgid`: The untranslated string.
*   `msgstr`: The translated string.

In the case of pluralization support, more entries can be defined.

*   `msgid_plural`: The untranslated plural string.
*   `msgstr[0]`: The translated string for the case 0.
*   `msgstr[N]`: The translated string for the case N.

The PO file specification can be found [here](https://www.gnu.org/savannah-checkouts/gnu/gettext/manual/html_node/PO-Files.html).

This example is based on an ASP.NET Core MVC application generated from a Visual Studio 2017 project template.

Add a reference to the `OrchardCore.Localization.Core` NuGet package.

The `.csproj` file now contains a line similar to the following (version number may vary):

```
<PackageReference Include="OrchardCore.Localization.Core" Version="1.0.0" />
```

Add the required services to the `ConfigureServices` method of `Startup.cs`:

```
public void ConfigureServices(IServiceCollection services)
{
    services.AddMvc()
        .AddViewLocalization(LanguageViewLocationExpanderFormat.Suffix);

    services.AddPortableObjectLocalization();

    services.Configure<RequestLocalizationOptions>(options =>
        {
            var supportedCultures = new List<CultureInfo>
            {
                new CultureInfo("en-US"),
                new CultureInfo("en"),
                new CultureInfo("fr-FR"),
                new CultureInfo("fr")
            };

            options.DefaultRequestCulture = new RequestCulture("en-US");
            options.SupportedCultures = supportedCultures;
            options.SupportedUICultures = supportedCultures;
        });
}
```

Add the required middleware to the `Configure` method of `Startup.cs`:

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/Home/Error");
    }

    app.UseRouting();
    app.UseStaticFiles();

    app.UseRequestLocalization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllerRoute(name: "default", pattern: "{controller=Home}/{action=Index}/{id?}");
    });
}
```

Add the following code to your Razor view of choice. `About.cshtml` is used in this example.

```
@using Microsoft.AspNetCore.Mvc.Localization
@inject IViewLocalizer Localizer

<p>@Localizer["Hello world!"]</p>
```

An `IViewLocalizer` instance is injected and used to translate the text "Hello world!".

Create a file named _<culture code>.po_ in your application root folder. In this example, the file name is _fr.po_ because the French language is used:

```
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

This file stores both the string to translate and the French-translated string. Translations revert to their parent culture, if necessary. In this example, the _fr.po_ file is used if the requested culture is `fr-FR` or `fr-CA`.

Run your application, and navigate to the URL `/Home/About`. The text **Hello world!** is displayed.

Navigate to the URL `/Home/About?culture=fr-FR`. The text **Bonjour le monde!** is displayed.

PO files support pluralization forms, which is useful when the same string needs to be translated differently based on a cardinality. This task is made complicated by the fact that each language defines custom rules to select which string to use based on the cardinality.

The Orchard Localization package provides an API to invoke these different plural forms automatically.

Add the following content to the previously mentioned _fr.po_ file:

```
msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Il y a un élément."
msgstr[1] "Il y a {0} éléments."
```

See [What is a PO file?](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/portable-object-localization?view=aspnetcore-10.0#what-is-a-po-file) for an explanation of what each entry in this example represents.

English and French strings were used in the previous example. English and French have only two pluralization forms and share the same form rules, which is that a cardinality of one is mapped to the first plural form. Any other cardinality is mapped to the second plural form.

Not all languages share the same rules. This is illustrated with the Czech language, which has three plural forms.

Create the `cs.po` file as follows, and note how the pluralization needs three different translations:

```
msgid "Hello world!"
msgstr "Ahoj světe!!"

msgid "There is one item."
msgid_plural "There are {0} items."
msgstr[0] "Existuje jedna položka."
msgstr[1] "Existují {0} položky."
msgstr[2] "Existuje {0} položek."
```

To accept Czech localizations, add `"cs"` to the list of supported cultures in the `ConfigureServices` method:

```
var supportedCultures = new List<CultureInfo>
{
    new CultureInfo("en-US"),
    new CultureInfo("en"),
    new CultureInfo("fr-FR"),
    new CultureInfo("fr"),
    new CultureInfo("cs")
};
```

Edit the `Views/Home/About.cshtml` file to render localized, plural strings for several cardinalities:

```
<p>@Localizer.Plural(1, "There is one item.", "There are {0} items.")</p>
<p>@Localizer.Plural(2, "There is one item.", "There are {0} items.")</p>
<p>@Localizer.Plural(5, "There is one item.", "There are {0} items.")</p>
```

**Note:** In a real world scenario, a variable would be used to represent the count. Here, we repeat the same code with three different values to expose a very specific case.

Upon switching cultures, you see the following:

For `/Home/About`:

```
There is one item.
There are 2 items.
There are 5 items.
```

For `/Home/About?culture=fr`:

```
Il y a un élément.
Il y a 2 éléments.
Il y a 5 éléments.
```

For `/Home/About?culture=cs`:

```
Existuje jedna položka.
Existují 2 položky.
Existuje 5 položek.
```

Note that for the Czech culture, the three translations are different. The French and English cultures share the same construction for the two last translated strings.

Applications often contain the strings to be translated in several places. The same string may have a different translation in certain locations within an app (Razor views or class files). A PO file supports the notion of a file context, which can be used to categorize the string being represented. Using a file context, a string can be translated differently, depending on the file context (or lack of a file context).

The PO localization services use the name of the full class or the view that's used when translating a string. This is accomplished by setting the value on the `msgctxt` entry.

Consider a minor addition to the previous _fr.po_ example. A Razor view located at `Views/Home/About.cshtml` can be defined as the file context by setting the reserved `msgctxt` entry's value:

```
msgctxt "Views.Home.About"
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

With the `msgctxt` set as such, text translation occurs when navigating to `/Home/About?culture=fr-FR`. The translation won't occur when navigating to `/Home/Contact?culture=fr-FR`.

When no specific entry is matched with a given file context, Orchard Core's fallback mechanism looks for an appropriate PO file without a context. Assuming there's no specific file context defined for `Views/Home/Contact.cshtml`, navigating to `/Home/Contact?culture=fr-FR` loads a PO file such as:

```
msgid "Hello world!"
msgstr "Bonjour le monde!"
```

The default location of PO files can be changed in `ConfigureServices`:

```
services.AddPortableObjectLocalization(options => options.ResourcesPath = "Localization");
```

In this example, the PO files are loaded from the _Localization_ folder.

When more complex logic is needed to locate PO files, the `OrchardCore.Localization.PortableObject.ILocalizationFileLocationProvider` interface can be implemented and registered as a service. This is useful when PO files can be stored in varying locations or when the files have to be found within a hierarchy of folders.

The package includes a `Plural` extension method that's specific to two plural forms. For languages requiring more plural forms, create an extension method. With an extension method, you won't need to provide any localization file for the default language — the original strings are already available directly in the code.

You can use the more generic `Plural(int count, string[] pluralForms, params object[] arguments)` overload which accepts a string array of translations.
