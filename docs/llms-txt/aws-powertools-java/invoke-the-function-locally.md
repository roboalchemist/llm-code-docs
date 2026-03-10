# invoke the function locally
sam local invoke IdempotentFunction \
    --event event.json \
    --env-vars env.json \
    --docker-network sam-local

```

```
{
    "IdempotentFunction": {
        "IDEMPOTENCY_TABLE_NAME": "idempotency"
    }
}

```

## Extra resources

If you're interested in a deep dive on how Amazon uses idempotency when building our APIs, check out [this article](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).

The large message utility handles SQS and SNS messages which have had their payloads offloaded to S3 if they are larger than the maximum allowed size (256 KB).

Notice

The large message utility (available in the `powertools-sqs` module for versions v1.16.1 and earlier) is now deprecated and replaced by the `powertools-large-messages` described in this page. You can still get the documentation [here](../sqs_large_message_handling/) and the migration guide [here](#migration-from-the-sqs-large-message-utility).

## Features

- Automatically retrieve the content of S3 objects when SQS or SNS messages have been offloaded to S3.
- Automatically delete the S3 Objects after processing succeeds.
- Compatible with the batch module (with SQS).

## Background

```
stateDiagram-v2
    direction LR
    Function : Lambda Function

    state Application {
        direction TB
        sendMsg: sendMessage(QueueUrl, MessageBody)
        extendLib: extended-client-lib
        [*] --> sendMsg
        sendMsg --> extendLib
        state extendLib {
            state if_big <<choice>>
            bigMsg: MessageBody > 256KB ?
            putObject: putObject(S3Bucket, S3Key, Body)
            updateMsg: Update MessageBody<br>with a pointer to S3<br>and add a message attribute
            bigMsg --> if_big
            if_big --> [*]: size(body) <= 256kb
            if_big --> putObject: size(body) > 256kb
            putObject --> updateMsg
            updateMsg --> [*]
        }
    }

    state Function {
        direction TB
        iterateMsgs: Iterate over messages
        ptLargeMsg: powertools-large-messages
        [*] --> Handler
        Handler --> iterateMsgs
        iterateMsgs --> ptLargeMsg
        state ptLargeMsg {
            state if_pointer <<choice>>
            pointer: Message attribute <br>for large message ?
            normalMsg: Small message,<br>body left unchanged
            getObject: getObject(S3Pointer)
            deleteObject: deleteObject(S3Pointer)
            updateBody: Update message body<br>with content from S3 object<br>and remove message attribute
            updateMD5: Update MD5 of the body<br>and attributes (SQS only)
            yourcode: <b>YOUR CODE HERE!</b>
            pointer --> if_pointer
            if_pointer --> normalMsg : False
            normalMsg --> [*]
            if_pointer --> getObject : True
            getObject --> updateBody
            updateBody --> updateMD5
            updateMD5 --> yourcode
            yourcode --> deleteObject
            deleteObject --> [*]
        }
    }

    [*] --> Application
    Application --> Function : Lambda Invocation
    Function --> [*]

```

SQS and SNS message payload is limited to 256KB. If you wish to send messages with a larger payload, you can leverage the [amazon-sqs-java-extended-client-lib](https://github.com/awslabs/amazon-sqs-java-extended-client-lib) or [amazon-sns-java-extended-client-lib](https://github.com/awslabs/amazon-sns-java-extended-client-lib) which offload the message to Amazon S3. See documentation ([SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.html) / [SNS](https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html))

When offloaded to S3, the message contains a specific message attribute and the payload only contains a pointer to the S3 object (bucket and object key).

This utility automatically retrieves messages which have been offloaded to S3 using the extended client libraries. Once a message's payload has been processed successfully, the utility deletes the payload from S3.

This utility is compatible with versions *[1.1.0+](https://github.com/awslabs/amazon-sqs-java-extended-client-lib/releases/tag/1.1.0)* of amazon-sqs-java-extended-client-lib and *[1.0.0+](https://github.com/awslabs/amazon-sns-java-extended-client-lib/releases/tag/1.0.0)* of amazon-sns-java-extended-client-lib.

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-large-messages</artifactId>
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
                        <artifactId>powertools-large-messages</artifactId>
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
        <artifactId>powertools-large-messages</artifactId>
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
                         <artifactId>powertools-large-messages</artifactId>
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
        aspect 'software.amazon.lambda:powertools-large-messages:1.20.2'
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
        aspect 'software.amazon.lambda:powertools-large-messages:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Permissions

As the utility interacts with Amazon S3, the lambda function must have the following permissions on the S3 bucket used for the large messages offloading:

- `s3:GetObject`
- `s3:DeleteObject`

## Annotation

The annotation `@LargeMessage` can be used on any method where the *first* parameter is one of:

- `SQSEvent.SQSMessage`
- `SNSEvent.SNSRecord`

```
import software.amazon.lambda.powertools.largemessages.LargeMessage;

