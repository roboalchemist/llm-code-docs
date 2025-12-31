# Source: https://firebase.google.com/docs/reference/admin/dotnet/migrate-dotnet-v2.md.txt

Firebase Admin SDK for .NET v2.0.0 introduces some breaking changes that may affect your application code. Review this guide, and make changes as necessary.

## Update target frameworks

The Admin SDK no longer supports`netstandard1.5`and`net45`[target framework monikers](https://docs.microsoft.com/en-us/dotnet/standard/frameworks). Instead, use`netstandard2.0`,`net461`or higher.

## Update code that uses the`PagedAsyncEnumerable`class

The Admin SDK provides several APIs that return instances of`PagedAsyncEnumerable`. This class provides a way to iterate through a sequence of items either one entry at a time or by pages. Because the Admin SDK is upgrading its dependency on the`Google.Api.Gax`package, you'll need to update code that uses the`PageAsyncEnumerable`class as follows:

**Before**  

    var pagedEnumerable = FirebaseAuth.DefaultInstance.ListUsersAsync(null);
    var responses = pagedEnumerable.AsRawResponses().GetEnumerator();
    while (await responses.MoveNext())
    {
        ExportedUserRecords response = responses.Current;
        foreach (ExportedUserRecord user in response.Users)
        {
            Console.WriteLine($"User: {user.Uid}");
        }
    }

    var enumerator = FirebaseAuth.DefaultInstance.ListUsersAsync(null).GetEnumerator();
    while (await enumerator.MoveNext())
    {
        ExportedUserRecord user = enumerator.Current;
        Console.WriteLine($"User: {user.Uid}");
    }

**After**  

    var pagedEnumerable = FirebaseAuth.DefaultInstance.ListUsersAsync(null);
    var responses = pagedEnumerable.AsRawResponses().GetAsyncEnumerator();
    while (await responses.MoveNextAsync())
    {
        ExportedUserRecords response = responses.Current;
        foreach (ExportedUserRecord user in response.Users)
        {
            Console.WriteLine($"User: {user.Uid}");
        }
    }

    var enumerator = FirebaseAuth.DefaultInstance.ListUsersAsync(null).GetAsyncEnumerator();
    while (await enumerator.MoveNextAsync())
    {
        ExportedUserRecord user = enumerator.Current;
        Console.WriteLine($"User: {user.Uid}");
    }