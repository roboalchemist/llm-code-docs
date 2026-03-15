# Source: https://docs.firehydrant.com/docs/custom-event-source.md

# Custom Event Source

There are times where you need more flexibility when sending an alert to an on-call team member. In some cases, you may need to include different details in the message, or change the alert level or notification priority. In those advanced use-cases, FireHydrant is equipped with the ability to define your own function to parse Signals the way you want them. You can think of these as lambdas that are run for each incoming event into your FireHydrant account, and emit an Event type.

## How it works

When FireHydrant receives incoming payloads for the default list of sources we support, we convert them into a common data structure we call an Event. The order looks like this:

1. `HTTP POST https://signals.firehydrant.com/v1/process/{orgkey}`
2. Parse incoming payload
3. Transpose it into an Event object
4. Store the Event, and fire any alerts that are relevant for it

For step 3, we have a common list of what we call “transposers” – these are the ones you find on the main page of event sources in FireHydrant. They work for *most* use cases you may have.

But when these pre-built transposers *don’t* suit your needs, you need a bit more horsepower. This is why we chose JavaScript to parse payloads that result, ultimately, into the [Event data type](https://docs.firehydrant.com/docs/events-data-model). The flow changes to be:

1. `HTTP POST https://signals.firehydrant.com/v1/relay/custom-source/{orgkey}`
2. Load custom JavaScript expression (based on `custom-source` in the URL)
3. Evaluate and execute the function with the incoming JSON payload
4. Take the result of the `transpose` function we ran
5. Validate the `transpose` function returned a valid Event
6. Store the Signal, and fire any alerts that are relevant for it

## Limitations

* As much as we’d love to give people as much time as they need to process signals, we do require that these scripts evaluate in **under 50 milliseconds.** *Trust us, we don’t dilly dally on these*.
* Scripts do not have access to any IO calls (filesystem, network)
* Scripts must be compatible with [ECMAScript 5.1](https://262.ecma-international.org/5.1/)

## Getting started

You can write your own *transposer script* to ensure that FireHydrant understands the payload. Create your own custom event source on **Signals> Event Sources > Add custom event source**.

## Transposer function

A valid JavaScript transposer script must:

1. Have the function name `transpose`.
2. Takes in 1 `input` as a parameter.
3. Returns a valid [Event Data Model](https://docs.firehydrant.com/docs/events-data-model) object.

<Image alt="The url for a generic webhook integration" align="center" width="800px" src="https://files.readme.io/8f3d5e6-CleanShot_2024-07-18_at_16.02.412x.png">
  A valid JavaScript custom event function
</Image>

Custom event sources are not limited only to the `transpose` function, either. You may define any valid Javascript function or expression and use them. For example, you may have a function to determine the Signal level that should be used.

```javascript
const levelMap = {
  "critical": 2,
  "error": 1,
  "warning": 1,
  "info": 0,
  "debug": 0
}

function payloadLevel(payload) {
  if (!payload?.level) return 0;
  return levelMap[payload.level.toLowerCase()] || 0;
}
```

## Provided input structure

Transpose function takes in `input` argument, which consist of request payload and body in the following structure:

```javascript
{
  headers: {
    "Content-Type": "application/json"
  },
  data: {
    // The request JSON payload here
  }
}
```

## Debugging

It’s very likely that, at some point, you’ll need to debug what’s going on with your custom script. In lieu of a `console.log` function, we provide a `debug` function that will automatically display the provided argument in the FireHydrant.

<Image alt="The url for a generic webhook integration" align="center" width="800px" src="https://files.readme.io/c6f1341-CleanShot_2024-07-18_at_16.16.222x.png">
  Debugging custom event source script
</Image>

The `debug` function is a variadic function as well. Meaning you can pass multiple arguments to it.There is a hard limit of 10 debug calls per execution of your script.

> 📘 Note:
>
> There is a hard limit of 10 debug calls per execution of your script.

### Debugging issues with malformed payloads

FireHydrant provides a way to see the raw events that have been received to better debug incoming payloads that you're transposing into Signals.

![](https://files.readme.io/30d8378b0900790ec4843284a9011fb775adc333d2a227f9f757c53235aaee9c-image.png)

When you click a payload, you'll be shown more details about payloads as well. For example, when a payload is rejected from Signals, we'll give you a helpful reason as to why.

![](https://files.readme.io/5ea4a98af695b5f9c0cc36f3c245f6ad5ee9b898d40226133c9fc79c2c4c65d5-CleanShot_2025-06-30_at_23.56.322x.png)

<br />

## Examples

The following are examples of default `transpose` functions for different types of monitoring providers.

### Alertmanager

```javascript
/*
 * Transpose a payload from a webhook into a signal.
 *
 * @returns {{summary: string, body: string, level: number, links: string[], images: string[], tags: string[], idempotency_key: string, status: number}} Signal object.
 */
function transpose(input) {
  const payload = input.data;
  const alerts = payload.alerts;

  const commonAnnotations = payload.commonAnnotations;
  const commonLabels = payload.commonLabels;
  const groupLabels = payload.groupLabels;

  const signal = {
    summary: commonAnnotations.summary || "Alert from Alertmanager",
    body: commonAnnotations.description || "No body provided",
    links: alerts.map(a => ({href: a.generatorURL || payload.externalURL, text: a.labels.alertname})),
    annotations: {
      ...(Object.keys(commonAnnotations).reduce((m, k) => {
        m[`annotations-${k}`] = commonAnnotations[k];
        return m;
      }, {})),
      ...(Object.keys(commonLabels).reduce((m, k) => {
        m[`labels-${k}`] = commonLabels[k];
        return m;
      }, {})),
      ...(Object.keys(groupLabels).reduce((m, k) => {
        m[`group-by-${k}`] = groupLabels[k];
        return m;
      }, {})),
      groupKey: payload.groupKey,
    },
    idempotency_key: md5(payload.groupKey),
  }

  return signal;
}
```

### Datadog

```javascript
const levelMap = {
  "critical": 2,
  "error": 1,
  "warning": 1,
  "info": 0,
  "debug": 0
}

function payloadLevel(payload) {
  if (!payload?.level) return 0;
  return levelMap[payload.level.toLowerCase()] || 0;
}

function payloadStatus(s) {
  if (!s) return 0;
  return s === "Triggered" ? 0 : 1;
}

function payloadTags(tags) {
  if (typeof tags === "string") {
    return tags.split(",")
  }
  if (Array.isArray(tags)) {
    return tags
  }
  return []
}

/*
 * Transpose a payload from a webhook into a signal.
 *
 * @returns {{summary: string, body: string, level: number, links: string[], images: string[], tags: string[], idempotency_key: string, status: number}} Signal object.
 */
function transpose(input) {
  const payload = input.data;
  const signal = {
    summary: payload?.summary || "Alert from Datadog",
    body: payload?.body || "No body provided",
    level: payloadLevel(payload?.level),
    links: payload?.links || [],
    images: (payload?.images || []).filter(i => !!i.src),
    tags: payloadTags(payload?.tags),
    idempotency_key: payload?.summary || "",
    status: payloadStatus(payload?.status),
  }
  if (payload?.unique_key) {
    signal.idempotency_key = payload?.unique_key;
  }
  return signal
}

```