public class SqsMessageHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {

    @Override
    public SQSBatchResponse handleRequest(SQSEvent event, Context context) {
        for (SQSMessage message: event.getRecords()) {
            processRawMessage(message, context);
        }
        return SQSBatchResponse.builder().build();
    }

    @LargeMessage
    private void processRawMessage(SQSEvent.SQSMessage sqsMessage, Context context) {
        // sqsMessage.getBody() will contain the content of the S3 object
    }
}

```

```
import software.amazon.lambda.powertools.largemessages.LargeMessage;

public class SnsRecordHandler implements RequestHandler<SNSEvent, String> {

    @Override
    public String handleRequest(SNSEvent event, Context context) {
        processSNSRecord(event.records.get(0)); // there are always only one message 
        return "Hello World";
    }

    @LargeMessage
    private void processSNSRecord(SNSEvent.SNSRecord snsRecord) {
        // snsRecord.getSNS().getMessage() will contain the content of the S3 object
    }
}

```

When the Lambda function is invoked with a SQS or SNS event, the utility first checks if the content was offloaded to S3. In the case of a large message, there is a message attribute specifying the size of the offloaded message and the message contains a pointer to the S3 object.

If this is the case, the utility will retrieve the object from S3 using the `getObject(bucket, key)` API, and place the content of the object in the message payload. You can then directly use the content of the message. If there was an error during the S3 download, the function will fail with a `LargeMessageProcessingException`.

After your code is invoked and returns without error, the object is deleted from S3 using the `deleteObject(bucket, key)` API. You can disable the deletion of S3 objects with the following configuration:

```
@LargeMessage(deleteS3Object = false)
private void processRawMessage(SQSEvent.SQSMessage sqsMessage) {
    // do something with the message
}

```

Use together with batch module

This utility works perfectly together with the batch module (`powertools-batch`), especially for SQS:

```
public class SqsBatchHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {
    private final BatchMessageHandler<SQSEvent, SQSBatchResponse> handler;

    public SqsBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withSqsBatchHandler()
                .buildWithRawMessageHandler(this::processMessage);
    }

    @Override
    public SQSBatchResponse handleRequest(SQSEvent sqsEvent, Context context) {
        return handler.processBatch(sqsEvent, context);
    }

    @LargeMessage
    private void processMessage(SQSEvent.SQSMessage sqsMessage) {
        // do something with the message
    }
}

```

Use together with idempotency module

This utility also works together with the idempotency module (`powertools-idempotency`). You can add both the `@LargeMessage` and `@Idempotent` annotations, in any order, to the same method. The `@Idempotent` takes precedence over the `@LargeMessage` annotation. It means Idempotency module will use the initial raw message (containing the S3 pointer) and not the large message.

```
public class SqsBatchHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {

    public SqsBatchHandler() {
        Idempotency.config().withConfig(
                    IdempotencyConfig.builder()
                            .withEventKeyJMESPath("body") // get the body of the message for the idempotency key
                            .build())
            .withPersistenceStore(
                    DynamoDBPersistenceStore.builder()
                            .withTableName(System.getenv("IDEMPOTENCY_TABLE"))
                            .build()
            ).configure();
    }

    @Override
    public SQSBatchResponse handleRequest(SQSEvent sqsEvent, Context context) {
        for (SQSMessage message: event.getRecords()) {
            processRawMessage(message, context);
        }
        return SQSBatchResponse.builder().build();
    }

    @Idempotent
    @LargeMessage
    private String processRawMessage(@IdempotencyKey SQSEvent.SQSMessage sqsMessage, Context context) {
        // do something with the message
    }
}

```

## Customizing S3 client configuration

To interact with S3, the utility creates a default S3 Client :

```
S3Client client = S3Client.builder()
                    .httpClient(UrlConnectionHttpClient.builder().build())
                    .region(Region.of(System.getenv(AWS_REGION_ENV)))
                    .build();

```

If you need to customize this `S3Client`, you can leverage the `LargeMessageConfig` singleton:

```
import software.amazon.lambda.powertools.largemessages.LargeMessage;

public class SnsRecordHandler implements RequestHandler<SNSEvent, String> {

    public SnsRecordHandler() {
        LargeMessageConfig.init().withS3Client(/* put your custom S3Client here */);
    }

    @Override
    public String handleRequest(SNSEvent event, Context context) {
        processSNSRecord(event.records.get(0)); 
        return "Hello World";
    }

    @LargeMessage
    private void processSNSRecord(SNSEvent.SNSRecord snsRecord) {
        // snsRecord.getSNS().getMessage() will contain the content of the S3 object
    }
}

