# Source: https://docs.zapier.com/platform/publish/integration-checks-reference.md

# Integration check reference

> Before you can submit your integration for publishing, it runs through a set of automated checks to ensure it's working properly and giving our users (and yours) the best possible experience.

To [publish your integration](/platform/publish/public-integration), all Errors and Publishing Tasks must be validated. Warnings are non-blocking and not strictly required to proceed as they would not prevent you from promoting a version, though we do recommend you review them for usability of your integration.

If your integration will remain private, it isn't *necessary* to pass the validation checks. You will be able to [share it with users](/platform/manage/sharing) as is. However, you can still select `Run Validation` from the *Version Overview* tab in the Platform UI or run the `zapier-platform validate` command (or deprecated `zapier validate`) [in the Platform CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#validate) to be notified of any issues and recommendations to better the user experience.

To help better address a check in communication, each check is given a unique ID, consisting of a capital letter and three digits, such as `D001`.

You don't need to know the implication of the initial capitial letter. But if you're curious, they are:

| Area                      | Description                                                                                                                                                                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connected **A**ccounts    | Connected accounts that are linked to your integration. We verify these to ensure the authentication is working.                                                                                                                                         |
| **C**ompatibility         | Only apply when your integration is public, these checks verify how the new version is backward compatible with the currently public version. They ask questions like “would this change break existing Zaps, Zap Templates, or connected accounts?”     |
| **D**efinition            | Definition of the integration, including auth and trigger/search/action configurations. Some of these checks could block you from saving/pushing if the violation results in a broken trigger/search/action.                                             |
| **E**nvironment Variables | Integration environment variables may impact the runtime behavior of your integration versions. These checks may prompt you for confirmation before performing actions like migrating or promoting.                                                      |
| **L**ifecycle             | The lifecycle state of your integration or its versions, such as the visibility (private, pending, or public) and the version state (deprecated, non-production, or production).                                                                         |
| **M**arketing             | Public-facing information, such as the app title, description, and logo. The intent of these rules is to give Zapier users a consistent style among texts and images across all public integrations. They're more likely to block you from going public. |
| **S**tats                 | Usage stats, such as the number of users your integration has. These are more likely to block you from going public.                                                                                                                                     |
| **T** - Zap History       | Data from runs in your Zap History, produced by live (enabled) Zaps. These are more likely to block you from going public. The “T” checks are named as such for historical reasons. Zapier now shows tasks in the Zap History.                           |
| **U**ser                  | Things in the developer's (your) account, such as Terms of Service acceptance.                                                                                                                                                                           |
| **Z**ap                   | Things related to Zaps, such as the trigger samples you pulled into the Zap editor.                                                                                                                                                                      |

When the checks are run, we'll give a brief blurb summarizing the violation (with a check ID) along with a link to this page. This will act as a full reference explaining each error and giving examples for each.

{/* See platform/README.md for instructions. */}

***

## <span id="A001">A001 - A Connected Account Exists</span>

To ensure you've tested auth, we require you to set up at least one connected
account.

***

## <span id="C001">C001 - Try To Avoid Hiding/Removing Public Triggers/Searches/Creates</span>

During promotion, we compare features of your currently public version with your soon-to-be-public version.

When you hide/remove a trigger in a new version, Zap Templates that use that trigger become invalid. Try to avoid this when you can. The same applies for searches and creates.

***

## <span id="C002">C002 - Try To Avoid Removing Input Fields</span>

During promotion, we compare features of your currently public version with your soon-to-be-public version.

When you change/remove the `key` property of an `input_field`, Zap Templates that use that field become invalid. Try to avoid this when you can.

***

## <span id="C003">C003 - Try To Avoid Removing Sample Data</span>

During promotion, we compare features of your currently public version with your soon-to-be-public version.

When you change/remove the `key` property of an item in your `sample`, Zap Templates that use that field become invalid. Try to avoid this when you can.

***

## <span id="D001">D001 - Input Fields Should Be Insensitive</span>

Input fields collect user-provided values. They must not contain sensitive
credentials such as API keys, tokens, secrets, or passwords.

Sensitive values should be centrally used in auth because input fields
typically aren't treated with the same level of security as auth fields are
(e.g. scrubbed from logs) and aren't action specific. Additionally, the
ability to test the validity of auth doesn't exist for action fields, so
anything auth related should be put into an auth field instead.

