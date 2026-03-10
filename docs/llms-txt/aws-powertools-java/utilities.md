# Utilities

The batch processing utility provides a way to handle partial failures when processing batches of messages from SQS queues, SQS FIFO queues, Kinesis Streams, or DynamoDB Streams.

```
stateDiagram-v2
    direction LR
    BatchSource: Amazon SQS <br/><br/> Amazon Kinesis Data Streams <br/><br/> Amazon DynamoDB Streams <br/><br/>
    LambdaInit: Lambda invocation
    BatchProcessor: Batch Processor
    RecordHandler: Record Handler function
    YourLogic: Your logic to process each batch item
    LambdaResponse: Lambda response
    BatchSource --> LambdaInit
    LambdaInit --> BatchProcessor
    BatchProcessor --> RecordHandler
    state BatchProcessor {
        [*] --> RecordHandler: Your function
        RecordHandler --> YourLogic
    }
    RecordHandler --> BatchProcessor: Collect results
    BatchProcessor --> LambdaResponse: Report items that failed processing
```

**Key Features**

- Reports batch item failures to reduce number of retries for a record upon errors
- Simple interface to process each batch record
- Integrates with Java Events library and the deserialization module
- Build your own batch processor by extending primitives

**Background**

When using SQS, Kinesis Data Streams, or DynamoDB Streams as a Lambda event source, your Lambda functions are triggered with a batch of messages. If your function fails to process any message from the batch, the entire batch returns to your queue or stream. This same batch is then retried until either condition happens first: **a)** your Lambda function returns a successful response, **b)** record reaches maximum retry attempts, or **c)** records expire.

```
journey
  section Conditions
    Successful response: 5: Success
    Maximum retries: 3: Failure
    Records expired: 1: Failure
```

This behavior changes when you enable Report Batch Item Failures feature in your Lambda function event source configuration:

- [**SQS queues**](#sqs-standard). Only messages reported as failure will return to the queue for a retry, while successful ones will be deleted.
- [**Kinesis data streams**](#kinesis-and-dynamodb-streams) and [**DynamoDB streams**](#kinesis-and-dynamodb-streams). Single reported failure will use its sequence number as the stream checkpoint. Multiple reported failures will use the lowest sequence number as checkpoint.

With this utility, batch records are processed individually â only messages that failed to be processed return to the queue or stream for a further retry. You simply build a `BatchProcessor` in your handler, and return its response from the handler's `processMessage` implementation. Exceptions are handled internally and an appropriate partial response for the message source is returned to Lambda for you.

Warning

While this utility lowers the chance of processing messages more than once, it is still not guaranteed. We recommend implementing processing logic in an idempotent manner wherever possible, for instance, by taking advantage of [the idempotency module](../idempotency/). More details on how Lambda works with SQS can be found in the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)

## Install

We simply add `powertools-batch` to our build dependencies. Note - if you are using other Powertools modules that require code-weaving, such as `powertools-core`, you will need to configure that also.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-batch</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>

```

```
    repositories {
        mavenCentral()
    }

    dependencies {
        implementation 'software.amazon.lambda:powertools-batch:1.20.2'
    }

```

## Getting Started

For this feature to work, you need to **(1)** configure your Lambda function event source to use `ReportBatchItemFailures`, and **(2)** return a specific response to report which records failed to be processed.

You can use your preferred deployment framework to set the correct configuration while this utility, while the `powertools-batch` module handles generating the response, which simply needs to be returned as the result of your Lambda handler.

A complete [Serverless Application Model](https://aws.amazon.com/serverless/sam/) example can be found [here](https://github.com/aws-powertools/powertools-lambda-java/tree/main/examples/powertools-examples-batch) covering all of the batch sources.

For more information on configuring `ReportBatchItemFailures`, see the details for [SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-batchfailurereporting), [Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-batchfailurereporting),and [DynamoDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-batchfailurereporting).

You do not need any additional IAM permissions to use this utility, except for what each event source requires.

### Processing messages from SQS

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSBatchResponse;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import software.amazon.lambda.powertools.batch.BatchMessageHandlerBuilder;
import software.amazon.lambda.powertools.batch.handler.BatchMessageHandler;

public class SqsBatchHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {

    private final BatchMessageHandler<SQSEvent, SQSBatchResponse> handler;

    public SqsBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withSqsBatchHandler()
                .buildWithMessageHandler(this::processMessage, Product.class);
    }

    @Override
    public SQSBatchResponse handleRequest(SQSEvent sqsEvent, Context context) {
        return handler.processBatch(sqsEvent, context);
    }


    private void processMessage(Product p, Context c) {
        // Process the product
    }

}

```

```
public class Product {
    private long id;

    private String name;

    private double price;

    public Product() {
    }

    public Product(long id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

```

```
    {
        "Records": [
        {
            "messageId": "d9144555-9a4f-4ec3-99a0-34ce359b4b54",
            "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
            "body": "{\n  \"id\": 1234,\n  \"name\": \"product\",\n  \"price\": 42\n}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1601975706495",
                "SenderId": "AROAIFU437PVZ5L2J53F5",
                "ApproximateFirstReceiveTimestamp": "1601975706499"
            },
            "messageAttributes": {
            },
            "md5OfBody": "13e7f7851d2eaa5c01f208ebadbf1e72",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:eu-central-1:123456789012:TestLambda",
            "awsRegion": "eu-central-1"
        },
        {
            "messageId": "e9144555-9a4f-4ec3-99a0-34ce359b4b54",
            "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
            "body": "{\n  \"id\": 12345,\n  \"name\": \"product5\",\n  \"price\": 45\n}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1601975706495",
                "SenderId": "AROAIFU437PVZ5L2J53F5",
                "ApproximateFirstReceiveTimestamp": "1601975706499"
            },
            "messageAttributes": {
            },
            "md5OfBody": "13e7f7851d2eaa5c01f208ebadbf1e72",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:eu-central-1:123456789012:TestLambda",
            "awsRegion": "eu-central-1"
        }]
    }

```

### Processing messages from Kinesis Streams

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KinesisEvent;
import com.amazonaws.services.lambda.runtime.events.StreamsEventResponse;
import software.amazon.lambda.powertools.batch.BatchMessageHandlerBuilder;
import software.amazon.lambda.powertools.batch.handler.BatchMessageHandler;

public class KinesisBatchHandler implements RequestHandler<KinesisEvent, StreamsEventResponse> {

    private final BatchMessageHandler<KinesisEvent, StreamsEventResponse> handler;

    public KinesisBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withKinesisBatchHandler()
                .buildWithMessageHandler(this::processMessage, Product.class);
    }

    @Override
    public StreamsEventResponse handleRequest(KinesisEvent kinesisEvent, Context context) {
        return handler.processBatch(kinesisEvent, context);
    }

    private void processMessage(Product p, Context c) {
        // process the product
    }

}

```

```
public class Product {
    private long id;

    private String name;

    private double price;

    public Product() {
    }

