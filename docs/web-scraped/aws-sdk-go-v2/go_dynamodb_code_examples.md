# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_dynamodb_code_examples.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#go_dynamodb_code_examples "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

BasicsActionsScenariosServerless examplesAWS community contributions

# DynamoDB examples using SDK for Go V2

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with DynamoDB.

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

_AWS community contributions_ are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

  * Basics

  * Actions

  * Scenarios

  * Serverless examples

  * AWS community contributions




## Basics

The following code example shows how to:

  * Create a table that can hold movie data.

  * Put, get, and update a single movie in the table.

  * Write movie data to the table from a sample JSON file.

  * Query for movies that were released in a given year.

  * Scan for movies that were released in a range of years.

  * Delete a movie from the table, then delete the table.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 

Run an interactive scenario to create the table and perform actions on it.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"strings"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/dynamodb/actions"
    )
    
    // RunMovieScenario is an interactive example that shows you how to use the AWS SDK for Go
    // to create and use an Amazon DynamoDB table that stores data about movies.
    //
    //  1. Create a table that can hold movie data.
    //  2. Put, get, and update a single movie in the table.
    //  3. Write movie data to the table from a sample JSON file.
    //  4. Query for movies that were released in a given year.
    //  5. Scan for movies that were released in a range of years.
    //  6. Delete a movie from the table.
    //  7. Delete the table.
    //
    // This example creates a DynamoDB service client from the specified sdkConfig so that
    // you can replace it with a mocked or stubbed config for unit testing.
    //
    // It uses a questioner from the `demotools` package to get input during the example.
    // This package can be found in the ..\..\demotools folder of this repo.
    //
    // The specified movie sampler is used to get sample data from a URL that is loaded
    // into the named table.
    func RunMovieScenario(
    	ctx context.Context, sdkConfig aws.Config, questioner demotools.IQuestioner, tableName string,
    	movieSampler actions.IMovieSampler) {
    	defer func() {
    		if r := recover(); r != nil {
    			fmt.Printf("Something went wrong with the demo.")
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon DynamoDB getting started demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	tableBasics := actions.TableBasics{TableName: tableName,
    		DynamoDbClient: dynamodb.NewFromConfig(sdkConfig)}
    
    	exists, err := tableBasics.TableExists(ctx)
    	if err != nil {
    		panic(err)
    	}
    	if !exists {
    		log.Printf("Creating table %v...\n", tableName)
    		_, err = tableBasics.CreateMovieTable(ctx)
    		if err != nil {
    			panic(err)
    		} else {
    			log.Printf("Created table %v.\n", tableName)
    		}
    	} else {
    		log.Printf("Table %v already exists.\n", tableName)
    	}
    
    	var customMovie actions.Movie
    	customMovie.Title = questioner.Ask("Enter a movie title to add to the table:",
    		demotools.NotEmpty{})
    	customMovie.Year = questioner.AskInt("What year was it released?",
    		demotools.NotEmpty{}, demotools.InIntRange{Lower: 1900, Upper: 2030})
    	customMovie.Info = map[string]interface{}{}
    	customMovie.Info["rating"] = questioner.AskFloat64(
    		"Enter a rating between 1 and 10:",
    		demotools.NotEmpty{}, demotools.InFloatRange{Lower: 1, Upper: 10})
    	customMovie.Info["plot"] = questioner.Ask("What's the plot? ",
    		demotools.NotEmpty{})
    	err = tableBasics.AddMovie(ctx, customMovie)
    	if err == nil {
    		log.Printf("Added %v to the movie table.\n", customMovie.Title)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Let's update your movie. You previously rated it %v.\n", customMovie.Info["rating"])
    	customMovie.Info["rating"] = questioner.AskFloat64(
    		"What new rating would you give it?",
    		demotools.NotEmpty{}, demotools.InFloatRange{Lower: 1, Upper: 10})
    	log.Printf("You summarized the plot as '%v'.\n", customMovie.Info["plot"])
    	customMovie.Info["plot"] = questioner.Ask("What would you say now?",
    		demotools.NotEmpty{})
    	attributes, err := tableBasics.UpdateMovie(ctx, customMovie)
    	if err == nil {
    		log.Printf("Updated %v with new values.\n", customMovie.Title)
    		for _, attVal := range attributes {
    			for valKey, val := range attVal {
    				log.Printf("\t%v: %v\n", valKey, val)
    			}
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Getting movie data from %v and adding 250 movies to the table...\n",
    		movieSampler.GetURL())
    	movies := movieSampler.GetSampleMovies()
    	written, err := tableBasics.AddMovieBatch(ctx, movies, 250)
    	if err != nil {
    		panic(err)
    	} else {
    		log.Printf("Added %v movies to the table.\n", written)
    	}
    
    	show := 10
    	if show > written {
    		show = written
    	}
    	log.Printf("The first %v movies in the table are:", show)
    	for index, movie := range movies[:show] {
    		log.Printf("\t%v. %v\n", index+1, movie.Title)
    	}
    	movieIndex := questioner.AskInt(
    		"Enter the number of a movie to get info about it: ",
    		demotools.InIntRange{Lower: 1, Upper: show},
    	)
    	movie, err := tableBasics.GetMovie(ctx, movies[movieIndex-1].Title, movies[movieIndex-1].Year)
    	if err == nil {
    		log.Println(movie)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Let's get a list of movies released in a given year.")
    	releaseYear := questioner.AskInt("Enter a year between 1972 and 2018: ",
    		demotools.InIntRange{Lower: 1972, Upper: 2018},
    	)
    	releases, err := tableBasics.Query(ctx, releaseYear)
    	if err == nil {
    		if len(releases) == 0 {
    			log.Printf("I couldn't find any movies released in %v!\n", releaseYear)
    		} else {
    			for _, movie = range releases {
    				log.Println(movie)
    			}
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Now let's scan for movies released in a range of years.")
    	startYear := questioner.AskInt("Enter a year: ",
    		demotools.InIntRange{Lower: 1972, Upper: 2018})
    	endYear := questioner.AskInt("Enter another year: ",
    		demotools.InIntRange{Lower: 1972, Upper: 2018})
    	releases, err = tableBasics.Scan(ctx, startYear, endYear)
    	if err == nil {
    		if len(releases) == 0 {
    			log.Printf("I couldn't find any movies released between %v and %v!\n", startYear, endYear)
    		} else {
    			log.Printf("Found %v movies. In this list, the plot is <nil> because "+
    				"we used a projection expression when scanning for items to return only "+
    				"the title, year, and rating.\n", len(releases))
    			for _, movie = range releases {
    				log.Println(movie)
    			}
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	var tables []string
    	if questioner.AskBool("Do you want to list all of your tables? (y/n) ", "y") {
    		tables, err = tableBasics.ListTables(ctx)
    		if err == nil {
    			log.Printf("Found %v tables:", len(tables))
    			for _, table := range tables {
    				log.Printf("\t%v", table)
    			}
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Let's remove your movie '%v'.\n", customMovie.Title)
    	if questioner.AskBool("Do you want to delete it from the table? (y/n) ", "y") {
    		err = tableBasics.DeleteMovie(ctx, customMovie)
    	}
    	if err == nil {
    		log.Printf("Deleted %v.\n", customMovie.Title)
    	}
    
    	if questioner.AskBool("Delete the table, too? (y/n)", "y") {
    		err = tableBasics.DeleteTable(ctx)
    	} else {
    		log.Println("Don't forget to delete the table when you're done or you might " +
    			"incur charges on your account.")
    	}
    	if err == nil {
    		log.Printf("Deleted table %v.\n", tableBasics.TableName)
    	}
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

Create a struct and methods that call DynamoDB actions.
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // TableExists determines whether a DynamoDB table exists.
    func (basics TableBasics) TableExists(ctx context.Context) (bool, error) {
    	exists := true
    	_, err := basics.DynamoDbClient.DescribeTable(
    		ctx, &dynamodb.DescribeTableInput{TableName: aws.String(basics.TableName)},
    	)
    	if err != nil {
    		var notFoundEx *types.ResourceNotFoundException
    		if errors.As(err, &notFoundEx) {
    			log.Printf("Table %v does not exist.\n", basics.TableName)
    			err = nil
    		} else {
    			log.Printf("Couldn't determine existence of table %v. Here's why: %v\n", basics.TableName, err)
    		}
    		exists = false
    	}
    	return exists, err
    }
    
    
    
    // CreateMovieTable creates a DynamoDB table with a composite primary key defined as
    // a string sort key named `title`, and a numeric partition key named `year`.
    // This function uses NewTableExistsWaiter to wait for the table to be created by
    // DynamoDB before it returns.
    func (basics TableBasics) CreateMovieTable(ctx context.Context) (*types.TableDescription, error) {
    	var tableDesc *types.TableDescription
    	table, err := basics.DynamoDbClient.CreateTable(ctx, &dynamodb.CreateTableInput{
    		AttributeDefinitions: []types.AttributeDefinition{{
    			AttributeName: aws.String("year"),
    			AttributeType: types.ScalarAttributeTypeN,
    		}, {
    			AttributeName: aws.String("title"),
    			AttributeType: types.ScalarAttributeTypeS,
    		}},
    		KeySchema: []types.KeySchemaElement{{
    			AttributeName: aws.String("year"),
    			KeyType:       types.KeyTypeHash,
    		}, {
    			AttributeName: aws.String("title"),
    			KeyType:       types.KeyTypeRange,
    		}},
    		TableName:   aws.String(basics.TableName),
    		BillingMode: types.BillingModePayPerRequest,
    	})
    	if err != nil {
    		log.Printf("Couldn't create table %v. Here's why: %v\n", basics.TableName, err)
    	} else {
    		waiter := dynamodb.NewTableExistsWaiter(basics.DynamoDbClient)
    		err = waiter.Wait(ctx, &dynamodb.DescribeTableInput{
    			TableName: aws.String(basics.TableName)}, 5*time.Minute)
    		if err != nil {
    			log.Printf("Wait for table exists failed. Here's why: %v\n", err)
    		}
    		tableDesc = table.TableDescription
    		log.Printf("Ccreating table test")
    	}
    	return tableDesc, err
    }
    
    
    
    // ListTables lists the DynamoDB table names for the current account.
    func (basics TableBasics) ListTables(ctx context.Context) ([]string, error) {
    	var tableNames []string
    	var output *dynamodb.ListTablesOutput
    	var err error
    	tablePaginator := dynamodb.NewListTablesPaginator(basics.DynamoDbClient, &dynamodb.ListTablesInput{})
    	for tablePaginator.HasMorePages() {
    		output, err = tablePaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't list tables. Here's why: %v\n", err)
    			break
    		} else {
    			tableNames = append(tableNames, output.TableNames...)
    		}
    	}
    	return tableNames, err
    }
    
    
    
    // AddMovie adds a movie the DynamoDB table.
    func (basics TableBasics) AddMovie(ctx context.Context, movie Movie) error {
    	item, err := attributevalue.MarshalMap(movie)
    	if err != nil {
    		panic(err)
    	}
    	_, err = basics.DynamoDbClient.PutItem(ctx, &dynamodb.PutItemInput{
    		TableName: aws.String(basics.TableName), Item: item,
    	})
    	if err != nil {
    		log.Printf("Couldn't add item to table. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    
    // UpdateMovie updates the rating and plot of a movie that already exists in the
    // DynamoDB table. This function uses the `expression` package to build the update
    // expression.
    func (basics TableBasics) UpdateMovie(ctx context.Context, movie Movie) (map[string]map[string]interface{}, error) {
    	var err error
    	var response *dynamodb.UpdateItemOutput
    	var attributeMap map[string]map[string]interface{}
    	update := expression.Set(expression.Name("info.rating"), expression.Value(movie.Info["rating"]))
    	update.Set(expression.Name("info.plot"), expression.Value(movie.Info["plot"]))
    	expr, err := expression.NewBuilder().WithUpdate(update).Build()
    	if err != nil {
    		log.Printf("Couldn't build expression for update. Here's why: %v\n", err)
    	} else {
    		response, err = basics.DynamoDbClient.UpdateItem(ctx, &dynamodb.UpdateItemInput{
    			TableName:                 aws.String(basics.TableName),
    			Key:                       movie.GetKey(),
    			ExpressionAttributeNames:  expr.Names(),
    			ExpressionAttributeValues: expr.Values(),
    			UpdateExpression:          expr.Update(),
    			ReturnValues:              types.ReturnValueUpdatedNew,
    		})
    		if err != nil {
    			log.Printf("Couldn't update movie %v. Here's why: %v\n", movie.Title, err)
    		} else {
    			err = attributevalue.UnmarshalMap(response.Attributes, &attributeMap)
    			if err != nil {
    				log.Printf("Couldn't unmarshall update response. Here's why: %v\n", err)
    			}
    		}
    	}
    	return attributeMap, err
    }
    
    
    
    // AddMovieBatch adds a slice of movies to the DynamoDB table. The function sends
    // batches of 25 movies to DynamoDB until all movies are added or it reaches the
    // specified maximum.
    func (basics TableBasics) AddMovieBatch(ctx context.Context, movies []Movie, maxMovies int) (int, error) {
    	var err error
    	var item map[string]types.AttributeValue
    	written := 0
    	batchSize := 25 // DynamoDB allows a maximum batch size of 25 items.
    	start := 0
    	end := start + batchSize
    	for start < maxMovies && start < len(movies) {
    		var writeReqs []types.WriteRequest
    		if end > len(movies) {
    			end = len(movies)
    		}
    		for _, movie := range movies[start:end] {
    			item, err = attributevalue.MarshalMap(movie)
    			if err != nil {
    				log.Printf("Couldn't marshal movie %v for batch writing. Here's why: %v\n", movie.Title, err)
    			} else {
    				writeReqs = append(
    					writeReqs,
    					types.WriteRequest{PutRequest: &types.PutRequest{Item: item}},
    				)
    			}
    		}
    		_, err = basics.DynamoDbClient.BatchWriteItem(ctx, &dynamodb.BatchWriteItemInput{
    			RequestItems: map[string][]types.WriteRequest{basics.TableName: writeReqs}})
    		if err != nil {
    			log.Printf("Couldn't add a batch of movies to %v. Here's why: %v\n", basics.TableName, err)
    		} else {
    			written += len(writeReqs)
    		}
    		start = end
    		end += batchSize
    	}
    
    	return written, err
    }
    
    
    
    // GetMovie gets movie data from the DynamoDB table by using the primary composite key
    // made of title and year.
    func (basics TableBasics) GetMovie(ctx context.Context, title string, year int) (Movie, error) {
    	movie := Movie{Title: title, Year: year}
    	response, err := basics.DynamoDbClient.GetItem(ctx, &dynamodb.GetItemInput{
    		Key: movie.GetKey(), TableName: aws.String(basics.TableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't get info about %v. Here's why: %v\n", title, err)
    	} else {
    		err = attributevalue.UnmarshalMap(response.Item, &movie)
    		if err != nil {
    			log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    		}
    	}
    	return movie, err
    }
    
    
    
    // Query gets all movies in the DynamoDB table that were released in the specified year.
    // The function uses the `expression` package to build the key condition expression
    // that is used in the query.
    func (basics TableBasics) Query(ctx context.Context, releaseYear int) ([]Movie, error) {
    	var err error
    	var response *dynamodb.QueryOutput
    	var movies []Movie
    	keyEx := expression.Key("year").Equal(expression.Value(releaseYear))
    	expr, err := expression.NewBuilder().WithKeyCondition(keyEx).Build()
    	if err != nil {
    		log.Printf("Couldn't build expression for query. Here's why: %v\n", err)
    	} else {
    		queryPaginator := dynamodb.NewQueryPaginator(basics.DynamoDbClient, &dynamodb.QueryInput{
    			TableName:                 aws.String(basics.TableName),
    			ExpressionAttributeNames:  expr.Names(),
    			ExpressionAttributeValues: expr.Values(),
    			KeyConditionExpression:    expr.KeyCondition(),
    		})
    		for queryPaginator.HasMorePages() {
    			response, err = queryPaginator.NextPage(ctx)
    			if err != nil {
    				log.Printf("Couldn't query for movies released in %v. Here's why: %v\n", releaseYear, err)
    				break
    			} else {
    				var moviePage []Movie
    				err = attributevalue.UnmarshalListOfMaps(response.Items, &moviePage)
    				if err != nil {
    					log.Printf("Couldn't unmarshal query response. Here's why: %v\n", err)
    					break
    				} else {
    					movies = append(movies, moviePage...)
    				}
    			}
    		}
    	}
    	return movies, err
    }
    
    
    
    // Scan gets all movies in the DynamoDB table that were released in a range of years
    // and projects them to return a reduced set of fields.
    // The function uses the `expression` package to build the filter and projection
    // expressions.
    func (basics TableBasics) Scan(ctx context.Context, startYear int, endYear int) ([]Movie, error) {
    	var movies []Movie
    	var err error
    	var response *dynamodb.ScanOutput
    	filtEx := expression.Name("year").Between(expression.Value(startYear), expression.Value(endYear))
    	projEx := expression.NamesList(
    		expression.Name("year"), expression.Name("title"), expression.Name("info.rating"))
    	expr, err := expression.NewBuilder().WithFilter(filtEx).WithProjection(projEx).Build()
    	if err != nil {
    		log.Printf("Couldn't build expressions for scan. Here's why: %v\n", err)
    	} else {
    		scanPaginator := dynamodb.NewScanPaginator(basics.DynamoDbClient, &dynamodb.ScanInput{
    			TableName:                 aws.String(basics.TableName),
    			ExpressionAttributeNames:  expr.Names(),
    			ExpressionAttributeValues: expr.Values(),
    			FilterExpression:          expr.Filter(),
    			ProjectionExpression:      expr.Projection(),
    		})
    		for scanPaginator.HasMorePages() {
    			response, err = scanPaginator.NextPage(ctx)
    			if err != nil {
    				log.Printf("Couldn't scan for movies released between %v and %v. Here's why: %v\n",
    					startYear, endYear, err)
    				break
    			} else {
    				var moviePage []Movie
    				err = attributevalue.UnmarshalListOfMaps(response.Items, &moviePage)
    				if err != nil {
    					log.Printf("Couldn't unmarshal query response. Here's why: %v\n", err)
    					break
    				} else {
    					movies = append(movies, moviePage...)
    				}
    			}
    		}
    	}
    	return movies, err
    }
    
    
    
    // DeleteMovie removes a movie from the DynamoDB table.
    func (basics TableBasics) DeleteMovie(ctx context.Context, movie Movie) error {
    	_, err := basics.DynamoDbClient.DeleteItem(ctx, &dynamodb.DeleteItemInput{
    		TableName: aws.String(basics.TableName), Key: movie.GetKey(),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete %v from the table. Here's why: %v\n", movie.Title, err)
    	}
    	return err
    }
    
    
    
    // DeleteTable deletes the DynamoDB table and all of its data.
    func (basics TableBasics) DeleteTable(ctx context.Context) error {
    	_, err := basics.DynamoDbClient.DeleteTable(ctx, &dynamodb.DeleteTableInput{
    		TableName: aws.String(basics.TableName)})
    	if err != nil {
    		log.Printf("Couldn't delete table %v. Here's why: %v\n", basics.TableName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see the following topics in _AWS SDK for Go API Reference_.

    * [BatchWriteItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.BatchWriteItem)

    * [CreateTable](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.CreateTable)

    * [DeleteItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.DeleteItem)

    * [DeleteTable](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.DeleteTable)

    * [DescribeTable](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.DescribeTable)

    * [GetItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.GetItem)

    * [PutItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.PutItem)

    * [Query](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.Query)

    * [Scan](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.Scan)

    * [UpdateItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.UpdateItem)




## Actions

The following code example shows how to use `BatchExecuteStatement`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 

Define a function receiver struct for the example.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // PartiQLRunner encapsulates the Amazon DynamoDB service actions used in the
    // PartiQL examples. It contains a DynamoDB service client that is used to act on the
    // specified table.
    type PartiQLRunner struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    

Use batches of INSERT statements to add items.
    
    
    // AddMovieBatch runs a batch of PartiQL INSERT statements to add multiple movies to the
    // DynamoDB table.
    func (runner PartiQLRunner) AddMovieBatch(ctx context.Context, movies []Movie) error {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year, movie.Info})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(fmt.Sprintf(
    				"INSERT INTO \"%v\" VALUE {'title': ?, 'year': ?, 'info': ?}", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	_, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	if err != nil {
    		log.Printf("Couldn't insert a batch of items with PartiQL. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    

Use batches of SELECT statements to get items.
    
    
    // GetMovieBatch runs a batch of PartiQL SELECT statements to get multiple movies from
    // the DynamoDB table by title and year.
    func (runner PartiQLRunner) GetMovieBatch(ctx context.Context, movies []Movie) ([]Movie, error) {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(
    				fmt.Sprintf("SELECT * FROM \"%v\" WHERE title=? AND year=?", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	output, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	var outMovies []Movie
    	if err != nil {
    		log.Printf("Couldn't get a batch of items with PartiQL. Here's why: %v\n", err)
    	} else {
    		for _, response := range output.Responses {
    			var movie Movie
    			err = attributevalue.UnmarshalMap(response.Item, &movie)
    			if err != nil {
    				log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    			} else {
    				outMovies = append(outMovies, movie)
    			}
    		}
    	}
    	return outMovies, err
    }
    
    
    

Use batches of UPDATE statements to update items.
    
    
    // UpdateMovieBatch runs a batch of PartiQL UPDATE statements to update the rating of
    // multiple movies that already exist in the DynamoDB table.
    func (runner PartiQLRunner) UpdateMovieBatch(ctx context.Context, movies []Movie, ratings []float64) error {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{ratings[index], movie.Title, movie.Year})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(
    				fmt.Sprintf("UPDATE \"%v\" SET info.rating=? WHERE title=? AND year=?", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	_, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	if err != nil {
    		log.Printf("Couldn't update the batch of movies. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    

Use batches of DELETE statements to delete items.
    
    
    // DeleteMovieBatch runs a batch of PartiQL DELETE statements to remove multiple movies
    // from the DynamoDB table.
    func (runner PartiQLRunner) DeleteMovieBatch(ctx context.Context, movies []Movie) error {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(
    				fmt.Sprintf("DELETE FROM \"%v\" WHERE title=? AND year=?", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	_, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	if err != nil {
    		log.Printf("Couldn't delete the batch of movies. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [BatchExecuteStatement](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.BatchExecuteStatement) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `BatchWriteItem`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // AddMovieBatch adds a slice of movies to the DynamoDB table. The function sends
    // batches of 25 movies to DynamoDB until all movies are added or it reaches the
    // specified maximum.
    func (basics TableBasics) AddMovieBatch(ctx context.Context, movies []Movie, maxMovies int) (int, error) {
    	var err error
    	var item map[string]types.AttributeValue
    	written := 0
    	batchSize := 25 // DynamoDB allows a maximum batch size of 25 items.
    	start := 0
    	end := start + batchSize
    	for start < maxMovies && start < len(movies) {
    		var writeReqs []types.WriteRequest
    		if end > len(movies) {
    			end = len(movies)
    		}
    		for _, movie := range movies[start:end] {
    			item, err = attributevalue.MarshalMap(movie)
    			if err != nil {
    				log.Printf("Couldn't marshal movie %v for batch writing. Here's why: %v\n", movie.Title, err)
    			} else {
    				writeReqs = append(
    					writeReqs,
    					types.WriteRequest{PutRequest: &types.PutRequest{Item: item}},
    				)
    			}
    		}
    		_, err = basics.DynamoDbClient.BatchWriteItem(ctx, &dynamodb.BatchWriteItemInput{
    			RequestItems: map[string][]types.WriteRequest{basics.TableName: writeReqs}})
    		if err != nil {
    			log.Printf("Couldn't add a batch of movies to %v. Here's why: %v\n", basics.TableName, err)
    		} else {
    			written += len(writeReqs)
    		}
    		start = end
    		end += batchSize
    	}
    
    	return written, err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [BatchWriteItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.BatchWriteItem) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `CreateTable`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // CreateMovieTable creates a DynamoDB table with a composite primary key defined as
    // a string sort key named `title`, and a numeric partition key named `year`.
    // This function uses NewTableExistsWaiter to wait for the table to be created by
    // DynamoDB before it returns.
    func (basics TableBasics) CreateMovieTable(ctx context.Context) (*types.TableDescription, error) {
    	var tableDesc *types.TableDescription
    	table, err := basics.DynamoDbClient.CreateTable(ctx, &dynamodb.CreateTableInput{
    		AttributeDefinitions: []types.AttributeDefinition{{
    			AttributeName: aws.String("year"),
    			AttributeType: types.ScalarAttributeTypeN,
    		}, {
    			AttributeName: aws.String("title"),
    			AttributeType: types.ScalarAttributeTypeS,
    		}},
    		KeySchema: []types.KeySchemaElement{{
    			AttributeName: aws.String("year"),
    			KeyType:       types.KeyTypeHash,
    		}, {
    			AttributeName: aws.String("title"),
    			KeyType:       types.KeyTypeRange,
    		}},
    		TableName:   aws.String(basics.TableName),
    		BillingMode: types.BillingModePayPerRequest,
    	})
    	if err != nil {
    		log.Printf("Couldn't create table %v. Here's why: %v\n", basics.TableName, err)
    	} else {
    		waiter := dynamodb.NewTableExistsWaiter(basics.DynamoDbClient)
    		err = waiter.Wait(ctx, &dynamodb.DescribeTableInput{
    			TableName: aws.String(basics.TableName)}, 5*time.Minute)
    		if err != nil {
    			log.Printf("Wait for table exists failed. Here's why: %v\n", err)
    		}
    		tableDesc = table.TableDescription
    		log.Printf("Ccreating table test")
    	}
    	return tableDesc, err
    }
    
    
    

  * For API details, see [CreateTable](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.CreateTable) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteItem`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // DeleteMovie removes a movie from the DynamoDB table.
    func (basics TableBasics) DeleteMovie(ctx context.Context, movie Movie) error {
    	_, err := basics.DynamoDbClient.DeleteItem(ctx, &dynamodb.DeleteItemInput{
    		TableName: aws.String(basics.TableName), Key: movie.GetKey(),
    	})
    	if err != nil {
    		log.Printf("Couldn't delete %v from the table. Here's why: %v\n", movie.Title, err)
    	}
    	return err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [DeleteItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.DeleteItem) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DeleteTable`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // DeleteTable deletes the DynamoDB table and all of its data.
    func (basics TableBasics) DeleteTable(ctx context.Context) error {
    	_, err := basics.DynamoDbClient.DeleteTable(ctx, &dynamodb.DeleteTableInput{
    		TableName: aws.String(basics.TableName)})
    	if err != nil {
    		log.Printf("Couldn't delete table %v. Here's why: %v\n", basics.TableName, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [DeleteTable](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.DeleteTable) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `DescribeTable`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // TableExists determines whether a DynamoDB table exists.
    func (basics TableBasics) TableExists(ctx context.Context) (bool, error) {
    	exists := true
    	_, err := basics.DynamoDbClient.DescribeTable(
    		ctx, &dynamodb.DescribeTableInput{TableName: aws.String(basics.TableName)},
    	)
    	if err != nil {
    		var notFoundEx *types.ResourceNotFoundException
    		if errors.As(err, &notFoundEx) {
    			log.Printf("Table %v does not exist.\n", basics.TableName)
    			err = nil
    		} else {
    			log.Printf("Couldn't determine existence of table %v. Here's why: %v\n", basics.TableName, err)
    		}
    		exists = false
    	}
    	return exists, err
    }
    
    
    

  * For API details, see [DescribeTable](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.DescribeTable) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ExecuteStatement`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 

Define a function receiver struct for the example.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // PartiQLRunner encapsulates the Amazon DynamoDB service actions used in the
    // PartiQL examples. It contains a DynamoDB service client that is used to act on the
    // specified table.
    type PartiQLRunner struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    

Use an INSERT statement to add an item.
    
    
    // AddMovie runs a PartiQL INSERT statement to add a movie to the DynamoDB table.
    func (runner PartiQLRunner) AddMovie(ctx context.Context, movie Movie) error {
    	params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year, movie.Info})
    	if err != nil {
    		panic(err)
    	}
    	_, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("INSERT INTO \"%v\" VALUE {'title': ?, 'year': ?, 'info': ?}",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't insert an item with PartiQL. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    

Use a SELECT statement to get an item.
    
    
    // GetMovie runs a PartiQL SELECT statement to get a movie from the DynamoDB table by
    // title and year.
    func (runner PartiQLRunner) GetMovie(ctx context.Context, title string, year int) (Movie, error) {
    	var movie Movie
    	params, err := attributevalue.MarshalList([]interface{}{title, year})
    	if err != nil {
    		panic(err)
    	}
    	response, err := runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("SELECT * FROM \"%v\" WHERE title=? AND year=?",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't get info about %v. Here's why: %v\n", title, err)
    	} else {
    		err = attributevalue.UnmarshalMap(response.Items[0], &movie)
    		if err != nil {
    			log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    		}
    	}
    	return movie, err
    }
    
    
    

Use a SELECT statement to get a list of items and project the results.
    
    
    // GetAllMovies runs a PartiQL SELECT statement to get all movies from the DynamoDB table.
    // pageSize is not typically required and is used to show how to paginate the results.
    // The results are projected to return only the title and rating of each movie.
    func (runner PartiQLRunner) GetAllMovies(ctx context.Context, pageSize int32) ([]map[string]interface{}, error) {
    	var output []map[string]interface{}
    	var response *dynamodb.ExecuteStatementOutput
    	var err error
    	var nextToken *string
    	for moreData := true; moreData; {
    		response, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    			Statement: aws.String(
    				fmt.Sprintf("SELECT title, info.rating FROM \"%v\"", runner.TableName)),
    			Limit:     aws.Int32(pageSize),
    			NextToken: nextToken,
    		})
    		if err != nil {
    			log.Printf("Couldn't get movies. Here's why: %v\n", err)
    			moreData = false
    		} else {
    			var pageOutput []map[string]interface{}
    			err = attributevalue.UnmarshalListOfMaps(response.Items, &pageOutput)
    			if err != nil {
    				log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    			} else {
    				log.Printf("Got a page of length %v.\n", len(response.Items))
    				output = append(output, pageOutput...)
    			}
    			nextToken = response.NextToken
    			moreData = nextToken != nil
    		}
    	}
    	return output, err
    }
    
    
    

Use an UPDATE statement to update an item.
    
    
    // UpdateMovie runs a PartiQL UPDATE statement to update the rating of a movie that
    // already exists in the DynamoDB table.
    func (runner PartiQLRunner) UpdateMovie(ctx context.Context, movie Movie, rating float64) error {
    	params, err := attributevalue.MarshalList([]interface{}{rating, movie.Title, movie.Year})
    	if err != nil {
    		panic(err)
    	}
    	_, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("UPDATE \"%v\" SET info.rating=? WHERE title=? AND year=?",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't update movie %v. Here's why: %v\n", movie.Title, err)
    	}
    	return err
    }
    
    
    

Use a DELETE statement to delete an item.
    
    
    // DeleteMovie runs a PartiQL DELETE statement to remove a movie from the DynamoDB table.
    func (runner PartiQLRunner) DeleteMovie(ctx context.Context, movie Movie) error {
    	params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year})
    	if err != nil {
    		panic(err)
    	}
    	_, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("DELETE FROM \"%v\" WHERE title=? AND year=?",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't delete %v from the table. Here's why: %v\n", movie.Title, err)
    	}
    	return err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [ExecuteStatement](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.ExecuteStatement) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `GetItem`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // GetMovie gets movie data from the DynamoDB table by using the primary composite key
    // made of title and year.
    func (basics TableBasics) GetMovie(ctx context.Context, title string, year int) (Movie, error) {
    	movie := Movie{Title: title, Year: year}
    	response, err := basics.DynamoDbClient.GetItem(ctx, &dynamodb.GetItemInput{
    		Key: movie.GetKey(), TableName: aws.String(basics.TableName),
    	})
    	if err != nil {
    		log.Printf("Couldn't get info about %v. Here's why: %v\n", title, err)
    	} else {
    		err = attributevalue.UnmarshalMap(response.Item, &movie)
    		if err != nil {
    			log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    		}
    	}
    	return movie, err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [GetItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.GetItem) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `ListTables`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // ListTables lists the DynamoDB table names for the current account.
    func (basics TableBasics) ListTables(ctx context.Context) ([]string, error) {
    	var tableNames []string
    	var output *dynamodb.ListTablesOutput
    	var err error
    	tablePaginator := dynamodb.NewListTablesPaginator(basics.DynamoDbClient, &dynamodb.ListTablesInput{})
    	for tablePaginator.HasMorePages() {
    		output, err = tablePaginator.NextPage(ctx)
    		if err != nil {
    			log.Printf("Couldn't list tables. Here's why: %v\n", err)
    			break
    		} else {
    			tableNames = append(tableNames, output.TableNames...)
    		}
    	}
    	return tableNames, err
    }
    
    
    

  * For API details, see [ListTables](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.ListTables) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `PutItem`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // AddMovie adds a movie the DynamoDB table.
    func (basics TableBasics) AddMovie(ctx context.Context, movie Movie) error {
    	item, err := attributevalue.MarshalMap(movie)
    	if err != nil {
    		panic(err)
    	}
    	_, err = basics.DynamoDbClient.PutItem(ctx, &dynamodb.PutItemInput{
    		TableName: aws.String(basics.TableName), Item: item,
    	})
    	if err != nil {
    		log.Printf("Couldn't add item to table. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [PutItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.PutItem) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `Query`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // Query gets all movies in the DynamoDB table that were released in the specified year.
    // The function uses the `expression` package to build the key condition expression
    // that is used in the query.
    func (basics TableBasics) Query(ctx context.Context, releaseYear int) ([]Movie, error) {
    	var err error
    	var response *dynamodb.QueryOutput
    	var movies []Movie
    	keyEx := expression.Key("year").Equal(expression.Value(releaseYear))
    	expr, err := expression.NewBuilder().WithKeyCondition(keyEx).Build()
    	if err != nil {
    		log.Printf("Couldn't build expression for query. Here's why: %v\n", err)
    	} else {
    		queryPaginator := dynamodb.NewQueryPaginator(basics.DynamoDbClient, &dynamodb.QueryInput{
    			TableName:                 aws.String(basics.TableName),
    			ExpressionAttributeNames:  expr.Names(),
    			ExpressionAttributeValues: expr.Values(),
    			KeyConditionExpression:    expr.KeyCondition(),
    		})
    		for queryPaginator.HasMorePages() {
    			response, err = queryPaginator.NextPage(ctx)
    			if err != nil {
    				log.Printf("Couldn't query for movies released in %v. Here's why: %v\n", releaseYear, err)
    				break
    			} else {
    				var moviePage []Movie
    				err = attributevalue.UnmarshalListOfMaps(response.Items, &moviePage)
    				if err != nil {
    					log.Printf("Couldn't unmarshal query response. Here's why: %v\n", err)
    					break
    				} else {
    					movies = append(movies, moviePage...)
    				}
    			}
    		}
    	}
    	return movies, err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [Query](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.Query) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `Scan`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // Scan gets all movies in the DynamoDB table that were released in a range of years
    // and projects them to return a reduced set of fields.
    // The function uses the `expression` package to build the filter and projection
    // expressions.
    func (basics TableBasics) Scan(ctx context.Context, startYear int, endYear int) ([]Movie, error) {
    	var movies []Movie
    	var err error
    	var response *dynamodb.ScanOutput
    	filtEx := expression.Name("year").Between(expression.Value(startYear), expression.Value(endYear))
    	projEx := expression.NamesList(
    		expression.Name("year"), expression.Name("title"), expression.Name("info.rating"))
    	expr, err := expression.NewBuilder().WithFilter(filtEx).WithProjection(projEx).Build()
    	if err != nil {
    		log.Printf("Couldn't build expressions for scan. Here's why: %v\n", err)
    	} else {
    		scanPaginator := dynamodb.NewScanPaginator(basics.DynamoDbClient, &dynamodb.ScanInput{
    			TableName:                 aws.String(basics.TableName),
    			ExpressionAttributeNames:  expr.Names(),
    			ExpressionAttributeValues: expr.Values(),
    			FilterExpression:          expr.Filter(),
    			ProjectionExpression:      expr.Projection(),
    		})
    		for scanPaginator.HasMorePages() {
    			response, err = scanPaginator.NextPage(ctx)
    			if err != nil {
    				log.Printf("Couldn't scan for movies released between %v and %v. Here's why: %v\n",
    					startYear, endYear, err)
    				break
    			} else {
    				var moviePage []Movie
    				err = attributevalue.UnmarshalListOfMaps(response.Items, &moviePage)
    				if err != nil {
    					log.Printf("Couldn't unmarshal query response. Here's why: %v\n", err)
    					break
    				} else {
    					movies = append(movies, moviePage...)
    				}
    			}
    		}
    	}
    	return movies, err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [Scan](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.Scan) in _AWS SDK for Go API Reference_. 




The following code example shows how to use `UpdateItem`.

**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 
    
    
    import (
    	"context"
    	"errors"
    	"log"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // TableBasics encapsulates the Amazon DynamoDB service actions used in the examples.
    // It contains a DynamoDB service client that is used to act on the specified table.
    type TableBasics struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // UpdateMovie updates the rating and plot of a movie that already exists in the
    // DynamoDB table. This function uses the `expression` package to build the update
    // expression.
    func (basics TableBasics) UpdateMovie(ctx context.Context, movie Movie) (map[string]map[string]interface{}, error) {
    	var err error
    	var response *dynamodb.UpdateItemOutput
    	var attributeMap map[string]map[string]interface{}
    	update := expression.Set(expression.Name("info.rating"), expression.Value(movie.Info["rating"]))
    	update.Set(expression.Name("info.plot"), expression.Value(movie.Info["plot"]))
    	expr, err := expression.NewBuilder().WithUpdate(update).Build()
    	if err != nil {
    		log.Printf("Couldn't build expression for update. Here's why: %v\n", err)
    	} else {
    		response, err = basics.DynamoDbClient.UpdateItem(ctx, &dynamodb.UpdateItemInput{
    			TableName:                 aws.String(basics.TableName),
    			Key:                       movie.GetKey(),
    			ExpressionAttributeNames:  expr.Names(),
    			ExpressionAttributeValues: expr.Values(),
    			UpdateExpression:          expr.Update(),
    			ReturnValues:              types.ReturnValueUpdatedNew,
    		})
    		if err != nil {
    			log.Printf("Couldn't update movie %v. Here's why: %v\n", movie.Title, err)
    		} else {
    			err = attributevalue.UnmarshalMap(response.Attributes, &attributeMap)
    			if err != nil {
    				log.Printf("Couldn't unmarshall update response. Here's why: %v\n", err)
    			}
    		}
    	}
    	return attributeMap, err
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

  * For API details, see [UpdateItem](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.UpdateItem) in _AWS SDK for Go API Reference_. 




## Scenarios

The following code example shows how to:

  * Get a batch of items by running multiple SELECT statements.

  * Add a batch of items by running multiple INSERT statements.

  * Update a batch of items by running multiple UPDATE statements.

  * Delete a batch of items by running multiple DELETE statements.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 

Run a scenario that creates a table and runs batches of PartiQL queries.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"strings"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/dynamodb/actions"
    )
    
    // RunPartiQLBatchScenario shows you how to use the AWS SDK for Go
    // to run batches of PartiQL statements to query a table that stores data about movies.
    //
    //   - Use batches of PartiQL statements to add, get, update, and delete data for
    //     individual movies.
    //
    // This example creates an Amazon DynamoDB service client from the specified sdkConfig so that
    // you can replace it with a mocked or stubbed config for unit testing.
    //
    // This example creates and deletes a DynamoDB table to use during the scenario.
    func RunPartiQLBatchScenario(ctx context.Context, sdkConfig aws.Config, tableName string) {
    	defer func() {
    		if r := recover(); r != nil {
    			fmt.Printf("Something went wrong with the demo.")
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon DynamoDB PartiQL batch demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	tableBasics := actions.TableBasics{
    		DynamoDbClient: dynamodb.NewFromConfig(sdkConfig),
    		TableName:      tableName,
    	}
    	runner := actions.PartiQLRunner{
    		DynamoDbClient: dynamodb.NewFromConfig(sdkConfig),
    		TableName:      tableName,
    	}
    
    	exists, err := tableBasics.TableExists(ctx)
    	if err != nil {
    		panic(err)
    	}
    	if !exists {
    		log.Printf("Creating table %v...\n", tableName)
    		_, err = tableBasics.CreateMovieTable(ctx)
    		if err != nil {
    			panic(err)
    		} else {
    			log.Printf("Created table %v.\n", tableName)
    		}
    	} else {
    		log.Printf("Table %v already exists.\n", tableName)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	currentYear, _, _ := time.Now().Date()
    	customMovies := []actions.Movie{{
    		Title: "House PartiQL",
    		Year:  currentYear - 5,
    		Info: map[string]interface{}{
    			"plot":   "Wacky high jinks result from querying a mysterious database.",
    			"rating": 8.5}}, {
    		Title: "House PartiQL 2",
    		Year:  currentYear - 3,
    		Info: map[string]interface{}{
    			"plot":   "Moderate high jinks result from querying another mysterious database.",
    			"rating": 6.5}}, {
    		Title: "House PartiQL 3",
    		Year:  currentYear - 1,
    		Info: map[string]interface{}{
    			"plot":   "Tepid high jinks result from querying yet another mysterious database.",
    			"rating": 2.5},
    	},
    	}
    
    	log.Printf("Inserting a batch of movies into table '%v'.\n", tableName)
    	err = runner.AddMovieBatch(ctx, customMovies)
    	if err == nil {
    		log.Printf("Added %v movies to the table.\n", len(customMovies))
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Getting data for a batch of movies.")
    	movies, err := runner.GetMovieBatch(ctx, customMovies)
    	if err == nil {
    		for _, movie := range movies {
    			log.Println(movie)
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	newRatings := []float64{7.7, 4.4, 1.1}
    	log.Println("Updating a batch of movies with new ratings.")
    	err = runner.UpdateMovieBatch(ctx, customMovies, newRatings)
    	if err == nil {
    		log.Printf("Updated %v movies with new ratings.\n", len(customMovies))
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Getting projected data from the table to verify our update.")
    	log.Println("Using a page size of 2 to demonstrate paging.")
    	projections, err := runner.GetAllMovies(ctx, 2)
    	if err == nil {
    		log.Println("All movies:")
    		for _, projection := range projections {
    			log.Println(projection)
    		}
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Println("Deleting a batch of movies.")
    	err = runner.DeleteMovieBatch(ctx, customMovies)
    	if err == nil {
    		log.Printf("Deleted %v movies.\n", len(customMovies))
    	}
    
    	err = tableBasics.DeleteTable(ctx)
    	if err == nil {
    		log.Printf("Deleted table %v.\n", tableBasics.TableName)
    	}
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

Create a struct and methods that run PartiQL statements.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // PartiQLRunner encapsulates the Amazon DynamoDB service actions used in the
    // PartiQL examples. It contains a DynamoDB service client that is used to act on the
    // specified table.
    type PartiQLRunner struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // AddMovieBatch runs a batch of PartiQL INSERT statements to add multiple movies to the
    // DynamoDB table.
    func (runner PartiQLRunner) AddMovieBatch(ctx context.Context, movies []Movie) error {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year, movie.Info})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(fmt.Sprintf(
    				"INSERT INTO \"%v\" VALUE {'title': ?, 'year': ?, 'info': ?}", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	_, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	if err != nil {
    		log.Printf("Couldn't insert a batch of items with PartiQL. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    
    // GetMovieBatch runs a batch of PartiQL SELECT statements to get multiple movies from
    // the DynamoDB table by title and year.
    func (runner PartiQLRunner) GetMovieBatch(ctx context.Context, movies []Movie) ([]Movie, error) {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(
    				fmt.Sprintf("SELECT * FROM \"%v\" WHERE title=? AND year=?", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	output, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	var outMovies []Movie
    	if err != nil {
    		log.Printf("Couldn't get a batch of items with PartiQL. Here's why: %v\n", err)
    	} else {
    		for _, response := range output.Responses {
    			var movie Movie
    			err = attributevalue.UnmarshalMap(response.Item, &movie)
    			if err != nil {
    				log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    			} else {
    				outMovies = append(outMovies, movie)
    			}
    		}
    	}
    	return outMovies, err
    }
    
    
    
    // GetAllMovies runs a PartiQL SELECT statement to get all movies from the DynamoDB table.
    // pageSize is not typically required and is used to show how to paginate the results.
    // The results are projected to return only the title and rating of each movie.
    func (runner PartiQLRunner) GetAllMovies(ctx context.Context, pageSize int32) ([]map[string]interface{}, error) {
    	var output []map[string]interface{}
    	var response *dynamodb.ExecuteStatementOutput
    	var err error
    	var nextToken *string
    	for moreData := true; moreData; {
    		response, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    			Statement: aws.String(
    				fmt.Sprintf("SELECT title, info.rating FROM \"%v\"", runner.TableName)),
    			Limit:     aws.Int32(pageSize),
    			NextToken: nextToken,
    		})
    		if err != nil {
    			log.Printf("Couldn't get movies. Here's why: %v\n", err)
    			moreData = false
    		} else {
    			var pageOutput []map[string]interface{}
    			err = attributevalue.UnmarshalListOfMaps(response.Items, &pageOutput)
    			if err != nil {
    				log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    			} else {
    				log.Printf("Got a page of length %v.\n", len(response.Items))
    				output = append(output, pageOutput...)
    			}
    			nextToken = response.NextToken
    			moreData = nextToken != nil
    		}
    	}
    	return output, err
    }
    
    
    
    // UpdateMovieBatch runs a batch of PartiQL UPDATE statements to update the rating of
    // multiple movies that already exist in the DynamoDB table.
    func (runner PartiQLRunner) UpdateMovieBatch(ctx context.Context, movies []Movie, ratings []float64) error {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{ratings[index], movie.Title, movie.Year})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(
    				fmt.Sprintf("UPDATE \"%v\" SET info.rating=? WHERE title=? AND year=?", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	_, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	if err != nil {
    		log.Printf("Couldn't update the batch of movies. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    
    // DeleteMovieBatch runs a batch of PartiQL DELETE statements to remove multiple movies
    // from the DynamoDB table.
    func (runner PartiQLRunner) DeleteMovieBatch(ctx context.Context, movies []Movie) error {
    	statementRequests := make([]types.BatchStatementRequest, len(movies))
    	for index, movie := range movies {
    		params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year})
    		if err != nil {
    			panic(err)
    		}
    		statementRequests[index] = types.BatchStatementRequest{
    			Statement: aws.String(
    				fmt.Sprintf("DELETE FROM \"%v\" WHERE title=? AND year=?", runner.TableName)),
    			Parameters: params,
    		}
    	}
    
    	_, err := runner.DynamoDbClient.BatchExecuteStatement(ctx, &dynamodb.BatchExecuteStatementInput{
    		Statements: statementRequests,
    	})
    	if err != nil {
    		log.Printf("Couldn't delete the batch of movies. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    

  * For API details, see [BatchExecuteStatement](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.BatchExecuteStatement) in _AWS SDK for Go API Reference_. 




The following code example shows how to:

  * Get an item by running a SELECT statement.

  * Add an item by running an INSERT statement.

  * Update an item by running an UPDATE statement.

  * Delete an item by running a DELETE statement.




**SDK for Go V2**
    

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/dynamodb#code-examples). 

Run a scenario that creates a table and runs PartiQL queries.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"strings"
    	"time"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/awsdocs/aws-doc-sdk-examples/gov2/dynamodb/actions"
    )
    
    // RunPartiQLSingleScenario shows you how to use the AWS SDK for Go
    // to use PartiQL to query a table that stores data about movies.
    //
    // * Use PartiQL statements to add, get, update, and delete data for individual movies.
    //
    // This example creates an Amazon DynamoDB service client from the specified sdkConfig so that
    // you can replace it with a mocked or stubbed config for unit testing.
    //
    // This example creates and deletes a DynamoDB table to use during the scenario.
    func RunPartiQLSingleScenario(ctx context.Context, sdkConfig aws.Config, tableName string) {
    	defer func() {
    		if r := recover(); r != nil {
    			fmt.Printf("Something went wrong with the demo.")
    		}
    	}()
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Welcome to the Amazon DynamoDB PartiQL single action demo.")
    	log.Println(strings.Repeat("-", 88))
    
    	tableBasics := actions.TableBasics{
    		DynamoDbClient: dynamodb.NewFromConfig(sdkConfig),
    		TableName:      tableName,
    	}
    	runner := actions.PartiQLRunner{
    		DynamoDbClient: dynamodb.NewFromConfig(sdkConfig),
    		TableName:      tableName,
    	}
    
    	exists, err := tableBasics.TableExists(ctx)
    	if err != nil {
    		panic(err)
    	}
    	if !exists {
    		log.Printf("Creating table %v...\n", tableName)
    		_, err = tableBasics.CreateMovieTable(ctx)
    		if err != nil {
    			panic(err)
    		} else {
    			log.Printf("Created table %v.\n", tableName)
    		}
    	} else {
    		log.Printf("Table %v already exists.\n", tableName)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	currentYear, _, _ := time.Now().Date()
    	customMovie := actions.Movie{
    		Title: "24 Hour PartiQL People",
    		Year:  currentYear,
    		Info: map[string]interface{}{
    			"plot":   "A group of data developers discover a new query language they can't stop using.",
    			"rating": 9.9,
    		},
    	}
    
    	log.Printf("Inserting movie '%v' released in %v.", customMovie.Title, customMovie.Year)
    	err = runner.AddMovie(ctx, customMovie)
    	if err == nil {
    		log.Printf("Added %v to the movie table.\n", customMovie.Title)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Getting data for movie '%v' released in %v.", customMovie.Title, customMovie.Year)
    	movie, err := runner.GetMovie(ctx, customMovie.Title, customMovie.Year)
    	if err == nil {
    		log.Println(movie)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	newRating := 6.6
    	log.Printf("Updating movie '%v' with a rating of %v.", customMovie.Title, newRating)
    	err = runner.UpdateMovie(ctx, customMovie, newRating)
    	if err == nil {
    		log.Printf("Updated %v with a new rating.\n", customMovie.Title)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Getting data again to verify the update.")
    	movie, err = runner.GetMovie(ctx, customMovie.Title, customMovie.Year)
    	if err == nil {
    		log.Println(movie)
    	}
    	log.Println(strings.Repeat("-", 88))
    
    	log.Printf("Deleting movie '%v'.\n", customMovie.Title)
    	err = runner.DeleteMovie(ctx, customMovie)
    	if err == nil {
    		log.Printf("Deleted %v.\n", customMovie.Title)
    	}
    
    	err = tableBasics.DeleteTable(ctx)
    	if err == nil {
    		log.Printf("Deleted table %v.\n", tableBasics.TableName)
    	}
    
    	log.Println(strings.Repeat("-", 88))
    	log.Println("Thanks for watching!")
    	log.Println(strings.Repeat("-", 88))
    }
    
    
    

Define a Movie struct that is used in this example.
    
    
    import (
    	"archive/zip"
    	"bytes"
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // Movie encapsulates data about a movie. Title and Year are the composite primary key
    // of the movie in Amazon DynamoDB. Title is the sort key, Year is the partition key,
    // and Info is additional data.
    type Movie struct {
    	Title string                 `dynamodbav:"title"`
    	Year  int                    `dynamodbav:"year"`
    	Info  map[string]interface{} `dynamodbav:"info"`
    }
    
    // GetKey returns the composite primary key of the movie in a format that can be
    // sent to DynamoDB.
    func (movie Movie) GetKey() map[string]types.AttributeValue {
    	title, err := attributevalue.Marshal(movie.Title)
    	if err != nil {
    		panic(err)
    	}
    	year, err := attributevalue.Marshal(movie.Year)
    	if err != nil {
    		panic(err)
    	}
    	return map[string]types.AttributeValue{"title": title, "year": year}
    }
    
    // String returns the title, year, rating, and plot of a movie, formatted for the example.
    func (movie Movie) String() string {
    	return fmt.Sprintf("%v\n\tReleased: %v\n\tRating: %v\n\tPlot: %v\n",
    		movie.Title, movie.Year, movie.Info["rating"], movie.Info["plot"])
    }
    
    
    

Create a struct and methods that run PartiQL statements.
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/aws/aws-sdk-go-v2/aws"
    	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
    	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
    )
    
    // PartiQLRunner encapsulates the Amazon DynamoDB service actions used in the
    // PartiQL examples. It contains a DynamoDB service client that is used to act on the
    // specified table.
    type PartiQLRunner struct {
    	DynamoDbClient *dynamodb.Client
    	TableName      string
    }
    
    
    
    // AddMovie runs a PartiQL INSERT statement to add a movie to the DynamoDB table.
    func (runner PartiQLRunner) AddMovie(ctx context.Context, movie Movie) error {
    	params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year, movie.Info})
    	if err != nil {
    		panic(err)
    	}
    	_, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("INSERT INTO \"%v\" VALUE {'title': ?, 'year': ?, 'info': ?}",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't insert an item with PartiQL. Here's why: %v\n", err)
    	}
    	return err
    }
    
    
    
    // GetMovie runs a PartiQL SELECT statement to get a movie from the DynamoDB table by
    // title and year.
    func (runner PartiQLRunner) GetMovie(ctx context.Context, title string, year int) (Movie, error) {
    	var movie Movie
    	params, err := attributevalue.MarshalList([]interface{}{title, year})
    	if err != nil {
    		panic(err)
    	}
    	response, err := runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("SELECT * FROM \"%v\" WHERE title=? AND year=?",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't get info about %v. Here's why: %v\n", title, err)
    	} else {
    		err = attributevalue.UnmarshalMap(response.Items[0], &movie)
    		if err != nil {
    			log.Printf("Couldn't unmarshal response. Here's why: %v\n", err)
    		}
    	}
    	return movie, err
    }
    
    
    
    // UpdateMovie runs a PartiQL UPDATE statement to update the rating of a movie that
    // already exists in the DynamoDB table.
    func (runner PartiQLRunner) UpdateMovie(ctx context.Context, movie Movie, rating float64) error {
    	params, err := attributevalue.MarshalList([]interface{}{rating, movie.Title, movie.Year})
    	if err != nil {
    		panic(err)
    	}
    	_, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("UPDATE \"%v\" SET info.rating=? WHERE title=? AND year=?",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't update movie %v. Here's why: %v\n", movie.Title, err)
    	}
    	return err
    }
    
    
    
    // DeleteMovie runs a PartiQL DELETE statement to remove a movie from the DynamoDB table.
    func (runner PartiQLRunner) DeleteMovie(ctx context.Context, movie Movie) error {
    	params, err := attributevalue.MarshalList([]interface{}{movie.Title, movie.Year})
    	if err != nil {
    		panic(err)
    	}
    	_, err = runner.DynamoDbClient.ExecuteStatement(ctx, &dynamodb.ExecuteStatementInput{
    		Statement: aws.String(
    			fmt.Sprintf("DELETE FROM \"%v\" WHERE title=? AND year=?",
    				runner.TableName)),
    		Parameters: params,
    	})
    	if err != nil {
    		log.Printf("Couldn't delete %v from the table. Here's why: %v\n", movie.Title, err)
    	}
    	return err
    }
    
    
    

  * For API details, see [ExecuteStatement](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/dynamodb#Client.ExecuteStatement) in _AWS SDK for Go API Reference_. 




## Serverless examples

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

Amazon DocumentDB

IAM

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
