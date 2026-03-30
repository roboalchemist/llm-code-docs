# Source: https://docs.airbyte.com/platform/connector-development/ux-handbook.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/ux-handbook.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/ux-handbook.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/ux-handbook.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/ux-handbook.md

# UX Handbook

Copy Page

## Connector Development UX Handbook[​](#connector-development-ux-handbook "Direct link to Connector Development UX Handbook")

![Connector UX Handbook](/assets/images/uivsux-e9ea8aebc759d646ae4ce97922331846.png)

### Overview[​](#overview "Direct link to Overview")

The goal of this handbook is to allow scaling high quality decision making when developing connectors.

The Handbook is a living document, meant to be continuously updated. It is the best snapshot we can produce of the lessons learned from building and studying hundreds of connectors. While helpful, this snapshot is never perfect. Therefore, this Handbook is not a replacement for good judgment, but rather learnings that should help guide your work.

### How to use this handbook[​](#how-to-use-this-handbook "Direct link to How to use this handbook")

1. When thinking about a UX-impacting decision regarding connectors, consult this Handbook.
2. If the Handbook does not answer your question, then consider proposing an update to the Handbook if you believe your question will be applicable to more cases.

### Definition of UX-impacting changes[​](#definition-of-ux-impacting-changes "Direct link to Definition of UX-impacting changes")

UX-impacting changes are ones which impact how the user directly interacts with, consumes, or perceives the product.

**Examples**:

1. Public-facing documentation
2. Input configuration
3. Output schema
4. Prerequisite configuration by the user (e.g: you need to link an instagram account to your Facebook page for this connector to work properly)
5. Consolidating two connectors into one, or splitting one connector into two
6. Wait time for human-at-keyboard
7. Anything that negatively impacts the runtime of the connector (e.g: a change that makes the runtime go from 10 minutes to 20 minutes on the same data size)
8. Any other change which you deem UX-impacting
   <!-- -->
   1. The guide can’t cover everything, so this is an escape hatch based on the developer’s judgment.

**Examples of UX-impacting changes**:

1. Adding or removing an input field to/from spec.json
2. Adding or removing fields from the output schema
3. Adding a new stream or category of stream (e.g: supporting views in databases)
4. Adding OAuth support

**Examples of non-UX-impacting changes**:

1. Refactoring without changing functionality
2. Bugfix (e.g: pagination doesn’t work correctly)

### Guiding Principles[​](#guiding-principles "Direct link to Guiding Principles")

Would you trust AWS or Docker if it only worked 70, 80, or 90% of the time or if it leaked your business secrets? Yeah, me neither. You would only build on a tool if it worked at least 99% of the time. Infrastructure should give you back your time, rather than become a debugging timesink.

The same is true with Airbyte: if it worked less than 99% of the time, many users will stop using it. Airbyte is an infrastructure component within a user’s data pipeline. Our users’ goal is to move data; Airbyte is an implementation detail. In that sense, it is much closer to Terraform, Docker, or AWS than an end application.

#### Trust & Reliability are the top concerns[​](#trust--reliability-are-the-top-concerns "Direct link to Trust & Reliability are the top concerns")

Our users have the following hierarchy of needs:

![](/assets/images/ux_hierarchy_pyramid2-969ec27c9a44e3daa11fcff4e94bf2a8.png)

**Security**

Users often move very confidential data like revenue numbers, salaries, or confidential documents through Airbyte. A user therefore must trust that their data is secure. This means no leaking credentials in logs or plain text, no vulnerabilities in the product, no frivolous sharing of credentials or data over internal slack channels, video calls, or other communications etc.

**Data integrity**

Data replicated by Airbyte must be correct and complete. If a user moves data with Airbyte, then all of the data must be present, and it must all be correct - no corruption, incorrect values, or wrongly formatted data.

Some tricky examples which can break data integrity if not handled correctly:

* Zipcodes for the US east coast should not lose their leading zeros because of being detected as integer
* Database timezones could affect the value of timestamps
* Esoteric text values (e.g: weird UTF characters)

**Reliability**

