# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_sqs_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_sqs_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

ActionsScenariosServerless examples

# Amazon SQS examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon SQS.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using Amazon SQS.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/sqs#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    )
    
    // main uses the AWS SDK for Go V2 to create an Amazon Simple Queue Service
    // (Amazon SQS) client and list the queues in your account.
    // This example uses the default settings specified in your shared credentials
    // and config files.
    func main() {
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
    		fmt.Println(err)
    		return
    	}
    	sqsClient := sqs.NewFromConfig(sdkConfig)
    	fmt.Println("Let's list the queues for your account.")
    	var queueUrls []string
    	paginator := sqs.NewListQueuesPaginator(sqsClient, &sqs.ListQueuesInput{})
    	for paginator.HasMorePages() {
    		output, err := paginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get queues. Here's why: %v\n", err)
    			break
    		} else {
    			queueUrls = append(queueUrls, output.QueueUrls...)
    		}
    	}
    	if len(queueUrls) == 0 {
    		fmt.Println("You don't have any queues!")
    	} else {
    		for _, queueUrl := range queueUrls {
    			fmt.Printf("\t%v\n", queueUrl)
    		}
    	}
    }
    
    
    

  * For API details, see [ListQueues](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.ListQueues) in _AWS SDK for Go API Reference_. 




###### Topics

  * Actions

  * Scenarios

  * Serverless examples




## Actions

