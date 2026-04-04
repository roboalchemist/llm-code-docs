# Source: https://docs.getint.io/getting-started-with-the-platform/about-getint-concepts/what-are-runs.md

# What are Runs?

### Initiating Synchronization

A Run occurs when Getint sends API requests to connected collaboration tools. These requests aim to gather data on all newly created items and their respective fields, as well as any recent updates, as defined in the integration setup.

### How Run Intervals Affect Your Integration

Integrations execute sequentially, meaning each one must finish before the next can begin. This sequence is essential for understanding how often integrations can run.

For example, Jira Cloud users can set a minimum run interval of 3 minutes, while Data Center customers have a range between 60 to 120 seconds (primarily 120 seconds). However, On-Premise users can set run intervals starting from 0 seconds.

When setting an interval for integration (like every 15 seconds), remember that this doesn't guarantee the integration will occur exactly at that interval. The actual frequency depends on various factors, such as the total number of integrations and the time each one takes to complete.

### Detection and Integration of Changes

Getint actively searches for new items or changes in existing items during a Run. Detected changes are then integrated, ensuring data across the tools remains synchronized and current.

### Handling Concurrent Changes

Getint effectively merges data when changes occur simultaneously in the same field across integrated tools. This merging mechanism is crucial for preserving all updates and preventing data loss.

### Recording and Logging of Runs

Every Run is meticulously recorded and logged within Getint. This means that users have the ability to review and analyze the actions taken during each Run.

The logs provide valuable insights into the outcomes of each synchronization process. They are an essential tool for users to easily identify and understand any errors or discrepancies that may occur.

### Ensuring Data Integrity and Continuity

Regular Runs are essential for maintaining data integrity and continuity across different platforms. They ensure that all integrated systems reflect the latest and most accurate data.

In summary, a Run in Getint is not only a process of querying and integrating data but also involves a comprehensive recording and logging mechanism. This feature allows users to monitor, analyze, and troubleshoot the synchronization process, ensuring transparency and control over data integration across their collaboration tools.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
