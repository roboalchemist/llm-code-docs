# Source: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/llms.txt

# AWS Elemental Inference API Reference

> This is the AWS Elemental Inference REST API Reference. It provides information on the URL, request contents, and response contents of each AWS Elemental Inference REST operation.

- [Welcome](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_Operations.html)

- [AssociateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_AssociateFeed.html): Associates a resource with the feed.
- [CreateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateFeed.html): Creates a feed.
- [DeleteFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DeleteFeed.html): Deletes the specified feed.
- [DisassociateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DisassociateFeed.html): Releases the resource (for example, an MediaLive channel) that is associated with this feed.
- [GetFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFeed.html): Retrieves information about the specified feed.
- [ListFeeds](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListFeeds.html): Displays a list of feeds that belong to this AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListTagsForResource.html): List all tags that are on an Elemental Inference resource in the current region.
- [TagResource](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_TagResource.html): Associates the specified tags to the resource identified by the specified resourceArn in the current region.
- [UntagResource](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UntagResource.html): Deletes specified tags from the specified resource in the current region.
- [UpdateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateFeed.html): Updates the name and/or outputs in a feed.


## [Data Types](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_Types.html)

- [ClippingConfig](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ClippingConfig.html): A type of OutputConfig, used when the output in a feed is for the clip feature.
- [CreateOutput](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateOutput.html): Contains configuration information about one output in a feed.
- [CroppingConfig](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CroppingConfig.html): A type of OutputConfig, used when the output in a feed is for the crop feature.
- [FeedAssociation](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_FeedAssociation.html): Contains information about the resource that is associated with a feed.
- [FeedSummary](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_FeedSummary.html): Contains configuration information about a feed.
- [GetOutput](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetOutput.html): Contains configuration information about one output in a feed.
- [OutputConfig](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_OutputConfig.html): Contains one typed output.
- [UpdateOutput](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateOutput.html): Contains configuration information about one output in a feed.
