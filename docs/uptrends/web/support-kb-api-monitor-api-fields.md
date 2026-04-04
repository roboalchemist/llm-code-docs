# Source: https://www.uptrends.com/support/kb/api/monitor-api-fields/

Title: Monitor API fields | Uptrends

URL Source: https://www.uptrends.com/support/kb/api/monitor-api-fields/

Markdown Content:
**Note:** Effective 27 August 2025, some fields in the **GET and POST /Monitor** and **GET, PUT, and PATCH /Monitor/{monitorGuid}** endpoints will be deprecated. For more information, refer to the [API changelog](https://www.uptrends.com/support/kb/api/changelog/).

When working with the [Monitor API](https://www.uptrends.com/support/kb/api/monitor-api/) endpoint, the monitor object contains API fields, which may vary depending on the monitor type and its configuration. For more information about the available HTTP methods and monitor object model, refer to the [Uptrends API v4 documentation](https://api.uptrends.com/v4/swagger/index.html).

Common monitor fields
---------------------

The table shows the fields that are generally available for all monitor types.

| Field name | Description |
| --- | --- |
| `MonitorGuid` | The unique identifier of the monitor. This field must be omitted in your request body when using POST. It may be specified in PUT or PATCH requests, but it must match the monitorGuid specified in the URL of your API call. |
| `Name` | The name of the monitor. |
| `MonitorType` | The [type of monitor](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-types/). Once a monitor is created, the type cannot be changed. The availability of monitor types depends on your pricing plan. Values include: * `Http, Https, Connect, Ping, POP3, SMTP, SFTP, FTP` * `MySQL, MSSQL, WebserviceHttp, WebserviceHttps` * `DNS, IMAP, Certificate, FullPageCheck` * `MultiStepApi, PostmanApi, Transaction` |
| `GenerateAlert` | Indicates `true` if the **Generate Alerts** setting is enabled in the monitor. Otherwise, `false`, meaning no alerts will be generated for this monitor in case of an error. |
| `IsActive` | Indicates `true` if the monitor is actively running in the account. If the [monitor mode](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/monitor-mode/) is set to development mode, this value returns `false`. |
| `IsLocked` | Contains a read-only field and indicates `true` if the monitor is currently locked for editing. This happens if the Support team is reviewing your monitor. If you’ll include this field in a POST request, you must specify the value as `false`. If you’ll include this field in a PUT or PATCH request, you may only specify the current value for this monitor. For example, if the monitor is locked (true), your request must also be `"locked": true`. |
| `CustomFields` | Refers to the custom data set in the main settings of your monitor. This lets you include external information and custom data from third-party integrations as part of your alerting. For example, `{ "Component": "{{@CustomField(ComponentId)}}" }`For more information, refer to the [Custom fields](https://www.uptrends.com/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content/#including-external-ids-or-custom-data) article. |
| `SelectedCheckpoints` | An integer that refers to the [checkpoint regions or individual checkpoints](https://www.uptrends.com/checkpoints/) where the monitor is executed. |
| `UsePrimaryCheckpointsOnly` | Indicates `true` if the checkpoint selection is set to primary checkpoints, which is recommended. Otherwise, if the monitor is set to non-primary checkpoints, this returns `false`. For more information, refer to the [Checkpoints](https://www.uptrends.com/support/kb/synthetic-monitoring/checkpoints/non-primary-checkpoints/) article. |
| `CheckInterval` | An integer that indicates the time interval, in minutes, between individual checks. For more information, refer to the [Check interval](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/check-interval-explained/) article. |
| `MonitorMode` | Refers to whether the monitor is in `Development`, `Staging` or `Production` mode. For more information, refer to the [Monitor mode](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/monitor-mode/) article. |
| `Notes` | Custom notes or description set for the monitor. |
| `Hash` | The hash value corresponding to the monitor. |
| `CreatedDate` | The date and time when the monitor is created. |
| `LastModifiedDate` | The date and time when the monitor is last updated. |
| `NameForPhoneAlerts` | Refers to the value of the [speech-friendly monitor name](https://www.uptrends.com/support/kb/alerting/speech-friendly-monitor-names-for-phone-alerts/). This is the monitor name we’ll use in text-to-speech phone alerting, provided that the **Use alternate monitor names** has been enabled in the phone alert integration. If not, this field will not be available through the API. |

### Concurrent monitoring fields

The table shows the fields related to [concurrent monitoring](https://www.uptrends.com/support/kb/synthetic-monitoring/concurrent-monitoring/concurrent-monitoring-overview/) that are generally available for all monitor types.

| Field name | Description |
| --- | --- |
| `UseConcurrentMonitoring` | Indicates `true` if monitors can run multiple checks at once from multiple checkpoints. Otherwise, `false`. |
| `ConcurrentUnconfirmedErrorThreshold` | An integer that indicates the percentage of the total number of active checkpoints that returned unconfirmed errors. For more information, refer to the [How concurrent monitoring works](https://www.uptrends.com/support/kb/synthetic-monitoring/concurrent-monitoring/how-does-concurrent-monitoring-work/) article. |
| `ConcurrentConfirmedErrorThreshold` | An integer that indicates the percentage of the total number of active checkpoints that returned a confirmed error. For more information, refer to the [How concurrent monitoring works](https://www.uptrends.com/support/kb/synthetic-monitoring/concurrent-monitoring/how-does-concurrent-monitoring-work/) article. |

Other monitor fields
--------------------

The table shows the fields that may be available depending on the monitor type. The **Monitor type** column indicates whether the field is available to monitor types, such as [uptime (https, ssl, dns, and others)](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-types/#uptime-monitors-basic-checks), [browser for full page checks](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-types/#browser-monitors-full-page-check), [msa for multi-step API monitors](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-types/#api-monitors), [postman](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/postman-monitoring/postman-api-monitoring/), and [transaction](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-types/#transaction-monitors) monitors.

| Field name | Description | Monitor type |
| --- | --- | --- |
| `BrowserType` | The type of browser used to test the monitor. For more information, refer to the [Browser types](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/browser-types/) article. | `browser, transaction` |
| `BrowserWindowDimensions` | The browser’s dimension, such as screen size, user agent, or device model, used to test your website’s behavior. | `browser, transaction` |
| `HttpMethod` | The type of HTTP method used (`GET, POST`). | `https` |
| `RequestHeaders` | The name and value of the request headers. For example, `{"Key": "Accept", "Value": "application/json"}`. | `https, browser, transaction` |
| `RequestBody` | The value of the request body. For example, `name=Joe&productId={{ProductId}}&sols={{sols}}`. | `https` |
| `TlsVersion` | The TLS version used. For example, `Tls12_Tls11_Tls10`. | `https` |
| `HttpVersion` | The HTTP version used. For example `Negotiate`. | `https` |
| `UserAgent` | The browser type and version used to execute the monitor. If you leave this value empty, the `Native` user agent will be sent. For example, `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0`. For more information, refer to the [User agent](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks/#what-is-a-user-agent) article. | `https, browser, transaction` |
| `NetworkAddress` | The network address that should be used to connect to the server or service you want to monitor. When you specify a host name (for example, `server.your-domain.com`), that host name will be resolved during a monitor check on the checkpoint server that performs the check, using the DNS settings that are available on that location. Alternatively, specify an IPv4 or IPv6 address. If you want to specify a specific port number (when appropriate), please use the Port field. Port numbers should not be included in the NetworkAddress field. | `sftp, ftp, smtp, pop3, imap, mssql, mysql, ping, connect` |
| `Port` | The TCP port number that should be used to establish a connection to the host name or IP address you specified. | `dns, sftp, ftp, smtp, pop3, imap, mssql, mysql, connect` |
| `Url` | The full URL of the website, page, or service that you want to monitor. The URL should include http:// or https://. If necessary, you can also include a port number if you are using a non-default port number. For example, `https://your-domain.com:8080/your-page`. You can also use a fixed IP address as part of the URL instead of a host name, if your server listens to an incoming requests without a host name. | `https, ssl, browser` |
| `IpVersion` | Indicates which IP version, such as `IPv4` or `IPv6`, should be used to connect to the server or network address you specify. If you choose IPv6, the monitor will only be executed on checkpoint locations that support IPv6. | `https, ssl, connect, dns, sftp, ftp, smtp, pop3, imap, mssql, mysql ping` |
| `ThrottlingOptions` | Refers to the bandwidth throttling used and its type. The following fiels are available: * `ThrottlingType` — type of throttling used to simulate network conditions (`Inactive, Browser, Simulated`). * `ThrottlingValue` — value set for connection (`Adsl, Fiber, Cable, 2G, 3G, 4G`). * `ThrottlingSpeedUp` — upload speed limit. * `ThrottlingSpeedDown` — download speed limit. * `ThrottlingLatency` — an integer value for network latency. For example, `{"ThrottlingType":"Inactive","ThrottlingValue":"Adsl", "ThrottlingSpeedUp":0,"ThrottlingSpeedDown":0,"ThrottlingLatency":0}`. For more information, refer to the [Bandwidth throttling](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/bandwidth-throttling/) article. | `browser, transaction` |
| `IgnoreExternalElements` | Indicates `true` if the `Ignore external elements` is enabled in a Full Page Check monitor. This lets you ignore page elements of domains outside of the domain group when checking error conditions in the waterfall chart. | `browser` |
| `DatabaseName` | The name of the database used for database server monitor types. For more information, refer to the [Database server monitors](https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/database-server-monitors/) article. | `mssql, mysql` |
| `ImapSecureConnection` | `true` or `false`. Refers to whether the IMAP monitor type is connected securely to an IMAP server. For more information, refer to the [Mail server monitors](https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/mail-server-monitors/) article. | `imap` |
| `Credits` | The number of credits used in the monitor. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [Calculate credits](https://www.uptrends.com/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms/) article. | `msa, postman, transaction` |

### Authentication fields

| Field name | Description |
| --- | --- |
| `AuthenticationType` | The type of authentication to send authentication data along with the outgoing request (`None, Basic, NTLM, Digest`). For more information, refer to the [Authentication types](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/request/multi-step-authentication/) article. |
| `Username` | The credential used for the username. |
| `Password` | The credential used for the password. |

### Error condition fields

The `ErrorConditions` field refers to the criteria configured in your monitor to detect any errors on your website, web service, or server. This includes the following fields that may vary depending on the monitor type (excluding multi-step API monitors) and configuration:

```
"ErrorConditions": [
    {
      "ErrorConditionType": "LoadTimeLimit1",
      "Value": "2500",
      "Effect": "Indicate"
    },
    {
      "ErrorConditionType": "ConsoleContentMatch",
      "Value": "error",
      "Level": "Error",
      "MatchType": "ErrorWhenContains"
    },
    {
      "ErrorConditionType": "PageElementMaxSizeWithPercentage",
      "Value": "50",
      "Percentage": "10"
    }
    ...
 ]
```

| Field Name | Description |
| --- | --- |
| `ErrorConditionType` | Refers to the type of error condition, which can be any of the following: * [LoadTimeLimit1, LoadTimeLimit2](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview/) * [ContentMatch](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match/) * [HttpStatus](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability/) * [TotalMaxBytes, TotalMinBytes, PageElementMaxSizeWithPercentage, PageElementFailedWithPercentage](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources/) * [UseRecommendedCoreWebVitals](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals/) * [FirstContentfulPaintMaximum, LargestContentfulPaintMaximum, TimeToInteractiveMaximum, CumulativeLayoutShiftMaximum, TotalBlockingTimeMaximum](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals/) * [RequestStartMaximum, TimeToFirstByteMaximum, DomInteractiveMaximum, DomCompleteMaximum](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c/) * [ConsoleContentMatch, ConsoleLevel](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content/) * [PageElementUrlMatch](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check/) |
| `Value` | Refers to the threshold value set for the error condition type. |
| `Effect` | Refers to whether the error condition type [generates an error or only shows a color-code](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings/#only-color-code) status. |
| `Percentage` | Refers to the percentage value of the error condition, if applicable. |
| `Level` | Specifies the console log level (`Error, Warning, Info`) for `ConsoleContentMatch` error conditions. |
| `MatchType` | Defines how content matching is performed (`ErrorWhenContains`, `ErrorWhenNotContains`). |

### Domain group fields

| Field name | Description | Monitor type |
| --- | --- | --- |
| `DomainGroupGuid` | The unique identifier of the domain group. | `browser` |
| `DomainGroupGuidSpecified` | Indicates `true` if a domain group is used. Otherwise, `false`. For more information, refer to the [Working with domain groups](https://www.uptrends.com/support/kb/synthetic-monitoring/browser-monitoring/working-with-domain-groups/) article. | `browser` |

### Blocking fields

| Field name | Description | Monitor type |
| --- | --- | --- |
| `BlockGoogleAnalytics` | Indicates `true` if Google Analytics is blocked. Otherwise, `false`. For more information, refer to the [URL and analytics blocking](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/analytics-blocking/) article. | `browser, transaction` |
| `BlockUptrendsRum` | Indicates `true` if the Uptrends RUM is blocked. Otherwise, `false`. | `browser, transaction` |
| `BlockUrls` | Contains a list of full or partial URLs that will be blocked when the monitor makes a request. For more information, refer to the [URL and analytics blocking](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/analytics-blocking/) article. | `browser, transaction` |

### Custom metrics field

| Field name | Description | Monitor type |
| --- | --- | --- |
| `CustomMetrics` | The custom metric name and variable name used within the API scenario. For example `"CustomMetrics": [{"Name": "ProductId", "VariableName": "ProductId"}]`. For more information, refer to the [Custom metrics](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/custom-api-metrics-setup/) article. | `msa`, `transaction` |

### Certificate fields

The following fields are available for [SSL monitor types](https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors/) and other monitor types.

| Field name | Description | Monitor type |
| --- | --- | --- |
| `CertificateName` | The common name of the certificate. | `ssl` |
| `CertificateOrganization` | The value of the certificate organization. | `ssl` |
| `CertificateOrganizationalUnit` | The value of the certificate organizational unit. | `ssl` |
| `CertificateSerialNumber` | The serial number of the certificate. | `ssl` |
| `CertificateFingerprint` | The fingerprint value of the certificate. | `ssl` |
| `CertificateIssuerName` | The common name of the issuer. | `ssl` |
| `CertificateIssuerCompanyName` | The organization name of the issuer. | `ssl` |
| `CertificateIssuerOrganizationalUnit` | The organizational unit of the issuer. | `ssl` |
| `CertificateExpirationWarningDays` | The number of days before the certificate expires. | `ssl` |
| `CheckCertificateErrors` | Indicates `true` if the **Check SSL certificate errors** monitor setting is enabled. Otherwise, `false`. | `https, ssl` |

### DNS fields

The following fields are available for [DNS](https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/dns/dns-overview/) and other monitor types.

| Field name | Description | Monitor type |
| --- | --- | --- |
| `DnsServer` | The domain name or IP address of your DNS server. | `dns` |
| `DnsQuery` | The type of DNS query used for testing (`ARecord, CnameRecord, MxRecord, NsRecord, TxtRecord, SoaRecord, RootServer, AaaaRecord, SrvRecord`). | `dns` |
| `DnsExpectedResult` | The value that you expect from the DNS query. | `dns` |
| `DnsTestValue` | The value that you test for. This is usually the domain name you want to verify in your DNS server. For example, `www.yourdomain.com`. | `dns` |
| `DnsBypasses` | Refers to the source and target domains used in a DNS bypass. This ensures that the specified domain or IP address is always resolved, regardless of the actual DNS record. For more information, refer to the [DNS bypass](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/dns-bypass/) article. | `browser, dns, transaction` |

Monitor-specific fields
-----------------------

### Multi-step API (MSA) monitor fields

The table shows the fields that are available for [multi-step API monitor types](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview/).

| Field name | Description |
| --- | --- |
| `PredefinedVariables` | The key and value of the predefined variable used within the API scenario. For example, `"PredefinedVariables": [ { "Key": "ProductPrice","Value": "ProductPriceValue"}],`. For more information, refer to the [Predefined variables](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/response/multi-step-variables/#predefined-variables) article. |
| `UserDefinedFunctions` | The type and how the user-defined function was used. For example, `"UserDefinedFunctions": [{"Name": "CleanFileName","Type":"Regex","Regex": "(.+)\.jpg"}]`. For more information, refer to the [User-defined functions](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/user-defined-functions/user-defined-functions/) article. |
| `MultiStepApiTransactionScript` | A script that follows the value and definition of the [MsaSteps](https://www.uptrends.com/support/kb/api/monitor-api-fields/#multi-step-api-msa-monitor-fields) field, but in a different format. This includes the step details, such as the monitored URL, request and response components, and other API configurations. |

#### MsaSteps field

The `MsaSteps` field in an MSA monitor returns a JSON object that defines the structure of a step, including the monitored URL, request and response components, and other API configurations. This field returns the same structure and output you see when you click Switch to script from the Multi-step API monitor editor. Simply copy and paste the output from the monitor editor and use it as a reference for your API.

```
"MsaSteps": [
    {
      "Url": "https://galacticresorts.com/api/Destinations/{{ProductId}}",
      "Method": "GET", 
      "Body": "name=Joe&productId={{ProductId}}&sols={{sols}}\n",
      "MultiPartForm": [
        {
          "Type": "VaultFile",
          "Key": "file",
          "Value": "b84daa9c-cdf3-4ba8-90fa-49aa70dc80c0"
        }
      ],
      "RequestHeaders": [
        {
          "Key": "Accept",
          "Value": "application/json"
        }
      ],
      "Variables": [
        {
          "Source": "ResponseBodyJson",
          "Property": "[0].ProductId",
          "Name": "ProductId",
          "Arguments": []
        }
      ],
      "Assertions": [
        {
          "Source": "ResponseStatusCode",
          "Property": "",
          "Comparison": "Equal",
          "TargetValue": "200"
        },
        {
          "Source": "Duration",
          "Property": "",
          "Comparison": "LessThan",
          "TargetValue": "25000"
        }
      ],
      "Name": "Retrieve all destinations",
      "UseFixedClientCertificate": false,
      "Authentication": {
        "Id": "32398b2a-246b-493b-be9a-f714cb0c0f61",
        "AuthenticationType": "Basic",
        "UserName": "uname",
        "PasswordSpecified": false
      },
      "IgnoreCertificateErrors": false,
      "Delay": 0,
      "StepType": "HttpRequest",
      "RetryUntilSuccessful": false,
      "MaxAttempts": 0,
      "RetryWaitMilliseconds": 1000,
      "PreRequestScript": "",
      "PostResponseScript": "// Get the value of a variable\nvar output = ut.variables.get(\"ProductId\");\n\n// Log its value in the console log\nut.log(\"Product ID: \" + output);",
      "CalculatedContentType": "application/x-www-form-urlencoded",
      "AllowedTlsVersions": [
        "Tls13"
      ],
      "MsaStepHttpVersion": "Http1_1"
    ....
    }
]
```

| MsaSteps field name | Description |
| --- | --- |
| `Url` | The full URL of the website, page, or API endpoint that you want to monitor. |
| `Method` | The HTTP method, such as `GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS`. |
| `BodyType` | Type of request body (`Raw, MultiPartForm, and others`) |
| `MultiPartForm` | Type of multi-part form along with its details. |
| `RequestHeaders` | Defines the [HTTP request headers](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/multi-step/#request) as key-value pairs. |
| `Variables` | Defines the [variables](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/response/multi-step-variables/) that stores value from the response. |
| `Assertions` | Refers to how the [API response is checked and validated](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/response/multi-step-assertions/). |
| `Name` | Name of the step. |
| `UseFixedClientCertificate` | Indicates `true` if a **Client certificate** option is selected in a step. Otherwise, `false`. For more information, refer to [Multi-step monitoring Client certificates](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/request/multi-step-monitoring-client-certificate-authentication/). |
| `Authentication` | The [type of authentication](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/request/multi-step-authentication/) to send authentication data along with the outgoing request (`None, Basic, NTLM, Digest`). For more information, refer to the [Authentication fields](https://www.uptrends.com/support/kb/api/monitor-api-fields/#authentication-fields). |
| `IgnoreCertificateErrors` | Indicates `true` if the **HTTPS connection** setting is selected in a step. Otherwise, `false`. |
| `Delay` | An integer that specifies the wait step duration in milliseconds. |
| `StepType` | Refers to whether the step is a request step (`HttpRequest`) or a wait step (`Delay`). |
| `RetryUntilSuccessful` | Indicates `true` if the **Maximum number of attempts** setting is enabled in a step. Otherwise, `false`. |
| `MaxAttempts` | An integer that refers to how many times the monitor retries a step. |
| `RetryWaitMilliseconds` | An integer that refers to the interval in milliseconds before the monitor retries a step again. |
| `PreRequestScript` | The custom script written and executed in the **Pre-Request** tab. For more information, refer to the [Multi-step API custom scripting](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/multi-step-custom-scripting/) article. |
| `PostResponseScript` | The custom script written and executed in the **Post-Response** tab. For more information, refer to the [Multi-step API custom scripting](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/multi-step-custom-scripting/) article. |
| `CalculatedContentType` | The value of the `Content-Type` header when a request body is specified. |
| `AllowedTlsVersions` | Refers to the TLS version used in a step. |
| `MsaStepHttpVersion` | Refers to the HTTP version used in a step. |

For more information, refer to the [Multi-step API script editor](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/multi-step-api-monitoring/msa-script-editor/#switching-to-the-script-editor) article.

### Transaction monitor fields

The table shows the fields that are available for [transaction monitor types](https://www.uptrends.com/support/kb/synthetic-monitoring/transactions/transactions-overview/).

| Field name | Description |
| --- | --- |
| `SelfServiceTransactionScript` | A script that follows the value and definition of the [TransactionStepDefinition](https://www.uptrends.com/support/kb/api/monitor-api-fields/#transaction-monitor-fields) field output. This includes the step details, such as the monitored URL, request and response components, and other configurations. |

#### TransactionStepDefinition field

The `TransactionStepDefinition` field in a transaction monitor returns a JSON object that defines a transaction step, including the monitored URL, test and validation types, and other configurations. This field returns the same structure and output you see when you click Switch to script from the Transaction monitor editor. Simply copy and paste the output from the monitor editor and use it as a reference for your API.

```
"TransactionStepDefinition": [
    {
      "name": "Navigate to start URL",
      "recordWaterfall": true,
      "recordFilmstrip": true,
      "collectPageSource": true,
      "actions": [
        {
          "navigate": {
            "url": "http://galacticresorts.com/Products",
            "description": "Navigate to URL"
          }
        },
        {
          "testDocumentContent": {
            "value": "Book now",
            "testType": "Contains",
            "description": "Content check"
          }
        },
        {
          "screenshot": {}
        }
      ],
      "errorConditions": [
        {
          "type": "PageElementUrlMatch",
          "data": {
            "matchType": "ErrorWhenContainsRegex",
            "value": "error"
          },
          "additionalConditions": []
        },
      ]
    },
    {
      "name": "Select holiday destination (random)",
      "recordWaterfall": false,
      "recordFilmstrip": false,
      "collectPageSource": false,
      "actions": [
        {
          "click": {
            "element": {
              "xpath": "(//a[@class='btn btn-primary btn-lg'])[{{@RandomInt(1,3)}}]"
            },
            "description": "Select 1 of the 3 destinations randomly"
          }
        },
        {
          "testElementContent": {
            "value": ".*",
            "testType": "MatchesRegex",
            "assignVariable": "{{DestinationName}}",
            "element": {
              "xpath": "//div[@class='productdetail']//h1"
            },
            "description": "Save destination name to variable"
          }
        }
      ],
      "errorConditions": []
    },
    ....
  ]
```

| TransactionStepDefinition field name | Description |
| --- | --- |
| `Name` | Name of the step. |
| `recordWaterfall` | Indicates `true` if the **Waterfall** option is enabled in a step. For more information, refer to the [Waterfall](https://www.uptrends.com/support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls/) article. |
| `recordFilmstrip` | Indicates `true` if the **Filmstrip** option is enabled in a step. For more information, refer to the [Filmstrip](https://www.uptrends.com/support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls/) article. |
| `collectPageSource` | Indicates `true` if the **Page source** option is enabled in a step. For more information, refer to the [Page source](https://www.uptrends.com/support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log/#in-transaction-monitors) article. |
| `actions` | An array of [page interactions](https://www.uptrends.com/support/kb/synthetic-monitoring/transactions/page-interactions/) that describe what the monitor should do and verify within a step. Actions can include navigation to a URL, validating page content, taking screenshots, or other interactions that confirm the expected behavior of the application. |
| `errorConditions` | The criteria configured in a step to detect any errors on your website, web service, or server. For more information, refer to the [Error conditions field](https://www.uptrends.com/support/kb/api/monitor-api-fields/#error-condition-fields) section. |

For more information, refer to the [Transaction monitor script editor](https://www.uptrends.com/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor/#scripting-source-code-directly) article.

### SFTP fields

The following fields are available for [SFTP](https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/ftp-and-sftp/#what-actions-can-an-sftp-monitor-perform) monitors.

| Field name | Description | Monitor type |
| --- | --- | --- |
| `SftpAction` | Refers to the type of action or test the monitor performs. For example `ConnectOnly` or `TestFileExists`. | `sftp` |
| `SftpActionPath` | Refers to the file name or relative path to the test file. For example, `/test.txt`. | `sftp` |