    public Product(long id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

```

```
    {
      "Records": [
        {
          "kinesis": {
            "partitionKey": "partitionKey-03",
            "kinesisSchemaVersion": "1.0",
            "data": "eyJpZCI6MTIzNCwgIm5hbWUiOiJwcm9kdWN0IiwgInByaWNlIjo0Mn0=",
            "sequenceNumber": "49545115243490985018280067714973144582180062593244200961",
            "approximateArrivalTimestamp": 1428537600,
            "encryptionType": "NONE"
          },
          "eventSource": "aws:kinesis",
          "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",
          "invokeIdentityArn": "arn:aws:iam::EXAMPLE",
          "eventVersion": "1.0",
          "eventName": "aws:kinesis:record",
          "eventSourceARN": "arn:aws:kinesis:EXAMPLE",
          "awsRegion": "eu-central-1"
        },
        {
          "kinesis": {
            "partitionKey": "partitionKey-03",
            "kinesisSchemaVersion": "1.0",
            "data": "eyJpZCI6MTIzNDUsICJuYW1lIjoicHJvZHVjdDUiLCAicHJpY2UiOjQ1fQ==",
            "sequenceNumber": "49545115243490985018280067714973144582180062593244200962",
            "approximateArrivalTimestamp": 1428537600,
            "encryptionType": "NONE"
          },
          "eventSource": "aws:kinesis",
          "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",
          "invokeIdentityArn": "arn:aws:iam::EXAMPLE",
          "eventVersion": "1.0",
          "eventName": "aws:kinesis:record",
          "eventSourceARN": "arn:aws:kinesis:EXAMPLE",
          "awsRegion": "eu-central-1"
        }
      ]
    }

```

### Processing messages from DynamoDB Streams

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.amazonaws.services.lambda.runtime.events.StreamsEventResponse;
import software.amazon.lambda.powertools.batch.BatchMessageHandlerBuilder;
import software.amazon.lambda.powertools.batch.handler.BatchMessageHandler;

public class DynamoDBStreamBatchHandler implements RequestHandler<DynamodbEvent, StreamsEventResponse> {

    private final BatchMessageHandler<DynamodbEvent, StreamsEventResponse> handler;

    public DynamoDBStreamBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withDynamoDbBatchHandler()
                .buildWithRawMessageHandler(this::processMessage);
    }

    @Override
    public StreamsEventResponse handleRequest(DynamodbEvent ddbEvent, Context context) {
        return handler.processBatch(ddbEvent, context);
    }

    private void processMessage(DynamodbEvent.DynamodbStreamRecord dynamodbStreamRecord, Context context) {
        // Process the change record
    }
}

```

```
    {
      "Records": [
        {
          "eventID": "c4ca4238a0b923820dcc509a6f75849b",
          "eventName": "INSERT",
          "eventVersion": "1.1",
          "eventSource": "aws:dynamodb",
          "awsRegion": "eu-central-1",
          "dynamodb": {
            "Keys": {
              "Id": {
                "N": "101"
              }
            },
            "NewImage": {
              "Message": {
                "S": "New item!"
              },
              "Id": {
                "N": "101"
              }
            },
            "ApproximateCreationDateTime": 1428537600,
            "SequenceNumber": "4421584500000000017450439091",
            "SizeBytes": 26,
            "StreamViewType": "NEW_AND_OLD_IMAGES"
          },
          "eventSourceARN": "arn:aws:dynamodb:eu-central-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899",
          "userIdentity": {
            "principalId": "dynamodb.amazonaws.com",
            "type": "Service"
          }
        },
        {
          "eventID": "c81e728d9d4c2f636f067f89cc14862c",
          "eventName": "MODIFY",
          "eventVersion": "1.1",
          "eventSource": "aws:dynamodb",
          "awsRegion": "eu-central-1",
          "dynamodb": {
            "Keys": {
              "Id": {
                "N": "101"
              }
            },
            "NewImage": {
              "Message": {
                "S": "This item has changed"
              },
              "Id": {
                "N": "101"
              }
            },
            "OldImage": {
              "Message": {
                "S": "New item!"
              },
              "Id": {
                "N": "101"
              }
            },
            "ApproximateCreationDateTime": 1428537600,
            "SequenceNumber": "4421584500000000017450439092",
            "SizeBytes": 59,
            "StreamViewType": "NEW_AND_OLD_IMAGES"
          },
          "eventSourceARN": "arn:aws:dynamodb:eu-central-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899"
        }
      ]
    }

```

## Handling Messages

### Raw message and deserialized message handlers

You must provide either a raw message handler, or a deserialized message handler. The raw message handler receives the envelope record type relevant for the particular event source - for instance, the SQS event source provides [SQSMessage](https://javadoc.io/doc/com.amazonaws/aws-lambda-java-events/2.2.2/com/amazonaws/services/lambda/runtime/events/SQSEvent.html) instances. The deserialized message handler extracts the body from this envelope, and deserializes it to a user-defined type. Note that deserialized message handlers are not relevant for the DynamoDB provider, as the format of the inner message is fixed by DynamoDB.

In general, the deserialized message handler should be used unless you need access to information on the envelope.

```
public void setup() {
    BatchMessageHandler<SQSEvent, SQSBatchResponse> handler = new BatchMessageHandlerBuilder()
            .withSqsBatchHandler()
            .buildWithRawMessageHandler(this::processRawMessage);
}

private void processRawMessage(SQSEvent.SQSMessage sqsMessage) {
    // Do something with the raw message
}

```

```
public void setup() {
    BatchMessageHandler<SQSEvent, SQSBatchResponse> handler = new BatchMessageHandlerBuilder()
            .withSqsBatchHandler()
            .buildWitMessageHandler(this::processRawMessage, Product.class);
}

private void processMessage(Product product) {
    // Do something with the deserialized message
}

```

### Success and failure handlers

You can register a success or failure handler which will be invoked as each message is processed by the batch module. This may be useful for reporting - for instance, writing metrics or logging failures.

These handlers are optional. Batch failures are handled by the module regardless of whether or not you provide a custom failure handler.

Handlers can be provided when building the batch processor and are available for all event sources. For instance for DynamoDB:

```
BatchMessageHandler<DynamodbEvent, StreamsEventResponse> handler = new BatchMessageHandlerBuilder()
            .withDynamoDbBatchHandler()
            .withSuccessHandler((m) -> {
                // Success handler receives the raw message
                LOGGER.info("Message with sequenceNumber {} was successfully processed",
                    m.getDynamodb().getSequenceNumber());
            })
            .withFailureHandler((m, e) -> {
                // Failure handler receives the raw message and the exception thrown.
                LOGGER.info("Message with sequenceNumber {} failed to be processed: {}"
                , e.getDynamodb().getSequenceNumber(), e);
            })
            .buildWithMessageHander(this::processMessage);

```

Info

If the success handler throws an exception, the item it is processing will be marked as failed by the batch processor. If the failure handler throws, the batch processing will continue; the item it is processing has already been marked as failed.

### Lambda Context

Both raw and deserialized message handlers can choose to take the Lambda context as an argument if they need it, or not:

```
    public class ClassWithHandlers {

        private void processMessage(Product product) {
            // Do something with the raw message
        }

        private void processMessageWithContext(Product product, Context context) {
            // Do something with the raw message and the lambda Context
        }
    }

```

[CloudFormation Custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) provide a way for [AWS Lambda functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html) to execute provisioning logic whenever CloudFormation stacks are created, updated, or deleted.

Powertools-cloudformation makes it easy to write Lambda functions in Java that are used as CloudFormation custom resources.\
The utility reads incoming CloudFormation events, calls your custom code depending on the operation (CREATE, UPDATE or DELETE) and sends responses back to CloudFormation.\
By using this library you do not need to write code to integrate with CloudFormation, and you only focus on writing the custom provisioning logic inside the Lambda function.

## Install

To install this utility, add the following dependency to your project.

```
<dependency>
    <groupId>software.amazon.lambda</groupId>
    <artifactId>powertools-cloudformation</artifactId>
    <version>1.20.2</version>
</dependency>

```

```
 dependencies {
    ...
    implementation 'software.amazon.lambda:powertools-cloudformation:1.20.2'
}

```

## Usage

To utilise the feature, extend the `AbstractCustomResourceHandler` class in your Lambda handler class.\
Next, implement and override the following 3 methods: `create`, `update` and `delete`. The `AbstractCustomResourceHandler` invokes the right method according to the CloudFormation [custom resource request event](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requests.html) it receives.\
Inside the methods, implement your custom provisioning logic, and return a `Response`. The `AbstractCustomResourceHandler` takes your `Response`, builds a [custom resource responses](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-responses.html) and sends it to CloudFormation automatically.

Custom resources notify cloudformation either of `SUCCESS` or `FAILED` status. You have 2 utility methods to represent these responses: `Response.success(physicalResourceId)` and `Response.failed(physicalResourceId)`.\
The `physicalResourceId` is an identifier that is used during the lifecycle operations of the Custom Resource.\
You should generate a `physicalResourceId` during the `CREATE` operation, CloudFormation stores the `physicalResourceId` and includes it in `UPDATE` and `DELETE` events.

Here an example of how to implement a Custom Resource using the powertools-cloudformation library:

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.events.CloudFormationCustomResourceEvent;
import software.amazon.lambda.powertools.cloudformation.AbstractCustomResourceHandler;
import software.amazon.lambda.powertools.cloudformation.Response;

public class MyCustomResourceHandler extends AbstractCustomResourceHandler {

    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "sample-resource-id-" + UUID.randomUUID(); //Create a unique ID for your resource
        ProvisioningResult provisioningResult = doProvisioning(physicalResourceId);
        if(provisioningResult.isSuccessful()){ //check if the provisioning was successful
            return Response.success(physicalResourceId);
        }else{
            return Response.failed(physicalResourceId);
        }
    }

    @Override
    protected Response update(CloudFormationCustomResourceEvent updateEvent, Context context) {
        String physicalResourceId = updateEvent.getPhysicalResourceId(); //Get the PhysicalResourceId from CloudFormation
        UpdateResult updateResult = doUpdates(physicalResourceId);
        if(updateResult.isSuccessful()){ //check if the update operations were successful
            return Response.success(physicalResourceId);
        }else{
            return Response.failed(physicalResourceId);
        }
    }

    @Override
    protected Response delete(CloudFormationCustomResourceEvent deleteEvent, Context context) {
        String physicalResourceId = deleteEvent.getPhysicalResourceId(); //Get the PhysicalResourceId from CloudFormation
        DeleteResult deleteResult = doDeletes(physicalResourceId);
        if(deleteResult.isSuccessful()){ //check if the delete operations were successful
            return Response.success(physicalResourceId);
        }else{
            return Response.failed(physicalResourceId);
        }
    }
}

```

### Missing `Response` and exception handling

If a `Response` is not returned by your code, `AbstractCustomResourceHandler` defaults the response to `SUCCESS`.\
If your code raises an exception (which is not handled), the `AbstractCustomResourceHandler` defaults the response to `FAILED`.

In both of the scenarios, powertools-java will return the `physicalResourceId` to CloudFormation based on the following logic:

- For CREATE operations, the `LogStreamName` from the Lambda context is used.
- For UPDATE and DELETE operations, the `physicalResourceId` provided in the `CloudFormationCustomResourceEvent` is used.

#### Why do you need a physicalResourceId?

It is recommended that you always explicitly provide a `physicalResourceId` in your response rather than letting Powertools for AWS Lambda (Java) generate if for you because `physicalResourceId` has a crucial role in the lifecycle of a CloudFormation custom resource. If the `physicalResourceId` changes between calls from Cloudformation, for instance in response to an `Update` event, Cloudformation [treats the resource update as a replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html).

### Customising a response

As well as the `Response.success(physicalResourceId)` and `Response.failed(physicalResourceId)`, you can customise the `Response` by using the `Response.builder()`. You customise the responses when you need additional attributes to be shared with other parts of the CloudFormation stack.

In the example below, the Lambda function creates a [Chime AppInstance](https://docs.aws.amazon.com/chime/latest/dg/create-app-instance.html) and maps the returned ARN to a "ChimeAppInstanceArn" attribute.

```
public class ChimeAppInstanceHandler extends AbstractCustomResourceHandler {
    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "my-app-name-" + UUID.randomUUID(); //Create a unique ID 
        CreateAppInstanceRequest chimeRequest = CreateAppInstanceRequest.builder()
                .name(physicalResourceId)
                .build();
        CreateAppInstanceResponse chimeResponse = ChimeClient.builder()
                .region("us-east-1")
                .createAppInstance(chimeRequest);

        Map<String, String> chimeAtts = Map.of("ChimeAppInstanceArn", chimeResponse.appInstanceArn());
        return Response.builder()
                .value(chimeAtts)
                .status(Response.Status.SUCCESS)
                .physicalResourceId(physicalResourceId)
                .build();
    }
}

```

For the example above the following response payload will be sent.

```
{
  "Status": "SUCCESS",
  "PhysicalResourceId": "2021/10/01/e3a37e552eff4718a5675c1e31f0649e",
  "StackId": "arn:aws:cloudformation:us-east-1:123456789000:stack/Custom-stack/59e4d2d0-2fe2-10ec-b00e-124d7c1c5f15",
  "RequestId": "7cae0346-0359-4dff-b80a-a82f247467b6",
  "LogicalResourceId:": "ChimeTriggerResource",
  "PhysicalResourceId:": "my-app-name-db4a47b9-0cac-45ba-8cc4-a480490c5779",
  "NoEcho": false,
  "Data": {
    "ChimeAppInstanceArn": "arn:aws:chime:us-east-1:123456789000:app-instance/150972c2-5490-49a9-8ba7-e7da4257c16a"
  }
}

```

Once the custom resource receives this response, its "ChimeAppInstanceArn" attribute is set and the [Fn::GetAtt function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) may be used to retrieve the attribute value and make it available to other resources in the stack.

#### Sensitive Response Data

If any attributes are sensitive, enable the "noEcho" flag to mask the output of the custom resource when it's retrieved with the Fn::GetAtt function.

```
public class SensitiveDataHandler extends AbstractResourceHandler {
    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "my-sensitive-resource-" + UUID.randomUUID(); //Create a unique ID 
        return Response.builder()
                .status(Response.Status.SUCCESS)
                .physicalResourceId(physicalResourceId)
                .value(Map.of("SomeSecret", sensitiveValue))
                .noEcho(true)
                .build();
    }
}

