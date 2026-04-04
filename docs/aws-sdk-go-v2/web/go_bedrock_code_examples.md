# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_bedrock_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_bedrock_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Actions

# Amazon Bedrock examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon Bedrock.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using Amazon Bedrock.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/bedrock"
    )
    
    const region = "us-east-1"
    
    // main uses the AWS SDK for Go (v2) to create an Amazon Bedrock client and
    // list the available foundation models in your account and the chosen region.
    // This example uses the default settings specified in your shared credentials
    // and config files.
    func main() {
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(region))
    	if err != nil {
    		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
    		fmt.Println(err)
    		return
    	}
    	bedrockClient := bedrock.NewFromConfig(sdkConfig)
    	result, err := bedrockClient.ListFoundationModels(ctx, &bedrock.ListFoundationModelsInput{})
    	if err != nil {
    		fmt.Printf("Couldn't list foundation models. Here's why: %v\n", err)
    		return
    	}
    	if len(result.ModelSummaries) == 0 {
    		fmt.Println("There are no foundation models.")
    	}
    	for _, modelSummary := range result.ModelSummaries {
    		fmt.Println(*modelSummary.ModelId)
    	}
    }
    
    
    

  * For API details, see [ListFoundationModels](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrock#Client.ListFoundationModels) in _AWS SDK for Go API Reference_. 




###### Topics

  * Actions




## Actions

The following code example shows how to use `ListFoundationModels`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock#code-examples). 

List the available Bedrock foundation models.
    
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/service/bedrock"
    	"github.com/aws/aws-sdk-go-v2/service/bedrock/types"
    )
    
    // FoundationModelWrapper encapsulates Amazon Bedrock actions used in the examples.
    // It contains a Bedrock service client that is used to perform foundation model actions.
    type FoundationModelWrapper struct {
    	BedrockClient *bedrock.Client
    }
    
    
    
    // ListPolicies lists Bedrock foundation models that you can use.
    func (wrapper FoundationModelWrapper) ListFoundationModels(ctx context.Context) ([]types.FoundationModelSummary, error) {
    
    	var models []types.FoundationModelSummary
    
    	result, err := wrapper.BedrockClient.ListFoundationModels(ctx, &bedrock.ListFoundationModelsInput{})
    
    	if err != nil {
    		log.Printf("Couldn't list foundation models. Here's why: %v\n", err)
    	} else {
    		models = result.ModelSummaries
    	}
    	return models, err
    }
    
    
    

  * For API details, see [ListFoundationModels](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrock#Client.ListFoundationModels) in _AWS SDK for Go API Reference_. 




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Aurora

Amazon Bedrock Runtime

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
