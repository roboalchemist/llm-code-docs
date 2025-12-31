# Source: https://resend.com/docs/send-with-dotnet.md

# Send emails with .NET

> Learn how to send your first email using the Resend .NET SDK.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

Prefer watching a video? Check out our video walkthrough below.

<YouTube id="HvFURxq1tgQ" />

## 1. Install

<CodeGroup>
  ```bash dotnet CLI theme={null}
  dotnet add package Resend
  ```

  ```bash Visual Studio (Package Manager Console) theme={null}
  PM> Install-Package Resend
  ```
</CodeGroup>

## 2. Send emails using HTML

In the startup of your application, configure the DI container as follows:

```csharp  theme={null}
using Resend;

builder.Services.AddOptions();
builder.Services.AddHttpClient<ResendClient>();
builder.Services.Configure<ResendClientOptions>( o =>
{
    o.ApiToken = Environment.GetEnvironmentVariable( "RESEND_APITOKEN" )!;
} );
builder.Services.AddTransient<IResend, ResendClient>();
```

Send an email using the injected `IResend` instance:

```csharp  theme={null}
using Resend;

public class FeatureImplementation
{
    private readonly IResend _resend;


    public FeatureImplementation( IResend resend )
    {
        _resend = resend;
    }


    public Task Execute()
    {
        var message = new EmailMessage();
        message.From = "Acme <onboarding@resend.dev>";
        message.To.Add( "delivered@resend.dev" );
        message.Subject = "hello world";
        message.HtmlBody = "<strong>it works!</strong>";

        await _resend.EmailSendAsync( message );
    }
}
```

## 3. Try it yourself

<CardGroup cols={2}>
  <Card title="ASP.NET Controller API" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-dotnet/tree/master/examples/WebControllerApi">
    See the full source code.
  </Card>

  <Card title="" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-dotnet/tree/master/examples">
    List of .NET examples (API, Web, HTML rendering, Async sending).
  </Card>
</CardGroup>
