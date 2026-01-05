# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_bedrock-runtime_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_bedrock-runtime_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

ScenariosAmazon Titan Image GeneratorAnthropic Claude

# Amazon Bedrock Runtime examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon Bedrock Runtime.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using Amazon Bedrock.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"encoding/json"
    	"flag"
    	"fmt"
    	"log"
    	"os"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
    )
    
    // Each model provider defines their own individual request and response formats.
    // For the format, ranges, and default values for the different models, refer to:
    // https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
    
    type ClaudeRequest struct {
    	Prompt            string `json:"prompt"`
    	MaxTokensToSample int    `json:"max_tokens_to_sample"`
    	// Omitting optional request parameters
    }
    
    type ClaudeResponse struct {
    	Completion string `json:"completion"`
    }
    
    // main uses the AWS SDK for Go (v2) to create an Amazon Bedrock Runtime client
    // and invokes Anthropic Claude 2 inside your account and the chosen region.
    // This example uses the default settings specified in your shared credentials
    // and config files.
    func main() {
    
    	region := flag.String("region", "us-east-1", "The AWS region")
    	flag.Parse()
    
    	fmt.Printf("Using AWS region: %s\n", *region)
    
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(*region))
    	if err != nil {
    		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
    		fmt.Println(err)
    		return
    	}
    
    	client := bedrockruntime.NewFromConfig(sdkConfig)
    
    	modelId := "anthropic.claude-v2"
    
    	prompt := "Hello, how are you today?"
    
    	// Anthropic Claude requires you to enclose the prompt as follows:
    	prefix := "Human: "
    	postfix := "\n\nAssistant:"
    	wrappedPrompt := prefix + prompt + postfix
    
    	request := ClaudeRequest{
    		Prompt:            wrappedPrompt,
    		MaxTokensToSample: 200,
    	}
    
    	body, err := json.Marshal(request)
    	if err != nil {
    		log.Panicln("Couldn't marshal the request: ", err)
    	}
    
    	result, err := client.InvokeModel(ctx, &bedrockruntime.InvokeModelInput{
    		ModelId:     aws.String(modelId),
    		ContentType: aws.String("application/json"),
    		Body:        body,
    	})
    
    	if err != nil {
    		errMsg := err.Error()
    		if strings.Contains(errMsg, "no such host") {
    			fmt.Printf("Error: The Bedrock service is not available in the selected region. Please double-check the service availability for your region at https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/.\n")
    		} else if strings.Contains(errMsg, "Could not resolve the foundation model") {
    			fmt.Printf("Error: Could not resolve the foundation model from model identifier: \"%v\". Please verify that the requested model exists and is accessible within the specified region.\n", modelId)
    		} else {
    			fmt.Printf("Error: Couldn't invoke Anthropic Claude. Here's why: %v\n", err)
    		}
    		os.Exit(1)
    	}
    
    	var response ClaudeResponse
    
    	err = json.Unmarshal(result.Body, &response)
    
    	if err != nil {
    		log.Fatal("failed to unmarshal", err)
    	}
    	fmt.Println("Prompt:\n", prompt)
    	fmt.Println("Response from Anthropic Claude:\n", response.Completion)
    }
    
    
    

  * For API details, see [InvokeModel](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModel) in _AWS SDK for Go API Reference_. 




###### Topics

  * Scenarios

  * Amazon Titan Image Generator

  * Anthropic Claude




## Scenarios

The following code example shows how to prepare and send a prompt to a variety of large-language models (LLMs) on Amazon Bedrock

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples). 

