# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store

Title: s3store package - go.temporal.io/server/common/archiver/s3store - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store

Markdown Content:
s3store package - go.temporal.io/server/common/archiver/s3store - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#)
    *   [Recorded Talks](https://go.dev/talks/) 
Videos from prior events

    *   [Meetups _![Image 7](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go) 
Meet other local Go developers

    *   [Conferences _![Image 8](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences) 
Learn and network with Go developers from around the world

    *   [Go blog](https://go.dev/blog) 
The Go project's official blog.

    *   [Go project](https://go.dev/help) 
Get help and stay informed from Go

    *    Get connected  [![Image 9](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts "Get connected with google-groups (Opens in new window)")[![Image 10](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang "Get connected with github (Opens in new window)")[![Image 11](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang "Get connected with twitter (Opens in new window)")[![Image 12](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/ "Get connected with reddit (Opens in new window)")[![Image 13](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/ "Get connected with slack (Opens in new window)")[![Image 14](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

[![Image 15: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.temporal.io/server](https://pkg.go.dev/go.temporal.io/server@v1.30.0)
3.   [common](https://pkg.go.dev/go.temporal.io/server/common@v1.30.0)
4.   [archiver](https://pkg.go.dev/go.temporal.io/server/common/archiver@v1.30.0)
5.   [s3store](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
s3store
=======

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.30.0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.temporal.io/server/common/archiver/s3store) Published: Feb 4, 2026  License: [MIT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store?tab=licenses)

 Opens a new window with license information. 

[Imports: 39](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 1](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 34: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/temporalio/temporal/tree/v1.30.0/go.mod) file ![Image 35](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 
*   ![Image 36: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Redistributable license ![Image 37](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 
*   ![Image 38: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Tagged version ![Image 39](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Modules with tagged versions give importers more predictable builds. 
*   ![Image 40: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Stable version ![Image 41](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
When a project reaches major version v1 it is considered stable. 
*   [Learn more about best practices](https://pkg.go.dev/about#best-practices)

Repository
----------

[github.com/temporalio/temporal](https://github.com/temporalio/temporal "https://github.com/temporalio/temporal")

Links
-----

*   [![Image 42: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/go.temporal.io%2Fserver/v1.30.0 "View this module on Open Source Insights")

 Jump to ... 

*   [README](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-readme)
    *   [Configuration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#readme-configuration)
    *   [Visibility query syntax](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#readme-visibility-query-syntax)
        *   [Limitations](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#readme-limitations)
        *   [Example](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#readme-example)

    *   [Storage in S3](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#readme-storage-in-s3)
    *   [Permissions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#readme-permissions)
    *   [Using localstack for local development](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#readme-using-localstack-for-local-development)

*   [Documentation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-documentation)
    *   [Overview](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-overview)
    *   [Index](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-index)
    *   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-functions)
        *   [BucketExists(ctx, s3cli, URI)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#BucketExists "BucketExists(ctx, s3cli, URI)")
        *   [Download(ctx, s3cli, URI, key)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Download "Download(ctx, s3cli, URI, key)")
        *   [Encode(message)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Encode "Encode(message)")
        *   [IsNotFoundError(err)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#IsNotFoundError "IsNotFoundError(err)")
        *   [KeyExists(ctx, s3cli, URI, key)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#KeyExists "KeyExists(ctx, s3cli, URI, key)")
        *   [NewHistoryArchiver(executionManager, logger, metricsHandler, config)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewHistoryArchiver "NewHistoryArchiver(executionManager, logger, metricsHandler, config)")
        *   [NewVisibilityArchiver(logger, metricsHandler, config)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewVisibilityArchiver "NewVisibilityArchiver(logger, metricsHandler, config)")
        *   [SerializeToken(token)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#SerializeToken "SerializeToken(token)")
        *   [SoftValidateURI(URI)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#SoftValidateURI "SoftValidateURI(URI)")
        *   [Upload(ctx, s3cli, URI, key, data)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Upload "Upload(ctx, s3cli, URI, key, data)")

    *   [Types](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-types)
        *   [type MockQueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser "type MockQueryParser")
            *   [NewMockQueryParser(ctrl)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewMockQueryParser "NewMockQueryParser(ctrl)")
            *   [(m) EXPECT()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser.EXPECT "(m) EXPECT()")
            *   [(m) Parse(query)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser.Parse "(m) Parse(query)")

        *   [type MockQueryParserMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder "type MockQueryParserMockRecorder")
            *   [(mr) Parse(query)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder.Parse "(mr) Parse(query)")

        *   [type QueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#QueryParser "type QueryParser")
            *   [NewQueryParser()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewQueryParser "NewQueryParser()")

*   [Source Files](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-sourcefiles)
*   [Directories](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-directories)

![Image 43](https://pkg.go.dev/static/shared/icon/chrome_reader_mode_gm_grey_24dp.svg) README [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-readme "Go to Readme")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Amazon S3 blobstore

#### Configuration

See [https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials) on how to set up authentication against s3

Enabling archival is done by using the configuration below. `Region` and `bucket URI` are required

```
archival:
  history:
    state: "enabled"
    enableRead: true
    provider:
      s3store:
        region: "us-east-1"
        logLevel: 0
  visibility:
    state: "enabled"
    enableRead: true
    provider:
      s3store:
        region: "us-east-1"
        logLevel: 0

namespaceDefaults:
  archival:
    history:
      state: "enabled"
      URI: "s3://<bucket-name>"
    visibility:
      state: "enabled"
      URI: "s3://<bucket-name>"
```

#### Visibility query syntax

You can query the visibility store by using the `tctl workflow listarchived` command

The syntax for the query is based on SQL

Supported column names are

*   WorkflowId _String_
*   WorkflowTypeName _String_
*   StartTime _Date_
*   CloseTime _Date_
*   SearchPrecision _String - Day, Hour, Minute, Second_

WorkflowId or WorkflowTypeName is required. If filtering on date use StartTime or CloseTime in combination with SearchPrecision.

Searching for a record will be done in times in the UTC timezone

SearchPrecision specifies what range you want to search for records. If you use `SearchPrecision = 'Day'` it will search all records starting from `2020-01-21T00:00:00Z` to `2020-01-21T59:59:59Z`

##### Limitations

*   The only operator supported is `=` due to how records are stored in s3.

##### Example

_Searches for all records done in day 2020-01-21 with the specified workflow id_

`./tctl --ns samples-namespace workflow listarchived -q "StartTime = '2020-01-21T00:00:00Z' AND WorkflowId='workflow-id' AND SearchPrecision='Day'"`

#### Storage in S3

Workflow runs are stored in s3 using the following structure

```
s3://<bucket-name>/<namespace-id>/
	history/<workflow-id>/<run-id>
	visibility/
            workflowTypeName/<workflow-type-name>/
                startTimeout/2020-01-21T16:16:11Z/<run-id>
                closeTimeout/2020-01-21T16:16:11Z/<run-id>
            workflowID/<workflow-id>/
                startTimeout/2020-01-21T16:16:11Z/<run-id>
                closeTimeout/2020-01-21T16:16:11Z/<run-id>
```

Enable AWS SDK Logging with config parameter `logLevel`. For example enable debug logging with `logLevel: 4096`. Possbile Values:

*   LogOff = 0 = 0x0
*   LogDebug = 4096 = 0x1000
*   LogDebugWithSigning = 4097 = 0x1001
*   LogDebugWithHTTPBody = 4098 = 0x1002
*   LogDebugWithRequestRetries = 4100 = 0x1004
*   LogDebugWithRequestErrors = 4104 = 0x1008
*   LogDebugWithEventStreamBody = 4112 = 0x1010
*   LogDebugWithDeprecated = 4128 = 0x1020

#### Permissions

Your s3 user must have at least the following permissions:

*   s3:ListBucket
*   s3:GetObject
*   s3:PutObject

#### Using localstack for local development

1.   Install awscli from [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2.   Install localstack from [here](https://github.com/localstack/localstack#installing)
3.   Launch localstack with `SERVICES=s3 localstack start`
4.   Create a bucket using `aws --endpoint-url=http://localhost:4566 s3 mb s3://temporal-development`
5.   Launch the server with the localstack s3 environment config`--env development-cass-s3 start`

Expand ▾Collapse ▴

![Image 44](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-documentation "Go to Documentation")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-overview "Go to Overview")

Package s3store is a generated GoMock package.

### Index [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-index "Go to Index")

*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-constants)
*   [func BucketExists(ctx context.Context, s3cli s3iface.S3API, URI archiver.URI) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#BucketExists)
*   [func Download(ctx context.Context, s3cli s3iface.S3API, URI archiver.URI, key string) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Download)
*   [func Encode(message proto.Message) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Encode)
*   [func IsNotFoundError(err error) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#IsNotFoundError)
*   [func KeyExists(ctx context.Context, s3cli s3iface.S3API, URI archiver.URI, key string) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#KeyExists)
*   [func NewHistoryArchiver(executionManager persistence.ExecutionManager, logger log.Logger, ...) (archiver.HistoryArchiver, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewHistoryArchiver)
*   [func NewVisibilityArchiver(logger log.Logger, metricsHandler metrics.Handler, config *config.S3Archiver) (archiver.VisibilityArchiver, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewVisibilityArchiver)
*   [func SerializeToken(token interface{}) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#SerializeToken)
*   [func SoftValidateURI(URI archiver.URI) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#SoftValidateURI)
*   [func Upload(ctx context.Context, s3cli s3iface.S3API, URI archiver.URI, key string, ...) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Upload)
*   [type MockQueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser)
*       *   [func NewMockQueryParser(ctrl *gomock.Controller) *MockQueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewMockQueryParser)

*       *   [func (m *MockQueryParser) EXPECT() *MockQueryParserMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser.EXPECT)
    *   [func (m *MockQueryParser) Parse(query string) (*parsedQuery, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser.Parse)

*   [type MockQueryParserMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder)
*       *   [func (mr *MockQueryParserMockRecorder) Parse(query any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder.Parse)

*   [type QueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#QueryParser)
*       *   [func NewQueryParser() QueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewQueryParser)

### Constants [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-constants "Go to Constants")

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser.go#L33)const (
 WorkflowTypeName = "WorkflowTypeName"  WorkflowID = "WorkflowId"  StartTime = "StartTime"  CloseTime = "CloseTime"  SearchPrecision = "SearchPrecision" )

All allowed fields for filtering

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser.go#L42)const (
 PrecisionDay = "Day"  PrecisionHour = "Hour"  PrecisionMinute = "Minute"  PrecisionSecond = "Second" )

Precision specific values

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/history_archiver.go#L31)const (
// URIScheme is the scheme for the s3 implementation	URIScheme = "s3"
)

### Variables [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-functions "Go to Functions")

#### func [BucketExists](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L77)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#BucketExists "Go to BucketExists")added in v1.19.0

func BucketExists(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), s3cli [s3iface](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface).[S3API](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface#S3API), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI)) [error](https://pkg.go.dev/builtin#error)

#### func [Download](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L206)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Download "Go to Download")added in v1.19.0

func Download(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), s3cli [s3iface](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface).[S3API](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface#S3API), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), key [string](https://pkg.go.dev/builtin#string)) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

#### func [Encode](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L30)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Encode "Go to Encode")added in v1.19.0

func Encode(message [proto](https://pkg.go.dev/google.golang.org/protobuf/proto).[Message](https://pkg.go.dev/google.golang.org/protobuf/proto#Message)) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

#### func [IsNotFoundError](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L108)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#IsNotFoundError "Go to IsNotFoundError")added in v1.19.0

func IsNotFoundError(err [error](https://pkg.go.dev/builtin#error)) [bool](https://pkg.go.dev/builtin#bool)

#### func [KeyExists](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L92)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#KeyExists "Go to KeyExists")added in v1.19.0

func KeyExists(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), s3cli [s3iface](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface).[S3API](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface#S3API), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), key [string](https://pkg.go.dev/builtin#string)) ([bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error))

#### func [NewHistoryArchiver](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/history_archiver.go#L70)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewHistoryArchiver "Go to NewHistoryArchiver")

func NewHistoryArchiver(
	executionManager [persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/persistence).[ExecutionManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/persistence#ExecutionManager),
	logger [log](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log).[Logger](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log#Logger),
	metricsHandler [metrics](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics).[Handler](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics#Handler),
	config *[config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config).[S3Archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#S3Archiver),
) ([archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[HistoryArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#HistoryArchiver), [error](https://pkg.go.dev/builtin#error))

NewHistoryArchiver creates a new archiver.HistoryArchiver based on s3

#### func [NewVisibilityArchiver](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/visibility_archiver.go#L57)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewVisibilityArchiver "Go to NewVisibilityArchiver")

func NewVisibilityArchiver(
	logger [log](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log).[Logger](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log#Logger),
	metricsHandler [metrics](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics).[Handler](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics#Handler),
	config *[config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config).[S3Archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#S3Archiver),
) ([archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[VisibilityArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#VisibilityArchiver), [error](https://pkg.go.dev/builtin#error))

NewVisibilityArchiver creates a new archiver.VisibilityArchiver based on s3

#### func [SerializeToken](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L45)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#SerializeToken "Go to SerializeToken")added in v1.19.0

func SerializeToken(token interface{}) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

#### func [SoftValidateURI](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L67)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#SoftValidateURI "Go to SoftValidateURI")added in v1.19.0

func SoftValidateURI(URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI)) [error](https://pkg.go.dev/builtin#error)

Only validates the scheme and buckets are passed

#### func [Upload](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go#L186)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#Upload "Go to Upload")added in v1.19.0

func Upload(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), s3cli [s3iface](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface).[S3API](https://pkg.go.dev/github.com/aws/aws-sdk-go/service/s3/s3iface#S3API), URI [archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver).[URI](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver#URI), key [string](https://pkg.go.dev/builtin#string), data [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

### Types [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#pkg-types "Go to Types")

#### type [MockQueryParser](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser_mock.go#L19)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser "Go to MockQueryParser")

type MockQueryParser struct {
	// contains filtered or unexported fields
}

MockQueryParser is a mock of QueryParser interface.

#### func [NewMockQueryParser](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser_mock.go#L31)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewMockQueryParser "Go to NewMockQueryParser")

func NewMockQueryParser(ctrl *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Controller](https://pkg.go.dev/go.uber.org/mock/gomock#Controller)) *[MockQueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser)

NewMockQueryParser creates a new mock instance.

#### func (*MockQueryParser) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser_mock.go#L38)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser.EXPECT "Go to MockQueryParser.EXPECT")

func (m *[MockQueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser)) EXPECT() *[MockQueryParserMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

#### func (*MockQueryParser) [Parse](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser_mock.go#L43)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser.Parse "Go to MockQueryParser.Parse")

func (m *[MockQueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParser)) Parse(query [string](https://pkg.go.dev/builtin#string)) (*parsedQuery, [error](https://pkg.go.dev/builtin#error))

Parse mocks base method.

#### type [MockQueryParserMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser_mock.go#L26)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder "Go to MockQueryParserMockRecorder")

type MockQueryParserMockRecorder struct {
	// contains filtered or unexported fields
}

MockQueryParserMockRecorder is the mock recorder for MockQueryParser.

#### func (*MockQueryParserMockRecorder) [Parse](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser_mock.go#L52)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder.Parse "Go to MockQueryParserMockRecorder.Parse")

func (mr *[MockQueryParserMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#MockQueryParserMockRecorder)) Parse(query [any](https://pkg.go.dev/builtin#any)) *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

Parse indicates an expected call of Parse.

#### type [QueryParser](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser.go#L17)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#QueryParser "Go to QueryParser")

type QueryParser interface {
 Parse(query [string](https://pkg.go.dev/builtin#string)) (*parsedQuery, [error](https://pkg.go.dev/builtin#error)) }

QueryParser parses a limited SQL where clause into a struct

#### func [NewQueryParser](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser.go#L50)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#NewQueryParser "Go to NewQueryParser")

func NewQueryParser() [QueryParser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#QueryParser)

NewQueryParser creates a new query parser for filestore

![Image 45](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-sourcefiles "Go to Source Files")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/temporalio/temporal/tree/v1.30.0/common/archiver/s3store)

*   [history_archiver.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/history_archiver.go "history_archiver.go")
*   [query_parser.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser.go "query_parser.go")
*   [query_parser_mock.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/query_parser_mock.go "query_parser_mock.go")
*   [util.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/util.go "util.go")
*   [visibility_archiver.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/archiver/s3store/visibility_archiver.go "visibility_archiver.go")

![Image 46](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store#section-directories "Go to Directories")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal Collapse all

| Path | Synopsis |
| --- | --- |
| [mocks](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/archiver/s3store/mocks) Package mocks is a generated GoMock package. | Package mocks is a generated GoMock package. |

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 47: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 48: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 49: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 50: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 51](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 52: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 53](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 54](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
