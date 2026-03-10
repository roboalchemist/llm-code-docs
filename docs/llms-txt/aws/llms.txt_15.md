# Source: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/llms.txt

# Amazon Simple Queue Service API Reference

> Welcome to the Amazon SQS API Reference.

- [Welcome](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Operations.html)

- [AddPermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_AddPermission.html): Adds a permission to a queue for a specific principal.
- [CancelMessageMoveTask](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CancelMessageMoveTask.html): Cancels a specified message movement task.
- [ChangeMessageVisibility](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html): Changes the visibility timeout of a specified message in a queue to a new value.
- [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatch.html): Changes the visibility timeout of multiple messages.
- [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html): Creates a new standard or FIFO queue.
- [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html): Deletes the specified message from the specified queue.
- [DeleteMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatch.html): Deletes up to ten messages from the specified queue.
- [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html): Deletes the queue specified by the QueueUrl, regardless of the queue's contents.
- [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html): Gets attributes for the specified queue.
- [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html): The GetQueueUrl API returns the URL of an existing Amazon SQS queue.
- [ListDeadLetterSourceQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html): Returns a list of your queues that have the RedrivePolicy queue attribute configured with a dead-letter queue.
- [ListMessageMoveTasks](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html): Gets the most recent message movement tasks (up to 10) under a specific source queue.
- [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html): Returns a list of your queues in the current region.
- [ListQueueTags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html): List all cost allocation tags added to the specified Amazon SQS queue.
- [PurgeQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.html): Deletes available messages in a queue (including in-flight messages) specified by the QueueURL parameter.
- [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html): Retrieves one or more messages (up to 10), from the specified queue.
- [RemovePermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_RemovePermission.html): Revokes any permissions in the queue policy that matches the specified Label parameter.
- [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html): Delivers a message to the specified queue.
- [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html): You can use SendMessageBatch to send up to 10 messages to the specified queue by assigning either identical or different values to each message (or by not assigning values at all).
- [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html): Sets the value of one or more queue attributes, like a policy.
- [StartMessageMoveTask](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_StartMessageMoveTask.html): Starts an asynchronous task to move messages from a specified source queue to a specified destination queue.
- [TagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_TagQueue.html): Add cost allocation tags to the specified Amazon SQS queue.
- [UntagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_UntagQueue.html): Remove cost allocation tags from the specified Amazon SQS queue.


## [Data Types](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Types.html)

- [BatchResultErrorEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_BatchResultErrorEntry.html): Gives a detailed description of the result of an action on each entry in the request.
- [ChangeMessageVisibilityBatchRequestEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatchRequestEntry.html): Encloses a receipt handle and an entry ID for each message in .
- [ChangeMessageVisibilityBatchResultEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatchResultEntry.html): Encloses the Id of an entry in .
- [DeleteMessageBatchRequestEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatchRequestEntry.html): Encloses a receipt handle and an identifier for it.
- [DeleteMessageBatchResultEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatchResultEntry.html): Encloses the Id of an entry in .
- [ListMessageMoveTasksResultEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasksResultEntry.html): Contains the details of a message movement task.
- [Message](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Message.html): An Amazon SQS message.
- [MessageAttributeValue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_MessageAttributeValue.html): The user-specified message attribute value.
- [MessageSystemAttributeValue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_MessageSystemAttributeValue.html): The user-specified message system attribute value.
- [SendMessageBatchRequestEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatchRequestEntry.html): Contains the details of a single Amazon SQS message along with an Id.
- [SendMessageBatchResultEntry](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatchResultEntry.html): Encloses a MessageId for a successfully-enqueued message in a .