```

## Migration from the SQS Large Message utility

- Replace the dependency in maven / gradle: `powertools-sqs` ==> `powertools-large-messages`
- Replace the annotation: `@SqsLargeMessage` ==> `@LargeMessage` (the new module handles both SQS and SNS)
- Move the annotation away from the Lambda `handleRequest` method and put it on a method with `SQSEvent.SQSMessage` or `SNSEvent.SNSRecord` as first parameter.
- The annotation now handles a single message, contrary to the previous version that was handling the complete batch. It gives more control, especially when dealing with partial failures with SQS (see the batch module).
- The new module only provides an annotation, an equivalent to the `SqsUtils` class is not available anymore in this new version.

Finally, if you are still using the `powertools-sqs` library for batch processing, consider moving to `powertools-batch` at the same time to remove the dependency on this library completely; it has been deprecated and will be removed in v2.

The parameters utility provides a way to retrieve parameter values from [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). It also provides a base class to create your parameter provider implementation.

**Key features**

- Retrieve one or multiple parameters from the underlying provider
- Cache parameter values for a given amount of time (defaults to 5 seconds)
- Transform parameter values from JSON or base 64 encoded strings

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-parameters</artifactId>
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
                         <artifactId>powertools-parameters</artifactId>
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
        <artifactId>powertools-parameters</artifactId>
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
                         <artifactId>powertools-parameters</artifactId>
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
        aspect 'software.amazon.lambda:powertools-parameters:1.20.2'
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
        aspect 'software.amazon.lambda:powertools-parameters:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

**IAM Permissions**

This utility requires additional permissions to work as expected. See the table below:

| Provider | Function/Method | IAM Permission | | --- | --- | --- | | SSM Parameter Store | `SSMProvider.get(String)` `SSMProvider.get(String, Class)` | `ssm:GetParameter` | | SSM Parameter Store | `SSMProvider.getMultiple(String)` | `ssm:GetParametersByPath` | | Secrets Manager | `SecretsProvider.get(String)` `SecretsProvider.get(String, Class)` | `secretsmanager:GetSecretValue` | | DynamoDB | `DynamoDBProvider.get(String)` `DynamoDBProvider.getMultiple(string)` | `dynamodb:GetItem` `dynamoDB:Query` |

## SSM Parameter Store

You can retrieve a single parameter using SSMProvider.get() and pass the key of the parameter. For multiple parameters, you can use SSMProvider.getMultiple() and pass the path to retrieve them all.

Alternatively, you can retrieve an instance of a provider and configure its underlying SDK client, in order to get data from other regions or use specific credentials.

```
import software.amazon.lambda.powertools.parameters.SSMProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSSM implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the SSM Provider
    SSMProvider ssmProvider = ParamManager.getSsmProvider();

    // Retrieve a single parameter
    String value = ssmProvider.get("/my/parameter");

    // Retrieve multiple parameters from a path prefix
    // This returns a Map with the parameter name as key
    Map<String, String> values = ssmProvider.getMultiple("/my/path/prefix");

}

```

```
import software.amazon.lambda.powertools.parameters.SSMProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSSM implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    SsmClient client = SsmClient.builder().region(Region.EU_CENTRAL_1).build();
    // Get an instance of the SSM Provider
    SSMProvider ssmProvider = ParamManager.getSsmProvider(client);

    // Retrieve a single parameter
    String value = ssmProvider.get("/my/parameter");

    // Retrieve multiple parameters from a path prefix
    // This returns a Map with the parameter name as key
    Map<String, String> values = ssmProvider.getMultiple("/my/path/prefix");

}

```

### Additional arguments

The AWS Systems Manager Parameter Store provider supports two additional arguments for the `get()` and `getMultiple()` methods:

| Option | Default | Description | | --- | --- | --- | | **withDecryption()** | `False` | Will automatically decrypt the parameter. | | **recursive()** | `False` | For `getMultiple()` only, will fetch all parameter values recursively based on a path prefix. |

**Example:**

```
import software.amazon.lambda.powertools.parameters.SSMProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSSM implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the SSM Provider
    SSMProvider ssmProvider = ParamManager.getSsmProvider();

    // Retrieve a single parameter and decrypt it
    String value = ssmProvider.withDecryption().get("/my/parameter");

    // Retrieve multiple parameters recursively from a path prefix
    Map<String, String> values = ssmProvider.recursive().getMultiple("/my/path/prefix");

}

```

## Secrets Manager

For secrets stored in Secrets Manager, use `getSecretsProvider`.

Alternatively, you can retrieve an instance of a provider and configure its underlying SDK client, in order to get data from other regions or use specific credentials.

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the Secrets Provider
    SecretsProvider secretsProvider = ParamManager.getSecretsProvider();

    // Retrieve a single secret
    String value = secretsProvider.get("/my/secret");

}

```

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    SecretsManagerClient client = SecretsManagerClient.builder().region(Region.EU_CENTRAL_1).build();
    // Get an instance of the Secrets Provider
    SecretsProvider secretsProvider = ParamManager.getSecretsProvider(client);

    // Retrieve a single secret
    String value = secretsProvider.get("/my/secret");

}

