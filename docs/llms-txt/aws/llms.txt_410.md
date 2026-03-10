# Source: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/llms.txt

#  FlexMatch Developer Guide

> Learn how to build custom matchmakers using Amazon GameLift ServersÂ FlexMatch. Work with the FlexMatch rules language and algorithm customizations to fine-tune how players are matched into your games. Set up FlexMatch for games that use Amazon GameLift Servers managed hosting, or build a standalone FlexMatch solution to work with other hosting solutions.

- [Security with FlexMatch](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-security.html)
- [Release notes and SDK versions](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-release-notes.html)
- [All Amazon GameLift Servers guides](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-guides.html)

## [What is FlexMatch?](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-intro.html)

### [How FlexMatch works](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/gamelift-match.html)

Learn about how Amazon GameLift ServersÂ FlexMatch uses customizable match rules to match players into games that deliver the best possible multiplayer experience.

- [FlexMatch matchmaking process](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/gamelift-match-howitworks.html): This topic describes the sequence of events in a basic matchmaking scenario, including the interactions between the various your game components and the FlexMatch service.
- [Supported AWS Regions](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-regions.html): Get information about what AWS Regions your can use when deploying Amazon GameLift Servers FlexMatch matchmaking resources for your game.


## [Getting started](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-getting-started.html)

- [Roadmap: Create a standalone matchmaking solution](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-tasks-safm.html): View a step-by-step list of integration tasks to complete when adding Amazon GameLift Servers FlexMatch matchmaking to your game.
- [Roadmap: Add matchmaking to Amazon GameLift Servers hosting](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-tasks.html): View a step-by-step list of integration tasks when adding Amazon GameLift Servers FlexMatch matchmaking to your game.


## [Building a FlexMatch matchmaker](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/matchmaker-build.html)

### [Design a matchmaker](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-configuration.html)

Design an Amazon GameLift Servers FlexMatch matchmaker for your game.

- [Choose a location for the matchmaker](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-configuration-regions.html): Decide where you want matchmaking activity to take place and create your matchmaking configuration and rule set in that location.
- [Add optional elements](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-configuration-options.html): In addition to these minimum requirements, you can configure your matchmaker with the following additional options.

### [Build a rule set](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets.html)

Learn about using rule sets for matchmaking with Amazon GameLift Servers FlexMatch.

### [Design a rule set](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-ruleset.html)

Learn about building matchmaking rules with Amazon GameLift Servers FlexMatch.

- [Describe the rule set (required)](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets-components-set.html): Provide details for the rule set.
- [Customize the match algorithm](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets-components-algorithm.html): FlexMatch optimizes the default algorithm for most games to get players into acceptable matches with minimal wait time.
- [Declare player attributes](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets-components-attributes.html): In this section, list individual player attributes to include in matchmaking requests.
- [Define match teams](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets-components-teams.html): Describe the structure and size of the teams for a match.
- [Set rules for player matching](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets-components-rules.html): Create a set of rule statements that evaluate players for acceptance in to a match.
- [Allow requirements to relax over time](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets-components-expansion.html): Expansions allow you to relax rule criteria over time when FlexMatch can't find a match.

### [Design a large-match rule set](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large.html)

Learn about building large-match rules for use with Amazon GameLift Servers FlexMatch.

- [Customize match algorithm for large matches](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large-algorithm.html): Add an algorithm component to the rule set, if one doesn't already exist.
- [Declare player attributes](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large-attributes.html): Make sure that you declare the player attribute that is used as a balancing attribute in the rule set algorithm.
- [Define teams](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large-teams.html): The process of defining team size and structure is the same as with small matches, but the way FlexMatch fills the teams is different.
- [Set rules for large matches](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large-rule.html): Matchmaking for large matches relies primarily on the balancing strategy and latency batching optimizations.
- [Relax large match requirements](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large-relax.html): As with small matches, you can use expansions to relax match requirements over time when no valid matches are possible.
- [Tutorial: Create a rule set](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-create-ruleset.html): Create custom rule sets with Amazon GameLift Servers FlexMatch to find the best player matches for your game.

### [Rule set examples](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples.html)

Copy and adapt elements from these FlexMatch rule set examples that cover a variety of matchmaking scenarios.

