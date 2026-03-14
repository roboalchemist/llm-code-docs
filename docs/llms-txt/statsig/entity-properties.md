# Source: https://docs.statsig.com/statsig-warehouse-native/configuration/entity-properties.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Entity Properties

> Entity Properties are categorical details about an entity (e.g. a user) in an experiment, which you can use across all experiments to filter or group experiment results in the Explore section. Create these at Data -> Entity Properties.

You can either provide additional detail about an entity that doesn't typically change (e.g. a user's home country), or a property that may change as part of an experiment (e.g. Subscriber Status : True/False). For the latter, you provide a timestamp field which will be used to identify most recent value prior to the user's exposure. This prevents imbalanced groups and biased results from when an experimental treatment impacts the property, for example if it increased the subscription rate.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/entity-properties/7fcac725-54b4-46be-bb68-52fcc308fe5f.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=34e947fb739dbe9f5e2a4fce87533183" alt="Entity Properties configuration interface" width="2257" height="1622" data-path="images/statsig-warehouse-native/configuration/entity-properties/7fcac725-54b4-46be-bb68-52fcc308fe5f.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/entity-properties/6c151cf4-d343-4750-8bfd-a6d48afd6e10.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=32c7fc3cb168bf8109606548c24c07c0" alt="Entity Properties setup screen with timestamp configuration" width="2220" height="1114" data-path="images/statsig-warehouse-native/configuration/entity-properties/6c151cf4-d343-4750-8bfd-a6d48afd6e10.png" />
</Frame>

## Example Data

For property sources, Statsig only needs a user\_id and property fields. Property sources can define **fixed** properties (e.g. a users Country of origin), but can also define **dynamic**
in which case you need to provide a timestamp for Statsig to identify the most recent pre-exposure record.

| Column Type      | Description                                                                                 | Format/Rules                   |
| ---------------- | ------------------------------------------------------------------------------------------- | ------------------------------ |
| timestamp        | *Optional* an identifier of when the property was defined. Required for dynamic properties  | Castable to Timestamp/Date     |
| unit identifier  | **Required** At least one entity to which this metric belongs                               | Generally a user ID or similar |
| property columns | **Required** Fields which can be used to group by and filter results in exploratory queries |                                |

For example, a static property source could just be:

| user\_id        | company\_id | country |
| --------------- | ----------- | ------- |
| my\_user\_17503 | c\_22235455 | US      |
| my\_user\_18821 | c\_22235455 | CA      |

Which could be used to filter and group by any experiment that was exposed one either user\_id or company\_id.

For a dynamic property, it might look like this:

| user\_id        | timestamp  | company\_id | intent\_segment | spend\_segment |
| --------------- | ---------- | ----------- | --------------- | -------------- |
| my\_user\_17503 | 2023-10-10 | c\_22235455 | high\_intent    | high           |
| my\_user\_17503 | 2023-10-11 | c\_22235455 | high\_intent    | high           |
| my\_user\_17503 | 2023-10-12 | c\_22235455 | mid\_intent     | high           |
| my\_user\_18821 | 2023-10-10 | c\_22235455 | low\_intent     | low            |
| my\_user\_18821 | 2023-10-11 | c\_22235455 | low\_intent     | mid            |
| my\_user\_18821 | 2023-10-12 | c\_22235455 | low\_intent     | mid            |

The first user in this example has their intent\_segment property change on `2023-10-12`; based on what the intent\_segment was prior to their exposure, they might have different intent\_segment values for different experiment analyses.


Built with [Mintlify](https://mintlify.com).