```

## DynamoDB

To get secrets stored in DynamoDB, use `getDynamoDbProvider`, providing the name of the table that contains the secrets. As with the other providers, an overloaded methods allows you to retrieve a `DynamoDbProvider` providing a client if you need to configure it yourself.

```
import software.amazon.lambda.powertools.parameters.DynamoDbProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithDynamoDbParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the DynamoDbProvider
    DynamoDbProvider ddbProvider = ParamManager.getDynamoDbProvider("my-parameters-table");

    // Retrieve a single parameter
    String value = ddbProvider.get("my-key"); 
} 

```

```
import software.amazon.lambda.powertools.parameters.DynamoDbProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;

public class AppWithDynamoDbParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get a DynamoDB Client with an explicit region
    DynamoDbClient ddbClient = DynamoDbClient.builder()
            .httpClientBuilder(UrlConnectionHttpClient.builder())
            .region(Region.EU_CENTRAL_2)
            .build();

    // Get an instance of the DynamoDbProvider
    DynamoDbProvider provider = ParamManager.getDynamoDbProvider(ddbClient, "test-table");

    // Retrieve a single parameter
    String value = ddbProvider.get("my-key"); 
} 

```

## AppConfig

To get parameters stored in AppConfig, use `getAppConfigProvider`, providing the application and environment name to retrieve configuration from. As with the other providers, an overloaded method allows you to retrieve an `AppConfigProvider` providing a client if you need to configure it yourself.

```
import software.amazon.lambda.powertools.parameters.AppConfigProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWitAppConfigParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the AppConfigProvider
    AppConfigProvider appConfigProvider = ParamManager.getAppConfigProvider("my-environment", "my-app");

    // Retrieve a single parameter
    String value = appConfigProvider.get("my-key"); 
} 

```

```
import software.amazon.lambda.powertools.parameters.AppConfigProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;
import software.amazon.awssdk.services.appconfigdata.AppConfigDataClient;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;

public class AppWithDynamoDbParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an AppConfig Client with an explicit region
    AppConfigDataClient appConfigDataClient = AppConfigDataClient.builder()
            .httpClientBuilder(UrlConnectionHttpClient.builder())
            .region(Region.EU_CENTRAL_2)
            .build();

    // Get an instance of the DynamoDbProvider
    AppConfigProvider appConfigProvider = ParamManager.getAppConfigProvider(appConfigDataClient, "my-environment", "my-app");

    // Retrieve a single parameter
    String value = appConfigProvider.get("my-key"); 
} 

```

## Advanced configuration

### Caching

By default, all parameters and their corresponding values are cached for 5 seconds.

You can customize this default value using `defaultMaxAge`. You can also customize this value for each parameter using `withMaxAge`.

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the Secrets Provider
    SecretsProvider secretsProvider = ParamManager.getSecretsProvider()
                                                  .defaultMaxAge(10, ChronoUnit.SECONDS);

    String value = secretsProvider.get("/my/secret");

}

```

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    SecretsManagerClient client = SecretsManagerClient.builder().region(Region.EU_CENTRAL_1).build();

    SecretsProvider secretsProvider = ParamManager.getSecretsProvider(client);

    String value = secretsProvider.withMaxAge(10, ChronoUnit.SECONDS).get("/my/secret");

}

```

### Transform values

Parameter values can be transformed using `withTransformation(transformerClass)`. Base64 and JSON transformations are provided. For more complex transformation, you need to specify how to deserialize-

`SSMProvider.getMultiple()` does not support transformation and will return simple Strings.

```
   String value = provider
                    .withTransformation(Transformer.base64)
                    .get("/my/parameter/b64");

```

```
   MyObj object = provider
                    .withTransformation(Transformer.json)
                    .get("/my/parameter/json", MyObj.class);

```

## Write your own Transformer

You can write your own transformer, by implementing the `Transformer` interface and the `applyTransformation()` method. For example, if you wish to deserialize XML into an object.

```
public class XmlTransformer<T> implements Transformer<T> {

    private final XmlMapper mapper = new XmlMapper();

    @Override
    public T applyTransformation(String value, Class<T> targetClass) throws TransformationException {
        try {
            return mapper.readValue(value, targetClass);
        } catch (IOException e) {
            throw new TransformationException(e);
        }
    }
}

```

```
    MyObj object = provider
                        .withTransformation(XmlTransformer.class)
                        .get("/my/parameter/xml", MyObj.class);

```

### Fluent API

To simplify the use of the library, you can chain all method calls before a get.

```
    ssmProvider
      .defaultMaxAge(10, SECONDS)     // will set 10 seconds as the default cache TTL
      .withMaxAge(1, MINUTES)         // will set the cache TTL for this value at 1 minute
      .withTransformation(json)       // json is a static import from Transformer.json
      .withDecryption()               // enable decryption of the parameter value
      .get("/my/param", MyObj.class); // finally get the value