Invoke multiple foundation models on Amazon Bedrock.
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"log"
    	"math/rand"
    	"os"
    	"path/filepath"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/bedrock-runtime/actions"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // InvokeModelsScenario demonstrates how to use the Amazon Bedrock Runtime client
    // to invoke various foundation models for text and image generation
    //
    // 1. Generate text with Anthropic Claude 2
    // 2. Generate text with Meta Llama 2 Chat
    // 3. Generate text and asynchronously process the response stream with Anthropic Claude 2
    // 4. Generate an image with the Amazon Titan image generation model
    type InvokeModelsScenario struct {
    	sdkConfig             aws.Config
    	invokeModelWrapper    actions.InvokeModelWrapper
    	responseStreamWrapper actions.InvokeModelWithResponseStreamWrapper
    	questioner            demotools.IQuestioner
    }
    
    // NewInvokeModelsScenario constructs an InvokeModelsScenario instance from a configuration.
    // It uses the specified config to get a Bedrock Runtime client and create wrappers for the
    // actions used in the scenario.
    func NewInvokeModelsScenario(sdkConfig aws.Config, questioner demotools.IQuestioner) InvokeModelsScenario {
    	client := bedrockruntime.NewFromConfig(sdkConfig)
    	return InvokeModelsScenario{
    		sdkConfig:             sdkConfig,
    		invokeModelWrapper:    actions.InvokeModelWrapper{BedrockRuntimeClient: client},
    		responseStreamWrapper: actions.InvokeModelWithResponseStreamWrapper{BedrockRuntimeClient: client},
    		questioner:            questioner,
    	}
    }
    
    // Runs the interactive scenario.
    func (scenario InvokeModelsScenario) Run(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Printf("Something went wrong with the demo: %v\n", r)
    		}
    	}()
    
    	log.Println(strings.Repeat("=", 77))
    	log.Println("Welcome to the Amazon Bedrock Runtime model invocation demo.")
    	log.Println(strings.Repeat("=", 77))
    
    	log.Printf("First, let's invoke a few large-language models using the synchronous client:\n\n")
    
    	text2textPrompt := "In one paragraph, who are you?"
    
    	log.Println(strings.Repeat("-", 77))
    	log.Printf("Invoking Claude with prompt: %v\n", text2textPrompt)
    	scenario.InvokeClaude(ctx, text2textPrompt)
    
    	log.Println(strings.Repeat("=", 77))
    	log.Printf("Now, let's invoke Claude with the asynchronous client and process the response stream:\n\n")
    
    	log.Println(strings.Repeat("-", 77))
    	log.Printf("Invoking Claude with prompt: %v\n", text2textPrompt)
    	scenario.InvokeWithResponseStream(ctx, text2textPrompt)
    
    	log.Println(strings.Repeat("=", 77))
    	log.Printf("Now, let's create an image with the Amazon Titan image generation model:\n\n")
    
    	text2ImagePrompt := "stylized picture of a cute old steampunk robot"
    	seed := rand.Int63n(2147483648)
    
    	log.Println(strings.Repeat("-", 77))
    	log.Printf("Invoking Amazon Titan with prompt: %v\n", text2ImagePrompt)
    	scenario.InvokeTitanImage(ctx, text2ImagePrompt, seed)
    
    	log.Println(strings.Repeat("=", 77))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("=", 77))
    }
    
    func (scenario InvokeModelsScenario) InvokeClaude(ctx context.Context, prompt string) {
    	completion, err := scenario.invokeModelWrapper.InvokeClaude(ctx, prompt)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("\nClaude     : %v\n", strings.TrimSpace(completion))
    }
    
    func (scenario InvokeModelsScenario) InvokeWithResponseStream(ctx context.Context, prompt string) {
    	log.Println("\nClaude with response stream:")
    	_, err := scenario.responseStreamWrapper.InvokeModelWithResponseStream(ctx, prompt)
    	if err != nil {
    		panic(err)
    	}
    	log.Println()
    }
    
    func (scenario InvokeModelsScenario) InvokeTitanImage(ctx context.Context, prompt string, seed int64) {
    	base64ImageData, err := scenario.invokeModelWrapper.InvokeTitanImage(ctx, prompt, seed)
    	if err != nil {
    		panic(err)
    	}
    	imagePath := saveImage(base64ImageData, "amazon.titan-image-generator-v1")
    	fmt.Printf("The generated image has been saved to %s\n", imagePath)
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [InvokeModel](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModel)

    * [InvokeModelWithResponseStream](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModelWithResponseStream)




## Amazon Titan Image Generator

The following code example shows how to invoke Amazon Titan Image on Amazon Bedrock to generate an image.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples). 

Create an image with the Amazon Titan Image Generator.
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
    )
    
    // InvokeModelWrapper encapsulates Amazon Bedrock actions used in the examples.
    // It contains a Bedrock Runtime client that is used to invoke foundation models.
    type InvokeModelWrapper struct {
    	BedrockRuntimeClient *bedrockruntime.Client
    }
    
    
    
    type TitanImageRequest struct {
    	TaskType              string                `json:"taskType"`
    	TextToImageParams     TextToImageParams     `json:"textToImageParams"`
    	ImageGenerationConfig ImageGenerationConfig `json:"imageGenerationConfig"`
    }
    type TextToImageParams struct {
    	Text string `json:"text"`
    }
    type ImageGenerationConfig struct {
    	NumberOfImages int     `json:"numberOfImages"`
    	Quality        string  `json:"quality"`
    	CfgScale       float64 `json:"cfgScale"`
    	Height         int     `json:"height"`
    	Width          int     `json:"width"`
    	Seed           int64   `json:"seed"`
    }
    
    type TitanImageResponse struct {
    	Images []string `json:"images"`
    }
    
    // Invokes the Titan Image model to create an image using the input provided
    // in the request body.
    func (wrapper InvokeModelWrapper) InvokeTitanImage(ctx context.Context, prompt string, seed int64) (string, error) {
    	modelId := "amazon.titan-image-generator-v1"
    
    	body, err := json.Marshal(TitanImageRequest{
    		TaskType: "TEXT_IMAGE",
    		TextToImageParams: TextToImageParams{
    			Text: prompt,
    		},
    		ImageGenerationConfig: ImageGenerationConfig{
    			NumberOfImages: 1,
    			Quality:        "standard",
    			CfgScale:       8.0,
    			Height:         512,
    			Width:          512,
    			Seed:           seed,
    		},
    	})
    
    	if err != nil {
    		log.Fatal("failed to marshal", err)
    	}
    
    	output, err := wrapper.BedrockRuntimeClient.InvokeModel(ctx, &bedrockruntime.InvokeModelInput{
    		ModelId:     aws.String(modelId),
    		ContentType: aws.String("application/json"),
    		Body:        body,
    	})
    
    	if err != nil {
    		ProcessError(err, modelId)
    	}
    
    	var response TitanImageResponse
    	if err := json.Unmarshal(output.Body, &response); err != nil {
    		log.Fatal("failed to unmarshal", err)
    	}
    
    	base64ImageData := response.Images[0]
    
    	return base64ImageData, nil
    
    }
    
    
    

  * For API details, see [InvokeModel](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModel) in _AWS SDK for Go API Reference_. 




