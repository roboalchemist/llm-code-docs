# Source: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/llms.txt

# Amazon Augmented AI API Reference

> Amazon Augmented AI (Amazon A2I) adds the benefit of human judgment to any machine learning application. When an AI application can't evaluate data with a high degree of confidence, human reviewers can take over. This human review is called a human review workflow. To create and start a human review workflow, you need three resources: a worker task template, a flow definition, and a human loop.

- [Welcome](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_Operations.html)

- [DeleteHumanLoop](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_DeleteHumanLoop.html): Deletes the specified human loop for a flow definition.
- [DescribeHumanLoop](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_DescribeHumanLoop.html): Returns information about the specified human loop.
- [ListHumanLoops](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_ListHumanLoops.html): Returns information about human loops, given the specified parameters.
- [StartHumanLoop](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_StartHumanLoop.html): Starts a human loop, provided that at least one activation condition is met.
- [StopHumanLoop](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_StopHumanLoop.html): Stops the specified human loop.


## [Data Types](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_Types.html)

- [HumanLoopDataAttributes](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_HumanLoopDataAttributes.html): Attributes of the data specified by the customer.
- [HumanLoopInput](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_HumanLoopInput.html): An object containing the human loop input in JSON format.
- [HumanLoopOutput](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_HumanLoopOutput.html): Information about where the human output will be stored.
- [HumanLoopSummary](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_HumanLoopSummary.html): Summary information about the human loop.
