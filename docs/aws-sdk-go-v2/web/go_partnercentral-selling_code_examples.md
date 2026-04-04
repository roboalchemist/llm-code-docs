# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_partnercentral-selling_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_partnercentral-selling_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

Actions

# Partner Central examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Partner Central.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

  * Actions




## Actions

The following code example shows how to use `GetOpportunity`.

**SDK for Go V2**
    

Get an opportunity.
    
    
    package main
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/partnercentralselling"
    )
    
    func main() {
    	config, err := config.LoadDefaultConfig(context.TODO())
    
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	config.Region = "us-east-1"
    
    	client := partnercentralselling.NewFromConfig(config)
    
    	output, err := client.GetOpportunity(context.TODO(), &partnercentralselling.GetOpportunityInput{
    		Identifier: aws.String("O1111111"),
    		Catalog:    aws.String("AWS"),
    	})
    
    	if err != nil {
    		log.Fatal(err)
    	}
    	log.Println("printing opportuniy...\n")
    
    	jsonOutput, err := json.MarshalIndent(output, "", "    ")
    
    	fmt.Println(string(jsonOutput))
    }
    
    

  * For API details, see [GetOpportunity](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.GetOpportunity) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListOpportunities`.

**SDK for Go V2**
    

List opportunities.
    
    
    package main
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/partnercentralselling"
    )
    
    func main() {
    	config, err := config.LoadDefaultConfig(context.TODO())
    
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	config.Region = "us-east-1"
    
    	client := partnercentralselling.NewFromConfig(config)
    
    	output, err := client.ListOpportunities(context.TODO(), &partnercentralselling.ListOpportunitiesInput{
    		MaxResults: aws.Int32(2),
    		Catalog:    aws.String("AWS"),
    	})
    
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	jsonOutput, err := json.MarshalIndent(output, "", "    ")
    	fmt.Println(string(jsonOutput))
    }
    
    

  * For API details, see [ListOpportunities](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.ListOpportunities) in _AWS SDK for Go API Reference_. 




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon MSK

Amazon RDS

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
