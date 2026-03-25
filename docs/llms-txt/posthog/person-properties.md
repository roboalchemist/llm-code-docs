# Source: https://posthog.com/docs/product-analytics/person-properties.md

# Person properties - Docs

Person properties enable you to capture, manage, and analyze specific data about a user. You can use them to create [filters](/docs/product-analytics/trends.md#filtering-events-based-on-properties) or [cohorts](/docs/data/cohorts.md), which can then be used in [insights](/docs/product-analytics/insights.md), [feature flags](/docs/feature-flags.md), [surveys](/docs/surveys.md), and more.

Person properties are stored on [person profiles](/docs/data/persons.md). When setting properties, a person profile is created if it doesn't already exist.

## How to set person properties

The recommended way to set person properties is to send a `$set` event with a `$set` property. For SDKs that provide helper methods (such as `posthog.setPersonProperties`), we recommend using them, as they handle important side effects like switching the user to identified mode.

PostHog AI

### Web

```javascript
posthog.setPersonProperties(
    { name: 'Max Hedgehog' }, // $set properties
    { initial_url: '/blog' }  // $set_once properties
)
```

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id',
    event: '$set',
    properties: {
        $set: { name: 'Max Hedgehog'  },
        $set_once: { initial_url: '/blog' },
    },
})
```

### Python

```python
posthog.capture(
    'distinct_id',
    event='$set',
    properties={
        '$set': {'name': 'Max Hedgehog'},
        '$set_once': {'initial_url': '/blog'}
    }
)
```

### PHP

```php
PostHog::capture([
    'distinctId' => 'distinct_id',
    'event' => '$set',
    'properties' => [
        '$set' => [
            'name' => 'Max Hedgehog'
        ],
        '$set_once' => [
            'initial_url' => '/blog'
        ]
    ]
]);
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id',
    event: '$set',
    properties: {
        '$set': { name: 'Max Hedgehog' },
        '$set_once': { initial_url: '/blog' }
    }
})
```

### Go

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id",
    Event:      "$set",
    Properties: map[string]interface{}{
        "$set": map[string]interface{}{
            "name": "Max Hedgehog",
        },
        "$set_once": map[string]interface{}{
            "initial_url": "/blog",
        },
    },
})
```

### Java

```java
posthog.capture("distinct_id", "$set", new HashMap<String, Object>() {
  {
    put("$set",  new HashMap<String, Object>() {
      {
        put("name", "Max Hedgehog");
      }
    });
    put("$set_once",  new HashMap<String, Object>() {
      {
        put("initial_url", "/blog");
      }
    });
  }
});
```

### Terminal

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "properties": {
      "$set": {"name": "Max Hedgehog" },
      "$set_once": {"initial_url": "/blog"}
    },
    "timestamp": "2020-08-16 09:03:11.913767",
    "distinct_id": "1234",
    "event": "$set"
}' https://us.i.posthog.com/i/v0/e/
```

You can also set person properties when you call the [`identify`](/docs/data/identify.md) method:

PostHog AI

### Web

```javascript
posthog.identify(
  'distinct_id',  // Replace 'distinct_id' with your user's unique identifier
  { email: 'max@hedgehogmail.com', name: 'Max Hedgehog' } // optional: set additional person properties
);
```

### Android

```kotlin
PostHog.identify(
    distinctId = distinctID, // Replace 'distinctID' with your user's unique identifier
    // optional: set additional person properties
    userProperties = mapOf(
        "name" to "Max Hedgehog",
        "email" to "max@hedgehogmail.com"
    )
)
```

### iOS

```swift
PostHogSDK.shared.identify("distinct_id", // Replace "distinct_id" with your user's unique identifier
                           userProperties: ["name": "Max Hedgehog", "email": "max@hedgehogmail.com"]) // optional: set additional person properties