```

#### Customizing Serialization

Although using a `Map` as the Response's value is the most straightforward way to provide attribute name/value pairs, any arbitrary `java.lang.Object` may be used. By default, these objects are serialized with an internal Jackson `ObjectMapper`. If the object requires special serialization logic, a custom `ObjectMapper` can be specified.

```
public class CustomSerializationHandler extends AbstractResourceHandler {
    /**
     * Type representing the custom response Data. 
     */
    static class Policy {
        public ZonedDateTime getExpires() {
            return ZonedDateTime.now().plusDays(10);
        }
    }

    /**
     * Mapper for serializing Policy instances.
     */
    private final ObjectMapper policyMapper = new ObjectMapper()
            .registerModule(new JavaTimeModule())
            .disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);

    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "my-policy-name-" + UUID.randomUUID(); //Create a unique ID 
        Policy policy = new Policy();
        return Response.builder()
                .status(Response.Status.SUCCESS)
                .physicalResourceId(physicalResourceId)
                .value(policy)
                .objectMapper(policyMapper) // customize serialization
                .build();
    }
}

```

## Advanced

### Understanding the CloudFormation custom resource lifecycle

While the library provides an easy-to-use interface, we recommend that you understand the lifecycle of CloudFormation custom resources before using them in production.

#### Creating a custom resource

When CloudFormation issues a CREATE on a custom resource, there are 2 possible states: `CREATE_COMPLETE` and `CREATE_FAILED`

```
stateDiagram
    direction LR
    createState: Create custom resource
    [*] --> createState
    createState --> CREATE_COMPLETE 
    createState --> CREATE_FAILED
