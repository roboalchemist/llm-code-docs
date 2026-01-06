# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_lambda_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_lambda_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

BasicsActionsScenariosServerless examplesAWS community contributions

# Lambda examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Lambda.

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

_AWS community contributions_ are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using Lambda.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    )
    
    // main uses the AWS SDK for Go (v2) to create an AWS Lambda client and list up to 10
    // functions in your account.
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
    	lambdaClient := lambda.NewFromConfig(sdkConfig)
    
    	maxItems := 10
    	fmt.Printf("Let's list up to %v functions for your account.\n", maxItems)
    	result, err := lambdaClient.ListFunctions(ctx, &lambda.ListFunctionsInput{
    		MaxItems: aws.Int32(int32(maxItems)),
    	})
    	if err != nil {
    		fmt.Printf("Couldn't list functions for your account. Here's why: %v\n", err)
    		return
    	}
    	if len(result.Functions) == 0 {
    		fmt.Println("You don't have any functions!")
    	} else {
    		for _, function := range result.Functions {
    			fmt.Printf("\t%v\n", *function.FunctionName)
    		}
    	}
    }
    
    
    

  * For API details, see [ListFunctions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.ListFunctions) in _AWS SDK for Go API Reference_. 




###### Topics

  * Basics

  * Actions

  * Scenarios

  * Serverless examples

  * AWS community contributions




## Basics

The following code example shows how to:

  * Create an IAM role and Lambda function, then upload handler code.

  * Invoke the function with a single parameter and get results.

  * Update the function code and configure with an environment variable.

  * Invoke the function with new parameters and get results. Display the returned execution log.

  * List the functions for your account, then clean up resources.




For more information, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html).

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 