```

### React Native

```jsx
posthog.identify('distinct_id', { // Replace "distinct_id" with your user's unique identifier
    email: 'max@hedgehogmail.com', // optional: set additional person properties
    name: 'Max Hedgehog'
})
```

### Dart

```dart
await Posthog().identify(
  userId: 'distinct_id', // Replace "distinct_id" with your user's unique identifier
  userProperties: {
    email: "max@hedgehogmail.com", // optional: set additional person properties
    name: "Max Hedgehog"
});
```

Person property values can be strings, booleans, numbers, objects, or arrays. For objects and arrays, you can use [SQL expressions](/docs/sql/expressions.md) to access nested properties in PostHog.

> **Note:** Person properties are set in the order the events are ingested, and not according to event timestamps. Since we typically ingest events as soon as we receive them, you only need to take this into consideration when you're [importing historical data](/docs/migrate.md).

### What is the difference between `set` and `set_once`?

Using `set` replaces any property value that may have been set on a person profile. In contrast, `set_once` only sets the property if it has never been set before.

`set` is typically used for properties that may change over time – e.g., email, current plan, organization name. `set_once` is typically only used for information that is guaranteed to never change – e.g., the first URL a user visited, or the date a user first logged in.

For example:

PostHog AI

### Web

```javascript
posthog.capture(
    'event_name',
    {
        $set: { name: 'Max Hedgehog'  },
        $set_once: { initial_url: '/blog' },
    }
)
posthog.capture(
    'event_name',
    {
        $set: { name: 'Mr. Fox'  },
        $set_once: { initial_url: '/pricing' },
    }
)
// name: 'Mr. Fox'
// initial_url: '/blog'
// When using anonymous events with `person_profiles: 'identified_only'`,
// adding `$set` or `$set_once` properties to an event will not create a
// person profile. Use one of the functions mentioned here:
// https://posthog.com/docs/data/anonymous-vs-identified-events
```

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id',
    event: 'event_name',
    properties: {
        $set: { name: 'Max Hedgehog'  },
        $set_once: { initial_url: '/blog' },
    },
})
client.capture({
    distinctId: 'distinct_id',
    event: 'event_name',
    properties: {
        $set: { name: 'Mr. Fox'  },
        $set_once: { initial_url: '/pricing' },
    },
})
// name: 'Mr. Fox'
// initial_url: '/blog'
```

### Python

```python
posthog.capture(
    'distinct_id',
    event='event_name',
    properties={
        '$set': {'name': 'Max Hedgehog'},
        '$set_once': {'initial_url': '/blog'}
    }
)
posthog.capture(
    'distinct_id',
    event='event_name',
    properties={
        '$set': {'name': 'Mr. Fox'},
        '$set_once': {'initial_url': '/pricing'}
    }
)
# name: 'Mr. Fox'
# initial_url: '/blog'
```

### PHP

```php
PostHog::capture([
    'distinctId' => 'distinct_id',
    'event' => 'event_name',
    'properties' => [
        '$set' => [
            'name' => 'Max Hedgehog'
        ],
        '$set_once' => [
            'initial_url' => '/blog'
        ]
    ]
]);
PostHog::capture([
    'distinctId' => 'distinct_id',
    'event' => 'event_name',
    'properties' => [
        '$set' => [
            'name' => 'Mr. Fox'
        ],
        '$set_once' => [
            'initial_url' => '/pricing'
        ]
    ]
]);
# name: 'Mr. Fox'
# initial_url: '/blog'
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id',
    event: 'event_name',
    properties: {
        '$set': { name: 'Max Hedgehog' },
        '$set_once': { initial_url: '/blog' }
    }
})
posthog.capture({
    distinct_id: 'distinct_id',
    event: 'event_name',
    properties: {
        '$set': { name: 'Mr. Fox' },
        '$set_once': { initial_url: '/pricing' }
    }
})
# name: 'Mr. Fox'
# initial_url: '/blog'
```

