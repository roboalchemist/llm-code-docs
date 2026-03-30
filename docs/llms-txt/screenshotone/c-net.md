# Source: https://screenshotone.com/docs/code-examples/c-net/

# C# (.NET) SDK and Code Examples

import Alert from "@/components/Alert.astro";

<Alert>
    If you have any questions, please, reach out at `support@screenshotone.com`.
</Alert>

<Alert>
    Massive thanks and rays of goodness to Andy Robinson ([Indie
    Hackers](https://www.indiehackers.com/TheOrigin),
    [GitHub](https://github.com/theorigin)) for providing the fully-featured
    high-quality C# (.NET) SDK.
</Alert>

### Installation

Add the library via nuget using the package manager console:

```bash
PM> Install-Package ScreenshotOne.dotnetsdk
```

Or from the .NET CLI as:

```bash
dotnet add package ScreenshotOne.dotnetsdk
```

### Usage

Don't forget to [sign up](https://dash.screenshotone.com/sign-up) to get access and secret keys.

Generate a screenshot URL without executing request:

```csharp
var client = new Client("&lt;access key&gt;", "&lt;secret key&gt;");
var options = TakeOptions.Url("https://www.amazon.com")
  .FullPage(true)
  .Format(Format.PNG)
  .BlockCookieBanners(true);

var url = client.GenerateTakeUrl(options);

// url = https://api.screenshotone.com/take?url=https%3A%2F%2Fwww.amazon.com&full_page=true&format=png&block_cookie_banners=true&access_key=_OzqMIjpCw-ARQ&signature=8a08e62d13a5c3490fda0734b6707791d3decc9ab9ba41e8cc045288a39db502

```

Take a screenshot and save the image in the file:

```csharp
var client = new Client("&lt;access key&gt;", "&lt;secret key&gt;");
var options = TakeOptions.Url("https://www.google.com")
  .FullPage(true)
  .Format(Format.PNG)
  .BlockCookieBanners(true);

var bytes = await client.Take(options);

File.WriteAllBytes(@"c:\temp\example.png", bytes);
```

Check out [other SDKs and code examples](/docs/code-examples/).