Create an interactive scenario that shows you how to get started with Lambda functions.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"context"
    	"encoding/base64"
    	"encoding/json"
    	"errors"
    	"fmt"
    	"log"
    	"os"
    	"strings"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	iamtypes "github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/lambda/actions"
    )
    
    // GetStartedFunctionsScenario shows you how to use AWS Lambda to perform the following
    // actions:
    //
    //  1. Create an AWS Identity and Access Management (IAM) role and Lambda function, then upload handler code.
    //  2. Invoke the function with a single parameter and get results.
    //  3. Update the function code and configure with an environment variable.
    //  4. Invoke the function with new parameters and get results. Display the returned execution log.
    //  5. List the functions for your account, then clean up resources.
    type GetStartedFunctionsScenario struct {
    	sdkConfig       aws.Config
    	functionWrapper actions.FunctionWrapper
    	questioner      demotools.IQuestioner
    	helper          IScenarioHelper
    	isTestRun       bool
    }
    
    // NewGetStartedFunctionsScenario constructs a GetStartedFunctionsScenario instance from a configuration.
    // It uses the specified config to get a Lambda client and create wrappers for the actions
    // used in the scenario.
    func NewGetStartedFunctionsScenario(sdkConfig aws.Config, questioner demotools.IQuestioner,
    	helper IScenarioHelper) GetStartedFunctionsScenario {
    	lambdaClient := lambda.NewFromConfig(sdkConfig)
    	return GetStartedFunctionsScenario{
    		sdkConfig:       sdkConfig,
    		functionWrapper: actions.FunctionWrapper{LambdaClient: lambdaClient},
    		questioner:      questioner,
    		helper:          helper,
    	}
    }
    
    // Run runs the interactive scenario.
    func (scenario GetStartedFunctionsScenario) Run(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Printf("Something went wrong with the demo.\n")
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the AWS Lambda get started with functions demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	role := scenario.GetOrCreateRole(ctx)
    	funcName := scenario.CreateFunction(ctx, role)
    	scenario.InvokeIncrement(ctx, funcName)
    	scenario.UpdateFunction(ctx, funcName)
    	scenario.InvokeCalculator(ctx, funcName)
    	scenario.ListFunctions(ctx)
    	scenario.Cleanup(ctx, role, funcName)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // GetOrCreateRole checks whether the specified role exists and returns it if it does.
    // Otherwise, a role is created that specifies Lambda as a trusted principal.
    // The AWSLambdaBasicExecutionRole managed policy is attached to the role and the role
    // is returned.
    func (scenario GetStartedFunctionsScenario) GetOrCreateRole(ctx context.Context) *iamtypes.Role {
    	var role *iamtypes.Role
    	iamClient := iam.NewFromConfig(scenario.sdkConfig)
    	log.Println("First, we need an IAM role that Lambda can assume.")
    	roleName := scenario.questioner.Ask("Enter a name for the role:", demotools.NotEmpty{})
    	getOutput, err := iamClient.GetRole(ctx, &iam.GetRoleInput{
    		RoleName: aws.String(roleName)})
    	if err != nil {
    		var noSuch *iamtypes.NoSuchEntityException
    		if errors.As(err, &noSuch) {
    			log.Printf("Role %v doesn't exist. Creating it....\n", roleName)
    		} else {
    			log.Panicf("Couldn't check whether role %v exists. Here's why: %v\n",
    				roleName, err)
    		}
    	} else {
    		role = getOutput.Role
    		log.Printf("Found role %v.\n", *role.RoleName)
    	}
    	if role == nil {
    		trustPolicy := PolicyDocument{
    			Version: "2012-10-17",
    			Statement: []PolicyStatement{{
    				Effect:    "Allow",
    				Principal: map[string]string{"Service": "lambda.amazonaws.com"},
    				Action:    []string{"sts:AssumeRole"},
    			}},
    		}
    		policyArn := "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    		createOutput, err := iamClient.CreateRole(ctx, &iam.CreateRoleInput{
    			AssumeRolePolicyDocument: aws.String(trustPolicy.String()),
    			RoleName:                 aws.String(roleName),
    		})
    		if err != nil {
    			log.Panicf("Couldn't create role %v. Here's why: %v\n", roleName, err)
    		}
    		role = createOutput.Role
    		_, err = iamClient.AttachRolePolicy(ctx, &iam.AttachRolePolicyInput{
    			PolicyArn: aws.String(policyArn),
    			RoleName:  aws.String(roleName),
    		})
    		if err != nil {
    			log.Panicf("Couldn't attach a policy to role %v. Here's why: %v\n", roleName, err)
    		}
    		log.Printf("Created role %v.\n", *role.RoleName)
    		log.Println("Let's give AWS a few seconds to propagate resources...")
    		scenario.helper.Pause(10)
    	}
    	log.Println(strings.Repeat("-", 88))
    	return role
    }
    
    // CreateFunction creates a Lambda function and uploads a handler written in Python.
    // The code for the Python handler is packaged as a []byte in .zip format.
    func (scenario GetStartedFunctionsScenario) CreateFunction(ctx context.Context, role *iamtypes.Role) string {
    	log.Println("Let's create a function that increments a number.\n" +
    		"The function uses the 'lambda_handler_basic.py' script found in the \n" +
    		"'handlers' directory of this project.")
    	funcName := scenario.questioner.Ask("Enter a name for the Lambda function:", demotools.NotEmpty{})
    	zipPackage := scenario.helper.CreateDeploymentPackage("lambda_handler_basic.py", fmt.Sprintf("%v.py", funcName))
    	log.Printf("Creating function %v and waiting for it to be ready.", funcName)
    	funcState := scenario.functionWrapper.CreateFunction(ctx, funcName, fmt.Sprintf("%v.lambda_handler", funcName),
    		role.Arn, zipPackage)
    	log.Printf("Your function is %v.", funcState)
    	log.Println(strings.Repeat("-", 88))
    	return funcName
    }
    
    // InvokeIncrement invokes a Lambda function that increments a number. The function
    // parameters are contained in a Go struct that is used to serialize the parameters to
    // a JSON payload that is passed to the function.
    // The result payload is deserialized into a Go struct that contains an int value.
    func (scenario GetStartedFunctionsScenario) InvokeIncrement(ctx context.Context, funcName string) {
    	parameters := actions.IncrementParameters{Action: "increment"}
    	log.Println("Let's invoke our function. This function increments a number.")
    	parameters.Number = scenario.questioner.AskInt("Enter a number to increment:", demotools.NotEmpty{})
    	log.Printf("Invoking %v with %v...\n", funcName, parameters.Number)
    	invokeOutput := scenario.functionWrapper.Invoke(ctx, funcName, parameters, false)
    	var payload actions.LambdaResultInt
    	err := json.Unmarshal(invokeOutput.Payload, &payload)
    	if err != nil {
    		log.Panicf("Couldn't unmarshal payload from invoking %v. Here's why: %v\n",
    			funcName, err)
    	}
    	log.Printf("Invoking %v with %v returned %v.\n", funcName, parameters.Number, payload)
    	log.Println(strings.Repeat("-", 88))
    }
    
    // UpdateFunction updates the code for a Lambda function by uploading a simple arithmetic
    // calculator written in Python. The code for the Python handler is packaged as a
    // []byte in .zip format.
    // After the code is updated, the configuration is also updated with a new log
    // level that instructs the handler to log additional information.
    func (scenario GetStartedFunctionsScenario) UpdateFunction(ctx context.Context, funcName string) {
    	log.Println("Let's update the function to an arithmetic calculator.\n" +
    		"The function uses the 'lambda_handler_calculator.py' script found in the \n" +
    		"'handlers' directory of this project.")
    	scenario.questioner.Ask("Press Enter when you're ready.")
    	log.Println("Creating deployment package...")
    	zipPackage := scenario.helper.CreateDeploymentPackage("lambda_handler_calculator.py",
    		fmt.Sprintf("%v.py", funcName))
    	log.Println("...and updating the Lambda function and waiting for it to be ready.")
    	funcState := scenario.functionWrapper.UpdateFunctionCode(ctx, funcName, zipPackage)
    	log.Printf("Updated function %v. Its current state is %v.", funcName, funcState)
    	log.Println("This function uses an environment variable to control logging level.")
    	log.Println("Let's set it to DEBUG to get the most logging.")
    	scenario.functionWrapper.UpdateFunctionConfiguration(ctx, funcName,
    		map[string]string{"LOG_LEVEL": "DEBUG"})
    	log.Println(strings.Repeat("-", 88))
    }
    
    // InvokeCalculator invokes the Lambda calculator function. The parameters are stored in a
    // Go struct that is used to serialize the parameters to a JSON payload. That payload is then passed
    // to the function.
    // The result payload is deserialized to a Go struct that stores the result as either an
    // int or float32, depending on the kind of operation that was specified.
    func (scenario GetStartedFunctionsScenario) InvokeCalculator(ctx context.Context, funcName string) {
    	wantInvoke := true
    	choices := []string{"plus", "minus", "times", "divided-by"}
    	for wantInvoke {
    		choice := scenario.questioner.AskChoice("Select an arithmetic operation:\n", choices)
    		x := scenario.questioner.AskInt("Enter a value for x:", demotools.NotEmpty{})
    		y := scenario.questioner.AskInt("Enter a value for y:", demotools.NotEmpty{})
    		log.Printf("Invoking %v %v %v...", x, choices[choice], y)
    		calcParameters := actions.CalculatorParameters{
    			Action: choices[choice],
    			X:      x,
    			Y:      y,
    		}
    		invokeOutput := scenario.functionWrapper.Invoke(ctx, funcName, calcParameters, true)
    		var payload any
    		if choice == 3 { // divide-by results in a float.
    			payload = actions.LambdaResultFloat{}
    		} else {
    			payload = actions.LambdaResultInt{}
    		}
    		err := json.Unmarshal(invokeOutput.Payload, &payload)
    		if err != nil {
    			log.Panicf("Couldn't unmarshal payload from invoking %v. Here's why: %v\n",
    				funcName, err)
    		}
    		log.Printf("Invoking %v with %v %v %v returned %v.\n", funcName,
    			calcParameters.X, calcParameters.Action, calcParameters.Y, payload)
    		scenario.questioner.Ask("Press Enter to see the logs from the call.")
    		logRes, err := base64.StdEncoding.DecodeString(*invokeOutput.LogResult)
    		if err != nil {
    			log.Panicf("Couldn't decode log result. Here's why: %v\n", err)
    		}
    		log.Println(string(logRes))
    		wantInvoke = scenario.questioner.AskBool("Do you want to calculate again? (y/n)", "y")
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    // ListFunctions lists up to the specified number of functions for your account.
    func (scenario GetStartedFunctionsScenario) ListFunctions(ctx context.Context) {
    	count := scenario.questioner.AskInt(
    		"Let's list functions for your account. How many do you want to see?", demotools.NotEmpty{})
    	functions := scenario.functionWrapper.ListFunctions(ctx, count)
    	log.Printf("Found %v functions:", len(functions))
    	for _, function := range functions {
    		log.Printf("\t%v", *function.FunctionName)
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    // Cleanup removes the IAM and Lambda resources created by the example.
    func (scenario GetStartedFunctionsScenario) Cleanup(ctx context.Context, role *iamtypes.Role, funcName string) {
    	if scenario.questioner.AskBool("Do you want to clean up resources created for this example? (y/n)",
    		"y") {
    		iamClient := iam.NewFromConfig(scenario.sdkConfig)
    		policiesOutput, err := iamClient.ListAttachedRolePolicies(ctx,
    			&iam.ListAttachedRolePoliciesInput{RoleName: role.RoleName})
    		if err != nil {
    			log.Panicf("Couldn't get policies attached to role %v. Here's why: %v\n",
    				*role.RoleName, err)
    		}
    		for _, policy := range policiesOutput.AttachedPolicies {
    			_, err = iamClient.DetachRolePolicy(ctx, &iam.DetachRolePolicyInput{
    				PolicyArn: policy.PolicyArn, RoleName: role.RoleName,
    			})
    			if err != nil {
    				log.Panicf("Couldn't detach policy %v from role %v. Here's why: %v\n",
    					*policy.PolicyArn, *role.RoleName, err)
    			}
    		}
    		_, err = iamClient.DeleteRole(ctx, &iam.DeleteRoleInput{RoleName: role.RoleName})
    		if err != nil {
    			log.Panicf("Couldn't delete role %v. Here's why: %v\n", *role.RoleName, err)
    		}
    		log.Printf("Deleted role %v.\n", *role.RoleName)
    
    		scenario.functionWrapper.DeleteFunction(ctx, funcName)
    		log.Printf("Deleted function %v.\n", funcName)
    	} else {
    		log.Println("Okay. Don't forget to delete the resources when you're done with them.")
    	}
    }
    
    // IScenarioHelper abstracts I/O and wait functions from a scenario so that they
    // can be mocked for unit testing.
    type IScenarioHelper interface {
    	Pause(secs int)
    	CreateDeploymentPackage(sourceFile string, destinationFile string) *bytes.Buffer
    }
    
    // ScenarioHelper lets the caller specify the path to Lambda handler functions.
    type ScenarioHelper struct {
    	HandlerPath string
    }
    
    // Pause waits for the specified number of seconds.
    func (helper *ScenarioHelper) Pause(secs int) {
    	time.Sleep(time.Duration(secs) * time.Second)
    }
    
    // CreateDeploymentPackage creates an AWS Lambda deployment package from a source file. The
    // deployment package is stored in .zip format in a bytes.Buffer. The buffer can be
    // used to pass a []byte to Lambda when creating the function.
    // The specified destinationFile is the name to give the file when it's deployed to Lambda.
    func (helper *ScenarioHelper) CreateDeploymentPackage(sourceFile string, destinationFile string) *bytes.Buffer {
    	var err error
    	buffer := &bytes.Buffer{}
    	writer := zip.NewWriter(buffer)
    	zFile, err := writer.Create(destinationFile)
    	if err != nil {
    		log.Panicf("Couldn't create destination archive %v. Here's why: %v\n", destinationFile, err)
    	}
    	sourceBody, err := os.ReadFile(fmt.Sprintf("%v/%v", helper.HandlerPath, sourceFile))
    	if err != nil {
    		log.Panicf("Couldn't read handler source file %v. Here's why: %v\n",
    			sourceFile, err)
    	} else {
    		_, err = zFile.Write(sourceBody)
    		if err != nil {
    			log.Panicf("Couldn't write handler %v to zip archive. Here's why: %v\n",
    				sourceFile, err)
    		}
    	}
    	err = writer.Close()
    	if err != nil {
    		log.Panicf("Couldn't close zip writer. Here's why: %v\n", err)
    	}
    	return buffer
    }
    
    
    

Create a struct that wraps individual Lambda actions.
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    // GetFunction gets data about the Lambda function specified by functionName.
    func (wrapper FunctionWrapper) GetFunction(ctx context.Context, functionName string) types.State {
    	var state types.State
    	funcOutput, err := wrapper.LambdaClient.GetFunction(ctx, &lambda.GetFunctionInput{
    		FunctionName: aws.String(functionName),
    	})
    	if err != nil {
    		log.Panicf("Couldn't get function %v. Here's why: %v\n", functionName, err)
    	} else {
    		state = funcOutput.Configuration.State
    	}
    	return state
    }
    
    
    
    // CreateFunction creates a new Lambda function from code contained in the zipPackage
    // buffer. The specified handlerName must match the name of the file and function
    // contained in the uploaded code. The role specified by iamRoleArn is assumed by
    // Lambda and grants specific permissions.
    // When the function already exists, types.StateActive is returned.
    // When the function is created, a lambda.FunctionActiveV2Waiter is used to wait until the
    // function is active.
    func (wrapper FunctionWrapper) CreateFunction(ctx context.Context, functionName string, handlerName string,
    	iamRoleArn *string, zipPackage *bytes.Buffer) types.State {
    	var state types.State
    	_, err := wrapper.LambdaClient.CreateFunction(ctx, &lambda.CreateFunctionInput{
    		Code:         &types.FunctionCode{ZipFile: zipPackage.Bytes()},
    		FunctionName: aws.String(functionName),
    		Role:         iamRoleArn,
    		Handler:      aws.String(handlerName),
    		Publish:      true,
    		Runtime:      types.RuntimePython39,
    	})
    	if err != nil {
    		var resConflict *types.ResourceConflictException
    		if errors.As(err, &resConflict) {
    			log.Printf("Function %v already exists.\n", functionName)
    			state = types.StateActive
    		} else {
    			log.Panicf("Couldn't create function %v. Here's why: %v\n", functionName, err)
    		}
    	} else {
    		waiter := lambda.NewFunctionActiveV2Waiter(wrapper.LambdaClient)
    		funcOutput, err := waiter.WaitForOutput(ctx, &lambda.GetFunctionInput{
    			FunctionName: aws.String(functionName)}, 1*time.Minute)
    		if err != nil {
    			log.Panicf("Couldn't wait for function %v to be active. Here's why: %v\n", functionName, err)
    		} else {
    			state = funcOutput.Configuration.State
    		}
    	}
    	return state
    }
    
    
    
    // UpdateFunctionCode updates the code for the Lambda function specified by functionName.
    // The existing code for the Lambda function is entirely replaced by the code in the
    // zipPackage buffer. After the update action is called, a lambda.FunctionUpdatedV2Waiter
    // is used to wait until the update is successful.
    func (wrapper FunctionWrapper) UpdateFunctionCode(ctx context.Context, functionName string, zipPackage *bytes.Buffer) types.State {
    	var state types.State
    	_, err := wrapper.LambdaClient.UpdateFunctionCode(ctx, &lambda.UpdateFunctionCodeInput{
    		FunctionName: aws.String(functionName), ZipFile: zipPackage.Bytes(),
    	})
    	if err != nil {
    		log.Panicf("Couldn't update code for function %v. Here's why: %v\n", functionName, err)
    	} else {
    		waiter := lambda.NewFunctionUpdatedV2Waiter(wrapper.LambdaClient)
    		funcOutput, err := waiter.WaitForOutput(ctx, &lambda.GetFunctionInput{
    			FunctionName: aws.String(functionName)}, 1*time.Minute)
    		if err != nil {
    			log.Panicf("Couldn't wait for function %v to be active. Here's why: %v\n", functionName, err)
    		} else {
    			state = funcOutput.Configuration.State
    		}
    	}
    	return state
    }
    
    
    
    // UpdateFunctionConfiguration updates a map of environment variables configured for
    // the Lambda function specified by functionName.
    func (wrapper FunctionWrapper) UpdateFunctionConfiguration(ctx context.Context, functionName string, envVars map[string]string) {
    	_, err := wrapper.LambdaClient.UpdateFunctionConfiguration(ctx, &lambda.UpdateFunctionConfigurationInput{
    		FunctionName: aws.String(functionName),
    		Environment:  &types.Environment{Variables: envVars},
    	})
    	if err != nil {
    		log.Panicf("Couldn't update configuration for %v. Here's why: %v", functionName, err)
    	}
    }
    
    
    
    // ListFunctions lists up to maxItems functions for the account. This function uses a
    // lambda.ListFunctionsPaginator to paginate the results.
    func (wrapper FunctionWrapper) ListFunctions(ctx context.Context, maxItems int) []types.FunctionConfiguration {
    	var functions []types.FunctionConfiguration
    	paginator := lambda.NewListFunctionsPaginator(wrapper.LambdaClient, &lambda.ListFunctionsInput{
    		MaxItems: aws.Int32(int32(maxItems)),
    	})
    	for paginator.HasMorePages() && len(functions) < maxItems {
    		pageOutput, err := paginator.NextPage(ctx)
    		if err != nil {
    			log.Panicf("Couldn't list functions for your account. Here's why: %v\n", err)
    		}
    		functions = append(functions, pageOutput.Functions...)
    	}
    	return functions
    }
    
    
    
    // DeleteFunction deletes the Lambda function specified by functionName.
    func (wrapper FunctionWrapper) DeleteFunction(ctx context.Context, functionName string) {
    	_, err := wrapper.LambdaClient.DeleteFunction(ctx, &lambda.DeleteFunctionInput{
    		FunctionName: aws.String(functionName),
    	})
    	if err != nil {
    		log.Panicf("Couldn't delete function %v. Here's why: %v\n", functionName, err)
    	}
    }
    
    
    
    // Invoke invokes the Lambda function specified by functionName, passing the parameters
    // as a JSON payload. When getLog is true, types.LogTypeTail is specified, which tells
    // Lambda to include the last few log lines in the returned result.
    func (wrapper FunctionWrapper) Invoke(ctx context.Context, functionName string, parameters any, getLog bool) *lambda.InvokeOutput {
    	logType := types.LogTypeNone
    	if getLog {
    		logType = types.LogTypeTail
    	}
    	payload, err := json.Marshal(parameters)
    	if err != nil {
    		log.Panicf("Couldn't marshal parameters to JSON. Here's why %v\n", err)
    	}
    	invokeOutput, err := wrapper.LambdaClient.Invoke(ctx, &lambda.InvokeInput{
    		FunctionName: aws.String(functionName),
    		LogType:      logType,
    		Payload:      payload,
    	})
    	if err != nil {
    		log.Panicf("Couldn't invoke function %v. Here's why: %v\n", functionName, err)
    	}
    	return invokeOutput
    }
    
    
    
    // IncrementParameters is used to serialize parameters to the increment Lambda handler.
    type IncrementParameters struct {
    	Action string `json:"action"`
    	Number int    `json:"number"`
    }
    
    // CalculatorParameters is used to serialize parameters to the calculator Lambda handler.
    type CalculatorParameters struct {
    	Action string `json:"action"`
    	X      int    `json:"x"`
    	Y      int    `json:"y"`
    }
    
    // LambdaResultInt is used to deserialize an int result from a Lambda handler.
    type LambdaResultInt struct {
    	Result int `json:"result"`
    }
    
    // LambdaResultFloat is used to deserialize a float32 result from a Lambda handler.
    type LambdaResultFloat struct {
    	Result float32 `json:"result"`
    }
    
    
    

Define a Lambda handler that increments a number.
    
    
    import logging
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    
    def lambda_handler(event, context):
        """
        Accepts an action and a single number, performs the specified action on the number,
        and returns the result. The only allowable action is 'increment'.
    
        :param event: The event dict that contains the parameters sent when the function
                      is invoked.
        :param context: The context in which the function is called.
        :return: The result of the action.
        """
        result = None
        action = event.get("action")
        if action == "increment":
            result = event.get("number", 0) + 1
            logger.info("Calculated result of %s", result)
        else:
            logger.error("%s is not a valid action.", action)
    
        response = {"result": result}
        return response
    
    
    
    

Define a second Lambda handler that performs arithmetic operations.
    
    
    import logging
    import os
    
    
    logger = logging.getLogger()
    
    # Define a list of Python lambda functions that are called by this AWS Lambda function.
    ACTIONS = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "times": lambda x, y: x * y,
        "divided-by": lambda x, y: x / y,
    }
    
    
    def lambda_handler(event, context):
        """
        Accepts an action and two numbers, performs the specified action on the numbers,
        and returns the result.
    
        :param event: The event dict that contains the parameters sent when the function
                      is invoked.
        :param context: The context in which the function is called.
        :return: The result of the specified action.
        """
        # Set the log level based on a variable configured in the Lambda environment.
        logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
        logger.debug("Event: %s", event)
    
        action = event.get("action")
        func = ACTIONS.get(action)
        x = event.get("x")
        y = event.get("y")
        result = None
        try:
            if func is not None and x is not None and y is not None:
                result = func(x, y)
                logger.info("%s %s %s is %s", x, action, y, result)
            else:
                logger.error("I can't calculate %s %s %s.", x, action, y)
        except ZeroDivisionError:
            logger.warning("I can't divide %s by 0!", x)
    
        response = {"result": result}
        return response
    
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [CreateFunction](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.CreateFunction)

    * [DeleteFunction](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.DeleteFunction)

    * [GetFunction](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.GetFunction)

    * [Invoke](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.Invoke)

    * [ListFunctions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.ListFunctions)

    * [UpdateFunctionCode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.UpdateFunctionCode)

    * [UpdateFunctionConfiguration](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.UpdateFunctionConfiguration)




## Actions

The following code example shows how to use `CreateFunction`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    
    // CreateFunction creates a new Lambda function from code contained in the zipPackage
    // buffer. The specified handlerName must match the name of the file and function
    // contained in the uploaded code. The role specified by iamRoleArn is assumed by
    // Lambda and grants specific permissions.
    // When the function already exists, types.StateActive is returned.
    // When the function is created, a lambda.FunctionActiveV2Waiter is used to wait until the
    // function is active.
    func (wrapper FunctionWrapper) CreateFunction(ctx context.Context, functionName string, handlerName string,
    	iamRoleArn *string, zipPackage *bytes.Buffer) types.State {
    	var state types.State
    	_, err := wrapper.LambdaClient.CreateFunction(ctx, &lambda.CreateFunctionInput{
    		Code:         &types.FunctionCode{ZipFile: zipPackage.Bytes()},
    		FunctionName: aws.String(functionName),
    		Role:         iamRoleArn,
    		Handler:      aws.String(handlerName),
    		Publish:      true,
    		Runtime:      types.RuntimePython39,
    	})
    	if err != nil {
    		var resConflict *types.ResourceConflictException
    		if errors.As(err, &resConflict) {
    			log.Printf("Function %v already exists.\n", functionName)
    			state = types.StateActive
    		} else {
    			log.Panicf("Couldn't create function %v. Here's why: %v\n", functionName, err)
    		}
    	} else {
    		waiter := lambda.NewFunctionActiveV2Waiter(wrapper.LambdaClient)
    		funcOutput, err := waiter.WaitForOutput(ctx, &lambda.GetFunctionInput{
    			FunctionName: aws.String(functionName)}, 1*time.Minute)
    		if err != nil {
    			log.Panicf("Couldn't wait for function %v to be active. Here's why: %v\n", functionName, err)
    		} else {
    			state = funcOutput.Configuration.State
    		}
    	}
    	return state
    }
    
    
    

  * For API details, see [CreateFunction](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.CreateFunction) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteFunction`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    
    // DeleteFunction deletes the Lambda function specified by functionName.
    func (wrapper FunctionWrapper) DeleteFunction(ctx context.Context, functionName string) {
    	_, err := wrapper.LambdaClient.DeleteFunction(ctx, &lambda.DeleteFunctionInput{
    		FunctionName: aws.String(functionName),
    	})
    	if err != nil {
    		log.Panicf("Couldn't delete function %v. Here's why: %v\n", functionName, err)
    	}
    }
    
    
    

  * For API details, see [DeleteFunction](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.DeleteFunction) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetFunction`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    
    // GetFunction gets data about the Lambda function specified by functionName.
    func (wrapper FunctionWrapper) GetFunction(ctx context.Context, functionName string) types.State {
    	var state types.State
    	funcOutput, err := wrapper.LambdaClient.GetFunction(ctx, &lambda.GetFunctionInput{
    		FunctionName: aws.String(functionName),
    	})
    	if err != nil {
    		log.Panicf("Couldn't get function %v. Here's why: %v\n", functionName, err)
    	} else {
    		state = funcOutput.Configuration.State
    	}
    	return state
    }
    
    
    

  * For API details, see [GetFunction](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.GetFunction) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `Invoke`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    
    // Invoke invokes the Lambda function specified by functionName, passing the parameters
    // as a JSON payload. When getLog is true, types.LogTypeTail is specified, which tells
    // Lambda to include the last few log lines in the returned result.
    func (wrapper FunctionWrapper) Invoke(ctx context.Context, functionName string, parameters any, getLog bool) *lambda.InvokeOutput {
    	logType := types.LogTypeNone
    	if getLog {
    		logType = types.LogTypeTail
    	}
    	payload, err := json.Marshal(parameters)
    	if err != nil {
    		log.Panicf("Couldn't marshal parameters to JSON. Here's why %v\n", err)
    	}
    	invokeOutput, err := wrapper.LambdaClient.Invoke(ctx, &lambda.InvokeInput{
    		FunctionName: aws.String(functionName),
    		LogType:      logType,
    		Payload:      payload,
    	})
    	if err != nil {
    		log.Panicf("Couldn't invoke function %v. Here's why: %v\n", functionName, err)
    	}
    	return invokeOutput
    }
    
    
    

  * For API details, see [Invoke](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.Invoke) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListFunctions`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    
    // ListFunctions lists up to maxItems functions for the account. This function uses a
    // lambda.ListFunctionsPaginator to paginate the results.
    func (wrapper FunctionWrapper) ListFunctions(ctx context.Context, maxItems int) []types.FunctionConfiguration {
    	var functions []types.FunctionConfiguration
    	paginator := lambda.NewListFunctionsPaginator(wrapper.LambdaClient, &lambda.ListFunctionsInput{
    		MaxItems: aws.Int32(int32(maxItems)),
    	})
    	for paginator.HasMorePages() && len(functions) < maxItems {
    		pageOutput, err := paginator.NextPage(ctx)
    		if err != nil {
    			log.Panicf("Couldn't list functions for your account. Here's why: %v\n", err)
    		}
    		functions = append(functions, pageOutput.Functions...)
    	}
    	return functions
    }
    
    
    

  * For API details, see [ListFunctions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.ListFunctions) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `UpdateFunctionCode`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    
    // UpdateFunctionCode updates the code for the Lambda function specified by functionName.
    // The existing code for the Lambda function is entirely replaced by the code in the
    // zipPackage buffer. After the update action is called, a lambda.FunctionUpdatedV2Waiter
    // is used to wait until the update is successful.
    func (wrapper FunctionWrapper) UpdateFunctionCode(ctx context.Context, functionName string, zipPackage *bytes.Buffer) types.State {
    	var state types.State
    	_, err := wrapper.LambdaClient.UpdateFunctionCode(ctx, &lambda.UpdateFunctionCodeInput{
    		FunctionName: aws.String(functionName), ZipFile: zipPackage.Bytes(),
    	})
    	if err != nil {
    		log.Panicf("Couldn't update code for function %v. Here's why: %v\n", functionName, err)
    	} else {
    		waiter := lambda.NewFunctionUpdatedV2Waiter(wrapper.LambdaClient)
    		funcOutput, err := waiter.WaitForOutput(ctx, &lambda.GetFunctionInput{
    			FunctionName: aws.String(functionName)}, 1*time.Minute)
    		if err != nil {
    			log.Panicf("Couldn't wait for function %v to be active. Here's why: %v\n", functionName, err)
    		} else {
    			state = funcOutput.Configuration.State
    		}
    	}
    	return state
    }
    
    
    

  * For API details, see [UpdateFunctionCode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.UpdateFunctionCode) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `UpdateFunctionConfiguration`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/lambda#code-examples). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/lambda"
    	"github.com/aws/aws-sdk-go-v2/service/lambda/types"
    )
    
    // FunctionWrapper encapsulates function actions used in the examples.
    // It contains an AWS Lambda service client that is used to perform user actions.
    type FunctionWrapper struct {
    	LambdaClient *lambda.Client
    }
    
    
    
    // UpdateFunctionConfiguration updates a map of environment variables configured for
    // the Lambda function specified by functionName.
    func (wrapper FunctionWrapper) UpdateFunctionConfiguration(ctx context.Context, functionName string, envVars map[string]string) {
    	_, err := wrapper.LambdaClient.UpdateFunctionConfiguration(ctx, &lambda.UpdateFunctionConfigurationInput{
    		FunctionName: aws.String(functionName),
    		Environment:  &types.Environment{Variables: envVars},
    	})
    	if err != nil {
    		log.Panicf("Couldn't update configuration for %v. Here's why: %v", functionName, err)
    	}
    }
    
    
    

  * For API details, see [UpdateFunctionConfiguration](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/lambda#Client.UpdateFunctionConfiguration) in _AWS SDK for Go API Reference_. 




## Scenarios

The following code example shows how to automatically confirm known Amazon Cognito users with a Lambda function.

  * Configure a user pool to call a Lambda function for the `PreSignUp` trigger.

  * Sign up a user with Amazon Cognito.

  * The Lambda function scans a DynamoDB table and automatically confirms known users.

  * Sign in as the new user, then clean up resources.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/user_pools_and_lambda_triggers#code-examples). 

Run an interactive scenario at a command prompt.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"strings"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // AutoConfirm separates the steps of this scenario into individual functions so that
    // they are simpler to read and understand.
    type AutoConfirm struct {
    	helper       IScenarioHelper
    	questioner   demotools.IQuestioner
    	resources    Resources
    	cognitoActor *actions.CognitoActions
    }
    
    // NewAutoConfirm constructs a new auto confirm runner.
    func NewAutoConfirm(sdkConfig aws.Config, questioner demotools.IQuestioner, helper IScenarioHelper) AutoConfirm {
    	scenario := AutoConfirm{
    		helper:       helper,
    		questioner:   questioner,
    		resources:    Resources{},
    		cognitoActor: &actions.CognitoActions{CognitoClient: cognitoidentityprovider.NewFromConfig(sdkConfig)},
    	}
    	scenario.resources.init(scenario.cognitoActor, questioner)
    	return scenario
    }
    
    // AddPreSignUpTrigger adds a Lambda handler as an invocation target for the PreSignUp trigger.
    func (runner *AutoConfirm) AddPreSignUpTrigger(ctx context.Context, userPoolId string, functionArn string) {
    	log.Printf("Let's add a Lambda function to handle the PreSignUp trigger from Cognito.\n" +
    		"This trigger happens when a user signs up, and lets your function take action before the main Cognito\n" +
    		"sign up processing occurs.\n")
    	err := runner.cognitoActor.UpdateTriggers(
    		ctx, userPoolId,
    		actions.TriggerInfo{Trigger: actions.PreSignUp, HandlerArn: aws.String(functionArn)})
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Lambda function %v added to user pool %v to handle the PreSignUp trigger.\n",
    		functionArn, userPoolId)
    }
    
    // SignUpUser signs up a user from the known user table with a password you specify.
    func (runner *AutoConfirm) SignUpUser(ctx context.Context, clientId string, usersTable string) (string, string) {
    	log.Println("Let's sign up a user to your Cognito user pool. When the user's email matches an email in the\n" +
    		"DynamoDB known users table, it is automatically verified and the user is confirmed.")
    
    	knownUsers, err := runner.helper.GetKnownUsers(ctx, usersTable)
    	if err != nil {
    		panic(err)
    	}
    	userChoice := runner.questioner.AskChoice("Which user do you want to use?\n", knownUsers.UserNameList())
    	user := knownUsers.Users[userChoice]
    
    	var signedUp bool
    	var userConfirmed bool
    	password := runner.questioner.AskPassword("Enter a password that has at least eight characters, uppercase, lowercase, numbers and symbols.\n"+
    		"(the password will not display as you type):", 8)
    	for !signedUp {
    		log.Printf("Signing up user '%v' with email '%v' to Cognito.\n", user.UserName, user.UserEmail)
    		userConfirmed, err = runner.cognitoActor.SignUp(ctx, clientId, user.UserName, password, user.UserEmail)
    		if err != nil {
    			var invalidPassword *types.InvalidPasswordException
    			if errors.As(err, &invalidPassword) {
    				password = runner.questioner.AskPassword("Enter another password:", 8)
    			} else {
    				panic(err)
    			}
    		} else {
    			signedUp = true
    		}
    	}
    	log.Printf("User %v signed up, confirmed = %v.\n", user.UserName, userConfirmed)
    
    	log.Println(strings.Repeat("-", 88))
    
    	return user.UserName, password
    }
    
    // SignInUser signs in a user.
    func (runner *AutoConfirm) SignInUser(ctx context.Context, clientId string, userName string, password string) string {
    	runner.questioner.Ask("Press Enter when you're ready to continue.")
    	log.Printf("Let's sign in as %v...\n", userName)
    	authResult, err := runner.cognitoActor.SignIn(ctx, clientId, userName, password)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Successfully signed in. Your access token starts with: %v...\n", (*authResult.AccessToken)[:10])
    	log.Println(strings.Repeat("-", 88))
    	return *authResult.AccessToken
    }
    
    // Run runs the scenario.
    func (runner *AutoConfirm) Run(ctx context.Context, stackName string) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    			runner.resources.Cleanup(ctx)
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Printf("Welcome\n")
    
    	log.Println(strings.Repeat("-", 88))
    
    	stackOutputs, err := runner.helper.GetStackOutputs(ctx, stackName)
    	if err != nil {
    		panic(err)
    	}
    	runner.resources.userPoolId = stackOutputs["UserPoolId"]
    	runner.helper.PopulateUserTable(ctx, stackOutputs["TableName"])
    
    	runner.AddPreSignUpTrigger(ctx, stackOutputs["UserPoolId"], stackOutputs["AutoConfirmFunctionArn"])
    	runner.resources.triggers = append(runner.resources.triggers, actions.PreSignUp)
    	userName, password := runner.SignUpUser(ctx, stackOutputs["UserPoolClientId"], stackOutputs["TableName"])
    	runner.helper.ListRecentLogEvents(ctx, stackOutputs["AutoConfirmFunction"])
    	runner.resources.userAccessTokens = append(runner.resources.userAccessTokens,
    		runner.SignInUser(ctx, stackOutputs["UserPoolClientId"], userName, password))
    
    	runner.resources.Cleanup(ctx)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Handle the `PreSignUp` trigger with a Lambda function.
    
    
    import (
    	"context"
    	"log"
    	"os"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	dynamodbtypes "github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    const TABLE_NAME = "TABLE_NAME"
    
    // UserInfo defines structured user data that can be marshalled to a DynamoDB format.
    type UserInfo struct {
    	UserName  string `dynamodbav:"UserName"`
    	UserEmail string `dynamodbav:"UserEmail"`
    }
    
    // GetKey marshals the user email value to a DynamoDB key format.
    func (user UserInfo) GetKey() map[string]dynamodbtypes.AttributeValue {
    	userEmail, err := attributevalue.Marshal(user.UserEmail)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]dynamodbtypes.AttributeValue{"UserEmail": userEmail}
    }
    
    type handler struct {
    	dynamoClient *dynamodb.Client
    }
    
    // HandleRequest handles the PreSignUp event by looking up a user in an Amazon DynamoDB table and
    // specifying whether they should be confirmed and verified.
    func (h *handler) HandleRequest(ctx context.Context, event events.CognitoEventUserPoolsPreSignup) (events.CognitoEventUserPoolsPreSignup, error) {
    	log.Printf("Received presignup from %v for user '%v'", event.TriggerSource, event.UserName)
    	if event.TriggerSource != "PreSignUp_SignUp" {
    		// Other trigger sources, such as PreSignUp_AdminInitiateAuth, ignore the response from this handler.
    		return event, nil
    	}
    	tableName := os.Getenv(TABLE_NAME)
    	user := UserInfo{
    		UserEmail: event.Request.UserAttributes["email"],
    	}
    	log.Printf("Looking up email %v in table %v.\n", user.UserEmail, tableName)
    	output, err := h.dynamoClient.GetItem(ctx, &dynamodb.GetItemInput{
    		Key:       user.GetKey(),
    		TableName: aws.String(tableName),
    	})
    	if err != nil {
    		log.Printf("Error looking up email %v.\n", user.UserEmail)
    		return event, err
    	}
    	if output.Item == nil {
    		log.Printf("Email %v not found. Email verification is required.\n", user.UserEmail)
    		return event, err
    	}
    
    	err = attributevalue.UnmarshalMap(output.Item, &user)
    	if err != nil {
    		log.Printf("Couldn't unmarshal DynamoDB item. Here's why: %v\n", err)
    		return event, err
    	}
    
    	if user.UserName != event.UserName {
    		log.Printf("UserEmail %v found, but stored UserName '%v' does not match supplied UserName '%v'. Verification is required.\n",
    			user.UserEmail, user.UserName, event.UserName)
    	} else {
    		log.Printf("UserEmail %v found with matching UserName %v. User is confirmed.\n", user.UserEmail, user.UserName)
    		event.Response.AutoConfirmUser = true
    		event.Response.AutoVerifyEmail = true
    	}
    
    	return event, err
    }
    
    func main() {
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		log.Panicln(err)
    	}
    	h := handler{
    		dynamoClient: dynamodb.NewFromConfig(sdkConfig),
    	}
    	lambda.Start(h.HandleRequest)
    }
    
    
    

Create a struct that performs common tasks.
    
    
    import (
    	"context"
    	"log"
    	"strings"
    	"time"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cloudformation"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // IScenarioHelper defines common functions used by the workflows in this example.
    type IScenarioHelper interface {
    	Pause(secs int)
    	GetStackOutputs(ctx context.Context, stackName string) (actions.StackOutputs, error)
    	PopulateUserTable(ctx context.Context, tableName string)
    	GetKnownUsers(ctx context.Context, tableName string) (actions.UserList, error)
    	AddKnownUser(ctx context.Context, tableName string, user actions.User)
    	ListRecentLogEvents(ctx context.Context, functionName string)
    }
    
    // ScenarioHelper contains AWS wrapper structs used by the workflows in this example.
    type ScenarioHelper struct {
    	questioner  demotools.IQuestioner
    	dynamoActor *actions.DynamoActions
    	cfnActor    *actions.CloudFormationActions
    	cwlActor    *actions.CloudWatchLogsActions
    	isTestRun   bool
    }
    
    // NewScenarioHelper constructs a new scenario helper.
    func NewScenarioHelper(sdkConfig aws.Config, questioner demotools.IQuestioner) ScenarioHelper {
    	scenario := ScenarioHelper{
    		questioner:  questioner,
    		dynamoActor: &actions.DynamoActions{DynamoClient: dynamodb.NewFromConfig(sdkConfig)},
    		cfnActor:    &actions.CloudFormationActions{CfnClient: cloudformation.NewFromConfig(sdkConfig)},
    		cwlActor:    &actions.CloudWatchLogsActions{CwlClient: cloudwatchlogs.NewFromConfig(sdkConfig)},
    	}
    	return scenario
    }
    
    // Pause waits for the specified number of seconds.
    func (helper ScenarioHelper) Pause(secs int) {
    	if !helper.isTestRun {
    		time.Sleep(time.Duration(secs) * time.Second)
    	}
    }
    
    // GetStackOutputs gets the outputs from the specified CloudFormation stack in a structured format.
    func (helper ScenarioHelper) GetStackOutputs(ctx context.Context, stackName string) (actions.StackOutputs, error) {
    	return helper.cfnActor.GetOutputs(ctx, stackName), nil
    }
    
    // PopulateUserTable fills the known user table with example data.
    func (helper ScenarioHelper) PopulateUserTable(ctx context.Context, tableName string) {
    	log.Printf("First, let's add some users to the DynamoDB %v table we'll use for this example.\n", tableName)
    	err := helper.dynamoActor.PopulateTable(ctx, tableName)
    	if err != nil {
    		panic(err)
    	}
    }
    
    // GetKnownUsers gets the users from the known users table in a structured format.
    func (helper ScenarioHelper) GetKnownUsers(ctx context.Context, tableName string) (actions.UserList, error) {
    	knownUsers, err := helper.dynamoActor.Scan(ctx, tableName)
    	if err != nil {
    		log.Printf("Couldn't get known users from table %v. Here's why: %v\n", tableName, err)
    	}
    	return knownUsers, err
    }
    
    // AddKnownUser adds a user to the known users table.
    func (helper ScenarioHelper) AddKnownUser(ctx context.Context, tableName string, user actions.User) {
    	log.Printf("Adding user '%v' with email '%v' to the DynamoDB known users table...\n",
    		user.UserName, user.UserEmail)
    	err := helper.dynamoActor.AddUser(ctx, tableName, user)
    	if err != nil {
    		panic(err)
    	}
    }
    
    // ListRecentLogEvents gets the most recent log stream and events for the specified Lambda function and displays them.
    func (helper ScenarioHelper) ListRecentLogEvents(ctx context.Context, functionName string) {
    	log.Println("Waiting a few seconds to let Lambda write to CloudWatch Logs...")
    	helper.Pause(10)
    	log.Println("Okay, let's check the logs to find what's happened recently with your Lambda function.")
    	logStream, err := helper.cwlActor.GetLatestLogStream(ctx, functionName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Getting some recent events from log stream %v\n", *logStream.LogStreamName)
    	events, err := helper.cwlActor.GetLogEvents(ctx, functionName, *logStream.LogStreamName, 10)
    	if err != nil {
    		panic(err)
    	}
    	for _, event := range events {
    		log.Printf("\t%v", *event.Message)
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Create a struct that wraps Amazon Cognito actions.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
    )
    
    type CognitoActions struct {
    	CognitoClient *cognitoidentityprovider.Client
    }
    
    
    
    // Trigger and TriggerInfo define typed data for updating an Amazon Cognito trigger.
    type Trigger int
    
    const (
    	PreSignUp Trigger = iota
    	UserMigration
    	PostAuthentication
    )
    
    type TriggerInfo struct {
    	Trigger    Trigger
    	HandlerArn *string
    }
    
    // UpdateTriggers adds or removes Lambda triggers for a user pool. When a trigger is specified with a `nil` value,
    // it is removed from the user pool.
    func (actor CognitoActions) UpdateTriggers(ctx context.Context, userPoolId string, triggers ...TriggerInfo) error {
    	output, err := actor.CognitoClient.DescribeUserPool(ctx, &cognitoidentityprovider.DescribeUserPoolInput{
    		UserPoolId: aws.String(userPoolId),
    	})
    	if err != nil {
    		log.Printf("Couldn't get info about user pool %v. Here's why: %v\n", userPoolId, err)
    		return err
    	}
    	lambdaConfig := output.UserPool.LambdaConfig
    	for _, trigger := range triggers {
    		switch trigger.Trigger {
    		case PreSignUp:
    			lambdaConfig.PreSignUp = trigger.HandlerArn
    		case UserMigration:
    			lambdaConfig.UserMigration = trigger.HandlerArn
    		case PostAuthentication:
    			lambdaConfig.PostAuthentication = trigger.HandlerArn
    		}
    	}
    	_, err = actor.CognitoClient.UpdateUserPool(ctx, &cognitoidentityprovider.UpdateUserPoolInput{
    		UserPoolId:   aws.String(userPoolId),
    		LambdaConfig: lambdaConfig,
    	})
    	if err != nil {
    		log.Printf("Couldn't update user pool %v. Here's why: %v\n", userPoolId, err)
    	}
    	return err
    }
    
    
    
    // SignUp signs up a user with Amazon Cognito.
    func (actor CognitoActions) SignUp(ctx context.Context, clientId string, userName string, password string, userEmail string) (bool, error) {
    	confirmed := false
    	output, err := actor.CognitoClient.SignUp(ctx, &cognitoidentityprovider.SignUpInput{
    		ClientId: aws.String(clientId),
    		Password: aws.String(password),
    		Username: aws.String(userName),
    		UserAttributes: []types.AttributeType{
    			{Name: aws.String("email"), Value: aws.String(userEmail)},
    		},
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't sign up user %v. Here's why: %v\n", userName, err)
    		}
    	} else {
    		confirmed = output.UserConfirmed
    	}
    	return confirmed, err
    }
    
    
    
    // SignIn signs in a user to Amazon Cognito using a username and password authentication flow.
    func (actor CognitoActions) SignIn(ctx context.Context, clientId string, userName string, password string) (*types.AuthenticationResultType, error) {
    	var authResult *types.AuthenticationResultType
    	output, err := actor.CognitoClient.InitiateAuth(ctx, &cognitoidentityprovider.InitiateAuthInput{
    		AuthFlow:       "USER_PASSWORD_AUTH",
    		ClientId:       aws.String(clientId),
    		AuthParameters: map[string]string{"USERNAME": userName, "PASSWORD": password},
    	})
    	if err != nil {
    		var resetRequired *types.PasswordResetRequiredException
    		if errors.As(err, &resetRequired) {
    			log.Println(*resetRequired.Message)
    		} else {
    			log.Printf("Couldn't sign in user %v. Here's why: %v\n", userName, err)
    		}
    	} else {
    		authResult = output.AuthenticationResult
    	}
    	return authResult, err
    }
    
    
    
    // ForgotPassword starts a password recovery flow for a user. This flow typically sends a confirmation code
    // to the user's configured notification destination, such as email.
    func (actor CognitoActions) ForgotPassword(ctx context.Context, clientId string, userName string) (*types.CodeDeliveryDetailsType, error) {
    	output, err := actor.CognitoClient.ForgotPassword(ctx, &cognitoidentityprovider.ForgotPasswordInput{
    		ClientId: aws.String(clientId),
    		Username: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't start password reset for user '%v'. Here;s why: %v\n", userName, err)
    	}
    	return output.CodeDeliveryDetails, err
    }
    
    
    
    // ConfirmForgotPassword confirms a user with a confirmation code and a new password.
    func (actor CognitoActions) ConfirmForgotPassword(ctx context.Context, clientId string, code string, userName string, password string) error {
    	_, err := actor.CognitoClient.ConfirmForgotPassword(ctx, &cognitoidentityprovider.ConfirmForgotPasswordInput{
    		ClientId:         aws.String(clientId),
    		ConfirmationCode: aws.String(code),
    		Password:         aws.String(password),
    		Username:         aws.String(userName),
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't confirm user %v. Here's why: %v", userName, err)
    		}
    	}
    	return err
    }
    
    
    
    // DeleteUser removes a user from the user pool.
    func (actor CognitoActions) DeleteUser(ctx context.Context, userAccessToken string) error {
    	_, err := actor.CognitoClient.DeleteUser(ctx, &cognitoidentityprovider.DeleteUserInput{
    		AccessToken: aws.String(userAccessToken),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete user. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    
    // AdminCreateUser uses administrator credentials to add a user to a user pool. This method leaves the user
    // in a state that requires they enter a new password next time they sign in.
    func (actor CognitoActions) AdminCreateUser(ctx context.Context, userPoolId string, userName string, userEmail string) error {
    	_, err := actor.CognitoClient.AdminCreateUser(ctx, &cognitoidentityprovider.AdminCreateUserInput{
    		UserPoolId:     aws.String(userPoolId),
    		Username:       aws.String(userName),
    		MessageAction:  types.MessageActionTypeSuppress,
    		UserAttributes: []types.AttributeType{{Name: aws.String("email"), Value: aws.String(userEmail)}},
    	})
    	if err != nil {
    		var userExists *types.UsernameExistsException
    		if errors.As(err, &userExists) {
    			log.Printf("User %v already exists in the user pool.", userName)
    			err = nil
    		} else {
    			log.Printf("Couldn't create user %v. Here's why: %v\n", userName, err)
    		}
    	}
    	return err
    }
    
    
    
    // AdminSetUserPassword uses administrator credentials to set a password for a user without requiring a
    // temporary password.
    func (actor CognitoActions) AdminSetUserPassword(ctx context.Context, userPoolId string, userName string, password string) error {
    	_, err := actor.CognitoClient.AdminSetUserPassword(ctx, &cognitoidentityprovider.AdminSetUserPasswordInput{
    		Password:   aws.String(password),
    		UserPoolId: aws.String(userPoolId),
    		Username:   aws.String(userName),
    		Permanent:  true,
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't set password for user %v. Here's why: %v\n", userName, err)
    		}
    	}
    	return err
    }
    
    
    

Create a struct that wraps DynamoDB actions.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // DynamoActions encapsulates the Amazon Simple Notification Service (Amazon SNS) actions
    // used in the examples.
    type DynamoActions struct {
    	DynamoClient *dynamodb.Client
    }
    
    // User defines structured user data.
    type User struct {
    	UserName  string
    	UserEmail string
    	LastLogin *LoginInfo `dynamodbav:",omitempty"`
    }
    
    // LoginInfo defines structured custom login data.
    type LoginInfo struct {
    	UserPoolId string
    	ClientId   string
    	Time       string
    }
    
    // UserList defines a list of users.
    type UserList struct {
    	Users []User
    }
    
    // UserNameList returns the usernames contained in a UserList as a list of strings.
    func (users *UserList) UserNameList() []string {
    	names := make([]string, len(users.Users))
    	for i := 0; i < len(users.Users); i++ {
    		names[i] = users.Users[i].UserName
    	}
    	return names
    }
    
    // PopulateTable adds a set of test users to the table.
    func (actor DynamoActions) PopulateTable(ctx context.Context, tableName string) error {
    	var err error
    	var item map[string]types.AttributeValue
    	var writeReqs []types.WriteRequest
    	for i := 1; i < 4; i++ {
    		item, err = attributevalue.MarshalMap(User{UserName: fmt.Sprintf("test_user_%v", i), UserEmail: fmt.Sprintf("test_email_%v@example.com", i)})
    		if err != nil {
    			log.Printf("Couldn't marshall user into DynamoDB format. Here's why: %v\n", err)
    			return err
    		}
    		writeReqs = append(writeReqs, types.WriteRequest{PutRequest: &types.PutRequest{Item: item}})
    	}
    	_, err = actor.DynamoClient.BatchWriteItem(ctx, &dynamodb.BatchWriteItemInput{
    		RequestItems: map[string][]types.WriteRequest{tableName: writeReqs},
    	})
    	if err != nil {
    		log.Printf("Couldn't populate table %v with users. Here's why: %v\n", tableName, err)
    	}
    	return err
    }
    
    // Scan scans the table for all items.
    func (actor DynamoActions) Scan(ctx context.Context, tableName string) (UserList, error) {
    	var userList UserList
    	output, err := actor.DynamoClient.Scan(ctx, &dynamodb.ScanInput{
    		TableName: aws.String(tableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't scan table %v for items. Here's why: %v\n", tableName, err)
    	} else {
    		err = attributevalue.UnmarshalListOfMaps(output.Items, &userList.Users)
    		if err != nil {
    			log.Printf("Couldn't unmarshal items into users. Here's why: %v\n", err)
    		}
    	}
    	return userList, err
    }
    
    // AddUser adds a user item to a table.
    func (actor DynamoActions) AddUser(ctx context.Context, tableName string, user User) error {
    	userItem, err := attributevalue.MarshalMap(user)
    	if err != nil {
    		log.Printf("Couldn't marshall user to item. Here's why: %v\n", err)
    	}
    	_, err = actor.DynamoClient.PutItem(ctx, &dynamodb.PutItemInput{
    		Item:      userItem,
    		TableName: aws.String(tableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't put item in table %v. Here's why: %v", tableName, err)
    	}
    	return err
    }
    
    
    

Create a struct that wraps CloudWatch Logs actions.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs/types"
    )
    
    type CloudWatchLogsActions struct {
    	CwlClient *cloudwatchlogs.Client
    }
    
    // GetLatestLogStream gets the most recent log stream for a Lambda function.
    func (actor CloudWatchLogsActions) GetLatestLogStream(ctx context.Context, functionName string) (types.LogStream, error) {
    	var logStream types.LogStream
    	logGroupName := fmt.Sprintf("/aws/lambda/%s", functionName)
    	output, err := actor.CwlClient.DescribeLogStreams(ctx, &cloudwatchlogs.DescribeLogStreamsInput{
    		Descending:   aws.Bool(true),
    		Limit:        aws.Int32(1),
    		LogGroupName: aws.String(logGroupName),
    		OrderBy:      types.OrderByLastEventTime,
    	})
    	if err != nil {
    		log.Printf("Couldn't get log streams for log group %v. Here's why: %v\n", logGroupName, err)
    	} else {
    		logStream = output.LogStreams[0]
    	}
    	return logStream, err
    }
    
    // GetLogEvents gets the most recent eventCount events from the specified log stream.
    func (actor CloudWatchLogsActions) GetLogEvents(ctx context.Context, functionName string, logStreamName string, eventCount int32) (
    	[]types.OutputLogEvent, error) {
    	var events []types.OutputLogEvent
    	logGroupName := fmt.Sprintf("/aws/lambda/%s", functionName)
    	output, err := actor.CwlClient.GetLogEvents(ctx, &cloudwatchlogs.GetLogEventsInput{
    		LogStreamName: aws.String(logStreamName),
    		Limit:         aws.Int32(eventCount),
    		LogGroupName:  aws.String(logGroupName),
    	})
    	if err != nil {
    		log.Printf("Couldn't get log event for log stream %v. Here's why: %v\n", logStreamName, err)
    	} else {
    		events = output.Events
    	}
    	return events, err
    }
    
    
    

Create a struct that wraps CloudFormation actions.
    
    
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
    
    
    

Clean up resources.
    
    
    import (
    	"context"
    	"log"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // Resources keeps track of AWS resources created during an example and handles
    // cleanup when the example finishes.
    type Resources struct {
    	userPoolId       string
    	userAccessTokens []string
    	triggers         []actions.Trigger
    
    	cognitoActor *actions.CognitoActions
    	questioner   demotools.IQuestioner
    }
    
    func (resources *Resources) init(cognitoActor *actions.CognitoActions, questioner demotools.IQuestioner) {
    	resources.userAccessTokens = []string{}
    	resources.triggers = []actions.Trigger{}
    	resources.cognitoActor = cognitoActor
    	resources.questioner = questioner
    }
    
    // Cleanup deletes all AWS resources created during an example.
    func (resources *Resources) Cleanup(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Printf("Something went wrong during cleanup.\n%v\n", r)
    			log.Println("Use the AWS Management Console to remove any remaining resources \n" +
    				"that were created for this scenario.")
    		}
    	}()
    
    	wantDelete := resources.questioner.AskBool("Do you want to remove all of the AWS resources that were created "+
    		"during this demo (y/n)?", "y")
    	if wantDelete {
    		for _, accessToken := range resources.userAccessTokens {
    			err := resources.cognitoActor.DeleteUser(ctx, accessToken)
    			if err != nil {
    				log.Println("Couldn't delete user during cleanup.")
    				panic(err)
    			}
    			log.Println("Deleted user.")
    		}
    		triggerList := make([]actions.TriggerInfo, len(resources.triggers))
    		for i := 0; i < len(resources.triggers); i++ {
    			triggerList[i] = actions.TriggerInfo{Trigger: resources.triggers[i], HandlerArn: nil}
    		}
    		err := resources.cognitoActor.UpdateTriggers(ctx, resources.userPoolId, triggerList...)
    		if err != nil {
    			log.Println("Couldn't update Cognito triggers during cleanup.")
    			panic(err)
    		}
    		log.Println("Removed Cognito triggers from user pool.")
    	} else {
    		log.Println("Be sure to remove resources when you're done with them to avoid unexpected charges!")
    	}
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [DeleteUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.DeleteUser)

    * [InitiateAuth](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.InitiateAuth)

    * [SignUp](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.SignUp)

    * [UpdateUserPool](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.UpdateUserPool)




The following code example shows how to automatically migrate known Amazon Cognito users with a Lambda function.

  * Configure a user pool to call a Lambda function for the `MigrateUser` trigger.

  * Sign in to Amazon Cognito with a username and email that is not in the user pool.

  * The Lambda function scans a DynamoDB table and automatically migrates known users to the user pool.

  * Perform the forgot password flow to reset the password for the migrated user.

  * Sign in as the new user, then clean up resources.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/user_pools_and_lambda_triggers#code-examples). 

Run an interactive scenario at a command prompt.
    
    
    import (
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"strings"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // MigrateUser separates the steps of this scenario into individual functions so that
    // they are simpler to read and understand.
    type MigrateUser struct {
    	helper       IScenarioHelper
    	questioner   demotools.IQuestioner
    	resources    Resources
    	cognitoActor *actions.CognitoActions
    }
    
    // NewMigrateUser constructs a new migrate user runner.
    func NewMigrateUser(sdkConfig aws.Config, questioner demotools.IQuestioner, helper IScenarioHelper) MigrateUser {
    	scenario := MigrateUser{
    		helper:       helper,
    		questioner:   questioner,
    		resources:    Resources{},
    		cognitoActor: &actions.CognitoActions{CognitoClient: cognitoidentityprovider.NewFromConfig(sdkConfig)},
    	}
    	scenario.resources.init(scenario.cognitoActor, questioner)
    	return scenario
    }
    
    // AddMigrateUserTrigger adds a Lambda handler as an invocation target for the MigrateUser trigger.
    func (runner *MigrateUser) AddMigrateUserTrigger(ctx context.Context, userPoolId string, functionArn string) {
    	log.Printf("Let's add a Lambda function to handle the MigrateUser trigger from Cognito.\n" +
    		"This trigger happens when an unknown user signs in, and lets your function take action before Cognito\n" +
    		"rejects the user.\n\n")
    	err := runner.cognitoActor.UpdateTriggers(
    		ctx, userPoolId,
    		actions.TriggerInfo{Trigger: actions.UserMigration, HandlerArn: aws.String(functionArn)})
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Lambda function %v added to user pool %v to handle the MigrateUser trigger.\n",
    		functionArn, userPoolId)
    
    	log.Println(strings.Repeat("-", 88))
    }
    
    // SignInUser adds a new user to the known users table and signs that user in to Amazon Cognito.
    func (runner *MigrateUser) SignInUser(ctx context.Context, usersTable string, clientId string) (bool, actions.User) {
    	log.Println("Let's sign in a user to your Cognito user pool. When the username and email matches an entry in the\n" +
    		"DynamoDB known users table, the email is automatically verified and the user is migrated to the Cognito user pool.")
    
    	user := actions.User{}
    	user.UserName = runner.questioner.Ask("\nEnter a username:")
    	user.UserEmail = runner.questioner.Ask("\nEnter an email that you own. This email will be used to confirm user migration\n" +
    		"during this example:")
    
    	runner.helper.AddKnownUser(ctx, usersTable, user)
    
    	var err error
    	var resetRequired *types.PasswordResetRequiredException
    	var authResult *types.AuthenticationResultType
    	signedIn := false
    	for !signedIn && resetRequired == nil {
    		log.Printf("Signing in to Cognito as user '%v'. The expected result is a PasswordResetRequiredException.\n\n", user.UserName)
    		authResult, err = runner.cognitoActor.SignIn(ctx, clientId, user.UserName, "_")
    		if err != nil {
    			if errors.As(err, &resetRequired) {
    				log.Printf("\nUser '%v' is not in the Cognito user pool but was found in the DynamoDB known users table.\n"+
    					"User migration is started and a password reset is required.", user.UserName)
    			} else {
    				panic(err)
    			}
    		} else {
    			log.Printf("User '%v' successfully signed in. This is unexpected and probably means you have not\n"+
    				"cleaned up a previous run of this scenario, so the user exist in the Cognito user pool.\n"+
    				"You can continue this example and select to clean up resources, or manually remove\n"+
    				"the user from your user pool and try again.", user.UserName)
    			runner.resources.userAccessTokens = append(runner.resources.userAccessTokens, *authResult.AccessToken)
    			signedIn = true
    		}
    	}
    
    	log.Println(strings.Repeat("-", 88))
    	return resetRequired != nil, user
    }
    
    // ResetPassword starts a password recovery flow.
    func (runner *MigrateUser) ResetPassword(ctx context.Context, clientId string, user actions.User) {
    	wantCode := runner.questioner.AskBool(fmt.Sprintf("In order to migrate the user to Cognito, you must be able to receive a confirmation\n"+
    		"code by email at %v. Do you want to send a code (y/n)?", user.UserEmail), "y")
    	if !wantCode {
    		log.Println("To complete this example and successfully migrate a user to Cognito, you must enter an email\n" +
    			"you own that can receive a confirmation code.")
    		return
    	}
    	codeDelivery, err := runner.cognitoActor.ForgotPassword(ctx, clientId, user.UserName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("\nA confirmation code has been sent to %v.", *codeDelivery.Destination)
    	code := runner.questioner.Ask("Check your email and enter it here:")
    
    	confirmed := false
    	password := runner.questioner.AskPassword("\nEnter a password that has at least eight characters, uppercase, lowercase, numbers and symbols.\n"+
    		"(the password will not display as you type):", 8)
    	for !confirmed {
    		log.Printf("\nConfirming password reset for user '%v'.\n", user.UserName)
    		err = runner.cognitoActor.ConfirmForgotPassword(ctx, clientId, code, user.UserName, password)
    		if err != nil {
    			var invalidPassword *types.InvalidPasswordException
    			if errors.As(err, &invalidPassword) {
    				password = runner.questioner.AskPassword("\nEnter another password:", 8)
    			} else {
    				panic(err)
    			}
    		} else {
    			confirmed = true
    		}
    	}
    	log.Printf("User '%v' successfully confirmed and migrated.\n", user.UserName)
    	log.Println("Signing in with your username and password...")
    	authResult, err := runner.cognitoActor.SignIn(ctx, clientId, user.UserName, password)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Successfully signed in. Your access token starts with: %v...\n", (*authResult.AccessToken)[:10])
    	runner.resources.userAccessTokens = append(runner.resources.userAccessTokens, *authResult.AccessToken)
    
    	log.Println(strings.Repeat("-", 88))
    }
    
    // Run runs the scenario.
    func (runner *MigrateUser) Run(ctx context.Context, stackName string) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    			runner.resources.Cleanup(ctx)
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Printf("Welcome\n")
    
    	log.Println(strings.Repeat("-", 88))
    
    	stackOutputs, err := runner.helper.GetStackOutputs(ctx, stackName)
    	if err != nil {
    		panic(err)
    	}
    	runner.resources.userPoolId = stackOutputs["UserPoolId"]
    
    	runner.AddMigrateUserTrigger(ctx, stackOutputs["UserPoolId"], stackOutputs["MigrateUserFunctionArn"])
    	runner.resources.triggers = append(runner.resources.triggers, actions.UserMigration)
    	resetNeeded, user := runner.SignInUser(ctx, stackOutputs["TableName"], stackOutputs["UserPoolClientId"])
    	if resetNeeded {
    		runner.helper.ListRecentLogEvents(ctx, stackOutputs["MigrateUserFunction"])
    		runner.ResetPassword(ctx, stackOutputs["UserPoolClientId"], user)
    	}
    
    	runner.resources.Cleanup(ctx)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Handle the `MigrateUser` trigger with a Lambda function.
    
    
    import (
    	"context"
    	"log"
    	"os"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    )
    
    const TABLE_NAME = "TABLE_NAME"
    
    // UserInfo defines structured user data that can be marshalled to a DynamoDB format.
    type UserInfo struct {
    	UserName  string `dynamodbav:"UserName"`
    	UserEmail string `dynamodbav:"UserEmail"`
    }
    
    type handler struct {
    	dynamoClient *dynamodb.Client
    }
    
    // HandleRequest handles the MigrateUser event by looking up a user in an Amazon DynamoDB table and
    // specifying whether they should be migrated to the user pool.
    func (h *handler) HandleRequest(ctx context.Context, event events.CognitoEventUserPoolsMigrateUser) (events.CognitoEventUserPoolsMigrateUser, error) {
    	log.Printf("Received migrate trigger from %v for user '%v'", event.TriggerSource, event.UserName)
    	if event.TriggerSource != "UserMigration_Authentication" {
    		return event, nil
    	}
    	tableName := os.Getenv(TABLE_NAME)
    	user := UserInfo{
    		UserName: event.UserName,
    	}
    	log.Printf("Looking up user '%v' in table %v.\n", user.UserName, tableName)
    	filterEx := expression.Name("UserName").Equal(expression.Value(user.UserName))
    	expr, err := expression.NewBuilder().WithFilter(filterEx).Build()
    	if err != nil {
    		log.Printf("Error building expression to query for user '%v'.\n", user.UserName)
    		return event, err
    	}
    	output, err := h.dynamoClient.Scan(ctx, &dynamodb.ScanInput{
    		TableName:                 aws.String(tableName),
    		FilterExpression:          expr.Filter(),
    		ExpressionAttributeNames:  expr.Names(),
    		ExpressionAttributeValues: expr.Values(),
    	})
    	if err != nil {
    		log.Printf("Error looking up user '%v'.\n", user.UserName)
    		return event, err
    	}
    	if len(output.Items) == 0 {
    		log.Printf("User '%v' not found, not migrating user.\n", user.UserName)
    		return event, err
    	}
    
    	var users []UserInfo
    	err = attributevalue.UnmarshalListOfMaps(output.Items, &users)
    	if err != nil {
    		log.Printf("Couldn't unmarshal DynamoDB items. Here's why: %v\n", err)
    		return event, err
    	}
    
    	user = users[0]
    	log.Printf("UserName '%v' found with email %v. User is migrated and must reset password.\n", user.UserName, user.UserEmail)
    	event.CognitoEventUserPoolsMigrateUserResponse.UserAttributes = map[string]string{
    		"email":          user.UserEmail,
    		"email_verified": "true", // email_verified is required for the forgot password flow.
    	}
    	event.CognitoEventUserPoolsMigrateUserResponse.FinalUserStatus = "RESET_REQUIRED"
    	event.CognitoEventUserPoolsMigrateUserResponse.MessageAction = "SUPPRESS"
    
    	return event, err
    }
    
    func main() {
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		log.Panicln(err)
    	}
    	h := handler{
    		dynamoClient: dynamodb.NewFromConfig(sdkConfig),
    	}
    	lambda.Start(h.HandleRequest)
    }
    
    
    

Create a struct that performs common tasks.
    
    
    import (
    	"context"
    	"log"
    	"strings"
    	"time"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cloudformation"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // IScenarioHelper defines common functions used by the workflows in this example.
    type IScenarioHelper interface {
    	Pause(secs int)
    	GetStackOutputs(ctx context.Context, stackName string) (actions.StackOutputs, error)
    	PopulateUserTable(ctx context.Context, tableName string)
    	GetKnownUsers(ctx context.Context, tableName string) (actions.UserList, error)
    	AddKnownUser(ctx context.Context, tableName string, user actions.User)
    	ListRecentLogEvents(ctx context.Context, functionName string)
    }
    
    // ScenarioHelper contains AWS wrapper structs used by the workflows in this example.
    type ScenarioHelper struct {
    	questioner  demotools.IQuestioner
    	dynamoActor *actions.DynamoActions
    	cfnActor    *actions.CloudFormationActions
    	cwlActor    *actions.CloudWatchLogsActions
    	isTestRun   bool
    }
    
    // NewScenarioHelper constructs a new scenario helper.
    func NewScenarioHelper(sdkConfig aws.Config, questioner demotools.IQuestioner) ScenarioHelper {
    	scenario := ScenarioHelper{
    		questioner:  questioner,
    		dynamoActor: &actions.DynamoActions{DynamoClient: dynamodb.NewFromConfig(sdkConfig)},
    		cfnActor:    &actions.CloudFormationActions{CfnClient: cloudformation.NewFromConfig(sdkConfig)},
    		cwlActor:    &actions.CloudWatchLogsActions{CwlClient: cloudwatchlogs.NewFromConfig(sdkConfig)},
    	}
    	return scenario
    }
    
    // Pause waits for the specified number of seconds.
    func (helper ScenarioHelper) Pause(secs int) {
    	if !helper.isTestRun {
    		time.Sleep(time.Duration(secs) * time.Second)
    	}
    }
    
    // GetStackOutputs gets the outputs from the specified CloudFormation stack in a structured format.
    func (helper ScenarioHelper) GetStackOutputs(ctx context.Context, stackName string) (actions.StackOutputs, error) {
    	return helper.cfnActor.GetOutputs(ctx, stackName), nil
    }
    
    // PopulateUserTable fills the known user table with example data.
    func (helper ScenarioHelper) PopulateUserTable(ctx context.Context, tableName string) {
    	log.Printf("First, let's add some users to the DynamoDB %v table we'll use for this example.\n", tableName)
    	err := helper.dynamoActor.PopulateTable(ctx, tableName)
    	if err != nil {
    		panic(err)
    	}
    }
    
    // GetKnownUsers gets the users from the known users table in a structured format.
    func (helper ScenarioHelper) GetKnownUsers(ctx context.Context, tableName string) (actions.UserList, error) {
    	knownUsers, err := helper.dynamoActor.Scan(ctx, tableName)
    	if err != nil {
    		log.Printf("Couldn't get known users from table %v. Here's why: %v\n", tableName, err)
    	}
    	return knownUsers, err
    }
    
    // AddKnownUser adds a user to the known users table.
    func (helper ScenarioHelper) AddKnownUser(ctx context.Context, tableName string, user actions.User) {
    	log.Printf("Adding user '%v' with email '%v' to the DynamoDB known users table...\n",
    		user.UserName, user.UserEmail)
    	err := helper.dynamoActor.AddUser(ctx, tableName, user)
    	if err != nil {
    		panic(err)
    	}
    }
    
    // ListRecentLogEvents gets the most recent log stream and events for the specified Lambda function and displays them.
    func (helper ScenarioHelper) ListRecentLogEvents(ctx context.Context, functionName string) {
    	log.Println("Waiting a few seconds to let Lambda write to CloudWatch Logs...")
    	helper.Pause(10)
    	log.Println("Okay, let's check the logs to find what's happened recently with your Lambda function.")
    	logStream, err := helper.cwlActor.GetLatestLogStream(ctx, functionName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Getting some recent events from log stream %v\n", *logStream.LogStreamName)
    	events, err := helper.cwlActor.GetLogEvents(ctx, functionName, *logStream.LogStreamName, 10)
    	if err != nil {
    		panic(err)
    	}
    	for _, event := range events {
    		log.Printf("\t%v", *event.Message)
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Create a struct that wraps Amazon Cognito actions.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
    )
    
    type CognitoActions struct {
    	CognitoClient *cognitoidentityprovider.Client
    }
    
    
    
    // Trigger and TriggerInfo define typed data for updating an Amazon Cognito trigger.
    type Trigger int
    
    const (
    	PreSignUp Trigger = iota
    	UserMigration
    	PostAuthentication
    )
    
    type TriggerInfo struct {
    	Trigger    Trigger
    	HandlerArn *string
    }
    
    // UpdateTriggers adds or removes Lambda triggers for a user pool. When a trigger is specified with a `nil` value,
    // it is removed from the user pool.
    func (actor CognitoActions) UpdateTriggers(ctx context.Context, userPoolId string, triggers ...TriggerInfo) error {
    	output, err := actor.CognitoClient.DescribeUserPool(ctx, &cognitoidentityprovider.DescribeUserPoolInput{
    		UserPoolId: aws.String(userPoolId),
    	})
    	if err != nil {
    		log.Printf("Couldn't get info about user pool %v. Here's why: %v\n", userPoolId, err)
    		return err
    	}
    	lambdaConfig := output.UserPool.LambdaConfig
    	for _, trigger := range triggers {
    		switch trigger.Trigger {
    		case PreSignUp:
    			lambdaConfig.PreSignUp = trigger.HandlerArn
    		case UserMigration:
    			lambdaConfig.UserMigration = trigger.HandlerArn
    		case PostAuthentication:
    			lambdaConfig.PostAuthentication = trigger.HandlerArn
    		}
    	}
    	_, err = actor.CognitoClient.UpdateUserPool(ctx, &cognitoidentityprovider.UpdateUserPoolInput{
    		UserPoolId:   aws.String(userPoolId),
    		LambdaConfig: lambdaConfig,
    	})
    	if err != nil {
    		log.Printf("Couldn't update user pool %v. Here's why: %v\n", userPoolId, err)
    	}
    	return err
    }
    
    
    
    // SignUp signs up a user with Amazon Cognito.
    func (actor CognitoActions) SignUp(ctx context.Context, clientId string, userName string, password string, userEmail string) (bool, error) {
    	confirmed := false
    	output, err := actor.CognitoClient.SignUp(ctx, &cognitoidentityprovider.SignUpInput{
    		ClientId: aws.String(clientId),
    		Password: aws.String(password),
    		Username: aws.String(userName),
    		UserAttributes: []types.AttributeType{
    			{Name: aws.String("email"), Value: aws.String(userEmail)},
    		},
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't sign up user %v. Here's why: %v\n", userName, err)
    		}
    	} else {
    		confirmed = output.UserConfirmed
    	}
    	return confirmed, err
    }
    
    
    
    // SignIn signs in a user to Amazon Cognito using a username and password authentication flow.
    func (actor CognitoActions) SignIn(ctx context.Context, clientId string, userName string, password string) (*types.AuthenticationResultType, error) {
    	var authResult *types.AuthenticationResultType
    	output, err := actor.CognitoClient.InitiateAuth(ctx, &cognitoidentityprovider.InitiateAuthInput{
    		AuthFlow:       "USER_PASSWORD_AUTH",
    		ClientId:       aws.String(clientId),
    		AuthParameters: map[string]string{"USERNAME": userName, "PASSWORD": password},
    	})
    	if err != nil {
    		var resetRequired *types.PasswordResetRequiredException
    		if errors.As(err, &resetRequired) {
    			log.Println(*resetRequired.Message)
    		} else {
    			log.Printf("Couldn't sign in user %v. Here's why: %v\n", userName, err)
    		}
    	} else {
    		authResult = output.AuthenticationResult
    	}
    	return authResult, err
    }
    
    
    
    // ForgotPassword starts a password recovery flow for a user. This flow typically sends a confirmation code
    // to the user's configured notification destination, such as email.
    func (actor CognitoActions) ForgotPassword(ctx context.Context, clientId string, userName string) (*types.CodeDeliveryDetailsType, error) {
    	output, err := actor.CognitoClient.ForgotPassword(ctx, &cognitoidentityprovider.ForgotPasswordInput{
    		ClientId: aws.String(clientId),
    		Username: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't start password reset for user '%v'. Here;s why: %v\n", userName, err)
    	}
    	return output.CodeDeliveryDetails, err
    }
    
    
    
    // ConfirmForgotPassword confirms a user with a confirmation code and a new password.
    func (actor CognitoActions) ConfirmForgotPassword(ctx context.Context, clientId string, code string, userName string, password string) error {
    	_, err := actor.CognitoClient.ConfirmForgotPassword(ctx, &cognitoidentityprovider.ConfirmForgotPasswordInput{
    		ClientId:         aws.String(clientId),
    		ConfirmationCode: aws.String(code),
    		Password:         aws.String(password),
    		Username:         aws.String(userName),
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't confirm user %v. Here's why: %v", userName, err)
    		}
    	}
    	return err
    }
    
    
    
    // DeleteUser removes a user from the user pool.
    func (actor CognitoActions) DeleteUser(ctx context.Context, userAccessToken string) error {
    	_, err := actor.CognitoClient.DeleteUser(ctx, &cognitoidentityprovider.DeleteUserInput{
    		AccessToken: aws.String(userAccessToken),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete user. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    
    // AdminCreateUser uses administrator credentials to add a user to a user pool. This method leaves the user
    // in a state that requires they enter a new password next time they sign in.
    func (actor CognitoActions) AdminCreateUser(ctx context.Context, userPoolId string, userName string, userEmail string) error {
    	_, err := actor.CognitoClient.AdminCreateUser(ctx, &cognitoidentityprovider.AdminCreateUserInput{
    		UserPoolId:     aws.String(userPoolId),
    		Username:       aws.String(userName),
    		MessageAction:  types.MessageActionTypeSuppress,
    		UserAttributes: []types.AttributeType{{Name: aws.String("email"), Value: aws.String(userEmail)}},
    	})
    	if err != nil {
    		var userExists *types.UsernameExistsException
    		if errors.As(err, &userExists) {
    			log.Printf("User %v already exists in the user pool.", userName)
    			err = nil
    		} else {
    			log.Printf("Couldn't create user %v. Here's why: %v\n", userName, err)
    		}
    	}
    	return err
    }
    
    
    
    // AdminSetUserPassword uses administrator credentials to set a password for a user without requiring a
    // temporary password.
    func (actor CognitoActions) AdminSetUserPassword(ctx context.Context, userPoolId string, userName string, password string) error {
    	_, err := actor.CognitoClient.AdminSetUserPassword(ctx, &cognitoidentityprovider.AdminSetUserPasswordInput{
    		Password:   aws.String(password),
    		UserPoolId: aws.String(userPoolId),
    		Username:   aws.String(userName),
    		Permanent:  true,
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't set password for user %v. Here's why: %v\n", userName, err)
    		}
    	}
    	return err
    }
    
    
    

Create a struct that wraps DynamoDB actions.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // DynamoActions encapsulates the Amazon Simple Notification Service (Amazon SNS) actions
    // used in the examples.
    type DynamoActions struct {
    	DynamoClient *dynamodb.Client
    }
    
    // User defines structured user data.
    type User struct {
    	UserName  string
    	UserEmail string
    	LastLogin *LoginInfo `dynamodbav:",omitempty"`
    }
    
    // LoginInfo defines structured custom login data.
    type LoginInfo struct {
    	UserPoolId string
    	ClientId   string
    	Time       string
    }
    
    // UserList defines a list of users.
    type UserList struct {
    	Users []User
    }
    
    // UserNameList returns the usernames contained in a UserList as a list of strings.
    func (users *UserList) UserNameList() []string {
    	names := make([]string, len(users.Users))
    	for i := 0; i < len(users.Users); i++ {
    		names[i] = users.Users[i].UserName
    	}
    	return names
    }
    
    // PopulateTable adds a set of test users to the table.
    func (actor DynamoActions) PopulateTable(ctx context.Context, tableName string) error {
    	var err error
    	var item map[string]types.AttributeValue
    	var writeReqs []types.WriteRequest
    	for i := 1; i < 4; i++ {
    		item, err = attributevalue.MarshalMap(User{UserName: fmt.Sprintf("test_user_%v", i), UserEmail: fmt.Sprintf("test_email_%v@example.com", i)})
    		if err != nil {
    			log.Printf("Couldn't marshall user into DynamoDB format. Here's why: %v\n", err)
    			return err
    		}
    		writeReqs = append(writeReqs, types.WriteRequest{PutRequest: &types.PutRequest{Item: item}})
    	}
    	_, err = actor.DynamoClient.BatchWriteItem(ctx, &dynamodb.BatchWriteItemInput{
    		RequestItems: map[string][]types.WriteRequest{tableName: writeReqs},
    	})
    	if err != nil {
    		log.Printf("Couldn't populate table %v with users. Here's why: %v\n", tableName, err)
    	}
    	return err
    }
    
    // Scan scans the table for all items.
    func (actor DynamoActions) Scan(ctx context.Context, tableName string) (UserList, error) {
    	var userList UserList
    	output, err := actor.DynamoClient.Scan(ctx, &dynamodb.ScanInput{
    		TableName: aws.String(tableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't scan table %v for items. Here's why: %v\n", tableName, err)
    	} else {
    		err = attributevalue.UnmarshalListOfMaps(output.Items, &userList.Users)
    		if err != nil {
    			log.Printf("Couldn't unmarshal items into users. Here's why: %v\n", err)
    		}
    	}
    	return userList, err
    }
    
    // AddUser adds a user item to a table.
    func (actor DynamoActions) AddUser(ctx context.Context, tableName string, user User) error {
    	userItem, err := attributevalue.MarshalMap(user)
    	if err != nil {
    		log.Printf("Couldn't marshall user to item. Here's why: %v\n", err)
    	}
    	_, err = actor.DynamoClient.PutItem(ctx, &dynamodb.PutItemInput{
    		Item:      userItem,
    		TableName: aws.String(tableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't put item in table %v. Here's why: %v", tableName, err)
    	}
    	return err
    }
    
    
    

Create a struct that wraps CloudWatch Logs actions.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs/types"
    )
    
    type CloudWatchLogsActions struct {
    	CwlClient *cloudwatchlogs.Client
    }
    
    // GetLatestLogStream gets the most recent log stream for a Lambda function.
    func (actor CloudWatchLogsActions) GetLatestLogStream(ctx context.Context, functionName string) (types.LogStream, error) {
    	var logStream types.LogStream
    	logGroupName := fmt.Sprintf("/aws/lambda/%s", functionName)
    	output, err := actor.CwlClient.DescribeLogStreams(ctx, &cloudwatchlogs.DescribeLogStreamsInput{
    		Descending:   aws.Bool(true),
    		Limit:        aws.Int32(1),
    		LogGroupName: aws.String(logGroupName),
    		OrderBy:      types.OrderByLastEventTime,
    	})
    	if err != nil {
    		log.Printf("Couldn't get log streams for log group %v. Here's why: %v\n", logGroupName, err)
    	} else {
    		logStream = output.LogStreams[0]
    	}
    	return logStream, err
    }
    
    // GetLogEvents gets the most recent eventCount events from the specified log stream.
    func (actor CloudWatchLogsActions) GetLogEvents(ctx context.Context, functionName string, logStreamName string, eventCount int32) (
    	[]types.OutputLogEvent, error) {
    	var events []types.OutputLogEvent
    	logGroupName := fmt.Sprintf("/aws/lambda/%s", functionName)
    	output, err := actor.CwlClient.GetLogEvents(ctx, &cloudwatchlogs.GetLogEventsInput{
    		LogStreamName: aws.String(logStreamName),
    		Limit:         aws.Int32(eventCount),
    		LogGroupName:  aws.String(logGroupName),
    	})
    	if err != nil {
    		log.Printf("Couldn't get log event for log stream %v. Here's why: %v\n", logStreamName, err)
    	} else {
    		events = output.Events
    	}
    	return events, err
    }
    
    
    

Create a struct that wraps CloudFormation actions.
    
    
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
    
    
    

Clean up resources.
    
    
    import (
    	"context"
    	"log"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // Resources keeps track of AWS resources created during an example and handles
    // cleanup when the example finishes.
    type Resources struct {
    	userPoolId       string
    	userAccessTokens []string
    	triggers         []actions.Trigger
    
    	cognitoActor *actions.CognitoActions
    	questioner   demotools.IQuestioner
    }
    
    func (resources *Resources) init(cognitoActor *actions.CognitoActions, questioner demotools.IQuestioner) {
    	resources.userAccessTokens = []string{}
    	resources.triggers = []actions.Trigger{}
    	resources.cognitoActor = cognitoActor
    	resources.questioner = questioner
    }
    
    // Cleanup deletes all AWS resources created during an example.
    func (resources *Resources) Cleanup(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Printf("Something went wrong during cleanup.\n%v\n", r)
    			log.Println("Use the AWS Management Console to remove any remaining resources \n" +
    				"that were created for this scenario.")
    		}
    	}()
    
    	wantDelete := resources.questioner.AskBool("Do you want to remove all of the AWS resources that were created "+
    		"during this demo (y/n)?", "y")
    	if wantDelete {
    		for _, accessToken := range resources.userAccessTokens {
    			err := resources.cognitoActor.DeleteUser(ctx, accessToken)
    			if err != nil {
    				log.Println("Couldn't delete user during cleanup.")
    				panic(err)
    			}
    			log.Println("Deleted user.")
    		}
    		triggerList := make([]actions.TriggerInfo, len(resources.triggers))
    		for i := 0; i < len(resources.triggers); i++ {
    			triggerList[i] = actions.TriggerInfo{Trigger: resources.triggers[i], HandlerArn: nil}
    		}
    		err := resources.cognitoActor.UpdateTriggers(ctx, resources.userPoolId, triggerList...)
    		if err != nil {
    			log.Println("Couldn't update Cognito triggers during cleanup.")
    			panic(err)
    		}
    		log.Println("Removed Cognito triggers from user pool.")
    	} else {
    		log.Println("Be sure to remove resources when you're done with them to avoid unexpected charges!")
    	}
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [ConfirmForgotPassword](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ConfirmForgotPassword)

    * [DeleteUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.DeleteUser)

    * [ForgotPassword](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ForgotPassword)

    * [InitiateAuth](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.InitiateAuth)

    * [SignUp](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.SignUp)

    * [UpdateUserPool](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.UpdateUserPool)




The following code example shows how to write custom activity data with a Lambda function after Amazon Cognito user authentication.

  * Use administrator functions to add a user to a user pool.

  * Configure a user pool to call a Lambda function for the `PostAuthentication` trigger.

  * Sign the new user in to Amazon Cognito.

  * The Lambda function writes custom information to CloudWatch Logs and to an DynamoDB table.

  * Get and display custom data from the DynamoDB table, then clean up resources.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/user_pools_and_lambda_triggers#code-examples). 

Run an interactive scenario at a command prompt.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"strings"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // ActivityLog separates the steps of this scenario into individual functions so that
    // they are simpler to read and understand.
    type ActivityLog struct {
    	helper       IScenarioHelper
    	questioner   demotools.IQuestioner
    	resources    Resources
    	cognitoActor *actions.CognitoActions
    }
    
    // NewActivityLog constructs a new activity log runner.
    func NewActivityLog(sdkConfig aws.Config, questioner demotools.IQuestioner, helper IScenarioHelper) ActivityLog {
    	scenario := ActivityLog{
    		helper:       helper,
    		questioner:   questioner,
    		resources:    Resources{},
    		cognitoActor: &actions.CognitoActions{CognitoClient: cognitoidentityprovider.NewFromConfig(sdkConfig)},
    	}
    	scenario.resources.init(scenario.cognitoActor, questioner)
    	return scenario
    }
    
    // AddUserToPool selects a user from the known users table and uses administrator credentials to add the user to the user pool.
    func (runner *ActivityLog) AddUserToPool(ctx context.Context, userPoolId string, tableName string) (string, string) {
    	log.Println("To facilitate this example, let's add a user to the user pool using administrator privileges.")
    	users, err := runner.helper.GetKnownUsers(ctx, tableName)
    	if err != nil {
    		panic(err)
    	}
    	user := users.Users[0]
    	log.Printf("Adding known user %v to the user pool.\n", user.UserName)
    	err = runner.cognitoActor.AdminCreateUser(ctx, userPoolId, user.UserName, user.UserEmail)
    	if err != nil {
    		panic(err)
    	}
    	pwSet := false
    	password := runner.questioner.AskPassword("\nEnter a password that has at least eight characters, uppercase, lowercase, numbers and symbols.\n"+
    		"(the password will not display as you type):", 8)
    	for !pwSet {
    		log.Printf("\nSetting password for user '%v'.\n", user.UserName)
    		err = runner.cognitoActor.AdminSetUserPassword(ctx, userPoolId, user.UserName, password)
    		if err != nil {
    			var invalidPassword *types.InvalidPasswordException
    			if errors.As(err, &invalidPassword) {
    				password = runner.questioner.AskPassword("\nEnter another password:", 8)
    			} else {
    				panic(err)
    			}
    		} else {
    			pwSet = true
    		}
    	}
    
    	log.Println(strings.Repeat("-", 88))
    
    	return user.UserName, password
    }
    
    // AddActivityLogTrigger adds a Lambda handler as an invocation target for the PostAuthentication trigger.
    func (runner *ActivityLog) AddActivityLogTrigger(ctx context.Context, userPoolId string, activityLogArn string) {
    	log.Println("Let's add a Lambda function to handle the PostAuthentication trigger from Cognito.\n" +
    		"This trigger happens after a user is authenticated, and lets your function take action, such as logging\n" +
    		"the outcome.")
    	err := runner.cognitoActor.UpdateTriggers(
    		ctx, userPoolId,
    		actions.TriggerInfo{Trigger: actions.PostAuthentication, HandlerArn: aws.String(activityLogArn)})
    	if err != nil {
    		panic(err)
    	}
    	runner.resources.triggers = append(runner.resources.triggers, actions.PostAuthentication)
    	log.Printf("Lambda function %v added to user pool %v to handle PostAuthentication Cognito trigger.\n",
    		activityLogArn, userPoolId)
    
    	log.Println(strings.Repeat("-", 88))
    }
    
    // SignInUser signs in as the specified user.
    func (runner *ActivityLog) SignInUser(ctx context.Context, clientId string, userName string, password string) {
    	log.Printf("Now we'll sign in user %v and check the results in the logs and the DynamoDB table.", userName)
    	runner.questioner.Ask("Press Enter when you're ready.")
    	authResult, err := runner.cognitoActor.SignIn(ctx, clientId, userName, password)
    	if err != nil {
    		panic(err)
    	}
    	log.Println("Sign in successful.",
    		"The PostAuthentication Lambda handler writes custom information to CloudWatch Logs.")
    
    	runner.resources.userAccessTokens = append(runner.resources.userAccessTokens, *authResult.AccessToken)
    }
    
    // GetKnownUserLastLogin gets the login info for a user from the Amazon DynamoDB table and displays it.
    func (runner *ActivityLog) GetKnownUserLastLogin(ctx context.Context, tableName string, userName string) {
    	log.Println("The PostAuthentication handler also writes login data to the DynamoDB table.")
    	runner.questioner.Ask("Press Enter when you're ready to continue.")
    	users, err := runner.helper.GetKnownUsers(ctx, tableName)
    	if err != nil {
    		panic(err)
    	}
    	for _, user := range users.Users {
    		if user.UserName == userName {
    			log.Println("The last login info for the user in the known users table is:")
    			log.Printf("\t%+v", *user.LastLogin)
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    // Run runs the scenario.
    func (runner *ActivityLog) Run(ctx context.Context, stackName string) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    			runner.resources.Cleanup(ctx)
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Printf("Welcome\n")
    
    	log.Println(strings.Repeat("-", 88))
    
    	stackOutputs, err := runner.helper.GetStackOutputs(ctx, stackName)
    	if err != nil {
    		panic(err)
    	}
    	runner.resources.userPoolId = stackOutputs["UserPoolId"]
    	runner.helper.PopulateUserTable(ctx, stackOutputs["TableName"])
    	userName, password := runner.AddUserToPool(ctx, stackOutputs["UserPoolId"], stackOutputs["TableName"])
    
    	runner.AddActivityLogTrigger(ctx, stackOutputs["UserPoolId"], stackOutputs["ActivityLogFunctionArn"])
    	runner.SignInUser(ctx, stackOutputs["UserPoolClientId"], userName, password)
    	runner.helper.ListRecentLogEvents(ctx, stackOutputs["ActivityLogFunction"])
    	runner.GetKnownUserLastLogin(ctx, stackOutputs["TableName"], userName)
    
    	runner.resources.Cleanup(ctx)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Handle the `PostAuthentication` trigger with a Lambda function.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    	"time"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	dynamodbtypes "github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    const TABLE_NAME = "TABLE_NAME"
    
    // LoginInfo defines structured login data that can be marshalled to a DynamoDB format.
    type LoginInfo struct {
    	UserPoolId string `dynamodbav:"UserPoolId"`
    	ClientId   string `dynamodbav:"ClientId"`
    	Time       string `dynamodbav:"Time"`
    }
    
    // UserInfo defines structured user data that can be marshalled to a DynamoDB format.
    type UserInfo struct {
    	UserName  string    `dynamodbav:"UserName"`
    	UserEmail string    `dynamodbav:"UserEmail"`
    	LastLogin LoginInfo `dynamodbav:"LastLogin"`
    }
    
    // GetKey marshals the user email value to a DynamoDB key format.
    func (user UserInfo) GetKey() map[string]dynamodbtypes.AttributeValue {
    	userEmail, err := attributevalue.Marshal(user.UserEmail)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]dynamodbtypes.AttributeValue{"UserEmail": userEmail}
    }
    
    type handler struct {
    	dynamoClient *dynamodb.Client
    }
    
    // HandleRequest handles the PostAuthentication event by writing custom data to the logs and
    // to an Amazon DynamoDB table.
    func (h *handler) HandleRequest(ctx context.Context, event events.CognitoEventUserPoolsPostAuthentication) (events.CognitoEventUserPoolsPostAuthentication, error) {
    	log.Printf("Received post authentication trigger from %v for user '%v'", event.TriggerSource, event.UserName)
    	tableName := os.Getenv(TABLE_NAME)
    	user := UserInfo{
    		UserName:  event.UserName,
    		UserEmail: event.Request.UserAttributes["email"],
    		LastLogin: LoginInfo{
    			UserPoolId: event.UserPoolID,
    			ClientId:   event.CallerContext.ClientID,
    			Time:       time.Now().Format(time.UnixDate),
    		},
    	}
    	// Write to CloudWatch Logs.
    	fmt.Printf("%#v", user)
    
    	// Also write to an external system. This examples uses DynamoDB to demonstrate.
    	userMap, err := attributevalue.MarshalMap(user)
    	if err != nil {
    		log.Printf("Couldn't marshal to DynamoDB map. Here's why: %v\n", err)
    	} else if len(userMap) == 0 {
    		log.Printf("User info marshaled to an empty map.")
    	} else {
    		_, err := h.dynamoClient.PutItem(ctx, &dynamodb.PutItemInput{
    			Item:      userMap,
    			TableName: aws.String(tableName),
    		})
    		if err != nil {
    			log.Printf("Couldn't write to DynamoDB. Here's why: %v\n", err)
    		} else {
    			log.Printf("Wrote user info to DynamoDB table %v.\n", tableName)
    		}
    	}
    
    	return event, nil
    }
    
    func main() {
    	ctx := context.Background()
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		log.Panicln(err)
    	}
    	h := handler{
    		dynamoClient: dynamodb.NewFromConfig(sdkConfig),
    	}
    	lambda.Start(h.HandleRequest)
    }
    
    
    

Create a struct that performs common tasks.
    
    
    import (
    	"context"
    	"log"
    	"strings"
    	"time"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cloudformation"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // IScenarioHelper defines common functions used by the workflows in this example.
    type IScenarioHelper interface {
    	Pause(secs int)
    	GetStackOutputs(ctx context.Context, stackName string) (actions.StackOutputs, error)
    	PopulateUserTable(ctx context.Context, tableName string)
    	GetKnownUsers(ctx context.Context, tableName string) (actions.UserList, error)
    	AddKnownUser(ctx context.Context, tableName string, user actions.User)
    	ListRecentLogEvents(ctx context.Context, functionName string)
    }
    
    // ScenarioHelper contains AWS wrapper structs used by the workflows in this example.
    type ScenarioHelper struct {
    	questioner  demotools.IQuestioner
    	dynamoActor *actions.DynamoActions
    	cfnActor    *actions.CloudFormationActions
    	cwlActor    *actions.CloudWatchLogsActions
    	isTestRun   bool
    }
    
    // NewScenarioHelper constructs a new scenario helper.
    func NewScenarioHelper(sdkConfig aws.Config, questioner demotools.IQuestioner) ScenarioHelper {
    	scenario := ScenarioHelper{
    		questioner:  questioner,
    		dynamoActor: &actions.DynamoActions{DynamoClient: dynamodb.NewFromConfig(sdkConfig)},
    		cfnActor:    &actions.CloudFormationActions{CfnClient: cloudformation.NewFromConfig(sdkConfig)},
    		cwlActor:    &actions.CloudWatchLogsActions{CwlClient: cloudwatchlogs.NewFromConfig(sdkConfig)},
    	}
    	return scenario
    }
    
    // Pause waits for the specified number of seconds.
    func (helper ScenarioHelper) Pause(secs int) {
    	if !helper.isTestRun {
    		time.Sleep(time.Duration(secs) * time.Second)
    	}
    }
    
    // GetStackOutputs gets the outputs from the specified CloudFormation stack in a structured format.
    func (helper ScenarioHelper) GetStackOutputs(ctx context.Context, stackName string) (actions.StackOutputs, error) {
    	return helper.cfnActor.GetOutputs(ctx, stackName), nil
    }
    
    // PopulateUserTable fills the known user table with example data.
    func (helper ScenarioHelper) PopulateUserTable(ctx context.Context, tableName string) {
    	log.Printf("First, let's add some users to the DynamoDB %v table we'll use for this example.\n", tableName)
    	err := helper.dynamoActor.PopulateTable(ctx, tableName)
    	if err != nil {
    		panic(err)
    	}
    }
    
    // GetKnownUsers gets the users from the known users table in a structured format.
    func (helper ScenarioHelper) GetKnownUsers(ctx context.Context, tableName string) (actions.UserList, error) {
    	knownUsers, err := helper.dynamoActor.Scan(ctx, tableName)
    	if err != nil {
    		log.Printf("Couldn't get known users from table %v. Here's why: %v\n", tableName, err)
    	}
    	return knownUsers, err
    }
    
    // AddKnownUser adds a user to the known users table.
    func (helper ScenarioHelper) AddKnownUser(ctx context.Context, tableName string, user actions.User) {
    	log.Printf("Adding user '%v' with email '%v' to the DynamoDB known users table...\n",
    		user.UserName, user.UserEmail)
    	err := helper.dynamoActor.AddUser(ctx, tableName, user)
    	if err != nil {
    		panic(err)
    	}
    }
    
    // ListRecentLogEvents gets the most recent log stream and events for the specified Lambda function and displays them.
    func (helper ScenarioHelper) ListRecentLogEvents(ctx context.Context, functionName string) {
    	log.Println("Waiting a few seconds to let Lambda write to CloudWatch Logs...")
    	helper.Pause(10)
    	log.Println("Okay, let's check the logs to find what's happened recently with your Lambda function.")
    	logStream, err := helper.cwlActor.GetLatestLogStream(ctx, functionName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Getting some recent events from log stream %v\n", *logStream.LogStreamName)
    	events, err := helper.cwlActor.GetLogEvents(ctx, functionName, *logStream.LogStreamName, 10)
    	if err != nil {
    		panic(err)
    	}
    	for _, event := range events {
    		log.Printf("\t%v", *event.Message)
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Create a struct that wraps Amazon Cognito actions.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
    	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
    )
    
    type CognitoActions struct {
    	CognitoClient *cognitoidentityprovider.Client
    }
    
    
    
    // Trigger and TriggerInfo define typed data for updating an Amazon Cognito trigger.
    type Trigger int
    
    const (
    	PreSignUp Trigger = iota
    	UserMigration
    	PostAuthentication
    )
    
    type TriggerInfo struct {
    	Trigger    Trigger
    	HandlerArn *string
    }
    
    // UpdateTriggers adds or removes Lambda triggers for a user pool. When a trigger is specified with a `nil` value,
    // it is removed from the user pool.
    func (actor CognitoActions) UpdateTriggers(ctx context.Context, userPoolId string, triggers ...TriggerInfo) error {
    	output, err := actor.CognitoClient.DescribeUserPool(ctx, &cognitoidentityprovider.DescribeUserPoolInput{
    		UserPoolId: aws.String(userPoolId),
    	})
    	if err != nil {
    		log.Printf("Couldn't get info about user pool %v. Here's why: %v\n", userPoolId, err)
    		return err
    	}
    	lambdaConfig := output.UserPool.LambdaConfig
    	for _, trigger := range triggers {
    		switch trigger.Trigger {
    		case PreSignUp:
    			lambdaConfig.PreSignUp = trigger.HandlerArn
    		case UserMigration:
    			lambdaConfig.UserMigration = trigger.HandlerArn
    		case PostAuthentication:
    			lambdaConfig.PostAuthentication = trigger.HandlerArn
    		}
    	}
    	_, err = actor.CognitoClient.UpdateUserPool(ctx, &cognitoidentityprovider.UpdateUserPoolInput{
    		UserPoolId:   aws.String(userPoolId),
    		LambdaConfig: lambdaConfig,
    	})
    	if err != nil {
    		log.Printf("Couldn't update user pool %v. Here's why: %v\n", userPoolId, err)
    	}
    	return err
    }
    
    
    
    // SignUp signs up a user with Amazon Cognito.
    func (actor CognitoActions) SignUp(ctx context.Context, clientId string, userName string, password string, userEmail string) (bool, error) {
    	confirmed := false
    	output, err := actor.CognitoClient.SignUp(ctx, &cognitoidentityprovider.SignUpInput{
    		ClientId: aws.String(clientId),
    		Password: aws.String(password),
    		Username: aws.String(userName),
    		UserAttributes: []types.AttributeType{
    			{Name: aws.String("email"), Value: aws.String(userEmail)},
    		},
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't sign up user %v. Here's why: %v\n", userName, err)
    		}
    	} else {
    		confirmed = output.UserConfirmed
    	}
    	return confirmed, err
    }
    
    
    
    // SignIn signs in a user to Amazon Cognito using a username and password authentication flow.
    func (actor CognitoActions) SignIn(ctx context.Context, clientId string, userName string, password string) (*types.AuthenticationResultType, error) {
    	var authResult *types.AuthenticationResultType
    	output, err := actor.CognitoClient.InitiateAuth(ctx, &cognitoidentityprovider.InitiateAuthInput{
    		AuthFlow:       "USER_PASSWORD_AUTH",
    		ClientId:       aws.String(clientId),
    		AuthParameters: map[string]string{"USERNAME": userName, "PASSWORD": password},
    	})
    	if err != nil {
    		var resetRequired *types.PasswordResetRequiredException
    		if errors.As(err, &resetRequired) {
    			log.Println(*resetRequired.Message)
    		} else {
    			log.Printf("Couldn't sign in user %v. Here's why: %v\n", userName, err)
    		}
    	} else {
    		authResult = output.AuthenticationResult
    	}
    	return authResult, err
    }
    
    
    
    // ForgotPassword starts a password recovery flow for a user. This flow typically sends a confirmation code
    // to the user's configured notification destination, such as email.
    func (actor CognitoActions) ForgotPassword(ctx context.Context, clientId string, userName string) (*types.CodeDeliveryDetailsType, error) {
    	output, err := actor.CognitoClient.ForgotPassword(ctx, &cognitoidentityprovider.ForgotPasswordInput{
    		ClientId: aws.String(clientId),
    		Username: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't start password reset for user '%v'. Here;s why: %v\n", userName, err)
    	}
    	return output.CodeDeliveryDetails, err
    }
    
    
    
    // ConfirmForgotPassword confirms a user with a confirmation code and a new password.
    func (actor CognitoActions) ConfirmForgotPassword(ctx context.Context, clientId string, code string, userName string, password string) error {
    	_, err := actor.CognitoClient.ConfirmForgotPassword(ctx, &cognitoidentityprovider.ConfirmForgotPasswordInput{
    		ClientId:         aws.String(clientId),
    		ConfirmationCode: aws.String(code),
    		Password:         aws.String(password),
    		Username:         aws.String(userName),
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't confirm user %v. Here's why: %v", userName, err)
    		}
    	}
    	return err
    }
    
    
    
    // DeleteUser removes a user from the user pool.
    func (actor CognitoActions) DeleteUser(ctx context.Context, userAccessToken string) error {
    	_, err := actor.CognitoClient.DeleteUser(ctx, &cognitoidentityprovider.DeleteUserInput{
    		AccessToken: aws.String(userAccessToken),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete user. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    
    // AdminCreateUser uses administrator credentials to add a user to a user pool. This method leaves the user
    // in a state that requires they enter a new password next time they sign in.
    func (actor CognitoActions) AdminCreateUser(ctx context.Context, userPoolId string, userName string, userEmail string) error {
    	_, err := actor.CognitoClient.AdminCreateUser(ctx, &cognitoidentityprovider.AdminCreateUserInput{
    		UserPoolId:     aws.String(userPoolId),
    		Username:       aws.String(userName),
    		MessageAction:  types.MessageActionTypeSuppress,
    		UserAttributes: []types.AttributeType{{Name: aws.String("email"), Value: aws.String(userEmail)}},
    	})
    	if err != nil {
    		var userExists *types.UsernameExistsException
    		if errors.As(err, &userExists) {
    			log.Printf("User %v already exists in the user pool.", userName)
    			err = nil
    		} else {
    			log.Printf("Couldn't create user %v. Here's why: %v\n", userName, err)
    		}
    	}
    	return err
    }
    
    
    
    // AdminSetUserPassword uses administrator credentials to set a password for a user without requiring a
    // temporary password.
    func (actor CognitoActions) AdminSetUserPassword(ctx context.Context, userPoolId string, userName string, password string) error {
    	_, err := actor.CognitoClient.AdminSetUserPassword(ctx, &cognitoidentityprovider.AdminSetUserPasswordInput{
    		Password:   aws.String(password),
    		UserPoolId: aws.String(userPoolId),
    		Username:   aws.String(userName),
    		Permanent:  true,
    	})
    	if err != nil {
    		var invalidPassword *types.InvalidPasswordException
    		if errors.As(err, &invalidPassword) {
    			log.Println(*invalidPassword.Message)
    		} else {
    			log.Printf("Couldn't set password for user %v. Here's why: %v\n", userName, err)
    		}
    	}
    	return err
    }
    
    
    

Create a struct that wraps DynamoDB actions.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // DynamoActions encapsulates the Amazon Simple Notification Service (Amazon SNS) actions
    // used in the examples.
    type DynamoActions struct {
    	DynamoClient *dynamodb.Client
    }
    
    // User defines structured user data.
    type User struct {
    	UserName  string
    	UserEmail string
    	LastLogin *LoginInfo `dynamodbav:",omitempty"`
    }
    
    // LoginInfo defines structured custom login data.
    type LoginInfo struct {
    	UserPoolId string
    	ClientId   string
    	Time       string
    }
    
    // UserList defines a list of users.
    type UserList struct {
    	Users []User
    }
    
    // UserNameList returns the usernames contained in a UserList as a list of strings.
    func (users *UserList) UserNameList() []string {
    	names := make([]string, len(users.Users))
    	for i := 0; i < len(users.Users); i++ {
    		names[i] = users.Users[i].UserName
    	}
    	return names
    }
    
    // PopulateTable adds a set of test users to the table.
    func (actor DynamoActions) PopulateTable(ctx context.Context, tableName string) error {
    	var err error
    	var item map[string]types.AttributeValue
    	var writeReqs []types.WriteRequest
    	for i := 1; i < 4; i++ {
    		item, err = attributevalue.MarshalMap(User{UserName: fmt.Sprintf("test_user_%v", i), UserEmail: fmt.Sprintf("test_email_%v@example.com", i)})
    		if err != nil {
    			log.Printf("Couldn't marshall user into DynamoDB format. Here's why: %v\n", err)
    			return err
    		}
    		writeReqs = append(writeReqs, types.WriteRequest{PutRequest: &types.PutRequest{Item: item}})
    	}
    	_, err = actor.DynamoClient.BatchWriteItem(ctx, &dynamodb.BatchWriteItemInput{
    		RequestItems: map[string][]types.WriteRequest{tableName: writeReqs},
    	})
    	if err != nil {
    		log.Printf("Couldn't populate table %v with users. Here's why: %v\n", tableName, err)
    	}
    	return err
    }
    
    // Scan scans the table for all items.
    func (actor DynamoActions) Scan(ctx context.Context, tableName string) (UserList, error) {
    	var userList UserList
    	output, err := actor.DynamoClient.Scan(ctx, &dynamodb.ScanInput{
    		TableName: aws.String(tableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't scan table %v for items. Here's why: %v\n", tableName, err)
    	} else {
    		err = attributevalue.UnmarshalListOfMaps(output.Items, &userList.Users)
    		if err != nil {
    			log.Printf("Couldn't unmarshal items into users. Here's why: %v\n", err)
    		}
    	}
    	return userList, err
    }
    
    // AddUser adds a user item to a table.
    func (actor DynamoActions) AddUser(ctx context.Context, tableName string, user User) error {
    	userItem, err := attributevalue.MarshalMap(user)
    	if err != nil {
    		log.Printf("Couldn't marshall user to item. Here's why: %v\n", err)
    	}
    	_, err = actor.DynamoClient.PutItem(ctx, &dynamodb.PutItemInput{
    		Item:      userItem,
    		TableName: aws.String(tableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't put item in table %v. Here's why: %v", tableName, err)
    	}
    	return err
    }
    
    
    

Create a struct that wraps CloudWatch Logs actions.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
    	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs/types"
    )
    
    type CloudWatchLogsActions struct {
    	CwlClient *cloudwatchlogs.Client
    }
    
    // GetLatestLogStream gets the most recent log stream for a Lambda function.
    func (actor CloudWatchLogsActions) GetLatestLogStream(ctx context.Context, functionName string) (types.LogStream, error) {
    	var logStream types.LogStream
    	logGroupName := fmt.Sprintf("/aws/lambda/%s", functionName)
    	output, err := actor.CwlClient.DescribeLogStreams(ctx, &cloudwatchlogs.DescribeLogStreamsInput{
    		Descending:   aws.Bool(true),
    		Limit:        aws.Int32(1),
    		LogGroupName: aws.String(logGroupName),
    		OrderBy:      types.OrderByLastEventTime,
    	})
    	if err != nil {
    		log.Printf("Couldn't get log streams for log group %v. Here's why: %v\n", logGroupName, err)
    	} else {
    		logStream = output.LogStreams[0]
    	}
    	return logStream, err
    }
    
    // GetLogEvents gets the most recent eventCount events from the specified log stream.
    func (actor CloudWatchLogsActions) GetLogEvents(ctx context.Context, functionName string, logStreamName string, eventCount int32) (
    	[]types.OutputLogEvent, error) {
    	var events []types.OutputLogEvent
    	logGroupName := fmt.Sprintf("/aws/lambda/%s", functionName)
    	output, err := actor.CwlClient.GetLogEvents(ctx, &cloudwatchlogs.GetLogEventsInput{
    		LogStreamName: aws.String(logStreamName),
    		Limit:         aws.Int32(eventCount),
    		LogGroupName:  aws.String(logGroupName),
    	})
    	if err != nil {
    		log.Printf("Couldn't get log event for log stream %v. Here's why: %v\n", logStreamName, err)
    	} else {
    		events = output.Events
    	}
    	return events, err
    }
    
    
    

Create a struct that wraps CloudFormation actions.
    
    
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
    
    
    

Clean up resources.
    
    
    import (
    	"context"
    	"log"
    	"user_pools_and_lambda_triggers/actions"
    
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    )
    
    // Resources keeps track of AWS resources created during an example and handles
    // cleanup when the example finishes.
    type Resources struct {
    	userPoolId       string
    	userAccessTokens []string
    	triggers         []actions.Trigger
    
    	cognitoActor *actions.CognitoActions
    	questioner   demotools.IQuestioner
    }
    
    func (resources *Resources) init(cognitoActor *actions.CognitoActions, questioner demotools.IQuestioner) {
    	resources.userAccessTokens = []string{}
    	resources.triggers = []actions.Trigger{}
    	resources.cognitoActor = cognitoActor
    	resources.questioner = questioner
    }
    
    // Cleanup deletes all AWS resources created during an example.
    func (resources *Resources) Cleanup(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Printf("Something went wrong during cleanup.\n%v\n", r)
    			log.Println("Use the AWS Management Console to remove any remaining resources \n" +
    				"that were created for this scenario.")
    		}
    	}()
    
    	wantDelete := resources.questioner.AskBool("Do you want to remove all of the AWS resources that were created "+
    		"during this demo (y/n)?", "y")
    	if wantDelete {
    		for _, accessToken := range resources.userAccessTokens {
    			err := resources.cognitoActor.DeleteUser(ctx, accessToken)
    			if err != nil {
    				log.Println("Couldn't delete user during cleanup.")
    				panic(err)
    			}
    			log.Println("Deleted user.")
    		}
    		triggerList := make([]actions.TriggerInfo, len(resources.triggers))
    		for i := 0; i < len(resources.triggers); i++ {
    			triggerList[i] = actions.TriggerInfo{Trigger: resources.triggers[i], HandlerArn: nil}
    		}
    		err := resources.cognitoActor.UpdateTriggers(ctx, resources.userPoolId, triggerList...)
    		if err != nil {
    			log.Println("Couldn't update Cognito triggers during cleanup.")
    			panic(err)
    		}
    		log.Println("Removed Cognito triggers from user pool.")
    	} else {
    		log.Println("Be sure to remove resources when you're done with them to avoid unexpected charges!")
    	}
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [AdminCreateUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.AdminCreateUser)

    * [AdminSetUserPassword](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.AdminSetUserPassword)

    * [DeleteUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.DeleteUser)

    * [InitiateAuth](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.InitiateAuth)

    * [UpdateUserPool](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.UpdateUserPool)




## Serverless examples

The following code example shows how to implement a Lambda function that connects to an RDS database. The function makes a simple database request and returns the result.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/lambda-function-connect-rds-iam) repository. 

Connecting to an Amazon RDS database in a Lambda function using Go.
    
    
    /*
    Golang v2 code here.
    */
    
    package main
    
    import (
    	"context"
    	"database/sql"
    	"encoding/json"
    	"fmt"
    	"os"
    
    	"github.com/aws/aws-lambda-go/lambda"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/feature/rds/auth"
    	_ "github.com/go-sql-driver/mysql"
    )
    
    type MyEvent struct {
    	Name string `json:"name"`
    }
    
    func HandleRequest(event *MyEvent) (map[string]interface{}, error) {
    
    	var dbName string = os.Getenv("DatabaseName")
    	var dbUser string = os.Getenv("DatabaseUser")
    	var dbHost string = os.Getenv("DBHost") // Add hostname without https
    	var dbPort int = os.Getenv("Port")      // Add port number
    	var dbEndpoint string = fmt.Sprintf("%s:%d", dbHost, dbPort)
    	var region string = os.Getenv("AWS_REGION")
    
    	cfg, err := config.LoadDefaultConfig(context.TODO())
    	if err != nil {
    		panic("configuration error: " + err.Error())
    	}
    
    	authenticationToken, err := auth.BuildAuthToken(
    		context.TODO(), dbEndpoint, region, dbUser, cfg.Credentials)
    	if err != nil {
    		panic("failed to create authentication token: " + err.Error())
    	}
    
    	dsn := fmt.Sprintf("%s:%s@tcp(%s)/%s?tls=true&allowCleartextPasswords=true",
    		dbUser, authenticationToken, dbEndpoint, dbName,
    	)
    
    	db, err := sql.Open("mysql", dsn)
    	if err != nil {
    		panic(err)
    	}
    
    	defer db.Close()
    
    	var sum int
    	err = db.QueryRow("SELECT ?+? AS sum", 3, 2).Scan(&sum)
    	if err != nil {
    		panic(err)
    	}
    	s := fmt.Sprint(sum)
    	message := fmt.Sprintf("The selected sum is: %s", s)
    
    	messageBytes, err := json.Marshal(message)
    	if err != nil {
    		return nil, err
    	}
    
    	messageString := string(messageBytes)
    	return map[string]interface{}{
    		"statusCode": 200,
    		"headers":    map[string]string{"Content-Type": "application/json"},
    		"body":       messageString,
    	}, nil
    }
    
    func main() {
    	lambda.Start(HandleRequest)
    }
    
    

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
    
    

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from a DynamoDB stream. The function retrieves the DynamoDB payload and logs the record contents.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda) repository. 

Consuming a DynamoDB event with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"github.com/aws/aws-lambda-go/lambda"
    	"github.com/aws/aws-lambda-go/events"
    	"fmt"
    )
    
    func HandleRequest(ctx context.Context, event events.DynamoDBEvent) (*string, error) {
    	if len(event.Records) == 0 {
    		return nil, fmt.Errorf("received empty event")
    	}
    
    	for _, record := range event.Records {
    	 	LogDynamoDBRecord(record)
    	}
    
    	message := fmt.Sprintf("Records processed: %d", len(event.Records))
    	return &message, nil
    }
    
    func main() {
    	lambda.Start(HandleRequest)
    }
    
    func LogDynamoDBRecord(record events.DynamoDBEventRecord){
    	fmt.Println(record.EventID)
    	fmt.Println(record.EventName)
    	fmt.Printf("%+v\n", record.Change)
    }
    

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
    

The following code example shows how to implement a Lambda function that receives an event triggered by uploading an object to an S3 bucket. The function retrieves the S3 bucket name and object key from the event parameter and calls the Amazon S3 API to retrieve and log the content type of the object.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 

Consuming an S3 event with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    )
    
    func handler(ctx context.Context, s3Event events.S3Event) error {
    	sdkConfig, err := config.LoadDefaultConfig(ctx)
    	if err != nil {
    		log.Printf("failed to load default config: %s", err)
    		return err
    	}
    	s3Client := s3.NewFromConfig(sdkConfig)
    
    	for _, record := range s3Event.Records {
    		bucket := record.S3.Bucket.Name
    		key := record.S3.Object.URLDecodedKey
    		headOutput, err := s3Client.HeadObject(ctx, &s3.HeadObjectInput{
    			Bucket: &bucket,
    			Key:    &key,
    		})
    		if err != nil {
    			log.Printf("error getting head of object %s/%s: %s", bucket, key, err)
    			return err
    		}
    		log.Printf("successfully retrieved %s/%s of type %s", bucket, key, *headOutput.ContentType)
    	}
    
    	return nil
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    

The following code example shows how to implement a Lambda function that receives an event triggered by receiving messages from an SNS topic. The function retrieves the messages from the event parameter and logs the content of each message.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-sns-to-lambda) repository. 

Consuming an SNS event with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    func handler(ctx context.Context, snsEvent events.SNSEvent) {
    	for _, record := range snsEvent.Records {
    		processMessage(record)
    	}
    	fmt.Println("done")
    }
    
    func processMessage(record events.SNSEventRecord) {
    	message := record.SNS.Message
    	fmt.Printf("Processed message: %s\n", message)
    	// TODO: Process your record here
    }
    
    func main() {
    	lambda.Start(handler)
    }
    
    

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
    
    

The following code example shows how to implement partial batch response for Lambda functions that receive events from a DynamoDB stream. The function reports the batch item failures in the response, signaling to Lambda to retry those messages later.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 

Reporting DynamoDB batch item failures with Lambda using Go.
    
    
    // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
    // SPDX-License-Identifier: Apache-2.0
    package main
    
    import (
    	"context"
    	"github.com/aws/aws-lambda-go/events"
    	"github.com/aws/aws-lambda-go/lambda"
    )
    
    type BatchItemFailure struct {
    	ItemIdentifier string `json:"ItemIdentifier"`
    }
    
    type BatchResult struct {
    	BatchItemFailures []BatchItemFailure `json:"BatchItemFailures"`
    }
    
    func HandleRequest(ctx context.Context, event events.DynamoDBEvent) (*BatchResult, error) {
    	var batchItemFailures []BatchItemFailure
    	curRecordSequenceNumber := ""
    
    	for _, record := range event.Records {
    		// Process your record
    		curRecordSequenceNumber = record.Change.SequenceNumber
    	}
    
    	if curRecordSequenceNumber != "" {
    		batchItemFailures = append(batchItemFailures, BatchItemFailure{ItemIdentifier: curRecordSequenceNumber})
    	}
    	
    	batchResult := BatchResult{
    		BatchItemFailures: batchItemFailures,
    	}
    
    	return &batchResult, nil
    }
    
    func main() {
    	lambda.Start(HandleRequest)
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
    
    

## AWS community contributions

The following code example shows how to build and test a serverless application using API Gateway with Lambda and DynamoDB

**SDK for Go V2**
    

Shows how to build and test a serverless application that consists of an API Gateway with Lambda and DynamoDB using the Go SDK. 

For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/aws-samples/serverless-go-demo). 

###### Services used in this example

  * API Gateway

  * DynamoDB

  * Lambda




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Kinesis

Amazon MSK

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