### Go

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id",
    Event:      "event_name",
    Properties: map[string]interface{}{
        "$set": map[string]interface{}{
            "name": "Max Hedgehog",
        },
        "$set_once": map[string]interface{}{
            "initial_url": "/blog",
        },
    },
})
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id",
    Event:      "event_name",
    Properties: map[string]interface{}{
        "$set": map[string]interface{}{
            "name": "Mr. Fox",
        },
        "$set_once": map[string]interface{}{
            "initial_url": "/pricing",
        },
    },
})
// name: 'Mr. Fox'
// initial_url: '/blog'
```

### Java

```java
posthog.capture("distinct_id", "event_name", new HashMap<String, Object>() {
  {
    put("$set",  new HashMap<String, Object>() {
      {
        put("name", "Max Hedgehog");
      }
    });
    put("$set_once",  new HashMap<String, Object>() {
      {
        put("initial_url", "/blog");
      }
    });
  }
});
posthog.capture("distinct_id", "event_name", new HashMap<String, Object>() {
  {
    put("$set",  new HashMap<String, Object>() {
      {
        put("name", "Mr. Fox");
      }
    });
    put("$set_once",  new HashMap<String, Object>() {
      {
        put("initial_url", "/pricing");
      }
    });
  }
});
// name: 'Mr. Fox'
// initial_url: '/blog'
```

### How to remove person properties

Similarly to how you set properties, you can use `$unset` to remove properties from person profiles with any event and including an array of property keys:

PostHog AI

### Web

```javascript
posthog.capture(
    'event_name',
    {
        $unset: ['email'],
    }
)
```

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id',
    event: 'event_name',
    properties: {
        $unset: ['email'],
    },
})
```

### Python

```python
posthog.capture(
    'distinct_id',
    event='event_name',
    properties={
        '$unset': ['email'],
    }
)
```

### PHP

```php
PostHog::capture([
    'distinctId' => 'distinct_id',
    'event' => 'event_name',
    'properties' => [
        '$unset' => [
           'email'
        ]
    ]
]);
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id',
    event: 'event_name',
    properties: {
        '$unset': ['email']
    }
})
```

### Go

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id",
    Event:      "event_name",
    Properties: map[string]interface{}{
        "$unset": []string{"email"},
    },
})
```

### Java

```java
posthog.capture("distinct_id", "event_name", new HashMap<String, Object>() {
  {
    put("$unset", new String[]{"name"});
  }
});
```

## `last_seen_at` field

PostHog automatically updates the `last_seen_at` field for a person when an event from them is captured. This gets updated once per hour, and the timestamp is always rounded down to the nearest hour.

You can prevent `last_seen_at` updates by setting the `$update_person_last_seen_at` *event* property to `false`.

This is useful for backend enrichment jobs or server-side events that update [person properties](/docs/product-analytics/person-properties.md) but don't represent real user activity.

PostHog AI

### Web

```javascript
posthog.capture('backend_enrichment', {
    $update_person_last_seen_at: false,
    $set: {
        enriched_property: 'value'
    }
})
```

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id',
    event: 'backend_enrichment',
    properties: {
        $update_person_last_seen_at: false,
        $set: {
            enriched_property: 'value'
        }
    },
})
```

### Python

```python
posthog.capture(
    'distinct_id',
    event='backend_enrichment',
    properties={
        '$update_person_last_seen_at': False,
        '$set': {
            'enriched_property': 'value'
        }
    }
)
```

When `$update_person_last_seen_at` is `false`, the event is processed normally but the person's `last_seen_at` timestamp remains unchanged.

> **Note:** This only applies when updating existing persons - `last_seen_at` is always set when a person is first created.

## Limitations

**Size Limitation**

Person properties have a size limit of **512KB** per person record. If you attempt to create or update a person with properties that exceed this limit, the update will be rejected and an ingestion warning will be logged. This is a limit on the combined size of all properties on the person record, not individual property values.

## How to view and edit a person profile and properties

