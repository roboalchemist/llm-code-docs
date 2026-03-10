# Source: https://docs.aws.amazon.com/health/latest/APIReference/llms.txt

# AWS Health API Reference

> Use the AWS Health API to retrieve information about AWS Health events.

- [Welcome](https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/health/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/health/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/health/latest/APIReference/API_Operations.html)

- [DescribeAffectedAccountsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedAccountsForOrganization.html): Returns a list of accounts in the organization from AWS Organizations that are affected by the provided event.
- [DescribeAffectedEntities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html): Returns a list of entities that have been affected by the specified events, based on the specified filter criteria.
- [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html): Returns a list of entities that have been affected by one or more events for one or more accounts in your organization in AWS Organizations, based on the filter criteria.
- [DescribeEntityAggregates](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEntityAggregates.html): Returns the number of entities that are affected by each of the specified events.
- [DescribeEntityAggregatesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEntityAggregatesForOrganization.html): Returns a list of entity aggregates for your AWS Organizations that are affected by each of the specified events.
- [DescribeEventAggregates](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventAggregates.html): Returns the number of events of each event type (issue, scheduled change, and account notification).
- [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html): Returns detailed information about one or more specified events.
- [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html): Returns detailed information about one or more specified events for one or more AWS accounts in your organization.
- [DescribeEvents](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html): Returns information about events that meet the specified filter criteria.
- [DescribeEventsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html): Returns information about events across your organization in AWS Organizations.
- [DescribeEventTypes](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventTypes.html): Returns the event types that meet the specified filter criteria.
- [DescribeHealthServiceStatusForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeHealthServiceStatusForOrganization.html): This operation provides status information on enabling or disabling AWS Health to work with your organization.
- [DisableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DisableHealthServiceAccessForOrganization.html): Disables AWS Health from working with AWS Organizations.
- [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html): Enables AWS Health to work with AWS Organizations.


## [Data Types](https://docs.aws.amazon.com/health/latest/APIReference/API_Types.html)

- [AccountEntityAggregate](https://docs.aws.amazon.com/health/latest/APIReference/API_AccountEntityAggregate.html): The number of entities in an account that are impacted by a specific event aggregated by the entity status codes.
- [AffectedEntity](https://docs.aws.amazon.com/health/latest/APIReference/API_AffectedEntity.html): Information about an entity that is affected by a Health event.
- [DateTimeRange](https://docs.aws.amazon.com/health/latest/APIReference/API_DateTimeRange.html): A range of dates and times that is used by the EventFilter and EntityFilter objects.
- [EntityAccountFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityAccountFilter.html): A JSON set of elements including the awsAccountId, eventArn and a set of statusCodes.
- [EntityAggregate](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityAggregate.html): The number of entities that are affected by one or more events.
- [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html): The values to use to filter results from the DescribeAffectedEntities operation.
- [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html): Summary information about an AWS Health event.
- [EventAccountFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventAccountFilter.html): The values used to filter results from the DescribeEventDetailsForOrganization and DescribeAffectedEntitiesForOrganization operations.
- [EventAggregate](https://docs.aws.amazon.com/health/latest/APIReference/API_EventAggregate.html): The number of events of each issue type.
- [EventDescription](https://docs.aws.amazon.com/health/latest/APIReference/API_EventDescription.html): The detailed description of the event.
- [EventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_EventDetails.html): Detailed information about an event.
- [EventDetailsErrorItem](https://docs.aws.amazon.com/health/latest/APIReference/API_EventDetailsErrorItem.html): Error information returned when a DescribeEventDetails operation can't find a specified event.
- [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html): The values to use to filter results from the DescribeEvents and DescribeEventAggregates operations.
- [EventType](https://docs.aws.amazon.com/health/latest/APIReference/API_EventType.html): Contains the metadata about a type of event that is reported by AWS Health.
- [EventTypeFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventTypeFilter.html): The values to use to filter results from the DescribeEventTypes operation.
- [OrganizationAffectedEntitiesErrorItem](https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationAffectedEntitiesErrorItem.html): Error information returned when a DescribeAffectedEntitiesForOrganization operation can't find or process a specific entity.
- [OrganizationEntityAggregate](https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEntityAggregate.html): The aggregate results of entities affected by the specified event in your organization.
- [OrganizationEvent](https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEvent.html): Summary information about an event, returned by the DescribeEventsForOrganization operation.
- [OrganizationEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEventDetails.html): Detailed information about an event.
- [OrganizationEventDetailsErrorItem](https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEventDetailsErrorItem.html): Error information returned when a DescribeEventDetailsForOrganization operation can't find a specified event.
- [OrganizationEventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEventFilter.html): The values to filter results from the DescribeEventsForOrganization operation.