<Icon icon="xmark" /> examples of **incorrect** input field keys:

```
"api_key"
"api_token"
"user_password"
```

<Icon icon="check" /> examples of **correct** input field keys:

```
"project_id"
"tag_name"
"user_email_address"
```

***

## <span id="D002">D002 - Provide Link in Help Text for Auth Fields</span>

It's often not obvious where a user can find their API credentials for a service. If
you use a pasted API key as an authentication method, it's strongly encouraged that
you link the user to the page (or relevant help doc) that has their key.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```
API key is found on the "API Details" page in settings
```

<Icon icon="check" /> an example of a **correct** implementation:

```
Go to the [API Details](https://my.site.com/manage/api-details) screen from your
Website Dashboard to find your API Key.
```

***

## <span id="D003">D003 - Connection Label Should Be Valid</span>

A Connection Label helps a customer remember which account they connected.
It should be short and easily identifiable, and must not contain sensitive
credentials such as API keys, tokens, secrets, or passwords.

For both [Platform UI](https://platform.zapier.com/build/connection-label)
and [CLI](https://platform.zapier.com/reference/cli-docs#connection-label),
the connection label is a string. You can use any data returned by your test
function, but you should never use sensitive fields.

For instance, if a successful run of the auth test returns the following data:

```js  theme={null}
{
  "name": "Malcom Reynolds",
  "email": "youcanttaketheskyfromme@serenity.com",
  "job": "Captain"
}
```

Your connection label could be the following:

```
{{name}} - {{email}}
```

The most important role of the label is to uniquely identify the connection.

<Icon icon="xmark" /> examples of **incorrect** connection labels:

```
"Slack"
"api_key"
"My token is: 12345"
"{{token}}"
"{{api_key}}"
"{{password}}"
"user token"
```

<Icon icon="check" /> examples of **correct** connection labels:

```
{{user}} @ {{team}}
{{name}} - {{email}}
{{username}}
{{user}} ({{email}})
```

***

## <span id="D004">D004 - ID Fields Should Have Dynamic Dropdowns</span>

We've found that instead of instructing users to paste an item `id` into Zapier,
providing them with a [dynamic dropdown](https://platform.zapier.com/reference/cli-docs#dynamic-dropdowns)
greatly increases the likelihood of the user setting up Zaps correctly. Users will
still be able to map custom fields, but this gets them started on the right foot.

Read more about implementing dynamic dropdowns below:

* [Platform UI](https://platform.zapier.com/build/add-fields#dynamic-dropdown)
* [Platform CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#dynamic-dropdowns)

***

## <span id="D005">D005 - Dynamic Dropdown Connects to a Non-Existing Trigger</span>

[Dynamic dropdowns](https://platform.zapier.com/reference/cli-docs#dynamic-dropdowns)
allow you to connect an input field to an existing trigger. The dropdown won't work
if the trigger key you specify doesn't exist.

***

## <span id="D006">D006 - REST Hook Trigger Needs a Polling URL</span>

When users are setting up a hook-based (aka instant) Trigger, it's important to have
a polling fallback. For example, imagine a Zap that triggers on a new Slack message.
If testing relies on the sending of a webhook, the test won't complete without the user
sending an actual message in a Slack channel, which is disruptive.

Instead, during testing, the Perform List (`performList`) operation fetches a
(real) recent message using the provided URL for polling and uses it as the test result.
The polling URL in a REST Hook trigger is only used for testing during a Zap setup.

It's very important that the structure of an object from a webhook and from a poll
are identical. Typically, this means modifying a poll result so that it looks like a
hook. If a poll has fields that a hook doesn't, the user may map them to a later
step, and when the Zap runs live, the value will be blank. This can cause errors
or unexpected results for users.

Let's walk through an example. Say we have a `New Contact` REST Hook trigger. When a
new contact is created, Zapier gets a webhook that looks like this:

```js  theme={null}
{
  "id": 1,
  "firstName": "Bruce",
  "lastName": "Wayne",
  "job": "Batman"
}
```

The accompanying polling URL would look something like `https://site.com/contacts/list`
and return:

```js  theme={null}
{
  "results": [
    {
      "id": 1,
      "firstName": "Bruce",
      "lastName": "Wayne",
      "job": "Batman",
      "friends": [2, 3, 4]
    },
    {
      "id": 2,
      "firstName": "Alfred",
      "lastName": "Pennyworth",
      "job": "Butler",
      "friends": [1, 3]
    }
  ]
}
```

To match the polling result to the hook result, you would modify this response to
remove the `friends` information, and return only the array of contacts, not the
enclosing object.

The polling result is not used when a user skips testing the Zap step. In that case,
Zapier uses the sample data.

See [Sample Data](/platform/build/sample-data) for more details on
this.

***

## <span id="D007">D007 - All URLs Should Be HTTPS</span>

When handling customer data (which all Zapier functions do), it's strongly
encouraged that all communication take place securely. Using SSL is a big part of
that, so ensure your URLs have HTTPS as their protocol.

If you need help setting up an SSL certificate for your API, we suggest
[Let's Encrypt](https://letsencrypt.org/).

<Icon icon="xmark" /> an example of an **incorrect** setup:

```text  theme={null}
http://example.com/messages/subscribe
```

<Icon icon="check" /> an example of a **correct** implementation:

```text  theme={null}
https://example.com/messages/subscribe
```

***

## <span id="D008">D008 - Invalid Markdown Link</span>

A valid markdown link consists of a pair of square brackets with the link text
paired with a pair of parentheses that have the link itself. See the
[markdown cheatsheet](https://www.markdownguide.org/basic-syntax/#links) for
more info.

If you want to show a full link without actually linking to it, use backticks. This
makes it clear to the user that they don't need to click the link, it's just used as
an example. Any link used in plain text needs to either be a proper link or in
backticks.

<Icon icon="xmark" /> examples of an **incorrect** implementation:

```
See [Google(https://google.com)
```

```
See https://google.com
```

<Icon icon="check" /> examples of a **correct** implementation:

```
See [Google](https://google.com)
```

```
See `https://google.com`
```

If you see this error, you should look through both the description for the
trigger/action/search and the help text for any fields that might have bad links.

***

## <span id="D009">D009 - Requires at Least One Search Field</span>

When making a search step, it's important to have a field to search by. Common
examples for searching for a user are by name, email, and username.

***

## <span id="D010">D010 - Missing Primary Key Fields in Static Sample Data</span>

For polling triggers, the deduper uses the primary key field(s) to decide if it's
seen an object before. You can define one or more output fields as the primary key.
Each field can be a string or a number. But it's important that the primary key is
unique. If no fields are set as `primary`, the deduper will by default use the `id`
field as the primary key.

Hooks are not deduped, so they're not required to have a primary key.

This check ensures the static samples in your integration definition contain the
primary key fields. It's similar to `T002`. The difference is that `T002` validates
the live polling results in the Zap History.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```js  theme={null}
{
  // The deduper uses `id` field by default if no output fields are `primary`.
  // So this sample should have an `id` field for it to pass.
  "sample": {
    "contact_id": 4,
    "contact_name": "David"
  }
}
```

```js  theme={null}
{
  // `contact_id` is set as `primary`, but it's missing in the sample
  "sample": {
    "id": 4,
    "contact_name": "David"
  },
  "outputFields": [
    { "key": "contact_id", "primary": true },
    { "key": "contact_name" }
  ]
}
```

<Icon icon="check" /> examples of a **correct** implementation:

```js  theme={null}
{
  "sample": {
    "id": 4,
    "contact_name": "David"
  }
}
```

```js  theme={null}
{
  // This example defines `contact_id` as the unique primary key.
  "sample": {
    "contact_id": 4,
    "contact_name": "David"
  },
  "outputFields": [
    { "key": "contact_id", "primary": true },
    { "key": "contact_name" }
  ]
}
```

```js  theme={null}
{
  // If multiple fields are unique together, you can set them as `primary`.
  "sample": {
    "repo": "zapier/zapier-platform",
    "number": 1234,
    "title": "Add this feature please"
  },
  "outputFields": [
    { "key": "repo", "primary": true },
    { "key": "number", "primary": true },
    { "key": "title" }
  ]
}
```

***

## <span id="D011">D011 - Redundant Help Text</span>

Help text is optional and meant to provide non-obvious information or links for the
user. If the label and help text are the same, they are considered redundant.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```js  theme={null}
{
  "label": "Subdomain",
  "help_text": "subdomain"
}
```

<Icon icon="check" /> an example of a **correct** implementation:

```js  theme={null}
{
  "label": "Subdomain",
  "help_text": "Where you (and your users) can access your forms, e.g., https://<SUBDOMAIN>.typeform.com"
}
```

***

## <span id="D012">D012 - Static Sample Is Required</span>

When a user sets up a trigger or action (create or search), they need sample data to
be returned in order to have fields available to map in the subsequent steps. If
testing the trigger returns no live results, we use static sample data as a
fallback.

It's very important that the data structure of the response from the actual
trigger/action request and in the sample data are identical. Otherwise, users could
map fields that don't exist in the live results, which results in a broken Zap.

See [Sample Data](https://platform.zapier.com/build/sample-data) for more details on this.

***

## <span id="D013">D013 - Connects to a Non-Existing Search</span>

[Search-Powered Fields](https://platform.zapier.com/reference/cli-docs#search-powered-fields)
prompt users to set up a search step to populate the value of the field. It won't
work if the search key you specify doesn't exist.

***

## <span id="D014">D014 - Search Connector can't be combined with certain other features.</span>

The type must be string, number, or integer.
The list, dict and children properties cannot be used.

<Icon icon="xmark" /> an example of an **incorrect** setup:

```js  theme={null}
{
  "key": "update_thing",
  "list": true,
  "search": "thing.id"
}
```

<Icon icon="check" /> an example of a **correct** implementation:

```js  theme={null}
{
  "key": "update_thing",
  "search": "thing.id",
  "dynamic": "things.id.name"
}
```

***

## <span id="D015">D015 - Search-Or-Create Connects to a Non-Existing Action/Search</span>

The search or create key you specify in `searchOrCreates` must reference to an
existing search or action. Otherwise, it won't work.

***

## <span id="D016">D016 - Consists Only a Static Webhook</span>

A REST Hook trigger missing a Subscribe or Unsubscribe endpoint, is presented to
users as a [Static Webhook](https://cdn.zappy.app/3b35908a6a0c232087b5da807cf9d6fb.png).
Static hooks are [not supported in public integrations](https://platform.zapier.com/publish/integration-checks-reference#D017),
but they could be used if the integration intends to remain private. However, Zapier
doesn't allow integrations that are a single static hook with the availability of
[Webhooks by Zapier](https://zapier.com/apps/webhook/integrations). To fix this, add
more triggers/searches/actions.

***

## <span id="D017">D017 - Static Hook Is Discouraged</span>

When a REST Hook trigger is missing a Subscribe or Unsubscribe endpoint, it is
presented to users as a [Static Webhook](https://cdn.zappy.app/3b35908a6a0c232087b5da807cf9d6fb.png).
As static webhooks require manual intervention by the user to set up correctly, we
no longer support adding new static webhook triggers to a public integration. Please
set up Subscribe and Unsubscribe requests for this trigger, or use a Polling trigger
type instead.

***

## <span id="D018">D018 - Titlecased Label</span>

In order to have a consistent style across trigger/action/search labels, they're
required to be presented in title case. If you fail this check, a passing version of
your label will be shown.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```
new contact
```

<Icon icon="check" /> an example of a **correct** implementation:

```
New Contact
```

***

## <span id="D021">D021 - Trigger Description Requirements</span>

Trigger descriptions must start with `Triggers when ` and end with a `.`.

<Icon icon="xmark" /> examples of an **incorrect** implementation:

```
Whenever there's a new contact, this goes?
```

```
Triggers whenever there's a new contact.
```

<Icon icon="check" /> examples of a **correct** implementation:

```
Triggers when there's a new contact.
```

***

## <span id="D022">D022 - Creates Should Try to Have Static Input Fields</span>

When making Zap Templates, it's helpful to have input fields that are common
for all users. Without any, it's hard to create templates. If possible,
add some static input fields that all users will be able to use.

***

## <span id="D023">D023 - ISO-8601 Date/Time Format in Static Sample</span>

To ensure Zapier can correctly parse dates and times, you should always use ISO-8601
format to represent dates or times. Timezone info should also be present if it
contains time.

This check is similiar to `T003`. This check validates the static samples in
your integration definition, while `T003` validates the live results
in the Zap History.

<Icon icon="xmark" /> examples of an **incorrect** implementation:

```
01 Aug 2023
```

```
01 Aug 2023 06:50:30
```

```
2023-08-01T06:50:30
```

<Icon icon="check" /> examples of a **correct** implementation:

```
2023-08-01
```

```
2023-08-01T06:50:30-0500
```

```
2023-09-15T09:59:59Z
```

***

## <span id="D024">D024 - Static Sample Respects Output Field Definition</span>

If you define output fields for a trigger/action/search, they should be consistent
with the static sample data. The specific checks are:

* "required" fields must be in the sample
* field values in the sample match their field type

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```
static sample: {"id": "1"}
output fields: [
    {"key":  "id", "type": "integer"},
    {"key": "email", "type": "string", "required": true}
]
```

<Icon icon="check" /> an example of a **correct** implementation:

```
static sample: {"id": 1, "email": "john@example.com"}
output fields: [
    {"key":  "id", "type": "integer"},
    {"key": "email", "type": "string", "required": true}
]
```

***

## <span id="D025">D025 - URLs Should Not Be Dangerous URIs</span>

In order to help prevent reflective cross-site-scripting (XSS) attacks on Zapier
customers, we require that URLs inside the app definition do not match potentially
dangerous URI patterns which could be used to run malicious code.

Read more about XSS in the [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).

<Icon icon="xmark" /> an example of an **incorrect** setup:

```text  theme={null}
javascript:alert('XSS');//
```

<Icon icon="check" /> an example of a **correct** implementation:

```text  theme={null}
https://example.com
```

***

## <span id="D026">D026 - Manual domain validation recommended if using "inputFormat" or domain-related authentication fields</span>

When utilizing authentication fields which allow a user to input their own domain or subdomain,
we strongly recommend performing [manual validation](https://platform.zapier.com/build/subdomain-validation)
on the input data to ensure that it matches your expectations and filters out values which
could be used to redirect users into unexpected domains.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```javascript  theme={null}
// No subdomain validation, trusting the user input
const response = await z.request({
  url: `https://${bundle.authData.yourSubdomainField}.mydomain.com/oauth/token`,
  // ...
});
```

<Icon icon="check" /> an example of a **correct** implementation:

```javascript  theme={null}
// Manual validation step to ensure the subdomain matches your requirements
if (!/^[a-z0-9-]+$/.test(bundle.authData.yourSubdomainField)) {
  throw new Error(
    "Subdomain can only contain letters, numbers and dashes (-).",
  );
}

const response = await z.request({
  url: `https://${bundle.authData.yourSubdomainField}.mydomain.com/oauth/token`,
  // ...
});
```

***

## <span id="D027">D027 - Not Using Latest Platform Version</span>

The integration is not using the latest platform core version. Consider upgrading to the
latest version to get the newest features, bug fixes, and security updates.

To upgrade, update the `zapier-platform-core` dependency in package.json
to the latest version and run `zapier-platform test` (or deprecated `zapier test`) if needed.

***

## <span id="D028">D028 - Clean Input Data Enabled</span>

The integration has `cleanInputData` set to true, which causes the platform to
automatically remove empty values `(null, '', [], {})` from `bundle.inputData`.
Consider setting `cleanInputData` to false to stop this automatic cleaning
for more predictable behavior, especially for line-item actions that
depend on array positions.

This can be set globally in the app flags or per-action in the operation definition:

```javascript  theme={null}
const App = {
  flags: {
    cleanInputData: false, // global flag
  },
  triggers: {
    recipe: {
      operation: {
        cleanInputData: true, // only enable for this trigger
      },
    },
  },
};
```

***

## <span id="E001">E001 - Environment Variables have changed between versions</span>

During promotion or migration, be sure to confirm that any environment variable
changes are intentional and won't cause runtime problems. Remember that changes to
environment variables in one version of an integration will not affect the environment
variables of other versions of the same integration.

***

## <span id="L001">L001 - Version Is Deprecated</span>

You can't promote a deprecated version.

***

## <span id="L002">L002 - Version Was Already Submitted</span>

You can't submit a version you've already submitted. If your integration was pushed
back and you want to resubmit for another review, you should make changes on a
**new** version and submit that.

***

## <span id="L003">L003 - Version Is Already Production</span>

This could happen if you're attempting to promote a version that is already in
production.

***

## <span id="L004">L004 - Changes From Partners Are Blocked</span>

This is necessary when Zapier team pushes changes to a partner-owned integration.
Partners would have to coordinate with Zapier team via [partners@zapier.com](mailto:partners@zapier.com)
to lift the restriction for subsequent changes from them.

***

## <span id="M001">M001 - App Category Is Required</span>

To correctly categorize your integration on Zapier, please choose the category that
fits best your app. You can specify a category for your integration in the
Integration Settings page.

***

## <span id="M002">M002 - Description Is Invalid</span>

Your app's description is a place to talk about your app, not ours! Even if we
really like your app, you're not allowed to say "Zapier" in your app's
description. We expect to see your app's name in the description followed by
"is a" to begin the description.

Additionally, it's discouraged that you talk about how this integration will "sync"
anything, as the space is supposed to be about your app itself instead of the Zapier
integration in particular.

Lastly, this section should be short and sweet. A brief description (roughly
tweet-sized) is best. Specifically, we're looking for 1 - 3 sentences or at least
40 characters and a maximum of 140 characters.

<Icon icon="xmark" /> an example of an **incorrect** setup:

```
Google Translate enables Zapier users to translate text from one language into
another.
```

<Icon icon="check" /> an example of a **correct** implementation:

```
Google Translate is a service that translates text from one language into another.
```

***

## <span id="M003">M003 - Role Must Be Employee or Contractor</span>

For your integration to go public, you must be employed or hired by the company who
makes the app used in the integration. Go to the Integration Settings page
to select your role.

***

## <span id="M004">M004 - Invalid Logo</span>

Your app's logo will be used all over the site in square containers and in various
sizes. To ensure it looks good at all sizes, the logo image must be:

* a square PNG image
* at least 256px by 256px in size
* in RGBA mode so it can have a transparent background

To resize an image or convert an image to PNG, you can use this
[tool](http://www.picresize.com/).

***

## <span id="M005">M005 - Admin Team Member Email Domain Matches App Domain</span>

To ensure that this integration is being submitted by the app owner we require that
one of the Admin team members listed on the project have an email address with the
same domain as your app's homepage URL (which must also be present). You can add the
homepage URL at `https://developer.zapier.com/app/APP_ID/version/APP_VERSION/settings`.
Collaborator team members with the same domain as the homepage do not meet this
requirement.

***

## <span id="M006">M006 - Homepage URL Must Be Present</span>

Each app must have a homepage URL. You can add the homepage
URL at `https://developer.zapier.com/app/APP_ID/version/APP_VERSION/settings`.

***

## <span id="M007">M007 - Public Integration Already Exists</span>

We only allow one public integration in our app directory for a given app. If a
public integration with the same title already exists, we won't approve your
submission to go public. If you're the owner of the existing public integration,
create an updated version with any edits and promote that instead of submitting a
new integration.

***

## <span id="S001">S001 - 3 Users with a live Zap</span>

To verify user demand, there should be at least 3 users who have a live Zap using
this integration. "Live" means the Zaps are switched on with at least one successful
[Zap run in recent history](https://help.zapier.com/hc/en-us/articles/8496291148685).

You can [invite others to test your integration](https://platform.zapier.com/manage/sharing)
before publication.

***

## <span id="S002">S002 - One Live Zap for Each Trigger/Search/Action</span>

To ensure any show-stopping bugs are worked out, every visible trigger/search/action
of your integration should have a live Zap that demonstrates it works. "Live" means
the Zaps are switched on with at least one successful
[Zap run in recent history](https://help.zapier.com/hc/en-us/articles/8496291148685).

You can create a [new Zapier account](https://help.zapier.com/hc/en-us/articles/8496197192461)
and [invite it to your integration](https://platform.zapier.com/manage/sharing) if
you need extra Zaps.

You can also [contact us](https://developer.zapier.com/contact) if you need a trial
extension.

***

## <span id="S003">S003 - Live Version Count Limit</span>

You can't have more than 100 previous or current production versions with live Zaps.
To continue, migrate users on older versions to a newer version.

***

## <span id="T001">T001 - One Successful Zap Run for Each Trigger/Search/Action</span>

There must be at least one successful Zap run for each visible trigger/action/search
in your app.

To ensure you have run a live test of every visible trigger/action/search, create a
Zap for each one, turn it on, and trigger a Zap run while it's on.

This check is performed using the [Zap History](https://zapier.com/app/history) for
accounts belonging to the integration admins, so build your test Zaps in these
accounts.

Learn more about the Zap History [here](https://help.zapier.com/hc/en-us/articles/8496291148685).

***

## <span id="T002">T002 - Missing Primary Key Fields in Live Polling Results</span>

For polling triggers, the deduper uses the primary key field(s) to decide if it's
seen an object before. You can define one or more output fields as the primary key.
Each field can be a string or a number. But it's important that the primary key is
unique. If no fields are set as `primary`, the deduper will by default use the `id`
field as the primary key.

Hooks are not deduped, so they're not required to have a primary key.

This check ensures the live polling results in the [Zap History](https://zapier.com/app/history)
contain the primary key fields. It's similar to `D010`. The difference is that
`D010` validates the static samples in your integration definition.

This check is performed using the [Zap History](https://zapier.com/app/history) for
accounts belonging to the integration admins, so build your test Zaps in these
accounts.

<Icon icon="xmark" /> examples of an **incorrect** implementation:

```js  theme={null}
{
  // The deduper uses `id` field by default if no output fields are `primary`.
  // So this sample should have an `id` field for it to pass.
  // Note that `<live_polling_result>` represents a polling result in Zap History,
  // not an actual key in your integration definition.
  "<live_polling_result>": {
    "contact_id": 4,
    "contact_name": "David"
  }
}
```

```js  theme={null}
{
  // `contact_id` is set as `primary`, but it's missing in the result
  "<live_polling_result>": {
    "id": 4,
    "contact_name": "David"
  },
  "outputFields": [
    { "key": "contact_id", "primary": true },
    { "key": "contact_name" }
  ]
}
```

<Icon icon="check" /> examples of a **correct** implementation:

```js  theme={null}
{
  "<live_result_result>": {
    "id": 4,
    "contact_name": "David"
  }
}
```

```js  theme={null}
{
  // This example defines `contact_id` as the unique primary key.
  "<live_polling_result>": {
    "contact_id": 4,
    "contact_name": "David"
  },
  "outputFields": [
    { "key": "contact_id", "primary": true },
    { "key": "contact_name" }
  ]
}
```

```js  theme={null}
{
  // If multiple fields are unique together, you can set them as `primary`.
  "<live_polling_result>": {
    "repo": "zapier/zapier-platform",
    "number": 1234,
    "title": "Add this feature please"
  },
  "outputFields": [
    { "key": "repo", "primary": true },
    { "key": "number", "primary": true },
    { "key": "title" }
  ]
}
```

***

## <span id="T003">T003 - ISO-8601 Date/Time Format in Zap History</span>

To ensure Zapier can correctly parse dates and times, you should always use ISO-8601
format to represent dates or times. Timezone info should also be present if it
contains time.

This check is similiar to `D023`. This check validates the data in the
[Zap History](https://zapier.com/app/history), while `D023` validates
the static samples in your integration definition.

This check is performed using the [Zap History](https://zapier.com/app/history) for
accounts belonging to the integration admins, so build your test Zaps in these
accounts.

<Icon icon="xmark" /> examples of an **incorrect** implementation:

```
01 Aug 2023
```

```
01 Aug 2023 06:50:30
```

```
2023-08-01T06:50:30
```

<Icon icon="check" /> examples of a **correct** implementation:

```
2023-08-01
```

```
2023-08-01T06:50:30-0500
```

```
2023-09-15T09:59:59Z
```

***

## <span id="T004">T004 - Static Sample Contains a Subset of Keys from Live Result</span>

Static samples provide Zapier users and partners a way to preview and map fields
for a trigger or action without actually making a request to your API. It's
important that static samples reflect the real results from these calls as seen
in the Zap History. Errors occur when a Zap uses a field from static sample that
is not provided once the Zap is running.

This check requires the static sample you define for each trigger/action/search to
contain a subset of the keys in the latest run in the [Zap History](https://zapier.com/app/history).

This check is performed using the [Zap History](https://zapier.com/app/history)
for accounts belonging to the integration admins, so build your test Zaps in
these accounts.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```json  theme={null}
static: {"id": 1, "email": "john@example.com"}
live: {"id": 2, "name": "Alice"}
```

<Icon icon="check" /> an example of a **correct** implementation:

```json  theme={null}
static: {"id": 1, "name": "John"}
live: {"id": 2, "name": "Alice", "email": "alice@example.com"}
```

See [Sample Data](https://platform.zapier.com/build/sample-data) for more details on this.

***

## <span id="T005">T005 - Live Trigger Result Respects Output Field Definition</span>

This check takes the latest run from the [Zap History](https://zapier.com/app/history)
and verifies whether the trigger result conforms to the output fields for the
trigger in your integration (if defined). The specific checks are:

* "required" fields must be in the trigger result
* field values in the trigger result match their field type

This check is performed using the [Zap History](https://zapier.com/app/history)
for accounts belonging to the integration admins, so build your test
Zaps in these accounts.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```json  theme={null}
live result: {"id": "1"}
output fields: [
    {"key":  "id", "type": "integer"},
    {"key": "email", "type": "string", "required": true}
]
```

<Icon icon="check" /> an example of a **correct** implementation:

```json  theme={null}
live result: {"id": 1, "email": "john@example.com"}
output fields: [
    {"key":  "id", "type": "integer"},
    {"key": "email", "type": "string", "required": true}
]
```

See [Sample Data](https://platform.zapier.com/build/sample-data) for more details on this.

***

## <span id="T006">T006 - Polling Sample Contains a Subset of Keys from Live Result</span>

For REST Hook triggers, we require you to provide a `Perform List` URL (check
`D006`) so that users can retrieve a real data sample in the Zap editor. This is
called a polling sample, and is created when you test the trigger in the Zap editor
before turning it on.

Errors occur when a Zap uses a field from the polling sample that is not
provided by the hook payload sent once the Zap is running.

To ensure this doesn't happen, this check compares the latest item in the
[Zap History](https://zapier.com/app/history) with the selected polling sample in
the corresponding Zap. For it to pass:

* There must be a Zap that is using the trigger.
* The Zap must have at least one Zap run (the most recent run will be used).
* The trigger must have been tested in the Zap editor via the Perform List method
  to retrieve a polling sample.
* The polling sample should have the same data keys, or a subset of keys, compared
  to those available in the Zap run data.

This check is performed using the [Zap History](https://zapier.com/app/history)
for accounts belonging to the integration admins, so build your test Zaps
in these accounts.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```json  theme={null}
polling sample: {"id": 1, "email": "john@example.com"}
live: {"id": 2, "name": "Alice"}
```

<Icon icon="check" /> an example of a **correct** implementation:

```json  theme={null}
polling sample: {"id": 1, "name": "John"}
live: {"id": 2, "name": "Alice", "email": "alice@example.com"}
```

See [Sample Data](https://platform.zapier.com/build/sample-data) for more details on this.

***

## <span id="U001">U001 - Developer Terms of Service</span>

You must agree to the latest Developer Terms of Service in order to proceed. Go to
[Developer Home](https://developer.zapier.com) to agree.

***

## <span id="Z001">Z001 - Polling Sample Respects Output Field Definition</span>

For REST Hook triggers, we require you to provide a `Perform List` URL (check
`D006`) so that users can pull a live sample in the Zap editor. This is called a
polling sample.

This check takes the latest polling sample from a Zap with this trigger
and verifies that the sample conforms to the output fields for the
trigger in your integration (if defined). The specific checks are:

* "required" fields must be in the polling sample
* field values in the trigger result must match their field type

This check is performed using the Zaps in accounts belonging to the
integration admins, so build your test Zaps in these accounts.

<Icon icon="xmark" /> an example of an **incorrect** implementation:

```json  theme={null}
polling sample: {"id": "1"}
output fields: [
    {"key":  "id", "type": "integer"},
    {"key": "email", "type": "string", "required": true}
]
```

<Icon icon="check" /> an example of a **correct** implementation:

```json  theme={null}
polling sample: {"id": 1, "email": "john@example.com"}
output fields: [
    {"key":  "id", "type": "integer"},
    {"key": "email", "type": "string", "required": true}
]
```

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