To view the person profile and properties for a particular person, go to [Persons & Groups](https://app.posthog.com/persons) in the PostHog app. Then, click on any person in the list to view their properties.

On a person's property list, you can add properties to them by clicking the "New property" button, and then adding a key, type, and value. You can also delete a custom property for a user by clicking the red garbage bin icon on the right side of the property listing.

You can find a list of all person properties in the [properties](https://us.posthog.com/data-management/properties?type=person) tab in **data management**. Just change the dropdown from **event properties** to **\*person properties**.

## Person display name

The display name is the person property value shown in the PostHog UI to represent a user. It is their person `distinct_id` by default, but can be configured in [project settings](https://us.posthog.com/settings/project#person-display-name).

![Where to change the display name in project settings](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/data/user-properties/change-display-name-light-mode.png)![Where to change the display name in project settings](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/data/user-properties/change-display-name-dark-mode.png)

## Default person properties

PostHog attempts to set the following properties when using the `posthog-js` library or JavaScript snippet. These properties are set when the person profile is created and updated via person events (e.g., `$set`, `$identify`).

**Setting person properties**

By default, only identified users have person profiles. See our [anonymous vs identified events documentation](/docs/data/anonymous-vs-identified-events.md) for more details.

| Property | Property Name | Description | Example |
| --- | --- | --- | --- |
| utm_campaign | UTM Campaign | UTM campaign tag (last-touch). | feature launch, discount |
| utm_content | UTM Content | UTM content tag (last-touch). | bottom link, second button |
| utm_medium | UTM Medium | UTM medium tag (last-touch). | Social, Organic, Paid, Email |
| utm_source | UTM Source | UTM source tag (last-touch). | Google, Bing, Twitter, Facebook |
| $browser | Browser | Name of the browser the user has used. | Chrome, Firefox |
| $browser_version | Browser Version | The browser version used. Used in combination with Browser. | 70, 79 |
| $initial_browser | Initial Browser | Name of the browser the user first used (first-touch). | Chrome, Firefox |
| $initial_browser_version | Initial Browser Version | The browser version the user first used (first-touch). Used in combination with Browser. | 70, 79 |
| $initial_current_url | Initial Current URL | The first URL the user visited, including all the trimmings. | [https://example.com/interesting-article?parameter=true](https://example.com/interesting-article?parameter=true) |
| $initial_device_type | Initial Device Type | The initial type of device that was used (first-touch). | Mobile, Tablet, Desktop |
| $initial_os | Initial OS | The operating system that the user first used (first-touch). | Windows, Mac OS X |
| $initial_pathname | Initial Path Name | The path of the Current URL, which means everything in the URL after the domain. Data from the first time this user was seen. | /pricing, /about-us/team |
| $initial_referrer | Initial Referrer URL | URL of where the user came from most recently (first-touch). Data from the first time this user was seen. | [https://google.com/search?q=posthog&rlz=1C](https://google.com/search?q=posthog&rlz=1C)... |
| $initial_referring_domain | Initial Referring Domain | Domain of where the user came from most recently (first-touch). Data from the first time this user was seen. | google.com, facebook.com |
| $initial_utm_campaign | Initial UTM Campaign | UTM campaign tag (first-touch). | feature launch, discount |
| $initial_utm_content | Initial UTM Content | UTM content tag (first-touch). | bottom link, second button |
| $initial_utm_medium | Initial UTM Medium | UTM medium tag (first-touch). | Social, Organic, Paid, Email |
| $initial_utm_source | Initial UTM Source | UTM source tag (first-touch). | Google, Bing, Twitter, Facebook |
| $os | OS | The operating system of the user. | Windows, Mac OS X |
| $referrer | Referrer URL | URL of where the user came from most recently (last-touch). | [https://google.com/search?q=posthog&rlz=1C](https://google.com/search?q=posthog&rlz=1C)... |
| $referring_domain | Referring Domain | Domain of where the user came from most recently (last-touch). | google.com, facebook.com |

### GeoIP Properties

By default, the [GeoIP plugin](/docs/apps/geoip-enrichment.md) is turned on for all PostHog projects. This adds the following properties to all events.

| Property | Property Name | Description | Example |
| --- | --- | --- | --- |
| $geoip_city_name | City Name | Name of the city matched to this event's IP address. | Sydney, Chennai, Brooklyn |
| $geoip_continent_code | Continent Code | Code of the continent matched to this event's IP address. | OC, AS, NA |
| $geoip_continent_name | Continent Name | Name of the continent matched to this event's IP address. | Oceania, Asia, North America |
| $geoip_country_code | Country Code | Code of the country matched to this event's IP address. | AU, IN, US |
| $geoip_country_name | Country Name | Name of the country matched to this event's IP address. | Australia, India, United States |
| $geoip_latitude | Latitude | Approximated latitude matched to this event's IP address. | -33.8591, 13.1337, 40.7 |
| $geoip_longitude | Longitude | Approximated longitude matched to this event's IP address. | 151.2, 80.8008, -73.9 |
| $geoip_postal_code | Postal Code | Approximated postal code matched to this event's IP address. | 2000, 600004, 11211 |
| $geoip_subdivision_1_code | Subdivision 1 Code | Code of the subdivision matched to this event's IP address. | NSW, TN, NY |
| $geoip_subdivision_1_name | Subdivision 1 Name | Name of the subdivision matched to this event's IP address. | New South Wales, Tamil Nadu, New York |
| $geoip_subdivision_2_code | Subdivision 2 Code | Code of the second subdivision matched to this event's IP address. | 201, 141, 045 |
| $geoip_subdivision_2_name | Subdivision 2 Name | Name of the second subdivision matched to this event's IP address. | Inner West, Chennai Central, Kings County |
| $geoip_time_zone | Timezone | Timezone matched to this event's IP address. | Australia/Sydney, Asia/Kolkata, America/New_York |
| $initial_geoip_city_name | Initial City Name | Name of the city matched to this event's IP address. Data from the first time this user was seen. | Sydney, Chennai, Brooklyn |
| $initial_geoip_continent_code | Initial Continent Code | Code of the continent matched to this event's IP address. Data from the first time this user was seen. | OC, AS, NA |
| $initial_geoip_continent_name | Initial Continent Name | Name of the continent matched to this event's IP address. Data from the first time this user was seen. | Oceania, Asia, North America |
| $initial_geoip_country_code | Initial Country Code | Code of the country matched to this event's IP address. Data from the first time this user was seen. | AU, IN, US |
| $initial_geoip_country_name | Initial Country Name | Name of the country matched to this event's IP address. Data from the first time this user was seen. | Australia, India, United States |
| $initial_geoip_latitude | Initial Latitude | Approximated latitude matched to this event's IP address. Data from the first time this user was seen. | -33.8591, 13.1337, 40.7 |
| $initial_geoip_subdivision_1_code | Initial Subdivision 1 Code | Code of the subdivision matched to this event's IP address. Data from the first time this user was seen. | NSW, TN, NY |
| $initial_geoip_longitude | Initial Longitude | Approximated longitude matched to this event's IP address. Data from the first time this user was seen. | 151.2, 80.8008, -73.9 |
| $initial_geoip_postal_code | Initial Postal Code | Approximated postal code matched to this event's IP address. Data from the first time this user was seen. | 2000, 600004, 11211 |
| $initial_geoip_subdivision_1_name | Initial Subdivision 1 Name | Name of the subdivision matched to this event's IP address. Data from the first time this user was seen. | New South Wales, Tamil Nadu, New York |
| $initial_geoip_subdivision_2_code | Initial Subdivision 2 Code | Code of the second subdivision matched to this event's IP address. Data from the first time this user was seen. | 201, 141, 045 |
| $initial_geoip_subdivision_2_name | Initial Subdivision 2 Name | Name of the second subdivision matched to this event's IP address. Data from the first time this user was seen. | Inner West, Chennai Central, Kings County |
| $initial_geoip_time_zone | Initial Timezone | Timezone matched to this event's IP address. Data from the first time this user was seen. | Australia/Sydney, Asia/Kolkata, America/New_York |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better