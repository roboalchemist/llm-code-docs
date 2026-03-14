# Source: https://docs.statsig.com/statsig-warehouse-native/configuration/assignment-sources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Assignment Sources

Assignment Sources are how you schematize your assignment data for Statsig, and they serve as the input data for determining who is in an experiment, and which treatment they got.

## Creating an Assignment Source

To create an assignment source, go to the data tab in Statsig and go to the Assignment Sources pane.

An Assignment Source is defined as a SQL query and a mapping of the output columns to specific fields
Statsig requires (user identifiers, a `timestamp`, an experiment identifier, and a group identifier).

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/assignment-sources/264100295-05d71c64-9b31-4531-b371-03b6cb692446.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=8d32bd4faa786753d13f28c49a10790f" alt="Assignment Source" width="1103" height="1133" data-path="images/statsig-warehouse-native/configuration/assignment-sources/264100295-05d71c64-9b31-4531-b371-03b6cb692446.png" />
</Frame>

## Scanning Assignment Sources

Statsig scans assignment sources on-demand and/or on a schedule to find experiment data. These jobs are very quick and identify unique groups, the ID types present in the experiment, and the estimated of users per group.

Once the scan is complete, you can view and create experiments from the Assignment source. The assignment's experience will also populate the Experiment creation flow after the scan completes.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/assignment-sources/87fac269-75bc-4a65-a660-339486605e24.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=8600effb9771b16a65155eae2790bba3" alt="Assignment source scan results showing detected experiments" width="1500" height="536" data-path="images/statsig-warehouse-native/configuration/assignment-sources/87fac269-75bc-4a65-a660-339486605e24.png" />
</Frame>

## Manage Assignment Sources

In the Assignment Source tab, you can see your Assignment sources and the experiments they're being used in.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/assignment-sources/264100297-c41cd747-089c-4ccf-8b45-b70a1b4e264a.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=5e88a2454f7295b11a2851466e7f3881" alt="Assignment Source Tab" width="1504" height="460" data-path="images/statsig-warehouse-native/configuration/assignment-sources/264100297-c41cd747-089c-4ccf-8b45-b70a1b4e264a.png" />
</Frame>

## Example Data

For experiment assignment sources, Statsig requires information on who was exposed, when, and to what experiment:

| Column Type            | Description                                                                               | Format/Rules                   |
| ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------ |
| timestamp              | **Required** an identifier of when the experiment exposure occurred                       | Castable to Timestamp/Date     |
| unit identifier        | **Required** at least one entity to which this metric belongs                             | Generally a user ID or similar |
| experiment identifier  | **Required** the experiment the exposure was for                                          | Usually an experiment name     |
| group identifier       | **Required** the experimental variant the user was assigned to                            | Usually a group name           |
| additional identifiers | *Optional* Entity identifiers for reuse across identifier types                           |                                |
| context columns        | *Optional* Fields which can be used to group by and filter results in exploratory queries |                                |

For example, you could pull from exposure event logging directly:

| timestamp           | user\_id        | company\_id | experiment\_name    | group\_name | country |
| ------------------- | --------------- | ----------- | ------------------- | ----------- | ------- |
| 2023-10-10 00:01:01 | my\_user\_17503 | c\_22235455 | ranking\_v1\_vs\_v2 | v1          | US      |
| 2023-10-10 00:02:15 | my\_user\_18821 | c\_22235455 | ranking\_v1\_vs\_v2 | v2          | CA      |
| 2023-10-10 00:02:22 | my\_user\_18821 | c\_22235455 | search UI revamp    | control     | CA      |


Built with [Mintlify](https://mintlify.com).