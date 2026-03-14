# Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview

Title: ASP.NET Core Data Source Overview - Telerik UI for ASP.NET Core

URL Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview

Markdown Content:
New to Telerik UI for ASP.NET Core?[Start a free 30-day trial](https://www.telerik.com/try/aspnet-core-ui)

[ASP.NET Core DataSource Overview](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#aspnet-core-datasource-overview)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Dec 11, 2025

The Telerik UI DataSource TagHelper and HtmlHelper for ASP.NET Core are server-side wrappers for the Kendo UI for jQuery DataSource.

The DataSource is an abstraction for using local data or remote data. In most cases, the DataSource definition is declared as part of the configurations for the Telerik UI helpers. The standalone DataSource component is suitable for scenarios that require a shared data source.

* [Demo page for the DataSource HtmlHelper](https://demos.telerik.com/aspnet-core/datasource/index)

* [Demo page for the DataSource TagHelper](https://demos.telerik.com/aspnet-core/datasource/tag-helper)

[Initialize the DataSource](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#initialize-the-datasource)
--------------------------------------------------------------------------------------------------------------------------------------------

The following example demonstrates how to define the DataSource. You can access the DataSource instance by `Name()` on the client and use the [API methods and events of the Kendo UI for jQuery DataSource widget](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource).

Razor

```
@(Html.Kendo().DataSource<OrderViewModel>()
        .Name("myDataSource")
        .Ajax(d=>d.Read(r => r.Action("ReadOrders", "Home")))
    )

    <script>
        $(document).ready(function () {
            myDataSource.read(); // A POST request will be sent to the HomeController "ReadOrders" action.
        });
    </script>
```

> * If your data is `IQueryable<T>` returned by a LINQ-enabled provider—Entity Framework, LINQ to SQL, Telerik OpenAccess, NHibernate or other—the LINQ expressions, created by the `ToDataSourceResult` method, are converted to SQL and executed by the database server.
> * Use the `ToDataSourceResult()` method to page, sort, filter, and group the collection that is passed to it. If this collection is already paged, the method returns an empty result.
> * As of the R1 2017 SP1 release, you can use the `ToDataSourceResultAsync` extension method to provide the asynchronous functionality of `ToDataSourceResult` by leveraging the `async` and `await` features of the .NET Framework.
> * If impersonation is enabled, use the `ToDataSourceResultAsync` extension method with only one thread in your ASP.NET application. If you create a new thread, the impersonation in the newly created child thread decreases because, by default, all newly created child threads in ASP.NET run under the ASP.NET identity of the worker process. To change this behavior, explicitly impersonate the current identity within the code of the child thread.

To use `DataSourceRequest` and `ToDataSourceResult()` with the DataSource HtmlHelper, add the following namespaces with `using` directives in the Controller:

C#

```
using Kendo.Mvc.Extensions;
    using Kendo.Mvc.UI;
```

To use `DataSourceRequest` and `ToDataSourceResult()` with the DataSource TagHelper, in addition to the Kendo namespaces above, also add the following directive to the View:

Razor

`@addTagHelper *, Kendo.Mvc`

[Basic Configuration](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#basic-configuration)
--------------------------------------------------------------------------------------------------------------------------------

You can declare the DataSource component configuration options by using the available methods—for example, you can define the page size, page, sort order, filter, group, aggregates, and the model.

> * To [sort](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/configuration/sort#sort) the data based on an object, set [the data field, by which the data items are sorted,](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/configuration/sort#sortfield) to a property of that object.
> * To [group](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/configuration/group) the data by an object, set [the group by data item field](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/configuration/group#groupfield) to a property of that object.
> * To [filter](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/configuration/filter) the data based on an object, set [the data item field, to which the filter operator is applied,](https://docs.telerik.com/kendo-ui/api/javascript/data/datasource/configuration/filter#filterfield) to a property of that object.

The configuration accepts the definition for all CRUD operations and facilitates the data sorting, filtering, and grouping.

Razor

```
@(Html.Kendo().DataSource<Kendo.Mvc.Examples.Models.ProductViewModel>()
        .Name("dataSource1")
        .Ajax(dataSource => dataSource
          .Read(read => read.Action("Products_Read", "DataSource"))
          .ServerOperation(false)
          .PageSize(5)
          .Sort(sort => sort.Add("FieldName").Ascending())
          .Filter(filter => filter.Add(field => field.FieldName).StartsWith("A"))
          .Group(group => group.Add(field => field.FieldName))
        )
    )
```

[Prevent Ajax Response Caching](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#prevent-ajax-response-caching)
----------------------------------------------------------------------------------------------------------------------------------------------------

To prevent Ajax response caching, refer to [this section from the Frequently Asked Questions article](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/faq#how-can-i-prevent-ajax-response-caching)

[Model Mapping](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#model-mapping)
--------------------------------------------------------------------------------------------------------------------

In some cases, you may use view model objects instead of entities returned by Entity Framework. For example, you may want to avoid serializing all Entity Framework properties as JSON or prevent serialization exceptions caused by circular references.

To map to a ViewModel on the fly, pass a mapping lambda as a second parameter to the `ToDataSourceResult()` extension method.

> The naming of the model properties of the view model objects and entities returned by Entity Framework must match. If usage of different naming is desired, implement [model mapping](https://www.telerik.com/aspnet-core-ui/documentation/knowledge-base/datasource-model-mapping).

C#

```
public ActionResult Products_Read([DataSourceRequest]DataSourceRequest request)
    {
        using (var northwind = new NorthwindEntities())
        {
            IQueryable<Product> products = northwind.Products;
            // Convert the Product entities to ProductViewModel instances.
            DataSourceResult result = products.ToDataSourceResult(request, product => new ProductViewModel
            {
                ProductID = product.ProductID,
                ProductName = product.ProductName,
                UnitsInStock = product.UnitsInStock
            });

            return Json(result);
        }
    }
```

[Functionality and Features](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#functionality-and-features)
----------------------------------------------------------------------------------------------------------------------------------------------

| Feature | Description |
| --- | --- |
| [Model](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/model) | Many scenarios require you to configure the Model of the DataSource. |
| [Aggregates](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/aggregates) | You can easily calculate the aggregates of the data set like Min, Max, Average, etc. |
| [Filtering](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/filter) | The built-in filtering enables you to search for a subset of data among the items. |
| [Sorting](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/sort) | The DataSource supports ascending and descending sorting. |
| [Grouping](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/group) | You can group the returned data based on a common criteria. |
| [Headers](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/headers) | You can set request headers by using the Headers configuration option of the DataSource. |
| [DataSource Types](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/types) | You can choose the type of DataSource that best fits your needs. |
| [CRUD Operations](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/crud) | The DataSource supports easy set up of its CRUD operations and handles the server response on its own. |

[Next Steps](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#next-steps)
--------------------------------------------------------------------------------------------------------------

* [Getting Started with the DataSource](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/getting-started)

* [Basic Usage of the DataSource HtmlHelper for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/datasource/index)

* [Basic Usage of the DataSource TagHelper](https://demos.telerik.com/aspnet-core/datasource/tag-helper)

* [DataSource in Razor Pages](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/razor-page)

[See Also](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview#see-also)
----------------------------------------------------------------------------------------------------------

* [Knowledge Base Section](https://www.telerik.com/aspnet-core-ui/documentation/knowledge-base)

* [Server-Side HtmlHelper API](https://www.telerik.com/aspnet-core-ui/documentation/api/datasource)

* [Server-Side TagHelper API](https://www.telerik.com/aspnet-core-ui/documentation/api/taghelpers/datasource)