```

## Create your own provider

You can create your own custom parameter store provider by inheriting the `BaseProvider` class and implementing the `String getValue(String key)` method to retrieve data from your underlying store. All transformation and caching logic is handled by the get() methods in the base class.

```
public class S3Provider extends BaseProvider {

    private final S3Client client;
    private String bucket;

    S3Provider(CacheManager cacheManager) {
        this(cacheManager, S3Client.create());
    }

    S3Provider(CacheManager cacheManager, S3Client client) {
        super(cacheManager);
        this.client = client;
    }

    public S3Provider withBucket(String bucket) {
        this.bucket = bucket;
        return this;
    }

    @Override
    protected String getValue(String key) {
        if (bucket == null) {
            throw new IllegalStateException("A bucket must be specified, using withBucket() method");
        }

        GetObjectRequest request = GetObjectRequest.builder().bucket(bucket).key(key).build();
        ResponseBytes<GetObjectResponse> response = client.getObject(request, ResponseTransformer.toBytes());
        return response.asUtf8String();
    }

    @Override
    protected Map<String, String> getMultipleValues(String path) {
        if (bucket == null) {
            throw new IllegalStateException("A bucket must be specified, using withBucket() method");
        }

        ListObjectsV2Request listRequest = ListObjectsV2Request.builder().bucket(bucket).prefix(path).build();
        List<S3Object> s3Objects = client.listObjectsV2(listRequest).contents();

        Map<String, String> result = new HashMap<>();
        s3Objects.forEach(s3Object -> {
            result.put(s3Object.key(), getValue(s3Object.key()));
        });

        return result;
    }

    @Override
    protected void resetToDefaults() {
        super.resetToDefaults();
        bucket = null;
    }

}

```

```
    S3Provider provider = new S3Provider(ParamManager.getCacheManager());

    provider.setTransformationManager(ParamManager.getTransformationManager());

    String value = provider.withBucket("myBucket").get("myKey");

```

## Annotation

You can make use of the annotation `@Param` to inject a parameter value in a variable.

By default, it will use `SSMProvider` to retrieve the value from AWS System Manager Parameter Store. You could specify a different provider as long as it extends `BaseProvider` and/or a `Transformer`.

```
public class AppWithAnnotation implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Param(key = "/my/parameter/json")
    ObjectToDeserialize value;

}

```

```
public class AppWithAnnotation implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Param(key = "/my/parameter/json" provider = SecretsProvider.class, transformer = JsonTransformer.class)
    ObjectToDeserialize value;

}

```

In this case `SecretsProvider` will be used to retrieve a raw value that is then transformed into the target Object by using `JsonTransformer`. To show the convenience of the annotation compare the following two code snippets.

### Install

If you want to use the `@Param` annotation in your project add configuration to compile-time weave (CTW) the powertools-parameters aspects into your project.

```
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 ...
                 <aspectLibraries>
                     ...
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-parameters</artifactId>
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
plugins{
    id 'java'
    id 'io.freefair.aspectj.post-compile-weaving' version '6.3.0'
}

repositories {
    mavenCentral()
}

dependencies {
    ...
    aspect 'software.amazon.lambda:powertools-parameters:1.20.2'
    implementation 'org.aspectj:aspectjrt:1.9.19'
}

```

This module contains a set of utilities you may use in your Lambda functions, to manipulate JSON.

## Easy deserialization

### Key features

- Easily deserialize the main content of an event (for example, the body of an API Gateway event)
- 15+ built-in events (see the [list below](#built-in-events))

### Getting started

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-serialization</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>

```

```
implementation 'software.amazon.lambda:powertools-serialization:1.20.2'

```

### EventDeserializer

The `EventDeserializer` can be used to extract the main part of an event (body, message, records) and deserialize it from JSON to your desired type.

It can handle single elements like the body of an API Gateway event:

```
import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;

public class APIGWHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(
            final APIGatewayProxyRequestEvent event, 
            final Context context) {

        Product product = extractDataFrom(event).as(Product.class);

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
    "body": "{\"id\":1234, \"name\":\"product\", \"price\":42}",
    "resource": "/{proxy+}",
    "path": "/path/to/resource",
    "httpMethod": "POST",
    "isBase64Encoded": false,
    "queryStringParameters": {
        "foo": "bar"
    },
    "pathParameters": {
        "proxy": "/path/to/resource"
    },
    "stageVariables": {
        "baz": "qux"
    },
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Custom User Agent String",
        "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
        "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https"
    },
    "requestContext": {
        "accountId": "123456789012",
        "resourceId": "123456",
        "stage": "prod",
        "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
        "requestTime": "09/Apr/2015:12:34:56 +0000",
        "requestTimeEpoch": 1428582896000,
        "identity": {
        "cognitoIdentityPoolId": null,
        "accountId": null,
        "cognitoIdentityId": null,
        "caller": null,
        "accessKey": null,
        "sourceIp": "127.0.0.1",
        "cognitoAuthenticationType": null,
        "cognitoAuthenticationProvider": null,
        "userArn": null,
        "userAgent": "Custom User Agent String",
        "user": null
    },
    "path": "/prod/path/to/resource",
    "resourcePath": "/{proxy+}",
    "httpMethod": "POST",
    "apiId": "1234567890",
    "protocol": "HTTP/1.1"
    }
}

```

