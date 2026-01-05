# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_iam_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_iam_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

BasicsActions

# IAM examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with IAM.

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using IAM.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    )
    
    // main uses the AWS SDK for Go (v2) to create an AWS Identity and Access Management (IAM)
    // client and list up to 10 policies in your account.
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
    	iamClient := iam.NewFromConfig(sdkConfig)
    	const maxPols = 10
    	fmt.Printf("Let's list up to %v policies for your account.\n", maxPols)
    	result, err := iamClient.ListPolicies(ctx, &iam.ListPoliciesInput{
    		MaxItems: aws.Int32(maxPols),
    	})
    	if err != nil {
    		fmt.Printf("Couldn't list policies for your account. Here's why: %v\n", err)
    		return
    	}
    	if len(result.Policies) == 0 {
    		fmt.Println("You don't have any policies!")
    	} else {
    		for _, policy := range result.Policies {
    			fmt.Printf("\t%v\n", *policy.PolicyName)
    		}
    	}
    }
    
    
    

  * For API details, see [ListPolicies](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListPolicies) in _AWS SDK for Go API Reference_. 




###### Topics

  * Basics

  * Actions




## Basics

The following code example shows how to create a user and assume a role. 

###### Warning

To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

  * Create a user with no permissions.

  * Create a role that grants permission to list Amazon S3 buckets for the account.

  * Add a policy to let the user assume the role.

  * Assume the role and list S3 buckets using temporary credentials, then clean up resources.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 