- [Example: Create two teams with evenly matched players](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-1.html): This example illustrates how to set up two equally matched teams of players with the following instructions.
- [Example: Create uneven teams (Hunters vs Monster)](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-2.html): This example describes a game mode in which a group of players hunt a single monster.
- [Example: Set team-level requirements and latency limits](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-3.html): This example illustrates how to set up player teams and apply a set of rules to each team instead of each individual player.
- [Example: Use explicit sorting to find best matches](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-4.html): This example sets up a simple match with two teams of three players.
- [Example: Find intersections across multiple player attributes](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-5.html): This example illustrates how to use a collection rule to find intersections in two or more player attributes.
- [Example: Compare attributes across all players](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-6.html): This example illustrates how to compare player attributes across a group of players.
- [Example: Create a large match](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-7.html): This example illustrates how to set up a rule set for matches that can exceed 40 players.
- [Example: Create a multi-team large match](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-8.html): This example illustrates how to set up a rule set for matches with multiple teams that can exceed 40 players.
- [Example: Create a large match with players with similar attributes](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-9.html): This example illustrates how to set up a rule set for matches with two teams using batchDistance.
- [Example: Use a compound rule to create a match with players with similar attributes or similar selections](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-10.html): This example illustrates how to set up a rule set for matches with two teams using compound.
- [Example: Create a rule that uses a player's block list](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-11.html): This example illustrates a rule set that lets players avoid being matched with certain other players.

### [Create a matchmaking configuration](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-create-configuration.html)

Create a new matchmaking configuration for use with Amazon GameLift Servers FlexMatch.

- [Tutorial: Create a matchmaker for hosting](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-create-configuration-withqueue.html): Before creating a matchmaking configuration, create a rule set and an Amazon GameLift Servers game session queue to use with the matchmaker.
- [Tutorial: Create a matchmaker for standalone FlexMatch](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-create-configuration-standalone.html): Before creating a matchmaking configuration, create a rule set to use with the matchmaker.
- [Tutorial: Edit a matchmaking configuration](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-create-configuration-edit.html): To edit a matchmaking configuration, choose Matchmaking configurations from the navigation bar and choose the configuration you want to edit.

### [Set up event notifications](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-notification.html)

Learn how to set up notifications for your Amazon GameLift Servers matchmaking activities.

- [Tutorial: Set up an Amazon SNS topic](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-notification-sns.html): You can have Amazon GameLift Servers publish all events that a FlexMatch matchmaker generates to an Amazon SNS topic.
- [Set up an SNS topic with server-side encryption](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/queue-notification-sns-sse.html): You can use server-side encryption (SSE) to store sensitive data in encrypted topics.
- [Configure a topic subscription to invoke a Lambda function](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-notification-lambda.html): You can invoke a Lambda function using event notifications published to your Amazon SNS topic.


## [Preparing games for FlexMatch](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-integration-intro.html)

### [Add FlexMatch to a game client](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-client.html)

Learn how to request matchmaking for your players with Amazon GameLift Servers FlexMatch.

- [Request matchmaking for players](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-client-start.html): Add code to your game backend service to manage matchmaking requests to a FlexMatch matchmaker.
- [Track matchmaking events](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-client-track.html): Set up notifications to track events that Amazon GameLift Servers emits for matchmaking processes.
- [Request player acceptance](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-client-accept.html): If you're using a matchmaker that has player acceptance turned on, add code to your client service to manage the player acceptance process.
- [Connect to a match](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-client-connect.html): Add code to your client service to handle a successfully formed match (status COMPLETED or event MatchmakingSucceeded).
- [Sample matchmaking requests](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-client-sample.html): The following code snippets build matchmaking requests for several different matchmakers.

### [Add FlexMatch to a game server](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-server.html)

Enable your game server to start game sessions for games created with FlexMatch.

- [Set up a game server for FlexMatch](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-server-setup.html): Game servers that are hosted with Amazon GameLift Servers must be integrated with the Amazon GameLift Servers server SDK and have core functionality as described in Add Amazon GameLift Servers to your game server.


## [Backfill existing games](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-backfill.html)

- [Turn on automatic backfill](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-backfill-auto.html): With automatic match backfill, Amazon GameLift Servers automatically triggers a backfill request whenever a game session starts with one or more unfilled player slots.
- [Generate manual backfill requests from a game server](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-backfill-server.html): You can manually initiate match backfill requests from the game server process that is hosting the game session.
- [Generate manual backfill requests from a backend service](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-backfill-client.html): As an alternative to sending backfill requests from a game server, you may want to send them from a client-side game service.
- [Update match data on the game server](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-backfill-server-data.html): No matter how you initiate match backfill requests in your game, your game server must be able to handle the game session updates that Amazon GameLift Servers delivers as a result of match backfill requests.


## [FlexMatch reference](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/reference-flexmatch.html)

- [FlexMatch API reference (AWS SDK)](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/reference-awssdk-flex.html): View a task-based listing of Amazon GameLift Servers FlexMatch Service API actions in the AWS SDK.

### [Rules language](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rules-reference.html)

Look up rules language and syntax for Amazon GameLift Servers FlexMatch.

### [Rule set schema](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-ruleset-schema.html)

Look up schema elements for an Amazon GameLift Servers FlexMatch rule set.

- [Rule set schema for large matches](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-ruleset-schema-large.html): The following schema documents all possible properties and allowed values for a rule set that is used to build matches of greater than 40 players.
- [Rule set property definitions](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-ruleset-property-definitions.html): Look up property definitions for an Amazon GameLift Servers FlexMatch rule set.
- [Rule types](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rules-reference-ruletype.html): Look up the syntax for FlexMatch rule types.
- [Property expressions](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rules-reference-property-expression.html): Look up the syntax for Amazon GameLift Servers FlexMatch property expressions.

### [Matchmaking events](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events.html)

Vew examples of matchmaking event types that are emitted by Amazon GameLift Servers FlexMatch.

- [MatchmakingSearching](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-matchmakingsearching.html): Ticket has been entered into matchmaking.
- [PotentialMatchCreated](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-potentialmatchcreated.html): A potential match has been created.
- [AcceptMatch](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-acceptmatch.html): Players have accepted a potential match.
- [AcceptMatchCompleted](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-acceptmatchcompleted.html): Match acceptance is complete due to player acceptance, player rejection, or acceptance timeout.
- [MatchmakingSucceeded](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-matchmakingsucceeded.html): Matchmaking has successfully completed and a game session has been created.
- [MatchmakingTimedOut](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-matchmakingtimedout.html): Matchmaking ticket has failed by timing out.
- [MatchmakingCancelled](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-matchmakingcancelled.html): Matchmaking ticket has been canceled due to StopMatchmaking API call.
- [MatchmakingFailed](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-events-matchmakingfailed.html): Matchmaking ticket has encountered an error.