The following code example shows how to use `CreateQueue`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    )
    
    // SqsActions encapsulates the Amazon Simple Queue Service (Amazon SQS) actions
    // used in the examples.
    type SqsActions struct {
    	SqsClient *sqs.Client
    }
    
    
    
    // CreateQueue creates an Amazon SQS queue with the specified name. You can specify
    // whether the queue is created as a FIFO queue.
    func (actor SqsActions) CreateQueue(ctx context.Context, queueName string, isFifoQueue bool) (string, error) {
    	var queueUrl string
    	queueAttributes := map[string]string{}
    	if isFifoQueue {
    		queueAttributes["FifoQueue"] = "true"
    	}
    	queue, err := actor.SqsClient.CreateQueue(ctx, &sqs.CreateQueueInput{
    		QueueName:  aws.String(queueName),
    		Attributes: queueAttributes,
    	})
    	if err != nil {
    		log.Printf("Couldn't create queue %v. Here's why: %v\n", queueName, err)
    	} else {
    		queueUrl = *queue.QueueUrl
    	}
    
    	return queueUrl, err
    }
    
    
    

  * For API details, see [CreateQueue](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.CreateQueue) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteMessageBatch`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    )
    
    // SqsActions encapsulates the Amazon Simple Queue Service (Amazon SQS) actions
    // used in the examples.
    type SqsActions struct {
    	SqsClient *sqs.Client
    }
    
    
    
    // DeleteMessages uses the DeleteMessageBatch action to delete a batch of messages from
    // an Amazon SQS queue.
    func (actor SqsActions) DeleteMessages(ctx context.Context, queueUrl string, messages []types.Message) error {
    	entries := make([]types.DeleteMessageBatchRequestEntry, len(messages))
    	for msgIndex := range messages {
    		entries[msgIndex].Id = aws.String(fmt.Sprintf("%v", msgIndex))
    		entries[msgIndex].ReceiptHandle = messages[msgIndex].ReceiptHandle
    	}
    	_, err := actor.SqsClient.DeleteMessageBatch(ctx, &sqs.DeleteMessageBatchInput{
    		Entries:  entries,
    		QueueUrl: aws.String(queueUrl),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete messages from queue %v. Here's why: %v\n", queueUrl, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteMessageBatch](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.DeleteMessageBatch) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteQueue`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    )
    
    // SqsActions encapsulates the Amazon Simple Queue Service (Amazon SQS) actions
    // used in the examples.
    type SqsActions struct {
    	SqsClient *sqs.Client
    }
    
    
    
    // DeleteQueue deletes an Amazon SQS queue.
    func (actor SqsActions) DeleteQueue(ctx context.Context, queueUrl string) error {
    	_, err := actor.SqsClient.DeleteQueue(ctx, &sqs.DeleteQueueInput{
    		QueueUrl: aws.String(queueUrl)})
    	if err != nil {
    		log.Printf("Couldn't delete queue %v. Here's why: %v\n", queueUrl, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteQueue](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.DeleteQueue) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetQueueAttributes`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    )
    
    // SqsActions encapsulates the Amazon Simple Queue Service (Amazon SQS) actions
    // used in the examples.
    type SqsActions struct {
    	SqsClient *sqs.Client
    }
    
    
    
    // GetQueueArn uses the GetQueueAttributes action to get the Amazon Resource Name (ARN)
    // of an Amazon SQS queue.
    func (actor SqsActions) GetQueueArn(ctx context.Context, queueUrl string) (string, error) {
    	var queueArn string
    	arnAttributeName := types.QueueAttributeNameQueueArn
    	attribute, err := actor.SqsClient.GetQueueAttributes(ctx, &sqs.GetQueueAttributesInput{
    		QueueUrl:       aws.String(queueUrl),
    		AttributeNames: []types.QueueAttributeName{arnAttributeName},
    	})
    	if err != nil {
    		log.Printf("Couldn't get ARN for queue %v. Here's why: %v\n", queueUrl, err)
    	} else {
    		queueArn = attribute.Attributes[string(arnAttributeName)]
    	}
    	return queueArn, err
    }
    
    
    

  * For API details, see [GetQueueAttributes](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.GetQueueAttributes) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListQueues`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/sqs#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    )
    
    // main uses the AWS SDK for Go V2 to create an Amazon Simple Queue Service
    // (Amazon SQS) client and list the queues in your account.
    // This example uses the default settings specified in your shared credentials
    // and config files.
    func main() {
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
    		fmt.Println(err)
    		return
    	}
    	sqsClient := sqs.NewFromConfig(sdkConfig)
    	fmt.Println("Let's list the queues for your account.")
    	var queueUrls []string
    	paginator := sqs.NewListQueuesPaginator(sqsClient, &sqs.ListQueuesInput{})
    	for paginator.HasMorePages() {
    		output, err := paginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get queues. Here's why: %v\n", err)
    			break
    		} else {
    			queueUrls = append(queueUrls, output.QueueUrls...)
    		}
    	}
    	if len(queueUrls) == 0 {
    		fmt.Println("You don't have any queues!")
    	} else {
    		for _, queueUrl := range queueUrls {
    			fmt.Printf("\t%v\n", queueUrl)
    		}
    	}
    }
    
    
    

  * For API details, see [ListQueues](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.ListQueues) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ReceiveMessage`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    )
    
    // SqsActions encapsulates the Amazon Simple Queue Service (Amazon SQS) actions
    // used in the examples.
    type SqsActions struct {
    	SqsClient *sqs.Client
    }
    
    
    
    // GetMessages uses the ReceiveMessage action to get messages from an Amazon SQS queue.
    func (actor SqsActions) GetMessages(ctx context.Context, queueUrl string, maxMessages int32, waitTime int32) ([]types.Message, error) {
    	var messages []types.Message
    	result, err := actor.SqsClient.ReceiveMessage(ctx, &sqs.ReceiveMessageInput{
    		QueueUrl:            aws.String(queueUrl),
    		MaxNumberOfMessages: maxMessages,
    		WaitTimeSeconds:     waitTime,
    	})
    	if err != nil {
    		log.Printf("Couldn't get messages from queue %v. Here's why: %v\n", queueUrl, err)
    	} else {
    		messages = result.Messages
    	}
    	return messages, err
    }
    
    
    

  * For API details, see [ReceiveMessage](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.ReceiveMessage) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `SetQueueAttributes`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    )
    
    // SqsActions encapsulates the Amazon Simple Queue Service (Amazon SQS) actions
    // used in the examples.
    type SqsActions struct {
    	SqsClient *sqs.Client
    }
    
    
    
    // AttachSendMessagePolicy uses the SetQueueAttributes action to attach a policy to an
    // Amazon SQS queue that allows the specified Amazon SNS topic to send messages to the
    // queue.
    func (actor SqsActions) AttachSendMessagePolicy(ctx context.Context, queueUrl string, queueArn string, topicArn string) error {
    	policyDoc := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:    "Allow",
    			Action:    "sqs:SendMessage",
    			Principal: map[string]string{"Service": "sns.amazonaws.com"},
    			Resource:  aws.String(queueArn),
    			Condition: PolicyCondition{"ArnEquals": map[string]string{"aws:SourceArn": topicArn}},
    		}},
    	}
    	policyBytes, err := json.Marshal(policyDoc)
    	if err != nil {
    		log.Printf("Couldn't create policy document. Here's why: %v\n", err)
    		return err
    	}
    	_, err = actor.SqsClient.SetQueueAttributes(ctx, &sqs.SetQueueAttributesInput{
    		Attributes: map[string]string{
    			string(types.QueueAttributeNamePolicy): string(policyBytes),
    		},
    		QueueUrl: aws.String(queueUrl),
    	})
    	if err != nil {
    		log.Printf("Couldn't set send message policy on queue %v. Here's why: %v\n", queueUrl, err)
    	}
    	return err
    }
    
    // PolicyDocument defines a policy document as a Go struct that can be serialized
    // to JSON.
    type PolicyDocument struct {
    	Version   string
    	Statement []PolicyStatement
    }
    
    // PolicyStatement defines a statement in a policy document.
    type PolicyStatement struct {
    	Effect    string
    	Action    string
    	Principal map[string]string `json:",omitempty"`
    	Resource  *string           `json:",omitempty"`
    	Condition PolicyCondition   `json:",omitempty"`
    }
    
    // PolicyCondition defines a condition in a policy.
    type PolicyCondition map[string]map[string]string
    
    
    

  * For API details, see [SetQueueAttributes](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.SetQueueAttributes) in _AWS SDK for Go API Reference_. 




## Scenarios

The following code example shows how to:

  * Create topic (FIFO or non-FIFO).

  * Subscribe several queues to the topic with an option to apply a filter.

  * Publish messages to the topic.

  * Poll the queues for messages received.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples). 

Run an interactive scenario at a command prompt.
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    	"strings"
    	"topics_and_queues/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sns"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    const FIFO_SUFFIX = ".fifo"
    const TONE_KEY = "tone"
    
    var ToneChoices = []string{"cheerful", "funny", "serious", "sincere"}
    
    // MessageBody is used to deserialize the body of a message from a JSON string.
    type MessageBody struct {
    	Message string
    }
    
    // ScenarioRunner separates the steps of this scenario into individual functions so that
    // they are simpler to read and understand.
    type ScenarioRunner struct {
    	questioner demotools.IQuestioner
    	snsActor   *actions.SnsActions
    	sqsActor   *actions.SqsActions
    }
    
    func (runner ScenarioRunner) CreateTopic(ctx context.Context) (string, string, bool, bool) {
    	log.Println("SNS topics can be configured as FIFO (First-In-First-Out) or standard.\n" +
    		"FIFO topics deliver messages in order and support deduplication and message filtering.")
    	isFifoTopic := runner.questioner.AskBool("\nWould you like to work with FIFO topics? (y/n) ", "y")
    
    	contentBasedDeduplication := false
    	if isFifoTopic {
    		log.Println(strings.Repeat("-", 88))
    		log.Println("Because you have chosen a FIFO topic, deduplication is supported.\n" +
    			"Deduplication IDs are either set in the message or are automatically generated\n" +
    			"from content using a hash function. If a message is successfully published to\n" +
    			"an SNS FIFO topic, any message published and determined to have the same\n" +
    			"deduplication ID, within the five-minute deduplication interval, is accepted\n" +
    			"but not delivered. For more information about deduplication, see:\n" +
    			"\thttps://docs.aws.amazon.com/sns/latest/dg/fifo-message-dedup.html.")
    		contentBasedDeduplication = runner.questioner.AskBool(
    			"\nDo you want to use content-based deduplication instead of entering a deduplication ID? (y/n) ", "y")
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	topicName := runner.questioner.Ask("Enter a name for your SNS topic. ")
    	if isFifoTopic {
    		topicName = fmt.Sprintf("%v%v", topicName, FIFO_SUFFIX)
    		log.Printf("Because you have selected a FIFO topic, '%v' must be appended to\n"+
    			"the topic name.", FIFO_SUFFIX)
    	}
    
    	topicArn, err := runner.snsActor.CreateTopic(ctx, topicName, isFifoTopic, contentBasedDeduplication)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Your new topic with the name '%v' and Amazon Resource Name (ARN) \n"+
    		"'%v' has been created.", topicName, topicArn)
    
    	return topicName, topicArn, isFifoTopic, contentBasedDeduplication
    }
    
    func (runner ScenarioRunner) CreateQueue(ctx context.Context, ordinal string, isFifoTopic bool) (string, string) {
    	queueName := runner.questioner.Ask(fmt.Sprintf("Enter a name for the %v SQS queue. ", ordinal))
    	if isFifoTopic {
    		queueName = fmt.Sprintf("%v%v", queueName, FIFO_SUFFIX)
    		if ordinal == "first" {
    			log.Printf("Because you are creating a FIFO SQS queue, '%v' must "+
    				"be appended to the queue name.\n", FIFO_SUFFIX)
    		}
    	}
    	queueUrl, err := runner.sqsActor.CreateQueue(ctx, queueName, isFifoTopic)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Your new SQS queue with the name '%v' and the queue URL "+
    		"'%v' has been created.", queueName, queueUrl)
    
    	return queueName, queueUrl
    }
    
    func (runner ScenarioRunner) SubscribeQueueToTopic(
    	ctx context.Context, queueName string, queueUrl string, topicName string, topicArn string, ordinal string,
    	isFifoTopic bool) (string, bool) {
    
    	queueArn, err := runner.sqsActor.GetQueueArn(ctx, queueUrl)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("The ARN of your queue is: %v.\n", queueArn)
    
    	err = runner.sqsActor.AttachSendMessagePolicy(ctx, queueUrl, queueArn, topicArn)
    	if err != nil {
    		panic(err)
    	}
    	log.Println("Attached an IAM policy to the queue so the SNS topic can send " +
    		"messages to it.")
    	log.Println(strings.Repeat("-", 88))
    
    	var filterPolicy map[string][]string
    	if isFifoTopic {
    		if ordinal == "first" {
    			log.Println("Subscriptions to a FIFO topic can have filters.\n" +
    				"If you add a filter to this subscription, then only the filtered messages\n" +
    				"will be received in the queue.\n" +
    				"For information about message filtering, see\n" +
    				"\thttps://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html\n" +
    				"For this example, you can filter messages by a \"tone\" attribute.")
    		}
    
    		wantFiltering := runner.questioner.AskBool(
    			fmt.Sprintf("Do you want to filter messages that are sent to \"%v\"\n"+
    				"from the %v topic? (y/n) ", queueName, topicName), "y")
    		if wantFiltering {
    			log.Println("You can filter messages by one or more of the following \"tone\" attributes.")
    
    			var toneSelections []string
    			askAboutTones := true
    			for askAboutTones {
    				toneIndex := runner.questioner.AskChoice(
    					"Enter the number of the tone you want to filter by:\n", ToneChoices)
    				toneSelections = append(toneSelections, ToneChoices[toneIndex])
    				askAboutTones = runner.questioner.AskBool("Do you want to add another tone to the filter? (y/n) ", "y")
    			}
    			log.Printf("Your subscription will be filtered to only pass the following tones: %v\n", toneSelections)
    			filterPolicy = map[string][]string{TONE_KEY: toneSelections}
    		}
    	}
    
    	subscriptionArn, err := runner.snsActor.SubscribeQueue(ctx, topicArn, queueArn, filterPolicy)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("The queue %v is now subscribed to the topic %v with the subscription ARN %v.\n",
    		queueName, topicName, subscriptionArn)
    
    	return subscriptionArn, filterPolicy != nil
    }
    
    func (runner ScenarioRunner) PublishMessages(ctx context.Context, topicArn string, isFifoTopic bool, contentBasedDeduplication bool, usingFilters bool) {
    	var message string
    	var groupId string
    	var dedupId string
    	var toneSelection string
    	publishMore := true
    	for publishMore {
    		groupId = ""
    		dedupId = ""
    		toneSelection = ""
    		message = runner.questioner.Ask("Enter a message to publish: ")
    		if isFifoTopic {
    			log.Println("Because you are using a FIFO topic, you must set a message group ID.\n" +
    				"All messages within the same group will be received in the order they were published.")
    			groupId = runner.questioner.Ask("Enter a message group ID: ")
    			if !contentBasedDeduplication {
    				log.Println("Because you are not using content-based deduplication,\n" +
    					"you must enter a deduplication ID.")
    				dedupId = runner.questioner.Ask("Enter a deduplication ID: ")
    			}
    		}
    		if usingFilters {
    			if runner.questioner.AskBool("Add a tone attribute so this message can be filtered? (y/n) ", "y") {
    				toneIndex := runner.questioner.AskChoice(
    					"Enter the number of the tone you want to filter by:\n", ToneChoices)
    				toneSelection = ToneChoices[toneIndex]
    			}
    		}
    
    		err := runner.snsActor.Publish(ctx, topicArn, message, groupId, dedupId, TONE_KEY, toneSelection)
    		if err != nil {
    			panic(err)
    		}
    		log.Println(("Your message was published."))
    
    		publishMore = runner.questioner.AskBool("Do you want to publish another messsage? (y/n) ", "y")
    	}
    }
    
    func (runner ScenarioRunner) PollForMessages(ctx context.Context, queueUrls []string) {
    	log.Println("Polling queues for messages...")
    	for _, queueUrl := range queueUrls {
    		var messages []types.Message
    		for {
    			currentMsgs, err := runner.sqsActor.GetMessages(ctx, queueUrl, 10, 1)
    			if err != nil {
    				panic(err)
    			}
    			if len(currentMsgs) == 0 {
    				break
    			}
    			messages = append(messages, currentMsgs...)
    		}
    		if len(messages) == 0 {
    			log.Printf("No messages were received by queue %v.\n", queueUrl)
    		} else if len(messages) == 1 {
    			log.Printf("One message was received by queue %v:\n", queueUrl)
    
    		} else {
    			log.Printf("%v messages were received by queue %v:\n", len(messages), queueUrl)
    		}
    		for msgIndex, message := range messages {
    			messageBody := MessageBody{}
    			err := json.Unmarshal([]byte(*message.Body), &messageBody)
    			if err != nil {
    				panic(err)
    			}
    			log.Printf("Message %v: %v\n", msgIndex+1, messageBody.Message)
    		}
    
    		if len(messages) > 0 {
    			log.Printf("Deleting %v messages from queue %v.\n", len(messages), queueUrl)
    			err := runner.sqsActor.DeleteMessages(ctx, queueUrl, messages)
    			if err != nil {
    				panic(err)
    			}
    		}
    	}
    }
    
    // RunTopicsAndQueuesScenario is an interactive example that shows you how to use the
    // AWS SDK for Go to create and use Amazon SNS topics and Amazon SQS queues.
    //
    // 1. Create a topic (FIFO or non-FIFO).
    // 2. Subscribe several queues to the topic with an option to apply a filter.
    // 3. Publish messages to the topic.
    // 4. Poll the queues for messages received.
    // 5. Delete the topic and the queues.
    //
    // This example creates service clients from the specified sdkConfig so that
    // you can replace it with a mocked or stubbed config for unit testing.
    //
    // It uses a questioner from the `demotools` package to get input during the example.
    // This package can be found in the ..\..\demotools folder of this repo.
    func RunTopicsAndQueuesScenario(
    	ctx context.Context, sdkConfig aws.Config, questioner demotools.IQuestioner) {
    	resources := Resources{}
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.\n" +
    				"Cleaning up any resources that were created...")
    			resources.Cleanup(ctx)
    		}
    	}()
    	queueCount := 2
    
    	log.Println(strings.Repeat("-", 88))
    	log.Printf("Welcome to messaging with topics and queues.\n\n"+
    		"In this scenario, you will create an SNS topic and subscribe %v SQS queues to the\n"+
    		"topic. You can select from several options for configuring the topic and the\n"+
    		"subscriptions for the queues. You can then post to the topic and see the results\n"+
    		"in the queues.\n", queueCount)
    
    	log.Println(strings.Repeat("-", 88))
    
    	runner := ScenarioRunner{
    		questioner: questioner,
    		snsActor:   &actions.SnsActions{SnsClient: sns.NewFromConfig(sdkConfig)},
    		sqsActor:   &actions.SqsActions{SqsClient: sqs.NewFromConfig(sdkConfig)},
    	}
    	resources.snsActor = runner.snsActor
    	resources.sqsActor = runner.sqsActor
    
    	topicName, topicArn, isFifoTopic, contentBasedDeduplication := runner.CreateTopic(ctx)
    	resources.topicArn = topicArn
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Now you will create %v SQS queues and subscribe them to the topic.\n", queueCount)
    	ordinals := []string{"first", "next"}
    	usingFilters := false
    	for _, ordinal := range ordinals {
    		queueName, queueUrl := runner.CreateQueue(ctx, ordinal, isFifoTopic)
    		resources.queueUrls = append(resources.queueUrls, queueUrl)
    
    		_, filtering := runner.SubscribeQueueToTopic(ctx, queueName, queueUrl, topicName, topicArn, ordinal, isFifoTopic)
    		usingFilters = usingFilters || filtering
    	}
    
    	log.Println(strings.Repeat("-", 88))
    	runner.PublishMessages(ctx, topicArn, isFifoTopic, contentBasedDeduplication, usingFilters)
    	log.Println(strings.Repeat("-", 88))
    	runner.PollForMessages(ctx, resources.queueUrls)
    
    	log.Println(strings.Repeat("-", 88))
    
    	wantCleanup := questioner.AskBool("Do you want to remove all AWS resources created for this scenario? (y/n) ", "y")
    	if wantCleanup {
    		log.Println("Cleaning up resources...")
    		resources.Cleanup(ctx)
    	}
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Define a struct that wraps Amazon SNS actions used in this example.
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sns"
    	"github.com/aws/aws-sdk-go-v2/service/sns/types"
    )
    
    // SnsActions encapsulates the Amazon Simple Notification Service (Amazon SNS) actions
    // used in the examples.
    type SnsActions struct {
    	SnsClient *sns.Client
    }
    
    
    
    // CreateTopic creates an Amazon SNS topic with the specified name. You can optionally
    // specify that the topic is created as a FIFO topic and whether it uses content-based
    // deduplication instead of ID-based deduplication.
    func (actor SnsActions) CreateTopic(ctx context.Context, topicName string, isFifoTopic bool, contentBasedDeduplication bool) (string, error) {
    	var topicArn string
    	topicAttributes := map[string]string{}
    	if isFifoTopic {
    		topicAttributes["FifoTopic"] = "true"
    	}
    	if contentBasedDeduplication {
    		topicAttributes["ContentBasedDeduplication"] = "true"
    	}
    	topic, err := actor.SnsClient.CreateTopic(ctx, &sns.CreateTopicInput{
    		Name:       aws.String(topicName),
    		Attributes: topicAttributes,
    	})
    	if err != nil {
    		log.Printf("Couldn't create topic %v. Here's why: %v\n", topicName, err)
    	} else {
    		topicArn = *topic.TopicArn
    	}
    
    	return topicArn, err
    }
    
    
    
    // DeleteTopic delete an Amazon SNS topic.
    func (actor SnsActions) DeleteTopic(ctx context.Context, topicArn string) error {
    	_, err := actor.SnsClient.DeleteTopic(ctx, &sns.DeleteTopicInput{
    		TopicArn: aws.String(topicArn)})
    	if err != nil {
    		log.Printf("Couldn't delete topic %v. Here's why: %v\n", topicArn, err)
    	}
    	return err
    }
    
    
    
    // SubscribeQueue subscribes an Amazon Simple Queue Service (Amazon SQS) queue to an
    // Amazon SNS topic. When filterMap is not nil, it is used to specify a filter policy
    // so that messages are only sent to the queue when the message has the specified attributes.
    func (actor SnsActions) SubscribeQueue(ctx context.Context, topicArn string, queueArn string, filterMap map[string][]string) (string, error) {
    	var subscriptionArn string
    	var attributes map[string]string
    	if filterMap != nil {
    		filterBytes, err := json.Marshal(filterMap)
    		if err != nil {
    			log.Printf("Couldn't create filter policy, here's why: %v\n", err)
    			return "", err
    		}
    		attributes = map[string]string{"FilterPolicy": string(filterBytes)}
    	}
    	output, err := actor.SnsClient.Subscribe(ctx, &sns.SubscribeInput{
    		Protocol:              aws.String("sqs"),
    		TopicArn:              aws.String(topicArn),
    		Attributes:            attributes,
    		Endpoint:              aws.String(queueArn),
    		ReturnSubscriptionArn: true,
    	})
    	if err != nil {
    		log.Printf("Couldn't susbscribe queue %v to topic %v. Here's why: %v\n",
    			queueArn, topicArn, err)
    	} else {
    		subscriptionArn = *output.SubscriptionArn
    	}
    
    	return subscriptionArn, err
    }
    
    
    
    // Publish publishes a message to an Amazon SNS topic. The message is then sent to all
    // subscribers. When the topic is a FIFO topic, the message must also contain a group ID
    // and, when ID-based deduplication is used, a deduplication ID. An optional key-value
    // filter attribute can be specified so that the message can be filtered according to
    // a filter policy.
    func (actor SnsActions) Publish(ctx context.Context, topicArn string, message string, groupId string, dedupId string, filterKey string, filterValue string) error {
    	publishInput := sns.PublishInput{TopicArn: aws.String(topicArn), Message: aws.String(message)}
    	if groupId != "" {
    		publishInput.MessageGroupId = aws.String(groupId)
    	}
    	if dedupId != "" {
    		publishInput.MessageDeduplicationId = aws.String(dedupId)
    	}
    	if filterKey != "" && filterValue != "" {
    		publishInput.MessageAttributes = map[string]types.MessageAttributeValue{
    			filterKey: {DataType: aws.String("String"), StringValue: aws.String(filterValue)},
    		}
    	}
    	_, err := actor.SnsClient.Publish(ctx, &publishInput)
    	if err != nil {
    		log.Printf("Couldn't publish message to topic %v. Here's why: %v", topicArn, err)
    	}
    	return err
    }
    
    
    

Define a struct that wraps Amazon SQS actions used in this example.
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/sqs"
    	"github.com/aws/aws-sdk-go-v2/service/sqs/types"
    )
    
    // SqsActions encapsulates the Amazon Simple Queue Service (Amazon SQS) actions
    // used in the examples.
    type SqsActions struct {
    	SqsClient *sqs.Client
    }
    
    
    
    // CreateQueue creates an Amazon SQS queue with the specified name. You can specify
    // whether the queue is created as a FIFO queue.
    func (actor SqsActions) CreateQueue(ctx context.Context, queueName string, isFifoQueue bool) (string, error) {
    	var queueUrl string
    	queueAttributes := map[string]string{}
    	if isFifoQueue {
    		queueAttributes["FifoQueue"] = "true"
    	}
    	queue, err := actor.SqsClient.CreateQueue(ctx, &sqs.CreateQueueInput{
    		QueueName:  aws.String(queueName),
    		Attributes: queueAttributes,
    	})
    	if err != nil {
    		log.Printf("Couldn't create queue %v. Here's why: %v\n", queueName, err)
    	} else {
    		queueUrl = *queue.QueueUrl
    	}
    
    	return queueUrl, err
    }
    
    
    
    // GetQueueArn uses the GetQueueAttributes action to get the Amazon Resource Name (ARN)
    // of an Amazon SQS queue.
    func (actor SqsActions) GetQueueArn(ctx context.Context, queueUrl string) (string, error) {
    	var queueArn string
    	arnAttributeName := types.QueueAttributeNameQueueArn
    	attribute, err := actor.SqsClient.GetQueueAttributes(ctx, &sqs.GetQueueAttributesInput{
    		QueueUrl:       aws.String(queueUrl),
    		AttributeNames: []types.QueueAttributeName{arnAttributeName},
    	})
    	if err != nil {
    		log.Printf("Couldn't get ARN for queue %v. Here's why: %v\n", queueUrl, err)
    	} else {
    		queueArn = attribute.Attributes[string(arnAttributeName)]
    	}
    	return queueArn, err
    }
    
    
    
    // AttachSendMessagePolicy uses the SetQueueAttributes action to attach a policy to an
    // Amazon SQS queue that allows the specified Amazon SNS topic to send messages to the
    // queue.
    func (actor SqsActions) AttachSendMessagePolicy(ctx context.Context, queueUrl string, queueArn string, topicArn string) error {
    	policyDoc := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:    "Allow",
    			Action:    "sqs:SendMessage",
    			Principal: map[string]string{"Service": "sns.amazonaws.com"},
    			Resource:  aws.String(queueArn),
    			Condition: PolicyCondition{"ArnEquals": map[string]string{"aws:SourceArn": topicArn}},
    		}},
    	}
    	policyBytes, err := json.Marshal(policyDoc)
    	if err != nil {
    		log.Printf("Couldn't create policy document. Here's why: %v\n", err)
    		return err
    	}
    	_, err = actor.SqsClient.SetQueueAttributes(ctx, &sqs.SetQueueAttributesInput{
    		Attributes: map[string]string{
    			string(types.QueueAttributeNamePolicy): string(policyBytes),
    		},
    		QueueUrl: aws.String(queueUrl),
    	})
    	if err != nil {
    		log.Printf("Couldn't set send message policy on queue %v. Here's why: %v\n", queueUrl, err)
    	}
    	return err
    }
    
    // PolicyDocument defines a policy document as a Go struct that can be serialized
    // to JSON.
    type PolicyDocument struct {
    	Version   string
    	Statement []PolicyStatement
    }
    
    // PolicyStatement defines a statement in a policy document.
    type PolicyStatement struct {
    	Effect    string
    	Action    string
    	Principal map[string]string `json:",omitempty"`
    	Resource  *string           `json:",omitempty"`
    	Condition PolicyCondition   `json:",omitempty"`
    }
    
    // PolicyCondition defines a condition in a policy.
    type PolicyCondition map[string]map[string]string
    
    
    
    // GetMessages uses the ReceiveMessage action to get messages from an Amazon SQS queue.
    func (actor SqsActions) GetMessages(ctx context.Context, queueUrl string, maxMessages int32, waitTime int32) ([]types.Message, error) {
    	var messages []types.Message
    	result, err := actor.SqsClient.ReceiveMessage(ctx, &sqs.ReceiveMessageInput{
    		QueueUrl:            aws.String(queueUrl),
    		MaxNumberOfMessages: maxMessages,
    		WaitTimeSeconds:     waitTime,
    	})
    	if err != nil {
    		log.Printf("Couldn't get messages from queue %v. Here's why: %v\n", queueUrl, err)
    	} else {
    		messages = result.Messages
    	}
    	return messages, err
    }
    
    
    
    // DeleteMessages uses the DeleteMessageBatch action to delete a batch of messages from
    // an Amazon SQS queue.
    func (actor SqsActions) DeleteMessages(ctx context.Context, queueUrl string, messages []types.Message) error {
    	entries := make([]types.DeleteMessageBatchRequestEntry, len(messages))
    	for msgIndex := range messages {
    		entries[msgIndex].Id = aws.String(fmt.Sprintf("%v", msgIndex))
    		entries[msgIndex].ReceiptHandle = messages[msgIndex].ReceiptHandle
    	}
    	_, err := actor.SqsClient.DeleteMessageBatch(ctx, &sqs.DeleteMessageBatchInput{
    		Entries:  entries,
    		QueueUrl: aws.String(queueUrl),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete messages from queue %v. Here's why: %v\n", queueUrl, err)
    	}
    	return err
    }
    
    
    
    // DeleteQueue deletes an Amazon SQS queue.
    func (actor SqsActions) DeleteQueue(ctx context.Context, queueUrl string) error {
    	_, err := actor.SqsClient.DeleteQueue(ctx, &sqs.DeleteQueueInput{
    		QueueUrl: aws.String(queueUrl)})
    	if err != nil {
    		log.Printf("Couldn't delete queue %v. Here's why: %v\n", queueUrl, err)
    	}
    	return err
    }
    
    
    

Clean up resources.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"topics_and_queues/actions"
    )
    
    // Resources keeps track of AWS resources created during an example and handles
    // cleanup when the example finishes.
    type Resources struct {
    	topicArn  string
    	queueUrls []string
    	snsActor  *actions.SnsActions
    	sqsActor  *actions.SqsActions
    }
    
    // Cleanup deletes all AWS resources created during an example.
    func (resources Resources) Cleanup(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			fmt.Println("Something went wrong during cleanup. Use the AWS Management Console\n" +
    				"to remove any remaining resources that were created for this scenario.")
    		}
    	}()
    
    	var err error
    	if resources.topicArn != "" {
    		log.Printf("Deleting topic %v.\n", resources.topicArn)
    		err = resources.snsActor.DeleteTopic(ctx, resources.topicArn)
    		if err != nil {
    			panic(err)
    		}
    	}
    
    	for _, queueUrl := range resources.queueUrls {
    		log.Printf("Deleting queue %v.\n", queueUrl)
    		err = resources.sqsActor.DeleteQueue(ctx, queueUrl)
    		if err != nil {
    			panic(err)
    		}
    	}
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [CreateQueue](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.CreateQueue)

    * [CreateTopic](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.CreateTopic)

    * [DeleteMessageBatch](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.DeleteMessageBatch)

    * [DeleteQueue](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.DeleteQueue)

    * [DeleteTopic](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.DeleteTopic)

    * [GetQueueAttributes](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.GetQueueAttributes)

    * [Publish](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.Publish)

    * [ReceiveMessage](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.ReceiveMessage)

    * [SetQueueAttributes](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.SetQueueAttributes)

    * [Subscribe](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.Subscribe)

    * [Unsubscribe](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.Unsubscribe)




## Serverless examples

The following code example shows how to implement a Lambda function that receives an event triggered by receiving messages from an SQS queue. The function retrieves the messages from the event parameter and logs the content of each message.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-sqs-to-lambda) repository. 

Consuming an SQS event with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package integration_sqs_to_lambda
    
    import (
    	"fmt"
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    func handler(event events.SQSEvent) error {
    	for _, record := range event.Records {
    		err := processMessage(record)
    		if err != nil {
    			return err
    		}
    	}
    	fmt.Println("done")
    	return nil
    }
    
    func processMessage(record events.SQSMessage) error {
    	fmt.Printf("Processed message %s\n", record.Body)
    	// TODO: Do interesting work based on the new message
    	return nil
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    

The following code example shows how to implement partial batch response for Lambda functions that receive events from an SQS queue. The function reports the batch item failures in the response, signaling to Lambda to retry those messages later.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/lambda-function-sqs-report-batch-item-failures) repository. 

Reporting SQS batch item failures with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"fmt"
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    func handler(ctx context.Context, sqsEvent events.SQSEvent) (map[string]interface{}, error) {
    	batchItemFailures := []map[string]interface{}{}
    
    	for _, message := range sqsEvent.Records {
    		if len(message.Body) > 0 {
    			// Your message processing condition here
    			fmt.Printf("Successfully processed message: %s\n", message.Body)
    		} else {
    			// Message processing failed
    			fmt.Printf("Failed to process message %s\n", message.MessageId)
    			batchItemFailures = append(batchItemFailures, map[string]interface{}{"itemIdentifier": message.MessageId})
    		}
    	}
    
    	sqsBatchResponse := map[string]interface{}{
    		"batchItemFailures": batchItemFailures,
    	}
    	return sqsBatchResponse, nil
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon SNS

Migrate to v2

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
