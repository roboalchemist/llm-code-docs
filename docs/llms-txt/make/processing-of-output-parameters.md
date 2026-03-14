# Source: https://developers.make.com/custom-apps-documentation/best-practices/output-parameters/processing-of-output-parameters.md

# Processing of output parameters

## Response output <a href="#response-output" id="response-output"></a>

A module's response output should be defined for the case when a request is fulfilled successfully. The output definition should not contain error messages (this belongs in the Base section's error handling) nor the additional metadata which may arrive bundled with the actual response information.

{% tabs %}
{% tab title="Incorrect example" %}
No matter the module type, the output shouldn't be defined like this:

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5fd241ed760a7c19847cc1c26a0d749f916ea2d6%2Fprocessingoutputpara_incorrectexample.png?alt=media" alt="" width="543"></div>
{% endtab %}
{% endtabs %}

The best approach is to return the API response as it is. In many cases, the response varies based on the user who is using the app, as responses can contain different custom fields. If the response returned is unchanged and if all the parameters still aren't described in the output parameters, Make will automatically suggest additional parameters from incoming data.

### Search modules

{% tabs %}
{% tab title="Good practice" %}

```json
"response": {
    "output": "{{item}}",
    "iterate": "{{body}}"
}
```

{% endtab %}

{% tab title="Bad practice " %}

```json
"response": {
    "output": {
        "id": "{{item.id}}",
        "name": "{{item.name}}"
    },
    "iterate": "{{body}}"
}
```

{% endtab %}
{% endtabs %}

### Action modules

{% tabs %}
{% tab title="Good practice" %}

```json
"response": {
    "output": "{{body}}"
}
```

{% endtab %}

{% tab title="Bad practice" %}

```json
"response": {
    "output": {
        "id": "{{body.id}}",
        "name": "{{body.name}}"
    }
}
```

{% endtab %}
{% endtabs %}

## Delete unnecessary output data

Your output data might include information related to a backend process. While you may use this information for error handling, for example, it's not necessary to pass this information to another service.

Sending superfluous information might cause confusion. For example, a 'status' value of a task could be easily mistaken for the 'status' of the processing of data.

To avoid confusion, structure your output in a user-friendly format and delete unnecessary output data.

{% tabs %}
{% tab title="Incorrect output" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1cc0f8e242ae562ca0a91c15f348f4f57c23dfa2%2Fdeleteoutput_incorrect.png?alt=media" alt="" width="294"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Correct output" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2f7bcf4dc1fd29efb115c40cbba9f453dea5397d%2Fdeleteoutput_correct.png?alt=media" alt="" width="298"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

## Parse dates

You should always parse datetime in the module output with the following **exceptions**:

* No date, only time. For example, `13:30`.
* No time, only date. For example, `2024-01-01`.
* With both date and time, but no time zone. For example: `2020-06-08 12:37:56`.
  * Exception: If the API documentation specifies that the given datetime is in UTC or some other time zone.
  * Do not use the Make user’s time zone or the Make organization’s time zone, because it may be different from the time zone configured in the third-party services.
* Time stamp in seconds or milliseconds.
  * Exception: If it has a clear indication by its name, in the API documentation or metadata endpoints, that shows such fields are a `Date` type field. **DO NOT** try to parse time stamps by assuming a lengthy number must be a time stamp.

### Examples

#### Pipedrive <a href="#pipedrive" id="pipedrive"></a>

Part of the response from Pipedrive API `/activities` :

```json
[
    {
        "id": 8,
        "due_date": "2022-06-09",
        "due_time": "10:00",
        "duration": "01:00",
        "add_time": "2020-06-08 12:37:56",
        "marked_as_done_time": "2020-08-08 08:08:38",
        "update_time": "2020-08-08 12:37:56"
    }
]
```

[API documentation: Date format](https://pipedrive.readme.io/docs/core-api-concepts-date-format) from Pipedrive

<table><thead><tr><th width="197.4814453125" valign="top">Field</th><th width="146.5" valign="top">Parse?</th><th valign="top">Reason</th></tr></thead><tbody><tr><td valign="top"><code>due_date</code></td><td valign="top">No</td><td valign="top">No time, only date.</td></tr><tr><td valign="top"><code>due_time</code></td><td valign="top">No</td><td valign="top">No date, only time.</td></tr><tr><td valign="top"><code>duration</code></td><td valign="top">No</td><td valign="top">No date, only time.</td></tr><tr><td valign="top"><code>add_time</code></td><td valign="top">Yes</td><td valign="top"><p>Only date and time with no time zone.</p><p><strong>BUT</strong> we know it’s UTC.</p></td></tr><tr><td valign="top"><code>marked_as_done_time</code></td><td valign="top">Yes</td><td valign="top"><p>Only date and time with no time zone.</p><p><strong>BUT</strong> we know it’s UTC.</p></td></tr><tr><td valign="top"><code>update_time</code></td><td valign="top">Yes</td><td valign="top"><p>Only date and time with no time zone.</p><p><strong>BUT</strong> we know it’s UTC.</p></td></tr></tbody></table>

#### Virtuagym <a href="#virtuagym" id="virtuagym"></a>

Part of the response from Virtuagym API `/api/v0/activity`:

{% tabs %}
{% tab title="Source" %}

```json
{
    "act_inst_id": 25957,
    "timestamp_edit": 1319816131,
    "timestamp": 1319796000
}
```

{% endtab %}
{% endtabs %}

<table><thead><tr><th width="163.77777099609375" valign="top">Field</th><th width="161" valign="top">Parse?</th><th valign="top">Reason</th></tr></thead><tbody><tr><td valign="top"><code>timestamp_edit</code></td><td valign="top">Yes</td><td valign="top">Timestamp in seconds with clear indication by it’s name.</td></tr><tr><td valign="top"><code>timestamp</code></td><td valign="top">Yes</td><td valign="top">Timestamp in seconds with clear indication by it’s name.</td></tr></tbody></table>

## Flatten nested outputs

Deeply nested outputs result in undesirable UX when the user maps the values.

Consider:

* creating a mappable version of the key-value pairs, and
* flattening unnecessary nested collections.

{% tabs %}
{% tab title="Good example of output (OpenAI)" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-29faa87576cd0cd89f3564296d775075d39c9b8c%2Fnestedoutputs1.png?alt=media" alt="" width="426"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Good example of output (Unbounce)" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-afc626167bbd9bf6efe467b186b3eacf040cb6ad%2Fnestedoutputs2.png?alt=media" alt="" width="281"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Bad example of output" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-08037e6ab8ca9aedd819c9da01535766afb0f707%2Fnestedoutputs3.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

See an additional example of[ implementing dynamic mappable parameters using a custom IML function](https://developers.make.com/custom-apps-documentation/app-components/iml-functions/dynamic-mappable-parameters).
