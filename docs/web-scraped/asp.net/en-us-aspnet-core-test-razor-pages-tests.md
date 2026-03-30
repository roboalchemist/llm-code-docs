# Source: https://learn.microsoft.com/en-us/aspnet/core/test/razor-pages-tests?view=aspnetcore-10.0

Title: Razor Pages unit tests in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/test/razor-pages-tests?view=aspnetcore-10.0

Markdown Content:
ASP.NET Core supports unit tests of Razor Pages apps. Tests of the data access layer (DAL) and page models help ensure:

*   Parts of a Razor Pages app work independently and together as a unit during app construction.
*   Classes and methods have limited scopes of responsibility.
*   Additional documentation exists on how the app should behave.
*   Regressions, which are errors brought about by updates to the code, are found during automated building and deployment.

This topic assumes that you have a basic understanding of Razor Pages apps and unit tests. If you're unfamiliar with Razor Pages apps or test concepts, see the following topics:

*   [Razor Pages architecture and concepts in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0)
*   [Tutorial: Get started with Razor Pages in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0)
*   [Testing with `dotnet test`](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test)

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/test/razor-pages-tests/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

The sample project is composed of two apps:

| App | Project folder | Description |
| --- | --- | --- |
| Message app | _src/RazorPagesTestSample_ | Allows a user to add a message, delete one message, delete all messages, and analyze messages (find the average number of words per message). |
| Test app | _tests/RazorPagesTestSample.Tests_ | Used to unit test the DAL and Index page model of the message app. |

