# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_cloudwatch-logs_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_cloudwatch-logs_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Actions

# CloudWatch Logs examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with CloudWatch Logs.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

  * Actions




## Actions

The following code example shows how to use `StartLiveTail`.

**SDK for Go V2**
    

Include the required files.
    
    
    import (
    	"context"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs/types"
    )
    
    

Handle the events from the Live Tail session.
    
    
    func handleEventStreamAsync(stream *cloudwatchlogs.StartLiveTailEventStream) {
    	eventsChan := stream.Events()
    	for {
    		event := <-eventsChan
    		switch e := event.(type) {
    		case *types.StartLiveTailResponseStreamMemberSessionStart:
    			log.Println("Received SessionStart event")
    		case *types.StartLiveTailResponseStreamMemberSessionUpdate:
    			for _, logEvent := range e.Value.SessionResults {
    				log.Println(*logEvent.Message)
    			}
    		default:
    			// Handle on-stream exceptions
    			if err := stream.Err(); err != nil {
    				log.Fatalf("Error occured during streaming: %v", err)
    			} else if event == nil {
    				log.Println("Stream is Closed")
    				return
    			} else {
    				log.Fatalf("Unknown event type: %T", e)
    			}
    		}
    	}
    }
    
    

Start the Live Tail session.
    
    
    	cfg, err := config.LoadDefaultConfig(context.TODO())
    	if err != nil {
    		panic("configuration error, " + err.Error())
    	}
    	client := cloudwatchlogs.NewFromConfig(cfg)
    
    	request := &cloudwatchlogs.StartLiveTailInput{
    		LogGroupIdentifiers:   logGroupIdentifiers,
    		LogStreamNames:        logStreamNames,
    		LogEventFilterPattern: logEventFilterPattern,
    	}
    
    	response, err := client.StartLiveTail(context.TODO(), request)
    	// Handle pre-stream Exceptions
    	if err != nil {
    		log.Fatalf("Failed to start streaming: %v", err)
    	}
    
    	// Start a Goroutine to handle events over stream
    	stream := response.GetStream()
    	go handleEventStreamAsync(stream)
    
    

Stop the Live Tail session after a period of time has elapsed.
    
    
    	// Close the stream (which ends the session) after a timeout
    	time.Sleep(10 * time.Second)
    	stream.Close()
    	log.Println("Event stream closed")
    
    

  * For API details, see [StartLiveTail](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs#Client.StartLiveTail) in _AWS SDK for Go API Reference_. 




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CloudFormation

Amazon Cognito Identity Provider

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