## Anthropic Claude

The following code example shows how to send a text message to Anthropic Claude, using Bedrock's Converse API.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples). 

Send a text message to Anthropic Claude, using Bedrock's Converse API.
    
    
    import (
    	"context"
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime/types"
    )
    
    // ConverseWrapper encapsulates Amazon Bedrock actions used in the examples.
    // It contains a Bedrock Runtime client that is used to invoke Bedrock.
    type ConverseWrapper struct {
    	BedrockRuntimeClient *bedrockruntime.Client
    }
    
    
    
    func (wrapper ConverseWrapper) ConverseClaude(ctx context.Context, prompt string) (string, error) {
    	var content = types.ContentBlockMemberText{
    		Value: prompt,
    	}
    	var message = types.Message{
    		Content: []types.ContentBlock{&content},
    		Role:    "user",
    	}
    	modelId := "anthropic.claude-3-haiku-20240307-v1:0"
    	var converseInput = bedrockruntime.ConverseInput{
    		ModelId:  aws.String(modelId),
    		Messages: []types.Message{message},
    	}
    	response, err := wrapper.BedrockRuntimeClient.Converse(ctx, &converseInput)
    	if err != nil {
    		ProcessError(err, modelId)
    	}
    
    	responseText, _ := response.Output.(*types.ConverseOutputMemberMessage)
    	responseContentBlock := responseText.Value.Content[0]
    	text, _ := responseContentBlock.(*types.ContentBlockMemberText)
    	return text.Value, nil
    
    }
    
    
    

  * For API details, see [Converse](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.Converse) in _AWS SDK for Go API Reference_. 




The following code example shows how to send a text message to Anthropic Claude, using the Invoke Model API.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples). 

Invoke the Anthropic Claude 2 foundation model to generate text.
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
    )
    
    // InvokeModelWrapper encapsulates Amazon Bedrock actions used in the examples.
    // It contains a Bedrock Runtime client that is used to invoke foundation models.
    type InvokeModelWrapper struct {
    	BedrockRuntimeClient *bedrockruntime.Client
    }
    
    
    
    // Each model provider has their own individual request and response formats.
    // For the format, ranges, and default values for Anthropic Claude, refer to:
    // https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-claude.html
    
    type ClaudeRequest struct {
    	Prompt            string   `json:"prompt"`
    	MaxTokensToSample int      `json:"max_tokens_to_sample"`
    	Temperature       float64  `json:"temperature,omitempty"`
    	StopSequences     []string `json:"stop_sequences,omitempty"`
    }
    
    type ClaudeResponse struct {
    	Completion string `json:"completion"`
    }
    
    // Invokes Anthropic Claude on Amazon Bedrock to run an inference using the input
    // provided in the request body.
    func (wrapper InvokeModelWrapper) InvokeClaude(ctx context.Context, prompt string) (string, error) {
    	modelId := "anthropic.claude-v2"
    
    	// Anthropic Claude requires enclosing the prompt as follows:
    	enclosedPrompt := "Human: " + prompt + "\n\nAssistant:"
    
    	body, err := json.Marshal(ClaudeRequest{
    		Prompt:            enclosedPrompt,
    		MaxTokensToSample: 200,
    		Temperature:       0.5,
    		StopSequences:     []string{"\n\nHuman:"},
    	})
    
    	if err != nil {
    		log.Fatal("failed to marshal", err)
    	}
    
    	output, err := wrapper.BedrockRuntimeClient.InvokeModel(ctx, &bedrockruntime.InvokeModelInput{
    		ModelId:     aws.String(modelId),
    		ContentType: aws.String("application/json"),
    		Body:        body,
    	})
    
    	if err != nil {
    		ProcessError(err, modelId)
    	}
    
    	var response ClaudeResponse
    	if err := json.Unmarshal(output.Body, &response); err != nil {
    		log.Fatal("failed to unmarshal", err)
    	}
    
    	return response.Completion, nil
    }
    
    
    

  * For API details, see [InvokeModel](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModel) in _AWS SDK for Go API Reference_. 




