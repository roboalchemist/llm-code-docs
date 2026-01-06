# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_kafka_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_kafka_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Serverless examples

# Amazon MSK examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon MSK.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

  * Serverless examples




## Serverless examples

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from an Amazon MSK cluster. The function retrieves the MSK payload and logs the record contents.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-msk-to-lambda) repository. 

Consuming an Amazon MSK event with Lambda using Go.
    
    
    package main
    
    import (
    	"encoding/base64"
    	"fmt"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    func handler(event events.KafkaEvent) {
    	for key, records := range event.Records {
    		fmt.Println("Key:", key)
    
    		for _, record := range records {
    			fmt.Println("Record:", record)
    
    			decodedValue, _ := base64.StdEncoding.DecodeString(record.Value)
    			message := string(decodedValue)
    			fmt.Println("Message:", message)
    		}
    	}
    }
    
    func main() {
    	lambda.Start(handler)
    }
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Lambda

Partner Central

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
