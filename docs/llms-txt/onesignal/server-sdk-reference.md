# Source: https://documentation.onesignal.com/docs/en/server-sdk-reference.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Server SDK Reference

> Install, configure, and use OneSignal server SDKs to send push notifications, emails, and SMS from your backend in Node.js, Python, Java, Go, PHP, Ruby, C#, and Rust.

All OneSignal server SDKs are generated from the same OpenAPI specification, so they share a consistent interface regardless of language. Each SDK wraps the [OneSignal REST API](/reference/create-message) and provides typed models for requests and responses.

## Available SDKs

| Language  | Package                                                                                            | Repository                                                  |
| --------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Node.js   | [@onesignal/node-onesignal](https://www.npmjs.com/package/@onesignal/node-onesignal)               | [GitHub](https://github.com/OneSignal/node-onesignal)       |
| Python    | [onesignal-python-api](https://pypi.org/project/onesignal-python-api/)                             | [GitHub](https://github.com/OneSignal/onesignal-python-api) |
| Java      | [onesignal-java-client](https://central.sonatype.com/artifact/com.onesignal/onesignal-java-client) | [GitHub](https://github.com/OneSignal/onesignal-java-api)   |
| Go        | [onesignal-go-api](https://pkg.go.dev/github.com/OneSignal/onesignal-go-api)                       | [GitHub](https://github.com/OneSignal/onesignal-go-api)     |
| PHP       | [onesignal/onesignal-php-api](https://packagist.org/packages/onesignal/onesignal-php-api)          | [GitHub](https://github.com/OneSignal/onesignal-php-api)    |
| Ruby      | [onesignal](https://rubygems.org/gems/onesignal)                                                   | [GitHub](https://github.com/OneSignal/onesignal-ruby-api)   |
| C# (.NET) | [OneSignalApi](https://www.nuget.org/packages/OneSignalApi)                                        | [GitHub](https://github.com/OneSignal/onesignal-dotnet-api) |
| Rust      | [onesignal-rust-api](https://crates.io/crates/onesignal-rust-api)                                  | [GitHub](https://github.com/OneSignal/onesignal-rust-api)   |
| C++       | —                                                                                                  | [GitHub](https://github.com/OneSignal/onesignal-cpp-api)    |

***

## Installation

<Tabs>
  <Tab title="Node.js">
    ```bash  theme={null}
    npm install @onesignal/node-onesignal
    ```
  </Tab>

  <Tab title="Python">
    ```bash  theme={null}
    pip install onesignal-python-api
    ```
  </Tab>

  <Tab title="Java">
    **Maven**

    ```xml  theme={null}
    <dependency>
      <groupId>com.onesignal</groupId>
      <artifactId>onesignal-java-client</artifactId>
      <version>5.3.0</version>
    </dependency>
    ```

    **Gradle**

    ```groovy  theme={null}
    implementation "com.onesignal:onesignal-java-client:5.3.0"
    ```
  </Tab>

  <Tab title="Go">
    ```bash  theme={null}
    go get github.com/OneSignal/onesignal-go-api/v5
    ```
  </Tab>

  <Tab title="PHP">
    Add to `composer.json`:

    ```json  theme={null}
    {
      "require": {
        "onesignal/onesignal-php-api": "*@dev"
      }
    }
    ```

    Then run `composer update`.
  </Tab>

  <Tab title="Ruby">
    Add to your `Gemfile`:

    ```ruby  theme={null}
    gem 'onesignal', '~> 5.3.0-beta1'
    ```

    Then run `bundle install`.
  </Tab>

  <Tab title="C# (.NET)">
    ```bash  theme={null}
    dotnet add package OneSignalApi
    ```
  </Tab>

  <Tab title="Rust">
    Add to `Cargo.toml` under `[dependencies]`:

    ```toml  theme={null}
    onesignal-rust-api = "5.3.0"
    ```
  </Tab>
</Tabs>

***

## Configuration

Every SDK requires authentication via API keys. Two key types are available:

* **REST API Key** — required for most endpoints (sending notifications, managing users, etc.). Found in your app's **Settings > Keys & IDs**.
* **Organization API Key** — only required for organization-level endpoints like creating or listing apps. Found in **Organization Settings**.

<Tabs>
  <Tab title="Node.js">
    ```javascript  theme={null}
    const OneSignal = require('@onesignal/node-onesignal');

    const configuration = OneSignal.createConfiguration({
      restApiKey: 'YOUR_REST_API_KEY',
      organizationApiKey: 'YOUR_ORGANIZATION_API_KEY',
    });

    const client = new OneSignal.DefaultApi(configuration);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import onesignal
    from onesignal.api import default_api

    configuration = onesignal.Configuration(
        rest_api_key='YOUR_REST_API_KEY',
        organization_api_key='YOUR_ORGANIZATION_API_KEY',
    )

    with onesignal.ApiClient(configuration) as api_client:
        client = default_api.DefaultApi(api_client)
    ```
  </Tab>

  <Tab title="Java">
    ```java  theme={null}
    import com.onesignal.client.ApiClient;
    import com.onesignal.client.Configuration;
    import com.onesignal.client.auth.HttpBearerAuth;
    import com.onesignal.client.api.DefaultApi;

    ApiClient defaultClient = Configuration.getDefaultApiClient();

    HttpBearerAuth restApiAuth = (HttpBearerAuth) defaultClient
        .getAuthentication("rest_api_key");
    restApiAuth.setBearerToken("YOUR_REST_API_KEY");

    HttpBearerAuth orgApiAuth = (HttpBearerAuth) defaultClient
        .getAuthentication("organization_api_key");
    orgApiAuth.setBearerToken("YOUR_ORGANIZATION_API_KEY");

    DefaultApi client = new DefaultApi(defaultClient);
    ```
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import onesignal "github.com/OneSignal/onesignal-go-api"

    restAuth := context.WithValue(
        context.Background(),
        onesignal.RestApiKey,
        "YOUR_REST_API_KEY",
    )

    orgAuth := context.WithValue(
        restAuth,
        onesignal.OrganizationApiKey,
        "YOUR_ORGANIZATION_API_KEY",
    )

    apiClient := onesignal.NewAPIClient(onesignal.NewConfiguration())
    ```
  </Tab>

  <Tab title="PHP">
    ```php  theme={null}
    use onesignal\client\api\DefaultApi;
    use onesignal\client\Configuration;
    use GuzzleHttp;

    $config = Configuration::getDefaultConfiguration()
        ->setRestApiKeyToken('YOUR_REST_API_KEY')
        ->setOrganizationApiKeyToken('YOUR_ORGANIZATION_API_KEY');

    $client = new DefaultApi(
        new GuzzleHttp\Client(),
        $config
    );
    ```
  </Tab>

  <Tab title="Ruby">
    ```ruby  theme={null}
    require 'onesignal'

    OneSignal.configure do |config|
      config.rest_api_key = 'YOUR_REST_API_KEY'
      config.organization_api_key = 'YOUR_ORGANIZATION_API_KEY'
    end

    client = OneSignal::DefaultApi.new
    ```
  </Tab>

  <Tab title="C# (.NET)">
    ```csharp  theme={null}
    using OneSignalApi.Api;
    using OneSignalApi.Client;

    var config = new Configuration();
    config.BasePath = "https://api.onesignal.com";
    config.AccessToken = "YOUR_REST_API_KEY";

    var client = new DefaultApi(config);
    ```
  </Tab>

  <Tab title="Rust">
    ```rust  theme={null}
    use onesignal::apis::configuration::Configuration;

    fn create_configuration() -> Configuration {
        let mut config = Configuration::new();
        config.rest_api_key_token = Some("YOUR_REST_API_KEY".to_string());
        config.organization_api_key_token = Some("YOUR_ORGANIZATION_API_KEY".to_string());
        config
    }
    ```
  </Tab>
</Tabs>

<Warning>
  Store your API keys in environment variables or a secrets manager. Never commit them to source control.
</Warning>

***

## Send a push notification

Send push notifications to web and mobile [Subscriptions](./subscriptions) by targeting a segment.

<Tabs>
  <Tab title="Node.js">
    ```javascript  theme={null}
    const notification = new OneSignal.Notification();
    notification.app_id = 'YOUR_APP_ID';
    notification.contents = { en: 'Hello from OneSignal!' };
    notification.headings = { en: 'Push Notification' };
    notification.included_segments = ['Subscribed Users'];

    const response = await client.createNotification(notification);
    console.log('Notification ID:', response.id);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    notification = onesignal.Notification(
        app_id='YOUR_APP_ID',
        contents=onesignal.StringMap(en='Hello from OneSignal!'),
        headings=onesignal.StringMap(en='Push Notification'),
        included_segments=['Subscribed Users'],
    )

    response = client.create_notification(notification)
    print('Notification ID:', response.id)
    ```
  </Tab>

  <Tab title="Java">
    ```java  theme={null}
    import com.onesignal.client.model.Notification;
    import com.onesignal.client.model.StringMap;

    Notification notification = new Notification();
    notification.setAppId("YOUR_APP_ID");

    StringMap contents = new StringMap();
    contents.en("Hello from OneSignal!");
    notification.setContents(contents);

    StringMap headings = new StringMap();
    headings.en("Push Notification");
    notification.setHeadings(headings);

    notification.setIncludedSegments(Arrays.asList("Subscribed Users"));

    var response = client.createNotification(notification);
    System.out.println("Notification ID: " + response.getId());
    ```
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    notification := *onesignal.NewNotification("YOUR_APP_ID")
    notification.SetContents(onesignal.StringMap{En: onesignal.PtrString("Hello from OneSignal!")})
    notification.SetHeadings(onesignal.StringMap{En: onesignal.PtrString("Push Notification")})
    notification.SetIncludedSegments([]string{"Subscribed Users"})

    response, _, err := apiClient.DefaultApi
        .CreateNotification(orgAuth)
        .Notification(notification)
        .Execute()

    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Notification ID:", response.GetId())
    ```
  </Tab>

  <Tab title="PHP">
    ```php  theme={null}
    use onesignal\client\model\Notification;
    use onesignal\client\model\StringMap;

    $content = new StringMap();
    $content->setEn('Hello from OneSignal!');

    $headings = new StringMap();
    $headings->setEn('Push Notification');

    $notification = new Notification();
    $notification->setAppId('YOUR_APP_ID');
    $notification->setContents($content);
    $notification->setHeadings($headings);
    $notification->setIncludedSegments(['Subscribed Users']);

    $response = $client->createNotification($notification);
    echo 'Notification ID: ' . $response->getId();
    ```
  </Tab>

  <Tab title="Ruby">
    ```ruby  theme={null}
    notification = OneSignal::Notification.new({
      app_id: 'YOUR_APP_ID',
      contents: { en: 'Hello from OneSignal!' },
      headings: { en: 'Push Notification' },
      included_segments: ['Subscribed Users']
    })

    response = client.create_notification(notification)
    puts "Notification ID: #{response.id}"
    ```
  </Tab>

  <Tab title="C# (.NET)">
    ```csharp  theme={null}
    using OneSignalApi.Model;

    var notification = new Notification(appId: "YOUR_APP_ID")
    {
        Contents = new StringMap(en: "Hello from OneSignal!"),
        Headings = new StringMap(en: "Push Notification"),
        IncludedSegments = new List<string> { "Subscribed Users" }
    };

    var response = client.CreateNotification(notification);
    Console.WriteLine("Notification ID: " + response.Id);
    ```
  </Tab>

  <Tab title="Rust">
    ```rust  theme={null}
    use onesignal::apis::default_api;
    use onesignal::models::{Notification, StringMap};

    let mut contents = StringMap::new();
    contents.en = Some("Hello from OneSignal!".to_string());

    let mut headings = StringMap::new();
    headings.en = Some("Push Notification".to_string());

    let mut notification = Notification::new("YOUR_APP_ID".to_string());
    notification.contents = Some(Box::new(contents));
    notification.headings = Some(Box::new(headings));
    notification.included_segments = Some(vec!["Subscribed Users".to_string()]);

    let config = create_configuration();
    let response = default_api::create_notification(&config, notification).await;
    ```
  </Tab>
</Tabs>

***

## Send an email

Send emails to [Subscriptions](./subscriptions) with the `email` channel.

<Tabs>
  <Tab title="Node.js">
    ```javascript  theme={null}
    const notification = new OneSignal.Notification();
    notification.app_id = 'YOUR_APP_ID';
    notification.email_subject = 'Important Update';
    notification.email_body = '<h1>Hello!</h1><p>This is an HTML email.</p>';
    notification.included_segments = ['Subscribed Users'];
    notification.channel_for_external_user_ids = 'email';

    const response = await client.createNotification(notification);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    notification = onesignal.Notification(
        app_id='YOUR_APP_ID',
        email_subject='Important Update',
        email_body='<h1>Hello!</h1><p>This is an HTML email.</p>',
        included_segments=['Subscribed Users'],
        channel_for_external_user_ids='email',
    )

    response = client.create_notification(notification)
    ```
  </Tab>

  <Tab title="Java">
    ```java  theme={null}
    Notification notification = new Notification();
    notification.setAppId("YOUR_APP_ID");
    notification.setEmailSubject("Important Update");
    notification.setEmailBody("<h1>Hello!</h1><p>This is an HTML email.</p>");
    notification.setIncludedSegments(Arrays.asList("Subscribed Users"));
    notification.setChannelForExternalUserIds("email");

    var response = client.createNotification(notification);
    ```
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    notification := *onesignal.NewNotification("YOUR_APP_ID")
    notification.SetEmailSubject("Important Update")
    notification.SetEmailBody("<h1>Hello!</h1><p>This is an HTML email.</p>")
    notification.SetIncludedSegments([]string{"Subscribed Users"})
    notification.SetChannelForExternalUserIds("email")

    response, _, err := apiClient.DefaultApi
        .CreateNotification(orgAuth)
        .Notification(notification)
        .Execute()
    ```
  </Tab>

  <Tab title="PHP">
    ```php  theme={null}
    $notification = new Notification();
    $notification->setAppId('YOUR_APP_ID');
    $notification->setEmailSubject('Important Update');
    $notification->setEmailBody('<h1>Hello!</h1><p>This is an HTML email.</p>');
    $notification->setIncludedSegments(['Subscribed Users']);
    $notification->setChannelForExternalUserIds('email');

    $response = $client->createNotification($notification);
    ```
  </Tab>

  <Tab title="Ruby">
    ```ruby  theme={null}
    notification = OneSignal::Notification.new({
      app_id: 'YOUR_APP_ID',
      email_subject: 'Important Update',
      email_body: '<h1>Hello!</h1><p>This is an HTML email.</p>',
      included_segments: ['Subscribed Users'],
      channel_for_external_user_ids: 'email'
    })

    response = client.create_notification(notification)
    ```
  </Tab>

  <Tab title="C# (.NET)">
    ```csharp  theme={null}
    var notification = new Notification(appId: "YOUR_APP_ID")
    {
        EmailSubject = "Important Update",
        EmailBody = "<h1>Hello!</h1><p>This is an HTML email.</p>",
        IncludedSegments = new List<string> { "Subscribed Users" },
        ChannelForExternalUserIds = "email"
    };

    var response = client.CreateNotification(notification);
    ```
  </Tab>

  <Tab title="Rust">
    ```rust  theme={null}
    let mut notification = Notification::new("YOUR_APP_ID".to_string());
    notification.email_subject = Some("Important Update".to_string());
    notification.email_body = Some("<h1>Hello!</h1><p>This is an HTML email.</p>".to_string());
    notification.included_segments = Some(vec!["Subscribed Users".to_string()]);
    notification.channel_for_external_user_ids = Some("email".to_string());

    let response = default_api::create_notification(&config, notification).await;
    ```
  </Tab>
</Tabs>

***

## Send an SMS

Send SMS text messages to [Subscriptions](./subscriptions) with the `sms` channel.

<Tabs>
  <Tab title="Node.js">
    ```javascript  theme={null}
    const notification = new OneSignal.Notification();
    notification.app_id = 'YOUR_APP_ID';
    notification.contents = { en: 'Your SMS message content here' };
    notification.included_segments = ['Subscribed Users'];
    notification.channel_for_external_user_ids = 'sms';
    notification.sms_from = '+15551234567';

    const response = await client.createNotification(notification);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    notification = onesignal.Notification(
        app_id='YOUR_APP_ID',
        contents=onesignal.StringMap(en='Your SMS message content here'),
        included_segments=['Subscribed Users'],
        channel_for_external_user_ids='sms',
        sms_from='+15551234567',
    )

    response = client.create_notification(notification)
    ```
  </Tab>

  <Tab title="Java">
    ```java  theme={null}
    StringMap contents = new StringMap();
    contents.en("Your SMS message content here");

    Notification notification = new Notification();
    notification.setAppId("YOUR_APP_ID");
    notification.setContents(contents);
    notification.setIncludedSegments(Arrays.asList("Subscribed Users"));
    notification.setChannelForExternalUserIds("sms");
    notification.setSmsFrom("+15551234567");

    var response = client.createNotification(notification);
    ```
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    notification := *onesignal.NewNotification("YOUR_APP_ID")
    notification.SetContents(onesignal.StringMap{En: onesignal.PtrString("Your SMS message content here")})
    notification.SetIncludedSegments([]string{"Subscribed Users"})
    notification.SetChannelForExternalUserIds("sms")
    notification.SetSmsFrom("+15551234567")

    response, _, err := apiClient.DefaultApi
        .CreateNotification(orgAuth)
        .Notification(notification)
        .Execute()
    ```
  </Tab>

  <Tab title="PHP">
    ```php  theme={null}
    $content = new StringMap();
    $content->setEn('Your SMS message content here');

    $notification = new Notification();
    $notification->setAppId('YOUR_APP_ID');
    $notification->setContents($content);
    $notification->setIncludedSegments(['Subscribed Users']);
    $notification->setChannelForExternalUserIds('sms');
    $notification->setSmsFrom('+15551234567');

    $response = $client->createNotification($notification);
    ```
  </Tab>

  <Tab title="Ruby">
    ```ruby  theme={null}
    notification = OneSignal::Notification.new({
      app_id: 'YOUR_APP_ID',
      contents: { en: 'Your SMS message content here' },
      included_segments: ['Subscribed Users'],
      channel_for_external_user_ids: 'sms',
      sms_from: '+15551234567'
    })

    response = client.create_notification(notification)
    ```
  </Tab>

  <Tab title="C# (.NET)">
    ```csharp  theme={null}
    var notification = new Notification(appId: "YOUR_APP_ID")
    {
        Contents = new StringMap(en: "Your SMS message content here"),
        IncludedSegments = new List<string> { "Subscribed Users" },
        ChannelForExternalUserIds = "sms",
        SmsFrom = "+15551234567"
    };

    var response = client.CreateNotification(notification);
    ```
  </Tab>

  <Tab title="Rust">
    ```rust  theme={null}
    let mut contents = StringMap::new();
    contents.en = Some("Your SMS message content here".to_string());

    let mut notification = Notification::new("YOUR_APP_ID".to_string());
    notification.contents = Some(Box::new(contents));
    notification.included_segments = Some(vec!["Subscribed Users".to_string()]);
    notification.channel_for_external_user_ids = Some("sms".to_string());
    notification.sms_from = Some("+15551234567".to_string());

    let response = default_api::create_notification(&config, notification).await;
    ```
  </Tab>
</Tabs>

***

## Full API reference

Each server SDK supports the same set of API endpoints. Refer to your SDK's API documentation for the complete method list, including users, subscriptions, segments, templates, and more.

| SDK       | API reference                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------- |
| Node.js   | [DefaultApi.md](https://github.com/OneSignal/node-onesignal/blob/main/DefaultApi.md)              |
| Python    | [DefaultApi.md](https://github.com/OneSignal/onesignal-python-api/blob/main/docs/DefaultApi.md)   |
| Java      | [DefaultApi.md](https://github.com/OneSignal/onesignal-java-api/blob/main/docs/DefaultApi.md)     |
| Go        | [DefaultApi.md](https://github.com/OneSignal/onesignal-go-api/blob/main/docs/DefaultApi.md)       |
| PHP       | [DefaultApi.md](https://github.com/OneSignal/onesignal-php-api/blob/main/docs/Api/DefaultApi.md)  |
| Ruby      | [DefaultApi.md](https://github.com/OneSignal/onesignal-ruby-api/blob/main/docs/DefaultApi.md)     |
| C# (.NET) | [DefaultApi.md](https://github.com/OneSignal/onesignal-dotnet-api/blob/main/docs/DefaultApi.md)   |
| Rust      | [default\_api docs](https://github.com/OneSignal/onesignal-rust-api/blob/main/docs/DefaultApi.md) |
| C++       | [GitHub](https://github.com/OneSignal/onesignal-cpp-api)                                          |

For the underlying REST API, see the [complete API reference](/reference/create-message).

***

## FAQ

### Which server SDK should I choose?

Use the SDK that matches your backend language. All server SDKs are generated from the same OpenAPI specification and support the same endpoints, so functionality is identical across languages.

### What is the difference between the REST API Key and Organization API Key?

The **REST API Key** is scoped to a single app and is required for most operations like sending notifications and managing users. The **Organization API Key** is scoped to your organization and is only needed for creating or listing apps. Most integrations only need the REST API Key.

### Can I use the REST API directly instead of an SDK?

Yes. The server SDKs are convenience wrappers around the [OneSignal REST API](/reference/create-message). You can call the API directly using any HTTP client with Bearer token authentication.

### Are these SDKs auto-generated?

Yes. All server SDKs are generated from the OneSignal OpenAPI specification using [OpenAPI Generator](https://openapi-generator.tech). This ensures consistent API coverage across all languages.

Built with [Mintlify](https://mintlify.com).