A connector needs to be reliable. Otherwise, a user will need to spend a lot of time debugging, and at that point, they’re better off using a competing product. The connector should be able to handle large inputs, weirdly formatted inputs, all data types, and basically anything a user should throw at it.

In other words, a connector should work 100% of the time, but 99.9% is occasionally acceptable.

#### Speed[​](#speed "Direct link to Speed")

Sync speed minimizes the time needed for deriving value from data. It also provides a better user experience as it allows quick iteration on connector configurations without suffering through long wait times.

**Ease of use**

People love and trust a product that is easy to use. This means that it works as quickly as possible, introduces no friction, and uses sensible defaults that are good enough for 95% of users.

An important component of usability is predictability. That is, as much as possible, a user should know before running a connector what its output will be and what the different tables will mean.

Ideally, they would even see an ERD describing the output schema they can expect to find in the destination. (This particular feature is tracked [here](https://github.com/airbytehq/airbyte/issues/3731)).

**Feature Set**

Our connectors should cover as many use cases as is feasible. While it may not always work like that given our incremental delivery preference, we should always strive to provide the most featureful connectors which cover as much of the underlying API or database surface as possible.

There is also a tension between featureset and ease of use. The more features are available, the more thought it takes to make the product easy and intuitive to use. We’ll elaborate on this later.

### Airbyte's Target Personas[​](#airbytes-target-personas "Direct link to Airbyte's Target Personas")

Without repeating too many details mentioned elsewhere, the important thing to know is Airbyte serves all the following personas:

| **Persona**        | **Level of technical knowledge**                                                                                                                                                                                                                                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Analyst       | Proficient with:<br /><br />Data manipulation tools like Excel or SQL<br />Dashboard tools like Looker<br /><br />Not very familiar with reading API docs and doesn't know what a curl request is. But might be able to generate an API key if you tell them exactly how.                                                               |
| Analytics Engineer | Proficient with:<br /><br />SQL & DBT<br />Git<br />A scripting language like Python<br />Shallow familiarity with infra tools like Docker<br /><br />Much more technical than a data analyst, but not as much as a data engineer                                                                                                       |
| Data Engineer      | Proficient with:<br /><br />SQL & DBT<br />Git<br />2 or more programming languages<br />Infra tools like Docker or Kubernetes<br />Cloud technologies like AWS or GCP<br />Building or consuming APIs<br />orhestartion tools like Airflow<br /><br />The most technical persona we serve. Think of them like an engineer on your team |

Keep in mind that the distribution of served personas will differ per connector. Data analysts are highly unlikely to form the majority of users for a very technical connector like say, Kafka.

## Specific Guidelines[​](#specific-guidelines "Direct link to Specific Guidelines")

### Input Configuration[​](#input-configuration "Direct link to Input Configuration")

*aka spec.json*

**Avoid configuration completely when possible**

Configuration means more work for the user and more chances for confusion, friction, or misconfiguration. If I could wave a magic wand, a user wouldn’t have to configure anything at all. Unfortunately, this is not reality, and some configuration is strictly required. When this is the case, follow the guidelines below.

**Avoid exposing implementation details in configuration**

If a configuration controls an implementation detail (like how many retries a connector should make before failing), then there should be almost no reason to expose this. If you feel a need to expose it, consider it might be a smell that the connector implementation is not robust.

Put another way, if a configuration tells the user how to do its job of syncing data rather than what job to achieve, it’s a code smell.

For example, the memory requirements for a database connector which syncs a table with very wide rows (50mb rows) can be very different than when syncing a table with very narrow rows (10kb per row). In this case, it may be acceptable to ask the user for some sort of “hint”/tuning parameter in configuration (hidden behind advanced configuration) to ensure the connector performs reliably or quickly. But even then, this option would strictly be a necessary evil/escape hatch. It is much more preferable for the connector to auto-detect what this setting should be and never need to bother the user with it.

**Minimize required configurations by setting defaults whenever possible**

In many cases, a configuration can be avoided by setting a default value for it but still making it possible to set other values. Whenever possible, follow this pattern.

**Hide technical or niche parameters under an “Advanced” section**

Sometimes, it’s inevitable that we need to expose some advanced or technical configuration. For example, the option to upload a TLS certificate to connect to a database, or the option to configure the number of retries done by an API connector: while these may be useful to some small percentage of users, it’s not worth making all users think or get confused about them.

Note: this is currently blocked by this [issue](https://github.com/airbytehq/airbyte/issues/3681).

**Add a “title” and “description” property for every input parameter**

This displays this information to the user in a polished way and gives less technical users (e.g: analysts) confidence that they can use this product. Be specific and unambiguous in the wording, explaining more than just the field name alone provides.

For example, the following spec:

```
{
  "type": "object",
  "properties": {
    "user_name": {
      "type": "string"
    }
  }
}
```

produces the following input field in the UI:

![](data:image/png;base64,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)

Whereas the following specification:

```
{
  "type": "object",
  "properties": {
    "user_name": {
      "type": "string",
      "description": "The username you use to login to the database",
      "title": "Username"
    }
  }
}
```

produces the following UI:

![](/assets/images/ux_username_good-ee29f5600754abe6aaa6418879cca9bd.png)

The title should use Pascal Case “with spaces” e.g: “Attribution Lookback Window”, “Host URL”, etc...

**Clearly document the meaning and impact of all parameters**

All configurations must have an unmistakable explanation describing their purpose and impact, even the obvious ones. Remember, something that is obvious to an analyst may not be obvious to an engineer, and vice-versa.

For example, in some Ads APIs like Facebook, the user’s data may continue to be updated up to 28 days after it is created. This happens because a user may take action because of an ad (like buying a product) many days after they see the ad. In this case, the user may want to configure a “lookback” window for attributing.

Adding a parameter “attribution\_lookback\_window” with no explanation might confuse the user more than it helps them. Instead, we should add a clear title and description which describes what this parameter is and how different values will impact the data output by the connector.

**Document how users can obtain configuration parameters**

If a user needs to obtain an API key or host name, tell them exactly where to find it. Ideally you would show them screenshots, though include a date and API version in those if possible, so it’s clear when they’ve aged out of date.

**Links should point to page anchors where applicable**.

Often, you are trying to redirect the user to a specific part of the page. For example, if you wanted to point someone to the "Input Configuration" section of this doc, it is better to point them to `https://docs.airbyte.com/connector-development/ux-handbook#input-configuration` instead of `https://docs.airbyte.com/connector-development/ux-handbook`.

**Fail fast & actionably**

A user should not be able to configure something that will not work. If a user’s configuration is invalid, we should inform them as precisely as possible about what they need to do to fix the issue.

One helpful aid is to use the json-schema “pattern” keyword to accept inputs which adhere to the correct input shape.

### Output Data & Schemas[​](#output-data--schemas "Direct link to Output Data & Schemas")

#### Strongly Favor ELT over ETL[​](#strongly-favor-elt-over-etl "Direct link to Strongly Favor ELT over ETL")

Extract-Load-Transform (ELT) means extracting and loading the data into a destination while leaving its format/schema as unchanged as possible, and making transformation the responsibility of the consumer. By contrast, ETL means transforming data before it is sent to the destination, for example changing its schema to make it easier to consume in the destination.

When extracting data, strongly prefer ELT to ETL for the following reasons:

**Removes Airbyte as a development bottleneck**

If we get into the habit of structuring the output of each source according to how some users want to use it, then we will invite more feature requests from users asking us to transform data in a particular way. This introduces Airbyte’s dev team as an unnecessary bottleneck for these users.

Instead, we should set the standard that a user should be responsible for transformations once they’ve loaded data in a destination.

**Will always be backwards compatible**

APIs already follow strong conventions to maintain backwards compatibility. By transforming data, we break this guarantee, which means we may break downstream flows for our users.

**Future proof**

We may have a vision of what a user needs today. But if our persona evolves next year, then we’ll probably also need to adapt our transformation logic, which would require significant dev and data migration efforts.

**More flexible**

Current users have different needs from data. By being opinionated on how they should consume data, we are effectively favoring one user persona over the other. While there might be some cases where this is warranted, it should be done with extreme intentionality.

**More efficient**

With ETL, if the “T” ever needs to change, then we need to re-extract all data for all users. This is computationally and financially expensive and will place a lot of pressure on the source systems as we re-extract all data.

#### Describe output schemas as completely and reliably as possible[​](#describe-output-schemas-as-completely-and-reliably-as-possible "Direct link to Describe output schemas as completely and reliably as possible")

Our most popular destinations are strongly typed like Postgres, BigQuery, or Parquet & Avro.

Being strongly typed enables optimizations and syntactic sugar to make it very easy & performant for the user to query data.

To provide the best UX when moving data to these destinations, Airbyte source connectors should describe their schema in as much detail as correctness allows.

In some cases, describing schemas is impossible to do reliably. For example, MongoDB doesn’t have any schemas. To infer the schema, one needs to read all the records in a particular table. And even then, once new records are added, they also must all be read in order to update the inferred schema. At the time of writing, this is infeasible to do performantly in Airbyte since we do not have an intermediate staging area to do this. In this case, we should do the “best we can” to describe the schema, keeping in mind that reliability of the described schema is more important than expressiveness.

That is, we would rather not describe a schema at all than describe it incorrectly, as incorrect descriptions **will** lead to failures downstream.

To keep schema descriptions reliable, [automate schema generation](https://docs.airbyte.com/connector-development/cdk-python/schemas#generating-schemas-from-openapi-definitions) whenever possible.

#### Be very cautious about breaking changes to output schemas[​](#be-very-cautious-about-breaking-changes-to-output-schemas "Direct link to Be very cautious about breaking changes to output schemas")

Assuming we follow ELT over ETL, and automate generation of output schemas, this should come up very rarely. However, it is still important enough to warrant mention.

If for any reason we need to change the output schema declared by a connector in a backwards breaking way, consider it a necessary evil that should be avoided if possible. Basically, the only reasons for a backwards breaking change should be:

* a connector previously had an incorrect schema, or
* It was not following ELT principles and is now being changed to follow them

Other breaking changes should probably be escalated for approval.

### Prerequisite Configurations & assumptions[​](#prerequisite-configurations--assumptions "Direct link to Prerequisite Configurations & assumptions")

**Document all assumptions**

If a connector makes assumptions about the underlying data source, then these assumptions must be documented. For example: for some features of the Facebook Pages connector to work, a user must have an Instagram Business account linked to an Instagram page linked to their Facebook Page. In this case, the externally facing documentation page for the connector must be very clear about this.

**Provide how-tos for prerequisite configuration**

If a user needs to set up their data source in a particular way to pull data, then we must provide documentation for how they should do it.

For example, to set up CDC for databases, a user must create logical replication slots and do a few other things. These steps should be documented with examples or screenshots wherever possible (e.g: here are the SQL statements you need to run, with the following permissions, on the following screen, etc.)

### External Documentation[​](#external-documentation "Direct link to External Documentation")

This section is concerned with the external-facing documentation of a connector that goes in <https://docs.airbyte.com> e.g: [this one](https://docs.airbyte.com/integrations/sources/amazon-seller-partner)

**Documentation should communicate persona-impacting behaviors**

When writing documentation ask: who is the intended target persona for a piece of documentation, and what information do they need to understand how this connector impacts their workflows?

For example, data analysts & analytics engineers probably don’t care if we use Debezium for database replication. To them, the important thing is that we provide Change Data Capture (CDC) -- Debezium is an implementation detail. Therefore, when communicating information about our database replication logic, we should emphasize the end behaviors, rather than implementation details.

**Example**: Don’t say: “Debezium cannot process UTF-16 character set“.

Instead, say: “When using CDC, UTF-16 characters are not currently supported”

A user who doesn’t already know what Debezium is might be left confused by the first phrasing, so we should use the second phrasing.

\*: *this is a fake example. AFAIK there is no such limitation in Debezi-- I mean, the Postgres connector.*
