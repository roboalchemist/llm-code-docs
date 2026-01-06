# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_aurora_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_aurora_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

BasicsActions

# Aurora examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Aurora.

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Get started**

The following code examples show how to get started using Aurora.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/config"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    )
    
    // main uses the AWS SDK for Go V2 to create an Amazon Aurora client and list up to 20
    // DB clusters in your account.
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
    	auroraClient := rds.NewFromConfig(sdkConfig)
    	const maxClusters = 20
    	fmt.Printf("Let's list up to %v DB clusters.\n", maxClusters)
    	output, err := auroraClient.DescribeDBClusters(
    		ctx, &rds.DescribeDBClustersInput{MaxRecords: aws.Int32(maxClusters)})
    	if err != nil {
    		fmt.Printf("Couldn't list DB clusters: %v\n", err)
    		return
    	}
    	if len(output.DBClusters) == 0 {
    		fmt.Println("No DB clusters found.")
    	} else {
    		for _, cluster := range output.DBClusters {
    			fmt.Printf("DB cluster %v has database %v.\n", *cluster.DBClusterIdentifier,
    				*cluster.DatabaseName)
    		}
    	}
    }
    
    
    

  * For API details, see [DescribeDBClusters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusters) in _AWS SDK for Go API Reference_. 




###### Topics

  * Basics

  * Actions




## Basics

The following code example shows how to:

  * Create a custom Aurora DB cluster parameter group and set parameter values.

  * Create a DB cluster that uses the parameter group.

  * Create a DB instance that contains a database.

  * Take a snapshot of the DB cluster, then clean up resources.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 