It can also handle a collection of elements like the records of an SQS event:

```
import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;

public class SQSHandler implements RequestHandler<SQSEvent, String> {

    public String handleRequest(
            final SQSEvent event, 
            final Context context) {

        List<Product> products = extractDataFrom(event).asListOf(Product.class);

    }

```

```
{
    "Records": [
      {
        "messageId": "d9144555-9a4f-4ec3-99a0-34ce359b4b54",
        "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
        "body": "{  \"id\": 1234,  \"name\": \"product\",  \"price\": 42}",
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
        "messageId": "d9144555-9a4f-4ec3-99a0-34ce359b4b54",
        "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
        "body": "{  \"id\": 12345,  \"name\": \"product5\",  \"price\": 45}",
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
      }
    ]
}

```

Tip

In the background, `EventDeserializer` is using Jackson. The `ObjectMapper` is configured in `JsonConfig`. You can customize the configuration of the mapper if needed: `JsonConfig.get().getObjectMapper()`. Using this feature, you don't need to add Jackson to your project and create another instance of `ObjectMapper`.

### Built-in events

| Event Type | Path to the content | List | | --- | --- | --- | | `APIGatewayProxyRequestEvent` | `body` | | | `APIGatewayV2HTTPEvent` | `body` | | | `SNSEvent` | `Records[0].Sns.Message` | | | `SQSEvent` | `Records[*].body` | x | | `ScheduledEvent` | `detail` | | | `ApplicationLoadBalancerRequestEvent` | `body` | | | `CloudWatchLogsEvent` | `powertools_base64_gzip(data)` | | | `CloudFormationCustomResourceEvent` | `resourceProperties` | | | `KinesisEvent` | `Records[*].kinesis.powertools_base64(data)` | x | | `KinesisFirehoseEvent` | `Records[*].powertools_base64(data)` | x | | `KafkaEvent` | `records[*].values[*].powertools_base64(value)` | x | | `ActiveMQEvent` | `messages[*].powertools_base64(data)` | x | | `RabbitMQEvent` | `rmqMessagesByQueue[*].values[*].powertools_base64(data)` | x | | `KinesisAnalyticsFirehoseInputPreprocessingEvent` | `Records[*].kinesis.powertools_base64(data)` | x | | `KinesisAnalyticsStreamsInputPreprocessingEvent` | `Records[*].kinesis.powertools_base64(data)` | x |

## JMESPath functions

Tip

