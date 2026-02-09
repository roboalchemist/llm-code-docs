# Source: https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info.md

---
title: User Monitoring and Protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > How App and API Protection
  Works in Datadog > User Monitoring and Protection
---

# User Monitoring and Protection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Instrument your services and track user activity to detect and block bad actors.

Add authenticated user information on traces to identify and block bad actors targeting your authenticated attack surface. To do this, set the user ID tag on the running APM trace, providing the necessary instrumentation for AAP to block authenticated attackers. This allows AAP to associate attacks and business logic events to users.

Track user logins and activity to detect account takeovers and business logic abuse with out-of-the-box detection rules, and to ultimately block attackers.

The custom user activity for which out-of-the-box detection rules are available are as follow:

| Built-in event names   | Required metadata                                                      | Related rules                                                                                                                                                                                                                                                                                           |
| ---------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `activity.sensitive`   | `{ "name": "coupon_use", "required_role": "user" }`                    | [Rate limited activity from IP](https://docs.datadoghq.com/security/default_rules/bl-rate-limiting/)[Unauthorized activity detected](https://docs.datadoghq.com/security/default_rules/bl-privilege-violation-user/)                                                                                    |
| `users.login.success`  | User ID is mandatory, optional metadata can be added                   | [Credential Stuffing attack](https://docs.datadoghq.com/security/default_rules/appsec-ato-groupby-ip/)[Bruteforce attack](https://docs.datadoghq.com/security/default_rules/appsec-ato-bf/)[Distributed Credential Stuffing](https://docs.datadoghq.com/security/default_rules/distributed-ato-ua-asn/) |
| `users.login.failure`  | User ID and `usr.exists` are mandatory, optional metadata can be added | [Credential Stuffing attack](https://docs.datadoghq.com/security/default_rules/appsec-ato-groupby-ip/)[Bruteforce attack](https://docs.datadoghq.com/security/default_rules/appsec-ato-bf/)[Distributed Credential Stuffing](https://docs.datadoghq.com/security/default_rules/distributed-ato-ua-asn/) |
| `users.signup`         | `{ "usr.id": "12345" }`                                                | [Excessive account creations from an IP](https://docs.datadoghq.com/security/default_rules/bl-signup-ratelimit/)                                                                                                                                                                                        |
| `users.delete`         | `{ "usr.id": "12345" }`                                                | [Excessive account deletion from an IP](https://docs.datadoghq.com/security/default_rules/bl-account-deletion-ratelimit/)                                                                                                                                                                               |
| `users.password_reset` | `{ "usr.id": "12345", "usr.login": "user@email.com", "exists": true }` | [Password reset brute force attempts](https://docs.datadoghq.com/security/default_rules/bl-password-reset/)                                                                                                                                                                                             |
| `payment.failure`      | None                                                                   | [Excessive payment failures from IP](https://docs.datadoghq.com/security/default_rules/bl-payment-failures/)                                                                                                                                                                                            |

## Adding authenticated user information to traces and enabling user blocking capability{% #adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability %}

{% alert level="info" %}
**Automated Detection of User Activity:** Datadog Tracing Libraries attempt to detect and report user activity events automatically. For more information, see [Disabling automatic user activity event tracking](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#disabling-automatic-user-activity-event-tracking).
{% /alert %}

You can [add custom tags to your root span](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/), or use the instrumentation functions described below.

{% tab title="Java" %}
Use the Java tracer's API for adding custom tags to a root span and add user information so that you can monitor authenticated requests in the application.

User monitoring tags are applied on the root span and start with the prefix `usr` followed by the name of the field. For example, `usr.name` is a user monitoring tag that tracks the user's name.

**Note**: Check that you have added [necessary dependencies to your application](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/opentracing/java#setup).

The example below shows how to obtain the root span, add the relevant user monitoring tags, and enable user blocking capability:

```java
import io.opentracing.Span;
import io.opentracing.util.GlobalTracer;
import datadog.appsec.api.blocking.Blocking;
import datadog.trace.api.interceptor.MutableSpan;

// Get the active span
final Span span = GlobalTracer.get().activeSpan();
if ((span instanceof MutableSpan)) {
   MutableSpan localRootSpan = ((MutableSpan) span).getLocalRootSpan();
   // Setting the mandatory user id tag
   localRootSpan.setTag("usr.id", "d131dd02c56eec4");
   // Setting optional user monitoring tags
   localRootSpan.setTag("usr.name", "Jean Example");
   localRootSpan.setTag("usr.email", "jean.example@example.com");
   localRootSpan.setTag("usr.session_id", "987654321");
   localRootSpan.setTag("usr.role", "admin");
   localRootSpan.setTag("usr.scope", "read:message, write:files");
}

Blocking
    .forUser("d131dd02c56eec4")
    .blockIfMatch();
```

{% /tab %}

{% tab title=".NET" %}
The .NET tracer package provides the `SetUser()` function, which allows you to monitor authenticated requests by adding user information to the trace.

The example below shows how to add the relevant user monitoring tags and enable user blocking capability:

```csharp

using Datadog.Trace;

// ...

    var userDetails = new UserDetails()
    {
        // the systems internal identifier for the users
        Id = "d41452f2-483d-4082-8728-171a3570e930",
        // the email address of the user
        Email = "test@adventure-works.com",
        // the user's name, as displayed by the system
        Name = "Jane Doh",
        // the user's session id
        SessionId = "d0632156-132b-4baa-95b2-a492c5f9cb16",
        // the role the user is making the request under
        Role = "standard",
    };
    Tracer.Instance.ActiveScope?.Span.SetUser(userDetails);
```

For information and options, read [the .NET tracer documentation](https://github.com/DataDog/dd-trace-dotnet/tree/master/docs/Datadog.Trace#user-identification).
{% /tab %}

{% tab title="Go" %}
The Go tracer package provides the `SetUser()` function, which allows you to monitor authenticated requests by adding user information to the trace. For more options, see [the Go tracer documentation](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace/tracer#SetUser) (or [v1 documentation](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer#SetUser)).

This example shows how to retrieve the current tracer span, use it to set user monitoring tags, and enable user blocking capability. **Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

```go
import (
  "github.com/DataDog/dd-trace-go/v2/appsec"
)

func handler(w http.ResponseWriter, r *http.Request) {
  if appsec.SetUser(r.Context(), "my-uid") != nil {
    // The user must be blocked by aborting the request handler asap.
    // The blocking response is automatically handled and sent by the appsec middleware.
    return
  }
}
```

{% /tab %}

{% tab title="Ruby" %}
Use one of the following APIs to add user information to a trace so that you can monitor authenticated requests in the application:

{% collapsible-section open=null %}
#### set_user

Starting with `ddtrace` 1.1.0, the `Datadog::Kit::Identity.set_user` method is available. This is the recommended API for adding user information to traces:

```ruby
# Get the active trace
trace = Datadog::Tracing.active_trace

# Set mandatory user id tag
Datadog::Kit::Identity.set_user(trace, id: 'd131dd02c56eeec4')

# Or set any of these optional user monitoring tags
Datadog::Kit::Identity.set_user(
  trace,

  # mandatory id
  id: 'd131dd02c56eeec4',

  # optional tags with known semantics
  name: 'Jean Example',
  email:, 'jean.example@example.com',
  session_id:, '987654321',
  role: 'admin',
  scope: 'read:message, write:files',

  # optional free-form tags
  another_tag: 'another_value',
)
```

{% /collapsible-section %}

{% collapsible-section open=null #ruby-set-tag %}
#### set_tag

If `Datadog::Kit::Identity.set_user` does not meet your needs, you can use `set_tag` instead.

User monitoring tags are applied on the trace and start with the prefix `usr.` followed by the name of the field. For example, `usr.name` is a user monitoring tag that tracks the user's name.

The example below shows how to obtain the active trace and add relevant user monitoring tags:

**Notes**:

- Tag values must be strings.
- The `usr.id` tag is mandatory.

```ruby
# Get the active trace
trace = Datadog::Tracing.active_trace

# Set mandatory user id tag
trace.set_tag('usr.id', 'd131dd02c56eeec4')

# Set optional user monitoring tags with known sematics
trace.set_tag('usr.name', 'Jean Example')
trace.set_tag('usr.email', 'jean.example@example.com')
trace.set_tag('usr.session_id', '987654321')
trace.set_tag('usr.role', 'admin')
trace.set_tag('usr.scope', 'read:message, write:files')

# Set free-form tags:
trace.set_tag('usr.another_tag', 'another_value')
```

{% /collapsible-section %}

{% /tab %}

{% tab title="PHP" %}
The PHP tracer provides the `\DDTrace\set_user()` function, which allows you to monitor and block authenticated requests.

`\DDTrace\set_user()` adds the relevant user tags and metadata to the trace and automatically performs user blocking.

The following example shows how to set user monitoring tags and enable user blocking:

```php
<?php
// Blocking is performed internally through the set_user call.
\DDTrace\set_user(
    // A unique identifier of the user is required.
    '123456789',

    // All other fields are optional.
    [
        'name' =>  'Jean Example',
        'email' => 'jean.example@example.com',
        'session_id' => '987654321',
        'role' => 'admin',
        'scope' => 'read:message, write:files',
    ]
);
?>
```

{% /tab %}

{% tab title="Node.js" %}
The Node tracer package provides the `tracer.setUser(user)` function, which allows you to monitor authenticated requests by adding user information to the trace.

The example below shows how to add relevant user monitoring tags and enable user blocking capability:

```javascript
const tracer = require('dd-trace').init()

function handle () {
  tracer.setUser({
    id: '123456789', // *REQUIRED* Unique identifier of the user.

    // All other fields are optional.
    email: 'jane.doe@example.com', // Email of the user.
    name: 'Jane Doe', // User-friendly name of the user.
    session_id: '987654321', // Session ID of the user.
    role: 'admin', // Role the user is making the request under.
    scope: 'read:message, write:files', // Scopes or granted authorizations the user currently possesses.

    // Arbitrary fields are also accepted to attach custom data to the user (RBAC, Oauth, etcâ¦)
    custom_tag: 'custom data'
  })

// Set the currently authenticated user and check whether they are blocked
if (tracer.appsec.isUserBlocked(user)) {  // also set the currently authenticated user
  return tracer.appsec.blockRequest(req, res) // blocking response is sent
  }

}
```

For information and options, read [the Node.js tracer documentation](https://datadoghq.dev/dd-trace-js/#set-user).
{% /tab %}

{% tab title="Python" %}
Starting in dd-trace-py v3.7, you can use the new Python tracer's SDK to track users and user events.

In previous versions, you can monitor authenticated requests by adding user information to the trace with the `set_user` function provided by the Python tracer package.

{% collapsible-section open=null #python-user-info-sdk %}
#### User Tracking SDK

Starting in dd-trace-py v3.7, this example shows how to set user monitoring tags and enable user blocking capability:

```python
from ddtrace.appsec.track_user_sdk import track_user

# starting in dd-trace-py v3.17, you can use track_user_id
# without login information, but user_id is required
# this is the recommended API since it enables best product functionality with least room for mistakes
track_user_id(
    "some_user_id",
    session_id="session_id",
    metadata={
        "name": "John",
        "email": "test@test.com",
        "scope": "some_scope",
        "role": "manager",
    },
)

# Alternatively, you can use track_user
user_login = "some_login"
# to enable all features (user_id and/or session_id monitoring and blocking), 
# make sure you provide the corresponding optional arguments
track_user(
    user_login,
    user_id="some_user_id",
    session_id="session_id",
    metadata={
        "name": "John",
        "email": "test@test.com",
        "scope": "some_scope",
        "role": "manager",
    },
)
```

{% /collapsible-section %}

{% collapsible-section open=null #python-user-info-legacy %}
#### Legacy API

This example shows how to set user monitoring tags and enable user blocking capability using the legacy API; however, using the new User Tracking SDK, described above, is encouraged.

```python
from ddtrace.contrib.trace_utils import set_user
from ddtrace import tracer
# Call set_user() to trace the currently authenticated user id
user_id = "some_user_id"
set_user(tracer, user_id, name="John", email="test@test.com", scope="some_scope",
         role="manager", session_id="session_id", propagate=True)
```

{% /collapsible-section %}

{% /tab %}

## Adding business logic information (login success, login failure, any business logic) to traces{% #adding-business-logic-information-login-success-login-failure-any-business-logic-to-traces %}

{% alert level="info" %}
**A note on usr.id and usr.login:** Investigation login abuse rely on two similar, but different concepts. usr.id contains the unique identifier of the user account in database. It's unique and immutable. It's unavailable when someone tries to log into a non-existant account. User blocking targets usr.id.The user generally isn't aware of their user ID. Instead, they rely on mutable identifiers (phone number, username, email address...). The string used by the user to log into an account should be reported as usr.login in login events.If no usr.login is provided, usr.id will be used instead.
{% /alert %}

{% tab title="Java" %}
Starting in dd-trace-java v1.8.0, you can use the Java tracer's API to track user events.

The following examples show how to track login events or custom events (using signup as an example).

{% collapsible-section open=null %}
#### Login success

```java
import datadog.trace.api.EventTracker;
import datadog.trace.api.GlobalTracer;

public class LoginController {

    private User doLogin(String userName, String password) {
        // this is where you get User based on userName/password credentials
        User user = checkLogin(userName, password);

        Map<String, String> metadata = new HashMap<>();
        metadata.put("email", user.getEmail());
        metadata.put("usr.login", userName);

        // If your system has multiple "tenants", please provide it. A tenant is an environment/group of user
        metadata.put("usr.org", usr.getTenant());

        // track user authentication success events
        GlobalTracer
            .getEventTracker()
            .trackLoginSuccessEvent(user.getId(), metadata);

    }
}
```

{% /collapsible-section %}

{% collapsible-section open=null #java-login-failure %}
#### Login failure

```java
import datadog.trace.api.EventTracker;
import datadog.trace.api.GlobalTracer;

public class LoginController {

    private User doLogin(String userName, String password) {
        // this is where you get User based on userName/password credentials
        User user = checkLogin(userName, password);

        // if function returns null - user doesn't exist
        boolean userExists = (user != null);
        String userId = null;
        Map<String, String> metadata = new HashMap<>();
        metadata.put("usr.login", userName);
        if (userExists != null) {
            userId = getUserId(userName)
            metadata.put("email", user.getEmail());
        } else {
            userId = userName;
        }

        // track user authentication error events
        GlobalTracer
            .getEventTracker()
            .trackLoginFailureEvent(userId, userExists, metadata);
    }
}
```

{% /collapsible-section %}

{% collapsible-section open=null #java-custom-business %}
#### Custom business logic

```java
import datadog.trace.api.EventTracker;
import datadog.trace.api.GlobalTracer;

public class LoginController {

    private User doSignup(String userId, String email) {
        // this is where you create your user account
        User user = createUser(userId, email);

        Map<String, String> metadata = new HashMap<>();
        metadata.put("usr.id", user.getId());

        // track user signup events
        GlobalTracer
            .getEventTracker()
            .trackCustomEvent("users.signup", metadata);
    }
}
```

{% /collapsible-section %}

{% /tab %}

{% tab title=".NET" %}
Starting in dd-trace-dotnet v2.23.0, you can use the .NET tracer's API to track user events.

The following examples show how to track login events or custom events (using signup as an example).

{% collapsible-section open=null %}
#### Login success

```csharp
using Datadog.Trace.AppSec;

void OnLogonSuccess(string userId, string login...)
{
    // metadata is optional
    var metadata = new Dictionary<string, string>()
    {
        { "usr.login", login }
    };
    EventTrackingSdk.TrackUserLoginSuccessEvent(userId, metadata);

    // ...
}
```

{% /collapsible-section %}

{% collapsible-section open=null #dotnet-login-failure %}
#### Login failure

```csharp
using Datadog.Trace.AppSec;

void OnLogonFailure(string userId, string login, bool userExists, ...)
{
    // If no userId can be provided, any unique user identifier (username, email...) may be used
    // metadata is optional
    var metadata = new Dictionary<string, string>()
    {
        { "usr.login", login }
    };
    EventTrackingSdk.TrackUserLoginFailureEvent(userId, userExists, metadata);

    // ...
}
```

{% /collapsible-section %}

{% collapsible-section open=null #dotnet-custom-business %}
#### Custom business logic

```csharp
void OnUserSignupComplete(string userId, ...)
{
    // the metadata parameter is optional, but adding the "usr.id"
    var metadata = new Dictionary<string, string>()
    {
        { "usr.id", userId }
    };
    // Leveraging custom business logic tracking to track user signups
    EventTrackingSdk.TrackCustomEvent("users.signup", metadata);

    // ...
}
```

{% /collapsible-section %}

{% /tab %}

{% tab title="Go" %}
Starting in dd-trace-go v1.47.0, you can use the Go tracer's API to track user events.

The following examples show how to track login events or custom events (using signup as an example). **Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

{% collapsible-section open=null %}
#### Login success

```go
import (
  "github.com/DataDog/dd-trace-go/v2/appsec"
)

func handler(w http.ResponseWriter, r *http.Request) {
  metadata := make(map[string]string) /* optional extra event metadata */
  userdata := /* optional extra user data */

  metadata["usr.login"] = "user-email"

  // Track login success, replace `my-uid` by a unique identifier of the user (such as numeric, username, and email)
  if appsec.TrackUserLoginSuccessEvent(r.Context(), "my-uid", metadata, userdata) != nil {
    // The given user id is blocked and the handler should be aborted asap.
    // The blocking response will be sent by the appsec middleware.
    return
  }
}
```

{% /collapsible-section %}

{% collapsible-section open=null #go-login-failure %}
#### Login failure

```go
import (
  "github.com/DataDog/dd-trace-go/v2/appsec"
)

func handler(w http.ResponseWriter, r *http.Request) {
  exists := /* whether the given user id exists or not */
  metadata := make(map[string]string) /* optional extra event metadata */
  metadata["usr.login"] = "user-email"

  // Replace `my-uid` by a unique identifier of the user (numeric, username, email...)
  appsec.TrackUserLoginFailureEvent(r.Context(), "my-uid", exists, metadata)
}
```

{% /collapsible-section %}

{% collapsible-section open=null #go-custom-business %}
#### Custom business logic

```go
import (
  "github.com/DataDog/dd-trace-go/v2/appsec"
)

func handler(w http.ResponseWriter, r *http.Request) {
  metadata := map[string]string{"usr.id": "my-uid"}

  // Leveraging custom business logic tracking to track user signups
  appsec.TrackCustomEvent(r.Context(), "users.signup", metadata)
}
```

{% /collapsible-section %}

{% /tab %}

{% tab title="Ruby" %}
Starting in dd-trace-rb v1.9.0, you can use the Ruby tracer's API to track user events. Version v2.19.0 of dd-trace-rb introduces new methods under the `Datadog::Kit::AppSec::Events::V2` namespace. Existing event tracking methods are retained for compatibility.

The following examples show how to track login events or custom events (using signup as an example).

{% collapsible-section open=null %}
#### Login success

```ruby
require 'datadog/kit/appsec/events/v2'

login = 'user@some.com'
user = 'some-user-id'    # any unique string identifier (i.e. id, username or email)
user = {                 # or user could be a Hash with an id and other fields
  id: 'some-user-id',    # id is mandatory
  email: 'user@some.com' # other fields are optional
}
metadata = { 'some.key': 'value' } # any arbitrary key-value pairs

Datadog::Kit::AppSec::Events::V2.track_user_login_success(login, user, metadata)
```

{% /collapsible-section %}

{% collapsible-section open=null #ruby-login-failure %}
#### Login failure

```ruby
require 'datadog/kit/appsec/events/v2'

login = 'user@some.com' # the string used by the user to log in
user_exists = true      # if the user login exists in database for example
metadata = { 'some.key': 'value' } # any arbitrary key-value pairs

Datadog::Kit::AppSec::Events::V2.track_user_login_failure(login, user_exists, metadata)
```

{% /collapsible-section %}

{% collapsible-section open=null #ruby-custom-business %}
#### Custom business logic

```ruby
require 'datadog/kit/appsec/events'

span = nil
trace = Datadog::Tracing.active_trace
metadata = { 'usr.id': 'some-user-id' }
event_name = 'users.signup'

Datadog::Kit::AppSec::Events.track(event_name, trace, span, metadata)
```

{% /collapsible-section %}

#### Migrating to the new login success and failure methods{% #migrating-to-the-new-login-success-and-failure-methods %}

The new methods in `Datadog::Kit::AppSec::Events::V2` introduce a more intuitive parameter order and clearer separation of concerns. Here are the key changes:

1. The login identifier (email, username) is the first parameter and is mandatory.
1. The user object/ID is optional in success events and has been removed from failure events.
1. Metadata has been simplified and no longer requires the `usr.login` field.
1. The trace and span parameters are no longer required and are automatically inferred.

**Note**: the legacy methods `track_login_success` and `track_login_failure` are deprecated in favor of the new methods `track_user_login_success` and `track_user_login_failure`, respectively.

In the following example, the commented code is no longer necessary.

{% collapsible-section open=null #ruby-v2-migration-login-success %}
#### Login success

```ruby
require 'datadog/kit/appsec/events/v2'

login = 'user@some.com' # new mandatory argument
user = {                # same as before, but now the Hash is optional
  id: 'some-user-id',   # providing a user ID will nonetheless help with post-compromised activity correlation
  email: 'user@some.com'
}
metadata = {
# 'usr.login': 'user@some.com', this is no longer necessary in metadata, but became the required first parameter
  'some.key': 'value'
}

# deprecated
# Datadog::Kit::AppSec::Events.track_login_success(trace, span, user: user, **metadata)

Datadog::Kit::AppSec::Events::V2.track_user_login_success(login, user, metadata)
```

{% /collapsible-section %}

{% collapsible-section open=null #ruby-v2-migration-login-failure %}
#### Login failure

```ruby
require 'datadog/kit/appsec/events/v2'

login = 'user@some.com' # new mandatory argument
user_exists = true      # if the user login exists in database for example
metadata = {
# 'usr.login': 'user@some.com', this is no longer necessary in metadata, but became the required first parameter
  'some.key': 'value'
}

# deprecated
# Datadog::Kit::AppSec::Events.track_login_failure(trace, span, user_exists: user_exists, user_id: login, **metadata)

Datadog::Kit::AppSec::Events::V2.track_user_login_failure(login, user_exists, metadata)
```

{% /collapsible-section %}

{% /tab %}

{% tab title="PHP" %}
Starting in dd-trace-php v0.84.0, you can use the PHP tracer's API to track user events. Version v1.11.0 of dd-trace-php introduces new methods under the `\datadog\appsec\v2\` namespace. Existing event tracking methods are retained for compatibility.

The following examples show how to track login events or custom events (using signup as an example).

{% collapsible-section open=null %}
#### Login success

```php
<?php
$user = [
    'id' => 'user-id', // id is mandatory. If no ID is available, any unique identifier works (username, email...)
    'email' => 'user@email.com' // other fields are optional
]; //User data can be provided as an array
$user = 'user-id'; //or user could be just an ID
$login = 'user@email.com';
$metadata = [ 'key' => 'value' ]; // you can add arbitrary fields to metadata

// Log a successful user authentication event
// user and metadata are optional
\datadog\appsec\v2\track_user_login_success($login, $user, $metadata);
?>
```

{% /collapsible-section %}

{% collapsible-section open=null #php-login-failure %}
#### Login failure

```php
<?php
$login = 'user-id'; // the string used by the user to log in
$userExists = true; // if the user login exists in database or not
$metadata = [ 'key' => 'value' ]; // you can add arbitrary fields to metadata

// Log a failed user authentication event
// userExists is optional and it defaults to false
// metadata is optional
\datadog\appsec\v2\track_user_login_failure($login, $userExists, $metadata);
?>
```

{% /collapsible-section %}

{% collapsible-section open=null #php-custom-business %}
#### Custom business logic

```php
<?php
$eventName = 'users.signup'; // custom event name
$metadata = ['usr.id' => $id]; // you can add arbitrary fields to metadata
\datadog\appsec\track_custom_event($eventName, $metadata);
?>
```

{% /collapsible-section %}

#### Migrating to the new login success and failure methods{% #migrating-to-the-new-login-success-and-failure-methods %}

The new methods in `\datadog\appsec\v2\` namespace introduce a more intuitive parameter order and clearer separation of concerns. Here are the key changes:

1. The login identifier (email, username) is the first parameter and is mandatory.
1. The user array/ID is optional in success events and has been removed from failure events.
1. Metadata has been simplified and no longer requires the `usr.login` field.

**Note**: the legacy methods `\datadog\appsec\track_user_login_success_event` and `\datadog\appsec\track_user_login_failure_event` are deprecated in favor of the new methods `\datadog\appsec\v2\track_user_login_success` and `\datadog\appsec\v2\track_user_login_failure`, respectively.

In the following example, the commented code is no longer necessary.

{% collapsible-section open=null %}
#### Login success

```php
<?php
// in a controller:
$user = [
    'id' => 'user-id', // id is mandatory. If no ID is available, any unique identifier works (username, email...)
    'email' => 'user@email.com' // other fields are optional
]; // same as before, but now the array is optional. Providing a user ID nonetheless helps with post-compromised activity correlation

$login = 'user@email.com'; // new mandatory argument

$metadata = [
//  'usr.login' => 'user@email.com', this is no longer necessary in metadata. Must be the first argument
  'key' => 'value'
];

// \datadog\appsec\track_user_login_success_event($user, $metadata) // deprecated
\datadog\appsec\v2\track_user_login_success($login, $user, $metadata);
?>
```

{% /collapsible-section %}

{% collapsible-section open=null #php-migration-login-failure %}
#### Login failure

```php
<?php

$userId = 'user-id'; // No longer mandatory, but helpful when available
$login = 'user@email.com'; // new mandatory argument
$userExists = true;
$metadata = [
//  'usr.login' => 'user@email.com', this is no longer necessary in metadata. Must be the first argument
  'usr.id' => 'user-id', // Helps with correlating login failures with the rest of the user activity
  'key' => 'value'
];

// \datadog\appsec\track_user_login_failure_event($userId, $exists, $metadata); // deprecated
\datadog\appsec\v2\track_user_login_failure($login, $userExists, $metadata);
```

{% /collapsible-section %}

{% /tab %}

{% tab title="Node.js" %}
Starting in dd-trace-js v3.13.1, you can use the Node.js tracer API to track user events. Version v5.48.0 of dd-trace-js introduces new methods under the `eventTrackingV2` namespace. Existing event tracking methods are retained for compatibility.

The following examples show how to track login events or custom events (using signup as an example).

{% collapsible-section open=null %}
#### Login success

```javascript
const tracer = require('dd-trace')

// in a controller:
const user = {
id: 'user-id', // id is mandatory. If no ID is available, any unique identifier works (username, email...)
  email: 'user@email.com' // other fields are optional
}
const user = 'user-id' // user could be just the ID
const login = 'user@email.com'
const metadata = { 'key': 'value' } // you can add arbitrary fields

// Log a successful user authentication event
// user and metadata are optional
tracer.appsec.eventTrackingV2.trackUserLoginSuccess(login, user, metadata)
```

{% /collapsible-section %}

{% collapsible-section open=null #nodejs-login-failure %}
#### Login failure

```javascript
const tracer = require('dd-trace')

// in a controller:
const login = 'user-id' // the string used by the user to log in
const userExists = true // if the user login exists in database for example
const metadata = { 'key': 'value' } // you can add arbitrary fields

// Log a failed user authentication event
// userExists is optional and it is defaulted to false
// metadata is optional
tracer.appsec.eventTrackingV2.trackUserLoginFailure(login, userExists, metadata)
```

{% /collapsible-section %}

{% collapsible-section open=null #nodejs-custom-business %}
#### Custom business logic

```javascript
const tracer = require('dd-trace')

// in a controller:
const eventName = 'users.signup'
const metadata = { 'usr.id': 'user-id' }

tracer.appsec.trackCustomEvent(eventName, metadata)
```

{% /collapsible-section %}

#### Migrating to the new login success and failure methods{% #migrating-to-the-new-login-success-and-failure-methods %}

The new methods in `eventTrackingV2` introduce a more intuitive parameter order and clearer separation of concerns. Here are the key changes:

1. The login identifier (email, username) is the first parameter and is mandatory.
1. The user object/ID is optional in success events and has been removed from failure events.
1. Metadata has been simplified and no longer requires the `usr.login` field.

**Note**: the legacy methods `trackUserLoginSuccessEvent` and `trackUserLoginFailureEvent` are deprecated in favor of the new methods `eventTrackingV2.trackUserLoginSuccess` and `eventTrackingV2.trackUserLoginFailure`, respectively.

In the following example, the commented code is no longer necessary.

{% collapsible-section open=null %}
#### Login success

```javascript
const tracer = require('dd-trace')

// in a controller:
const user = {
  id: 'user-id',
  email: 'user@email.com'
} // same as before, but now the object is optional. Providing a user ID will nonetheless help with post-compromised activity correlation

const login = 'user@email.com' // new mandatory argument

const metadata = {
//  'usr.login': 'user@email.com', this is no longer necessary in metadata. Must be the main argument
  'key': 'value'
}

// tracer.appsec.trackUserLoginSuccessEvent(user, metadata) // deprecated
tracer.appsec.eventTrackingV2.trackUserLoginSuccess(login, user, metadata)
```

{% /collapsible-section %}

{% collapsible-section open=null #nodejs-migration-login-failure %}
#### Login failure

```javascript
const tracer = require('dd-trace')

// in a controller with the deprecated method:
const userId = 'user-id' // No longer mandatory, but helpful when available
const login = 'user@email.com' // new mandatory argument
const userExists = true
const metadata = {
//  'usr.login': 'user@email.com', this is no longer necessary in metadata. Must be the first argument
  'usr.id': userId, // Helps with correlating login failures with the rest of the user activity
  'key': 'value'
}

// tracer.appsec.trackUserLoginFailureEvent(userId, userExists, metadata) // deprecated
tracer.appsec.eventTrackingV2.trackUserLoginFailure(login, userExists, metadata)
```

{% /collapsible-section %}

{% /tab %}

{% tab title="Python" %}
Starting in dd-trace-py v1.9.0, you can use the Python tracer's API to track user events.

Starting in dd-trace-py v3.7, you can use the new Python tracer's SDK to track users and user events.

The following examples show how to track login events, signup events, or custom events.

{% collapsible-section open=null #python-business-logic-sdk %}
#### User Tracking SDK

Available since dd-trace-py v3.7, `track_user_sdk` provides 5 functions:

- `track_login_success`
- `track_login_failure`
- `track_signup`
- `track_custom_event`
- `track_user`

Available since dd-trace-py v3.17, `track_user_sdk` provides this additional function:

- `tracker_user_id`

```python
from ddtrace.appsec import track_user_sdk

## This function should be called when a user successfully logs in to the
# application.

# user_id and metadata are optional
metadata = {"usr.email": "user@email.com"}
track_user_sdk.track_login_success(
    "some_user_login",
    user_id="some_user_id",
    metadata=metadata,
)


## This function should be called when a user fails to log in to the
# application.

# user_id and metadata are optional
metadata = {"usr.error": "login failure"}

# If you want to track the login failure as a "login do not exists"
exists = False
track_user_sdk.track_login_failure(
    "some_user_login",
    exists,
    metadata=metadata,
)

# If you want to track the login failure as a "login exists but
# authentification failed
exists = True
track_user_sdk.track_login_failure(
    "some_user_login",
    exists,
    user_id="some_user_id",
    metadata=metadata,
)


## This function should be called when a user successfully signs up for
# the application.

# user_id, success and metadata are optional, success is True by default.
metadata = {"usr.email": "user@email.com"}
track_user_sdk.track_signup(
    "some_user_login",
    user_id="some_user_id",
    success=True,
    metadata=metadata,
)


## This function should be called when a custom user event occurs in the
# application.

# metadata is required
metadata = {
    "usr.address": {"line1": "221b Baker Street", "city": "London"},
    "phone": "0123456789",
}
track_user_sdk.track_custom_event("my_event_name", metadata)
```

{% /collapsible-section %}

{% collapsible-section open=null #python-business-logic-example %}
#### FastAPI Toy App with SDK

The following example is a fully functioning Toy application that uses the User Tracking SDK with a memory-based user database. This example illustrates the possible usage of the SDK but does not provide the necessary requirements of a real application, such as a persistent data model or a secure authentication system.

```python
from uuid import uuid4

import ddtrace.auto  # noqa: F401
from ddtrace.appsec.track_user_sdk import (
    track_custom_event,
    track_login_failure,
    track_login_success,
    track_signup,
    track_user,
)
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware


class User(BaseModel):
    user_id: str
    username: str
    password: str


users: dict[str, User] = {}

app = FastAPI()


@app.middleware("http")
async def track_user_middleware(request: Request, call_next):
    user = request.session.get("username")
    session_id = request.session.get("session_id")
    if user and session_id and user in users:
        track_user(user, users[user].user_id, session_id=session_id)
    return await call_next(request)


session_secret = "just-a-test"
app.add_middleware(SessionMiddleware, secret_key=session_secret)


@app.post("/signup")
async def signup(username: str, password: str):
    if username in users:
        return JSONResponse(
            {"error": "User already exists"},
            status_code=400,
        )

    user_id = str(uuid4())
    users[username] = User(
        user_id=user_id,
        username=username,
        password=password,
    )

    track_signup(username, user_id, success=True)
    return {"message": "User created successfully"}


@app.post("/login")
async def login(username: str, password: str, request: Request):
    if username not in users:
        track_login_failure(username, False)
        return JSONResponse(
            {"error": "Invalid user password combination"},
            status_code=403,
        )

    if users[username].password != password:
        track_login_failure(username, True, users[username].user_id)
        return JSONResponse(
            {"error": "Invalid user password combination"},
            status_code=403,
        )

    track_login_success(username, users[username].user_id)
    request.session["username"] = username
    request.session["session_id"] = str(uuid4())

    return {"message": "Login successful"}


@app.get("/whoami")
async def whoami(request: Request) -> User:
    if (
        "username" not in request.session
        or request.session["username"] not in users
    ):
        raise HTTPException(status_code=403, detail="User not logged in")

    track_custom_event(
        "user_has_forgotten_who_they_are",
        metadata={
            "username": request.session["username"],
            "session_id": request.session["session_id"],
        },
    )
    return users[request.session["username"]]
```

{% /collapsible-section %}

{% collapsible-section open=null #python-business-logic-legacy %}
#### Legacy API

The preferred method is to use the new User Tracking SDK (available since dd-trace-py v1.9) instead of the Legacy API.

```python
from ddtrace.appsec.trace_utils import track_user_login_success_event
from ddtrace.appsec.trace_utils import track_user_login_failure_event
from ddtrace.appsec.trace_utils import track_custom_event
from ddtrace import tracer
metadata = {"usr.login": "user@email.com"}
# name, email, scope, role, session_id and propagate are optional arguments which
# default to None except propagate that defaults to True. They'll be
# passed to the set_user() function
track_user_login_success_event(tracer, "userid", metadata)


# exists indicates if the failed login user exists in the system
exists = False
# if no numeric userId is available, any unique identifier will do (username, email...)
track_user_login_failure_event(tracer, "userid", exists, metadata)


metadata = {"usr.id": "userid"}
event_name = "users.signup"
track_custom_event(tracer, event_name, metadata)
```

{% /collapsible-section %}

{% /tab %}

### Tracking business logic information without modifying the code{% #tracking-business-logic-information-without-modifying-the-code %}

If your service has AAP enabled and [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) enabled, you can create a custom WAF rule to flag any request it matches with a custom business logic tag. This doesn't require any modification to your application, and can be done entirely from Datadog.

To get started, navigate to the [Custom WAF Rule page](https://app.datadoghq.com/security/appsec/in-app-waf?config_by=custom-rules) and click on "Create New Rule".

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/custom-waf-rule-menu.d88a25f94d8944130ca93cd784ab8ba0.png?auto=format"
   alt="Access the Custom WAF Rule Menu from the AAP homepage by clicking on Protection, then In-App WAF and Custom Rules" /%}

This will open a menu in which you may define your custom WAF rule. By selecting the "Business Logic" category, you will be able to configure an event type (for instance, `users.password_reset`). You can then select the service you want to track, and a specific endpoint. You may also use the rule condition to target a specific parameter to identify the codeflow you want to *instrument*. When the condition matches, the library tags the trace and flags it to be forwarded to AAP. If you don't need the condition, you may set a broad condition to match everything.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/custom-waf-rule-form.a7b2e37e44d0e67d90458da4c8544875.png?auto=format"
   alt="Screenshot of the form that appear when you click on the Create New Rule button" /%}

Once saved, the rule is deployed to instances of the service that have Remote Configuration enabled.

## Automatic user activity event tracking{% #automatic-user-activity-event-tracking %}

When AAP is enabled, Datadog Tracing Libraries attempt to detect user activity events automatically.

The events that can be automatically detected are:

- `users.login.success`
- `users.login.failure`
- `users.signup`

### Automatic user activity event tracking modes{% #automatic-user-activity-event-tracking-modes %}

Automatic user activity tracking offers the following modes:

- `identification` mode (short name: `ident`):
  - This mode is the default and always collects the user ID or best effort.
  - The user ID is collected on login success and login failure. With failure, the user ID is collected regardless of whether the user exists or not.
  - When the instrumented framework doesn't clearly provide a user ID, but rather a structured user object, the user ID is determined on a best effort basis based on the object field names. This list of field names are considered, ordered by priority:
    - `id`
    - `email`
    - `username`
    - `login`
    - `user`
  - If no user ID is available or found, the user event is not emitted.
- `anonymization` mode (short name: `anon`):
  - This mode is the same as `identification`, but anonymizes the user ID by hashing (SHA256) it and cropping the resulting hash.
- `disabled` mode:
  - AAP libraries do *not* collect any user ID from their automated instrumentations.
  - User login events are not emitted.

{% alert level="info" %}
All modes only affect automated instrumentation. The modes don't apply to manual collection. Manual collection is configured using an SDK, and those settings are not overridden by automated instrumentation.
{% /alert %}

### Manual configuration{% #manual-configuration %}

Datadog libraries allow you to configure auto-instrumentation by using the `DD_APPSEC_AUTO_USER_INSTRUMENTATION_MODE` environment variable with the short name for the mode: `ident`|`anon`|`disabled`.

The default mode is `identification` mode (short name: `ident`).

For example, `DD_APPSEC_AUTO_USER_INSTRUMENTATION_MODE=anon`.

### Deprecated modes{% #deprecated-modes %}

{% alert level="info" %}
Previous modes are deprecated, but compatibility will be maintained until the next major release.
{% /alert %}

The following modes are deprecated:

- `safe` mode: The trace library does not include any PII information on the events metadata. The tracer library tries to collect the user ID, and only if the user ID is a valid [GUID](https://docs.datadoghq.com/security/default_rules/bl-payment-failures/)
- `extended` mode: The trace library tries to collect the user ID, and the user email. In this mode, Datadog does not check the type for the user ID to be a GUID. The trace library reports whatever value can be extracted from the event.

**Note**: There could be cases in which the trace library won't be able to extract any information from the user event. The event would be reported with empty metadata. In those cases, use the SDK to manually instrument the user events.

## Disabling user activity event tracking{% #disabling-user-activity-event-tracking %}

To disable automated user activity detection through your [AAP Software Catalog](https://app.datadoghq.com/security/appsec/inventory/services?tab=capabilities), change the automatic tracking mode environment variable `DD_APPSEC_AUTO_USER_INSTRUMENTATION_MODE` to `disabled` on the service you want to deactivate. All modes only affect automated instrumentation and require [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) to be enabled.

For manual configuration, you can set the environment variable `DD_APPSEC_AUTOMATED_USER_EVENTS_TRACKING_ENABLED` to `false` on your service and restart it. This must be set on the application hosting the Datadog Tracing Library, and not on the Datadog Agent.