The following code example shows how to send a text message to Anthropic Claude models, using the Invoke Model API, and print the response stream.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples). 

Use the Invoke Model API to send a text message and process the response stream in real-time.
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"fmt"
    	"log"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
    	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime/types"
    )
    
    // InvokeModelWithResponseStreamWrapper encapsulates Amazon Bedrock actions used in the examples.
    // It contains a Bedrock Runtime client that is used to invoke foundation models.
    type InvokeModelWithResponseStreamWrapper struct {
    	BedrockRuntimeClient *bedrockruntime.Client
    }
    
    
    
    // Each model provider defines their own individual request and response formats.
    // For the format, ranges, and default values for the different models, refer to:
    // https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
    
    type Request struct {
    	Prompt            string  `json:"prompt"`
    	MaxTokensToSample int     `json:"max_tokens_to_sample"`
    	Temperature       float64 `json:"temperature,omitempty"`
    }
    
    type Response struct {
    	Completion string `json:"completion"`
    }
    
    // Invokes Anthropic Claude on Amazon Bedrock to run an inference and asynchronously
    // process the response stream.
    
    func (wrapper InvokeModelWithResponseStreamWrapper) InvokeModelWithResponseStream(ctx context.Context, prompt string) (string, error) {
    
    	modelId := "anthropic.claude-v2"
    
    	// Anthropic Claude requires you to enclose the prompt as follows:
    	prefix := "Human: "
    	postfix := "\n\nAssistant:"
    	prompt = prefix + prompt + postfix
    
    	request := ClaudeRequest{
    		Prompt:            prompt,
    		MaxTokensToSample: 200,
    		Temperature:       0.5,
    		StopSequences:     []string{"\n\nHuman:"},
    	}
    
    	body, err := json.Marshal(request)
    	if err != nil {
    		log.Panicln("Couldn't marshal the request: ", err)
    	}
    
    	output, err := wrapper.BedrockRuntimeClient.InvokeModelWithResponseStream(ctx, &bedrockruntime.InvokeModelWithResponseStreamInput{
    		Body:        body,
    		ModelId:     aws.String(modelId),
    		ContentType: aws.String("application/json"),
    	})
    
    	if err != nil {
    		errMsg := err.Error()
    		if strings.Contains(errMsg, "no such host") {
    			log.Printf("The Bedrock service is not available in the selected region. Please double-check the service availability for your region at https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/.\n")
    		} else if strings.Contains(errMsg, "Could not resolve the foundation model") {
    			log.Printf("Could not resolve the foundation model from model identifier: \"%v\". Please verify that the requested model exists and is accessible within the specified region.\n", modelId)
    		} else {
    			log.Printf("Couldn't invoke Anthropic Claude. Here's why: %v\n", err)
    		}
    	}
    
    	resp, err := processStreamingOutput(ctx, output, func(ctx context.Context, part []byte) error {
    		fmt.Print(string(part))
    		return nil
    	})
    
    	if err != nil {
    		log.Fatal("streaming output processing error: ", err)
    	}
    
    	return resp.Completion, nil
    
    }
    
    type StreamingOutputHandler func(ctx context.Context, part []byte) error
    
    func processStreamingOutput(ctx context.Context, output *bedrockruntime.InvokeModelWithResponseStreamOutput, handler StreamingOutputHandler) (Response, error) {
    
    	var combinedResult string
    	resp := Response{}
    
    	for event := range output.GetStream().Events() {
    		switch v := event.(type) {
    		case *types.ResponseStreamMemberChunk:
    
    			//fmt.Println("payload", string(v.Value.Bytes))
    
    			var resp Response
    			err := json.NewDecoder(bytes.NewReader(v.Value.Bytes)).Decode(&resp)
    			if err != nil {
    				return resp, err
    			}
    
    			err = handler(ctx, []byte(resp.Completion))
    			if err != nil {
    				return resp, err
    			}
    
    			combinedResult += resp.Completion
    
    		case *types.UnknownUnionMember:
    			fmt.Println("unknown tag:", v.Tag)
    
    		default:
    			fmt.Println("union is nil or unknown type")
    		}
    	}
    
    	resp.Completion = combinedResult
    
    	return resp, nil
    }
    
    
    

  * For API details, see [InvokeModelWithResponseStream](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModelWithResponseStream) in _AWS SDK for Go API Reference_. 




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon Bedrock

CloudFormation

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
