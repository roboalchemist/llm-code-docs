# Source: https://docs.aws.amazon.com/dcv/latest/sm-dev/llms.txt

# Amazon DCV Session Manager Developer Guide

- [What is Session Manager?](https://docs.aws.amazon.com/dcv/latest/sm-dev/what-is-sm.html)
- [Release Notes and Document History](https://docs.aws.amazon.com/dcv/latest/sm-dev/doc-history-release-notes.html)

## [Getting started with Session Manager API](https://docs.aws.amazon.com/dcv/latest/sm-dev/getting-started.html)

- [Step 1: Generate your API client](https://docs.aws.amazon.com/dcv/latest/sm-dev/client-sdk.html): The Session Manager APIs are defined in a single YAML file.
- [Step 2: Register your client API](https://docs.aws.amazon.com/dcv/latest/sm-dev/credentials.html): API requests use an access token to verify your credentials.
- [Step 3: Get an access token and make an API request](https://docs.aws.amazon.com/dcv/latest/sm-dev/request.html): This example will walk through the steps to get your access token set up, then show you how to make a basic API request.


## [Session Manager API reference](https://docs.aws.amazon.com/dcv/latest/sm-dev/reference.html)

- [CloseServers](https://docs.aws.amazon.com/dcv/latest/sm-dev/CloseServers.html): Closes one or more Amazon DCV servers.
- [CreateSessions](https://docs.aws.amazon.com/dcv/latest/sm-dev/CreateSessions.html): Creates a new Amazon DCV session with the specified details.
- [DescribeServers](https://docs.aws.amazon.com/dcv/latest/sm-dev/DescribeServers.html): Describes one or more Amazon DCV servers.
- [DescribeSessions](https://docs.aws.amazon.com/dcv/latest/sm-dev/DescribeSessions.html): Describes one or more Amazon DCV sessions.
- [DeleteSessions](https://docs.aws.amazon.com/dcv/latest/sm-dev/DeleteSessions.html): Deletes the specified Amazon DCV session and removes it from the Broker's cache.
- [GetSessionConnectionData](https://docs.aws.amazon.com/dcv/latest/sm-dev/GetSessionConnectionData.html): Gets connection information for a specific user's connection to a specific Amazon DCV session.
- [GetSessionScreenshots](https://docs.aws.amazon.com/dcv/latest/sm-dev/GetSessionScreenshots.html): Gets screenshots of one or more Amazon DCV sessions.
- [OpenServers](https://docs.aws.amazon.com/dcv/latest/sm-dev/OpenServers.html): Opens one or more Amazon DCV servers.
- [UpdateSessionPermissions](https://docs.aws.amazon.com/dcv/latest/sm-dev/UpdateSessionPermissions.html): Updates the user permissions for a specific Amazon DCV session.
