# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_rds_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_rds_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

BasicsActionsServerless examples

# Amazon RDS examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon RDS.

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using Amazon RDS.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    )
    
    // main uses the AWS SDK for Go V2 to create an Amazon Relational Database Service (Amazon RDS)
    // client and list up to 20 DB instances in your account.
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
    	rdsClient := rds.NewFromConfig(sdkConfig)
    	const maxInstances = 20
    	fmt.Printf("Let's list up to %v DB instances.\n", maxInstances)
    	output, err := rdsClient.DescribeDBInstances(ctx,
    		&rds.DescribeDBInstancesInput{MaxRecords: aws.Int32(maxInstances)})
    	if err != nil {
    		fmt.Printf("Couldn't list DB instances: %v\n", err)
    		return
    	}
    	if len(output.DBInstances) == 0 {
    		fmt.Println("No DB instances found.")
    	} else {
    		for _, instance := range output.DBInstances {
    			fmt.Printf("DB instance %v has database %v.\n", *instance.DBInstanceIdentifier,
    				*instance.DBName)
    		}
    	}
    }
    
    
    

  * For API details, see [DescribeDBInstances](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBInstances) in _AWS SDK for Go API Reference_. 




###### Topics

  * Basics

  * Actions

  * Serverless examples




## Basics

The following code example shows how to:

  * Create a custom DB parameter group and set parameter values.

  * Create a DB instance that's configured to use the parameter group. The DB instance also contains a database.

  * Take a snapshot of the instance.

  * Delete the instance and parameter group.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 