```

If the resource is created successfully, the `physicalResourceId` is stored by CloudFormation for future operations.\
If the resource failed to create, CloudFormation triggers a rollback operation by default (rollback can be disabled, see [stack failure options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-failure-options.html))

#### Updating a custom resource

CloudFormation issues an UPDATE operation on a custom resource only when one or more custom resource properties change. During the update, the custom resource may update successfully, or may fail the update.

```
stateDiagram
    direction LR
    updateState: Update custom resource
    [*] --> updateState
    updateState --> UPDATE_COMPLETE 
    updateState --> UPDATE_FAILED
```

In both of these scenarios, the custom resource can return the same `physicalResourceId` it received in the CloudFormation event, or a different `physicalResourceId`.\
Semantically an `UPDATE_COMPLETE` that returns the same `physicalResourceId` it received indicates that the existing resource was updated successfully.\
Instead, an `UPDATE_COMPLETE` with a different `physicalResourceId` means that a new physical resource was created successfully.

```
flowchart BT
    id1(Logical resource)
    id2(Previous physical Resource)
    id3(New physical Resource)
    id2 --> id1 
    id3 --> id1 
```

Therefore, after the custom resource update completed or failed, there may be other cleanup operations by Cloudformation during the rollback, as described in the diagram below:

```
stateDiagram
    state if_state <<choice>>
    updateState: Update custom resource
    deletePrev: DELETE resource with previous physicalResourceId
    updatePrev: Rollback - UPDATE resource with previous properties
    noOp: No further operations
    [*] --> updateState
    updateState --> UPDATE_COMPLETE
    UPDATE_COMPLETE --> if_state
    if_state --> noOp : Same physicalResourceId
    if_state --> deletePrev : Different physicalResourceId
    updateState --> UPDATE_FAILED
    UPDATE_FAILED --> updatePrev
```

#### Deleting a custom resource

CloudFormation issues a DELETE on a custom resource when:

- the CloudFormation stack is being deleted
- a new `physicalResourceId` was received during an update, and CloudFormation proceeds to rollback(DELETE) the custom resource with the previous `physicalResourceId`.

```
stateDiagram
    direction LR
    deleteState: Delete custom resource
    [*] --> deleteState
    deleteState --> DELETE_COMPLETE 
    deleteState --> DELETE_FAILED
```

The idempotency utility provides a simple solution to convert your Lambda functions into idempotent operations which are safe to retry.

## Terminology

The property of idempotency means that an operation does not cause additional side effects if it is called more than once with the same input parameters.

**Idempotent operations will return the same result when they are called multiple times with the same parameters**. This makes idempotent operations safe to retry. [Read more](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) about idempotency.

**Idempotency key** is a hash representation of either the entire event or a specific configured subset of the event, and invocation results are **JSON serialized** and stored in your persistence storage layer.

## Key features

- Prevent Lambda handler function from executing more than once on the same event payload during a time window
- Ensure Lambda handler returns the same result when called with the same payload
- Select a subset of the event as the idempotency key using JMESPath expressions
- Set a time window in which records with the same payload should be considered duplicates

## Getting started

### Installation

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-idempotency</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-idempotency</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-idempotency</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-idempotency</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-idempotency:1.20.2'
    }

    sourceCompatibility = 11 // or higher
    targetCompatibility = 11 // or higher

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-idempotency:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

### Required resources

Before getting started, you need to create a persistent storage layer where the idempotency utility can store its state - your Lambda functions will need read and write access to it.

As of now, Amazon DynamoDB is the only supported persistent storage layer, so you'll need to create a table first.

**Default table configuration**

If you're not [changing the default configuration for the DynamoDB persistence layer](#dynamodbpersistencestore), this is the expected default configuration:

| Configuration | Value | Notes | | --- | --- | --- | | Partition key | `id` | | | TTL attribute name | `expiration` | This can only be configured after your table is created if you're using AWS Console |

Tip: You can share a single state table for all functions

You can reuse the same DynamoDB table to store idempotency state. We add your function name in addition to the idempotency key as a hash key.

```
Resources:
  IdempotencyTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      TimeToLiveSpecification:
        AttributeName: expiration
        Enabled: true
      BillingMode: PAY_PER_REQUEST

  IdempotencyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: Function
      Handler: helloworld.App::handleRequest
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref IdempotencyTable
      Environment:
        Variables:
          IDEMPOTENCY_TABLE: !Ref IdempotencyTable

```

Warning: Large responses with DynamoDB persistence layer

When using this utility with DynamoDB, your function's responses must be [smaller than 400KB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#limits-items). Larger items cannot be written to DynamoDB and will cause exceptions.

Info: DynamoDB

Each function invocation will generally make 2 requests to DynamoDB. If the result returned by your Lambda is less than 1kb, you can expect 2 WCUs per invocation. For retried invocations, you will see 1WCU and 1RCU. Review the [DynamoDB pricing documentation](https://aws.amazon.com/dynamodb/pricing/) to estimate the cost.

### Idempotent annotation

You can quickly start by initializing the `DynamoDBPersistenceStore` and using it with the `@Idempotent` annotation on your Lambda handler.

Important

Initialization and configuration of the `DynamoDBPersistenceStore` must be performed outside the handler, preferably in the constructor.

```
public class App implements RequestHandler<Subscription, SubscriptionResult> {