Run an interactive scenario at a command prompt.
    
    
    import (
    	"aurora/actions"
    	"context"
    	"fmt"
    	"log"
    	"slices"
    	"sort"
    	"strconv"
    	"strings"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/google/uuid"
    )
    
    // GetStartedClusters is an interactive example that shows you how to use the AWS SDK for Go
    // with Amazon Aurora to do the following:
    //
    // 1. Create a custom DB cluster parameter group and set parameter values.
    // 2. Create an Aurora DB cluster that is configured to use the parameter group.
    // 3. Create a DB instance in the DB cluster that contains a database.
    // 4. Take a snapshot of the DB cluster.
    // 5. Delete the DB instance, DB cluster, and parameter group.
    type GetStartedClusters struct {
    	sdkConfig  aws.Config
    	dbClusters actions.DbClusters
    	questioner demotools.IQuestioner
    	helper     IScenarioHelper
    	isTestRun  bool
    }
    
    // NewGetStartedClusters constructs a GetStartedClusters instance from a configuration.
    // It uses the specified config to get an Amazon Relational Database Service (Amazon RDS)
    // client and create wrappers for the actions used in the scenario.
    func NewGetStartedClusters(sdkConfig aws.Config, questioner demotools.IQuestioner,
    	helper IScenarioHelper) GetStartedClusters {
    	auroraClient := rds.NewFromConfig(sdkConfig)
    	return GetStartedClusters{
    		sdkConfig:  sdkConfig,
    		dbClusters: actions.DbClusters{AuroraClient: auroraClient},
    		questioner: questioner,
    		helper:     helper,
    	}
    }
    
    // Run runs the interactive scenario.
    func (scenario GetStartedClusters) Run(ctx context.Context, dbEngine string, parameterGroupName string,
    	clusterName string, dbName string) {
    	defer func() {
    		if r := recover(); r != nil {
    			log.Println("Something went wrong with the demo.")
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon Aurora DB Cluster demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	parameterGroup := scenario.CreateParameterGroup(ctx, dbEngine, parameterGroupName)
    	scenario.SetUserParameters(ctx, parameterGroupName)
    	cluster := scenario.CreateCluster(ctx, clusterName, dbEngine, dbName, parameterGroup)
    	scenario.helper.Pause(5)
    	dbInstance := scenario.CreateInstance(ctx, cluster)
    	scenario.DisplayConnection(cluster)
    	scenario.CreateSnapshot(ctx, clusterName)
    	scenario.Cleanup(ctx, dbInstance, cluster, parameterGroup)
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // CreateParameterGroup shows how to get available engine versions for a specified
    // database engine and create a DB cluster parameter group that is compatible with a
    // selected engine family.
    func (scenario GetStartedClusters) CreateParameterGroup(ctx context.Context, dbEngine string,
    	parameterGroupName string) *types.DBClusterParameterGroup {
    
    	log.Printf("Checking for an existing DB cluster parameter group named %v.\n",
    		parameterGroupName)
    	parameterGroup, err := scenario.dbClusters.GetParameterGroup(ctx, parameterGroupName)
    	if err != nil {
    		panic(err)
    	}
    	if parameterGroup == nil {
    		log.Printf("Getting available database engine versions for %v.\n", dbEngine)
    		engineVersions, err := scenario.dbClusters.GetEngineVersions(ctx, dbEngine, "")
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
    		log.Println("Creating a DB cluster parameter group.")
    		_, err = scenario.dbClusters.CreateParameterGroup(
    			ctx, parameterGroupName, families[familyIndex], "Example parameter group.")
    		if err != nil {
    			panic(err)
    		}
    		parameterGroup, err = scenario.dbClusters.GetParameterGroup(ctx, parameterGroupName)
    		if err != nil {
    			panic(err)
    		}
    	}
    	log.Printf("Parameter group %v:\n", *parameterGroup.DBParameterGroupFamily)
    	log.Printf("\tName: %v\n", *parameterGroup.DBClusterParameterGroupName)
    	log.Printf("\tARN: %v\n", *parameterGroup.DBClusterParameterGroupArn)
    	log.Printf("\tFamily: %v\n", *parameterGroup.DBParameterGroupFamily)
    	log.Printf("\tDescription: %v\n", *parameterGroup.Description)
    	log.Println(strings.Repeat("-", 88))
    	return parameterGroup
    
    }
    
    // SetUserParameters shows how to get the parameters contained in a custom parameter
    // group and update some of the parameter values in the group.
    func (scenario GetStartedClusters) SetUserParameters(ctx context.Context, parameterGroupName string) {
    	log.Println("Let's set some parameter values in your parameter group.")
    	dbParameters, err := scenario.dbClusters.GetParameters(ctx, parameterGroupName, "")
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
    	err = scenario.dbClusters.UpdateParameters(ctx, parameterGroupName, updateParams)
    	if err != nil {
    		panic(err)
    	}
    	log.Println("You can get a list of parameters you've set by specifying a source of 'user'.")
    	userParameters, err := scenario.dbClusters.GetParameters(ctx, parameterGroupName, "user")
    	if err != nil {
    		panic(err)
    	}
    	log.Println("Here are the parameters you've set:")
    	for _, param := range userParameters {
    		log.Printf("\t%v: %v\n", *param.ParameterName, *param.ParameterValue)
    	}
    	log.Println(strings.Repeat("-", 88))
    }
    
    // CreateCluster shows how to create an Aurora DB cluster that contains a database
    // of a specified type. The database is also configured to use a custom DB cluster
    // parameter group.
    func (scenario GetStartedClusters) CreateCluster(ctx context.Context, clusterName string, dbEngine string,
    	dbName string, parameterGroup *types.DBClusterParameterGroup) *types.DBCluster {
    
    	log.Println("Checking for an existing DB cluster.")
    	cluster, err := scenario.dbClusters.GetDbCluster(ctx, clusterName)
    	if err != nil {
    		panic(err)
    	}
    	if cluster == nil {
    		adminUsername := scenario.questioner.Ask(
    			"Enter an administrator user name for the database: ", demotools.NotEmpty{})
    		adminPassword := scenario.questioner.Ask(
    			"Enter a password for the administrator (at least 8 characters): ", demotools.NotEmpty{})
    		engineVersions, err := scenario.dbClusters.GetEngineVersions(ctx, dbEngine, *parameterGroup.DBParameterGroupFamily)
    		if err != nil {
    			panic(err)
    		}
    		var engineChoices []string
    		for _, engine := range engineVersions {
    			engineChoices = append(engineChoices, *engine.EngineVersion)
    		}
    		log.Println("The available engines for your parameter group are:")
    		engineIndex := scenario.questioner.AskChoice("Which engine do you want to use?\n", engineChoices)
    		log.Printf("Creating DB cluster %v and database %v.\n", clusterName, dbName)
    		log.Printf("The DB cluster is configured to use\nyour custom parameter group %v\n",
    			*parameterGroup.DBClusterParameterGroupName)
    		log.Printf("and selected engine %v.\n", engineChoices[engineIndex])
    		log.Println("This typically takes several minutes.")
    		cluster, err = scenario.dbClusters.CreateDbCluster(
    			ctx, clusterName, *parameterGroup.DBClusterParameterGroupName, dbName, dbEngine,
    			engineChoices[engineIndex], adminUsername, adminPassword)
    		if err != nil {
    			panic(err)
    		}
    		for *cluster.Status != "available" {
    			scenario.helper.Pause(30)
    			cluster, err = scenario.dbClusters.GetDbCluster(ctx, clusterName)
    			if err != nil {
    				panic(err)
    			}
    			log.Println("Cluster created and available.")
    		}
    	}
    	log.Println("Cluster data:")
    	log.Printf("\tDBClusterIdentifier: %v\n", *cluster.DBClusterIdentifier)
    	log.Printf("\tARN: %v\n", *cluster.DBClusterArn)
    	log.Printf("\tStatus: %v\n", *cluster.Status)
    	log.Printf("\tEngine: %v\n", *cluster.Engine)
    	log.Printf("\tEngine version: %v\n", *cluster.EngineVersion)
    	log.Printf("\tDBClusterParameterGroup: %v\n", *cluster.DBClusterParameterGroup)
    	log.Printf("\tEngineMode: %v\n", *cluster.EngineMode)
    	log.Println(strings.Repeat("-", 88))
    	return cluster
    }
    
    // CreateInstance shows how to create a DB instance in an existing Aurora DB cluster.
    // A new DB cluster contains no DB instances, so you must add one. The first DB instance
    // that is added to a DB cluster defaults to a read-write DB instance.
    func (scenario GetStartedClusters) CreateInstance(ctx context.Context, cluster *types.DBCluster) *types.DBInstance {
    	log.Println("Checking for an existing database instance.")
    	dbInstance, err := scenario.dbClusters.GetInstance(ctx, *cluster.DBClusterIdentifier)
    	if err != nil {
    		panic(err)
    	}
    	if dbInstance == nil {
    		log.Println("Let's create a database instance in your DB cluster.")
    		log.Println("First, choose a DB instance type:")
    		instOpts, err := scenario.dbClusters.GetOrderableInstances(
    			ctx, *cluster.Engine, *cluster.EngineVersion)
    		if err != nil {
    			panic(err)
    		}
    		var instChoices []string
    		for _, opt := range instOpts {
    			instChoices = append(instChoices, *opt.DBInstanceClass)
    		}
    		slices.Sort(instChoices)
    		instChoices = slices.Compact(instChoices)
    		instIndex := scenario.questioner.AskChoice(
    			"Which DB instance class do you want to use?\n", instChoices)
    		log.Println("Creating a database instance. This typically takes several minutes.")
    		dbInstance, err = scenario.dbClusters.CreateInstanceInCluster(
    			ctx, *cluster.DBClusterIdentifier, *cluster.DBClusterIdentifier, *cluster.Engine,
    			instChoices[instIndex])
    		if err != nil {
    			panic(err)
    		}
    		for *dbInstance.DBInstanceStatus != "available" {
    			scenario.helper.Pause(30)
    			dbInstance, err = scenario.dbClusters.GetInstance(ctx, *cluster.DBClusterIdentifier)
    			if err != nil {
    				panic(err)
    			}
    		}
    	}
    	log.Println("Instance data:")
    	log.Printf("\tDBInstanceIdentifier: %v\n", *dbInstance.DBInstanceIdentifier)
    	log.Printf("\tARN: %v\n", *dbInstance.DBInstanceArn)
    	log.Printf("\tStatus: %v\n", *dbInstance.DBInstanceStatus)
    	log.Printf("\tEngine: %v\n", *dbInstance.Engine)
    	log.Printf("\tEngine version: %v\n", *dbInstance.EngineVersion)
    	log.Println(strings.Repeat("-", 88))
    	return dbInstance
    }
    
    // DisplayConnection displays connection information about an Aurora DB cluster and tips
    // on how to connect to it.
    func (scenario GetStartedClusters) DisplayConnection(cluster *types.DBCluster) {
    	log.Println(
    		"You can now connect to your database using your favorite MySql client.\n" +
    			"One way to connect is by using the 'mysql' shell on an Amazon EC2 instance\n" +
    			"that is running in the same VPC as your database cluster. Pass the endpoint,\n" +
    			"port, and administrator user name to 'mysql' and enter your password\n" +
    			"when prompted:")
    	log.Printf("\n\tmysql -h %v -P %v -u %v -p\n",
    		*cluster.Endpoint, *cluster.Port, *cluster.MasterUsername)
    	log.Println("For more information, see the User Guide for Aurora:\n" +
    		"\thttps://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html#CHAP_GettingStartedAurora.Aurora.Connect")
    	log.Println(strings.Repeat("-", 88))
    }
    
    // CreateSnapshot shows how to create a DB cluster snapshot and wait until it's available.
    func (scenario GetStartedClusters) CreateSnapshot(ctx context.Context, clusterName string) {
    	if scenario.questioner.AskBool(
    		"Do you want to create a snapshot of your DB cluster (y/n)? ", "y") {
    		snapshotId := fmt.Sprintf("%v-%v", clusterName, scenario.helper.UniqueId())
    		log.Printf("Creating a snapshot named %v. This typically takes a few minutes.\n", snapshotId)
    		snapshot, err := scenario.dbClusters.CreateClusterSnapshot(ctx, clusterName, snapshotId)
    		if err != nil {
    			panic(err)
    		}
    		for *snapshot.Status != "available" {
    			scenario.helper.Pause(30)
    			snapshot, err = scenario.dbClusters.GetClusterSnapshot(ctx, snapshotId)
    			if err != nil {
    				panic(err)
    			}
    		}
    		log.Println("Snapshot data:")
    		log.Printf("\tDBClusterSnapshotIdentifier: %v\n", *snapshot.DBClusterSnapshotIdentifier)
    		log.Printf("\tARN: %v\n", *snapshot.DBClusterSnapshotArn)
    		log.Printf("\tStatus: %v\n", *snapshot.Status)
    		log.Printf("\tEngine: %v\n", *snapshot.Engine)
    		log.Printf("\tEngine version: %v\n", *snapshot.EngineVersion)
    		log.Printf("\tDBClusterIdentifier: %v\n", *snapshot.DBClusterIdentifier)
    		log.Printf("\tSnapshotCreateTime: %v\n", *snapshot.SnapshotCreateTime)
    		log.Println(strings.Repeat("-", 88))
    	}
    }
    
    // Cleanup shows how to clean up a DB instance, DB cluster, and DB cluster parameter group.
    // Before the DB cluster parameter group can be deleted, all associated DB instances and
    // DB clusters must first be deleted.
    func (scenario GetStartedClusters) Cleanup(ctx context.Context, dbInstance *types.DBInstance, cluster *types.DBCluster,
    	parameterGroup *types.DBClusterParameterGroup) {
    
    	if scenario.questioner.AskBool(
    		"\nDo you want to delete the database instance, DB cluster, and parameter group (y/n)? ", "y") {
    		log.Printf("Deleting database instance %v.\n", *dbInstance.DBInstanceIdentifier)
    		err := scenario.dbClusters.DeleteInstance(ctx, *dbInstance.DBInstanceIdentifier)
    		if err != nil {
    			panic(err)
    		}
    		log.Printf("Deleting database cluster %v.\n", *cluster.DBClusterIdentifier)
    		err = scenario.dbClusters.DeleteDbCluster(ctx, *cluster.DBClusterIdentifier)
    		if err != nil {
    			panic(err)
    		}
    		log.Println(
    			"Waiting for the DB instance and DB cluster to delete. This typically takes several minutes.")
    		for dbInstance != nil || cluster != nil {
    			scenario.helper.Pause(30)
    			if dbInstance != nil {
    				dbInstance, err = scenario.dbClusters.GetInstance(ctx, *dbInstance.DBInstanceIdentifier)
    				if err != nil {
    					panic(err)
    				}
    			}
    			if cluster != nil {
    				cluster, err = scenario.dbClusters.GetDbCluster(ctx, *cluster.DBClusterIdentifier)
    				if err != nil {
    					panic(err)
    				}
    			}
    		}
    		log.Printf("Deleting parameter group %v.", *parameterGroup.DBClusterParameterGroupName)
    		err = scenario.dbClusters.DeleteParameterGroup(ctx, *parameterGroup.DBClusterParameterGroupName)
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
    
    
    

Define functions that are called by the scenario to manage Aurora actions.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    // GetParameterGroup gets a DB cluster parameter group by name.
    func (clusters *DbClusters) GetParameterGroup(ctx context.Context, parameterGroupName string) (
    	*types.DBClusterParameterGroup, error) {
    	output, err := clusters.AuroraClient.DescribeDBClusterParameterGroups(
    		ctx, &rds.DescribeDBClusterParameterGroupsInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
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
    		return &output.DBClusterParameterGroups[0], err
    	}
    }
    
    
    // CreateParameterGroup creates a DB cluster parameter group that is based on the specified
    // parameter group family.
    func (clusters *DbClusters) CreateParameterGroup(
    	ctx context.Context, parameterGroupName string, parameterGroupFamily string, description string) (
    	*types.DBClusterParameterGroup, error) {
    
    	output, err := clusters.AuroraClient.CreateDBClusterParameterGroup(ctx,
    		&rds.CreateDBClusterParameterGroupInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    			DBParameterGroupFamily:      aws.String(parameterGroupFamily),
    			Description:                 aws.String(description),
    		})
    	if err != nil {
    		log.Printf("Couldn't create parameter group %v: %v\n", parameterGroupName, err)
    		return nil, err
    	} else {
    		return output.DBClusterParameterGroup, err
    	}
    }
    
    
    
    // DeleteParameterGroup deletes the named DB cluster parameter group.
    func (clusters *DbClusters) DeleteParameterGroup(ctx context.Context, parameterGroupName string) error {
    	_, err := clusters.AuroraClient.DeleteDBClusterParameterGroup(ctx,
    		&rds.DeleteDBClusterParameterGroupInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    		})
    	if err != nil {
    		log.Printf("Couldn't delete parameter group %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    
    // GetParameters gets the parameters that are contained in a DB cluster parameter group.
    func (clusters *DbClusters) GetParameters(ctx context.Context, parameterGroupName string, source string) (
    	[]types.Parameter, error) {
    
    	var output *rds.DescribeDBClusterParametersOutput
    	var params []types.Parameter
    	var err error
    	parameterPaginator := rds.NewDescribeDBClusterParametersPaginator(clusters.AuroraClient,
    		&rds.DescribeDBClusterParametersInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    			Source:                      aws.String(source),
    		})
    	for parameterPaginator.HasMorePages() {
    		output, err = parameterPaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get paramaeters for %v: %v\n", parameterGroupName, err)
    			break
    		} else {
    			params = append(params, output.Parameters...)
    		}
    	}
    	return params, err
    }
    
    
    
    // UpdateParameters updates parameters in a named DB cluster parameter group.
    func (clusters *DbClusters) UpdateParameters(ctx context.Context, parameterGroupName string, params []types.Parameter) error {
    	_, err := clusters.AuroraClient.ModifyDBClusterParameterGroup(ctx,
    		&rds.ModifyDBClusterParameterGroupInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    			Parameters:                  params,
    		})
    	if err != nil {
    		log.Printf("Couldn't update parameters in %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    
    // GetDbCluster gets data about an Aurora DB cluster.
    func (clusters *DbClusters) GetDbCluster(ctx context.Context, clusterName string) (*types.DBCluster, error) {
    	output, err := clusters.AuroraClient.DescribeDBClusters(ctx,
    		&rds.DescribeDBClustersInput{
    			DBClusterIdentifier: aws.String(clusterName),
    		})
    	if err != nil {
    		var notFoundError *types.DBClusterNotFoundFault
    		if errors.As(err, &notFoundError) {
    			log.Printf("DB cluster %v does not exist.\n", clusterName)
    			err = nil
    		} else {
    			log.Printf("Couldn't get DB cluster %v: %v\n", clusterName, err)
    		}
    		return nil, err
    	} else {
    		return &output.DBClusters[0], err
    	}
    }
    
    
    
    // CreateDbCluster creates a DB cluster that is configured to use the specified parameter group.
    // The newly created DB cluster contains a database that uses the specified engine and
    // engine version.
    func (clusters *DbClusters) CreateDbCluster(ctx context.Context, clusterName string, parameterGroupName string,
    	dbName string, dbEngine string, dbEngineVersion string, adminName string, adminPassword string) (
    	*types.DBCluster, error) {
    
    	output, err := clusters.AuroraClient.CreateDBCluster(ctx, &rds.CreateDBClusterInput{
    		DBClusterIdentifier:         aws.String(clusterName),
    		Engine:                      aws.String(dbEngine),
    		DBClusterParameterGroupName: aws.String(parameterGroupName),
    		DatabaseName:                aws.String(dbName),
    		EngineVersion:               aws.String(dbEngineVersion),
    		MasterUserPassword:          aws.String(adminPassword),
    		MasterUsername:              aws.String(adminName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create DB cluster %v: %v\n", clusterName, err)
    		return nil, err
    	} else {
    		return output.DBCluster, err
    	}
    }
    
    
    
    // DeleteDbCluster deletes a DB cluster without keeping a final snapshot.
    func (clusters *DbClusters) DeleteDbCluster(ctx context.Context, clusterName string) error {
    	_, err := clusters.AuroraClient.DeleteDBCluster(ctx, &rds.DeleteDBClusterInput{
    		DBClusterIdentifier: aws.String(clusterName),
    		SkipFinalSnapshot:   aws.Bool(true),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete DB cluster %v: %v\n", clusterName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    
    // CreateClusterSnapshot creates a snapshot of a DB cluster.
    func (clusters *DbClusters) CreateClusterSnapshot(ctx context.Context, clusterName string, snapshotName string) (
    	*types.DBClusterSnapshot, error) {
    	output, err := clusters.AuroraClient.CreateDBClusterSnapshot(ctx, &rds.CreateDBClusterSnapshotInput{
    		DBClusterIdentifier:         aws.String(clusterName),
    		DBClusterSnapshotIdentifier: aws.String(snapshotName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return output.DBClusterSnapshot, nil
    	}
    }
    
    
    
    // GetClusterSnapshot gets a DB cluster snapshot.
    func (clusters *DbClusters) GetClusterSnapshot(ctx context.Context, snapshotName string) (*types.DBClusterSnapshot, error) {
    	output, err := clusters.AuroraClient.DescribeDBClusterSnapshots(ctx,
    		&rds.DescribeDBClusterSnapshotsInput{
    			DBClusterSnapshotIdentifier: aws.String(snapshotName),
    		})
    	if err != nil {
    		log.Printf("Couldn't get snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return &output.DBClusterSnapshots[0], nil
    	}
    }
    
    
    
    // CreateInstanceInCluster creates a database instance in an existing DB cluster. The first database that is
    // created defaults to a read-write DB instance.
    func (clusters *DbClusters) CreateInstanceInCluster(ctx context.Context, clusterName string, instanceName string,
    	dbEngine string, dbInstanceClass string) (*types.DBInstance, error) {
    	output, err := clusters.AuroraClient.CreateDBInstance(ctx, &rds.CreateDBInstanceInput{
    		DBInstanceIdentifier: aws.String(instanceName),
    		DBClusterIdentifier:  aws.String(clusterName),
    		Engine:               aws.String(dbEngine),
    		DBInstanceClass:      aws.String(dbInstanceClass),
    	})
    	if err != nil {
    		log.Printf("Couldn't create instance %v: %v\n", instanceName, err)
    		return nil, err
    	} else {
    		return output.DBInstance, nil
    	}
    }
    
    
    
    // GetInstance gets data about a DB instance.
    func (clusters *DbClusters) GetInstance(ctx context.Context, instanceName string) (
    	*types.DBInstance, error) {
    	output, err := clusters.AuroraClient.DescribeDBInstances(ctx,
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
    func (clusters *DbClusters) DeleteInstance(ctx context.Context, instanceName string) error {
    	_, err := clusters.AuroraClient.DeleteDBInstance(ctx, &rds.DeleteDBInstanceInput{
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
    func (clusters *DbClusters) GetEngineVersions(ctx context.Context, engine string, parameterGroupFamily string) (
    	[]types.DBEngineVersion, error) {
    	output, err := clusters.AuroraClient.DescribeDBEngineVersions(ctx,
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
    func (clusters *DbClusters) GetOrderableInstances(ctx context.Context, engine string, engineVersion string) (
    	[]types.OrderableDBInstanceOption, error) {
    
    	var output *rds.DescribeOrderableDBInstanceOptionsOutput
    	var instances []types.OrderableDBInstanceOption
    	var err error
    	orderablePaginator := rds.NewDescribeOrderableDBInstanceOptionsPaginator(clusters.AuroraClient,
    		&rds.DescribeOrderableDBInstanceOptionsInput{
    			Engine:        aws.String(engine),
    			EngineVersion: aws.String(engineVersion),
    		})
    	for orderablePaginator.HasMorePages() {
    		output, err = orderablePaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get orderable DB instances: %v\n", err)
    			break
    		} else {
    			instances = append(instances, output.OrderableDBInstanceOptions...)
    		}
    	}
    	return instances, err
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [CreateDBCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBCluster)

    * [CreateDBClusterParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBClusterParameterGroup)

    * [CreateDBClusterSnapshot](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBClusterSnapshot)

    * [CreateDBInstance](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBInstance)

    * [DeleteDBCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBCluster)

    * [DeleteDBClusterParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBClusterParameterGroup)

    * [DeleteDBInstance](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBInstance)

    * [DescribeDBClusterParameterGroups](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusterParameterGroups)

    * [DescribeDBClusterParameters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusterParameters)

    * [DescribeDBClusterSnapshots](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusterSnapshots)

    * [DescribeDBClusters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusters)

    * [DescribeDBEngineVersions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBEngineVersions)

    * [DescribeDBInstances](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBInstances)

    * [DescribeOrderableDBInstanceOptions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeOrderableDBInstanceOptions)

    * [ModifyDBClusterParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.ModifyDBClusterParameterGroup)




## Actions

The following code example shows how to use `CreateDBCluster`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // CreateDbCluster creates a DB cluster that is configured to use the specified parameter group.
    // The newly created DB cluster contains a database that uses the specified engine and
    // engine version.
    func (clusters *DbClusters) CreateDbCluster(ctx context.Context, clusterName string, parameterGroupName string,
    	dbName string, dbEngine string, dbEngineVersion string, adminName string, adminPassword string) (
    	*types.DBCluster, error) {
    
    	output, err := clusters.AuroraClient.CreateDBCluster(ctx, &rds.CreateDBClusterInput{
    		DBClusterIdentifier:         aws.String(clusterName),
    		Engine:                      aws.String(dbEngine),
    		DBClusterParameterGroupName: aws.String(parameterGroupName),
    		DatabaseName:                aws.String(dbName),
    		EngineVersion:               aws.String(dbEngineVersion),
    		MasterUserPassword:          aws.String(adminPassword),
    		MasterUsername:              aws.String(adminName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create DB cluster %v: %v\n", clusterName, err)
    		return nil, err
    	} else {
    		return output.DBCluster, err
    	}
    }
    
    
    

  * For API details, see [CreateDBCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBCluster) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateDBClusterParameterGroup`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // CreateParameterGroup creates a DB cluster parameter group that is based on the specified
    // parameter group family.
    func (clusters *DbClusters) CreateParameterGroup(
    	ctx context.Context, parameterGroupName string, parameterGroupFamily string, description string) (
    	*types.DBClusterParameterGroup, error) {
    
    	output, err := clusters.AuroraClient.CreateDBClusterParameterGroup(ctx,
    		&rds.CreateDBClusterParameterGroupInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    			DBParameterGroupFamily:      aws.String(parameterGroupFamily),
    			Description:                 aws.String(description),
    		})
    	if err != nil {
    		log.Printf("Couldn't create parameter group %v: %v\n", parameterGroupName, err)
    		return nil, err
    	} else {
    		return output.DBClusterParameterGroup, err
    	}
    }
    
    
    

  * For API details, see [CreateDBClusterParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBClusterParameterGroup) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateDBClusterSnapshot`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // CreateClusterSnapshot creates a snapshot of a DB cluster.
    func (clusters *DbClusters) CreateClusterSnapshot(ctx context.Context, clusterName string, snapshotName string) (
    	*types.DBClusterSnapshot, error) {
    	output, err := clusters.AuroraClient.CreateDBClusterSnapshot(ctx, &rds.CreateDBClusterSnapshotInput{
    		DBClusterIdentifier:         aws.String(clusterName),
    		DBClusterSnapshotIdentifier: aws.String(snapshotName),
    	})
    	if err != nil {
    		log.Printf("Couldn't create snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return output.DBClusterSnapshot, nil
    	}
    }
    
    
    

  * For API details, see [CreateDBClusterSnapshot](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBClusterSnapshot) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateDBInstance`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // CreateInstanceInCluster creates a database instance in an existing DB cluster. The first database that is
    // created defaults to a read-write DB instance.
    func (clusters *DbClusters) CreateInstanceInCluster(ctx context.Context, clusterName string, instanceName string,
    	dbEngine string, dbInstanceClass string) (*types.DBInstance, error) {
    	output, err := clusters.AuroraClient.CreateDBInstance(ctx, &rds.CreateDBInstanceInput{
    		DBInstanceIdentifier: aws.String(instanceName),
    		DBClusterIdentifier:  aws.String(clusterName),
    		Engine:               aws.String(dbEngine),
    		DBInstanceClass:      aws.String(dbInstanceClass),
    	})
    	if err != nil {
    		log.Printf("Couldn't create instance %v: %v\n", instanceName, err)
    		return nil, err
    	} else {
    		return output.DBInstance, nil
    	}
    }
    
    
    

  * For API details, see [CreateDBInstance](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.CreateDBInstance) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteDBCluster`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // DeleteDbCluster deletes a DB cluster without keeping a final snapshot.
    func (clusters *DbClusters) DeleteDbCluster(ctx context.Context, clusterName string) error {
    	_, err := clusters.AuroraClient.DeleteDBCluster(ctx, &rds.DeleteDBClusterInput{
    		DBClusterIdentifier: aws.String(clusterName),
    		SkipFinalSnapshot:   aws.Bool(true),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete DB cluster %v: %v\n", clusterName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    

  * For API details, see [DeleteDBCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBCluster) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteDBClusterParameterGroup`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // DeleteParameterGroup deletes the named DB cluster parameter group.
    func (clusters *DbClusters) DeleteParameterGroup(ctx context.Context, parameterGroupName string) error {
    	_, err := clusters.AuroraClient.DeleteDBClusterParameterGroup(ctx,
    		&rds.DeleteDBClusterParameterGroupInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    		})
    	if err != nil {
    		log.Printf("Couldn't delete parameter group %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    

  * For API details, see [DeleteDBClusterParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DeleteDBClusterParameterGroup) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteDBInstance`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // DeleteInstance deletes a DB instance.
    func (clusters *DbClusters) DeleteInstance(ctx context.Context, instanceName string) error {
    	_, err := clusters.AuroraClient.DeleteDBInstance(ctx, &rds.DeleteDBInstanceInput{
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




The following code example shows how to use `DescribeDBClusterParameterGroups`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // GetParameterGroup gets a DB cluster parameter group by name.
    func (clusters *DbClusters) GetParameterGroup(ctx context.Context, parameterGroupName string) (
    	*types.DBClusterParameterGroup, error) {
    	output, err := clusters.AuroraClient.DescribeDBClusterParameterGroups(
    		ctx, &rds.DescribeDBClusterParameterGroupsInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
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
    		return &output.DBClusterParameterGroups[0], err
    	}
    }
    
    
    

  * For API details, see [DescribeDBClusterParameterGroups](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusterParameterGroups) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBClusterParameters`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // GetParameters gets the parameters that are contained in a DB cluster parameter group.
    func (clusters *DbClusters) GetParameters(ctx context.Context, parameterGroupName string, source string) (
    	[]types.Parameter, error) {
    
    	var output *rds.DescribeDBClusterParametersOutput
    	var params []types.Parameter
    	var err error
    	parameterPaginator := rds.NewDescribeDBClusterParametersPaginator(clusters.AuroraClient,
    		&rds.DescribeDBClusterParametersInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    			Source:                      aws.String(source),
    		})
    	for parameterPaginator.HasMorePages() {
    		output, err = parameterPaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get paramaeters for %v: %v\n", parameterGroupName, err)
    			break
    		} else {
    			params = append(params, output.Parameters...)
    		}
    	}
    	return params, err
    }
    
    
    

  * For API details, see [DescribeDBClusterParameters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusterParameters) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBClusterSnapshots`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // GetClusterSnapshot gets a DB cluster snapshot.
    func (clusters *DbClusters) GetClusterSnapshot(ctx context.Context, snapshotName string) (*types.DBClusterSnapshot, error) {
    	output, err := clusters.AuroraClient.DescribeDBClusterSnapshots(ctx,
    		&rds.DescribeDBClusterSnapshotsInput{
    			DBClusterSnapshotIdentifier: aws.String(snapshotName),
    		})
    	if err != nil {
    		log.Printf("Couldn't get snapshot %v: %v\n", snapshotName, err)
    		return nil, err
    	} else {
    		return &output.DBClusterSnapshots[0], nil
    	}
    }
    
    
    

  * For API details, see [DescribeDBClusterSnapshots](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusterSnapshots) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBClusters`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // GetDbCluster gets data about an Aurora DB cluster.
    func (clusters *DbClusters) GetDbCluster(ctx context.Context, clusterName string) (*types.DBCluster, error) {
    	output, err := clusters.AuroraClient.DescribeDBClusters(ctx,
    		&rds.DescribeDBClustersInput{
    			DBClusterIdentifier: aws.String(clusterName),
    		})
    	if err != nil {
    		var notFoundError *types.DBClusterNotFoundFault
    		if errors.As(err, &notFoundError) {
    			log.Printf("DB cluster %v does not exist.\n", clusterName)
    			err = nil
    		} else {
    			log.Printf("Couldn't get DB cluster %v: %v\n", clusterName, err)
    		}
    		return nil, err
    	} else {
    		return &output.DBClusters[0], err
    	}
    }
    
    
    

  * For API details, see [DescribeDBClusters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeDBClusters) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeDBEngineVersions`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // GetEngineVersions gets database engine versions that are available for the specified engine
    // and parameter group family.
    func (clusters *DbClusters) GetEngineVersions(ctx context.Context, engine string, parameterGroupFamily string) (
    	[]types.DBEngineVersion, error) {
    	output, err := clusters.AuroraClient.DescribeDBEngineVersions(ctx,
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

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // GetInstance gets data about a DB instance.
    func (clusters *DbClusters) GetInstance(ctx context.Context, instanceName string) (
    	*types.DBInstance, error) {
    	output, err := clusters.AuroraClient.DescribeDBInstances(ctx,
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




The following code example shows how to use `DescribeOrderableDBInstanceOptions`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // GetOrderableInstances uses a paginator to get DB instance options that can be used to create DB instances that are
    // compatible with a set of specifications.
    func (clusters *DbClusters) GetOrderableInstances(ctx context.Context, engine string, engineVersion string) (
    	[]types.OrderableDBInstanceOption, error) {
    
    	var output *rds.DescribeOrderableDBInstanceOptionsOutput
    	var instances []types.OrderableDBInstanceOption
    	var err error
    	orderablePaginator := rds.NewDescribeOrderableDBInstanceOptionsPaginator(clusters.AuroraClient,
    		&rds.DescribeOrderableDBInstanceOptionsInput{
    			Engine:        aws.String(engine),
    			EngineVersion: aws.String(engineVersion),
    		})
    	for orderablePaginator.HasMorePages() {
    		output, err = orderablePaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't get orderable DB instances: %v\n", err)
    			break
    		} else {
    			instances = append(instances, output.OrderableDBInstanceOptions...)
    		}
    	}
    	return instances, err
    }
    
    
    

  * For API details, see [DescribeOrderableDBInstanceOptions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.DescribeOrderableDBInstanceOptions) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ModifyDBClusterParameterGroup`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/aurora#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/rds"
    	"github.com/aws/aws-sdk-go-v2/service/rds/types"
    )
    
    type DbClusters struct {
    	AuroraClient *rds.Client
    }
    
    
    
    // UpdateParameters updates parameters in a named DB cluster parameter group.
    func (clusters *DbClusters) UpdateParameters(ctx context.Context, parameterGroupName string, params []types.Parameter) error {
    	_, err := clusters.AuroraClient.ModifyDBClusterParameterGroup(ctx,
    		&rds.ModifyDBClusterParameterGroupInput{
    			DBClusterParameterGroupName: aws.String(parameterGroupName),
    			Parameters:                  params,
    		})
    	if err != nil {
    		log.Printf("Couldn't update parameters in %v: %v\n", parameterGroupName, err)
    		return err
    	} else {
    		return nil
    	}
    }
    
    
    

  * For API details, see [ModifyDBClusterParameterGroup](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/rds#Client.ModifyDBClusterParameterGroup) in _AWS SDK for Go API Reference_. 




![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

API Gateway

Amazon Bedrock

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