Run an interactive scenario at a command prompt.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"sort"
    	"strconv"
    	"strings"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/rds/actions"
    	"github.com/google/uuid"
    )
    
    // GetStartedInstances is an interactive example that shows you how to use the AWS SDK for Go
    // with Amazon Relation Database Service (Amazon RDS) to do the following:
    //
    //  1. Create a custom DB parameter group and set parameter values.
    //  2. Create a DB instance that is configured to use the parameter group. The DB instance
    //     also contains a database.
    //  3. Take a snapshot of the DB instance.
    //  4. Delete the DB instance and parameter group.
    type GetStartedInstances struct {
    	sdkConfig  aws.Config
    	instances  actions.DbInstances
    	questioner demotools.IQuestioner
    	helper     IScenarioHelper
    	isTestRun  bool
    }
    
    // NewGetStartedInstances constructs a GetStartedInstances instance from a configuration.
    // It uses the specified config to get an Amazon RDS
    // client and create wrappers for the actions used in the scenario.
    func NewGetStartedInstances(sdkConfig aws.Config, questioner demotools.IQuestioner,
    	helper IScenarioHelper) GetStartedInstances {
    	rdsClient := rds.NewFromConfig(sdkConfig)
    	return GetStartedInstances{
    		sdkConfig:  sdkConfig,
    		instances:  actions.DbInstances{RdsClient: rdsClient},
    		questioner: questioner,
    		helper:     helper,
    	}
    }
    
    // Run runs the interactive scenario.
    func (scenario GetStartedInstances) Run(ctx context.Context, dbEngine string, parameterGroupName string,
    	instanceName string, dbName string) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon Relational Database Service (Amazon RDS) DB Instance demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	parameterGroup := scenario.CreateParameterGroup(ctx, dbEngine, parameterGroupName)
    	scenario.SetUserParameters(ctx, parameterGroupName)
    	instance := scenario.CreateInstance(ctx, instanceName, dbEngine, dbName, parameterGroup)
    	scenario.DisplayConnection(instance)
    	scenario.CreateSnapshot(ctx, instance)
    	scenario.Cleanup(ctx, instance, parameterGroup)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // CreateParameterGroup shows how to get available engine versions for a specified
    // database engine and create a DB parameter group that is compatible with a
    // selected engine family.
    func (scenario GetStartedInstances) CreateParameterGroup(ctx context.Context, dbEngine string,
    	parameterGroupName string) *types.DBParameterGroup {
    
    	log.Printf("Checking for an existing DB parameter group named %v.\n",
    		parameterGroupName)
    	parameterGroup, err := scenario.instances.GetParameterGroup(ctx, parameterGroupName)
    	if err != nil {
    		panic(err)
    	}
    	if parameterGroup == nil {
    		log.Printf("Getting available database engine versions for %v.\n", dbEngine)
    		engineVersions, err := scenario.instances.GetEngineVersions(ctx, dbEngine, "")
    		if err != nil {
    			panic(err)
    		}
    
    		familySet := map[string]struct{}{}
    		for _, family := range engineVersions {
    			familySet[*family.DBParameterGroupFamily] = struct{}{}
    		}
    		var families []string
    		for family := range familySet {
    			families = append(families, family)
    		}
    		sort.Strings(families)
    		familyIndex := scenario.questioner.AskChoice("Which family do you want to use?\n", families)
    		log.Println("Creating a DB parameter group.")
    		_, err = scenario.instances.CreateParameterGroup(
    			ctx, parameterGroupName, families[familyIndex], "Example parameter group.")
    		if err != nil {
    			panic(err)
    		}
    		parameterGroup, err = scenario.instances.GetParameterGroup(ctx, parameterGroupName)
    		if err != nil {
    			panic(err)
    		}
    	}
    	log.Printf("Parameter group %v:\n", *parameterGroup.DBParameterGroupFamily)
    	log.Printf("\tName: %v\n", *parameterGroup.DBParameterGroupName)
    	log.Printf("\tARN: %v\n", *parameterGroup.DBParameterGroupArn)
    	log.Printf("\tFamily: %v\n", *parameterGroup.DBParameterGroupFamily)
    	log.Printf("\tDescription: %v\n", *parameterGroup.Description)
    	log.Println(strings.Repeat("-", 88))
    	return parameterGroup
    }
    
    // SetUserParameters shows how to get the parameters contained in a custom parameter
    // group and update some of the parameter values in the group.
    func (scenario GetStartedInstances) SetUserParameters(ctx context.Context, parameterGroupName string) {
    	log.Println("Let's set some parameter values in your parameter group.")
    	dbParameters, err := scenario.instances.GetParameters(ctx, parameterGroupName, "")
    	if err != nil {
    		panic(err)
    	}
    	var updateParams []types.Parameter
    	for _, dbParam := range dbParameters {
    		if strings.HasPrefix(*dbParam.ParameterName, "auto_increment") &&
    			*dbParam.IsModifiable && *dbParam.DataType == "integer" {
    			log.Printf("The %v parameter is described as:\n\t%v",
    				*dbParam.ParameterName, *dbParam.Description)
    			rangeSplit := strings.Split(*dbParam.AllowedValues, "-")
    			lower, _ := strconv.Atoi(rangeSplit[0])
    			upper, _ := strconv.Atoi(rangeSplit[1])
    			newValue := scenario.questioner.AskInt(
    				fmt.Sprintf("Enter a value between %v and %v:", lower, upper),
    				demotools.InIntRange{Lower: lower, Upper: upper})
    			dbParam.ParameterValue = aws.String(strconv.Itoa(newValue))
    			updateParams = append(updateParams, dbParam)
    		}
    	}
    	err = scenario.instances.UpdateParameters(ctx, parameterGroupName, updateParams)
    	if err != nil {
    		panic(err)
    	}
    	log.Println("To get a list of parameters that you set previously, specify a source of 'user'.")
    	userParameters, err := scenario.instances.GetParameters(ctx, parameterGroupName, "user")
    	if err != nil {
    		panic(err)
    	}
    	log.Println("Here are the parameters you set:")
    	for _, param := range userParameters {
    		log.Printf("\t%v: %v\n", *param.ParameterName, *param.ParameterValue)
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    // CreateInstance shows how to create a DB instance that contains a database of a
    // specified type. The database is also configured to use a custom DB parameter group.
    func (scenario GetStartedInstances) CreateInstance(ctx context.Context, instanceName string, dbEngine string,
    	dbName string, parameterGroup *types.DBParameterGroup) *types.DBInstance {
    
    	log.Println("Checking for an existing DB instance.")
    	instance, err := scenario.instances.GetInstance(ctx, instanceName)
    	if err != nil {
    		panic(err)
    	}
    	if instance == nil {
    		adminUsername := scenario.questioner.Ask(
    			"Enter an administrator username for the database: ", demotools.NotEmpty{})
    		adminPassword := scenario.questioner.AskPassword(
    			"Enter a password for the administrator (at least 8 characters): ", 7)
    		engineVersions, err := scenario.instances.GetEngineVersions(ctx, dbEngine,
    			*parameterGroup.DBParameterGroupFamily)
    		if err != nil {
    			panic(err)
    		}
    		var engineChoices []string
    		for _, engine := range engineVersions {
    			engineChoices = append(engineChoices, *engine.EngineVersion)
    		}
    		engineIndex := scenario.questioner.AskChoice(
    			"The available engines for your parameter group are:\n", engineChoices)
    		engineSelection := engineVersions[engineIndex]
    		instOpts, err := scenario.instances.GetOrderableInstances(ctx, *engineSelection.Engine,
    			*engineSelection.EngineVersion)
    		if err != nil {
    			panic(err)
    		}
    		optSet := map[string]struct{}{}
    		for _, opt := range instOpts {
    			if strings.Contains(*opt.DBInstanceClass, "micro") {
    				optSet[*opt.DBInstanceClass] = struct{}{}
    			}
    		}
    		var optChoices []string
    		for opt := range optSet {
    			optChoices = append(optChoices, opt)
    		}
    		sort.Strings(optChoices)
    		optIndex := scenario.questioner.AskChoice(
    			"The available micro DB instance classes for your database engine are:\n", optChoices)
    		storageType := "standard"
    		allocatedStorage := int32(5)
    		log.Printf("Creating a DB instance named %v and database %v.\n"+
    			"The DB instance is configured to use your custom parameter group %v,\n"+
    			"selected engine %v,\n"+
    			"selected DB instance class %v,"+
    			"and %v GiB of %v storage.\n"+
    			"This typically takes several minutes.",
    			instanceName, dbName, *parameterGroup.DBParameterGroupName, *engineSelection.EngineVersion,
    			optChoices[optIndex], allocatedStorage, storageType)
    		instance, err = scenario.instances.CreateInstance(
    			ctx, instanceName, dbName, *engineSelection.Engine, *engineSelection.EngineVersion,
    			*parameterGroup.DBParameterGroupName, optChoices[optIndex], storageType,
    			allocatedStorage, adminUsername, adminPassword)
    		if err != nil {
    			panic(err)
    		}
    		for *instance.DBInstanceStatus != "available" {
    			scenario.helper.Pause(30)
    			instance, err = scenario.instances.GetInstance(ctx, instanceName)
    			if err != nil {
    				panic(err)
    			}
    		}
    		log.Println("Instance created and available.")
    	}
    	log.Println("Instance data:")
    	log.Printf("\tDBInstanceIdentifier: %v\n", *instance.DBInstanceIdentifier)
    	log.Printf("\tARN: %v\n", *instance.DBInstanceArn)
    	log.Printf("\tStatus: %v\n", *instance.DBInstanceStatus)
    	log.Printf("\tEngine: %v\n", *instance.Engine)
    	log.Printf("\tEngine version: %v\n", *instance.EngineVersion)
    	log.Println(strings.Repeat("-", 88))
    	return instance
    }
    
    // DisplayConnection displays connection information about a DB instance and tips
    // on how to connect to it.
    func (scenario GetStartedInstances) DisplayConnection(instance *types.DBInstance) {
    	log.Println(
    		"You can now connect to your database by using your favorite MySQL client.\n" +
    			"One way to connect is by using the 'mysql' shell on an Amazon EC2 instance\n" +
    			"that is running in the same VPC as your DB instance. Pass the endpoint,\n" +
    			"port, and administrator username to 'mysql'. Then, enter your password\n" +
    			"when prompted:")
    	log.Printf("\n\tmysql -h %v -P %v -u %v -p\n",
    		*instance.Endpoint.Address, instance.Endpoint.Port, *instance.MasterUsername)
    	log.Println("For more information, see the User Guide for RDS:\n" +
    		"\thttps://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html#CHAP_GettingStarted.Connecting.MySQL")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // CreateSnapshot shows how to create a DB instance snapshot and wait until it's available.
    func (scenario GetStartedInstances) CreateSnapshot(ctx context.Context, instance *types.DBInstance) {
    	if scenario.questioner.AskBool(
    		"Do you want to create a snapshot of your DB instance (y/n)? ", "y") {
    		snapshotId := fmt.Sprintf("%v-%v", *instance.DBInstanceIdentifier, scenario.helper.UniqueId())
    		log.Printf("Creating a snapshot named %v. This typically takes a few minutes.\n", snapshotId)
    		snapshot, err := scenario.instances.CreateSnapshot(ctx, *instance.DBInstanceIdentifier, snapshotId)
    		if err != nil {
    			panic(err)
    		}
    		for *snapshot.Status != "available" {
    			scenario.helper.Pause(30)
    			snapshot, err = scenario.instances.GetSnapshot(ctx, snapshotId)
    			if err != nil {
    				panic(err)
    			}
    		}
    		log.Println("Snapshot data:")
    		log.Printf("\tDBSnapshotIdentifier: %v\n", *snapshot.DBSnapshotIdentifier)
    		log.Printf("\tARN: %v\n", *snapshot.DBSnapshotArn)
    		log.Printf("\tStatus: %v\n", *snapshot.Status)
    		log.Printf("\tEngine: %v\n", *snapshot.Engine)
    		log.Printf("\tEngine version: %v\n", *snapshot.EngineVersion)
    		log.Printf("\tDBInstanceIdentifier: %v\n", *snapshot.DBInstanceIdentifier)
    		log.Printf("\tSnapshotCreateTime: %v\n", *snapshot.SnapshotCreateTime)
    		log.Println(strings.Repeat("-", 88))
    	}
    }
    
    // Cleanup shows how to clean up a DB instance and DB parameter group.
    // Before the DB parameter group can be deleted, all associated DB instances must first be deleted.
    func (scenario GetStartedInstances) Cleanup(
    	ctx context.Context, instance *types.DBInstance, parameterGroup *types.DBParameterGroup) {
    
    	if scenario.questioner.AskBool(
    		"\nDo you want to delete the database instance and parameter group (y/n)? ", "y") {
    		log.Printf("Deleting database instance %v.\n", *instance.DBInstanceIdentifier)
    		err := scenario.instances.DeleteInstance(ctx, *instance.DBInstanceIdentifier)
    		if err != nil {
    			panic(err)
    		}
    		log.Println(
    			"Waiting for the DB instance to delete. This typically takes several minutes.")
    		for instance != nil {
    			scenario.helper.Pause(30)
    			instance, err = scenario.instances.GetInstance(ctx, *instance.DBInstanceIdentifier)
    			if err != nil {
    				panic(err)
    			}
    		}
    		log.Printf("Deleting parameter group %v.", *parameterGroup.DBParameterGroupName)
    		err = scenario.instances.DeleteParameterGroup(ctx, *parameterGroup.DBParameterGroupName)
    		if err != nil {
    			panic(err)
    		}
    	}
    }
    
    // IScenarioHelper abstracts the function from a scenario so that it
    // can be mocked for unit testing.
    type IScenarioHelper interface {
    	Pause(secs int)
    	UniqueId() string
    }
    type ScenarioHelper struct{}
    
    // Pause waits for the specified number of seconds.
    func (helper ScenarioHelper) Pause(secs int) {
    	time.Sleep(time.Duration(secs) * time.Second)
    }
    
    // UniqueId returns a new UUID.
    func (helper ScenarioHelper) UniqueId() string {
    	return uuid.New().String()
    }
    
    
    

Define functions that are called by the scenario to manage Amazon RDS actions.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    // GetParameterGroup gets a DB parameter group by name.
    func (instances *DbInstances) GetParameterGroup(ctx context.Context, parameterGroupName string) (
    	*types.DBParameterGroup, error) {
    	output, err := instances.RdsClient.DescribeDBParameterGroups(
    		ctx, &rds.DescribeDBParameterGroupsInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    		})
    	if err != nil {
    		var notFoundError *types.DBParameterGroupNotFoundFault
    		if errors.As(err, &notFoundError) {
    			log.Printf("Parameter group %v does not exist.\n", parameterGroupName)
    			err = nil
    		} else {
    			log.Printf("Error getting parameter group %v: %v\n", parameterGroupName, err)
    		}
    		return nil, err
    	} else {
    		return &output.DBParameterGroups[0], err
    	}
    }
    
    
    
    // CreateParameterGroup creates a DB parameter group that is based on the specified
    // parameter group family.
    func (instances *DbInstances) CreateParameterGroup(
    	ctx context.Context, parameterGroupName string, parameterGroupFamily string, description string) (
    	*types.DBParameterGroup, error) {
    
    	output, err := instances.RdsClient.CreateDBParameterGroup(ctx,
    		&rds.CreateDBParameterGroupInput{
    			DBParameterGroupName:   aws.String(parameterGroupName),
    			DBParameterGroupFamily: aws.String(parameterGroupFamily),
    			Description:            aws.String(description),
    		})
    	if err != nil {
    		log.Printf("Couldn't create parameter group %v: %v\n", parameterGroupName, err)
    		return nil, err
    	} else {
    		return output.DBParameterGroup, err
    	}
    }
    
    
    
    // DeleteParameterGroup deletes the named DB parameter group.
    func (instances *DbInstances) DeleteParameterGroup(ctx context.Context, parameterGroupName string) error {
    	_, err := instances.RdsClient.DeleteDBParameterGroup(ctx,
    		&rds.DeleteDBParameterGroupInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    		})
    	if err != nil {
    		log.Printf("Couldn't delete parameter group %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    
    // GetParameters gets the parameters that are contained in a DB parameter group.
    func (instances *DbInstances) GetParameters(ctx context.Context, parameterGroupName string, source string) (
    	[]types.Parameter, error) {
    
    	var output *rds.DescribeDBParametersOutput
    	var params []types.Parameter
    	var err error
    	parameterPaginator := rds.NewDescribeDBParametersPaginator(instances.RdsClient,
    		&rds.DescribeDBParametersInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    			Source:               aws.String(source),
    		})
    	for parameterPaginator.HasMorePages() {
    		output, err = parameterPaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get parameters for %v: %v\n", parameterGroupName, err)
    			break
    		} else {
    			params = append(params, output.Parameters...)
    		}
    	}
    	return params, err
    }
    
    
    
    // UpdateParameters updates parameters in a named DB parameter group.
    func (instances *DbInstances) UpdateParameters(ctx context.Context, parameterGroupName string, params []types.Parameter) error {
    	_, err := instances.RdsClient.ModifyDBParameterGroup(ctx,
    		&rds.ModifyDBParameterGroupInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    			Parameters:           params,
    		})
    	if err != nil {
    		log.Printf("Couldn't update parameters in %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    
    // CreateSnapshot creates a snapshot of a DB instance.
    func (instances *DbInstances) CreateSnapshot(ctx context.Context, instanceName string, snapshotName string) (
    	*types.DBSnapshot, error) {
    	output, err := instances.RdsClient.CreateDBSnapshot(ctx, &rds.CreateDBSnapshotInput{
    		DBInstanceIdentifier: aws.String(instanceName),
    		DBSnapshotIdentifier: aws.String(snapshotName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return output.DBSnapshot, nil
    	}
    }
    
    
    
    // GetSnapshot gets a DB instance snapshot.
    func (instances *DbInstances) GetSnapshot(ctx context.Context, snapshotName string) (*types.DBSnapshot, error) {
    	output, err := instances.RdsClient.DescribeDBSnapshots(ctx,
    		&rds.DescribeDBSnapshotsInput{
    			DBSnapshotIdentifier: aws.String(snapshotName),
    		})
    	if err != nil {
    		log.Printf("Couldn't get snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return &output.DBSnapshots[0], nil
    	}
    }
    
    
    
    // CreateInstance creates a DB instance.
    func (instances *DbInstances) CreateInstance(ctx context.Context, instanceName string, dbName string,
    	dbEngine string, dbEngineVersion string, parameterGroupName string, dbInstanceClass string,
    	storageType string, allocatedStorage int32, adminName string, adminPassword string) (
    	*types.DBInstance, error) {
    	output, err := instances.RdsClient.CreateDBInstance(ctx, &rds.CreateDBInstanceInput{
    		DBInstanceIdentifier: aws.String(instanceName),
    		DBName:               aws.String(dbName),
    		DBParameterGroupName: aws.String(parameterGroupName),
    		Engine:               aws.String(dbEngine),
    		EngineVersion:        aws.String(dbEngineVersion),
    		DBInstanceClass:      aws.String(dbInstanceClass),
    		StorageType:          aws.String(storageType),
    		AllocatedStorage:     aws.Int32(allocatedStorage),
    		MasterUsername:       aws.String(adminName),
    		MasterUserPassword:   aws.String(adminPassword),
    	})
    	if err != nil {
    		log.Printf("Couldn't create instance %v: %v\n", instanceName, err)
    		return nil, err
    	} else {
    		return output.DBInstance, nil
    	}
    }
    
    
    
    // GetInstance gets data about a DB instance.
    func (instances *DbInstances) GetInstance(ctx context.Context, instanceName string) (
    	*types.DBInstance, error) {
    	output, err := instances.RdsClient.DescribeDBInstances(ctx,
    		&rds.DescribeDBInstancesInput{
    			DBInstanceIdentifier: aws.String(instanceName),
    		})
    	if err != nil {
    		var notFoundError *types.DBInstanceNotFoundFault
    		if errors.As(err, &notFoundError) {
    			log.Printf("DB instance %v does not exist.\n", instanceName)
    			err = nil
    		} else {
    			log.Printf("Couldn't get instance %v: %v\n", instanceName, err)
    		}
    		return nil, err
    	} else {
    		return &output.DBInstances[0], nil
    	}
    }
    
    
    
    // DeleteInstance deletes a DB instance.
    func (instances *DbInstances) DeleteInstance(ctx context.Context, instanceName string) error {
    	_, err := instances.RdsClient.DeleteDBInstance(ctx, &rds.DeleteDBInstanceInput{
    		DBInstanceIdentifier:   aws.String(instanceName),
    		SkipFinalSnapshot:      aws.Bool(true),
    		DeleteAutomatedBackups: aws.Bool(true),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete instance %v: %v\n", instanceName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    
    // GetEngineVersions gets database engine versions that are available for the specified engine
    // and parameter group family.
    func (instances *DbInstances) GetEngineVersions(ctx context.Context, engine string, parameterGroupFamily string) (
    	[]types.DBEngineVersion, error) {
    	output, err := instances.RdsClient.DescribeDBEngineVersions(ctx,
    		&rds.DescribeDBEngineVersionsInput{
    			Engine:                 aws.String(engine),
    			DBParameterGroupFamily: aws.String(parameterGroupFamily),
    		})
    	if err != nil {
    		log.Printf("Couldn't get engine versions for %v: %v\n", engine, err)
    		return nil, err
    	} else {
    		return output.DBEngineVersions, nil
    	}
    }
    
    
    
    // GetOrderableInstances uses a paginator to get DB instance options that can be used to create DB instances that are
    // compatible with a set of specifications.
    func (instances *DbInstances) GetOrderableInstances(ctx context.Context, engine string, engineVersion string) (
    	[]types.OrderableDBInstanceOption, error) {
    
    	var output *rds.DescribeOrderableDBInstanceOptionsOutput
    	var instanceOptions []types.OrderableDBInstanceOption
    	var err error
    	orderablePaginator := rds.NewDescribeOrderableDBInstanceOptionsPaginator(instances.RdsClient,
    		&rds.DescribeOrderableDBInstanceOptionsInput{
    			Engine:        aws.String(engine),
    			EngineVersion: aws.String(engineVersion),
    		})
    	for orderablePaginator.HasMorePages() {
    		output, err = orderablePaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get orderable DB instance options: %v\n", err)
    			break
    		} else {
    			instanceOptions = append(instanceOptions, output.OrderableDBInstanceOptions...)
    		}
    	}
    	return instanceOptions, err
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [CreateDBInstance](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBInstance)

    * [CreateDBParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBParameterGroup)

    * [CreateDBSnapshot](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBSnapshot)

    * [DeleteDBInstance](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBInstance)

    * [DeleteDBParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBParameterGroup)

    * [DescribeDBEngineVersions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBEngineVersions)

    * [DescribeDBInstances](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBInstances)

    * [DescribeDBParameterGroups](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBParameterGroups)

    * [DescribeDBParameters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBParameters)

    * [DescribeDBSnapshots](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBSnapshots)

    * [DescribeOrderableDBInstanceOptions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeOrderableDBInstanceOptions)

    * [ModifyDBParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.ModifyDBParameterGroup)




## Actions

The following code example shows how to use `CreateDBInstance`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // CreateInstance creates a DB instance.
    func (instances *DbInstances) CreateInstance(ctx context.Context, instanceName string, dbName string,
    	dbEngine string, dbEngineVersion string, parameterGroupName string, dbInstanceClass string,
    	storageType string, allocatedStorage int32, adminName string, adminPassword string) (
    	*types.DBInstance, error) {
    	output, err := instances.RdsClient.CreateDBInstance(ctx, &rds.CreateDBInstanceInput{
    		DBInstanceIdentifier: aws.String(instanceName),
    		DBName:               aws.String(dbName),
    		DBParameterGroupName: aws.String(parameterGroupName),
    		Engine:               aws.String(dbEngine),
    		EngineVersion:        aws.String(dbEngineVersion),
    		DBInstanceClass:      aws.String(dbInstanceClass),
    		StorageType:          aws.String(storageType),
    		AllocatedStorage:     aws.Int32(allocatedStorage),
    		MasterUsername:       aws.String(adminName),
    		MasterUserPassword:   aws.String(adminPassword),
    	})
    	if err != nil {
    		log.Printf("Couldn't create instance %v: %v\n", instanceName, err)
    		return nil, err
    	} else {
    		return output.DBInstance, nil
    	}
    }
    
    
    

  * For API details, see [CreateDBInstance](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBInstance) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateDBParameterGroup`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // CreateParameterGroup creates a DB parameter group that is based on the specified
    // parameter group family.
    func (instances *DbInstances) CreateParameterGroup(
    	ctx context.Context, parameterGroupName string, parameterGroupFamily string, description string) (
    	*types.DBParameterGroup, error) {
    
    	output, err := instances.RdsClient.CreateDBParameterGroup(ctx,
    		&rds.CreateDBParameterGroupInput{
    			DBParameterGroupName:   aws.String(parameterGroupName),
    			DBParameterGroupFamily: aws.String(parameterGroupFamily),
    			Description:            aws.String(description),
    		})
    	if err != nil {
    		log.Printf("Couldn't create parameter group %v: %v\n", parameterGroupName, err)
    		return nil, err
    	} else {
    		return output.DBParameterGroup, err
    	}
    }
    
    
    

  * For API details, see [CreateDBParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBParameterGroup) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateDBSnapshot`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // CreateSnapshot creates a snapshot of a DB instance.
    func (instances *DbInstances) CreateSnapshot(ctx context.Context, instanceName string, snapshotName string) (
    	*types.DBSnapshot, error) {
    	output, err := instances.RdsClient.CreateDBSnapshot(ctx, &rds.CreateDBSnapshotInput{
    		DBInstanceIdentifier: aws.String(instanceName),
    		DBSnapshotIdentifier: aws.String(snapshotName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return output.DBSnapshot, nil
    	}
    }
    
    
    

  * For API details, see [CreateDBSnapshot](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBSnapshot) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteDBInstance`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // DeleteInstance deletes a DB instance.
    func (instances *DbInstances) DeleteInstance(ctx context.Context, instanceName string) error {
    	_, err := instances.RdsClient.DeleteDBInstance(ctx, &rds.DeleteDBInstanceInput{
    		DBInstanceIdentifier:   aws.String(instanceName),
    		SkipFinalSnapshot:      aws.Bool(true),
    		DeleteAutomatedBackups: aws.Bool(true),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete instance %v: %v\n", instanceName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    

  * For API details, see [DeleteDBInstance](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBInstance) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteDBParameterGroup`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // DeleteParameterGroup deletes the named DB parameter group.
    func (instances *DbInstances) DeleteParameterGroup(ctx context.Context, parameterGroupName string) error {
    	_, err := instances.RdsClient.DeleteDBParameterGroup(ctx,
    		&rds.DeleteDBParameterGroupInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    		})
    	if err != nil {
    		log.Printf("Couldn't delete parameter group %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    

  * For API details, see [DeleteDBParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBParameterGroup) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBEngineVersions`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // GetEngineVersions gets database engine versions that are available for the specified engine
    // and parameter group family.
    func (instances *DbInstances) GetEngineVersions(ctx context.Context, engine string, parameterGroupFamily string) (
    	[]types.DBEngineVersion, error) {
    	output, err := instances.RdsClient.DescribeDBEngineVersions(ctx,
    		&rds.DescribeDBEngineVersionsInput{
    			Engine:                 aws.String(engine),
    			DBParameterGroupFamily: aws.String(parameterGroupFamily),
    		})
    	if err != nil {
    		log.Printf("Couldn't get engine versions for %v: %v\n", engine, err)
    		return nil, err
    	} else {
    		return output.DBEngineVersions, nil
    	}
    }
    
    
    

  * For API details, see [DescribeDBEngineVersions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBEngineVersions) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBInstances`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // GetInstance gets data about a DB instance.
    func (instances *DbInstances) GetInstance(ctx context.Context, instanceName string) (
    	*types.DBInstance, error) {
    	output, err := instances.RdsClient.DescribeDBInstances(ctx,
    		&rds.DescribeDBInstancesInput{
    			DBInstanceIdentifier: aws.String(instanceName),
    		})
    	if err != nil {
    		var notFoundError *types.DBInstanceNotFoundFault
    		if errors.As(err, &notFoundError) {
    			log.Printf("DB instance %v does not exist.\n", instanceName)
    			err = nil
    		} else {
    			log.Printf("Couldn't get instance %v: %v\n", instanceName, err)
    		}
    		return nil, err
    	} else {
    		return &output.DBInstances[0], nil
    	}
    }
    
    
    

  * For API details, see [DescribeDBInstances](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBInstances) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBParameterGroups`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // GetParameterGroup gets a DB parameter group by name.
    func (instances *DbInstances) GetParameterGroup(ctx context.Context, parameterGroupName string) (
    	*types.DBParameterGroup, error) {
    	output, err := instances.RdsClient.DescribeDBParameterGroups(
    		ctx, &rds.DescribeDBParameterGroupsInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    		})
    	if err != nil {
    		var notFoundError *types.DBParameterGroupNotFoundFault
    		if errors.As(err, &notFoundError) {
    			log.Printf("Parameter group %v does not exist.\n", parameterGroupName)
    			err = nil
    		} else {
    			log.Printf("Error getting parameter group %v: %v\n", parameterGroupName, err)
    		}
    		return nil, err
    	} else {
    		return &output.DBParameterGroups[0], err
    	}
    }
    
    
    

  * For API details, see [DescribeDBParameterGroups](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBParameterGroups) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBParameters`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // GetParameters gets the parameters that are contained in a DB parameter group.
    func (instances *DbInstances) GetParameters(ctx context.Context, parameterGroupName string, source string) (
    	[]types.Parameter, error) {
    
    	var output *rds.DescribeDBParametersOutput
    	var params []types.Parameter
    	var err error
    	parameterPaginator := rds.NewDescribeDBParametersPaginator(instances.RdsClient,
    		&rds.DescribeDBParametersInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    			Source:               aws.String(source),
    		})
    	for parameterPaginator.HasMorePages() {
    		output, err = parameterPaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get parameters for %v: %v\n", parameterGroupName, err)
    			break
    		} else {
    			params = append(params, output.Parameters...)
    		}
    	}
    	return params, err
    }
    
    
    

  * For API details, see [DescribeDBParameters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBParameters) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBSnapshots`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // GetSnapshot gets a DB instance snapshot.
    func (instances *DbInstances) GetSnapshot(ctx context.Context, snapshotName string) (*types.DBSnapshot, error) {
    	output, err := instances.RdsClient.DescribeDBSnapshots(ctx,
    		&rds.DescribeDBSnapshotsInput{
    			DBSnapshotIdentifier: aws.String(snapshotName),
    		})
    	if err != nil {
    		log.Printf("Couldn't get snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return &output.DBSnapshots[0], nil
    	}
    }
    
    
    

  * For API details, see [DescribeDBSnapshots](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBSnapshots) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeOrderableDBInstanceOptions`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // GetOrderableInstances uses a paginator to get DB instance options that can be used to create DB instances that are
    // compatible with a set of specifications.
    func (instances *DbInstances) GetOrderableInstances(ctx context.Context, engine string, engineVersion string) (
    	[]types.OrderableDBInstanceOption, error) {
    
    	var output *rds.DescribeOrderableDBInstanceOptionsOutput
    	var instanceOptions []types.OrderableDBInstanceOption
    	var err error
    	orderablePaginator := rds.NewDescribeOrderableDBInstanceOptionsPaginator(instances.RdsClient,
    		&rds.DescribeOrderableDBInstanceOptionsInput{
    			Engine:        aws.String(engine),
    			EngineVersion: aws.String(engineVersion),
    		})
    	for orderablePaginator.HasMorePages() {
    		output, err = orderablePaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get orderable DB instance options: %v\n", err)
    			break
    		} else {
    			instanceOptions = append(instanceOptions, output.OrderableDBInstanceOptions...)
    		}
    	}
    	return instanceOptions, err
    }
    
    
    

  * For API details, see [DescribeOrderableDBInstanceOptions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeOrderableDBInstanceOptions) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ModifyDBParameterGroup`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/rds#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbInstances struct {
    	RdsClient *rds.Client
    }
    
    
    
    // UpdateParameters updates parameters in a named DB parameter group.
    func (instances *DbInstances) UpdateParameters(ctx context.Context, parameterGroupName string, params []types.Parameter) error {
    	_, err := instances.RdsClient.ModifyDBParameterGroup(ctx,
    		&rds.ModifyDBParameterGroupInput{
    			DBParameterGroupName: aws.String(parameterGroupName),
    			Parameters:           params,
    		})
    	if err != nil {
    		log.Printf("Couldn't update parameters in %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    

  * For API details, see [ModifyDBParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.ModifyDBParameterGroup) in _AWS SDK for Go API Reference_. 




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
    
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Partner Central

Amazon Redshift

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
