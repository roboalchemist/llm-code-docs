# Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview

Title: ASP.NET Core Editors DateRangePicker Overview - Telerik UI for ASP.NET Core

URL Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview

Published Time: Fri, 13 Mar 2026 08:59:17 GMT

Markdown Content:
New to Telerik UI for ASP.NET Core?[Start a free 30-day trial](https://www.telerik.com/try/aspnet-core-ui)

Updated

on Dec 10, 2025

The Telerik UI DateRangePicker TagHelper and HtmlHelper for ASP.NET Core are server-side wrappers for the Kendo UI DateRangePicker widget.

The DateRangePicker is a container for holding start and end date inputs. It allows the user to select a date range from a calendar or through a direct input. The helper also supports custom templates for its `month` view, configuration options for minimum and maximum dates, a start view, and a depth for navigation.

* [Demo page for the DateRangePicker HtmlHelper](https://demos.telerik.com/aspnet-core/daterangepicker/index)

* [Demo page for the DateRangePicker TagHelper](https://demos.telerik.com/aspnet-core/daterangepicker/tag-helper)

[Basic Configuration](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview#basic-configuration)
---------------------------------------------------------------------------------------------------------------------------------------------

The following example demonstrates the basic configuration for the DateRangePicker.

Razor

```
@(Html.Kendo().DateRangePicker()
        .Name("daterangepicker") // The name of the DateRangePicker is mandatory. It specifies the "id" attribute of the DateRangePicker.
        .Min(new DateTime(1900, 1, 1)) // Sets the min date of the DateRangePicker.
        .Max(new DateTime(2099, 12, 31)) // Sets the min date of the DateRangePicker.
        .Range(r => r.Start(DateTime.Now).End(DateTime.Now.AddDays(10))) // Sets the range of the DateRangePicker.
    )
```

> Starting with the 2024 Q3 release, the HtmlHelper version of the component supports [declarative initialization](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/helper-basics/declarative-initialization).

[DateOnly compatability](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview#dateonly-compatability)
---------------------------------------------------------------------------------------------------------------------------------------------------

As of the 2024 Q4 Release the ASP.NET Core DateRangePicker is compatible with the [`DateOnly`](https://learn.microsoft.com/en-us/dotnet/api/system.dateonly?view=net-8.0) type. Following this release you can also set the `Start` and `End` range of the component to a `DateOnly` property:

Razor

```
@(Html.Kendo().DateRangePicker()
        .Name("daterangepicker") 
        .Range(r => r.Start(new DateOnly(2024,5,6)).End(new DateOnly(2024,5,6).AddDays(10))) // Sets the range of the DateRangePicker.
    )
```

[Functionality and Features](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview#functionality-and-features)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

| Feature | Description |
| --- | --- |
| [Disabled dates](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/disabled-dates) | The DateRangePicker allows you to disable specific days that shouldn't be selected by the end user, such as weekends and national holidays. |
| [Selected dates](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/selected-dates) | The DateRangePicker allows you to define the minimum and maximum dates it displays and also render a pre-selected date range. |
| [Start view and navigation depth](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/nav-depth) | The DateRangePicker enables you to set the initially rendered view and define the navigation depth of the views. |
| [Validation](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/validation) | The DateRangePicker does not automatically update the typed text when the typed text is invalid. Such changes in the input value may lead to unexpected behavior. |
| [Date formatting](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/date-formatting) | The DateRangePicker allows you to define its date formatting. |
| [Calendar types](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/calendar-types) | The DateRangePicker works with `Date` objects which support only the [Gregorian](https://en.wikipedia.org/wiki/Gregorian_calendar) calendar. |
| [Week number column](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/week-num-column) | The DateRangePicker provides options for rendering a column which displays the number of the weeks within the current `Month` view. |
| [Globalization](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/globalization/overview) | The DateRangePicker comes with globalization support that allows you to use the component in apps all over the world. |
| [Accessibility](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/accessibility/overview) | The DateRangePicker is accessible for screen readers, supports WAI-ARIA attributes, and delivers [keyboard shortcuts](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/accessibility/key-nav) for faster navigation. |
| [Reverse Selection](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/reverse-selection) | The component allows you to pick an end date which is before the start date. |
| [Buttons](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/buttons) | Learn more about the buttons supported by the component. |
| [Automatic Correction](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/auto-adjust) | You can configure whether the component will autocorrect the user's input when the `Min` and `Max` values are set. |

[Referencing Existing Instances](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview#referencing-existing-instances)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

To reference an existing DateRangePicker instance, use the [`jQuery.data()`](http://api.jquery.com/jQuery.data/) method. Once a reference has been established, use the [DateRangePicker client-side API](https://docs.telerik.com/kendo-ui/api/javascript/ui/daterangepicker#methods) to control its behavior.

The following example demonstrates how to access an existing DateRangePicker instance.

Razor

```
// Place the following after the DateRangePicker for ASP.NET Core declaration.
    <script>
    $(function() {
    // The Name() of the DateRangePicker is used to get its client-side instance.
        var daterangepicker = $("#daterangepicker").data("kendoDateRangePicker");
    });
    </script>
```

[Next Steps](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview#next-steps)
---------------------------------------------------------------------------------------------------------------------------

* [Getting Started with the DateRangePicker](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/getting-started)

* [Basic Usage of the DateRangePicker HtmlHelper for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/daterangepicker/index)

* [Basic Usage of the DateRangePicker TagHelper for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/daterangepicker/tag-helper)

* [DateRangePicker in Razor Pages](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/razor-page)

[See Also](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/editors/daterangepicker/overview#see-also)
-----------------------------------------------------------------------------------------------------------------------

* [Using the API of the DateRangePicker for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/daterangepicker/api)
* [Knowledge Base Section](https://www.telerik.com/aspnet-core-ui/documentation/knowledge-base)