[JMESPath](https://jmespath.org/) is a query language for JSON used by AWS CLI and Powertools for AWS Lambda (Java) to get a specific part of a json.

### Key features

- Deserialize JSON from JSON strings, base64, and compressed data
- Use JMESPath to extract and combine data recursively

### Getting started

You might have events that contain encoded JSON payloads as string, base64, or even in compressed format. It is a common use case to decode and extract them partially or fully as part of your Lambda function invocation.

You will generally use this in combination with other Powertools for AWS Lambda (Java) modules ([validation](../validation/) and [idempotency](../idempotency/)) where you might need to extract a portion of your data before using them.

### Built-in functions

Powertools for AWS Lambda (Java) provides the following JMESPath Functions to easily deserialize common encoded JSON payloads in Lambda functions:

#### powertools_json function

Use `powertools_json` function to decode any JSON string anywhere a JMESPath expression is allowed.

Below example use this function to load the content from the body of an API Gateway request event as a JSON object and retrieve the id field in it:

```
public class MyHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

  public MyHandler() {
    Idempotency.config()
    .withConfig(
        IdempotencyConfig.builder()
          .withEventKeyJMESPath("powertools_json(body).id")
          .build())
    .withPersistenceStore(
        DynamoDBPersistenceStore.builder()
          .withTableName(System.getenv("TABLE_NAME"))
          .build())
    .configure();
}

@Idempotent
public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent event, final Context context) {
}

```

```
{
  "body": "{\"message\": \"Lambda rocks\", \"id\": 43876123454654}",
  "resource": "/{proxy+}",
  "path": "/path/to/resource",
  "httpMethod": "POST",
  "queryStringParameters": {
    "foo": "bar"
  },
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "max-age=0",
  },
  "requestContext": {
    "accountId": "123456789012",
    "resourceId": "123456",
    "stage": "prod",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "requestTime": "09/Apr/2015:12:34:56 +0000",
    "requestTimeEpoch": 1428582896000,
    "identity": {
      "cognitoIdentityPoolId": null,
      "accountId": null,
      "cognitoIdentityId": null,
      "caller": null,
      "accessKey": null,
      "sourceIp": "127.0.0.1",
      "cognitoAuthenticationType": null,
      "cognitoAuthenticationProvider": null,
      "userArn": null,
      "userAgent": "Custom User Agent String",
      "user": null
    },
    "path": "/prod/path/to/resource",
    "resourcePath": "/{proxy+}",
    "httpMethod": "POST",
    "apiId": "1234567890",
    "protocol": "HTTP/1.1"
  }
}

```

#### powertools_base64 function

Use `powertools_base64` function to decode any base64 data.

Below sample will decode the base64 value within the `data` key, and decode the JSON string into a valid JSON before we can validate it.

```
import software.amazon.lambda.powertools.validation.ValidationUtils;

public class MyEventHandler implements RequestHandler<MyEvent, String> {

    @Override
    public String handleRequest(MyEvent myEvent, Context context) {
        validate(myEvent, "classpath:/schema.json", "powertools_base64(data)");
        return "OK";
   }
}

```

```
{
"data" : "ewogICJpZCI6IDQzMjQyLAogICJuYW1lIjogIkZvb0JhciBYWSIsCiAgInByaWNlIjogMjU4Cn0="
}

```

#### powertools_base64_gzip function

Use `powertools_base64_gzip` function to decompress and decode base64 data.

Below sample will decompress and decode base64 data.

```
import software.amazon.lambda.powertools.validation.ValidationUtils;

public class MyEventHandler implements RequestHandler<MyEvent, String> {

    @Override
    public String handleRequest(MyEvent myEvent, Context context) {
        validate(myEvent, "classpath:/schema.json", "powertools_base64_gzip(data)");
        return "OK";
   }
}

```

```
{
   "data" : "H4sIAAAAAAAA/6vmUlBQykxRslIwMTYyMdIBcfMSc1OBAkpu+flOiUUKEZFKYOGCosxkkLiRqQVXLQDnWo6bOAAAAA=="
}

```

### Bring your own JMESPath function

Warning

This should only be used for advanced use cases where you have special formats not covered by the built-in functions. Please open an issue in Github if you need us to add some common functions.

Your function must extend `io.burt.jmespath.function.BaseFunction`, take a String as parameter and return a String. You can read the [doc](https://github.com/burtcorp/jmespath-java#adding-custom-functions) for more information.

Below is an example that takes some xml and transform it into json. Once your function is created, you need to add it to powertools.You can then use it to do your validation or in idempotency module.

```
public class XMLFunction extends BaseFunction {
    public Base64Function() {
        super("powertools_xml", ArgumentConstraints.typeOf(JmesPathType.STRING));
    }

    @Override
    protected <T> T callFunction(Adapter<T> runtime, List<FunctionArgument<T>> arguments) {
        T value = arguments.get(0).value();
        String xmlString = runtime.toString(value);

        String jsonString =  // ... transform xmlString to json

        return runtime.createString(jsonString);
    }
}

```

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.ValidationUtils.validate;

static {
    JsonConfig.get().addFunction(new XMLFunction());
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        validate(myEvent, "classpath:/schema.json", "powertools_xml(path.to.xml_data)");
        return "OK";
   }
}

```

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.Validation;

static {
    JsonConfig.get().addFunction(new XMLFunction());
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    @Validation(inboundSchema="classpath:/schema.json", envelope="powertools_xml(path.to.xml_data)")
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        return "OK";
   }
}

```

This utility provides JSON Schema validation for payloads held within events and response used in AWS Lambda.

**Key features**

- Validate incoming events and responses
- Built-in validation for most common events (API Gateway, SNS, SQS, ...)
- JMESPath support validate only a sub part of the event

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-validation</artifactId>
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
                         <artifactId>powertools-validation</artifactId>
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
        <artifactId>powertools-validation</artifactId>
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
                         <artifactId>powertools-validation</artifactId>
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
        aspect 'software.amazon.lambda:powertools-validation:1.20.2'
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
        aspect 'software.amazon.lambda:powertools-validation:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Validating events

You can validate inbound and outbound events using `@Validation` annotation.

You can also use the `Validator#validate()` methods, if you want more control over the validation process such as handling a validation error.

We support JSON schema version 4, 6, 7 and 201909 (from [jmespath-jackson library](https://github.com/burtcorp/jmespath-java)).

### Validation annotation

`@Validation` annotation is used to validate either inbound events or functions' response.

It will fail fast with `ValidationException` if an event or response doesn't conform with given JSON Schema.

While it is easier to specify a json schema file in the classpath (using the notation `"classpath:/path/to/schema.json"`), you can also provide a JSON String containing the schema.

```
import software.amazon.lambda.powertools.validation.Validation;

public class MyFunctionHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Override
    @Validation(inboundSchema = "classpath:/schema_in.json", outboundSchema = "classpath:/schema_out.json")
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        // ...
        return something;
    }
}

```

Note

It is not a requirement to validate both inbound and outbound schemas - You can either use one, or both.

### Validate function

Validate standalone function is used within the Lambda handler, or any other methods that perform data validation.

You can also gracefully handle schema validation errors by catching `ValidationException`.

```
import static software.amazon.lambda.powertools.validation.ValidationUtils.*;

public class MyFunctionHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        try {
            validate(input, "classpath:/schema.json");
        } catch (ValidationException ex) {
            // do something before throwing it
            throw ex;
        }

        // ...
        return something;
    }
}

```

Note

Schemas are stored in memory for re-use, to avoid loading them from file each time.

## Built-in events and responses

For the following events and responses, the Validator will automatically perform validation on the content.

**Events**

| Type of event | Class | Path to content | | --- | --- | --- | | API Gateway REST | APIGatewayProxyRequestEvent | `body` | | API Gateway HTTP | APIGatewayV2HTTPEvent | `body` | | Application Load Balancer | ApplicationLoadBalancerRequestEvent | `body` | | Cloudformation Custom Resource | CloudFormationCustomResourceEvent | `resourceProperties` | | CloudWatch Logs | CloudWatchLogsEvent | `awslogs.powertools_base64_gzip(data)` | | EventBridge / Cloudwatch | ScheduledEvent | `detail` | | Kafka | KafkaEvent | `records[*][*].value` | | Kinesis | KinesisEvent | `Records[*].kinesis.powertools_base64(data)` | | Kinesis Firehose | KinesisFirehoseEvent | `Records[*].powertools_base64(data)` | | Kinesis Analytics from Firehose | KinesisAnalyticsFirehoseInputPreprocessingEvent | `Records[*].powertools_base64(data)` | | Kinesis Analytics from Streams | KinesisAnalyticsStreamsInputPreprocessingEvent | `Records[*].powertools_base64(data)` | | SNS | SNSEvent | `Records[*].Sns.Message` | | SQS | SQSEvent | `Records[*].body` |

**Responses**

| Type of response | Class | Path to content (envelope) | | --- | --- | --- | | API Gateway REST | APIGatewayProxyResponseEvent} | `body` | | API Gateway HTTP | APIGatewayV2HTTPResponse} | `body` | | API Gateway WebSocket | APIGatewayV2WebSocketResponse} | `body` | | Load Balancer | ApplicationLoadBalancerResponseEvent} | `body` | | Kinesis Analytics | KinesisAnalyticsInputPreprocessingResponse} | \`Records[\*].powertools_base64(data)\`\` |

## Custom events and responses

You can also validate any Event or Response type, once you have the appropriate schema.

Sometimes, you might want to validate only a portion of it - This is where the envelope parameter is for.

Envelopes are [JMESPath expressions](https://jmespath.org/tutorial.html) to extract a portion of JSON you want before applying JSON Schema validation.

```
import software.amazon.lambda.powertools.validation.Validation;