  public App() {
    // we need to initialize idempotency store before the handleRequest method is called
    Idempotency.config().withPersistenceStore(
      DynamoDBPersistenceStore.builder()
        .withTableName(System.getenv("TABLE_NAME"))
        .build()
      ).configure();
  }

  @Idempotent
  public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    SubscriptionPayment payment = createSubscriptionPayment(
      event.getUsername(),
      event.getProductId()
    );

    return new SubscriptionResult(payment.getId(), "success", 200);
  }
}

```

```
{
  "username": "xyz",
  "product_id": "123456789"
}

```

#### Idempotent annotation on another method

You can use the `@Idempotent` annotation for any synchronous Java function, not only the `handleRequest` one.

When using `@Idempotent` annotation on another method, you must tell which parameter in the method signature has the data we should use:

- If the method only has one parameter, it will be used by default.
- If there are 2 or more parameters, you must set the `@IdempotencyKey` on the parameter to use.

The parameter must be serializable in JSON. We use Jackson internally to (de)serialize objects

This example also demonstrates how you can integrate with [Batch utility](../batch/), so you can process each record in an idempotent manner.

```
public class AppSqsEvent implements RequestHandler<SQSEvent, String> {

  public AppSqsEvent() {
    Idempotency.config()
      .withPersistenceStore(
          DynamoDBPersistenceStore.builder()
            .withTableName(System.getenv("TABLE_NAME"))
            .build()
      ).withConfig(
           IdempotencyConfig.builder()
             .withEventKeyJMESPath("messageId") // see Choosing a payload subset section
             .build()
      ).configure();
    }

  @Override
  @SqsBatch(SampleMessageHandler.class)
  public String handleRequest(SQSEvent input, Context context) {
    dummy("hello", "world");
    return "{\"statusCode\": 200}";
  }

  @Idempotent
  private String dummy(String argOne, @IdempotencyKey String argTwo) {
    return "something";
  }

  public static class SampleMessageHandler implements SqsMessageHandler<Object> {
    @Override
    @Idempotent
    // no need to use @IdempotencyKey as there is only one parameter
    public String process(SQSMessage message) {
      String returnVal = doSomething(message.getBody());
      return returnVal;
    }
  }
}

```

```
{
    "Records": [
        {
            "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
            "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
            "body": "Test message.",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082649183",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082649185"
            },
            "messageAttributes": {
                "testAttr": {
                "stringValue": "100",
                "binaryValue": "base64Str",
                "dataType": "Number"
                }
            },
            "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
            "awsRegion": "us-east-2"
        }
    ]
}

```

### Choosing a payload subset for idempotency

Tip: Dealing with always changing payloads

When dealing with an elaborate payload (API Gateway request for example), where parts of the payload always change, you should configure the **`EventKeyJMESPath`**.

Use [`IdempotencyConfig`](#customizing-the-default-behavior) to instruct the Idempotent annotation to only use a portion of your payload to verify whether a request is idempotent, and therefore it should not be retried.

> **Payment scenario**

In this example, we have a Lambda handler that creates a payment for a user subscribing to a product. We want to ensure that we don't accidentally charge our customer by subscribing them more than once.

Imagine the function executes successfully, but the client never receives the response due to a connection issue. It is safe to retry in this instance, as the idempotent decorator will return a previously saved response.

Warning: Idempotency for JSON payloads

The payload extracted by the `EventKeyJMESPath` is treated as a string by default, so will be sensitive to differences in whitespace even when the JSON payload itself is identical.

To alter this behaviour, you can use the [JMESPath built-in function](../serialization/#jmespath-functions) `powertools_json()` to treat the payload as a JSON object rather than a string.

```
public class PaymentFunction implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

  public PaymentFunction() {
    Idempotency.config()
    .withConfig(
        IdempotencyConfig.builder()
          .withEventKeyJMESPath("powertools_json(body)")
          .build())
    .withPersistenceStore(
        DynamoDBPersistenceStore.builder()
          .withTableName(System.getenv("TABLE_NAME"))
          .build())
    .configure();
}

@Idempotent
public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent event, final Context context) {
  APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent();

  try {
    Subscription subscription = JsonConfig.get().getObjectMapper().readValue(event.getBody(), Subscription.class);

    SubscriptionPayment payment = createSubscriptionPayment(
         subscription.getUsername(),
         subscription.getProductId()
    );

    return response
             .withStatusCode(200)
             .withBody(String.format("{\"paymentId\":\"%s\"}", payment.getId()));

  } catch (JsonProcessingException e) {
    return response.withStatusCode(500);
  }
}

```

```
{
  "version":"2.0",
  "body":"{\"username\":\"xyz\",\"productId\":\"123456789\"}",
  "routeKey":"ANY /createpayment",
  "rawPath":"/createpayment",
  "rawQueryString":"",
  "headers": {
    "Header1": "value1",
    "Header2": "value2"
  },
  "requestContext":{
    "accountId":"123456789012",
    "apiId":"api-id",
    "domainName":"id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix":"id",
    "http":{
      "method":"POST",
      "path":"/createpayment",
      "protocol":"HTTP/1.1",
      "sourceIp":"ip",
      "userAgent":"agent"
    },
    "requestId":"id",
    "routeKey":"ANY /createpayment",
    "stage":"$default",
    "time":"10/Feb/2021:13:40:43 +0000",
    "timeEpoch":1612964443723
  },
  "isBase64Encoded":false
}

```

### Idempotency request flow

This sequence diagram shows an example flow of what happens in the payment scenario:

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        activate Persistence Layer
        Note right of Persistence Layer: Locked to prevent concurrent<br/>invocations with <br/> the same payload.
        Lambda-->>Lambda: Call handler (event)
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record with result
        Lambda-->>Client: Response sent to client
    else retried request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        Persistence Layer-->>Lambda: Already exists in persistence layer. Return result
        Lambda-->>Client: Response sent to client
    end
```

*Idempotent sequence*

The client was successful in receiving the result after the retry. Since the Lambda handler was only executed once, our customer hasn't been charged twice.

Note

Bear in mind that the entire Lambda handler is treated as a single idempotent operation. If your Lambda handler can cause multiple side effects, consider splitting it into separate functions.

#### Lambda timeouts

