# Source: https://docs.aws.amazon.com/OAM/latest/APIReference/llms.txt

# Amazon CloudWatch Observability Access Manager API Reference

> Use Amazon CloudWatch Observability Access Manager to create and manage links between source accounts and monitoring accounts by using CloudWatch cross-account observability. With CloudWatch cross-account observability, you can monitor and troubleshoot applications that span multiple accounts within a Region. Seamlessly search, visualize, and analyze your metrics, logs, traces, Application Signals services and service level objectives (SLOs), Application Insights applications, and internet monitors in any of the linked accounts without account boundaries.

- [Welcome](https://docs.aws.amazon.com/OAM/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/OAM/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/OAM/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/OAM/latest/APIReference/API_Operations.html)

- [CreateLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateLink.html): Creates a link between a source account and a sink that you have created in a monitoring account.
- [CreateSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html): Use this to create a sink in the current account, so that it can be used as a monitoring account in CloudWatch cross-account observability.
- [DeleteLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteLink.html): Deletes a link between a monitoring account sink and a source account.
- [DeleteSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteSink.html): Deletes a sink.
- [GetLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetLink.html): Returns complete information about one link.
- [GetSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSink.html): Returns complete information about one monitoring account sink.
- [GetSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSinkPolicy.html): Returns the current sink policy attached to this sink.
- [ListAttachedLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html): Returns a list of source account links that are linked to this monitoring account sink.
- [ListLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html): Use this operation in a source account to return a list of links to monitoring account sinks that this source account has.
- [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html): Use this operation in a monitoring account to return the list of sinks created in that account.
- [ListTagsForResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListTagsForResource.html): Displays the tags associated with a resource.
- [PutSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html): Creates or updates the resource policy that grants permissions to source accounts to link to the monitoring account sink.
- [TagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified resource.
- [UpdateLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UpdateLink.html): Use this operation to change what types of data are shared from a source account to its linked monitoring account sink.


## [Data Types](https://docs.aws.amazon.com/OAM/latest/APIReference/API_Types.html)

- [LinkConfiguration](https://docs.aws.amazon.com/OAM/latest/APIReference/API_LinkConfiguration.html): Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.
- [ListAttachedLinksItem](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinksItem.html): A structure that contains information about one link attached to this monitoring account sink.
- [ListLinksItem](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinksItem.html): A structure that contains information about one of this source account's links to a monitoring account.
- [ListSinksItem](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinksItem.html): A structure that contains information about one of this monitoring account's sinks.
- [LogGroupConfiguration](https://docs.aws.amazon.com/OAM/latest/APIReference/API_LogGroupConfiguration.html): This structure contains the Filter parameter which you can use to specify which log groups are to share log events from this source account to the monitoring account.
- [MetricConfiguration](https://docs.aws.amazon.com/OAM/latest/APIReference/API_MetricConfiguration.html): This structure contains the Filter parameter which you can use to specify which metric namespaces are to be shared from this source account to the monitoring account.
