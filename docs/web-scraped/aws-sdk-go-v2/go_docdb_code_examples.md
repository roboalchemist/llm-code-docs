# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_docdb_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_docdb_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Serverless examples

# Amazon DocumentDB examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon DocumentDB.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

  * Serverless examples




## Serverless examples

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from a DocumentDB change stream. The function retrieves the DocumentDB payload and logs the record contents.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-docdb-to-lambda) repository. 

Consuming a Amazon DocumentDB event with Lambda using Go.
    
    
    package main
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    type Event struct {
    	Events []Record `json:"events"`
    }
    
    type Record struct {
    	Event struct {
    		OperationType string `json:"operationType"`
    		NS            struct {
    			DB   string `json:"db"`
    			Coll string `json:"coll"`
    		} `json:"ns"`
    		FullDocument interface{} `json:"fullDocument"`
    	} `json:"event"`
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    func handler(ctx context.Context, event Event) (string, error) {
    	fmt.Println("Loading function")
    	for _, record := range event.Events {
    		logDocumentDBEvent(record)
    	}
    
    	return "OK", nil
    }
    
    func logDocumentDBEvent(record Record) {
    	fmt.Printf("Operation type: %s\n", record.Event.OperationType)
    	fmt.Printf("db: %s\n", record.Event.NS.DB)
    	fmt.Printf("collection: %s\n", record.Event.NS.Coll)
    	docBytes, _ := json.MarshalIndent(record.Event.FullDocument, "", "  ")
    	fmt.Printf("Full document: %s\n", string(docBytes))
    }
    
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon Cognito Identity Provider

DynamoDB

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