This is automatically done when you annotate your Lambda handler with [@Idempotent annotation](#idempotent-annotation).

To prevent against extended failed retries when a [Lambda function times out](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-verify-invocation-timeouts/), Powertools for AWS Lambda (Java) calculates and includes the remaining invocation available time as part of the idempotency record.

Example

If a second invocation happens **after** this timestamp, and the record is marked as `INPROGRESS`, we will execute the invocation again as if it was in the `EXPIRED` state. This means that if an invocation expired during execution, it will be quickly executed again on the next retry.

Important

If you are using the [@Idempotent annotation on another method](#idempotent-annotation-on-another-method) to guard isolated parts of your code, you must use `registerLambdaContext` method available in the `Idempotency` object to benefit from this protection.

Here is an example on how you register the Lambda context in your handler:

```
public class PaymentHandler implements RequestHandler<SQSEvent, List<String>> {

    public PaymentHandler() {
        Idempotency.config()
                .withPersistenceStore(
                        DynamoDBPersistenceStore.builder()
                                .withTableName(System.getenv("IDEMPOTENCY_TABLE"))
                                .build())
                .configure();
    }

    @Override
    public List<String> handleRequest(SQSEvent sqsEvent, Context context) {
        Idempotency.registerLambdaContext(context);
        return sqsEvent.getRecords().stream().map(record -> process(record.getMessageId(), record.getBody())).collect(Collectors.toList());
    }

    @Idempotent
    private String process(String messageId, @IdempotencyKey String messageBody) {
        logger.info("Processing messageId: {}", messageId);
        PaymentRequest request = extractDataFrom(messageBody).as(PaymentRequest.class);
        return paymentService.process(request);
    }

}

```

#### Lambda timeout sequence diagram

This sequence diagram shows an example flow of what happens if a Lambda function times out:

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        activate Persistence Layer
        Note right of Persistence Layer: Locked to prevent concurrent<br/>invocations with <br/> the same payload.
        Note over Lambda: Time out
        Lambda--xLambda: Call handler (event)
        Lambda-->>Client: Return error response
        deactivate Persistence Layer
    else concurrent request before timeout
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        Persistence Layer-->>Lambda: Request already INPROGRESS
        Lambda--xClient: Return IdempotencyAlreadyInProgressError
    else retry after Lambda timeout
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        activate Persistence Layer
        Note right of Persistence Layer: Locked to prevent concurrent<br/>invocations with <br/> the same payload.
        Lambda-->>Lambda: Call handler (event)
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record with result
        Lambda-->>Client: Response sent to client
    end
```

*Idempotent sequence for Lambda timeouts*

### Handling exceptions

If you are using the `@Idempotent` annotation on your Lambda handler or any other method, any unhandled exceptions that are thrown during the code execution will cause **the record in the persistence layer to be deleted**. This means that new invocations will execute your code again despite having the same payload. If you don't want the record to be deleted, you need to catch exceptions within the idempotent function and return a successful response.

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Persistence Layer
    Client->>Lambda: Invoke (event)
    Lambda->>Persistence Layer: Get or set (id=event.search(payload))
    activate Persistence Layer
    Note right of Persistence Layer: Locked during this time. Prevents multiple<br/>Lambda invocations with the same<br/>payload running concurrently.
    Lambda--xLambda: Call handler (event).<br/>Raises exception
    Lambda->>Persistence Layer: Delete record (id=event.search(payload))
    deactivate Persistence Layer
    Lambda-->>Client: Return error response
```

*Idempotent sequence exception*

If an Exception is raised *outside* the scope of a decorated method and after your method has been called, the persistent record will not be affected. In this case, idempotency will be maintained for your decorated function. Example:

```
  public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    // If an exception is thrown here, no idempotent record will ever get created as the
    // idempotent function does not get called 
    doSomeStuff();

    result = idempotentMethod(event);

    // This exception will not cause the idempotent record to be deleted, since it
    // happens after the decorated function has been successfully called    
    throw new Exception();
  }

  @Idempotent
  private String idempotentMethod(final Subscription subscription) {
    // perform some operation with no exception thrown
  }

```

Warning

**We will throw an `IdempotencyPersistenceLayerException`** if any of the calls to the persistence layer fail unexpectedly.

As this happens outside the scope of your decorated function, you are not able to catch it.

### Persistence stores

#### DynamoDBPersistenceStore

This persistence store is built-in, and you can either use an existing DynamoDB table or create a new one dedicated for idempotency state (recommended).

Use the builder to customize the table structure:

```
DynamoDBPersistenceStore.builder()
                        .withTableName(System.getenv("TABLE_NAME"))
                        .withKeyAttr("idempotency_key")
                        .withExpiryAttr("expires_at")
                        .withStatusAttr("current_status")
                        .withDataAttr("result_data")
                        .withValidationAttr("validation_key")
                        .build()

```

When using DynamoDB as a persistence layer, you can alter the attribute names by passing these parameters when initializing the persistence layer:

| Parameter | Required | Default | Description | | --- | --- | --- | --- | | **TableName** | Y | | Table name to store state | | **KeyAttr** | | `id` | Partition key of the table. Hashed representation of the payload (unless **SortKeyAttr** is specified) | | **ExpiryAttr** | | `expiration` | Unix timestamp of when record expires | | **StatusAttr** | | `status` | Stores status of the Lambda execution during and after invocation | | **DataAttr** | | `data` | Stores results of successfully idempotent methods | | **ValidationAttr** | | `validation` | Hashed representation of the parts of the event used for validation | | **SortKeyAttr** | | | Sort key of the table (if table is configured with a sort key). | | **StaticPkValue** | | `idempotency#{LAMBDA_FUNCTION_NAME}` | Static value to use as the partition key. Only used when **SortKeyAttr** is set. |

## Advanced

### Customizing the default behavior

Idempotency behavior can be further configured with **`IdempotencyConfig`** using a builder:

```
IdempotencyConfig.builder()
                .withEventKeyJMESPath("id")
                .withPayloadValidationJMESPath("paymentId")
                .withThrowOnNoIdempotencyKey(true)
                .withExpiration(Duration.of(5, ChronoUnit.MINUTES))
                .withUseLocalCache(true)
                .withLocalCacheMaxItems(432)
                .withHashFunction("SHA-256")
                .build()

```

These are the available options for further configuration:

| Parameter | Default | Description | | --- | --- | --- | | **EventKeyJMESPath** | `""` | JMESPath expression to extract the idempotency key from the event record. See available [built-in functions](serialization) | | **PayloadValidationJMESPath** | `""` | JMESPath expression to validate whether certain parameters have changed in the event | | **ThrowOnNoIdempotencyKey** | `False` | Throw exception if no idempotency key was found in the request | | **ExpirationInSeconds** | 3600 | The number of seconds to wait before a record is expired | | **UseLocalCache** | `false` | Whether to locally cache idempotency results (LRU cache) | | **LocalCacheMaxItems** | 256 | Max number of items to store in local cache | | **HashFunction** | `MD5` | Algorithm to use for calculating hashes, as supported by `java.security.MessageDigest` (eg. SHA-1, SHA-256, ...) |

These features are detailed below.

### Handling concurrent executions with the same payload

This utility will throw an **`IdempotencyAlreadyInProgressException`** if we receive **multiple invocations with the same payload while the first invocation hasn't completed yet**.

Info

If you receive `IdempotencyAlreadyInProgressException`, you can safely retry the operation.

This is a locking mechanism for correctness. Since we don't know the result from the first invocation yet, we can't safely allow another concurrent execution.

### Using in-memory cache

**By default, in-memory local caching is disabled**, to avoid using memory in an unpredictable way.

Warning

Be sure to configure the Lambda memory according to the number of records and the potential size of each record.

You can enable it as seen before with:

```
    IdempotencyConfig.builder()
        .withUseLocalCache(true)
        .build()

```

When enabled, we cache a maximum of 256 records in each Lambda execution environment - You can change it with the **`LocalCacheMaxItems`** parameter.

Note: This in-memory cache is local to each Lambda execution environment

This means it will be effective in cases where your function's concurrency is low in comparison to the number of "retry" invocations with the same payload, because cache might be empty.

### Expiring idempotency records

Note

By default, we expire idempotency records after **an hour** (3600 seconds).

In most cases, it is not desirable to store the idempotency records forever. Rather, you want to guarantee that the same payload won't be executed within a period of time.

You can change this window with the **`ExpirationInSeconds`** parameter:

```
IdempotencyConfig.builder()
    .withExpiration(Duration.of(5, ChronoUnit.MINUTES))
    .build()

```

Records older than 5 minutes will be marked as expired, and the Lambda handler will be executed normally even if it is invoked with a matching payload.

Note: DynamoDB time-to-live field

This utility uses **`expiration`** as the TTL field in DynamoDB, as [demonstrated in the SAM example earlier](#required-resources).

### Payload validation

Question: What if your function is invoked with the same payload except some outer parameters have changed?

Example: A payment transaction for a given productID was requested twice for the same customer, **however the amount to be paid has changed in the second transaction**.

By default, we will return the same result as it returned before, however in this instance it may be misleading; we provide a fail fast payload validation to address this edge case.

With **`PayloadValidationJMESPath`**, you can provide an additional JMESPath expression to specify which part of the event body should be validated against previous idempotent invocations

```
public App() {
  Idempotency.config()
    .withPersistenceStore(DynamoDBPersistenceStore.builder()
        .withTableName(System.getenv("TABLE_NAME"))
        .build())
    .withConfig(IdempotencyConfig.builder()
        .withEventKeyJMESPath("[userDetail, productId]")
        .withPayloadValidationJMESPath("amount")
        .build())
    .configure();
}

@Idempotent
public SubscriptionResult handleRequest(final Subscription input, final Context context) {
    // Creating a subscription payment is a side
    // effect of calling this function!
    SubscriptionPayment payment = createSubscriptionPayment(
      input.getUserDetail().getUsername(),
      input.getProductId(),
      input.getAmount()
    )
    // ...
    return new SubscriptionResult(
        "success", 200,
        payment.getId(),
        payment.getAmount()
    );
}

```

```
{
    "userDetail": {
        "username": "User1",
        "user_email": "user@example.com"
    },
    "productId": 1500,
    "charge_type": "subscription",
    "amount": 500
}

```

```
{
    "userDetail": {
        "username": "User1",
        "user_email": "user@example.com"
    },
    "productId": 1500,
    "charge_type": "subscription",
    "amount": 1
}

```

In this example, the **`userDetail`** and **`productId`** keys are used as the payload to generate the idempotency key, as per **`EventKeyJMESPath`** parameter.

Note

If we try to send the same request but with a different amount, we will raise **`IdempotencyValidationException`**.

Without payload validation, we would have returned the same result as we did for the initial request. Since we're also returning an amount in the response, this could be quite confusing for the client.

By using **`withPayloadValidationJMESPath("amount")`**, we prevent this potentially confusing behavior and instead throw an Exception.

### Making idempotency key required

If you want to enforce that an idempotency key is required, you can set **`ThrowOnNoIdempotencyKey`** to `true`.

This means that we will throw **`IdempotencyKeyException`** if the evaluation of **`EventKeyJMESPath`** is `null`.

When set to `false` (the default), if the idempotency key is null, then the data is not persisted in the store.

```
public App() {
  Idempotency.config()
    .withPersistenceStore(DynamoDBPersistenceStore.builder()
        .withTableName(System.getenv("TABLE_NAME"))
        .build())
    .withConfig(IdempotencyConfig.builder()
        // Requires "user"."uid" and "orderId" to be present
        .withEventKeyJMESPath("[user.uid, orderId]")
        .withThrowOnNoIdempotencyKey(true)
        .build())
    .configure();
}

@Idempotent
public OrderResult handleRequest(final Order input, final Context context) {
  // ...
}

```

```
{
    "user": {
        "uid": "BB0D045C-8878-40C8-889E-38B3CB0A61B1",
        "name": "Foo"
    },
    "orderId": 10000
}

```

Notice that `orderId` is now accidentally within `user` key

```
{
    "user": {
        "uid": "DE0D000E-1234-10D1-991E-EAC1DD1D52C8",
        "name": "Joe Bloggs",
        "orderId": 10000
    },
}

```

### Customizing DynamoDB configuration

When creating the `DynamoDBPersistenceStore`, you can set a custom [`DynamoDbClient`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/DynamoDbClient.html) if you need to customize the configuration:

```
public App() {
    DynamoDbClient customClient = DynamoDbClient.builder()
        .region(Region.US_WEST_2)
        .overrideConfiguration(ClientOverrideConfiguration.builder()
            .addExecutionInterceptor(new TracingInterceptor())
            .build()
        )
        .build();

    Idempotency.config().withPersistenceStore(
      DynamoDBPersistenceStore.builder()
            .withTableName(System.getenv("TABLE_NAME"))
            .withDynamoDbClient(customClient)
            .build()
  ).configure();
}

```

Default configuration is the following:

```
DynamoDbClient.builder()
    .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
    .httpClient(UrlConnectionHttpClient.builder().build())
    .region(Region.of(System.getenv(AWS_REGION_ENV)))
    .build();

```

### Using a DynamoDB table with a composite primary key

When using a composite primary key table (hash+range key), use `SortKeyAttr` parameter when initializing your persistence store.

With this setting, we will save the idempotency key in the sort key instead of the primary key. By default, the primary key will now be set to `idempotency#{LAMBDA_FUNCTION_NAME}`.

You can optionally set a static value for the partition key using the `StaticPkValue` parameter.

```
Idempotency.config().withPersistenceStore(
     DynamoDBPersistenceStore.builder()
       .withTableName(System.getenv("TABLE_NAME"))
       .withSortKeyAttr("sort_key")
       .build())
   .configure();

```

Data would then be stored in DynamoDB like this:

| id | sort_key | expiration | status | data | | --- | --- | --- | --- | --- | | idempotency#MyLambdaFunction | 1e956ef7da78d0cb890be999aecc0c9e | 1636549553 | COMPLETED | {"id": 12391, "message": "success"} | | idempotency#MyLambdaFunction | 2b2cdb5f86361e97b4383087c1ffdf27 | 1636549571 | COMPLETED | {"id": 527212, "message": "success"} | | idempotency#MyLambdaFunction | f091d2527ad1c78f05d54cc3f363be80 | 1636549585 | IN_PROGRESS | |

### Bring your own persistent store

This utility provides an abstract base class, so that you can implement your choice of persistent storage layer.

You can extend the `BasePersistenceStore` class and implement the abstract methods `getRecord`, `putRecord`, `updateRecord` and `deleteRecord`. You can have a look at [`DynamoDBPersistenceStore`](https://github.com/aws-powertools/powertools-lambda-java/blob/master/powertools-idempotency/src/main/java/software/amazon/lambda/powertools/idempotency/persistence/DynamoDBPersistenceStore.java) as an implementation reference.

Danger

Pay attention to the documentation for each method - you may need to perform additional checks inside these methods to ensure the idempotency guarantees remain intact.

For example, the `putRecord` method needs to throw an exception if a non-expired record already exists in the data store with a matching key.

## Compatibility with other utilities

### Validation utility

The idempotency utility can be used with the `@Validation` annotation from the [validation module](../validation/). Ensure that idempotency is the innermost annotation.

```
@Validation(inboundSchema = "classpath:/schema_in.json")
@Idempotent
public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
  // ...
}

```

Tip: JMESPath Powertools for AWS Lambda (Java) functions are also available

Built-in functions like `powertools_json`, `powertools_base64`, `powertools_base64_gzip` are also available to use in this utility. See [JMESPath Powertools for AWS Lambda (Java) functions](../serialization/)

## Testing your code

The idempotency utility provides several routes to test your code.

### Disabling the idempotency utility

When testing your code, you may wish to disable the idempotency logic altogether and focus on testing your business logic. To do this, you can set the environment variable `POWERTOOLS_IDEMPOTENCY_DISABLED` to true. If you prefer setting this for specific tests, and are using JUnit 5, you can use [junit-pioneer](https://junit-pioneer.org/docs/environment-variables/) library:

```
@Test
@SetEnvironmentVariable(key = Constants.IDEMPOTENCY_DISABLED_ENV, value = "true")
public void testIdempotencyDisabled_shouldJustRunTheFunction() {
    MyFunction func = new MyFunction();
    func.handleRequest(someInput, mockedContext);
}

```

You can also disable the idempotency for all tests using `maven-surefire-plugin` and adding the environment variable:

```
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <environmentVariables>
            <POWERTOOLS_IDEMPOTENCY_DISABLED>true</POWERTOOLS_IDEMPOTENCY_DISABLED>
        </environmentVariables>
    </configuration>
</plugin>

```

### Testing with DynamoDB Local

#### Unit tests

To unit test your function with DynamoDB Local, you can refer to this guide to [setup with Maven](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#apache-maven).

```
<dependencies>
    <!-- maven dependency for DynamoDB local -->
    <dependency>
       <groupId>com.amazonaws</groupId>
       <artifactId>DynamoDBLocal</artifactId>
       <version>[1.12,2.0)</version>
        <scope>test</scope>
    </dependency>
    <!-- Needed when building locally on M1 Mac -->
    <dependency>
        <groupId>io.github.ganadist.sqlite4java</groupId>
        <artifactId>libsqlite4java-osx-aarch64</artifactId>
        <version>1.0.392</version>
        <scope>test</scope>
        <type>dylib</type>
    </dependency>
</dependencies>
<repositories>
    <!-- custom repository to get the dependency -->
    <!-- see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#apache-maven -->
    <repository>
       <id>dynamodb-local-oregon</id>
       <name>DynamoDB Local Release Repository</name>
       <url>https://s3-us-west-2.amazonaws.com/dynamodb-local/release</url>
    </repository>
</repositories>
<plugins>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.0.0-M5</version>
        <configuration>
            <!-- need sqlite native libs -->
            <systemPropertyVariables>
                <sqlite4java.library.path>${project.build.directory}/native-libs</sqlite4java.library.path>
            </systemPropertyVariables>
            <!-- environment variables for the tests -->
            <environmentVariables>
                <IDEMPOTENCY_TABLE_NAME>idempotency</IDEMPOTENCY_TABLE_NAME>
                <AWS_REGION>eu-central-1</AWS_REGION>
            </environmentVariables>
        </configuration>
    </plugin>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <executions>
            <execution>
                <id>copy</id>
                <phase>test-compile</phase>
                <goals>
                    <goal>copy-dependencies</goal>
                </goals>
                <configuration>
                    <includeScope>test</includeScope>
                    <includeTypes>so,dll,dylib</includeTypes>
                    <outputDirectory>${project.build.directory}/native-libs</outputDirectory>
                </configuration>
            </execution>
        </executions>
    </plugin>
</plugins>

```

```
public class AppTest {
    @Mock
    private Context context;
    private App app;
    private static DynamoDbClient client;

    @BeforeAll
    public static void setupDynamoLocal() {
        int port = getFreePort();

        // Initialize DynamoDBLocal
        try {
            DynamoDBProxyServer dynamoProxy = ServerRunner.createServerFromCommandLineArgs(new String[]{
                    "-inMemory",
                    "-port",
                    Integer.toString(port)
            });
            dynamoProxy.start();
        } catch (Exception e) {
            throw new RuntimeException();
        }

        // Initialize DynamoDBClient
        client = DynamoDbClient.builder()
                .httpClient(UrlConnectionHttpClient.builder().build())
                .region(Region.EU_WEST_1)
                .endpointOverride(URI.create("http://localhost:" + port))
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create("FAKE", "FAKE")))
                .build();

        // create the table (use same table name as in pom.xml)
        client.createTable(CreateTableRequest.builder()
                .tableName("idempotency")
                .keySchema(KeySchemaElement.builder().keyType(KeyType.HASH).attributeName("id").build())
                .attributeDefinitions(
                        AttributeDefinition.builder().attributeName("id").attributeType(ScalarAttributeType.S).build()
                )
                .billingMode(BillingMode.PAY_PER_REQUEST)
                .build());
    }

    private static int getFreePort() {
        try {
            ServerSocket socket = new ServerSocket(0);
            int port = socket.getLocalPort();
            socket.close();
            return port;
        } catch (IOException ioe) {
            throw new RuntimeException(ioe);
        }
    }

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        app = new App(client);
    }

    @Test
    public void testApp() {
        app.handleRequest(..., context);
        // ... assert
    }
}

```

```
public class App implements RequestHandler<Subscription, SubscriptionResult> {

public App(DynamoDbClient ddbClient) {
    Idempotency.config().withPersistenceStore(
            DynamoDBPersistenceStore.builder()
                    .withTableName(System.getenv("IDEMPOTENCY_TABLE_NAME"))
                    .withDynamoDbClient(ddbClient)
                    .build()
    ).configure();
}

public App() {
    this(null);
}

@Idempotent
public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    // ...
}

```

#### SAM Local

```
public class App implements RequestHandler<Subscription, SubscriptionResult> {

  public App() {
    DynamoDbClientBuilder ddbBuilder = DynamoDbClient.builder()
       .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
       .httpClient(UrlConnectionHttpClient.builder().build());

    if (System.getenv("AWS_SAM_LOCAL") != null) {
      ddbBuilder.endpointOverride(URI.create("http://dynamo:8000"));
    } else {
      ddbBuilder.region(Region.of(System.getenv("AWS_REGION")));
    }

    Idempotency.config().withPersistenceStore(
       DynamoDBPersistenceStore.builder()
          .withTableName(System.getenv("IDEMPOTENCY_TABLE_NAME"))
          .withDynamoDbClient(ddbBuilder.build())
          .build()
    ).configure();
  }

  @Idempotent
  public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    // ...
  }
}

```

```