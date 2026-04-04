# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_kinesis_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_kinesis_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Serverless examples

# Kinesis examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Kinesis.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

  * Serverless examples




## Serverless examples

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from a Kinesis stream. The function retrieves the Kinesis payload, decodes from Base64, and logs the record contents.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-kinesis-to-lambda) repository. 

Consuming a Kinesis event with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    func handler(ctx context.Context, kinesisEvent events.KinesisEvent) error {
    	if len(kinesisEvent.Records) == 0 {
    		log.Printf("empty Kinesis event received")
    		return nil
    	}
    
    	for _, record := range kinesisEvent.Records {
    		log.Printf("processed Kinesis event with EventId: %v", record.EventID)
    		recordDataBytes := record.Kinesis.Data
    		recordDataText := string(recordDataBytes)
    		log.Printf("record data: %v", recordDataText)
    		// TODO: Do interesting work based on the new data
    	}
    	log.Printf("successfully processed %v records", len(kinesisEvent.Records))
    	return nil
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    

The following code example shows how to implement partial batch response for Lambda functions that receive events from a Kinesis stream. The function reports the batch item failures in the response, signaling to Lambda to retry those messages later.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-kinesis-to-lambda-with-batch-item-handling) repository. 

Reporting Kinesis batch item failures with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"fmt"
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    func handler(ctx context.Context, kinesisEvent events.KinesisEvent) (map[string]interface{}, error) {
    	batchItemFailures := []map[string]interface{}{}
    
    	for _, record := range kinesisEvent.Records {
    		curRecordSequenceNumber := ""
    
    		// Process your record
    		if /* Your record processing condition here */ {
    			curRecordSequenceNumber = record.Kinesis.SequenceNumber
    		}
    
    		// Add a condition to check if the record processing failed
    		if curRecordSequenceNumber != "" {
    			batchItemFailures = append(batchItemFailures, map[string]interface{}{"itemIdentifier": curRecordSequenceNumber})
    		}
    	}
    
    	kinesisBatchResponse := map[string]interface{}{
    		"batchItemFailures": batchItemFailures,
    	}
    	return kinesisBatchResponse, nil
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

IAM

Lambda

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
