# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_cloudformation_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_cloudformation_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Actions

# CloudFormation examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with CloudFormation.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

  * Actions




## Actions

The following code example shows how to use `DescribeStacks`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/user_pools_and_lambda_triggers#code-examples). 
    
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cloudformation"
    )
    
    // StackOutputs defines a map of outputs from a specific stack.
    type StackOutputs map[string]string
    
    type CloudFormationActions struct {
    	CfnClient *cloudformation.Client
    }
    
    // GetOutputs gets the outputs from a CloudFormation stack and puts them into a structured format.
    func (actor CloudFormationActions) GetOutputs(ctx context.Context, stackName string) StackOutputs {
    	output, err := actor.CfnClient.DescribeStacks(ctx, &cloudformation.DescribeStacksInput{
    		StackName: aws.String(stackName),
    	})
    	if err != nil || len(output.Stacks) == 0 {
    		log.Panicf("Couldn't find a CloudFormation stack named %v. Here's why: %v\n", stackName, err)
    	}
    	stackOutputs := StackOutputs{}
    	for _, out := range output.Stacks[0].Outputs {
    		stackOutputs[*out.OutputKey] = *out.OutputValue
    	}
    	return stackOutputs
    }
    
    
    

  * For API details, see [DescribeStacks](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cloudformation#Client.DescribeStacks) in _AWS SDK for Go API Reference_. 




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon Bedrock Runtime

CloudWatch Logs

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