public class MyCustomEventHandler implements RequestHandler<MyCustomEvent, String> {

    @Override
    @Validation(inboundSchema = "classpath:/my_custom_event_schema.json",
                envelope = "basket.products[*]")
    public String handleRequest(MyCustomEvent input, Context context) {
        return "OK";
    }
}

```

```
{
  "basket": {
    "products" : [
      {
        "id": 43242,
        "name": "FooBar XY",
        "price": 258
      },
      {
        "id": 765,
        "name": "BarBaz AB",
        "price": 43.99
      }
    ]
  }
}

```

This is quite powerful because you can use JMESPath Query language to extract records from [arrays, slice and dice](https://jmespath.org/tutorial.html#list-and-slice-projections), to [pipe expressions](https://jmespath.org/tutorial.html#pipe-expressions) and [function](https://jmespath.org/tutorial.html#functions) expressions, where you'd extract what you need before validating the actual payload.

## Change the schema version

By default, powertools-validation is configured with [V7](https://json-schema.org/draft-07/json-schema-release-notes.html). You can use the `ValidationConfig` to change that behaviour.

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.Validation;

static {
    ValidationConfig.get().setSchemaVersion(SpecVersion.VersionFlag.V4);
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    @Validation(inboundSchema="classpath:/schema.json", envelope="powertools_xml(path.to.xml_data)")
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        return "OK";
   }
}

```

## Advanced ObjectMapper settings

If you need to configure the Jackson ObjectMapper, you can use the `ValidationConfig`:

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.Validation;

static {
    ObjectMapper objectMapper= ValidationConfig.get().getObjectMapper();
    // update (de)serializationConfig or other properties
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    @Validation(inboundSchema="classpath:/schema.json", envelope="powertools_xml(path.to.xml_data)")
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        return "OK";
   }
}

```