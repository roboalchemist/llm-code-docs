# Source: https://docs.firehydrant.com/docs/change-events.md

# Change Events

A **Change Event** is any change to your system — a new configuration, a feature launch, changing code, etc. System changes cause most outages, so keeping track of them, when they happened, and what components were affected can dramatically impact incident mitigation.

On FireHydrant, Change Events can be created by specific integrations (e.g., [GitHub](https://docs.firehydrant.com/docs/github-integration)), via our [CLI (fhcli)](https://docs.firehydrant.com/docs/firehydrant-cli), via [API calls](https://developers.firehydrant.com/#/), and manually from the FireHydrant UI.

They are most powerful on FireHydrant when associated with specific Services and Environments they affect. See [using Change Events in incidents](#using-change-events-on-incidents) section below.

## Adding change events

### via User Interface

<Image alt="Creating a change event via UI" align="center" width="650px" src="https://files.readme.io/20040ee-image.png">
  Creating a change event via UI
</Image>

1. Go to **Catalog** in the top navigation and then **Change events** on the left.
2. Click "+ Add event" on the top right and you'll be taken to the interface for filling in a new change event.
3. On this page, you can fill in the following details about the change event:
   1. **Summary (required)** - A title or summary of the change
   2. **Description** - A longer description or detail of the change
   3. **Labels** - Key-value pairs of arbitrary values you define
   4. **Time options** - Each change can be at a **Point in Time** or across a **Range**. This changes how the next field is displayed
   5. **Date** or **Start/End Date** - The point in time or start/end times for this change. Changes according to the previous field's selection.
   6. **Services** - The service(s) that were impacted by this change
   7. **Environments** - The environment(s) that were impacted by this change

### via API

To use FireHydrant's API, you first must [create an API key](https://docs.firehydrant.com/docs/api-keys) which requires <Glossary>Owner</Glossary> permissions. Once you have a key, use the *[POST /changes/events](https://developers.firehydrant.com/#/operations/postV1ChangesEvents)* endpoint. Below is an example API call using `cURL`:

```shell FH API
curl --request POST \
  --url https://api.firehydrant.io/v1/changes/events \
  --header "Authorization: $FH_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
  "summary": "New change event via FH API example",
  "labels": {
    "type": "deployment",
    "author": "John Doe"
  },
  "starts_at": "2024-01-02T14:15:22Z",
  "ends_at": "2024-01-24T14:15:22Z",
  "environments": [
    "us-east-1"
  ],
  "services": [
    "iam-service"
  ]
}'
```

### via FH CLI

Like with the API method, you must [generate an API key](https://docs.firehydrant.com/docs/api-keys).

The FireHydrant [CLI (fhcli)](https://docs.firehydrant.com/docs/firehydrant-cli) is a bot/utility for the command line to interact with FireHydrant. One of its commands is `/fhcli event`, which enables you to create a Change Event using the CLI command. This is offered as an alternative to the standard `cURL` or API call - both are acceptable and will result in the same outcome.

Here is an example `fhcli` command to log a change event for a specific service + environment:

```Text FH CLI
fhcli --apiKey "$FH_API_KEY" event "New deployment event via FHCLI example" \
	--labels type=deployment,author="John Doe" \
  --environment us-east-1 \
  --service iam-service
```

### via Integrations

FireHydrant has multiple integrations that can create Change Events automatically:

* GitHub will automatically log any merges or commits to the main repository branch linked to a Service. To learn more, visit the [GitHub integration documentation](https://docs.firehydrant.com/docs/github-integration).
* The Kubernetes integration will automatically log change events according to what is defined in the manifest file. The relevant configuration is within the `config.yml` data for the `ConfigMap`, specifically `watch[*].resources[*].updateOn`. For more information, see the [Kubernetes](https://docs.firehydrant.com/docs/kubernetes-integration) documentation page.

## Using Change Events on Incidents

When Change Events are associated with Services and Environments, FireHydrant can intelligently associate them with incidents where those specific components are impacted. This can provide responders with an initial investigation pathway - and sometimes catalyst(s) - for the incident itself.

For example, given an incident in which the `iam-service` is impacted, FireHydrant will automatically associate any recent changes for the `iam-service` according to your [Suspect Changes Window](/docs/other-incident-settings#suspect-changes-window).

To see associated Change Events on an incident, navigate to an incident's Command Center page and then click on the **Change Events** tab.

<Image alt="Example incident where a change event for `iam-service` was automatically associated with an incident because it was within `1d` before the incident occurred" align="center" width="650px" src="https://files.readme.io/e1fdfe8-image.png">
  Example incident where a change event for `iam-service` was automatically associated with an incident because it was within `1d` before the incident occurred
</Image>

You can also associate change events manually to an incident by clicking on "Attach change event" or creating a new change event and attaching it by clicking "+ Create a change Event."

Once change events are attached to incidents, you can then mark their relevancy in the table below. The current options are **Suspect** (their initial state), **Caused**, **Fixed**, or outright dismiss the change event.

> 📘 Note:
>
> Any new change events that come in after an incident has already started will also be automatically associated with the incident according to impacted services/environments.

## Change Identities

Building on the above, FireHydrant enables you to loosely link change events together using what we call **Change Identities** - when you create change events via the FireHydrant API, you can include a key `change_identities` with them. Change events can have multiple identities.

For example, you might send one change event from your continuous integration system and another from your deployment system. Each of these is a unique change event, but you can tie them together with an identity, such as the commit SHA that initiated both automations.

### Example

<Image alt="Example Change Event with an identity" align="center" width="650px" src="https://files.readme.io/21136bd-image.png">
  Example Change Event with an identity
</Image>

For example, your test runner can send a change event and include an identity value of `commit_sha` with a value of `abc123`. When your test suite completes, using cURL, we can send a change event with the commit sha as an identity:

```shell Example
$ curl -X POST -H "Authorization: Bearer $FH_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "summary": "Finished Test Run",
    "starts_at": "2024-01-02T08:00:00",
    "change_identities": [
      {
        "type": "commit_sha",
        "value": "abcdef123456789"
      }
    ]
  }' https://api.firehydrant.io/v1/changes/events
```

This creates a change event in FireHydrant with the commit SHA as an identity.

> 🚧 Note:
>
> The value for each type in a change identity must be unique for a given change event. Duplicate values will be silently dropped. If you have types that may reasonably contain duplicate values, `author` and `reviewer` for instance, consider using a `label` instead.

Now, let's create another change event with the same change identity but also include another identity for a Docker image tag.

```shell Example
$ curl -X POST -H "Authorization: Bearer fhb-your-token-here" \
  -H "Content-Type: application/json" \
  -d '{ 
    "summary": "Built Docker Image",
    "starts_at": "2019-05-07T08:00:00",
    "change_identities": [
      {
        "type": "commit_sha",
        "value": "abcdef123456780"
      },
      {
        "type": "image",
        "value": "registry.firehydrant.io/firehydrant/laddertruck:master-abcdef123456789"
      }
    ]
  }' https://api.firehydrant.io/v1/changes/events
```

The above cURL snippet creates a change event just like the previous request; however, this new change event is also automatically linked to our previous change. All associated change events are cited (and linked) in the **Associated Changes** section at the bottom of the page.

### Loosely linking change events using partial identity

We can loosely link another change event in our deployment pipeline by only including a partial overlap of another change event's identities.

This is a valuable option because different stages have different contexts as a change moves through a pipeline. With a CI pipeline, you can usually get the commit SHA, but for deployment to a server, you may only know the artifact name (such as a Docker image or tarball name). By including previous identities, we can link events loosely together.

In this example, we only include the "image" identity that matches the previous change event we sent. FireHydrant links this event with the other event and has it in your group change view.

```shell Example
$ curl -X POST -H "Authorization: Bearer $FH_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "summary": "Deployed to Kubernetes (Production)",
    "starts_at": "2019-05-07T09:10:00",
    "change_identities": [
      {
        "type": "image",
        "value": "registry.firehydrant.io/firehydrant/laddertruck:master-abcdef123456700"
      }
    ]
  }' https://api.firehydrant.io/v1/changes/events
```