The tests can be run using the built-in test features of an IDE, such as [Visual Studio](https://learn.microsoft.com/en-us/visualstudio/test/unit-test-your-code). If using [Visual Studio Code](https://code.visualstudio.com/) or the command line, execute the following command at a command prompt in the _tests/RazorPagesTestSample.Tests_ folder:

```
dotnet test
```

The message app is a Razor Pages message system with the following characteristics:

*   The Index page of the app (`Pages/Index.cshtml` and `Pages/Index.cshtml.cs`) provides a UI and page model methods to control the addition, deletion, and analysis of messages (find the average number of words per message).
*   A message is described by the `Message` class (`Data/Message.cs`) with two properties: `Id` (key) and `Text` (message). The `Text` property is required and limited to 200 characters.
*   Messages are stored using [Entity Framework's in-memory database](https://learn.microsoft.com/en-us/ef/core/providers/in-memory/)†.
*   The app contains a DAL in its database context class, `AppDbContext` (`Data/AppDbContext.cs`). The DAL methods are marked `virtual`, which allows mocking the methods for use in the tests.
*   If the database is empty on app startup, the message store is initialized with three messages. These _seeded messages_ are also used in tests.

†The EF topic, [Test with InMemory](https://learn.microsoft.com/en-us/ef/core/miscellaneous/testing/in-memory), explains how to use an in-memory database for tests with MSTest. This topic uses the [xUnit](https://github.com/xunit/xunit) test framework. Test concepts and test implementations across different test frameworks are similar but not identical.

Although the sample app doesn't use the repository pattern and isn't an effective example of the [Unit of Work (UoW) pattern](https://martinfowler.com/eaaCatalog/unitOfWork.html), Razor Pages supports these patterns of development. For more information, see [Designing the infrastructure persistence layer](https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design) and [Test controller logic in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/testing?view=aspnetcore-10.0) (the sample implements the repository pattern).

The test app is a console app inside the _tests/RazorPagesTestSample.Tests_ folder.

| Test app folder | Description |
| --- | --- |
| _UnitTests_ | * `DataAccessLayerTest.cs` contains the unit tests for the DAL. * `IndexPageTests.cs` contains the unit tests for the Index page model. |
| _Utilities_ | Contains the `TestDbContextOptions` method used to create new database context options for each DAL unit test so that the database is reset to its baseline condition for each test. |

The test framework is [xUnit](https://github.com/xunit/xunit). The object mocking framework is [Moq](https://github.com/moq/moq4).

The message app has a DAL with four methods contained in the `AppDbContext` class (`src/RazorPagesTestSample/Data/AppDbContext.cs`). Each method has one or two unit tests in the test app.

| DAL method | Function |
| --- | --- |
| `GetMessagesAsync` | Obtains a `List<Message>` from the database sorted by the `Text` property. |
| `AddMessageAsync` | Adds a `Message` to the database. |
| `DeleteAllMessagesAsync` | Deletes all `Message` entries from the database. |
| `DeleteMessageAsync` | Deletes a single `Message` from the database by `Id`. |

Unit tests of the DAL require [DbContextOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.dbcontextoptions) when creating a new `AppDbContext` for each test. One approach to creating the `DbContextOptions` for each test is to use a [DbContextOptionsBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.dbcontextoptionsbuilder):

```
var optionsBuilder = new DbContextOptionsBuilder<AppDbContext>()
    .UseInMemoryDatabase("InMemoryDb");

using (var db = new AppDbContext(optionsBuilder.Options))
{
    // Use the db here in the unit test.
}
```

The problem with this approach is that each test receives the database in whatever state the previous test left it. This can be problematic when trying to write atomic unit tests that don't interfere with each other. To force the `AppDbContext` to use a new database context for each test, supply a `DbContextOptions` instance that's based on a new service provider. The test app shows how to do this using its `Utilities` class method `TestDbContextOptions` (`tests/RazorPagesTestSample.Tests/Utilities/Utilities.cs`):

```
public static DbContextOptions<AppDbContext> TestDbContextOptions()
{
    // Create a new service provider to create a new in-memory database.
    var serviceProvider = new ServiceCollection()
        .AddEntityFrameworkInMemoryDatabase()
        .BuildServiceProvider();

    // Create a new options instance using an in-memory database and 
    // IServiceProvider that the context should resolve all of its 
    // services from.
    var builder = new DbContextOptionsBuilder<AppDbContext>()
        .UseInMemoryDatabase("InMemoryDb")
        .UseInternalServiceProvider(serviceProvider);

    return builder.Options;
}
```

Using the `DbContextOptions` in the DAL unit tests allows each test to run atomically with a fresh database instance:

```
using (var db = new AppDbContext(Utilities.TestDbContextOptions()))
{
    // Use the db here in the unit test.
}
```

Each test method in the `DataAccessLayerTest` class (`UnitTests/DataAccessLayerTest.cs`) follows a similar Arrange-Act-Assert pattern:

1.   Arrange: The database is configured for the test and/or the expected outcome is defined.
2.   Act: The test is executed.
3.   Assert: Assertions are made to determine if the test result is a success.

For example, the `DeleteMessageAsync` method is responsible for removing a single message identified by its `Id` (`src/RazorPagesTestSample/Data/AppDbContext.cs`):

```
public async virtual Task DeleteMessageAsync(int id)
{
    var message = await Messages.FindAsync(id);

    if (message != null)
    {
        Messages.Remove(message);
        await SaveChangesAsync();
    }
}
```

There are two tests for this method. One test checks that the method deletes a message when the message is present in the database. The other method tests that the database doesn't change if the message `Id` for deletion doesn't exist. The `DeleteMessageAsync_MessageIsDeleted_WhenMessageIsFound` method is shown below:

```
[Fact]
public async Task DeleteMessageAsync_MessageIsDeleted_WhenMessageIsFound()
{
    using (var db = new AppDbContext(Utilities.TestDbContextOptions()))
    {
        // Arrange
        var seedMessages = AppDbContext.GetSeedingMessages();
        await db.AddRangeAsync(seedMessages);
        await db.SaveChangesAsync();
        var recId = 1;
        var expectedMessages = 
            seedMessages.Where(message => message.Id != recId).ToList();

        // Act
        await db.DeleteMessageAsync(recId);

        // Assert
        var actualMessages = await db.Messages.AsNoTracking().ToListAsync();
        Assert.Equal(
            expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
            actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
    }
}
```

First, the method performs the Arrange step, where preparation for the Act step takes place. The seeding messages are obtained and held in `seedMessages`. The seeding messages are saved into the database. The message with an `Id` of `1` is set for deletion. When the `DeleteMessageAsync` method is executed, the expected messages should have all of the messages except for the one with an `Id` of `1`. The `expectedMessages` variable represents this expected outcome.

```
// Arrange
var seedMessages = AppDbContext.GetSeedingMessages();
await db.AddRangeAsync(seedMessages);
await db.SaveChangesAsync();
var recId = 1;
var expectedMessages = 
    seedMessages.Where(message => message.Id != recId).ToList();
```

The method acts: The `DeleteMessageAsync` method is executed passing in the `recId` of `1`:

```
// Act
await db.DeleteMessageAsync(recId);
```

Finally, the method obtains the `Messages` from the context and compares it to the `expectedMessages` asserting that the two are equal:

```
// Assert
var actualMessages = await db.Messages.AsNoTracking().ToListAsync();
Assert.Equal(
    expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
    actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
```

In order to compare that the two `List<Message>` are the same:

*   The messages are ordered by `Id`.
*   Message pairs are compared on the `Text` property.

A similar test method, `DeleteMessageAsync_NoMessageIsDeleted_WhenMessageIsNotFound` checks the result of attempting to delete a message that doesn't exist. In this case, the expected messages in the database should be equal to the actual messages after the `DeleteMessageAsync` method is executed. There should be no change to the database's content:

```
[Fact]
public async Task DeleteMessageAsync_NoMessageIsDeleted_WhenMessageIsNotFound()
{
    using (var db = new AppDbContext(Utilities.TestDbContextOptions()))
    {
        // Arrange
        var expectedMessages = AppDbContext.GetSeedingMessages();
        await db.AddRangeAsync(expectedMessages);
        await db.SaveChangesAsync();
        var recId = 4;

        // Act
        try
        {
            await db.DeleteMessageAsync(recId);
        }
        catch
        {
            // recId doesn't exist
        }

        // Assert
        var actualMessages = await db.Messages.AsNoTracking().ToListAsync();
        Assert.Equal(
            expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
            actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
    }
}
```

Another set of unit tests is responsible for tests of page model methods. In the message app, the Index page models are found in the `IndexModel` class in `src/RazorPagesTestSample/Pages/Index.cshtml.cs`.

| Page model method | Function |
| --- | --- |
| `OnGetAsync` | Obtains the messages from the DAL for the UI using the `GetMessagesAsync` method. |
| `OnPostAddMessageAsync` | If the [ModelState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary) is valid, calls `AddMessageAsync` to add a message to the database. |
| `OnPostDeleteAllMessagesAsync` | Calls `DeleteAllMessagesAsync` to delete all of the messages in the database. |
| `OnPostDeleteMessageAsync` | Executes `DeleteMessageAsync` to delete a message with the `Id` specified. |
| `OnPostAnalyzeMessagesAsync` | If one or more messages are in the database, calculates the average number of words per message. |

The page model methods are tested using seven tests in the `IndexPageTests` class (`tests/RazorPagesTestSample.Tests/UnitTests/IndexPageTests.cs`). The tests use the familiar Arrange-Act-Assert pattern. These tests focus on:

*   Determining if the methods follow the correct behavior when the [ModelState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary) is invalid.
*   Confirming the methods produce the correct [IActionResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.iactionresult).
*   Checking that property value assignments are made correctly.

This group of tests often mock the methods of the DAL to produce expected data for the Act step where a page model method is executed. For example, the `GetMessagesAsync` method of the `AppDbContext` is mocked to produce output. When a page model method executes this method, the mock returns the result. The data doesn't come from the database. This creates predictable, reliable test conditions for using the DAL in the page model tests.

The `OnGetAsync_PopulatesThePageModel_WithAListOfMessages` test shows how the `GetMessagesAsync` method is mocked for the page model:

```
var mockAppDbContext = new Mock<AppDbContext>(optionsBuilder.Options);
var expectedMessages = AppDbContext.GetSeedingMessages();
mockAppDbContext.Setup(
    db => db.GetMessagesAsync()).Returns(Task.FromResult(expectedMessages));
var pageModel = new IndexModel(mockAppDbContext.Object);
```

When the `OnGetAsync` method is executed in the Act step, it calls the page model's `GetMessagesAsync` method.

Unit test Act step (`tests/RazorPagesTestSample.Tests/UnitTests/IndexPageTests.cs`):

```
// Act
await pageModel.OnGetAsync();
```

`IndexPage` page model's `OnGetAsync` method (`src/RazorPagesTestSample/Pages/Index.cshtml.cs`):

```
public async Task OnGetAsync()
{
    Messages = await _db.GetMessagesAsync();
}
```

The `GetMessagesAsync` method in the DAL doesn't return the result for this method call. The mocked version of the method returns the result.

In the `Assert` step, the actual messages (`actualMessages`) are assigned from the `Messages` property of the page model. A type check is also performed when the messages are assigned. The expected and actual messages are compared by their `Text` properties. The test asserts that the two `List<Message>` instances contain the same messages.

```
// Assert
var actualMessages = Assert.IsAssignableFrom<List<Message>>(pageModel.Messages);
Assert.Equal(
    expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
    actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
```

Other tests in this group create page model objects that include the [DefaultHttpContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.defaulthttpcontext), the [ModelStateDictionary](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary), an [ActionContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.actioncontext) to establish the `PageContext`, a `ViewDataDictionary`, and a `PageContext`. These are useful in conducting tests. For example, the message app establishes a `ModelState` error with [AddModelError](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary.addmodelerror) to check that a valid [PageResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.razorpages.pageresult) is returned when `OnPostAddMessageAsync` is executed:

```
[Fact]
public async Task OnPostAddMessageAsync_ReturnsAPageResult_WhenModelStateIsInvalid()
{
    // Arrange
    var optionsBuilder = new DbContextOptionsBuilder<AppDbContext>()
        .UseInMemoryDatabase("InMemoryDb");
    var mockAppDbContext = new Mock<AppDbContext>(optionsBuilder.Options);
    var expectedMessages = AppDbContext.GetSeedingMessages();
    mockAppDbContext.Setup(db => db.GetMessagesAsync()).Returns(Task.FromResult(expectedMessages));
    var httpContext = new DefaultHttpContext();
    var modelState = new ModelStateDictionary();
    var actionContext = new ActionContext(httpContext, new RouteData(), new PageActionDescriptor(), modelState);
    var modelMetadataProvider = new EmptyModelMetadataProvider();
    var viewData = new ViewDataDictionary(modelMetadataProvider, modelState);
    var tempData = new TempDataDictionary(httpContext, Mock.Of<ITempDataProvider>());
    var pageContext = new PageContext(actionContext)
    {
        ViewData = viewData
    };
    var pageModel = new IndexModel(mockAppDbContext.Object)
    {
        PageContext = pageContext,
        TempData = tempData,
        Url = new UrlHelper(actionContext)
    };
    pageModel.ModelState.AddModelError("Message.Text", "The Text field is required.");

    // Act
    var result = await pageModel.OnPostAddMessageAsync();

    // Assert
    Assert.IsType<PageResult>(result);
}
```

*   [Testing with `dotnet test`](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test)
*   [Test controller logic in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/testing?view=aspnetcore-10.0)
*   [Unit Test Your Code](https://learn.microsoft.com/en-us/visualstudio/test/unit-test-your-code) (Visual Studio)
*   [Integration tests in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0)
*   [xUnit.net](https://github.com/xunit/xunit)
*   [Getting started with xUnit.net](https://xunit.net/docs/getting-started/netcore/cmdline)
*   [Moq](https://github.com/moq/moq4)
*   [Moq Quickstart](https://github.com/Moq/moq4/wiki/Quickstart)

ASP.NET Core supports unit tests of Razor Pages apps. Tests of the data access layer (DAL) and page models help ensure:

*   Parts of a Razor Pages app work independently and together as a unit during app construction.
*   Classes and methods have limited scopes of responsibility.
*   Additional documentation exists on how the app should behave.
*   Regressions, which are errors brought about by updates to the code, are found during automated building and deployment.

This topic assumes that you have a basic understanding of Razor Pages apps and unit tests. If you're unfamiliar with Razor Pages apps or test concepts, see the following topics:

*   [Razor Pages architecture and concepts in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0)
*   [Tutorial: Get started with Razor Pages in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0)
*   [Testing with `dotnet test`](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test)

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/test/razor-pages-tests/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

The sample project is composed of two apps:

| App | Project folder | Description |
| --- | --- | --- |
| Message app | _src/RazorPagesTestSample_ | Allows a user to add a message, delete one message, delete all messages, and analyze messages (find the average number of words per message). |
| Test app | _tests/RazorPagesTestSample.Tests_ | Used to unit test the DAL and Index page model of the message app. |

The tests can be run using the built-in test features of an IDE, such as [Visual Studio](https://learn.microsoft.com/en-us/visualstudio/test/unit-test-your-code). If using [Visual Studio Code](https://code.visualstudio.com/) or the command line, execute the following command at a command prompt in the _tests/RazorPagesTestSample.Tests_ folder:

```
dotnet test
```

The message app is a Razor Pages message system with the following characteristics:

*   The Index page of the app (`Pages/Index.cshtml` and `Pages/Index.cshtml.cs`) provides a UI and page model methods to control the addition, deletion, and analysis of messages (find the average number of words per message).
*   A message is described by the `Message` class (`Data/Message.cs`) with two properties: `Id` (key) and `Text` (message). The `Text` property is required and limited to 200 characters.
*   Messages are stored using [Entity Framework's in-memory database](https://learn.microsoft.com/en-us/ef/core/providers/in-memory/)†.
*   The app contains a DAL in its database context class, `AppDbContext` (`Data/AppDbContext.cs`). The DAL methods are marked `virtual`, which allows mocking the methods for use in the tests.
*   If the database is empty on app startup, the message store is initialized with three messages. These _seeded messages_ are also used in tests.

†The EF topic, [Test with InMemory](https://learn.microsoft.com/en-us/ef/core/miscellaneous/testing/in-memory), explains how to use an in-memory database for tests with MSTest. This topic uses the [xUnit](https://github.com/xunit/xunit) test framework. Test concepts and test implementations across different test frameworks are similar but not identical.

Although the sample app doesn't use the repository pattern and isn't an effective example of the [Unit of Work (UoW) pattern](https://martinfowler.com/eaaCatalog/unitOfWork.html), Razor Pages supports these patterns of development. For more information, see [Designing the infrastructure persistence layer](https://learn.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design) and [Test controller logic in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/testing?view=aspnetcore-10.0) (the sample implements the repository pattern).

The test app is a console app inside the _tests/RazorPagesTestSample.Tests_ folder.

| Test app folder | Description |
| --- | --- |
| _UnitTests_ | * `DataAccessLayerTest.cs` contains the unit tests for the DAL. * `IndexPageTests.cs` contains the unit tests for the Index page model. |
| _Utilities_ | Contains the `TestDbContextOptions` method used to create new database context options for each DAL unit test so that the database is reset to its baseline condition for each test. |

The test framework is [xUnit](https://github.com/xunit/xunit). The object mocking framework is [Moq](https://github.com/moq/moq4).

The message app has a DAL with four methods contained in the `AppDbContext` class (`src/RazorPagesTestSample/Data/AppDbContext.cs`). Each method has one or two unit tests in the test app.

| DAL method | Function |
| --- | --- |
| `GetMessagesAsync` | Obtains a `List<Message>` from the database sorted by the `Text` property. |
| `AddMessageAsync` | Adds a `Message` to the database. |
| `DeleteAllMessagesAsync` | Deletes all `Message` entries from the database. |
| `DeleteMessageAsync` | Deletes a single `Message` from the database by `Id`. |

Unit tests of the DAL require [DbContextOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.dbcontextoptions) when creating a new `AppDbContext` for each test. One approach to creating the `DbContextOptions` for each test is to use a [DbContextOptionsBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.dbcontextoptionsbuilder):

```
var optionsBuilder = new DbContextOptionsBuilder<AppDbContext>()
    .UseInMemoryDatabase("InMemoryDb");

using (var db = new AppDbContext(optionsBuilder.Options))
{
    // Use the db here in the unit test.
}
```

The problem with this approach is that each test receives the database in whatever state the previous test left it. This can be problematic when trying to write atomic unit tests that don't interfere with each other. To force the `AppDbContext` to use a new database context for each test, supply a `DbContextOptions` instance that's based on a new service provider. The test app shows how to do this using its `Utilities` class method `TestDbContextOptions` (`tests/RazorPagesTestSample.Tests/Utilities/Utilities.cs`):

```
public static DbContextOptions<AppDbContext> TestDbContextOptions()
{
    // Create a new service provider to create a new in-memory database.
    var serviceProvider = new ServiceCollection()
        .AddEntityFrameworkInMemoryDatabase()
        .BuildServiceProvider();

    // Create a new options instance using an in-memory database and 
    // IServiceProvider that the context should resolve all of its 
    // services from.
    var builder = new DbContextOptionsBuilder<AppDbContext>()
        .UseInMemoryDatabase("InMemoryDb")
        .UseInternalServiceProvider(serviceProvider);

    return builder.Options;
}
```

Using the `DbContextOptions` in the DAL unit tests allows each test to run atomically with a fresh database instance:

```
using (var db = new AppDbContext(Utilities.TestDbContextOptions()))
{
    // Use the db here in the unit test.
}
```

Each test method in the `DataAccessLayerTest` class (`UnitTests/DataAccessLayerTest.cs`) follows a similar Arrange-Act-Assert pattern:

1.   Arrange: The database is configured for the test and/or the expected outcome is defined.
2.   Act: The test is executed.
3.   Assert: Assertions are made to determine if the test result is a success.

For example, the `DeleteMessageAsync` method is responsible for removing a single message identified by its `Id` (`src/RazorPagesTestSample/Data/AppDbContext.cs`):

```
public async virtual Task DeleteMessageAsync(int id)
{
    var message = await Messages.FindAsync(id);

    if (message != null)
    {
        Messages.Remove(message);
        await SaveChangesAsync();
    }
}
```

There are two tests for this method. One test checks that the method deletes a message when the message is present in the database. The other method tests that the database doesn't change if the message `Id` for deletion doesn't exist. The `DeleteMessageAsync_MessageIsDeleted_WhenMessageIsFound` method is shown below:

```
[Fact]
public async Task DeleteMessageAsync_MessageIsDeleted_WhenMessageIsFound()
{
    using (var db = new AppDbContext(Utilities.TestDbContextOptions()))
    {
        // Arrange
        var seedMessages = AppDbContext.GetSeedingMessages();
        await db.AddRangeAsync(seedMessages);
        await db.SaveChangesAsync();
        var recId = 1;
        var expectedMessages = 
            seedMessages.Where(message => message.Id != recId).ToList();

        // Act
        await db.DeleteMessageAsync(recId);

        // Assert
        var actualMessages = await db.Messages.AsNoTracking().ToListAsync();
        Assert.Equal(
            expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
            actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
    }
}
```

First, the method performs the Arrange step, where preparation for the Act step takes place. The seeding messages are obtained and held in `seedMessages`. The seeding messages are saved into the database. The message with an `Id` of `1` is set for deletion. When the `DeleteMessageAsync` method is executed, the expected messages should have all of the messages except for the one with an `Id` of `1`. The `expectedMessages` variable represents this expected outcome.

```
// Arrange
var seedMessages = AppDbContext.GetSeedingMessages();
await db.AddRangeAsync(seedMessages);
await db.SaveChangesAsync();
var recId = 1;
var expectedMessages = 
    seedMessages.Where(message => message.Id != recId).ToList();
```

The method acts: The `DeleteMessageAsync` method is executed passing in the `recId` of `1`:

```
// Act
await db.DeleteMessageAsync(recId);
```

Finally, the method obtains the `Messages` from the context and compares it to the `expectedMessages` asserting that the two are equal:

```
// Assert
var actualMessages = await db.Messages.AsNoTracking().ToListAsync();
Assert.Equal(
    expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
    actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
```

In order to compare that the two `List<Message>` are the same:

*   The messages are ordered by `Id`.
*   Message pairs are compared on the `Text` property.

A similar test method, `DeleteMessageAsync_NoMessageIsDeleted_WhenMessageIsNotFound` checks the result of attempting to delete a message that doesn't exist. In this case, the expected messages in the database should be equal to the actual messages after the `DeleteMessageAsync` method is executed. There should be no change to the database's content:

```
[Fact]
public async Task DeleteMessageAsync_NoMessageIsDeleted_WhenMessageIsNotFound()
{
    using (var db = new AppDbContext(Utilities.TestDbContextOptions()))
    {
        // Arrange
        var expectedMessages = AppDbContext.GetSeedingMessages();
        await db.AddRangeAsync(expectedMessages);
        await db.SaveChangesAsync();
        var recId = 4;

        // Act
        await db.DeleteMessageAsync(recId);

        // Assert
        var actualMessages = await db.Messages.AsNoTracking().ToListAsync();
        Assert.Equal(
            expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
            actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
    }
}
```

Another set of unit tests is responsible for tests of page model methods. In the message app, the Index page models are found in the `IndexModel` class in `src/RazorPagesTestSample/Pages/Index.cshtml.cs`.

| Page model method | Function |
| --- | --- |
| `OnGetAsync` | Obtains the messages from the DAL for the UI using the `GetMessagesAsync` method. |
| `OnPostAddMessageAsync` | If the [ModelState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary) is valid, calls `AddMessageAsync` to add a message to the database. |
| `OnPostDeleteAllMessagesAsync` | Calls `DeleteAllMessagesAsync` to delete all of the messages in the database. |
| `OnPostDeleteMessageAsync` | Executes `DeleteMessageAsync` to delete a message with the `Id` specified. |
| `OnPostAnalyzeMessagesAsync` | If one or more messages are in the database, calculates the average number of words per message. |

The page model methods are tested using seven tests in the `IndexPageTests` class (`tests/RazorPagesTestSample.Tests/UnitTests/IndexPageTests.cs`). The tests use the familiar Arrange-Act-Assert pattern. These tests focus on:

*   Determining if the methods follow the correct behavior when the [ModelState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary) is invalid.
*   Confirming the methods produce the correct [IActionResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.iactionresult).
*   Checking that property value assignments are made correctly.

This group of tests often mock the methods of the DAL to produce expected data for the Act step where a page model method is executed. For example, the `GetMessagesAsync` method of the `AppDbContext` is mocked to produce output. When a page model method executes this method, the mock returns the result. The data doesn't come from the database. This creates predictable, reliable test conditions for using the DAL in the page model tests.

The `OnGetAsync_PopulatesThePageModel_WithAListOfMessages` test shows how the `GetMessagesAsync` method is mocked for the page model:

```
var mockAppDbContext = new Mock<AppDbContext>(optionsBuilder.Options);
var expectedMessages = AppDbContext.GetSeedingMessages();
mockAppDbContext.Setup(
    db => db.GetMessagesAsync()).Returns(Task.FromResult(expectedMessages));
var pageModel = new IndexModel(mockAppDbContext.Object);
```

When the `OnGetAsync` method is executed in the Act step, it calls the page model's `GetMessagesAsync` method.

Unit test Act step (`tests/RazorPagesTestSample.Tests/UnitTests/IndexPageTests.cs`):

```
// Act
await pageModel.OnGetAsync();
```

`IndexPage` page model's `OnGetAsync` method (`src/RazorPagesTestSample/Pages/Index.cshtml.cs`):

```
public async Task OnGetAsync()
{
    Messages = await _db.GetMessagesAsync();
}
```

The `GetMessagesAsync` method in the DAL doesn't return the result for this method call. The mocked version of the method returns the result.

In the `Assert` step, the actual messages (`actualMessages`) are assigned from the `Messages` property of the page model. A type check is also performed when the messages are assigned. The expected and actual messages are compared by their `Text` properties. The test asserts that the two `List<Message>` instances contain the same messages.

```
// Assert
var actualMessages = Assert.IsAssignableFrom<List<Message>>(pageModel.Messages);
Assert.Equal(
    expectedMessages.OrderBy(m => m.Id).Select(m => m.Text), 
    actualMessages.OrderBy(m => m.Id).Select(m => m.Text));
```

Other tests in this group create page model objects that include the [DefaultHttpContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.defaulthttpcontext), the [ModelStateDictionary](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary), an [ActionContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.actioncontext) to establish the `PageContext`, a `ViewDataDictionary`, and a `PageContext`. These are useful in conducting tests. For example, the message app establishes a `ModelState` error with [AddModelError](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary.addmodelerror) to check that a valid [PageResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.razorpages.pageresult) is returned when `OnPostAddMessageAsync` is executed:

```
[Fact]
public async Task OnPostAddMessageAsync_ReturnsAPageResult_WhenModelStateIsInvalid()
{
    // Arrange
    var optionsBuilder = new DbContextOptionsBuilder<AppDbContext>()
        .UseInMemoryDatabase("InMemoryDb");
    var mockAppDbContext = new Mock<AppDbContext>(optionsBuilder.Options);
    var expectedMessages = AppDbContext.GetSeedingMessages();
    mockAppDbContext.Setup(db => db.GetMessagesAsync()).Returns(Task.FromResult(expectedMessages));
    var httpContext = new DefaultHttpContext();
    var modelState = new ModelStateDictionary();
    var actionContext = new ActionContext(httpContext, new RouteData(), new PageActionDescriptor(), modelState);
    var modelMetadataProvider = new EmptyModelMetadataProvider();
    var viewData = new ViewDataDictionary(modelMetadataProvider, modelState);
    var tempData = new TempDataDictionary(httpContext, Mock.Of<ITempDataProvider>());
    var pageContext = new PageContext(actionContext)
    {
        ViewData = viewData
    };
    var pageModel = new IndexModel(mockAppDbContext.Object)
    {
        PageContext = pageContext,
        TempData = tempData,
        Url = new UrlHelper(actionContext)
    };
    pageModel.ModelState.AddModelError("Message.Text", "The Text field is required.");

    // Act
    var result = await pageModel.OnPostAddMessageAsync();

    // Assert
    Assert.IsType<PageResult>(result);
}
```

*   [Testing with `dotnet test`](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test)
*   [Test controller logic in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/testing?view=aspnetcore-10.0)
*   [Unit Test Your Code](https://learn.microsoft.com/en-us/visualstudio/test/unit-test-your-code) (Visual Studio)
*   [Integration tests in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0)
*   [xUnit.net](https://github.com/xunit/xunit)
*   [Getting started with xUnit.net](https://xunit.net/docs/getting-started/netcore/cmdline)
*   [Moq](https://github.com/moq/moq4)
*   [Moq Quickstart](https://github.com/Moq/moq4/wiki/Quickstart)
*   [JustMockLite](https://github.com/telerik/JustMockLite): A mocking framework for .NET developers. (_Not maintained or supported by Microsoft._)