Run an interactive scenario at a command prompt.
    
    
    import (
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"math/rand"
    	"strings"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/credentials"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/aws-sdk-go-v2/service/s3"
    	"github.com/aws/aws-sdk-go-v2/service/sts"
    	"github.com/aws/smithy-go"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/iam/actions"
    )
    
    // AssumeRoleScenario shows you how to use the AWS Identity and Access Management (IAM)
    // service to perform the following actions:
    //
    //  1. Create a user who has no permissions.
    //  2. Create a role that grants permission to list Amazon Simple Storage Service
    //     (Amazon S3) buckets for the account.
    //  3. Add a policy to let the user assume the role.
    //  4. Try and fail to list buckets without permissions.
    //  5. Assume the role and list S3 buckets using temporary credentials.
    //  6. Delete the policy, role, and user.
    type AssumeRoleScenario struct {
    	sdkConfig      aws.Config
    	accountWrapper actions.AccountWrapper
    	policyWrapper  actions.PolicyWrapper
    	roleWrapper    actions.RoleWrapper
    	userWrapper    actions.UserWrapper
    	questioner     demotools.IQuestioner
    	helper         IScenarioHelper
    	isTestRun      bool
    }
    
    // NewAssumeRoleScenario constructs an AssumeRoleScenario instance from a configuration.
    // It uses the specified config to get an IAM client and create wrappers for the actions
    // used in the scenario.
    func NewAssumeRoleScenario(sdkConfig aws.Config, questioner demotools.IQuestioner,
    	helper IScenarioHelper) AssumeRoleScenario {
    	iamClient := iam.NewFromConfig(sdkConfig)
    	return AssumeRoleScenario{
    		sdkConfig:      sdkConfig,
    		accountWrapper: actions.AccountWrapper{IamClient: iamClient},
    		policyWrapper:  actions.PolicyWrapper{IamClient: iamClient},
    		roleWrapper:    actions.RoleWrapper{IamClient: iamClient},
    		userWrapper:    actions.UserWrapper{IamClient: iamClient},
    		questioner:     questioner,
    		helper:         helper,
    	}
    }
    
    // addTestOptions appends the API options specified in the original configuration to
    // another configuration. This is used to attach the middleware stubber to clients
    // that are constructed during the scenario, which is needed for unit testing.
    func (scenario AssumeRoleScenario) addTestOptions(scenarioConfig *aws.Config) {
    	if scenario.isTestRun {
    		scenarioConfig.APIOptions = append(scenarioConfig.APIOptions, scenario.sdkConfig.APIOptions...)
    	}
    }
    
    // Run runs the interactive scenario.
    func (scenario AssumeRoleScenario) Run(ctx context.Context) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Printf("Something went wrong with the demo.\n")
    			log.Println(r)
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the AWS Identity and Access Management (IAM) assume role demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	user := scenario.CreateUser(ctx)
    	accessKey := scenario.CreateAccessKey(ctx, user)
    	role := scenario.CreateRoleAndPolicies(ctx, user)
    	noPermsConfig := scenario.ListBucketsWithoutPermissions(ctx, accessKey)
    	scenario.ListBucketsWithAssumedRole(ctx, noPermsConfig, role)
    	scenario.Cleanup(ctx, user, role)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // CreateUser creates a new IAM user. This user has no permissions.
    func (scenario AssumeRoleScenario) CreateUser(ctx context.Context) *types.User {
    	log.Println("Let's create an example user with no permissions.")
    	userName := scenario.questioner.Ask("Enter a name for the example user:", demotools.NotEmpty{})
    	user, err := scenario.userWrapper.GetUser(ctx, userName)
    	if err != nil {
    		panic(err)
    	}
    	if user == nil {
    		user, err = scenario.userWrapper.CreateUser(ctx, userName)
    		if err != nil {
    			panic(err)
    		}
    		log.Printf("Created user %v.\n", *user.UserName)
    	} else {
    		log.Printf("User %v already exists.\n", *user.UserName)
    	}
    	log.Println(strings.Repeat("-", 88))
    	return user
    }
    
    // CreateAccessKey creates an access key for the user.
    func (scenario AssumeRoleScenario) CreateAccessKey(ctx context.Context, user *types.User) *types.AccessKey {
    	accessKey, err := scenario.userWrapper.CreateAccessKeyPair(ctx, *user.UserName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Created access key %v for your user.", *accessKey.AccessKeyId)
    	log.Println("Waiting a few seconds for your user to be ready...")
    	scenario.helper.Pause(10)
    	log.Println(strings.Repeat("-", 88))
    	return accessKey
    }
    
    // CreateRoleAndPolicies creates a policy that grants permission to list S3 buckets for
    // the current account and attaches the policy to a newly created role. It also adds an
    // inline policy to the specified user that grants the user permission to assume the role.
    func (scenario AssumeRoleScenario) CreateRoleAndPolicies(ctx context.Context, user *types.User) *types.Role {
    	log.Println("Let's create a role and policy that grant permission to list S3 buckets.")
    	scenario.questioner.Ask("Press Enter when you're ready.")
    	listBucketsRole, err := scenario.roleWrapper.CreateRole(ctx, scenario.helper.GetName(), *user.Arn)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Created role %v.\n", *listBucketsRole.RoleName)
    	listBucketsPolicy, err := scenario.policyWrapper.CreatePolicy(
    		ctx, scenario.helper.GetName(), []string{"s3:ListAllMyBuckets"}, "arn:aws:s3:::*")
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Created policy %v.\n", *listBucketsPolicy.PolicyName)
    	err = scenario.roleWrapper.AttachRolePolicy(ctx, *listBucketsPolicy.Arn, *listBucketsRole.RoleName)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Attached policy %v to role %v.\n", *listBucketsPolicy.PolicyName,
    		*listBucketsRole.RoleName)
    	err = scenario.userWrapper.CreateUserPolicy(ctx, *user.UserName, scenario.helper.GetName(),
    		[]string{"sts:AssumeRole"}, *listBucketsRole.Arn)
    	if err != nil {
    		panic(err)
    	}
    	log.Printf("Created an inline policy for user %v that lets the user assume the role.\n",
    		*user.UserName)
    	log.Println("Let's give AWS a few seconds to propagate these new resources and connections...")
    	scenario.helper.Pause(10)
    	log.Println(strings.Repeat("-", 88))
    	return listBucketsRole
    }
    
    // ListBucketsWithoutPermissions creates an Amazon S3 client from the user's access key
    // credentials and tries to list buckets for the account. Because the user does not have
    // permission to perform this action, the action fails.
    func (scenario AssumeRoleScenario) ListBucketsWithoutPermissions(ctx context.Context, accessKey *types.AccessKey) *aws.Config {
    	log.Println("Let's try to list buckets without permissions. This should return an AccessDenied error.")
    	scenario.questioner.Ask("Press Enter when you're ready.")
    	noPermsConfig, err := config.LoadDefaultConfig(ctx,
    		config.WithCredentialsProvider(credentials.NewStaticCredentialsProvider(
    			*accessKey.AccessKeyId, *accessKey.SecretAccessKey, ""),
    		))
    	if err != nil {
    		panic(err)
    	}
    
    	// Add test options if this is a test run. This is needed only for testing purposes.
    	scenario.addTestOptions(&noPermsConfig)
    
    	s3Client := s3.NewFromConfig(noPermsConfig)
    	_, err = s3Client.ListBuckets(ctx, &s3.ListBucketsInput{})
    	if err != nil {
    		// The SDK for Go does not model the AccessDenied error, so check ErrorCode directly.
    		var ae smithy.APIError
    		if errors.As(err, &ae) {
    			switch ae.ErrorCode() {
    			case "AccessDenied":
    				log.Println("Got AccessDenied error, which is the expected result because\n" +
    					"the ListBuckets call was made without permissions.")
    			default:
    				log.Println("Expected AccessDenied, got something else.")
    				panic(err)
    			}
    		}
    	} else {
    		log.Println("Expected AccessDenied error when calling ListBuckets without permissions,\n" +
    			"but the call succeeded. Continuing the example anyway...")
    	}
    	log.Println(strings.Repeat("-", 88))
    	return &noPermsConfig
    }
    
    // ListBucketsWithAssumedRole performs the following actions:
    //
    //  1. Creates an AWS Security Token Service (AWS STS) client from the config created from
    //     the user's access key credentials.
    //  2. Gets temporary credentials by assuming the role that grants permission to list the
    //     buckets.
    //  3. Creates an Amazon S3 client from the temporary credentials.
    //  4. Lists buckets for the account. Because the temporary credentials are generated by
    //     assuming the role that grants permission, the action succeeds.
    func (scenario AssumeRoleScenario) ListBucketsWithAssumedRole(ctx context.Context, noPermsConfig *aws.Config, role *types.Role) {
    	log.Println("Let's assume the role that grants permission to list buckets and try again.")
    	scenario.questioner.Ask("Press Enter when you're ready.")
    	stsClient := sts.NewFromConfig(*noPermsConfig)
    	tempCredentials, err := stsClient.AssumeRole(ctx, &sts.AssumeRoleInput{
    		RoleArn:         role.Arn,
    		RoleSessionName: aws.String("AssumeRoleExampleSession"),
    		DurationSeconds: aws.Int32(900),
    	})
    	if err != nil {
    		log.Printf("Couldn't assume role %v.\n", *role.RoleName)
    		panic(err)
    	}
    	log.Printf("Assumed role %v, got temporary credentials.\n", *role.RoleName)
    	assumeRoleConfig, err := config.LoadDefaultConfig(ctx,
    		config.WithCredentialsProvider(credentials.NewStaticCredentialsProvider(
    			*tempCredentials.Credentials.AccessKeyId,
    			*tempCredentials.Credentials.SecretAccessKey,
    			*tempCredentials.Credentials.SessionToken),
    		),
    	)
    	if err != nil {
    		panic(err)
    	}
    
    	// Add test options if this is a test run. This is needed only for testing purposes.
    	scenario.addTestOptions(&assumeRoleConfig)
    
    	s3Client := s3.NewFromConfig(assumeRoleConfig)
    	result, err := s3Client.ListBuckets(ctx, &s3.ListBucketsInput{})
    	if err != nil {
    		log.Println("Couldn't list buckets with assumed role credentials.")
    		panic(err)
    	}
    	log.Println("Successfully called ListBuckets with assumed role credentials, \n" +
    		"here are some of them:")
    	for i := 0; i < len(result.Buckets) && i < 5; i++ {
    		log.Printf("\t%v\n", *result.Buckets[i].Name)
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    // Cleanup deletes all resources created for the scenario.
    func (scenario AssumeRoleScenario) Cleanup(ctx context.Context, user *types.User, role *types.Role) {
    	if scenario.questioner.AskBool(
    		"Do you want to delete the resources created for this example? (y/n)", "y",
    	) {
    		policies, err := scenario.roleWrapper.ListAttachedRolePolicies(ctx, *role.RoleName)
    		if err != nil {
    			panic(err)
    		}
    		for _, policy := range policies {
    			err = scenario.roleWrapper.DetachRolePolicy(ctx, *role.RoleName, *policy.PolicyArn)
    			if err != nil {
    				panic(err)
    			}
    			err = scenario.policyWrapper.DeletePolicy(ctx, *policy.PolicyArn)
    			if err != nil {
    				panic(err)
    			}
    			log.Printf("Detached policy %v from role %v and deleted the policy.\n",
    				*policy.PolicyName, *role.RoleName)
    		}
    		err = scenario.roleWrapper.DeleteRole(ctx, *role.RoleName)
    		if err != nil {
    			panic(err)
    		}
    		log.Printf("Deleted role %v.\n", *role.RoleName)
    
    		userPols, err := scenario.userWrapper.ListUserPolicies(ctx, *user.UserName)
    		if err != nil {
    			panic(err)
    		}
    		for _, userPol := range userPols {
    			err = scenario.userWrapper.DeleteUserPolicy(ctx, *user.UserName, userPol)
    			if err != nil {
    				panic(err)
    			}
    			log.Printf("Deleted policy %v from user %v.\n", userPol, *user.UserName)
    		}
    		keys, err := scenario.userWrapper.ListAccessKeys(ctx, *user.UserName)
    		if err != nil {
    			panic(err)
    		}
    		for _, key := range keys {
    			err = scenario.userWrapper.DeleteAccessKey(ctx, *user.UserName, *key.AccessKeyId)
    			if err != nil {
    				panic(err)
    			}
    			log.Printf("Deleted access key %v from user %v.\n", *key.AccessKeyId, *user.UserName)
    		}
    		err = scenario.userWrapper.DeleteUser(ctx, *user.UserName)
    		if err != nil {
    			panic(err)
    		}
    		log.Printf("Deleted user %v.\n", *user.UserName)
    		log.Println(strings.Repeat("-", 88))
    	}
    
    }
    
    // IScenarioHelper abstracts input and wait functions from a scenario so that they
    // can be mocked for unit testing.
    type IScenarioHelper interface {
    	GetName() string
    	Pause(secs int)
    }
    
    const rMax = 100000
    
    type ScenarioHelper struct {
    	Prefix string
    	Random *rand.Rand
    }
    
    // GetName returns a unique name formed of a prefix and a random number.
    func (helper *ScenarioHelper) GetName() string {
    	return fmt.Sprintf("%v%v", helper.Prefix, helper.Random.Intn(rMax))
    }
    
    // Pause waits for the specified number of seconds.
    func (helper ScenarioHelper) Pause(secs int) {
    	time.Sleep(time.Duration(secs) * time.Second)
    }
    
    
    

Define a struct that wraps account actions.
    
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // AccountWrapper encapsulates AWS Identity and Access Management (IAM) account actions
    // used in the examples.
    // It contains an IAM service client that is used to perform account actions.
    type AccountWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // GetAccountPasswordPolicy gets the account password policy for the current account.
    // If no policy has been set, a NoSuchEntityException is error is returned.
    func (wrapper AccountWrapper) GetAccountPasswordPolicy(ctx context.Context) (*types.PasswordPolicy, error) {
    	var pwPolicy *types.PasswordPolicy
    	result, err := wrapper.IamClient.GetAccountPasswordPolicy(ctx,
    		&iam.GetAccountPasswordPolicyInput{})
    	if err != nil {
    		log.Printf("Couldn't get account password policy. Here's why: %v\n", err)
    	} else {
    		pwPolicy = result.PasswordPolicy
    	}
    	return pwPolicy, err
    }
    
    
    
    // ListSAMLProviders gets the SAML providers for the account.
    func (wrapper AccountWrapper) ListSAMLProviders(ctx context.Context) ([]types.SAMLProviderListEntry, error) {
    	var providers []types.SAMLProviderListEntry
    	result, err := wrapper.IamClient.ListSAMLProviders(ctx, &iam.ListSAMLProvidersInput{})
    	if err != nil {
    		log.Printf("Couldn't list SAML providers. Here's why: %v\n", err)
    	} else {
    		providers = result.SAMLProviderList
    	}
    	return providers, err
    }
    
    
    

Define a struct that wraps policy actions.
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // PolicyWrapper encapsulates AWS Identity and Access Management (IAM) policy actions
    // used in the examples.
    // It contains an IAM service client that is used to perform policy actions.
    type PolicyWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListPolicies gets up to maxPolicies policies.
    func (wrapper PolicyWrapper) ListPolicies(ctx context.Context, maxPolicies int32) ([]types.Policy, error) {
    	var policies []types.Policy
    	result, err := wrapper.IamClient.ListPolicies(ctx, &iam.ListPoliciesInput{
    		MaxItems: aws.Int32(maxPolicies),
    	})
    	if err != nil {
    		log.Printf("Couldn't list policies. Here's why: %v\n", err)
    	} else {
    		policies = result.Policies
    	}
    	return policies, err
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
    	Action    []string
    	Principal map[string]string `json:",omitempty"`
    	Resource  *string           `json:",omitempty"`
    }
    
    // CreatePolicy creates a policy that grants a list of actions to the specified resource.
    // PolicyDocument shows how to work with a policy document as a data structure and
    // serialize it to JSON by using Go's JSON marshaler.
    func (wrapper PolicyWrapper) CreatePolicy(ctx context.Context, policyName string, actions []string,
    	resourceArn string) (*types.Policy, error) {
    	var policy *types.Policy
    	policyDoc := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:   "Allow",
    			Action:   actions,
    			Resource: aws.String(resourceArn),
    		}},
    	}
    	policyBytes, err := json.Marshal(policyDoc)
    	if err != nil {
    		log.Printf("Couldn't create policy document for %v. Here's why: %v\n", resourceArn, err)
    		return nil, err
    	}
    	result, err := wrapper.IamClient.CreatePolicy(ctx, &iam.CreatePolicyInput{
    		PolicyDocument: aws.String(string(policyBytes)),
    		PolicyName:     aws.String(policyName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create policy %v. Here's why: %v\n", policyName, err)
    	} else {
    		policy = result.Policy
    	}
    	return policy, err
    }
    
    
    
    // GetPolicy gets data about a policy.
    func (wrapper PolicyWrapper) GetPolicy(ctx context.Context, policyArn string) (*types.Policy, error) {
    	var policy *types.Policy
    	result, err := wrapper.IamClient.GetPolicy(ctx, &iam.GetPolicyInput{
    		PolicyArn: aws.String(policyArn),
    	})
    	if err != nil {
    		log.Printf("Couldn't get policy %v. Here's why: %v\n", policyArn, err)
    	} else {
    		policy = result.Policy
    	}
    	return policy, err
    }
    
    
    
    // DeletePolicy deletes a policy.
    func (wrapper PolicyWrapper) DeletePolicy(ctx context.Context, policyArn string) error {
    	_, err := wrapper.IamClient.DeletePolicy(ctx, &iam.DeletePolicyInput{
    		PolicyArn: aws.String(policyArn),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete policy %v. Here's why: %v\n", policyArn, err)
    	}
    	return err
    }
    
    
    

Define a struct that wraps role actions.
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListRoles gets up to maxRoles roles.
    func (wrapper RoleWrapper) ListRoles(ctx context.Context, maxRoles int32) ([]types.Role, error) {
    	var roles []types.Role
    	result, err := wrapper.IamClient.ListRoles(ctx,
    		&iam.ListRolesInput{MaxItems: aws.Int32(maxRoles)},
    	)
    	if err != nil {
    		log.Printf("Couldn't list roles. Here's why: %v\n", err)
    	} else {
    		roles = result.Roles
    	}
    	return roles, err
    }
    
    
    
    // CreateRole creates a role that trusts a specified user. The trusted user can assume
    // the role to acquire its permissions.
    // PolicyDocument shows how to work with a policy document as a data structure and
    // serialize it to JSON by using Go's JSON marshaler.
    func (wrapper RoleWrapper) CreateRole(ctx context.Context, roleName string, trustedUserArn string) (*types.Role, error) {
    	var role *types.Role
    	trustPolicy := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:    "Allow",
    			Principal: map[string]string{"AWS": trustedUserArn},
    			Action:    []string{"sts:AssumeRole"},
    		}},
    	}
    	policyBytes, err := json.Marshal(trustPolicy)
    	if err != nil {
    		log.Printf("Couldn't create trust policy for %v. Here's why: %v\n", trustedUserArn, err)
    		return nil, err
    	}
    	result, err := wrapper.IamClient.CreateRole(ctx, &iam.CreateRoleInput{
    		AssumeRolePolicyDocument: aws.String(string(policyBytes)),
    		RoleName:                 aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create role %v. Here's why: %v\n", roleName, err)
    	} else {
    		role = result.Role
    	}
    	return role, err
    }
    
    
    
    // GetRole gets data about a role.
    func (wrapper RoleWrapper) GetRole(ctx context.Context, roleName string) (*types.Role, error) {
    	var role *types.Role
    	result, err := wrapper.IamClient.GetRole(ctx,
    		&iam.GetRoleInput{RoleName: aws.String(roleName)})
    	if err != nil {
    		log.Printf("Couldn't get role %v. Here's why: %v\n", roleName, err)
    	} else {
    		role = result.Role
    	}
    	return role, err
    }
    
    
    
    // CreateServiceLinkedRole creates a service-linked role that is owned by the specified service.
    func (wrapper RoleWrapper) CreateServiceLinkedRole(ctx context.Context, serviceName string, description string) (
    	*types.Role, error) {
    	var role *types.Role
    	result, err := wrapper.IamClient.CreateServiceLinkedRole(ctx, &iam.CreateServiceLinkedRoleInput{
    		AWSServiceName: aws.String(serviceName),
    		Description:    aws.String(description),
    	})
    	if err != nil {
    		log.Printf("Couldn't create service-linked role %v. Here's why: %v\n", serviceName, err)
    	} else {
    		role = result.Role
    	}
    	return role, err
    }
    
    
    
    // DeleteServiceLinkedRole deletes a service-linked role.
    func (wrapper RoleWrapper) DeleteServiceLinkedRole(ctx context.Context, roleName string) error {
    	_, err := wrapper.IamClient.DeleteServiceLinkedRole(ctx, &iam.DeleteServiceLinkedRoleInput{
    		RoleName: aws.String(roleName)},
    	)
    	if err != nil {
    		log.Printf("Couldn't delete service-linked role %v. Here's why: %v\n", roleName, err)
    	}
    	return err
    }
    
    
    
    // AttachRolePolicy attaches a policy to a role.
    func (wrapper RoleWrapper) AttachRolePolicy(ctx context.Context, policyArn string, roleName string) error {
    	_, err := wrapper.IamClient.AttachRolePolicy(ctx, &iam.AttachRolePolicyInput{
    		PolicyArn: aws.String(policyArn),
    		RoleName:  aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't attach policy %v to role %v. Here's why: %v\n", policyArn, roleName, err)
    	}
    	return err
    }
    
    
    
    // ListAttachedRolePolicies lists the policies that are attached to the specified role.
    func (wrapper RoleWrapper) ListAttachedRolePolicies(ctx context.Context, roleName string) ([]types.AttachedPolicy, error) {
    	var policies []types.AttachedPolicy
    	result, err := wrapper.IamClient.ListAttachedRolePolicies(ctx, &iam.ListAttachedRolePoliciesInput{
    		RoleName: aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list attached policies for role %v. Here's why: %v\n", roleName, err)
    	} else {
    		policies = result.AttachedPolicies
    	}
    	return policies, err
    }
    
    
    
    // DetachRolePolicy detaches a policy from a role.
    func (wrapper RoleWrapper) DetachRolePolicy(ctx context.Context, roleName string, policyArn string) error {
    	_, err := wrapper.IamClient.DetachRolePolicy(ctx, &iam.DetachRolePolicyInput{
    		PolicyArn: aws.String(policyArn),
    		RoleName:  aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't detach policy from role %v. Here's why: %v\n", roleName, err)
    	}
    	return err
    }
    
    
    
    // ListRolePolicies lists the inline policies for a role.
    func (wrapper RoleWrapper) ListRolePolicies(ctx context.Context, roleName string) ([]string, error) {
    	var policies []string
    	result, err := wrapper.IamClient.ListRolePolicies(ctx, &iam.ListRolePoliciesInput{
    		RoleName: aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list policies for role %v. Here's why: %v\n", roleName, err)
    	} else {
    		policies = result.PolicyNames
    	}
    	return policies, err
    }
    
    
    
    // DeleteRole deletes a role. All attached policies must be detached before a
    // role can be deleted.
    func (wrapper RoleWrapper) DeleteRole(ctx context.Context, roleName string) error {
    	_, err := wrapper.IamClient.DeleteRole(ctx, &iam.DeleteRoleInput{
    		RoleName: aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete role %v. Here's why: %v\n", roleName, err)
    	}
    	return err
    }
    
    
    
    

Define a struct that wraps user actions.
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListUsers gets up to maxUsers number of users.
    func (wrapper UserWrapper) ListUsers(ctx context.Context, maxUsers int32) ([]types.User, error) {
    	var users []types.User
    	result, err := wrapper.IamClient.ListUsers(ctx, &iam.ListUsersInput{
    		MaxItems: aws.Int32(maxUsers),
    	})
    	if err != nil {
    		log.Printf("Couldn't list users. Here's why: %v\n", err)
    	} else {
    		users = result.Users
    	}
    	return users, err
    }
    
    
    
    // GetUser gets data about a user.
    func (wrapper UserWrapper) GetUser(ctx context.Context, userName string) (*types.User, error) {
    	var user *types.User
    	result, err := wrapper.IamClient.GetUser(ctx, &iam.GetUserInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		var apiError smithy.APIError
    		if errors.As(err, &apiError) {
    			switch apiError.(type) {
    			case *types.NoSuchEntityException:
    				log.Printf("User %v does not exist.\n", userName)
    				err = nil
    			default:
    				log.Printf("Couldn't get user %v. Here's why: %v\n", userName, err)
    			}
    		}
    	} else {
    		user = result.User
    	}
    	return user, err
    }
    
    
    
    // CreateUser creates a new user with the specified name.
    func (wrapper UserWrapper) CreateUser(ctx context.Context, userName string) (*types.User, error) {
    	var user *types.User
    	result, err := wrapper.IamClient.CreateUser(ctx, &iam.CreateUserInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create user %v. Here's why: %v\n", userName, err)
    	} else {
    		user = result.User
    	}
    	return user, err
    }
    
    
    
    // CreateUserPolicy adds an inline policy to a user. This example creates a policy that
    // grants a list of actions on a specified role.
    // PolicyDocument shows how to work with a policy document as a data structure and
    // serialize it to JSON by using Go's JSON marshaler.
    func (wrapper UserWrapper) CreateUserPolicy(ctx context.Context, userName string, policyName string, actions []string,
    	roleArn string) error {
    	policyDoc := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:   "Allow",
    			Action:   actions,
    			Resource: aws.String(roleArn),
    		}},
    	}
    	policyBytes, err := json.Marshal(policyDoc)
    	if err != nil {
    		log.Printf("Couldn't create policy document for %v. Here's why: %v\n", roleArn, err)
    		return err
    	}
    	_, err = wrapper.IamClient.PutUserPolicy(ctx, &iam.PutUserPolicyInput{
    		PolicyDocument: aws.String(string(policyBytes)),
    		PolicyName:     aws.String(policyName),
    		UserName:       aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create policy for user %v. Here's why: %v\n", userName, err)
    	}
    	return err
    }
    
    
    
    // ListUserPolicies lists the inline policies for the specified user.
    func (wrapper UserWrapper) ListUserPolicies(ctx context.Context, userName string) ([]string, error) {
    	var policies []string
    	result, err := wrapper.IamClient.ListUserPolicies(ctx, &iam.ListUserPoliciesInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list policies for user %v. Here's why: %v\n", userName, err)
    	} else {
    		policies = result.PolicyNames
    	}
    	return policies, err
    }
    
    
    
    // DeleteUserPolicy deletes an inline policy from a user.
    func (wrapper UserWrapper) DeleteUserPolicy(ctx context.Context, userName string, policyName string) error {
    	_, err := wrapper.IamClient.DeleteUserPolicy(ctx, &iam.DeleteUserPolicyInput{
    		PolicyName: aws.String(policyName),
    		UserName:   aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete policy from user %v. Here's why: %v\n", userName, err)
    	}
    	return err
    }
    
    
    
    // DeleteUser deletes a user.
    func (wrapper UserWrapper) DeleteUser(ctx context.Context, userName string) error {
    	_, err := wrapper.IamClient.DeleteUser(ctx, &iam.DeleteUserInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete user %v. Here's why: %v\n", userName, err)
    	}
    	return err
    }
    
    
    
    // CreateAccessKeyPair creates an access key for a user. The returned access key contains
    // the ID and secret credentials needed to use the key.
    func (wrapper UserWrapper) CreateAccessKeyPair(ctx context.Context, userName string) (*types.AccessKey, error) {
    	var key *types.AccessKey
    	result, err := wrapper.IamClient.CreateAccessKey(ctx, &iam.CreateAccessKeyInput{
    		UserName: aws.String(userName)})
    	if err != nil {
    		log.Printf("Couldn't create access key pair for user %v. Here's why: %v\n", userName, err)
    	} else {
    		key = result.AccessKey
    	}
    	return key, err
    }
    
    
    
    // DeleteAccessKey deletes an access key from a user.
    func (wrapper UserWrapper) DeleteAccessKey(ctx context.Context, userName string, keyId string) error {
    	_, err := wrapper.IamClient.DeleteAccessKey(ctx, &iam.DeleteAccessKeyInput{
    		AccessKeyId: aws.String(keyId),
    		UserName:    aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete access key %v. Here's why: %v\n", keyId, err)
    	}
    	return err
    }
    
    
    
    // ListAccessKeys lists the access keys for the specified user.
    func (wrapper UserWrapper) ListAccessKeys(ctx context.Context, userName string) ([]types.AccessKeyMetadata, error) {
    	var keys []types.AccessKeyMetadata
    	result, err := wrapper.IamClient.ListAccessKeys(ctx, &iam.ListAccessKeysInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list access keys for user %v. Here's why: %v\n", userName, err)
    	} else {
    		keys = result.AccessKeyMetadata
    	}
    	return keys, err
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [AttachRolePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.AttachRolePolicy)

    * [CreateAccessKey](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateAccessKey)

    * [CreatePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreatePolicy)

    * [CreateRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateRole)

    * [CreateUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateUser)

    * [DeleteAccessKey](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteAccessKey)

    * [DeletePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeletePolicy)

    * [DeleteRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteRole)

    * [DeleteUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteUser)

    * [DeleteUserPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteUserPolicy)

    * [DetachRolePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DetachRolePolicy)

    * [PutUserPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.PutUserPolicy)




## Actions

The following code example shows how to use `AttachRolePolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // AttachRolePolicy attaches a policy to a role.
    func (wrapper RoleWrapper) AttachRolePolicy(ctx context.Context, policyArn string, roleName string) error {
    	_, err := wrapper.IamClient.AttachRolePolicy(ctx, &iam.AttachRolePolicyInput{
    		PolicyArn: aws.String(policyArn),
    		RoleName:  aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't attach policy %v to role %v. Here's why: %v\n", policyArn, roleName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [AttachRolePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.AttachRolePolicy) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateAccessKey`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // CreateAccessKeyPair creates an access key for a user. The returned access key contains
    // the ID and secret credentials needed to use the key.
    func (wrapper UserWrapper) CreateAccessKeyPair(ctx context.Context, userName string) (*types.AccessKey, error) {
    	var key *types.AccessKey
    	result, err := wrapper.IamClient.CreateAccessKey(ctx, &iam.CreateAccessKeyInput{
    		UserName: aws.String(userName)})
    	if err != nil {
    		log.Printf("Couldn't create access key pair for user %v. Here's why: %v\n", userName, err)
    	} else {
    		key = result.AccessKey
    	}
    	return key, err
    }
    
    
    

  * For API details, see [CreateAccessKey](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateAccessKey) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreatePolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // PolicyWrapper encapsulates AWS Identity and Access Management (IAM) policy actions
    // used in the examples.
    // It contains an IAM service client that is used to perform policy actions.
    type PolicyWrapper struct {
    	IamClient *iam.Client
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
    	Action    []string
    	Principal map[string]string `json:",omitempty"`
    	Resource  *string           `json:",omitempty"`
    }
    
    // CreatePolicy creates a policy that grants a list of actions to the specified resource.
    // PolicyDocument shows how to work with a policy document as a data structure and
    // serialize it to JSON by using Go's JSON marshaler.
    func (wrapper PolicyWrapper) CreatePolicy(ctx context.Context, policyName string, actions []string,
    	resourceArn string) (*types.Policy, error) {
    	var policy *types.Policy
    	policyDoc := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:   "Allow",
    			Action:   actions,
    			Resource: aws.String(resourceArn),
    		}},
    	}
    	policyBytes, err := json.Marshal(policyDoc)
    	if err != nil {
    		log.Printf("Couldn't create policy document for %v. Here's why: %v\n", resourceArn, err)
    		return nil, err
    	}
    	result, err := wrapper.IamClient.CreatePolicy(ctx, &iam.CreatePolicyInput{
    		PolicyDocument: aws.String(string(policyBytes)),
    		PolicyName:     aws.String(policyName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create policy %v. Here's why: %v\n", policyName, err)
    	} else {
    		policy = result.Policy
    	}
    	return policy, err
    }
    
    
    

  * For API details, see [CreatePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreatePolicy) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateRole`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // CreateRole creates a role that trusts a specified user. The trusted user can assume
    // the role to acquire its permissions.
    // PolicyDocument shows how to work with a policy document as a data structure and
    // serialize it to JSON by using Go's JSON marshaler.
    func (wrapper RoleWrapper) CreateRole(ctx context.Context, roleName string, trustedUserArn string) (*types.Role, error) {
    	var role *types.Role
    	trustPolicy := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:    "Allow",
    			Principal: map[string]string{"AWS": trustedUserArn},
    			Action:    []string{"sts:AssumeRole"},
    		}},
    	}
    	policyBytes, err := json.Marshal(trustPolicy)
    	if err != nil {
    		log.Printf("Couldn't create trust policy for %v. Here's why: %v\n", trustedUserArn, err)
    		return nil, err
    	}
    	result, err := wrapper.IamClient.CreateRole(ctx, &iam.CreateRoleInput{
    		AssumeRolePolicyDocument: aws.String(string(policyBytes)),
    		RoleName:                 aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create role %v. Here's why: %v\n", roleName, err)
    	} else {
    		role = result.Role
    	}
    	return role, err
    }
    
    
    

  * For API details, see [CreateRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateRole) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateServiceLinkedRole`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // CreateServiceLinkedRole creates a service-linked role that is owned by the specified service.
    func (wrapper RoleWrapper) CreateServiceLinkedRole(ctx context.Context, serviceName string, description string) (
    	*types.Role, error) {
    	var role *types.Role
    	result, err := wrapper.IamClient.CreateServiceLinkedRole(ctx, &iam.CreateServiceLinkedRoleInput{
    		AWSServiceName: aws.String(serviceName),
    		Description:    aws.String(description),
    	})
    	if err != nil {
    		log.Printf("Couldn't create service-linked role %v. Here's why: %v\n", serviceName, err)
    	} else {
    		role = result.Role
    	}
    	return role, err
    }
    
    
    

  * For API details, see [CreateServiceLinkedRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateServiceLinkedRole) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateUser`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // CreateUser creates a new user with the specified name.
    func (wrapper UserWrapper) CreateUser(ctx context.Context, userName string) (*types.User, error) {
    	var user *types.User
    	result, err := wrapper.IamClient.CreateUser(ctx, &iam.CreateUserInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create user %v. Here's why: %v\n", userName, err)
    	} else {
    		user = result.User
    	}
    	return user, err
    }
    
    
    

  * For API details, see [CreateUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.CreateUser) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteAccessKey`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // DeleteAccessKey deletes an access key from a user.
    func (wrapper UserWrapper) DeleteAccessKey(ctx context.Context, userName string, keyId string) error {
    	_, err := wrapper.IamClient.DeleteAccessKey(ctx, &iam.DeleteAccessKeyInput{
    		AccessKeyId: aws.String(keyId),
    		UserName:    aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete access key %v. Here's why: %v\n", keyId, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteAccessKey](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteAccessKey) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeletePolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // PolicyWrapper encapsulates AWS Identity and Access Management (IAM) policy actions
    // used in the examples.
    // It contains an IAM service client that is used to perform policy actions.
    type PolicyWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // DeletePolicy deletes a policy.
    func (wrapper PolicyWrapper) DeletePolicy(ctx context.Context, policyArn string) error {
    	_, err := wrapper.IamClient.DeletePolicy(ctx, &iam.DeletePolicyInput{
    		PolicyArn: aws.String(policyArn),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete policy %v. Here's why: %v\n", policyArn, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeletePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeletePolicy) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteRole`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // DeleteRole deletes a role. All attached policies must be detached before a
    // role can be deleted.
    func (wrapper RoleWrapper) DeleteRole(ctx context.Context, roleName string) error {
    	_, err := wrapper.IamClient.DeleteRole(ctx, &iam.DeleteRoleInput{
    		RoleName: aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete role %v. Here's why: %v\n", roleName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteRole) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteServiceLinkedRole`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // DeleteServiceLinkedRole deletes a service-linked role.
    func (wrapper RoleWrapper) DeleteServiceLinkedRole(ctx context.Context, roleName string) error {
    	_, err := wrapper.IamClient.DeleteServiceLinkedRole(ctx, &iam.DeleteServiceLinkedRoleInput{
    		RoleName: aws.String(roleName)},
    	)
    	if err != nil {
    		log.Printf("Couldn't delete service-linked role %v. Here's why: %v\n", roleName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteServiceLinkedRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteServiceLinkedRole) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteUser`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // DeleteUser deletes a user.
    func (wrapper UserWrapper) DeleteUser(ctx context.Context, userName string) error {
    	_, err := wrapper.IamClient.DeleteUser(ctx, &iam.DeleteUserInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete user %v. Here's why: %v\n", userName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteUser) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteUserPolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // DeleteUserPolicy deletes an inline policy from a user.
    func (wrapper UserWrapper) DeleteUserPolicy(ctx context.Context, userName string, policyName string) error {
    	_, err := wrapper.IamClient.DeleteUserPolicy(ctx, &iam.DeleteUserPolicyInput{
    		PolicyName: aws.String(policyName),
    		UserName:   aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete policy from user %v. Here's why: %v\n", userName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteUserPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteUserPolicy) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DetachRolePolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // DetachRolePolicy detaches a policy from a role.
    func (wrapper RoleWrapper) DetachRolePolicy(ctx context.Context, roleName string, policyArn string) error {
    	_, err := wrapper.IamClient.DetachRolePolicy(ctx, &iam.DetachRolePolicyInput{
    		PolicyArn: aws.String(policyArn),
    		RoleName:  aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't detach policy from role %v. Here's why: %v\n", roleName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DetachRolePolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DetachRolePolicy) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetAccountPasswordPolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // AccountWrapper encapsulates AWS Identity and Access Management (IAM) account actions
    // used in the examples.
    // It contains an IAM service client that is used to perform account actions.
    type AccountWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // GetAccountPasswordPolicy gets the account password policy for the current account.
    // If no policy has been set, a NoSuchEntityException is error is returned.
    func (wrapper AccountWrapper) GetAccountPasswordPolicy(ctx context.Context) (*types.PasswordPolicy, error) {
    	var pwPolicy *types.PasswordPolicy
    	result, err := wrapper.IamClient.GetAccountPasswordPolicy(ctx,
    		&iam.GetAccountPasswordPolicyInput{})
    	if err != nil {
    		log.Printf("Couldn't get account password policy. Here's why: %v\n", err)
    	} else {
    		pwPolicy = result.PasswordPolicy
    	}
    	return pwPolicy, err
    }
    
    
    

  * For API details, see [GetAccountPasswordPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.GetAccountPasswordPolicy) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetPolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // PolicyWrapper encapsulates AWS Identity and Access Management (IAM) policy actions
    // used in the examples.
    // It contains an IAM service client that is used to perform policy actions.
    type PolicyWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // GetPolicy gets data about a policy.
    func (wrapper PolicyWrapper) GetPolicy(ctx context.Context, policyArn string) (*types.Policy, error) {
    	var policy *types.Policy
    	result, err := wrapper.IamClient.GetPolicy(ctx, &iam.GetPolicyInput{
    		PolicyArn: aws.String(policyArn),
    	})
    	if err != nil {
    		log.Printf("Couldn't get policy %v. Here's why: %v\n", policyArn, err)
    	} else {
    		policy = result.Policy
    	}
    	return policy, err
    }
    
    
    

  * For API details, see [GetPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.GetPolicy) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetRole`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // GetRole gets data about a role.
    func (wrapper RoleWrapper) GetRole(ctx context.Context, roleName string) (*types.Role, error) {
    	var role *types.Role
    	result, err := wrapper.IamClient.GetRole(ctx,
    		&iam.GetRoleInput{RoleName: aws.String(roleName)})
    	if err != nil {
    		log.Printf("Couldn't get role %v. Here's why: %v\n", roleName, err)
    	} else {
    		role = result.Role
    	}
    	return role, err
    }
    
    
    

  * For API details, see [GetRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.GetRole) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetUser`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // GetUser gets data about a user.
    func (wrapper UserWrapper) GetUser(ctx context.Context, userName string) (*types.User, error) {
    	var user *types.User
    	result, err := wrapper.IamClient.GetUser(ctx, &iam.GetUserInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		var apiError smithy.APIError
    		if errors.As(err, &apiError) {
    			switch apiError.(type) {
    			case *types.NoSuchEntityException:
    				log.Printf("User %v does not exist.\n", userName)
    				err = nil
    			default:
    				log.Printf("Couldn't get user %v. Here's why: %v\n", userName, err)
    			}
    		}
    	} else {
    		user = result.User
    	}
    	return user, err
    }
    
    
    

  * For API details, see [GetUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.GetUser) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListAccessKeys`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListAccessKeys lists the access keys for the specified user.
    func (wrapper UserWrapper) ListAccessKeys(ctx context.Context, userName string) ([]types.AccessKeyMetadata, error) {
    	var keys []types.AccessKeyMetadata
    	result, err := wrapper.IamClient.ListAccessKeys(ctx, &iam.ListAccessKeysInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list access keys for user %v. Here's why: %v\n", userName, err)
    	} else {
    		keys = result.AccessKeyMetadata
    	}
    	return keys, err
    }
    
    
    

  * For API details, see [ListAccessKeys](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListAccessKeys) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListAttachedRolePolicies`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListAttachedRolePolicies lists the policies that are attached to the specified role.
    func (wrapper RoleWrapper) ListAttachedRolePolicies(ctx context.Context, roleName string) ([]types.AttachedPolicy, error) {
    	var policies []types.AttachedPolicy
    	result, err := wrapper.IamClient.ListAttachedRolePolicies(ctx, &iam.ListAttachedRolePoliciesInput{
    		RoleName: aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list attached policies for role %v. Here's why: %v\n", roleName, err)
    	} else {
    		policies = result.AttachedPolicies
    	}
    	return policies, err
    }
    
    
    

  * For API details, see [ListAttachedRolePolicies](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListAttachedRolePolicies) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListGroups`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // GroupWrapper encapsulates AWS Identity and Access Management (IAM) group actions
    // used in the examples.
    // It contains an IAM service client that is used to perform group actions.
    type GroupWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListGroups lists up to maxGroups number of groups.
    func (wrapper GroupWrapper) ListGroups(ctx context.Context, maxGroups int32) ([]types.Group, error) {
    	var groups []types.Group
    	result, err := wrapper.IamClient.ListGroups(ctx, &iam.ListGroupsInput{
    		MaxItems: aws.Int32(maxGroups),
    	})
    	if err != nil {
    		log.Printf("Couldn't list groups. Here's why: %v\n", err)
    	} else {
    		groups = result.Groups
    	}
    	return groups, err
    }
    
    
    

  * For API details, see [ListGroups](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListGroups) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListPolicies`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // PolicyWrapper encapsulates AWS Identity and Access Management (IAM) policy actions
    // used in the examples.
    // It contains an IAM service client that is used to perform policy actions.
    type PolicyWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListPolicies gets up to maxPolicies policies.
    func (wrapper PolicyWrapper) ListPolicies(ctx context.Context, maxPolicies int32) ([]types.Policy, error) {
    	var policies []types.Policy
    	result, err := wrapper.IamClient.ListPolicies(ctx, &iam.ListPoliciesInput{
    		MaxItems: aws.Int32(maxPolicies),
    	})
    	if err != nil {
    		log.Printf("Couldn't list policies. Here's why: %v\n", err)
    	} else {
    		policies = result.Policies
    	}
    	return policies, err
    }
    
    
    

  * For API details, see [ListPolicies](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListPolicies) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListRolePolicies`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListRolePolicies lists the inline policies for a role.
    func (wrapper RoleWrapper) ListRolePolicies(ctx context.Context, roleName string) ([]string, error) {
    	var policies []string
    	result, err := wrapper.IamClient.ListRolePolicies(ctx, &iam.ListRolePoliciesInput{
    		RoleName: aws.String(roleName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list policies for role %v. Here's why: %v\n", roleName, err)
    	} else {
    		policies = result.PolicyNames
    	}
    	return policies, err
    }
    
    
    

  * For API details, see [ListRolePolicies](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListRolePolicies) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListRoles`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
    // used in the examples.
    // It contains an IAM service client that is used to perform role actions.
    type RoleWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListRoles gets up to maxRoles roles.
    func (wrapper RoleWrapper) ListRoles(ctx context.Context, maxRoles int32) ([]types.Role, error) {
    	var roles []types.Role
    	result, err := wrapper.IamClient.ListRoles(ctx,
    		&iam.ListRolesInput{MaxItems: aws.Int32(maxRoles)},
    	)
    	if err != nil {
    		log.Printf("Couldn't list roles. Here's why: %v\n", err)
    	} else {
    		roles = result.Roles
    	}
    	return roles, err
    }
    
    
    

  * For API details, see [ListRoles](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListRoles) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListSAMLProviders`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    )
    
    // AccountWrapper encapsulates AWS Identity and Access Management (IAM) account actions
    // used in the examples.
    // It contains an IAM service client that is used to perform account actions.
    type AccountWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListSAMLProviders gets the SAML providers for the account.
    func (wrapper AccountWrapper) ListSAMLProviders(ctx context.Context) ([]types.SAMLProviderListEntry, error) {
    	var providers []types.SAMLProviderListEntry
    	result, err := wrapper.IamClient.ListSAMLProviders(ctx, &iam.ListSAMLProvidersInput{})
    	if err != nil {
    		log.Printf("Couldn't list SAML providers. Here's why: %v\n", err)
    	} else {
    		providers = result.SAMLProviderList
    	}
    	return providers, err
    }
    
    
    

  * For API details, see [ListSAMLProviders](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListSAMLProviders) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListUserPolicies`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListUserPolicies lists the inline policies for the specified user.
    func (wrapper UserWrapper) ListUserPolicies(ctx context.Context, userName string) ([]string, error) {
    	var policies []string
    	result, err := wrapper.IamClient.ListUserPolicies(ctx, &iam.ListUserPoliciesInput{
    		UserName: aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't list policies for user %v. Here's why: %v\n", userName, err)
    	} else {
    		policies = result.PolicyNames
    	}
    	return policies, err
    }
    
    
    

  * For API details, see [ListUserPolicies](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListUserPolicies) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListUsers`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // ListUsers gets up to maxUsers number of users.
    func (wrapper UserWrapper) ListUsers(ctx context.Context, maxUsers int32) ([]types.User, error) {
    	var users []types.User
    	result, err := wrapper.IamClient.ListUsers(ctx, &iam.ListUsersInput{
    		MaxItems: aws.Int32(maxUsers),
    	})
    	if err != nil {
    		log.Printf("Couldn't list users. Here's why: %v\n", err)
    	} else {
    		users = result.Users
    	}
    	return users, err
    }
    
    
    

  * For API details, see [ListUsers](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListUsers) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `PutUserPolicy`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/iam"
    	"github.com/aws/aws-sdk-go-v2/service/iam/types"
    	"github.com/aws/smithy-go"
    )
    
    // UserWrapper encapsulates user actions used in the examples.
    // It contains an IAM service client that is used to perform user actions.
    type UserWrapper struct {
    	IamClient *iam.Client
    }
    
    
    
    // CreateUserPolicy adds an inline policy to a user. This example creates a policy that
    // grants a list of actions on a specified role.
    // PolicyDocument shows how to work with a policy document as a data structure and
    // serialize it to JSON by using Go's JSON marshaler.
    func (wrapper UserWrapper) CreateUserPolicy(ctx context.Context, userName string, policyName string, actions []string,
    	roleArn string) error {
    	policyDoc := PolicyDocument{
    		Version: "2012-10-17",
    		Statement: []PolicyStatement{{
    			Effect:   "Allow",
    			Action:   actions,
    			Resource: aws.String(roleArn),
    		}},
    	}
    	policyBytes, err := json.Marshal(policyDoc)
    	if err != nil {
    		log.Printf("Couldn't create policy document for %v. Here's why: %v\n", roleArn, err)
    		return err
    	}
    	_, err = wrapper.IamClient.PutUserPolicy(ctx, &iam.PutUserPolicyInput{
    		PolicyDocument: aws.String(string(policyBytes)),
    		PolicyName:     aws.String(policyName),
    		UserName:       aws.String(userName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create policy for user %v. Here's why: %v\n", userName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [PutUserPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.PutUserPolicy) in _AWS SDK for Go API Reference_. 




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

DynamoDB

Kinesis

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
