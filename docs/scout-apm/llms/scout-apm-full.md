# Scout Apm Documentation

Source: https://docs.scoutapm.com/llms-full.txt

---

# Ruby

## Requirements 
Our Ruby agent supports Ruby on Rails 2.2+ and Ruby 1.8.7+. 
See a [list of libraries we instrument](/docs/ruby#instrumented-libraries). 

[Memory Bloat detection](/docs/features/#memory-bloat-detection) require Ruby 2.1+. 

Scout APM 4.0.0+ requires Ruby 2.1+. If you're using a Ruby version lower than 2.1, you can still use Scout APM 2.6.10.

For method-level tracing using our [AutoInstruments](/docs/ruby/features#auto-instruments) feature, you will need a version of the `parser` gem that matches the
Ruby version running your application.



## Installation 

See our [setup page](/docs/ruby/setup) on how to get setup in under 3 minutes in your local, staging and/or production environment.

## Updating



**1.** Ensure your Gemfile entry for Scout is: `gem 'scout_apm'`

**2.** Run `bundle update scout_apm`

**3.** Re-deploy your application.

The gem version changelog is [available here](https://github.com/scoutapp/scout_apm_ruby/blob/master/CHANGELOG.markdown).  

## Instrumented Libraries

The following libraries are currently instrumented:

* Datastores
  * ActiveRecord
  * ElasticSearch
  * Mongoid
  * Moped
  * Redis
* Rack frameworks
  * Rails
  * Sinatra
  * Grape
  * Middleware
* Rails libraries
  * ActionView
  * ActionController
* External HTTP calls
  * HTTPClient
  * Net::HTTP
  * Typhoeus
* Background Job Processing
  * DelayedJob
  * GoodJob
  * Resque
  * Shoryuken
  * Sidekiq
  * Sneakers
  * Solid Queue

Additionally, [Scout can also instrument request queuing time](/docs/features/#request-queuing).

You can instrument your own code or other libraries via [custom instrumentation](/docs/ruby/features/#custom-instrumentation).


# Python

> Looking for detailed tracing to support your microservices architecture? Check out our sister app, [TelemetryHub](https://telemetryhub.com/).

## Scout APM
Scout's Python agent supports many popular libraries to instrument SQL queries, template rendering, HTTP requests and more.
The package is called `scout-apm` [on PyPI](https://pypi.org/project/scout-apm).
Source code and issues can be found on our [scout_apm_python](https://github.com/scoutapp/scout_apm_python) GitHub repository.

## Requirements

`scout-apm` requires :

* Python 3.8+
* A POSIX operating system, such as Linux or macOS ([Request Windows support](https://github.com/scoutapp/scout_apm_python/issues/101)).

## Instrumented Libraries

Scout provides instrument for most of the popular Python libraries. Instrumentation may require some configuration (`Django`) or is automatically applied (`Requests`) by our agent.

### Some configuration required

The libraries below require a small number of configuration updates. Click on the respective library for instructions.

* [Bottle](/docs/python/other-libraries#bottle)
* [Celery](/docs/python/celery)
* [Dash](/docs/python/other-libraries#dash)
* [Django](/docs/python/django)
* [Dramatiq](/docs/python/other-libraries#dramatiq)
* [Falcon](/docs/python/other-libraries#falcon)
* [FastAPI](/docs/python/fastapi)
* [FastMCP](/docs/python/fastmcp)
* [Flask](/docs/python/flask)
* [Flask SQLAlchemy](/docs/python/flask/#flask-sqlalchemy)
* [Huey](/docs/python/other-libraries#huey)
* [Hug](/docs/python/other-libraries#hug)
* [RQ](/docs/python/other-libraries#rq)
* [SQLAlchemy](/docs/python/sqlalchemy)
* [Starlette](/docs/python/other-libraries#starlette)

Additionally, [Scout can also instrument request queuing time](/docs/features/#request-queuing).

### Automatically applied

The libraries below are automatically detected by the agent during the startup process and do not require explicit configuration to add instrumentation.

* ElasticSearch
* Jinja2
* PyMongo
* Redis
* UrlLib3 (used by the popular Requests)

### Deprecated support
The following libraries were instrumented in previous version of the `scout_apm` package, but are no longer supported. You can instrument these yourself or pin an earlier version of the agent. (`scout-apm=2.26.1`).  
This version of scout-apm also supports legacy Python versions including 2.7 and < 3.8

* [CherryPy](/docs/python/other-libraries#cherrypy)
* [Nameko](/docs/python/other-libraries#nameko)
* [Pyramid](/docs/python/other-libraries#pyramid)

You can instrument your own code or other libraries via [custom instrumentation](/docs/python/features/#custom-instrumentation). You can suggest additional libraries you'd like Scout to instrument [on GitHub](https://github.com/scoutapp/scout_apm_python/issues).

Below are database drivers that SQLAlchemy and Django integrate with that we support:

* SQLAlchemy
* SQLite
  - pysqlite
  - asiosqlite
  - pysqlcipher
* PostgreSQL
  - psycopg2
  - pg8000
  - asyncpg
  - psycopg2cffi
  - py-postgresql
  - pygresql
* MySQL / MariaDB
  - mysqlclient
  - PyMySQL
  - MySQL Python Connector
  - aiomysql
  - CyMySQL
  - OurSQL
  - PyODBC
* Oracle
  - cx-Oracle
  - PyODBC
  - mxODBC
  - pymssql
* Django
* SQLite
* PostgreSQL
  - psycopg2
* MySQL / MariaDB
  - mysqlclient
  - MySQL Python Connector
* Oracle
  - cx-Oracle
* MS SQL
  - django-mssql-backend
* Cockroach DB 
  - django-cockroachdb
* Firebird
  - django-firebird
* MongoDB
  - djongo (edited)


## Updating to the Newest Version

```sh
pip install scout-apm --upgrade
```

The package changelog is [available here](https://github.com/scoutapp/scout_apm_python/blob/master/CHANGELOG.md).


# Features

## PECL Extension

Several instruments require the native extension to be included, including timing of Redis, Elasticsearch, and Memcached.

For more information, or to compile manually, the [README](https://github.com/scoutapp/scout-apm-php-ext) has additional instructions.

```bash
sudo pecl install scoutapm
```

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate
specific deploys to changes in performance.

Scout identifies deploys via the following approaches:

* Detecting the current git sha (this is automatically detected when `composer install` is run)

* Setting the [SCOUT_REVISION_SHA](/docs/php/configuration#scout_revision_sha) environment variable equal to the SHA of your latest release during deployment: `git rev-parse --short HEAD`

## Request Queuing

Our PHP integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.

## Custom Context

[Context](/docs/features/#context) lets you see the key attributes of requests. For example,
you can add custom context to answer critical questions like:

* Which plan was the customer who had a slow request on?
* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

It's simple to add [custom context](/docs/features/#context) to your app:

```php
use Scoutapm\Laravel\Facades\ScoutApm; // Laravel only: Add near the other use statements

ScoutApm::addContext("Key", "Value");

// for example, passing in the user_id
// ScoutApm::addContext("user_id", Auth::id());

// or if you have an $agent instance:
$agent->addContext("Key", "Value");
```



### Context Key Restrictions

The Context `key` must be a `String` with only printable characters. Custom
context keys may contain alphanumeric characters, dashes, and underscores.
Spaces are not allowed.

Attempts to add invalid context will be ignored.

### Context Value Types

Context values can be any json-serializable type. Examples:

* `"1.1.1.1"`
* `"free"`
* `100`

### PII
To best help protect your data, we suggest using ids instead of explicit names and emails


## Custom Instrumentation

You can extend Scout to trace transactions outside our officially supported
libraries (e.g. Cron jobs and other web frameworks) and time the execution of
sections of code that falls outside our provided instrumentation.

### Transactions & Timing

Scoutâs instrumentation is divided into 2 areas:

1. __Transactions__: these wrap around an entire flow of work, like a web
   request or Cron job. The Scout Web UI groups data under transactions.
2. __Timing__: these measure small pieces of code that occur inside of a
   transaction, like an HTTP request to an outside service, or a database call.
   This is displayed within a transaction trace in the UI.

### Instrumenting Transactions

A transaction groups a sequence of work under in the Scout UI. These are used
to generate transaction traces. For example, you may create a transaction that
wraps around the entire execution of a PHP script that is ran as a Cron Job.

The Laravel instrumentation does this all for you. You only will need to
manually instrument transactions in special cases. Contact us at
support@scoutapm.com for help.

#### Limits

We limit the number of unique transactions that can be instrumented. Tracking
too many uniquely named transactions can impact the performance of the UI. Do not
dynamically generate transaction names in your instrumentation as this can quickly
exceed our rate limits. Use [context](/docs/php/features/#custom-context) to add
high-dimensionality information instead.

#### Web or Background transactions?

Scout distinguishes between two types of transactions:

* `WebTransaction`: For transactions that impact the user-facing experience.
  Time spent in these transactions will appear on your app overboard dashboard
  and appear in the "Web" area of the UI.
* `BackgroundTransaction`: For transactions that don't have an impact on the
  user-facing experience (example: cron jobs). These will be available in the
  "Background Jobs" area of the UI.

```php
$agent->webTransaction("GET Users", function() { ... your code ... });
$agent->send();
```

### Timing functions and blocks of code

In existing transactions, both automatically created with Laravel instruments,
and also manually created, you can time sections of code that are interesting
to your application.

Traces that allocate significant amount of time to `Controller` or `Job` layers
are good candidates to add custom instrumentation. This indicates a significant
amount of time is falling outside our default instrumentation.

#### Limits

We limit the number of metrics that can be instrumented. Tracking too many
unique metrics can impact the performance of our UI. Do not dynamically
generate metric types in your instrumentation as this can quickly exceed our
rate limits.

For high-cardinality details, use tags.

#### Getting Started

With existing code like:

```php
$request = new ServiceRequest();
$request->setApiVersion($version);
```

It is wrapped with instrumentation:

```php
// At top, with other imports
use Scoutapm\Laravel\Facades\ScoutApm;

// Replacing the above code
$request = ScoutApm::instrument(
    "Custom", // Kind
    "Building Service Request", // Name
    function ($span) use ($version) {
        $request = new ServiceRequest();
        $request->setApiVersion($version);
        return $request;
    }
);
```

* `kind` - A high level area of the application. This defaults to `Custom`.
  Your whole application should have a very low number of unique strings here.
  In our built-in instruments, this is things like `Template` and `SQL`. For
  custom instrumentation, it can be strings like `MongoDB` or `HTTP` or
  similar. This should not change based on input or state of the application.
* `name` - A semi-detailed version of what the section of code is. It should be
  static between different invocations of the method. Individual details like a
  user ID, or counts or other data points can be added as tags. Names like
  `retreive_from_api` or `GET` are good names.
* `span` - An object that represents instrumenting this section of code. You
  can set tags on it by calling `$span->tag("key", "value")`
* `tags` - A dictionary of key/value pairs. Key should be a string, but value
  can be any json-able structure. High-cardinality fields like a user ID are
  permitted.


  ## ARM and graviton Support

  We now have support for ARM and graviton.
  * Our PHP agent does not automatically detect ARM support, currently
    - To explicitly connect, the [core_agent_triple](/docs/php/configuration#core_agent_triple) configuration setting must be specified:

    ```bash
    SCOUT_CORE_AGENT_TRIPLE=aarch64-unknown-linux-musl
    SCOUT_CORE_AGENT_VERSION=v1.3.1
    ```


# Features

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate changes in your app to performance. To enable deploy tracking, first ensure you are on the latest version of `scout_apm`. See our [upgrade instructions](/docs/ruby/#updating). 

Scout identifies deploys via the following: 

1. If you are using Capistrano, no extra configuration is required. Scout reads the contents of the `REVISION` and/or `revisions.log` file and parses out the SHA of the most recent release. 
2. If you are using Heroku, enable [Dyno Metadata](https://devcenter.heroku.com/articles/dyno-metadata). This adds a `HEROKU_SLUG_COMMIT` environment variable to your dynos, which Scout then associates with deploys. 
3. If you are deploying via a custom approach, set a `SCOUT_REVISION_SHA` environment variable equal to the SHA of your latest release. 
    - For example on fly.io you could set it with `fly deploy -e SCOUT_REVISION_SHA=$(git rev-parse --short HEAD)`
4. If the app resides in a Git repo, Scout parses the output of `git rev-parse --short HEAD` to determine the revision SHA.

## Request Queuing

Our Ruby integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.

## Auto Instruments

In many apps, more than 30% of the time spent in a transaction is within custom code written by your development team. In traces, this shows up as time spent in "Controller" or "Job". AutoInstruments helps break down the time spent in your custom code without the need to add custom instrumentation on your own.

AutoInstruments instruments code expressions in Ruby on Rails controllers by instrumenting Rubyâs Abstract Syntax Tree ([AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree)) as code is loaded. These code expressions then appear in traces, just like the many libraries Scout already instruments:



In the screenshot of a trace above, 68% of the time would be allocated to the `Controller` without enabling AutoInstruments. With AutoInstruments enabled, `Controller` time is just 3% of the request and we can clearly see that most of the time is spent inside two method calls.

AutoInstruments is currently available for Ruby on Rails applications.

### Enabling AutoInstruments

AutoInstruments is available to apps using Ruby 2.3.1+. To enable:

**1.** Within your Rails app's directory, run:
```bash
bundle update scout_apm
```

AutoInstruments was released in `scout_apm` version 2.6.0. 


**2.** Set the `auto_instruments` [config option](/docs/ruby/configuration#auto_instruments) to `true`.

If you are using a config file:
```yaml
# config/scout_apm.yml
production:
  auto_instruments: true
```
If you are using environment variables:

`SCOUT_AUTO_INSTRUMENTS=true`

**3.** Deploy

A [detailed AutoInstruments FAQ](/docs/faq/#auto-instruments) is available in our reference area.

**Troubleshooting**:
You may need to add/upgrade the `parser` gem. 

To verify this, set `log_level: debug` in your scout_apm.yml (`SCOUT_LOG_LEVEL: debug` if using environment variable configuration -- such as for Heroku), then check your log/scout_apm.log (if on Heroku check Logplex or your log drains) for the following debug level log:
`AutoInstruments is enabled, but Parser::TreeRewriter is missing. Update 'parser' gem to >= 2.5.0.`

The `parser` gem version works best when it matches the version of Ruby running your application (e.g. `parser v3.1.1.0` for Ruby `3.1.1`)
It is great, but we have seen issues even when `parser` was "ahead" of the Ruby version,
so we recommend matching as closely as possible. See [parser's README](https://github.com/whitequark/parser?tab=readme-ov-file#backwards-compatibility)
for more information.

## Custom Context 

[Context](/docs/features/#context) lets you see the forest from the trees. For example, you can add custom context to answer critical questions like:

* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

It's simple to add [custom context](/docs/features/#context) to your app. There are two types of context:

### User Context

For context used to identify users (ex: id):

```ruby
ScoutApm::Context.add_user({})
```

Examples:

```ruby
ScoutApm::Context.add_user(id: @user.id)
ScoutApm::Context.add_user(id: @user.id, location: @user.location.to_s)
```

### General Context

```ruby
ScoutApm::Context.add({})
```

Examples:

```ruby
ScoutApm::Context.add(account: @account.id)
ScoutApm::Context.add(database_shard: @db.shard_id, monthly_spend: @account.monthly_spend)
```

### Default Context

Scout reports the Request URI and the user's remote IP Address by default.

### Context Types

Context values can be any of the following types:

* Numeric
* String
* Boolean
* Time
* Date

### Context Field Name Restrictions

Custom context names may contain alphanumeric characters, dashes, and underscores. Spaces are not allowed.

Attempts to add invalid context will be ignored.

### Example: adding the current user's id as context

Add the following to your `ApplicationController` class:

```ruby
before_filter :set_scout_context
```

Create the following method:

```ruby
def set_scout_context
  ScoutApm::Context.add_user(id: current_user.id) if current_user.is_a?(User)
end
```

### Example: adding the monthly spend as context

Add the following line to the `ApplicationController#set_scout_context` method defined above:

```ruby
ScoutApm::Context.add(monthly_spend: current_org.monthly_spend) if current_org
```

### PII
To better protect your data, we suggest using ids instead of explicit names and emails

## Renaming transactions

There may be cases where you require more control over how Scout names transactions for your endpoints and background jobs.

For example, if you have a controller-action that renders both JSON and HTML formats and the rendering time varies significantly between the two, it may make sense to define a unique transaction name for each.

Use `ScoutApm::Transaction#rename`:

```ruby
class PostsController < ApplicationController
  def index                              
    ScoutApm::Transaction.rename("posts/foobar")                                   
    @posts = Post.all                    
  end
end
```

In the example above, the default name for the transaction is `posts/index`, which appears as `PostsController#index` in the Scout UI. Renaming the transaction to `posts/foobar` identifies the transaction as `PostsController#foobar` in the Scout UI.  

Do not generate highly cardinality transaction names (ex: `ScoutApm::Transaction.rename("posts/foobar_#{current_user.id}")`) as we limit the number of transactions that can be tracked. High-cardinality transaction names can quickly surpass this limit.

### GraphQL

If you have a GraphQL endpoint which serves any number of queries, you likely want to have each of those types of queries show up in the Scout UI as different endpoints. You can accomplish this by renaming the transaction during the request like so:

```ruby
scout_transaction_name = "GraphQL/" + operation_name
ScoutApm::Transaction.rename(scout_transaction_name)
```

Where `operation_name` is determined dynamically based on the GraphQL query. E.g. `get_profile`, `find_user`, etc.

Do not generate highly cardinality transaction names, like `ScoutApm::Transaction.rename("GraphQL/foobar_#{current_user.id}")`, as we limit the number of transactions that can be tracked. High-cardinality transaction names can quickly surpass this limit.

## Custom Instrumentation

Traces that allocate significant amount of time to `Controller` or `Job` are good candidates to add custom instrumentation. This indicates a significant amount of time is falling outside our default instrumentation.

### Limits

We limit the number of metrics that can be instrumented. Tracking too many unique metrics can impact the performance of our UI. Do not dynamically generate metric types in your instrumentation (ie `self.class.instrument("user_#{user.id}", "generate") { ... })` as this can quickly exceed our rate limits.

### Instrumenting method calls

To instrument a method call, add the following to the class containing the method:

```ruby
  class User
    include ScoutApm::Tracer

    def export_activity
      # Do export work
    end
    instrument_method :export_activity
  end
```

The call to `instrument_method` should be after the method definition.

#### Naming methods instrumented via `instrument_method`

In the example above, the metric will appear in traces as `User#export_activity`. On timeseries charts, the time will be allocated to a `Custom` type.

__To modify the type__:

```ruby
instrument_method :export_activity, type: 'Exporting'
```

A new `Exporting` metric will now appear on charts. The trace item will be displayed as `Exporting/User/export_activity`.

__To modify the name__:

```ruby
instrument_method :export_activity, type: 'Exporting', name: 'user_activity'
```

The trace item will now be displayed as `Exporting/user_activity`.

### Instrumenting blocks of code

To instrument a block of code, add the following:

```ruby
  class User
    include ScoutApm::Tracer

    def generate_profile_pic
      self.class.instrument("User", "generate_profile_pic") do
        # Do work
      end
    end
  end
```

#### Naming methods instrumented via `instrument(type, name)`

In the example above, the metric appear in traces as `User/generate_profile_pic`. On timeseries charts, the time will be allocated to a `User` type. To modify the type or simply, simply change the `instrument` corresponding method arguments.

## Environments

It typically makes sense to treat each environment (production, staging, etc) as a separate application within Scout and ignore the development and test environments. Configure a unique app name for each environment as Scout aggregates data by the app name.

There are 2 approaches:

### 1. Modifying your scout_apm.yml config file

Here's an example `scout_apm.yml` configuration to achieve this:

```yaml
common: &defaults
  name: <%= "YOUR_APP_NAME (#{Rails.env})" %>
  key: YOUR_KEY
  log_level: info
  monitor: true

production:
  <<: *defaults

development:
  <<: *defaults
  monitor: false

test:
  <<: *defaults
  monitor: false

staging:
  <<: *defaults
```

### 2. Setting the SCOUT_NAME environment variable

Setting the `SCOUT_NAME` and `SCOUT_MONITOR` environment variables will override settings settings your `scout_apm.yml` config file.

To isolate data for a staging environment: `SCOUT_NAME="YOUR_APP_NAME (Staging)"`.

To disable monitoring: `SCOUT_MONITOR=false`.

See the full list of [configuration options](/docs/ruby/configuration).

## Disabling a Node

To disable Scout APM on any node in your environment, just set `monitor: false` in your `scout_apm.yml` configuration file on that server, and restart your app server. Example:

```yaml
common: &defaults
  name: <%= "YOUR_APP_NAME (#{Rails.env})" %>
  key: YOUR_KEY
  log_level: info
  monitor: false

production:
  <<: *defaults
```

Since the YAML config file allows ERB evaluation, you can even programatically enable/disable nodes based on host name. This example enables Scout APM on web1 through web5:

```yaml
common: &defaults
  name: <%= "YOUR_APP_NAME (#{Rails.env})" %>
  key: YOUR_KEY
  log_level: info
  monitor: <%= Socket.gethostname.match(/web[1..5]/) %>

production:
  <<: *defaults
```

After you've disabled a node in your configuration file and restarted your app server, the node show up as inactive in the UI after 10 minutes.


# Features

## Scout APM
Scout is Application Monitoring built for modern development teams. It's built to provide the fastest path to a slow line-of-code. [Signup for a trial](https://scoutapm.com/users/sign_up).

## App Performance Overview

The overview page provides an at-a-glance, auto-refreshing view of your app's performance and resource usage (mean response time by category, 95th percentile response time, throughput, error rate, and more). You can quickly dive into endpoint activity via click-and-drag (or pinch-and-expand with a mobile device) on the overview chart.



Additionally, you can compare metrics in the overview chart and see how your app's performance compares to different time periods.

## Endpoint Details

You can view metrics for specific controller-action and background job workers. There is a similar chart interaction to the App Performance Overview page, with one difference: your selection will render an updated list of transaction traces that correspond to the selected time period:


You can sort traces by response time, object allocations, date, and more.

## Transaction Traces

Scout collects detailed transactions across your web endpoints and background jobs automatically. The transaction traces provide a number of visual queues to direct you to hotspots. Dig into bottlenecks - down to the line-of-code, author, commit date, and deploy time - from this view.




### SQL Queries

Scout captures a sanitized version of SQL queries. Click the "SQL" button next to a call to view details.




#### Don't see an SQL button next to a database query?

Scout collects a sanitized version of SQL queries and displays these in transaction traces. To limit agent overhead sanitizing queries, we do not collect query statements with more than 16k characters.


### Code Backtraces

You'll see "CODE" buttons next to method calls that are >= 500 ms. [If you've enabled the GitHub integration](/docs/features/#github), you can see the line-of-code, associated SQL or HTTP endpoint (if applicable), author, commit date, and deploy time for the relevant slow code.



If you don't enable the GitHub integration, you'll see a backtrace.

### Trace Views

There are two displays for showing the details of a transaction trace:

* __Summary View__ - Method calls are aggregated together and ordered from most to least expensive.
* __Timeline View__ - Shows the execution order of calls as they occur during the transaction.

#### Summary View

Method calls are aggregated together and listed from most expensive to least expensive. The time displayed is the total time across all calls (not the time per-call).



#### Timeline View

See the execution order of your code.




The timeline view is especially helpful for:

* understanding the distribution of `Controller` time across a request. Is there a lot of time spent in your custom code at the beginning of a request? Is it spread out? Is it at the end of a request?
* understanding the timing of distinct SQL queries. Is one instance of many nearly identical queries slow or all of them?
* getting the complete picture of parent and children method calls. How many SQL calls are being triggered by the same view partial?

##### Upgrading to the timeline view

For older Ruby agents, if you see a message in the UI prompting you to upgrade, [follow our Ruby agent upgrade instructions](/docs/ruby/#updating-to-the-newest-version) to update to the latest agent, which supports sending the timeline trace format.

##### Timeline view limitations

* No ScoutProf support
* No Background job support

## Trace Explorer

What was the slowest request yesterday? How has the app performed for `user@domain.com`? Which endpoints are generating the bulk of slow requests? Trace Explorer lets you quickly filter the transaction traces collected by Scout, giving you answers to your unique questions.



Trace Explorer is accessed via the "Traces" navigation link when viewing an app.

### How to use Trace Explorer

There are two main areas of Trace Explorer:

* __Dimension Histograms__ - the top portion of the page generates a histogram representation for a number of trace dimensions (the response time distribution, count of traces by endpoints, and a display for each piece of [custom context](/docs/features/#custom-context)). Selecting a specific area of a chart filters the transactions to just the selected data.
* __List of transaction traces__ - the bottom portion of the page lists the [individual traces](/docs/features/#transaction-traces). The traces are updated to reflect those that match any filtered dimensions. You can increase the height of this pane by clicking and dragging the top portion of the pane. Clicking on a trace URI opens the transaction trace in a new browser tab.

### Custom Trace Querying



From the top right of the Trace Explorer, you can select a "Dataset" of 1000 traces. These include a random "Sample", the "Slowest" traces, or those with the "Most Allocations". In addition, you can select the "Query" button to build a custom query. Here, you can query on any attribute you'd like, including custom context you've set. Only want to load traces for a specific user_id? From a certain host? Apply as many conditions as you like, and then select "Apply Filters".

## Memory Bloat Detection

If a user triggers a request to your Rails application that results in a large number of object allocations (example: loading a large number of ActiveRecord objects), your app may require additional memory. The additional memory required to load the objects in memory is released back very slowly. Therefore, a single memory-hungry request will have a long-term impact on your Rails app's memory usage.

There are 3 specific features of Scout to aid in fixing memory bloat.

### Memory Bloat Insights

The Insights area of the dashboard identifies controller-actions and background jobs that have triggered significant memory increases. An overview of the object allocation breakdown by tier (ActiveRecord, ActionView, etc) is displayed on the dashboard.



### Memory Traces

When inspecting a [transaction trace](/docs/features/#transaction-traces), you'll see a "Memory Allocation Breakdown" section:



For perspective, we display how this trace's allocations compare to the norm.

## Insights History
In addition to the memory bloat insights, you will be able to view past memory bloat, slow query (if enabled), and N+1 insights. These insights will have a saved trace with them, and these trace have a longer retention period than our normal traces do.



## Alerting



Alerting keeps your team updated if your app's performance degrades. Alerts can be configured on the app as a whole as well as on individual endpoints and background jobs. Metrics include:

Web Requests:
* Mean Response Time
* 95th Percentile Response Time
* Apdex
* Error Rate
* Throughput
* Queue Time

Background Jobs:
* Mean Response Time
* Error Rate
* Throughput
* Queue Time


### Setting Up Alerts

There are four parts to alerting, the alert event, the alert conditon, the notification group, and notification channels.

While we will discuss them in this order, it makes more sense to actually create these in reverse order. Starting with first creating a notification channel, then adding this notification channel to a notification group, then assigning this notification group to be notified when alerts are created from the alert condition.

To get started, head to your orgâs settings menu:


**Alert event**:

An alert event is created anytime the threshold is passed for an alert condition. This alert event will either be an open event, or a closed event. For example, see the Slack notification alerts below:



**Alert Conditions**:

An alert condition is what creates the alert events. Alert conditions are set to check for if the payloads we have received are either great than or lower than one of the metrics listed above.

For example, you can set an alert condition to trigger an alert whenever throughput for all your endpoints exceeds 1000 RPM:



**Notification group**:

When an alert condition's threshold has been passed, and an alert has been created, the alert condition will notify the notification group. The notification group will then pass this message to all of its notification channels. For example, if a Slack notification channel, an email notification channel, and a Splunk notification channel are all part of the same group, they will all be notified of the alert event (they will receive both open and close events).



**Notification Channel**:

A notification channel belongs to a notification group, and is a specific channel that you want to notify. [Alerting integrations](/docs/integrations/#alerting) aren't just limited to a single notification. For example, you can have multiple Slack notification channels, with each notifying a different slack... channel. A better example is PagerDuty, you can have multiple PagerDuty notification channels, with each channel having a different alert level.



### Which Alerts Should I Set?

Setting up alerts can be pretty application dependent. Here are just a few examples below on when to use a specific alert condition:

**Throughput**:

If you have very consistent traffic, it could be useful setting up throughput alerts for your application. For example, if your application receives 1000 rpm per a minute during peak times, setting up an alert for when your application is 1500 rpm would allow you to see how your application is actually performing under higher stress.

**Response Time**:

Perhaps for your application there is a critical endpoint that you need responding within in specific amount of time, or a critical background job you need to execute within a set amount of time. Setting up response time alerts against these endpoints and jobs would be useful.

Setting up general application response time can be useful as well. If you have an API application, and your average response time is roughly 80ms, setting up alerts for when your response time goes above 200ms could be quite essential.

**Queue Time**:

Depending on one's architure, such as those using a PaaS, getting notifications for when your application is seeing a rise in queuetime can indiciate that your application is starting to reach capacity.

**Error Rate**:

Depending on one's application, getting more than 10 errors per a minute can be a sign that things aren't going smoothly (such as after an errant deploy).

#### Where can I have alerts sent?

Checkout our [alerting integrations page](/docs/integrations#alerting). We can integrate with popular on call tools such as [PagerDuty](/docs/integrations/alerting#pagerduty), [Splunk On-Call](/docs/integrations/alerting#splunk-on-call), and [Opsgenie](/docs/integrations/alerting#opsgenie). Additionally, you can send your alerts directly to [Slack](/docs/integrations/alerting#slack) channels where your dev team is located, to your dev's emails, as well as being able to send alerts to various webhooks and [Zapier](/docs/integrations/alerting#zapier).

The best part is, you aren't limited to sending an alert to a single place. When you create a notification channel, such as notifiying a slack channel, sending a critical alert to Splunk, etc. You can assign multiple notification channels to a notification group. When you set up an alert condition, you will assign a notification group to it. This notification group will then notify all notification channels that belong to it.

### Setting Up Notifications

There are three parts to receiving error notifications: notification channels, the channel's notification group, and the apps's error notificaiton groups.

It makes sense to create the notifications in this order, starting with first creating a notification channel, then adding this notification channel to a notification group, then assigning this notification group to the app's error notification groups.

To get started, head to your orgâs settings menu:


**Notification Channel**:

A notification channel belongs to a notification group, and is a specific channel that you want to notify. [Alerting integrations](/docs/integrations/#alerting) aren't just limited to a single notification. For example, you can have multiple Slack notification channels, with each notifying a different slack... channel. A better example is PagerDuty, you can have multiple PagerDuty notification channels, with each channel having a different alert level.




**Notification group**:

When an exception occurs, and the notificaiton group has been added the app's error notifications group, we will notify the notification group of the exception. The notification group will then pass this message to all of its notification channels. For example, if a Slack notification channel, an email notification channel, and a Splunk notification channel are all part of the same group, they will all be notified of the exception.



**App Error Notification Groups**:

Once either a new notification group has been created, or the Default group has had a channel added to it, notification groups will need to be assigned to the app's error notificaiton groups to be notified of when an exception occurs. 

App's can have as many notification groups assigned to them as needed.



#### Where can I have error notifications sent?

Checkout our [alerting integrations page](/docs/integrations#alerting). We can integrate with popular on call tools such as [PagerDuty](/docs/integrations/alerting#pagerduty), [Splunk On-Call](/docs/integrations/alerting#splunk-on-call), and [Opsgenie](/docs/integrations/alerting#opsgenie). Additionally, you can send your notifications directly to [Slack](/docs/integrations/alerting#slack) channels where your dev team is located, to your devs emails, as well as being able to send notifications to various webhooks and [Zapier](/docs/integrations/alerting#zapier).



The best part is, you aren't limited to sending an error notificaiton to a single place. When you create a notification channel, such as notifiying a slack channel, sending a critical alert to Splunk, etc. You can assign multiple notification channels to a notification group. When an exception occurs, we will notify all of the channels in the notification group.


## Deploy Tracking



Correlate deploys with your app's performance: Scout's GitHub-enhanced deploy tracking makes it easy to identify the Git branch or tag running now and which team members contributed to every deploy.


### Sorting

You can sort by memory allocations throughout the UI: from the list of endpoints, to our pulldowns, to transaction traces.



## Request Queuing

Our agents can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queuing" and provides an indication of your application's capacity. Large request queuing time is an indication that your app needs more capacity.



To see this metric within Scout, you need to configure your upstream software, adding an HTTP header that our agent reads. This is typically a one-line change.

### Setup

#### HTTP Header

The Scout agent depends on an HTTP request header set by an upstream load balancer (ex: HAProxy) or web server (ex: Apache, Ngnix).

__Protip:__ We suggest adding the header as early as possible in your infrastructure. This ensures you won't miss performance issues that appear before the header is set.

The agent will read any of the following headers as the start time of the request:

`X-Queue-Start, X-Request-Start, X-QUEUE-START, X-REQUEST-START, x-queue-start, x-request-start`

Include a value in the format `t=MICROSECONDS_SINCE_EPOCH` where `MICROSECONDS_SINCE_EPOCH` is an integer value of the number of microseconds that have elapsed since the beginning of Unix epoch.

__Nearly any front-end HTTP server or load balancer can be configured to add this header.__ Some examples are below.

#### Heroku

Time in queue is automatically collected for apps deployed on Heroku. This measures the time from when a request hits the Heroku router and when your app begins processing the request.

#### Apache

Apache's __mod_headers__ module includes a `%t` variable that is formatted for Scout usage. To enable request queue reporting, add this code to your Apache config:

````bash
RequestHeader set X-Request-Start "%t"
````

##### Apache Request Queuing and File Uploads

If you are using Apache, you may observe a spike in queue time within Scout for actions that process large file uploads. Apache adds the `X-Request-Start` header as soon as the request hits Apache. So, all of the time spent uploading a file will be reported as queue time.

This is different from Nginx, which will first buffer the file to a tmp file on disk, then once the upload is complete, add headers to the request.

#### HAProxy

HAProxy 1.5+ supports timestamped headers and can be set in the frontend or backend section. We suggest putting this in the frontend to get a more accurate number:

HAProxy < 1.9:

````bash
http-request set-header X-Request-Start t=%Ts
````

HAProxy >= 1.9:

````bash
http-request set-header X-Request-Start t=%[date()]%[date_us()]
````

#### Nginx

Nginx 1.2.6+ supports the use of the `#{msec}` variable. This makes adding the request queuing header straightforward.

General Nginx usage:

````bash
proxy_set_header X-Request-Start "t=${msec}";
````

Passenger 5+:

````bash
passenger_set_header X-Request-Start "t=${msec}";
````

Older Passsenger versions:

````bash
passenger_set_cgi_param X-REQUEST-START "t=${msec}";
````

Note: The Nginx option is local to the [location block](https://www.phusionpassenger.com/library/config/nginx/reference/#this-configuration-option-is-not-inherited-across-contexts), and isn't inherited.

#### AWS

Unfortunately with both ELB and ALB, Amazon adds a X-Amzn-Trace-Id header which only gives time in seconds from epoch. This is not a very accurate measurement, as a result we do not parse this header:
https://github.com/scoutapp/scout_apm_ruby/issues/196

## Context

Context lets you see the forest from the trees. For example, you can add custom context to answer critical questions like:

* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

Adding custom context is easy - learn how via [Ruby](/docs/ruby/features/#custom-context), [Elixir](/docs/elixir/features/#custom-context), [Python](/docs/python/features/#custom-context), [PHP](/docs/php/features/#custom-context), and [Node](/docs/node/features/#custom-context)

Context information is displayed in two areas:

* When viewing a [transaction trace](/docs/features/#transaction-traces) - click the "Context" section to see the context Scout has collected.
* When using [Trace Explorer](/docs/features/#trace-explorer) - filter traces by context.

## Endpoints Performance

### Endpoints Overview

The endpoints area within Scout provides a sortable view of your app's overall performance aggregated by endpoint name. Click on an endpoint to view details.



## Time Comparisons

You can easily compare the performance of your application between different time periods via the time selection on the top right corner of the UI.



## Database Monitoring

{{<show_support "Ruby, Python, PHP, Elixir">}}

When the database monitoring feature is enabled, you'll gain access to both a high-level overview of your database query performance and detailed information on specific queries. Together, these pieces make it easier to get to the source of slow query performance.

### Database Queries Overview

The high-level view helps you identify where to start:



The chart at the top shows your app's most time-consuming queries over time. Beneath the chart, you'll find a sortable list of queries grouped by a label (for Rails apps, this is the ActiveRecord model and operation) and the caller (a web endpoint or a background job):

This high-level view is engineered to reduce the investigation time required to:

* __identify slow queries__: it's easy for queries to become more inefficient over time as the size of your data grows. Sorting queries by "95th percentile response time" and "mean response time" makes it easy to identify your slowest queries.
* __solve capacity issues__: an overloaded database can have a dramatic impact on your app's performance. Sorting the list of queries by "% time consumed" shows you which queries are consuming the most time in your database.

#### Zooming

__If there is a spike in time consumed or throughput, you can easily see what changed during that period__. Click and drag over the area of interest on the chart:



Annotations are added to the queries list when zooming:

* The change in rank, based on % time consumed, of each query. Queries that jump significantly in rank may trigger a dramatic change in database performance.
* The % change across metrics in the zoom window vs. the larger timeframe. If the % change is not significant, the metric is faded.

#### Database Events

Scout highlights significant events in database performance in the sidebar. For example, if time spent in database queries increases dramatically, you'll find an insight here. Clicking on an insight jumps to the time window referenced by the insight.

### Database Query Details

After identifying an expensive query, you need to see where the query is called and the underlying SQL. Click on a query to reveal details:



You'll see the raw SQL and a list of individual query execution times that appeared in transaction traces. Scout collects backtraces on queries consuming more than 500 ms. If we've collected a backtrace for the query, you'll see an icon next to the timing information. Click on one of the traces to reveal that trace in a new window:



The source of that trace is immediately displayed.

### Slow Query Insights

When the database monitoring feature is enabled (with the pro plan), a new "Slow Query" insight is activated on your app dashboard:



This insight analyzes your queries in three dimensions, helping you focus on database optimizations that will most improve your app:

1. __Which queries are most impacting app performance?__ This is based on the total time consumed of each query, where time consumed is the average query latency multiplied by the query throughput.
2. __Which queries are significant bottlenecks inside web endpoints and background jobs?__ A single query that is responsible for a large percentage of the time spent in a transaction is a great place to investigate for a performance win.
3. __Which queries are consistently slow?__ These are queries that have a high average latency.



### Pricing

For direct users, Database Monitoring is available as pro plan feature. For Heroku users, it's available as an [addon](https://devcenter.heroku.com/articles/scout#database-monitoring-addon). See your billing page for pricing information.

### Database Monitoring Installation

[Update](/docs/ruby/#updating-to-the-newest-version) - or install - the `scout_apm` gem in your application. There's no special libraries to install on your database servers.

### Database Monitoring Library Support

Scout currently monitors queries executed via ActiveRecord, which includes most relational databases (PostgreSQL, MySQL, etc).

### What does SQL#other mean?

Some queries may be identified by a generic `SQL#other` label. This indicates our agent was unable to generate a friendly label from the raw SQL query. Ensure you are running version 2.3.3 of the `scout_apm` gem or higher as this release includes more advanced query labeling logic.

## External Services

Gain deeper visibility to further drill down metrics and the time spent in your API calls with our External Services Dashboard.



## Digest Email

At a frequency of your choice (daily or weekly), Scout crunches the numbers on your app's performance (both web endpoints and background jobs). Performance is compared to the previous week, and highlights are mentioned in the email.



The email identifies performance trends, slow outliers, and attempts to narrow down issues to a specific cause (like slow HTTP requests to another service).

## Insights Email
Similar to the digest email, choose a frequency of your choice (daily or weekly), and Scout aggregates the newest insights (N+1, Slow Query, and Memory Bloat) across all your applications.


Additionally, we also will aggregate up to 5 of the slowest web request and background job traces across all of your applications.



## Chart Embeds

You can embed an app's overview chart inside another web page (ex: an internal key metrics dashboard):

1. Access the application dashboard within the Scout UI.
2. Adjust the timeframe and metrics to those you'd like to include in the embedded chart.
3. Click the embed icon and copy the relevant code.



Note that you'll need to update the provided iframe url with a Scout API key.

When clicking on an embedded chart, you'll be redirected to the relevant application.

## ARM and graviton support

We now have support for ARM and graviton.
* The Ruby agent is platform agnostic
* Our Python agent automatically detects ARM support
  - To explicitly connect, the [core_agent_triple](/docs/python/configuration#core_agent_triple) configuration setting must be specified.
* For Elixir, PHP, and Node, the `code_agent_triple` configuration setting must be explicitly specified.
  - Find the [Elixir](/docs/elixir/configuration/#core_agent_triple) setting here
  - Find the [PHP](/docs/php/configuration/#core_agent_triple) setting here
  - Find the [Node](/docs/node/configuration/#core_agent_triple) setting here


# Features

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate changes in your app to performance. To enable deploy tracking, first ensure you are on the latest version of `scout_apm`. See our [upgrade instructions](/docs/elixir/#updating-to-newest-version).

Scout identifies deploys via the following:

1. A `revision_sha` config setting.
2. A `SCOUT_REVISION_SHA` environment variable equal to the SHA of your latest release.
3. If you are using Heroku, enable [Dyno Metadata](https://devcenter.heroku.com/articles/dyno-metadata). This adds a `HEROKU_SLUG_COMMIT` environment variable to your dynos, which Scout then associates with deploys.

## Request Queuing

Our Elixir integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.

__Note:__ For Elixir, we currently only support the following two headers: `x-queue-start` and `x-request-start`, and we don't support msec -- or decimal millisecond. Example of valid header:
`x-request-start: "1234567890123"`


## Custom Context

[Context](/docs/features/#context) lets you see the forest from the trees.
For example, you can add custom context to answer critical questions like:
* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers? It's simple to add [custom context](/docs/features/#context) to your app. There are two types of context:

### User Context
For context used to identify users (ex: id):
```elixir
ScoutApm.add_user(key, value)
```
Examples:

```elixir
ScoutApm.Context.add_user(:id, user.id)
```
### General Context
```elixir
ScoutApm.Context.add(key, value)
```
Examples:
```elixir
ScoutApm.Context.add(:account, account.id)
ScoutApm.Context.add(:monthly_spend, account.monthly_spend)
```
### Default Context
Scout reports the Request URI and the user's remote IP Address by default.
### Context Value Types Context values can be any of the following types:
* Printable strings (`String/printable?/1` returns `true`) * Boolean * Number
### Context Key Restrictions
Context keys can be an `Atom` or `String` with only printable characters.
Custom context keys may contain alphanumeric characters, dashes, and underscores. Spaces are not allowed. Attempts to add invalid context will be ignored.
### PII
To best help protect you data, we suggest using ids instead of explicit names and emails


## Custom Instrumentation

You can extend Scout to record additional types of transactions (background jobs, for example) and time the execution of code that fall outside our auto instrumentation.

For full details on instrumentation functions, see our [ScoutApm. Tracing Hex docs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html).

### Transactions & Timing

Scoutâs instrumentation is divided into 2 areas:

**1.**
__Transactions__: these wrap around a flow of work, like a web request or a GenServer call. The UI groups data under transactions. Use the `deftransaction/2` macro or wrap blocks of code with the `transaction/4` macro.

**2.**
 __Timing__: these measure individual pieces of work, like an HTTP request to an outside service or an Ecto query, and displays timing information within a transaction trace. Use the `deftiming/2` macro or the `timing/4` macro.

### Instrumenting transactions
#### deftransaction Macro Example

Replace your function `def` with `deftransaction` to instrument it.

You can override the name and type by setting the `@transaction_opts` attribute right before the function.

```elixir
defmodule YourApp.Web.RoomChannel do
use Phoenix.Channel import ScoutApm.Tracing

# Will appear under "Web" in the UI, named "YourApp.Web.RoomChannel.join".
@transaction_opts [type: "web"]
deftransaction join("topic:html", _message, socket) do
  {:ok, socket}
end

# Will appear under "Background Jobs" in the UI, named "RoomChannel.ping".
@transaction_opts [type: "background", name: "RoomChannel.ping"]
deftransaction handle_in("ping", %{"body" => body}, socket) do
  broadcast! socket, "new_msg", %{body: body} {:noreply, socket}
end
```

#### transaction/4 Example
Wrap the block of code you'd like to instrument with `transaction/4`:
```elixir
import ScoutApm.Tracking def
  do_async_work do Task.start(fn ->
    # Will appear under "Background Jobs" in the UI, named "Do Work".
    transaction(:background, "Do Work") do
      # Do work...
    end
  end)
end
```
See the [ScoutApm.Tracing Hexdocs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html) for details on instrumenting transactions.

### Timing functions and blocks of code

#### deftiming Macro Example

Replace your function `def` with `deftiming` to instrument it. You can override the name and category by setting the `@timing_opts` attribute right before the function.

```elixir
defmodule Searcher do
 import ScoutApm.Tracing

 # Time associated with this function will appear under "Hound" in timeseries charts.
 # The function will appear as `Hound/open_search` in transaction traces.
 @timing_opts [category: "Hound"] deftiming open_search(url) do
  navigate_to(url)
 end

 # Time associated with this function will appear under "Hound" in timeseries charts.
 # The function will appear as `Hound/homepage` in transaction traces.

 @timing_opts [category: "Hound", name: "homepage"]
 deftiming open_homepage(url) do
   navigate_to(url)
end
```
#### timing/4 Example

Wrap the block of code you'd like to instrument with `timing/4`:
```elixir
defmodule PhoenixApp.PageController do
use PhoenixApp.Web, :controller import ScoutApm.Tracing
def index(conn, _params) do
  timing("Timer", "sleep") do
    :timer.sleep(3000)
  end
  render conn, "index.html"
end
```
See the [ScoutApm.Tracing Hexdocs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html) for details on timing functions and blocks of code. #### Limits on category arity We limit the number of unique categories that can be instrumented. Tracking too many unique category can impact the performance of our UI. Do not dynamically generate categories in your instrumentation (ie `timing("user_#{user.id}", "generate", do: do_work())` as this can quickly exceed our rate limits.

#### Adding a description

Call `ScoutApm.Tracing.update_desc/1` to add relevant information to the instrumented item. This description is then viewable in traces. An example:
```elixir
timing("HTTP", "GitHub_Avatar") do
  url = "https://github.com/#{user.id}.png"
  update_desc("GET #{url}")
  HTTPoison.get(url)
end
```

#### Tracking

Already executed time Libraries like Ecto log details on executed queries. This includes timing information. To add a trace item for this, use `ScoutApm.Tracing.track`.
An example:
```elixir
defmodule YourApp.Mongo.Repo do
  use Ecto.Repo # Scout instrumentation of Mongo queries. These appear in traces as "Ecto/Read", "Ecto/Write", etc.

  def log(entry) do
    ScoutApm.Tracing.track( "Ecto", query_name(entry), entry.query_time, :microseconds )
    super entry
  end
end
```

In the example above, the metric will appear in traces as `Ecto/#{query_time(entry)}`. On timeseries charts, the time will be allocated to `Ecto`. [See the scout_apm hex docs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html#track/5) for more information on `track/`.

## Error Monitoring

Scout automatically captures unhandled exceptions in your Phoenix application. See the [Error Monitoring feature page](/docs/features/error-monitoring) for full details on the Scout Error Monitoring UI.

### Setup

Attach the Phoenix error telemetry handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.PhoenixErrorTelemetry.attach()
  # ...
end
```

Error monitoring is enabled by default (`errors_enabled: true`). No additional configuration is required.

### Manual Error Capture

You can also capture errors manually:

```elixir
try do
  some_risky_operation()
rescue
  e ->
    ScoutApm.Error.capture(e, stacktrace: __STACKTRACE__)
    reraise e, __STACKTRACE__
end
```

With additional context:

```elixir
ScoutApm.Error.capture(e,
  stacktrace: __STACKTRACE__,
  context: %{user_id: user.id},
  request_path: "/api/users",
  request_params: %{action: "update"}
)
```

### Configuration

```elixir
config :scout_apm,
  errors_enabled: true,
  errors_ignored_exceptions: [Phoenix.Router.NoRouteError],
  errors_filter_parameters: ["password", "credit_card"]
```

See [Error Monitoring configuration](/docs/elixir/configuration#error-monitoring-configurations) for all options.

## Log Management

Scout can forward your application logs for centralized search and analysis. See the [Log Management feature page](/docs/features/log-management) for full details on the Scout Log Management UI.

### Setup

**1.** Enable log management in your config and provide an ingest key (available in the Logs page of your Scout app):

```elixir
config :scout_apm,
  logs_enabled: true,
  logs_ingest_key: "your-logs-ingest-key"
```

**2.** Attach the log handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Logging.attach()
  # ...
end
```

Once enabled, Scout integrates with Elixir's built-in Logger. No changes to your existing logging code are required. Logs captured within Scout-tracked requests are automatically enriched with request context (request ID, transaction name, and custom context).

### Configuration

```elixir
config :scout_apm,
  logs_enabled: true,
  logs_ingest_key: "your-key",
  logs_level: :info,              # Minimum level to forward
  logs_filter_modules: []         # Modules to exclude
```

See [Log Management configuration](/docs/elixir/configuration#log-management-configurations) for all options.

## External Services

Scout automatically tracks outbound HTTP calls as "External Services", giving you visibility into time spent calling third-party APIs and services. HTTP clients are instrumented via `:telemetry`.

### Finch / Req

Finch instrumentation also covers libraries built on top of Finch, including [Req](https://github.com/wojtekmach/req).

Attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.FinchTelemetry.attach()
  # ...
end
```

No other changes are needed. All Finch HTTP requests will automatically appear as External Service spans in Scout.

### Tesla

Tesla requires the `Tesla.Middleware.Telemetry` middleware to be included in your client:

```elixir
defmodule MyApp.ApiClient do
  use Tesla

  plug Tesla.Middleware.Telemetry
  plug Tesla.Middleware.BaseUrl, "https://api.example.com"
  # ... other middleware
end
```

Then attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.TeslaTelemetry.attach()
  # ...
end
```

### What's Tracked

For both Finch and Tesla:
* **Operation**: `HTTP/{method}` (e.g., "HTTP/GET", "HTTP/POST")
* **URL**: The request URL (query strings are stripped to avoid leaking sensitive data)
* **Status Code**: The HTTP response status code
* **Duration**: Total request time

Requests to Scout APM's own endpoints are automatically excluded.

## LiveView Instrumentation

Scout automatically instruments Phoenix LiveView lifecycle callbacks via `:telemetry`.

### Setup

Attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.LiveViewTelemetry.attach()
  # ...
end
```

### What's Tracked

* **mount** â Tracked as LiveView transactions
* **handle_event** â Tracked as timed layers within transactions
* **handle_params** â Tracked as timed layers within transactions

LiveView modules are automatically named based on the module name.

## Oban Instrumentation

Scout automatically instruments [Oban](https://github.com/sorentwo/oban) background job execution via `:telemetry`.

### Setup

Attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.ObanTelemetry.attach()
  # ...
end
```

Jobs appear as `Job` type background transactions in Scout. Job names are derived from the worker module â for example, `MyApp.Workers.SendEmail` becomes `Job/SendEmail`.

## HEEx Template Instrumentation

Scout can instrument HEEx template rendering (Phoenix 1.6+) for visibility into template performance.

### Setup

Add the HEEx engine to your template engines configuration in `config/config.exs`:

```elixir
config :phoenix, :template_engines,
  eex: ScoutApm.Instruments.EExEngine,
  exs: ScoutApm.Instruments.ExsEngine,
  heex: ScoutApm.Instruments.HEExEngine
```

This requires `phoenix_live_view` to be a dependency in your project. No other setup is needed â HEEx templates will automatically appear as `Template/Render` spans in traces.

## Database Metrics

Ecto instrumentation now automatically captures additional database metrics:

* **`db.command`** â The SQL command type (e.g., SELECT, INSERT, UPDATE, DELETE)
* **`db.rows`** â The number of rows returned or affected

These are captured automatically with no additional setup beyond the standard [Ecto instrumentation](#installation).

## Server Timing

View performance metrics (time spent in Controller, Ecto, etc) for each of your app's requests in Chromeâs Developer tools with the [plug_server_timing](https://github.com/scoutapp/elixir_plug_server_timing) package. Production-safe.



For install instructions and configuration options, see [plug_server_timing](https://github.com/scoutapp/elixir_plug_server_timing) on GitHub.

## ARM Support

ARM and graviton Support

We now have support for ARM and graviton.
* Our Elixir agent does not automatically detect ARM support, currently
  - To explicitly connect, the [core_agent_triple](../../elixir/configuration#core_agent_triple) configuration setting must be specified.


# Features

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate specific deploys to changes in performance.

Scout identifies deploys via the following approaches:

* Setting the `revision_sha` configuration value:

```python
from scout_apm.api import Config
Config.set(revision_sha=os.popen("git rev-parse HEAD").read().strip())  # if the app directory is a git repo
```

* Setting a `SCOUT_REVISION_SHA` environment variable equal to the SHA of your latest release.
* If you are using Heroku, enable [Dyno Metadata](https://devcenter.heroku.com/articles/dyno-metadata). This adds a `HEROKU_SLUG_COMMIT` environment variable to your dynos, which Scout then associates with deploys.

## Request Queuing

Our Python integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.


## Custom Context

[Context](/docs/features/#context) lets you see the forest from the trees. For example, you can add custom context to answer critical questions like:

* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

It's simple to add [custom context](/docs/features/#context) to your app:

```python
import scout_apm.api
# scout_apm.api.Context.add(key, value)
scout_apm.api.Context.add("user_id", request.user.id)
```

### Context Key Restrictions

The Context `key` must be a `String` with only printable characters. Custom context keys may contain alphanumeric characters, dashes, and underscores. Spaces are not allowed.

Attempts to add invalid context will be ignored.

### Context Value Types

Context values can be any json-serializable type. Examples:

* `"1.1.1.1"`
* `"free"`
* `100`

### PII
To better protect your data, we suggest using ids instead of explicit names and emails

## Renaming Transactions

If you want to rename the current transaction, call `rename_transaction()` with the new name:

```python
import scout_apm.api

scout_apm.api.rename_transaction("Controller/" + "your_new_name_here")
```

You can use this whether the transaction was started from a built-in integration or custom instrumentation.

### GraphQL

If you have a GraphQL endpoint which serves any number of queries, you likely want to have each of those types of queries show up in the Scout UI as different endpoints. You can accomplish this by renaming the transaction during the request like so:

```python
import scout_apm.api

scout_apm.api.rename_transaction("Controller/" + derive_graphql_name())
```

Do not generate highly cardinality transaction names, like `ScoutApm::Transaction.rename("GraphQL/foobar_#{current_user.id}")`, as we limit the number of transactions that can be tracked. High-cardinality transaction names can quickly surpass this limit.

## Custom Instrumentation
You can extend Scout to trace transactions outside our officially supported frameworks (e.g. Cron jobs and micro web frameworks) and time the execution of code that falls outside our auto instrumentation.

### Transactions & Timing

Scoutâs instrumentation is divided into 2 areas:

1. __Transactions__: these wrap around a flow of work, like a web request or Cron job. The UI groups data under transactions. Use the `@scout_apm.api.WebTransaction()` decorator or wrap blocks of code via the `with scout_apm.api.WebTransaction('')` context manager.
2. __Timing__: these measure individual pieces of work, like an HTTP request to an outside service and display timing information within a transaction trace. Use the `@scout_apm.api.instrument()` decorator or the `with scout_apm.api.instrument() as instrument` context manager.

### Instrumenting transactions

A transaction groups a sequence of work under in the Scout UI. These are used to generate transaction traces. For example, you may create a transaction that wraps around the entire execution of a Python script that is ran as a Cron Job.

#### Limits

We limit the number of unique transactions that can be instrumented. Tracking too many unique transactions can impact the performance of our UI. Do not dynamically generate transaction names in your instrumentation (i.e. `with scout_apm.api.WebTransaction('update_user_"+user.id')`) as this can quickly exceed our rate limits. Use [context](/docs/python/features/#custom-context) to add high-dimensionality information instead.

#### Getting Started

Import the API module and configure Scout:

```python
import scout_apm.api

# A dict containing the configuration for APM.
# See our Python help docs for all configuration options.
config = {
    "name": "My App Name",
    "key": "APM_Key",
    "monitor": True,
}

# The `install()` method must be called early on within your app code in order
# to install the APM agent code and instrumentation.
scout_apm.api.install(config=config)
```

#### Web or Background transactions?

Scout distinguishes between two types of transactions:

* `WebTransaction`: For transactions that impact the user-facing experience. Time spent in these transactions will appear on your app overboard dashboard and appear in the "Web" area of the UI.
* `BackgroundTransaction`: For transactions that don't have an impact on the user-facing experience (example: cron jobs). These will be available in the "Background Jobs" area of the UI.

#### Explicit

```python
scout_apm.api.WebTransaction.start("Foo")  # or BackgroundTransaction.start()
# do some app work
scout_apm.api.WebTransaction.stop()
```

#### As a context manager

```python
with scout_apm.api.WebTransaction("Foo"):  # or BackgroundTransaction()
    # do some app work
```

#### As a decorator

```python
@scout_apm.api.WebTransaction("Foo")  # or BackgroundTransaction()
def my_foo_action(path):
    # do some app work
```

#### Cron Job Example

```python
#!/usr/bin/env python

import requests
import scout_apm.api

# A dict containing the configuration for APM.
# See our Python help docs for all configuration options.
config = {
    "name": "My App Name",
    "key": "YOUR_SCOUT_KEY",
    "monitor": True,
}

# The `install()` method must be called early on within your app code in order
# to install the APM agent code and instrumentation.
scout_apm.api.install(config=config)

# Will appear under Background jobs in the Scout UI
with scout_apm.api.BackgroundTransaction("Foo"):
    response = requests.get("https://httpbin.org/status/418")
    print(response.text)
```

### Timing functions and blocks of code

Traces that allocate significant amount of time to `View`, `Job`, or `Template` are good candidates to add custom instrumentation. This indicates a significant amount of time is falling outside our default instrumentation.

#### Limits

We limit the number of metrics that can be instrumented. Tracking too many unique metrics can impact the performance of our UI. Do not dynamically generate metric types in your instrumentation (ie `with scout_apm.api.instrument("Computation_for_user_" + user.id)`) as this can quickly exceed our rate limits.

For high-cardinality details, use tags: `with scout_apm.api.instrument("Computation", tags={"user": user.id})`.

#### Getting Started

Import the API module:

```python
import scout_apm.api

# or to not use the whole prefix on each call:
from scout_apm.api import instrument
```

```python
scout_apm.api.instrument(name, tags={}, kind="Custom")
```

* `name` - A semi-detailed version of what the section of code is. It should be static between different invocations of the method. Individual details like a user ID, or counts or other data points can be added as tags. Names like `retreive_from_api` or `GET` are good names.
* `kind` - A high level area of the application. This defaults to `Custom`. Your whole application should have a very low number of unique strings here. In our built-in instruments, this is things like `Template` and `SQL`. For custom instrumentation, it can be strings like `MongoDB` or `HTTP` or similar. This should not change based on input or state of the application.
* `tags` - Tagging adds context to the request, and can be viewed on the context tab of the trace, as well as on the trace explorer page. A dictionary of key/value pairs. Key should be a string, but value can be any json-able structure. High-cardinality fields like a user ID are permitted.

#### As a context manager

Wrap a section of code in a unique "span" of work.

The yielded object can be used to add additional tags individually.

```python
def foo():
    with scout_apm.api.instrument("Computation 1") as instrument:
        instrument.tag("record_count", 100)
        # Work

    with scout_apm.api.instrument("Computation 2", tags={"filtered_record_count": 50}) as instrument:
        # Work
```

#### As a decorator

Wraps a whole function, timing the execution of specified function within a transaction trace. This uses the same API as the ContextManager style.

```python
@scout_apm.api.instrument("Computation")
def bar():
    # Work
```

#### Instrumenting Async Code

The Python Agent supports decorating async functions for Python 3.6 and up. If you need to instrument an asynchronous function,
or a function that returns an awaitable, you can use the `async_` decorator to decorate your function:

```python
@scout_apm.api.WebTransaction.async_("Foo")
async def foo():
    # app work
@scout_apm.api.BackgroundTransaction.async_("Bar")
async def bar():
    # app work
@scout_apm.api.instrument.async_("Spam")
async def spam():
    # app work
# Use async_ even though this function doesn't use async def
# because it returns an awaitable.
@scout_apm.api.instrument.async_("Returns Awaitable")
def returns_awaitable():
    return spam()
```


**Note**:
*If you use the `async` decorator on a synchronous function that does not return an awaitable,a `RuntimeWarning` will be logged indicating that an awaitable was not awaited.*


## ARM and graviton Support

We now have support for ARM and graviton.
* Our Python agent automatically detects ARM support
  - To explicitly connect, the [core_agent_triple](../../python/configuration#core_agent_triple) configuration setting must be specified.


# Advanced-features

## PECL Extension

Several instruments require the native extension to be included, including timing of Redis, Elasticsearch, and Memcached.

For more information, or to compile manually, the [README](https://github.com/scoutapp/scout-apm-php-ext) has additional instructions.

```bash
sudo pecl install scoutapm
```

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate
specific deploys to changes in performance.

Scout identifies deploys via the following approaches:

* Detecting the current git sha (this is automatically detected when `composer install` is run)

* Setting the [SCOUT_REVISION_SHA](/docs/php/configuration#scout_revision_sha) environment variable equal to the SHA of your latest release during deployment: `git rev-parse --short HEAD`

## Request Queuing

Our PHP integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.

## Custom Context

[Context](/docs/features/#context) lets you see the key attributes of requests. For example,
you can add custom context to answer critical questions like:

* Which plan was the customer who had a slow request on?
* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

It's simple to add [custom context](/docs/features/#context) to your app:

```php
use Scoutapm\Laravel\Facades\ScoutApm; // Laravel only: Add near the other use statements

ScoutApm::addContext("Key", "Value");

// for example, passing in the user_id
// ScoutApm::addContext("user_id", Auth::id());

// or if you have an $agent instance:
$agent->addContext("Key", "Value");
```



### Context Key Restrictions

The Context `key` must be a `String` with only printable characters. Custom
context keys may contain alphanumeric characters, dashes, and underscores.
Spaces are not allowed.

Attempts to add invalid context will be ignored.

### Context Value Types

Context values can be any json-serializable type. Examples:

* `"1.1.1.1"`
* `"free"`
* `100`

### PII
To best help protect your data, we suggest using ids instead of explicit names and emails


## Custom Instrumentation

You can extend Scout to trace transactions outside our officially supported
libraries (e.g. Cron jobs and other web frameworks) and time the execution of
sections of code that falls outside our provided instrumentation.

### Transactions & Timing

Scoutâs instrumentation is divided into 2 areas:

1. __Transactions__: these wrap around an entire flow of work, like a web
   request or Cron job. The Scout Web UI groups data under transactions.
2. __Timing__: these measure small pieces of code that occur inside of a
   transaction, like an HTTP request to an outside service, or a database call.
   This is displayed within a transaction trace in the UI.

### Instrumenting Transactions

A transaction groups a sequence of work under in the Scout UI. These are used
to generate transaction traces. For example, you may create a transaction that
wraps around the entire execution of a PHP script that is ran as a Cron Job.

The Laravel instrumentation does this all for you. You only will need to
manually instrument transactions in special cases. Contact us at
support@scoutapm.com for help.

#### Limits

We limit the number of unique transactions that can be instrumented. Tracking
too many uniquely named transactions can impact the performance of the UI. Do not
dynamically generate transaction names in your instrumentation as this can quickly
exceed our rate limits. Use [context](/docs/php/features/#custom-context) to add
high-dimensionality information instead.

#### Web or Background transactions?

Scout distinguishes between two types of transactions:

* `WebTransaction`: For transactions that impact the user-facing experience.
  Time spent in these transactions will appear on your app overboard dashboard
  and appear in the "Web" area of the UI.
* `BackgroundTransaction`: For transactions that don't have an impact on the
  user-facing experience (example: cron jobs). These will be available in the
  "Background Jobs" area of the UI.

```php
$agent->webTransaction("GET Users", function() { ... your code ... });
$agent->send();
```

### Timing functions and blocks of code

In existing transactions, both automatically created with Laravel instruments,
and also manually created, you can time sections of code that are interesting
to your application.

Traces that allocate significant amount of time to `Controller` or `Job` layers
are good candidates to add custom instrumentation. This indicates a significant
amount of time is falling outside our default instrumentation.

#### Limits

We limit the number of metrics that can be instrumented. Tracking too many
unique metrics can impact the performance of our UI. Do not dynamically
generate metric types in your instrumentation as this can quickly exceed our
rate limits.

For high-cardinality details, use tags.

#### Getting Started

With existing code like:

```php
$request = new ServiceRequest();
$request->setApiVersion($version);
```

It is wrapped with instrumentation:

```php
// At top, with other imports
use Scoutapm\Laravel\Facades\ScoutApm;

// Replacing the above code
$request = ScoutApm::instrument(
    "Custom", // Kind
    "Building Service Request", // Name
    function ($span) use ($version) {
        $request = new ServiceRequest();
        $request->setApiVersion($version);
        return $request;
    }
);
```

* `kind` - A high level area of the application. This defaults to `Custom`.
  Your whole application should have a very low number of unique strings here.
  In our built-in instruments, this is things like `Template` and `SQL`. For
  custom instrumentation, it can be strings like `MongoDB` or `HTTP` or
  similar. This should not change based on input or state of the application.
* `name` - A semi-detailed version of what the section of code is. It should be
  static between different invocations of the method. Individual details like a
  user ID, or counts or other data points can be added as tags. Names like
  `retreive_from_api` or `GET` are good names.
* `span` - An object that represents instrumenting this section of code. You
  can set tags on it by calling `$span->tag("key", "value")`
* `tags` - A dictionary of key/value pairs. Key should be a string, but value
  can be any json-able structure. High-cardinality fields like a user ID are
  permitted.


  ## ARM and graviton Support

  We now have support for ARM and graviton.
  * Our PHP agent does not automatically detect ARM support, currently
    - To explicitly connect, the [core_agent_triple](/docs/php/configuration#core_agent_triple) configuration setting must be specified:

    ```bash
    SCOUT_CORE_AGENT_TRIPLE=aarch64-unknown-linux-musl
    SCOUT_CORE_AGENT_VERSION=v1.3.1
    ```


# Advanced-features

## Deploy Tracking

Scout can [track deploys](/docs/features#deploy-tracking), making it easier to correlate specific deploys to changes in performance.

To ensure scout tracks your deploy, please provide the `SCOUT_REVISION_SHA` environment variable. You may also set the `revisionSHA` on a `ScountConfiguration` object instance:

```javascript
const config = scout.buildScoutConfiguration({
    monitor: true,
    key: "<app key>",
    name: "<app name>",
    revisionSHA: "<sha>",
});
```
## Request Queuing

Our Node integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.

## Custom Context

[Context](/docs/features/#context) lets you see the key attributes of requests. For example,
you can add custom context to answer critical questions like:

* Which plan was the customer who had a slow request on?
* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

It's simple to add [custom context](/docs/features/#context) to your app:

```javascript
// Express only: Add context inside a handler function
app.get("/", (req, req) => {
  scout.api.Context.add("Key", "Value"); // returns a Promise
})
```

### Context Key Restrictions

The Context `key` must be a `String` with only printable characters. Custom
context keys may contain alphanumeric characters, dashes, and underscores.
Spaces are not allowed.

Attempts to add invalid context will be ignored.

### Context Value Types

Context values can be any json-serializable type. Examples:

* `"1.1.1.1"`
* `"free"`
* `100`

### PII
To best help protect your data, we suggest using ids instead of explicit names and emails

## Custom Instrumentation

You can extend Scout to trace transactions outside our officially supported libraries (e.g. Cron jobs and other web frameworks) and time the execution of sections of code that falls outside our provided instrumentation.

Asynchronous functionality can be marked as a transaction with code similar to the following:

```javascript
scout.api.WebTransaction.run("transaction-name", (finishTransaction) => {
   yourAsyncFunction()
   .then(() => finishTransaction())
   .catch(err => {
    // error handling code goes here
    finishTransaction();
   });
});
```

For Asynchronous functionality in a callback-passing style:

```javascript
scout.api.WebTransaction.run("transaction-name", (finishTransaction) => {
   yourCallbackStyleAsyncFunction((err) => {
    if (err) {
      // error handling code goes here
      return;
    }

    finishTransaction();
   });
});
```

Synchronous functionality can be marked as transactions with code similar to the following:

```javascript
scout.api.WebTransaction.runSync("sync-transaction-name", () => {
  yourSyncFunction();
});
```

### Transactions & Timing

Scoutâs instrumentation is divided into 2 areas:

1. __Transactions__: these wrap around an entire flow of work, like a web
   request or Cron job. The Scout Web UI groups data under transactions.
2. __Timing__: these measure small pieces of code that occur inside of a
   transaction, like an HTTP request to an outside service, or a database call.
   This is displayed within a transaction trace in the UI.

### Instrumenting Transactions

A transaction groups a sequence of work under in the Scout UI. These are used
to generate transaction traces. For example, you may create a transaction that
wraps around the entire execution of a NodeJS script that is ran as a Cron Job.

The Express integration does this all for you. You only will need to manually instrument transactions in special cases. [Contact us at support@scoutapm.com](mailto:support@scoutapm.com?subject=Custom%20Integration%20Assistance%20%5bYour%20App%5d) for help.

#### Limits

We limit the number of unique transactions that can be instrumented. Tracking
too many uniquely named transactions can impact the performance of the UI. Do not
dynamically generate transaction names in your instrumentation as this can quickly
exceed our rate limits. Use [context](/docs/node/advanced-features#custom-context) to add
high-dimensionality information instead.

#### Web or Background transactions?

Scout distinguishes between two types of transactions:

* `WebTransaction`: For transactions that impact the user-facing experience.
  Time spent in these transactions will appear on your app overboard dashboard
  and appear in the "Web" area of the UI.
* `BackgroundTransaction`: For transactions that don't have an impact on the
  user-facing experience (example: cron jobs). These will be available in the
  "Background Jobs" area of the UI.

```javascript
scout.api.WebTransaction.run("GET /users", () => { ... your code ... });
scout.api.BackgroundTransaction.run("your-bg-transaction", () => { ... your code ... });
```

### Timing functions and blocks of code

In existing transactions, both automatically created with Express instruments,
and also manually created, you can time sections of code that are interesting
to your application.

Traces that allocate significant amount of time to `Controller` or `Job` layers
are good candidates to add custom instrumentation. This indicates a significant
amount of time is falling outside our default instrumentation.

Asynchronous functionality may be instrumented with code similar to the following:

```javascript
// NOTE: The transaction is *implicit* inside of express route handlers, if you are using the express middleware
scout.api.WebTransaction.run("transaction-name", (finishTransaction) => {
  // Start the first instrumentation
  const first = scout.api.instrument("instrument-name", (finishInstrument) => {
    // instrument code
    return yourAsyncFunction()
        .then(() => finishInstrument());
  });

  // Start the second instrumentation
  scout.api.instrument("instrument-name", (finishInstrument) => {
    // instrument code
    return yourAsyncFunction()
        .then(() => finishInstrument());
  });

  // Finish the transaction once all instrumentations are recorded
  Promise.all([first, second])
    .then(() => finishTransaction());
});
```

For Asynchronous functionality in a callback-passing style:

```javascript
// NOTE: The transaction is *implicit* inside of express route handlers, if you are using the express middleware
scout.api.WebTransaction.run("transaction-name", (finishTransaction) => {
  // Start the first instrumentation
  const first = scout.api.instrument("first-instrumentation", (finishFirst) => {
    // instrument code
    yourCallbackStyleAsyncFunction((err) => {
      if (err) {
        // error handling code here
        return;
      }

      finishFirst();

      // Start a second instrumentation
      const second = scout.api.instrument("second-instrumentation", (finishSecond) => {
        // instrument code
        yourCallbackStyleAsyncFunction((err) => {
          if (err) {
            // error handling code here
            return;
          }

          finishSecond();
          finishTransaction();
        });
      });

    });
  });
});
```

Synchronous functionality can be instrumented with code similar to the following:

```javascript
// NOTE: The transaction is *implicit* inside of express route handlers, if you are using the express middleware
scout.api.WebTransaction.runSync("sync-transaction-name", (finishTransaction) => {
  scout.api.instrumentSync("first-instrumentation", () => {
    yourSyncFunction();
  });

  scout.api.instrumentSync("second-instrumentation", () => {
    yourSyncFunction();
  });
});
```

#### Limits

We limit the number of metrics that can be instrumented. Tracking too many
unique metrics can impact the performance of our UI. Do not dynamically
generate metric types in your instrumentation as this can quickly exceed our
rate limits.

For high-cardinality details, use context.

#### Getting Started

With existing code like:

```javascript
// A handler that handles GET /
const handler = (req, res) => {
    // Functionality here
};
```

The express middleware automatically wraps your request and handler with a transaction/instrumentation as if you'd written the following:

```javascript
scout.api.WebTransaction.run("Controller/GET /<your route>", finishTransaction => { // transaction name format is `<kind>/<name>`
  scout.api.instrument("Controller/GET /<your route>", finishSpan => { // instrumentation name format is `<kind>/<name>`
    // The original handler code
  });
});
```

* `kind` - A high level area of the application. This defaults to `Custom`.
  Your whole application should have a very low number of unique strings here.
  In our built-in instruments, this is things like `Template` and `SQL`. For
  custom instrumentation, it can be strings like `MongoDB` or `HTTP` or
  similar. This should not change based on input or state of the application.
* `name` - A semi-detailed version of what the section of code is. It should be
  static between different invocations of the method. Individual details like a
  user ID, or counts or other data points can be added as tags. Names like
  `retreive_from_api` or `GET` are good names.
* `span` - An object that represents instrumenting this section of code. You
  can set tags on it by calling `$span->tag("key", "value")`
* `tags` - A dictionary of key/value pairs. Key should be a string, but value
  can be any json-able structure. High-cardinality fields like a user ID are
  permitted.

  ## ARM and graviton Support

  We now have support for ARM and graviton.
  * Our Node agent does not automatically detect ARM support, currently
    - To explicitly connect, the [core_agent_triple](../../node/configuration#core_agent_triple) configuration setting must be specified.


# Advanced-features

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate changes in your app to performance. To enable deploy tracking, first ensure you are on the latest version of `scout_apm`. See our [upgrade instructions](/docs/ruby/#updating). 

Scout identifies deploys via the following: 

1. If you are using Capistrano, no extra configuration is required. Scout reads the contents of the `REVISION` and/or `revisions.log` file and parses out the SHA of the most recent release. 
2. If you are using Heroku, enable [Dyno Metadata](https://devcenter.heroku.com/articles/dyno-metadata). This adds a `HEROKU_SLUG_COMMIT` environment variable to your dynos, which Scout then associates with deploys. 
3. If you are deploying via a custom approach, set a `SCOUT_REVISION_SHA` environment variable equal to the SHA of your latest release. 
    - For example on fly.io you could set it with `fly deploy -e SCOUT_REVISION_SHA=$(git rev-parse --short HEAD)`
4. If the app resides in a Git repo, Scout parses the output of `git rev-parse --short HEAD` to determine the revision SHA.

## Request Queuing

Our Ruby integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.

## Auto Instruments

In many apps, more than 30% of the time spent in a transaction is within custom code written by your development team. In traces, this shows up as time spent in "Controller" or "Job". AutoInstruments helps break down the time spent in your custom code without the need to add custom instrumentation on your own.

AutoInstruments instruments code expressions in Ruby on Rails controllers by instrumenting Rubyâs Abstract Syntax Tree ([AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree)) as code is loaded. These code expressions then appear in traces, just like the many libraries Scout already instruments:



In the screenshot of a trace above, 68% of the time would be allocated to the `Controller` without enabling AutoInstruments. With AutoInstruments enabled, `Controller` time is just 3% of the request and we can clearly see that most of the time is spent inside two method calls.

AutoInstruments is currently available for Ruby on Rails applications.

### Enabling AutoInstruments

AutoInstruments is available to apps using Ruby 2.3.1+. To enable:

**1.** Within your Rails app's directory, run:
```bash
bundle update scout_apm
```

AutoInstruments was released in `scout_apm` version 2.6.0. 


**2.** Set the `auto_instruments` [config option](/docs/ruby/configuration#auto_instruments) to `true`.

If you are using a config file:
```yaml
# config/scout_apm.yml
production:
  auto_instruments: true
```
If you are using environment variables:

`SCOUT_AUTO_INSTRUMENTS=true`

**3.** Deploy

A [detailed AutoInstruments FAQ](/docs/faq/#auto-instruments) is available in our reference area.

**Troubleshooting**:
You may need to add/upgrade the `parser` gem. 

To verify this, set `log_level: debug` in your scout_apm.yml (`SCOUT_LOG_LEVEL: debug` if using environment variable configuration -- such as for Heroku), then check your log/scout_apm.log (if on Heroku check Logplex or your log drains) for the following debug level log:
`AutoInstruments is enabled, but Parser::TreeRewriter is missing. Update 'parser' gem to >= 2.5.0.`

The `parser` gem version works best when it matches the version of Ruby running your application (e.g. `parser v3.1.1.0` for Ruby `3.1.1`)
It is great, but we have seen issues even when `parser` was "ahead" of the Ruby version,
so we recommend matching as closely as possible. See [parser's README](https://github.com/whitequark/parser?tab=readme-ov-file#backwards-compatibility)
for more information.

## Custom Context 

[Context](/docs/features/#context) lets you see the forest from the trees. For example, you can add custom context to answer critical questions like:

* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

It's simple to add [custom context](/docs/features/#context) to your app. There are two types of context:

### User Context

For context used to identify users (ex: id):

```ruby
ScoutApm::Context.add_user({})
```

Examples:

```ruby
ScoutApm::Context.add_user(id: @user.id)
ScoutApm::Context.add_user(id: @user.id, location: @user.location.to_s)
```

### General Context

```ruby
ScoutApm::Context.add({})
```

Examples:

```ruby
ScoutApm::Context.add(account: @account.id)
ScoutApm::Context.add(database_shard: @db.shard_id, monthly_spend: @account.monthly_spend)
```

### Default Context

Scout reports the Request URI and the user's remote IP Address by default.

### Context Types

Context values can be any of the following types:

* Numeric
* String
* Boolean
* Time
* Date

### Context Field Name Restrictions

Custom context names may contain alphanumeric characters, dashes, and underscores. Spaces are not allowed.

Attempts to add invalid context will be ignored.

### Example: adding the current user's id as context

Add the following to your `ApplicationController` class:

```ruby
before_filter :set_scout_context
```

Create the following method:

```ruby
def set_scout_context
  ScoutApm::Context.add_user(id: current_user.id) if current_user.is_a?(User)
end
```

### Example: adding the monthly spend as context

Add the following line to the `ApplicationController#set_scout_context` method defined above:

```ruby
ScoutApm::Context.add(monthly_spend: current_org.monthly_spend) if current_org
```

### PII
To better protect your data, we suggest using ids instead of explicit names and emails

## Renaming transactions

There may be cases where you require more control over how Scout names transactions for your endpoints and background jobs.

For example, if you have a controller-action that renders both JSON and HTML formats and the rendering time varies significantly between the two, it may make sense to define a unique transaction name for each.

Use `ScoutApm::Transaction#rename`:

```ruby
class PostsController < ApplicationController
  def index                              
    ScoutApm::Transaction.rename("posts/foobar")                                   
    @posts = Post.all                    
  end
end
```

In the example above, the default name for the transaction is `posts/index`, which appears as `PostsController#index` in the Scout UI. Renaming the transaction to `posts/foobar` identifies the transaction as `PostsController#foobar` in the Scout UI.  

Do not generate highly cardinality transaction names (ex: `ScoutApm::Transaction.rename("posts/foobar_#{current_user.id}")`) as we limit the number of transactions that can be tracked. High-cardinality transaction names can quickly surpass this limit.

### GraphQL

If you have a GraphQL endpoint which serves any number of queries, you likely want to have each of those types of queries show up in the Scout UI as different endpoints. You can accomplish this by renaming the transaction during the request like so:

```ruby
scout_transaction_name = "GraphQL/" + operation_name
ScoutApm::Transaction.rename(scout_transaction_name)
```

Where `operation_name` is determined dynamically based on the GraphQL query. E.g. `get_profile`, `find_user`, etc.

Do not generate highly cardinality transaction names, like `ScoutApm::Transaction.rename("GraphQL/foobar_#{current_user.id}")`, as we limit the number of transactions that can be tracked. High-cardinality transaction names can quickly surpass this limit.

## Custom Instrumentation

Traces that allocate significant amount of time to `Controller` or `Job` are good candidates to add custom instrumentation. This indicates a significant amount of time is falling outside our default instrumentation.

### Limits

We limit the number of metrics that can be instrumented. Tracking too many unique metrics can impact the performance of our UI. Do not dynamically generate metric types in your instrumentation (ie `self.class.instrument("user_#{user.id}", "generate") { ... })` as this can quickly exceed our rate limits.

### Instrumenting method calls

To instrument a method call, add the following to the class containing the method:

```ruby
  class User
    include ScoutApm::Tracer

    def export_activity
      # Do export work
    end
    instrument_method :export_activity
  end
```

The call to `instrument_method` should be after the method definition.

#### Naming methods instrumented via `instrument_method`

In the example above, the metric will appear in traces as `User#export_activity`. On timeseries charts, the time will be allocated to a `Custom` type.

__To modify the type__:

```ruby
instrument_method :export_activity, type: 'Exporting'
```

A new `Exporting` metric will now appear on charts. The trace item will be displayed as `Exporting/User/export_activity`.

__To modify the name__:

```ruby
instrument_method :export_activity, type: 'Exporting', name: 'user_activity'
```

The trace item will now be displayed as `Exporting/user_activity`.

### Instrumenting blocks of code

To instrument a block of code, add the following:

```ruby
  class User
    include ScoutApm::Tracer

    def generate_profile_pic
      self.class.instrument("User", "generate_profile_pic") do
        # Do work
      end
    end
  end
```

#### Naming methods instrumented via `instrument(type, name)`

In the example above, the metric appear in traces as `User/generate_profile_pic`. On timeseries charts, the time will be allocated to a `User` type. To modify the type or simply, simply change the `instrument` corresponding method arguments.

## Environments

It typically makes sense to treat each environment (production, staging, etc) as a separate application within Scout and ignore the development and test environments. Configure a unique app name for each environment as Scout aggregates data by the app name.

There are 2 approaches:

### 1. Modifying your scout_apm.yml config file

Here's an example `scout_apm.yml` configuration to achieve this:

```yaml
common: &defaults
  name: <%= "YOUR_APP_NAME (#{Rails.env})" %>
  key: YOUR_KEY
  log_level: info
  monitor: true

production:
  <<: *defaults

development:
  <<: *defaults
  monitor: false

test:
  <<: *defaults
  monitor: false

staging:
  <<: *defaults
```

### 2. Setting the SCOUT_NAME environment variable

Setting the `SCOUT_NAME` and `SCOUT_MONITOR` environment variables will override settings settings your `scout_apm.yml` config file.

To isolate data for a staging environment: `SCOUT_NAME="YOUR_APP_NAME (Staging)"`.

To disable monitoring: `SCOUT_MONITOR=false`.

See the full list of [configuration options](/docs/ruby/configuration).

## Disabling a Node

To disable Scout APM on any node in your environment, just set `monitor: false` in your `scout_apm.yml` configuration file on that server, and restart your app server. Example:

```yaml
common: &defaults
  name: <%= "YOUR_APP_NAME (#{Rails.env})" %>
  key: YOUR_KEY
  log_level: info
  monitor: false

production:
  <<: *defaults
```

Since the YAML config file allows ERB evaluation, you can even programatically enable/disable nodes based on host name. This example enables Scout APM on web1 through web5:

```yaml
common: &defaults
  name: <%= "YOUR_APP_NAME (#{Rails.env})" %>
  key: YOUR_KEY
  log_level: info
  monitor: <%= Socket.gethostname.match(/web[1..5]/) %>

production:
  <<: *defaults
```

After you've disabled a node in your configuration file and restarted your app server, the node show up as inactive in the UI after 10 minutes.


# Advanced-features

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate changes in your app to performance. To enable deploy tracking, first ensure you are on the latest version of `scout_apm`. See our [upgrade instructions](/docs/elixir/#updating-to-newest-version).

Scout identifies deploys via the following:

1. A `revision_sha` config setting.
2. A `SCOUT_REVISION_SHA` environment variable equal to the SHA of your latest release.
3. If you are using Heroku, enable [Dyno Metadata](https://devcenter.heroku.com/articles/dyno-metadata). This adds a `HEROKU_SLUG_COMMIT` environment variable to your dynos, which Scout then associates with deploys.

## Request Queuing

Our Elixir integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.

__Note:__ For Elixir, we currently only support the following two headers: `x-queue-start` and `x-request-start`, and we don't support msec -- or decimal millisecond. Example of valid header:
`x-request-start: "1234567890123"`


## Custom Context

[Context](/docs/features/#context) lets you see the forest from the trees.
For example, you can add custom context to answer critical questions like:
* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers? It's simple to add [custom context](/docs/features/#context) to your app. There are two types of context:

### User Context
For context used to identify users (ex: id):
```elixir
ScoutApm.add_user(key, value)
```
Examples:

```elixir
ScoutApm.Context.add_user(:id, user.id)
```
### General Context
```elixir
ScoutApm.Context.add(key, value)
```
Examples:
```elixir
ScoutApm.Context.add(:account, account.id)
ScoutApm.Context.add(:monthly_spend, account.monthly_spend)
```
### Default Context
Scout reports the Request URI and the user's remote IP Address by default.
### Context Value Types Context values can be any of the following types:
* Printable strings (`String/printable?/1` returns `true`) * Boolean * Number
### Context Key Restrictions
Context keys can be an `Atom` or `String` with only printable characters.
Custom context keys may contain alphanumeric characters, dashes, and underscores. Spaces are not allowed. Attempts to add invalid context will be ignored.
### PII
To best help protect you data, we suggest using ids instead of explicit names and emails


## Custom Instrumentation

You can extend Scout to record additional types of transactions (background jobs, for example) and time the execution of code that fall outside our auto instrumentation.

For full details on instrumentation functions, see our [ScoutApm. Tracing Hex docs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html).

### Transactions & Timing

Scoutâs instrumentation is divided into 2 areas:

**1.**
__Transactions__: these wrap around a flow of work, like a web request or a GenServer call. The UI groups data under transactions. Use the `deftransaction/2` macro or wrap blocks of code with the `transaction/4` macro.

**2.**
 __Timing__: these measure individual pieces of work, like an HTTP request to an outside service or an Ecto query, and displays timing information within a transaction trace. Use the `deftiming/2` macro or the `timing/4` macro.

### Instrumenting transactions
#### deftransaction Macro Example

Replace your function `def` with `deftransaction` to instrument it.

You can override the name and type by setting the `@transaction_opts` attribute right before the function.

```elixir
defmodule YourApp.Web.RoomChannel do
use Phoenix.Channel import ScoutApm.Tracing

# Will appear under "Web" in the UI, named "YourApp.Web.RoomChannel.join".
@transaction_opts [type: "web"]
deftransaction join("topic:html", _message, socket) do
  {:ok, socket}
end

# Will appear under "Background Jobs" in the UI, named "RoomChannel.ping".
@transaction_opts [type: "background", name: "RoomChannel.ping"]
deftransaction handle_in("ping", %{"body" => body}, socket) do
  broadcast! socket, "new_msg", %{body: body} {:noreply, socket}
end
```

#### transaction/4 Example
Wrap the block of code you'd like to instrument with `transaction/4`:
```elixir
import ScoutApm.Tracking def
  do_async_work do Task.start(fn ->
    # Will appear under "Background Jobs" in the UI, named "Do Work".
    transaction(:background, "Do Work") do
      # Do work...
    end
  end)
end
```
See the [ScoutApm.Tracing Hexdocs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html) for details on instrumenting transactions.

### Timing functions and blocks of code

#### deftiming Macro Example

Replace your function `def` with `deftiming` to instrument it. You can override the name and category by setting the `@timing_opts` attribute right before the function.

```elixir
defmodule Searcher do
 import ScoutApm.Tracing

 # Time associated with this function will appear under "Hound" in timeseries charts.
 # The function will appear as `Hound/open_search` in transaction traces.
 @timing_opts [category: "Hound"] deftiming open_search(url) do
  navigate_to(url)
 end

 # Time associated with this function will appear under "Hound" in timeseries charts.
 # The function will appear as `Hound/homepage` in transaction traces.

 @timing_opts [category: "Hound", name: "homepage"]
 deftiming open_homepage(url) do
   navigate_to(url)
end
```
#### timing/4 Example

Wrap the block of code you'd like to instrument with `timing/4`:
```elixir
defmodule PhoenixApp.PageController do
use PhoenixApp.Web, :controller import ScoutApm.Tracing
def index(conn, _params) do
  timing("Timer", "sleep") do
    :timer.sleep(3000)
  end
  render conn, "index.html"
end
```
See the [ScoutApm.Tracing Hexdocs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html) for details on timing functions and blocks of code. #### Limits on category arity We limit the number of unique categories that can be instrumented. Tracking too many unique category can impact the performance of our UI. Do not dynamically generate categories in your instrumentation (ie `timing("user_#{user.id}", "generate", do: do_work())` as this can quickly exceed our rate limits.

#### Adding a description

Call `ScoutApm.Tracing.update_desc/1` to add relevant information to the instrumented item. This description is then viewable in traces. An example:
```elixir
timing("HTTP", "GitHub_Avatar") do
  url = "https://github.com/#{user.id}.png"
  update_desc("GET #{url}")
  HTTPoison.get(url)
end
```

#### Tracking

Already executed time Libraries like Ecto log details on executed queries. This includes timing information. To add a trace item for this, use `ScoutApm.Tracing.track`.
An example:
```elixir
defmodule YourApp.Mongo.Repo do
  use Ecto.Repo # Scout instrumentation of Mongo queries. These appear in traces as "Ecto/Read", "Ecto/Write", etc.

  def log(entry) do
    ScoutApm.Tracing.track( "Ecto", query_name(entry), entry.query_time, :microseconds )
    super entry
  end
end
```

In the example above, the metric will appear in traces as `Ecto/#{query_time(entry)}`. On timeseries charts, the time will be allocated to `Ecto`. [See the scout_apm hex docs](https://hexdocs.pm/scout_apm/ScoutApm.Tracing.html#track/5) for more information on `track/`.

## Error Monitoring

Scout automatically captures unhandled exceptions in your Phoenix application. See the [Error Monitoring feature page](/docs/features/error-monitoring) for full details on the Scout Error Monitoring UI.

### Setup

Attach the Phoenix error telemetry handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.PhoenixErrorTelemetry.attach()
  # ...
end
```

Error monitoring is enabled by default (`errors_enabled: true`). No additional configuration is required.

### Manual Error Capture

You can also capture errors manually:

```elixir
try do
  some_risky_operation()
rescue
  e ->
    ScoutApm.Error.capture(e, stacktrace: __STACKTRACE__)
    reraise e, __STACKTRACE__
end
```

With additional context:

```elixir
ScoutApm.Error.capture(e,
  stacktrace: __STACKTRACE__,
  context: %{user_id: user.id},
  request_path: "/api/users",
  request_params: %{action: "update"}
)
```

### Configuration

```elixir
config :scout_apm,
  errors_enabled: true,
  errors_ignored_exceptions: [Phoenix.Router.NoRouteError],
  errors_filter_parameters: ["password", "credit_card"]
```

See [Error Monitoring configuration](/docs/elixir/configuration#error-monitoring-configurations) for all options.

## Log Management

Scout can forward your application logs for centralized search and analysis. See the [Log Management feature page](/docs/features/log-management) for full details on the Scout Log Management UI.

### Setup

**1.** Enable log management in your config and provide an ingest key (available in the Logs page of your Scout app):

```elixir
config :scout_apm,
  logs_enabled: true,
  logs_ingest_key: "your-logs-ingest-key"
```

**2.** Attach the log handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Logging.attach()
  # ...
end
```

Once enabled, Scout integrates with Elixir's built-in Logger. No changes to your existing logging code are required. Logs captured within Scout-tracked requests are automatically enriched with request context (request ID, transaction name, and custom context).

### Configuration

```elixir
config :scout_apm,
  logs_enabled: true,
  logs_ingest_key: "your-key",
  logs_level: :info,              # Minimum level to forward
  logs_filter_modules: []         # Modules to exclude
```

See [Log Management configuration](/docs/elixir/configuration#log-management-configurations) for all options.

## External Services

Scout automatically tracks outbound HTTP calls as "External Services", giving you visibility into time spent calling third-party APIs and services. HTTP clients are instrumented via `:telemetry`.

### Finch / Req

Finch instrumentation also covers libraries built on top of Finch, including [Req](https://github.com/wojtekmach/req).

Attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.FinchTelemetry.attach()
  # ...
end
```

No other changes are needed. All Finch HTTP requests will automatically appear as External Service spans in Scout.

### Tesla

Tesla requires the `Tesla.Middleware.Telemetry` middleware to be included in your client:

```elixir
defmodule MyApp.ApiClient do
  use Tesla

  plug Tesla.Middleware.Telemetry
  plug Tesla.Middleware.BaseUrl, "https://api.example.com"
  # ... other middleware
end
```

Then attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.TeslaTelemetry.attach()
  # ...
end
```

### What's Tracked

For both Finch and Tesla:
* **Operation**: `HTTP/{method}` (e.g., "HTTP/GET", "HTTP/POST")
* **URL**: The request URL (query strings are stripped to avoid leaking sensitive data)
* **Status Code**: The HTTP response status code
* **Duration**: Total request time

Requests to Scout APM's own endpoints are automatically excluded.

## LiveView Instrumentation

Scout automatically instruments Phoenix LiveView lifecycle callbacks via `:telemetry`.

### Setup

Attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.LiveViewTelemetry.attach()
  # ...
end
```

### What's Tracked

* **mount** â Tracked as LiveView transactions
* **handle_event** â Tracked as timed layers within transactions
* **handle_params** â Tracked as timed layers within transactions

LiveView modules are automatically named based on the module name.

## Oban Instrumentation

Scout automatically instruments [Oban](https://github.com/sorentwo/oban) background job execution via `:telemetry`.

### Setup

Attach the handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.ObanTelemetry.attach()
  # ...
end
```

Jobs appear as `Job` type background transactions in Scout. Job names are derived from the worker module â for example, `MyApp.Workers.SendEmail` becomes `Job/SendEmail`.

## HEEx Template Instrumentation

Scout can instrument HEEx template rendering (Phoenix 1.6+) for visibility into template performance.

### Setup

Add the HEEx engine to your template engines configuration in `config/config.exs`:

```elixir
config :phoenix, :template_engines,
  eex: ScoutApm.Instruments.EExEngine,
  exs: ScoutApm.Instruments.ExsEngine,
  heex: ScoutApm.Instruments.HEExEngine
```

This requires `phoenix_live_view` to be a dependency in your project. No other setup is needed â HEEx templates will automatically appear as `Template/Render` spans in traces.

## Database Metrics

Ecto instrumentation now automatically captures additional database metrics:

* **`db.command`** â The SQL command type (e.g., SELECT, INSERT, UPDATE, DELETE)
* **`db.rows`** â The number of rows returned or affected

These are captured automatically with no additional setup beyond the standard [Ecto instrumentation](#installation).

## Server Timing

View performance metrics (time spent in Controller, Ecto, etc) for each of your app's requests in Chromeâs Developer tools with the [plug_server_timing](https://github.com/scoutapp/elixir_plug_server_timing) package. Production-safe.



For install instructions and configuration options, see [plug_server_timing](https://github.com/scoutapp/elixir_plug_server_timing) on GitHub.

## ARM Support

ARM and graviton Support

We now have support for ARM and graviton.
* Our Elixir agent does not automatically detect ARM support, currently
  - To explicitly connect, the [core_agent_triple](../../elixir/configuration#core_agent_triple) configuration setting must be specified.


# Advanced-features

## Deploy Tracking

Scout can [track deploys](/docs/features/#deploy-tracking), making it easier to correlate specific deploys to changes in performance.

Scout identifies deploys via the following approaches:

* Setting the `revision_sha` configuration value:

```python
from scout_apm.api import Config
Config.set(revision_sha=os.popen("git rev-parse HEAD").read().strip())  # if the app directory is a git repo
```

* Setting a `SCOUT_REVISION_SHA` environment variable equal to the SHA of your latest release.
* If you are using Heroku, enable [Dyno Metadata](https://devcenter.heroku.com/articles/dyno-metadata). This adds a `HEROKU_SLUG_COMMIT` environment variable to your dynos, which Scout then associates with deploys.

## Request Queuing

Our Python integration can measure the time it takes a request to reach your application from farther upstream (a load balancer or web server). This appears in Scout as "Request Queueing" and provides an indication of your application's capacity. Large request queueing time is an indication that your app needs more capacity.

Please view [request queueing section](/docs/features/#request-queuing) to learn how to get these insights.


## Custom Context

[Context](/docs/features/#context) lets you see the forest from the trees. For example, you can add custom context to answer critical questions like:

* How many users are impacted by slow requests?
* How many trial customers are impacted by slow requests?
* How much of an impact are slow requests having on our highest paying customers?

It's simple to add [custom context](/docs/features/#context) to your app:

```python
import scout_apm.api
# scout_apm.api.Context.add(key, value)
scout_apm.api.Context.add("user_id", request.user.id)
```

### Context Key Restrictions

The Context `key` must be a `String` with only printable characters. Custom context keys may contain alphanumeric characters, dashes, and underscores. Spaces are not allowed.

Attempts to add invalid context will be ignored.

### Context Value Types

Context values can be any json-serializable type. Examples:

* `"1.1.1.1"`
* `"free"`
* `100`

### PII
To better protect your data, we suggest using ids instead of explicit names and emails

## Renaming Transactions

If you want to rename the current transaction, call `rename_transaction()` with the new name:

```python
import scout_apm.api

scout_apm.api.rename_transaction("Controller/" + "your_new_name_here")
```

You can use this whether the transaction was started from a built-in integration or custom instrumentation.

### GraphQL

If you have a GraphQL endpoint which serves any number of queries, you likely want to have each of those types of queries show up in the Scout UI as different endpoints. You can accomplish this by renaming the transaction during the request like so:

```python
import scout_apm.api

scout_apm.api.rename_transaction("Controller/" + derive_graphql_name())
```

Do not generate highly cardinality transaction names, like `ScoutApm::Transaction.rename("GraphQL/foobar_#{current_user.id}")`, as we limit the number of transactions that can be tracked. High-cardinality transaction names can quickly surpass this limit.

## Custom Instrumentation
You can extend Scout to trace transactions outside our officially supported frameworks (e.g. Cron jobs and micro web frameworks) and time the execution of code that falls outside our auto instrumentation.

### Transactions & Timing

Scoutâs instrumentation is divided into 2 areas:

1. __Transactions__: these wrap around a flow of work, like a web request or Cron job. The UI groups data under transactions. Use the `@scout_apm.api.WebTransaction()` decorator or wrap blocks of code via the `with scout_apm.api.WebTransaction('')` context manager.
2. __Timing__: these measure individual pieces of work, like an HTTP request to an outside service and display timing information within a transaction trace. Use the `@scout_apm.api.instrument()` decorator or the `with scout_apm.api.instrument() as instrument` context manager.

### Instrumenting transactions

A transaction groups a sequence of work under in the Scout UI. These are used to generate transaction traces. For example, you may create a transaction that wraps around the entire execution of a Python script that is ran as a Cron Job.

#### Limits

We limit the number of unique transactions that can be instrumented. Tracking too many unique transactions can impact the performance of our UI. Do not dynamically generate transaction names in your instrumentation (i.e. `with scout_apm.api.WebTransaction('update_user_"+user.id')`) as this can quickly exceed our rate limits. Use [context](/docs/python/features/#custom-context) to add high-dimensionality information instead.

#### Getting Started

Import the API module and configure Scout:

```python
import scout_apm.api

# A dict containing the configuration for APM.
# See our Python help docs for all configuration options.
config = {
    "name": "My App Name",
    "key": "APM_Key",
    "monitor": True,
}

# The `install()` method must be called early on within your app code in order
# to install the APM agent code and instrumentation.
scout_apm.api.install(config=config)
```

#### Web or Background transactions?

Scout distinguishes between two types of transactions:

* `WebTransaction`: For transactions that impact the user-facing experience. Time spent in these transactions will appear on your app overboard dashboard and appear in the "Web" area of the UI.
* `BackgroundTransaction`: For transactions that don't have an impact on the user-facing experience (example: cron jobs). These will be available in the "Background Jobs" area of the UI.

#### Explicit

```python
scout_apm.api.WebTransaction.start("Foo")  # or BackgroundTransaction.start()
# do some app work
scout_apm.api.WebTransaction.stop()
```

#### As a context manager

```python
with scout_apm.api.WebTransaction("Foo"):  # or BackgroundTransaction()
    # do some app work
```

#### As a decorator

```python
@scout_apm.api.WebTransaction("Foo")  # or BackgroundTransaction()
def my_foo_action(path):
    # do some app work
```

#### Cron Job Example

```python
#!/usr/bin/env python

import requests
import scout_apm.api

# A dict containing the configuration for APM.
# See our Python help docs for all configuration options.
config = {
    "name": "My App Name",
    "key": "YOUR_SCOUT_KEY",
    "monitor": True,
}

# The `install()` method must be called early on within your app code in order
# to install the APM agent code and instrumentation.
scout_apm.api.install(config=config)

# Will appear under Background jobs in the Scout UI
with scout_apm.api.BackgroundTransaction("Foo"):
    response = requests.get("https://httpbin.org/status/418")
    print(response.text)
```

### Timing functions and blocks of code

Traces that allocate significant amount of time to `View`, `Job`, or `Template` are good candidates to add custom instrumentation. This indicates a significant amount of time is falling outside our default instrumentation.

#### Limits

We limit the number of metrics that can be instrumented. Tracking too many unique metrics can impact the performance of our UI. Do not dynamically generate metric types in your instrumentation (ie `with scout_apm.api.instrument("Computation_for_user_" + user.id)`) as this can quickly exceed our rate limits.

For high-cardinality details, use tags: `with scout_apm.api.instrument("Computation", tags={"user": user.id})`.

#### Getting Started

Import the API module:

```python
import scout_apm.api

# or to not use the whole prefix on each call:
from scout_apm.api import instrument
```

```python
scout_apm.api.instrument(name, tags={}, kind="Custom")
```

* `name` - A semi-detailed version of what the section of code is. It should be static between different invocations of the method. Individual details like a user ID, or counts or other data points can be added as tags. Names like `retreive_from_api` or `GET` are good names.
* `kind` - A high level area of the application. This defaults to `Custom`. Your whole application should have a very low number of unique strings here. In our built-in instruments, this is things like `Template` and `SQL`. For custom instrumentation, it can be strings like `MongoDB` or `HTTP` or similar. This should not change based on input or state of the application.
* `tags` - Tagging adds context to the request, and can be viewed on the context tab of the trace, as well as on the trace explorer page. A dictionary of key/value pairs. Key should be a string, but value can be any json-able structure. High-cardinality fields like a user ID are permitted.

#### As a context manager

Wrap a section of code in a unique "span" of work.

The yielded object can be used to add additional tags individually.

```python
def foo():
    with scout_apm.api.instrument("Computation 1") as instrument:
        instrument.tag("record_count", 100)
        # Work

    with scout_apm.api.instrument("Computation 2", tags={"filtered_record_count": 50}) as instrument:
        # Work
```

#### As a decorator

Wraps a whole function, timing the execution of specified function within a transaction trace. This uses the same API as the ContextManager style.

```python
@scout_apm.api.instrument("Computation")
def bar():
    # Work
```

#### Instrumenting Async Code

The Python Agent supports decorating async functions for Python 3.6 and up. If you need to instrument an asynchronous function,
or a function that returns an awaitable, you can use the `async_` decorator to decorate your function:

```python
@scout_apm.api.WebTransaction.async_("Foo")
async def foo():
    # app work
@scout_apm.api.BackgroundTransaction.async_("Bar")
async def bar():
    # app work
@scout_apm.api.instrument.async_("Spam")
async def spam():
    # app work
# Use async_ even though this function doesn't use async def
# because it returns an awaitable.
@scout_apm.api.instrument.async_("Returns Awaitable")
def returns_awaitable():
    return spam()
```


**Note**:
*If you use the `async` decorator on a synchronous function that does not return an awaitable,a `RuntimeWarning` will be logged indicating that an awaitable was not awaited.*


## ARM and graviton Support

We now have support for ARM and graviton.
* Our Python agent automatically detects ARM support
  - To explicitly connect, the [core_agent_triple](../../python/configuration#core_agent_triple) configuration setting must be specified.


# Alerting

Alerting keeps your team updated if your app's performance degrades. Alerts can be configured on the app as a whole as well as on individual endpoints and background jobs. Metrics include:

Web Requests:
* Mean Response Time
* 95th Percentile Response Time
* Apdex
* Error Rate
* Throughput
* Queue Time

Background Jobs:
* Mean Response Time
* Error Rate
* Throughput
* Queue Time


### Setting Up Alerts

There are four parts to alerting, the alert event, the alert conditon, the notification group, and notification channels.

While we will discuss them in this order, it makes more sense to actually create these in reverse order. Starting with first creating a notification channel, then adding this notification channel to a notification group, then assigning this notification group to be notified when alerts are created from the alert condition.

To get started, head to your orgâs settings menu:


**Alert event**:

An alert event is created anytime the threshold is passed for an alert condition. This alert event will either be an open event, or a closed event. For example, see the Slack notification alerts below:



**Alert Conditions**:

An alert condition is what creates the alert events. Alert conditions are set to check for if the payloads we have received are either great than or lower than one of the metrics listed above.

For example, you can set an alert condition to trigger an alert whenever throughput for all your endpoints exceeds 1000 RPM:



**Notification group**:

When an alert condition's threshold has been passed, and an alert has been created, the alert condition will notify the notification group. The notification group will then pass this message to all of its notification channels. For example, if a Slack notification channel, an email notification channel, and a Splunk notification channel are all part of the same group, they will all be notified of the alert event (they will receive both open and close events).



**Notification Channel**:

A notification channel belongs to a notification group, and is a specific channel that you want to notify. [Alerting integrations](/docs/integrations/#alerting) aren't just limited to a single notification. For example, you can have multiple Slack notification channels, with each notifying a different slack... channel. A better example is PagerDuty, you can have multiple PagerDuty notification channels, with each channel having a different alert level.


# Alerting

## Slack

To integrate with Slack, head to the notification channels page via the following [URL](https://scoutapm.com/notification_channels), or by heading to the Alerts & Notification dropdown tab and heading to Notification Channels on the left sidebar:



Then select Slack Alert button in the bottom right:



Once on the "New Slack Channel" page, click the "Add to Slack" button. This will redirect you to Slack



Once on Slack, you will need to give Scout authorization to your workspace



Once you have given Scout authorization, you will be redirected to scoutapm.com, and a "Slack Integration Successful" message should be shown. Click on the "Create a Slack notification channel" to be brought back to the "New Slack Channel" page.



Give the channel a name, and select the channel from the datalist that you would like to send Slack alerts to. 



Test it out! You can now test out the Slack integration via clicking the "Send test alert" button. Once you have set up alerts, you will see messages similar to:



Once you have created the integration/channel, you can now add the channel to a (or multiple) notification group(s). When you create alerts, you assign a notification group to alert. That way when an alert occurs all of the channels in that group get notified:

Once on the Notification Groups page, you can either add it to the default notification group, or create a new one:



### Error Notifications

To use this integration for Error Notifications, once you have added the channel to a notification group (such as in the example above), you will then need to add this notification group to the app's error notifications group. 

To do so, head to the "Error Notifications" link on the left hand side on the Alerts and Notifications page, and add the recently created (or updated "Default") notification group that contains the Slack integraiton channel.



### Private Channels 

If you are trying to send Slack notification to private channels, you will need to first invite/add the Scout APM `@Scout APM` app to the channel, then reload the notification channel page, and the channel should appear in the list.

#### Support

If you need help with this integration, please email us at [support](mailto:support@scoutapm.com).

#### User Data
To review and understand how we use and protect our users data, please visit our [privacy policy page](https://scoutapm.com/privacy).

## PagerDuty

### Integration key from PagerDuty
To integrate PagerDuty with Scout's Alert Notification system, first head over to pagerduty.com, log in to your account, and head to Services > Service Directory



Once one the Service Directory page, use the button in the upper right corner to create a new service.



On the new Service page, search for the Scout APM integration in the Integration Type field. Fill in the below fields to your liking.



Once you have saved the service, you will be able to grab the integration key on the "Integrations" tab. Copy this key and headback over to scoutapm.com



### Adding PagerDuty to Scout

Head back to scoutapm.com, and head to the notification channels page via the following [URL](https://scoutapm.com/notification_channels), or via heading to the Alerts & Notification dropdown tab and heading to Notification Channels on the left-hand sidebar:




To add a PagerDuty notification channel, click the "PagerDuty Alert" button in the bottom right:



Add a name for the Channel, then add the integration key you got when creating the ruleset on pagerduty into the API key field, and set the alert level you'd like this notificiation channel to be at



Once you have created the integration/channel, you can now add the channel to an (or multiple) notification group(s). When you create alerts, you assign a notification group to alert. That way when an alert occurs all of the channels in that group get notified:

Once on the Notification Group page, you can either add it to the default notification group, or create a new one:



### Error Notifications

To use this integration for Error Notifications, once you have added the channel to a notification group (such as in the example above), you will then need to add this notification group to the app's error notifications group. 

To do so, head to the "Error Notifications" link on the left hand side on the Alerts & Notifications page, and add the recently created (or updated "Default") notification group that contains the PagerDuty channel.



#### Support

If you need help with this integration, please email us at [support](mailto:support@scoutapm.com).

## Splunk On-Call
*Formerly Victorops*

### Integration URI from Splunk

To integrate Splunk On-Call with Scout's Alert Notification system, first head to integrations page on your account and search for the Scout integration and enable it



Once you have enabled the Scout integration, copy the Service API Key (such as 372b7111-casd-1234-5678-90cb1af0129f).



### Adding Splunk to Scout

Head back to scoutapm.com, and head to the notification channels page via the following [URL](https://scoutapm.com/notification_channels), or by heading to the Alerts & Notification dropdown tab and heading to Notification Channels on the left-hand sidebar:




To add a Splunk On-Call notification channel, click the "Splunk On-Call Alert" button in the bottom right:



Add a name for the Channel, then add the Service API key that you were presented with on the integration page. If you have a routing key that would like to set, place it in the routing key area. Then set the alerting level that you would like



Once you have created the integration/channel, you can now add the channel to an (or multiple) notification group(s). When you create alerts, you assign a notification group to alert. That way when an alert occurs all of the channels in that group get notified:

Once on the Notification Group page, you can either add it to the default notification group, or create a new one:



### Error Notifications

To use this integration for Error Notifications, once you have added the channel to a notification group (such as in the example above), you will then need to add this notification group to the app's error notifications group. 

To do so, head to the "Error Notifications" link on the left hand side on the Alerts & Notifications page, and add the recently created (or updated "Default") notification group that contains the Splunk On-Call channel.



#### Support

If you need help with this integration, please email us at [support](mailto:support@scoutapm.com).

## Opsgenie

### Integration key from Opsgenie
**Note** Requires a Standard plan or higher.

To integrate Opsgenie with Scout's Alert Notification system, first head over to opsgenie.com, log in to your account, and head to the settings page



Once one the settings page, on the left hand sidebar find the integrations list. On the integration list page, add a new API Integration:



On the Add API integration page, set the name to Scout, and set the values you'd like. We will need Create and Update privileges. Then Copy the API key and save the integration:



### Adding Opsgenie to Scout

Head back to scoutapm.com, and head to the notification channels page via the following [URL](https://scoutapm.com/notification_channels), or by heading to the Alerts & Notification dropdown tab and heading to Notification Channels on the left-hand sidebar:




To add a Opsgenie notification channel, click the "Opsgenie Alert" button in the bottom right:



Add a name for the Channel, then add the API key the API key field, and set the alert level you'd like this notificiation channel to be at



Once you have created the integration/channel, you can now add the channel to an (or multiple) notification group(s). When you create alerts, you assign a notification group to alert. That way when an alert occurs all of the channels in that group get notified:

Once on the Notification Group page, you can either add it to the default notification group, or create a new one:



### Error Notifications

To use this integration for Error Notifications, once you have added the channel to a notification group (such as in the example above), you will then need to add this notification group to the app's error notifications group. 

To do so, head to the "Error Notifications" link on the left hand side on the Alerts and Notifications page, and add the recently created (or updated "Default") notification group that contains the Opsgenie channel.



#### Support

If you need help with this integration, please email us at [support](mailto:support@scoutapm.com).

## Zapier

To integrate Zapier with Scout's Alert Notification system, you can utilize the Webhook feature on the *Application > Notification Channels* page. In this example, we will show how to setup Slack using Zapier.

### Zapier Configuration

First of all you will need to create an account with [Zapier](https://zapier.com/), and once you have done this, you can go ahead and create a *Zap*, by clicking on the Make a Zap! button on the top right-hand side of the screen, as shown in the image below.



You need to create a *Trigger* (for Scout) and an *Action* (for Slack) in order to make the two systems able to communicate. First of all, create the trigger by selecting *Webhooks by Zapier* as the App you want to work with.



Next you will need to select the type of trigger that you want, select *Catch Hook*. Next you will be given a URL, which is the Webhook that we will use to link to in Scout. Copy this URL and then open up Scout.



### Scout Configuration

In Scout, navigate to *Application > Notification Channels* and create a new Webhook, like the picture below, copying in the Zapier URL.



Next you will need to add or edit a Notification Group to include this new channel.



### Create an Alert

At this point if you try to carry on creating the Zap in Zapier, it will try to pull a sample Alert from Scout using the Webhook that we set up. The reason it does this is that it requires sample data from Scout in order to understand the format of the trigger, and what fields are available from the Scout. However, at this point there are not going to be any Alerts it can use because this Webhook has only just been set up. So here you have two options:

* Create a quick Alert in Scout to generate this sample data.
* Click *Skip This Step* and then *Continue Without Samples*.

We **strongly recommend** the first option, because later on when you are specifying the message that you are going to send to Slack, if you do not have sample data, you will not be able to use data that came from Scout. 



To create a quick Alert, open up Scout, go to *Alert > Alert Conditions* and create a simple condition that will alert, and choose the Slack Notification Group we set up earlier.



### Choose the Alert in Zapier

After the Alert has occurred in Scout, go back to Zapier and click the *Ok, I did this* button and it will connect with Scout and look for an Alert with this matching Webhook. Choose this as the sample you want to use and click *Continue*.



### Create a Slack Action

Next you need to add an Action step to the work-flow, this is the part were we integrate Slack. Click *Add a Step* on the left-hand side of the page.



Next click the *Action/Search* option, and you will be given the option to choose an app to connect.



Choose Slack, and then a new Action will be created on the left-hand side of the screen.



There are many different types of Slack Action that you can choose to perform, but let's choose *Send Channel Message*.



Next you can configure many aspects of the message that will be sent, such as which channel to send the message to and what particular data comes from the Scout Alert (shown in green). It is only possible to pull this data from Scout here if you created an Alert earlier like we advised.



Then you can send a test message to Slack to preview how it will look.



Then all that's left to do is to give your Zap a descriptive name and enable it.



Now everything is set up so that whenever an Alert occurs in Scout which is linked to this Notification Channel, you will see a message in Slack.


# Api

## Authorization

### Obtaining a token

1. Log into the Scout APM website
2. Go to your [organization's settings page](https://scoutapm.com/settings)
3. Enter a name (for your use), and obtain a token

### Sending Authorization

The key must be provided with every request, via one of several methods:

* An HTTP Header named `X-SCOUT-API`
* A URL query string argument named `key`*

*Note this isn't documented in OpenAPI spec below for simplicity, but is possible.

## OpenAPI Spec

{{<swagger>}}

## Time Steps
When using different durations, we will return different time steps. 

In the example above, when looking at a 1 week duration (`from=2021-03-20T22:00:00Z`, `to=2021-03-27T21:00:00Z`), we return data in an hourly timestep

Here's a list of our various durations and timesteps. Once a duration has exceeded a specific time duration, say 90 minutes, we will use the next largest available time duration (3 hours):

Time | Step | Example
--- | --- | ---
30 min | 1 minute | `from=2021-06-14T01:00:00Z&to=2021-06-14T01:30:00Z`
60 min | 1 minute | `from=2021-06-14T02:00:00Z&to=2021-06-14T03:00:00Z`
3 hrs | 2 minutes | `from=2021-06-14T03:00:00Z&to=2021-06-14T06:00:00Z`
6 hrs | 5 minutes | `from=2021-06-14T07:00:00Z&to=2021-06-14T13:00:00Z`
12 hrs | 5 minutes | `from=2021-06-14T14:00:00Z&to=2021-06-15T02:00:00Z`
1 day | 10 minutes | `from=2021-06-15T03:00:00Z&to=2021-06-16T03:00:00Z`
3 days | 30 minutes | `from=2021-06-16T04:00:00Z&to=2021-06-19T04:00:00Z`
7 days | 1 hour | `from=2021-06-19T05:00:00Z&to=2021-06-26T05:00:00Z`
14 days | 2 hours | `from=2021-06-26T06:00:00Z&to=2021-07-10T06:00:00Z`


# Celery

## Installation



## Installation

The latest `scout-apm` package supports Celery 3.1+.

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Configure Scout in your Celery application file:

```python
import scout_apm.celery
from scout_apm.api import Config
from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

# If you are using app.config_from_object() to point to your Django settings
# and have configured Scout there, configuring here is not necessary:
Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="Same as Web App Name",
    monitor=True,
)

# This attaches the instrumentation to your app and makes Scout work:
scout_apm.celery.install(app)
```

The `app` argument is optional and was added in version 2.12.0, but you should provide it for complete instrumentation.

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` instead of calling `Config.set`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.


# Compliance

## What Data is Collected by the Scout APM Agent?

When you install our APM agent into your application, we instrument your code in order to gather timing and other data. The data collected for all transactions includes:

  * Numeric metrics (timing, object allocations, memory)
  * Controller (in MVC terms) name and invoked controller function name
  * Background job name and invoked function name
  * SQL table and operation (e.g. Users#select)

In addition to collecting general data for every transaction, Scout uses an algorithm to pick out the most interesting transactions. These detailed transactions gather more information about the specifics of the transaction including:

  * URL path
  * URL parameters
  * SQL query strings (scrubbed and sanitized before being sent to Scout)
  * Outgoing HTTP request URLs (of instrumented HTTP libraries)
  * End user IP (the IP of a user making a request to your web server)
  * File name and line number of slow functions (used to display a backtrace)

Some of this information can be disabled for detailed transactions. Refer to the configuration section for your language at [https://scoutapm.com/docs](https://scoutapm.com/docs)

In Ruby, you can set `log_level = debug` to inspect the entire payload sent by our agent.

## HIPAA

Our agent can be installed safely in HIPAA compliant environments. To ensure user data is properly de-identified:

1. Disable sending HTTP query parameters if these contain sensitive data via the `uri_reporting` config option.
2. Do not add custom context (like reporting the current user in the session.)

Email [support@scoutapm.com](mailto:support@scoutapm.com) with any questions regarding the installation of Scout in HIPAA compliant environments.

## GDPR

While our monitoring agents are primarily metric-focused, they can be configured to send personal data if the customer wishes.

Under the GDPR, Scout is defined as a [Data Processor](https://gdpr-info.eu/art-28-gdpr/). If you'd like to view and sign our Data Processing Agreement, you can contact us at [support@scoutapm.com](mailto:support@scoutapm.com).

## PCI DSS

Scoutâs payment and card information is handled by Stripe, which has been audited by an independent PCI Qualified Security Assessor and is certified as a PCI Level 1 Service Provider, the most stringent level of certification available in the payments industry.

Scout does not typically receive credit card data, making it compliant with Payment Card Industry Data Security Standards (PCI DSS) in most situations.


# Configuration

## Configuration Options

The PHP agent can be configured via either environment variables or code.

### Environment Variables

You can also configure Scout APM via environment variables. To configure Scout via enviroment variables, uppercase the config key and prefix it with `SCOUT_`. For example, to set the `key` configuration via environment variables use: `export SCOUT_KEY=YOURKEY`

### Code based

Scout APM variables can also be set via code:

For Laravel, you can use a [skeleton configuration file](/docs/php/laravel#code-based-configuration)

For Symfony, you can [configure Scout in your config/packages/scoutapm.xml file](/docs/php/symfony)

## Common Configurations

SettingÂ Name | Description | Default | Required
--- | --- | --- | ---
key | The organization API key. | | Yes
name | Name of the application (ex: 'Photos App'). | | Yes
monitor | Whether monitoring data should be reported. | `false` | Yes
log_level | Override the SCOUT log level. Can only be used to quiet the agent, will not override the underlying logger's level | `"info"` | No

## Additional Configurations
SettingÂ Name | Description | Default |  Required
--- | --- | --- | ---
revision_sha | The Git SHA associated with this release. | [See docs](/docs/php/features/#deploy-tracking) | No
uri_reporting | Whether to include, exclude, or partially include parameters the reported URI. [See below for more info](#uri-reporting) | `path` | No
uri_filtered_params | A string containing a JSON array of filtered_params when `uri_reporting` is set to `filtered_params`. See below for more info | [See default values below](#uri-filtered-parameters) | No
scm_subdirectory | The relative path from the base of your Git repo to the directory which contains your application code. | | No
ignore | A string containing a JSON array of endpoints that Scout should ignore. | `[]` | No
ignore_jobs | A string containing a JSON array of jobs (e.g. Artisan commands, or Queue Jobs) that Scout should ignore. | `["horizon"]` | No
disabled_instruments | A string containing a JSON array of instruments that Scout should not install. | `[]` | No
hostname | The hostname the metrics should be aggregrated under. | `hostname` | No
log_payload_content | Will log the payload that gets sent to the core agent. Useful for [troubleshooting](/docs/php/troubleshooting) | | No
errors_ignored_exceptions | Excludes certain exceptions from being reported | `[]` | No
errors_filtered_params | Filtered parameters in exceptions | `[password, s3-key, scout_key]` | No

## Core Agent Configurations
SettingÂ Name | Description | Default |  Required
--- | --- | --- | ---
core_agent_dir | Path to create the directory which will store the [Core Agent](/docs/core-agent). | `/tmp/scout_apm_core` | No
core_agent_download | Whether to download the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_launch | Whether to start the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_permissions | The permission bits to set when creating the directory of the [Core Agent](/docs/core-agent). | `700` | No
core_agent_full_name | The release/url we look for when downloading the core-agent. | Auto-detected | No
core_agent_triple | If you are running a MUSL based Linux (such as ArchLinux), you may need to explicitly specify the platform triple. E.g. `x86_64-unknown-linux-musl` | Auto detected | No
core_agent_log_level | The log level of the core agent process. This should be one of: `"trace"`, `"debug"`, `"info"`, `"warn"`, `"error"`. This does not affect the log level of the PHP library. To change that, directly configure `logging` as per [the documentation](/docs/php/logging). | `"info"` | No
core_agent_log_file | The log file for the [Core Agent](/docs/core-agent) to write its logs to. If not set, it won't be written. This does not affect the logging configuration of the Php library. To change that, directly configure the php `logging` module as per [the below documentation](/docs/php/logging) | `"info"` | No
core_agent_config_file  | Point to a configuration file for the [Core Agent](/docs/core-agent). This may be useful for debugging your setup with files provided by Scout APM staff. | | No
core_agent_triple  | If you are running a MUSL based Linux (such as ArchLinux), you may need to explicitly specify the platform triple. E.g. `x86_64-unknown-linux-musl` | Auto detected | No
core_agent_socket_path  | The path to the socket to connect to the [Core Agent](/docs/core-agent), passed to it when launching. This may be either a TCP address, in the format <code>tcp://&lt;address&gt;:&lt;port&gt;</code>, or an absolute path to create as a Unix socket. The deafult is to use TCP. Prior to version 5.0.0, this defaulted to using a Unix socket in the same directoy as the core agent | `tcp://127.0.0.1:6590`| No

## Environments

It typically makes sense to treat each environment (production, staging, etc) as a separate application within Scout and ignore the development and test environments. Configure a unique app name for each environment as Scout aggregates data by the app name.

Ex:
```bash
export SCOUT_KEY=YOURKEY
export SCOUT_NAME=YOURAPPNAME (Production)
```

## URI Reporting

Whether to include, exclude, or partially include parameters when reporting the URI. Possible values include, `full_path` (all parameters reported), `filtered_params` (see `uri_filtered_params` or below for more info), or `path` (remove all parameters). In 6.4+ the default is `path`, in 6.3 and lower the default is `full_path`

### URI Filtered Parameters

By default, the value of `uri_filtered_params` is `['access', 'access_token', 'api_key' 'apikey', 'auth', 'auth_token', 'card', 'certificate', 'credentials', 'crypt', 'key', 'mysql_pwd', 'otp', 'passwd', 'password', 'private', 'protected', 'salt', 'secret', 'ssn', 'stripetoken', 'token']`

When `uri_filtered_params` is set, we **do not merge** the default list and the new. To add or remove parameters from this filtering list, we suggest copying the above default list and making changes to it accordingly.

See the PHP agent's repo for more info:

https://github.com/scoutapp/scout-apm-php/blob/master/src/Config/Source/DefaultSource.php


# Configuration

## Configuration Options

The Node agent can be configured via two methods:

1. Code Based
2. Environment Variables

### Code Based
Scout can be configured in the Scout.install function via passing in an object/dictionary with the  configuration values:
```javascript
await scout.install({
    allowShutdown: true, // allow shutting down spawned scout-agent processes from this program
    monitor: true, // enable monitoring
    name: "",
    key: "",
  });
```

### Environment Variables
You can also configure Scout APM via environment variables. To configure Scout via enviroment variables, uppercase the config key and prefix it with `SCOUT_`. For example, to set the `key` configuration via environment variables use: `export SCOUT_KEY=YOURKEY`

## Common Configurations
SettingÂ Name | Description | Default | Required
--- | --- | --- | --- 
key | The organization API key. | | Yes
name | Name of the application (ex: 'Photos App'). | | Yes
monitor | Whether monitoring data should be reported. | `false` | Yes
log_level | Override the SCOUT log level. Can only be used to quiet the agent, will not override the underlying logger's level | `'info'` | No

## Additional Configurations
SettingÂ Name | Description | Default |  Required
--- | --- | --- | ---
revision_sha | The Git SHA associated with this release. | [See docs](/docs/node/configuration/#deploy-tracking) | No
scm_subdirectory | The relative path from the base of your Git repo to the directory which contains your application code. | | No
ignore | A string containing a JSON array of endpoints that Scout should ignore. | `[]` | No
disabled_instruments | A string containing a JSON array of instruments that Scout should not install. | `[]` | No
hostname | The hostname the metrics should be aggregrated under. | `hostname` | No

## Core Agent Configurations
SettingÂ Name | Description | Default |  Required
--- | --- | --- | ---
core_agent_dir | Path to create the directory which will store the [Core Agent](/docs/core-agent). | `/tmp/scout_apm_core` | No
core_agent_download | Whether to download the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_launch | Whether to start the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_permissions | The permission bits to set when creating the directory of the [Core Agent](/docs/core-agent). | `700` | No
core_agent_full_name | The release/url we look for when downloading the core-agent. | Auto-detected | No
core_agent_triple | If you are running a MUSL based Linux (such as ArchLinux), you may need to explicitly specify the platform triple. E.g. `x86_64-unknown-linux-musl` | Auto detected | No
core_agent_log_level | The log level of the core agent process. This should be one of: `"trace"`, `"debug"`, `"info"`, `"warn"`, `"error"`. This does not affect the log level of the NodeJS library. To change that, directly configure `logging` as per [the documentation](/docs/node/logging). | `"info"` | No
core_agent_log_file | The log file for the core agent process | `"/path/to/your/log/file"` | No

## Environments

It typically makes sense to treat each environment (production, staging, etc) as a separate application within Scout and ignore the development and test environments. 

Configure a unique app name for each environment as Scout aggregates data by the app name. For example, `app-staging` might be used to represent a Staging environment where as `app-production` would represent a Production environment.


# Configuration

## Configuration Options

The Ruby agent can be configured via the `config/scout_apm.yml` Yaml file and/or environment variables. A config file with your organization key is available for download as part of the install instructions.

Heroku users should use environment variables instead of the scout_apm.yml.

### ERB evaluation

ERB is evaluated when loading the config file. For example, you can set the app name based on the hostname:

```yaml
common: &defaults
  name: <%= "ProjectPlanner.io (#{Rails.env})" %>
```

### Environment Variables

You can also configure Scout APM via environment variables. Environment variables override settings provided in `scout_apm.yml`. To configure Scout via enviroment variables, uppercase the config key and prefix it with `SCOUT_`. For example, to set the `key` via environment variables: `export SCOUT_KEY=YOURKEY`

## Common Configurations

The following configuration settings are available:

SettingÂ Name | Description | Default | Required
--- | --- | --- | ---
name | Name of the application (ex: 'Photos App'). | `Rails.application.class.to_s. sub(/::Application$/, '')` | Yes
key | The organization API key. | | Yes
monitor | Whether monitoring should be enabled. | `false` | Yes
auto_instruments | Instrument custom code with [Auto Instruments](/docs/ruby/features#auto-instruments). | `false` | No
errors_enabled | True or false. If true, monitor errors and send them to Scout. | `false` | Yes
log_level | The logging level of the agent. | `INFO` | No

## Additional Configurations

SettingÂ Name | Description | Default | Required
--- | --- | --- | ---
job_params_capture | When true, automatically collect job arguments as context with Sidekiq. | `false` | No
job_filtered_params | A list of params to filter. Automatically includes Rail's `filter_parameters`. | `[]` | No
detailed_middleware | When true, the time spent in each middleware is visible in transaction traces vs. an aggregrate across all middlewares. This adds additional overhead and is disabled by default as middleware is an uncommon bottleneck. | `false` | No
hostname | Allows renaming of the node/host name | `Socket.gethostname` | No
revision_sha | The Git SHA that corresponds to the version of the app being deployed. | [See docs](/docs/ruby/features/#deploy-tracking) | No
scm_subdirectory | The relative path from the base of your Git repo to the directory which contains your application code. | | No
sample_rate | Gobal sample rate for your application. Rate should be 0.0 - 1.0 serving as a decimal rate of requests to capture (ex: `0.80` to capture 80% of requests). Prior to `v6.0.0`, integer sampling was allowed with the lowest rate as 1%. | `1.0` | No
endpoint_sample_rate | Sample rate for all endpoints. `sample_endpoints` will override this rate for matching endpoints. Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `1.0` | No
job_sample_rate | Sample rate for all jobs. `sample_jobs` will override this rate for matching jobs. Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `1.0` | No
ignore_endpoints | An Array of web endpoints that Scout should not instrument. Routes that match the prefixed path (ex: `['/health', '/status']`) will be ignored by the agent. Replaces old `ignore` configuration. | `[]` | No
ignore_jobs | An Array of job names that Scout should not instrument. Jobs with exact name match will be ignored by the agent. | `[]` | No
sample_endpoints | An Array of web endpoints that Scout should sample at the provided rate (ex: `['/busy_endpoint:50']`). Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `[]` | No
sample_jobs | An Array of job names that Scout should sample at the provided rate (ex: `['MyJob:70']`). Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `[]` | No
max_traces | The
enable_background_jobs | Indicates if background jobs should be monitored. |  `true` |  No
collect_remote_ip | Automatically capture end user IP addresses as part of each trace's context. | `true` | No
record_queue_time | Automatically capture request queue time when a [queuing request header](/docs/features#setup) is found. | `true` | No
auto_instruments_ignore | Excludes the listed files names from being auto instrumented. Ex: `['application_controller']`. |  `[]` | No
errors_ignored_exceptions | Excludes certain exceptions from being reported | `[ActiveRecord::RecordNotFound, ActionController::RoutingError]` | No
errors_filtered_params | Filtered parameters in exceptions | `[password, s3-key]` | No
log_file_path | The path to the `scout_apm.log` log file directory. Use `stdout` to log to STDOUT. | `Environment#root+log/`Â or `STDOUT` if running on Heroku. | No
proxy | Specify the proxy URL (ex: `https://proxy`) if a proxy is required. |  | No
host | The protocol + domain where the agent should report. | `https://scoutapm.com` | No
uri_reporting | By default Scout reports the URL and filtered query parameters with transaction traces. Sensitive parameters in the URL will be redacted. To exclude query params entirely, use `path`. | `filtered_params` | No
disabled_instruments | An Array of instruments that Scout should not install. Each Array element should should be a string-ified, case-sensitive class name (ex: `['Elasticsearch','HttpClient']`). The default installed instruments can be viewed in the [agent source](https://github.com/scoutapp/scout_apm_ruby/tree/master/lib/scout_apm/instruments). | `[]` | No
timeline_traces | Send traces in both the summary and [timeline](/docs/features#timeline-view) formats. | `true` | No
use_prepend | Where supported, use `Method#prepend` for instrumentation. | `false` | No
alias_method_instruments | If `use_prepend` is set to `true`, specify which particular instruments should still use the `alias_method` approach. Each Array element should should be a string-ified, case-sensitive class name (ex: `['Elasticsearch','HttpClient']`). The default installed instruments can be viewed in the [agent source](https://github.com/scoutapp/scout_apm_ruby/tree/master/lib/scout_apm/instruments). | `[]` | No
prepend_instruments | If `use_prepend` is set to `false`, specify which particular instruments should use the `prepend` approach. Each Array element should should be a string-ified, case-sensitive class name (ex: `['Elasticsearch','HttpClient']`). The default installed instruments can be viewed in the [agent source](https://github.com/scoutapp/scout_apm_ruby/tree/master/lib/scout_apm/instruments). | `[]` | No
backtrace_additional_directories | An Array of additional directory names to include in backtrace parsing. By default, the agent only captures backtrace frames from files under `lib/`, `app/`, and `config/`. Configured directories are matched by prefix against paths relative to your app root (ex: configuring `'engines'` matches any path starting with `engines/`). Useful for Rails engines, components, or other non-standard directory structures (ex: `['engines', 'components']`). | `[]` | No

## Environments

It typically makes sense to treat each environment (production, staging, etc) as a separate application within Scout and ignore the development and test environments. Configure a unique app name for each environment as Scout aggregates data by the app name.

Ex:
```bash
export SCOUT_KEY=YOURKEY
export SCOUT_NAME=YOURAPPNAME (Production)
```

## Library Instrumentation Method

For many of our instruments, the Scout Ruby agent has historically used `Module#alias_method` to monkeypatch specific library methods to gather telemetry. The more modern approach is to use `Module#prepend`, which many other gems now use as default. In certain cases, if a gem that uses `Module#prepend` and another gem that uses `Module#alias_method` have applied their instrumentation to the same library, an infinite loop can occur resulting in a `StackLevelTooDeep` exception.

Moving from `alias_method` to `prepend` has caused major headaches for nearly all gems which made the switch, despite making the change in a major version semantic version bump. In order to allow a less disruptive upgrade path, Scout will continue to use `alias_method` as the default, but with available configuration option to move either all instrumentation to `prepend`, or selectively move instrumentation to `prepend`.

**With Scout APM Version 5.3.0 and above**, use the following configuration options to control the instrumentation method:

  * `use_prepend` - default: `false`. If set to `true`, all instrumentation which supports the `Module#prepend` method will use that.

  * `alias_method_instruments` - default: `[]`. If `use_prepend` is set to `true`, you can still specify which particular instruments should use the `alias_method` approach with this configuration option.

  * `prepend_instruments` - default: `[]`. If `use_prepend` is `false`, you can still specify which particular instruments should use the `prepend` approach with this configuration option.

The Scout instrumentation for the following libraries support `Module#prepend` in addition to `Module#alias_method` in `scout_apm >= 5.3.0` :

  * ElasticSearch
  * HTTP
  * HTTPClient
  * Memcached
  * MongoDB (Moped)
  * Net::HTTP
  * Redis


# Configuration

## Configuration Options

### Code based

The Elixir agent can be configured via the `config/scout_apm.exs` file. A config file with your organization key is available for download as part of the install instructions. 
A application name and key is required: 

```elixir
config :scout_apm, 
name: "Your App", # The app name that will appear within the Scout UI 
key: "YOUR SCOUT KEY" 
``` 


### Environment Variables

Alternately, you can also use environment variables of your choosing by formatting your configuration as a tuple with :system as the first value and the environment variable expected as the second. To configure Scout via enviroment variables, uppercase the config key and prefix it with `SCOUT_`. For example, to set the `key` configuration via environment variables use: `export SCOUT_KEY=YOURKEY`

```elixir
config :scout_apm, 
name: { :system, "SCOUT_NAME" }, 
key: { :system, "SCOUT_KEY" } 
``` 

## Common Configurations
SettingÂ Name | Description | Default | Required
--- | --- | --- | ---
key | The organization API key. | | Yes
name | Name of the application (ex: 'Photos App'). | | Yes
monitor | Whether monitoring data should be reported. | `true` | Yes
log_level | The logging level of the agent. Possible values: `:debug`, `:info`, `:warn`, and `:error`. | `:info` | No

## Additional Configurations
SettingÂ Name | Description | Default | Required
--- | --- | --- | ---
host | The protocol + domain where the agent should report. | `https://checkin.scoutapm.com` | No
revision_sha | The Git SHA associated with this release. | [See docs](/docs/elixir/features#deploy-tracking) | No
ignore | An array of URL prefixes to ignore in the Scout Plug instrumentation. Routes that match the prefixed path (ex: `['/health', '/status']`) will be ignored by the agent. | `[]` | No
hostname | The host registered with the [Core Agent.](/docs/core-agent) | | No

## Error Monitoring Configurations

These settings control Scout's [error monitoring](/docs/features/error-monitoring) feature. Error monitoring is enabled by default and automatically captures unhandled exceptions in Phoenix controllers.

Setting Name | Description | Default | Required
--- | --- | --- | ---
errors_enabled | Enable or disable error capture. | `true` | No
errors_host | The endpoint where errors are reported. | `https://errors.scoutapm.com` | No
errors_batch_size | Number of errors sent per batch. | `5` | No
errors_max_queue_size | Maximum number of errors queued before dropping. | `500` | No
errors_flush_interval_ms | How often (in milliseconds) the error queue is flushed. | `1000` | No
errors_ignored_exceptions | A list of exception modules to ignore (e.g., `[Phoenix.Router.NoRouteError]`). | `[]` | No
errors_filter_parameters | A list of parameter keys to redact from error reports (e.g., `["password", "credit_card"]`). | `[]` | No

## Log Management Configurations

These settings control Scout's [log management](/docs/features/log-management) feature. Log management must be explicitly enabled and requires an ingest key.

Setting Name | Description | Default | Required
--- | --- | --- | ---
logs_enabled | Enable or disable log forwarding to Scout. | `false` | No
logs_endpoint | The OTLP endpoint where logs are sent. | `https://otlp.scoutotel.com:4318` | No
logs_ingest_key | The ingest API key for log forwarding. Available in the Logs page of your Scout app. Falls back to the main `key` if not set. | `nil` | Yes (if logs enabled)
logs_batch_size | Number of log records sent per batch. | `100` | No
logs_max_queue_size | Maximum number of log records queued before dropping. | `5000` | No
logs_flush_interval_ms | How often (in milliseconds) the log queue is flushed. | `5000` | No
logs_level | The minimum log level to forward. Possible values: `:debug`, `:info`, `:warning`, `:error`. | `:info` | No
logs_filter_modules | A list of logger module names to exclude from forwarding. | `[]` | No

## Core Agent Configurations
SettingÂ Name | Description | Default |  Required
--- | --- | --- | ---
core_agent_dir | Path to create the directory which will store the [Core Agent](/docs/core-agent). | `/tmp/scout_apm_core` | No
core_agent_download | Whether to download the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_launch | Whether to start the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_permissions | The permission bits to set when creating the directory of the [Core Agent](/docs/core-agent). | `700` | No
core_agent_full_name | The release/url we look for when downloading the core-agent. | Auto-detected | No
core_agent_triple | If you are running a MUSL based Linux (such as ArchLinux), you may need to explicitly specify the platform triple. E.g. `x86_64-unknown-linux-musl` | Auto detected | No
core_agent_log_level | The log level of the core agent process. This should be one of: `"trace"`, `"debug"`, `"info"`, `"warn"`, `"error"`. This does not affect the log level of the NodeJS library. To change that, directly configure `logging` as per [the documentation](/docs/node/logging). | `"info"` | No
core_agent_log_file | The log file for the core agent process | `"/path/to/your/log/file"` | No


## Environments

It typically makes sense to treat each environment (production, staging, etc) as a separate application within Scout. To do so, configure a unique app name for each environment. Scout aggregates data by the app name.

An example:

```elixir
# config/staging.exs

config :scout_apm,
  name: "YOUR APP - Staging"
```


## Instrumenting Common Libraries

We've collected best practices for instrumenting common transactions and timing functions below. If you have a suggestion, [please share it](mailto:support@scoutapm.com). See our [custom instrumentation quickstart](/docs/elixir/features/#custom-instrumentation) for more details on adding instrumentation.

* Transactions
  * [Phoenix Channels](#phoenix-channels)
  * [Plug Chunked Response](#plug-chunked-response-http-streaming)
  * [GenServer calls](#genserver-calls)
  * [Task.start](#taskstart)
  * [Task.Supervisor.start_child](#tasksupervisorstart_child)
  * [Exq](#exq)
  * [Absinthe (GraphQL)](#absinthe)
* Timing
  * [HTTPoison](#httpoison)
  * [MongoDB Ecto](#mongodb-ecto)

### Phoenix Channels


#### Web or background transactions?

* __web__: For channel-related functions that impact the user-facing experience. Time spent in these transactions will appear on your app overboard dashboard and appear in the "Web" area of the UI.
* __background__: For functions that don't have an impact on the user-facing experience (example: click-tracking). These will be available in the "Background Jobs" area of the UI.

#### Naming channel transactions

Provide an identifiable name based on the message the `handle_out/` or `handle_in/` function receives.

An example:

```elixir
defmodule FirestormWeb.Web.PostsChannel do
  use FirestormWeb.Web, :channel
  import ScoutApm.Tracing

  # Will appear under "Web" in the UI, named "PostsChannel.update"
  @transaction_opts [type: "web", name: "PostsChannel.update"]
  deftransaction handle_out("update", msg, socket) do
    push socket, "update", FetchView.render("index.json", msg)
  end
end
```

### Plug Chunked Response (HTTP Streaming)

In a Plug application, a chunked response needs to be instrumented directly, rather than relying on
the default Scout instrumentation Plug. The key part is to `start_layer` beforehand, and then call
`before_send` after the chunked response is complete.

```elixir
def chunked(conn, _params) do
  # The "Controller" argument is required, and should not be changed. The second argument is the
  # name this endpoint will appear as in the Scout UI. The `action_name` function determines this
  # automatically.
  ScoutApm.TrackedRequest.start_layer("Controller", ScoutApm.Plugs.ControllerTimer.action_name(conn))

  conn =
    conn
    |> put_resp_content_type("text/plain")
    |> send_chunked(200)

  {:ok, conn} =
    Repo.transaction(fn ->
      Example.build_chunked_query(...)
      |> Enum.reduce_while(conn, fn data, conn ->
        case chunk(conn, data) do
          {:ok, conn} ->
            {:cont, conn}

          {:error, :closed} ->
            {:halt, conn}
        end
      end)
    end)

  ScoutApm.Plugs.ControllerTimer.before_send(conn)

  conn
end
```

Then have the default instrumentation ignore the endpoint's URL prefix (since it is manually instrumented now).
See the [ignore configuration](/docs/elixir/features/#ignore-transactions) for more details.

```elixir
config :scout_apm,
  name: "My Scout App Name",
  key: "My Scout Key",
  ignore: ["/chunked"]
```


### GenServer calls

It's common to use `GenServer` to handle background work outside the web request flow. Suggestions:

* Treat these as `background` transactions
* Provide a `name` based on the message each `handle_call/3` function handles.
* Use `deftransaction` to define the method
* Add a `@transaction_opts` module attribute to override the name and type (`background`)

An example:

```elixir
defmodule Flight.Checker do
  use GenServer
  import ScoutApm.Tracing

  # Will appear under "Background Jobs" in the UI, named "Flight.handle_check".
  @transaction_opts [type: "background", name: "check"]
  deftransaction handle_call({:check, flight}, _from, state) do
    # Do work...
  end
end
```

### Task.start

These execute asynchronously, so treat as a `background` transaction.

```elixir
Task.start(fn ->
  # Will appear under "Background Jobs" in the UI, named "Crawler.crawl".
  ScoutApm.Tracing.transaction(:background,"Crawler.crawl") do
    Crawler.crawl(url)
  end
end)
```

### Task.Supervisor.start_child

Like `Task.start`, these execute asynchronously, so treat as a `background` transaction.

```elixir
Task.Supervisor.start_child(YourApp.TaskSupervisor, fn ->
  # Will appear under "Background Jobs" in the UI, named "Crawler.crawl".
  ScoutApm.Tracing.transaction(:background,"Crawler.crawl") do
    Crawler.crawl(url)
  end
end)
```

### Exq

To instrument [Exq](https://github.com/akira/exq) background jobs, `import ScoutApm.Tracing`, use `deftransaction` to define the function, and add a `@transaction_opts` module attribute to optionally override the name and type:

```elixir
defmodule MyWorker do
  import ScoutApm.Tracing

  # Will appear under "Background Jobs" in the UI, named "MyWorker.perform".
  @transaction_opts [type: "background"]
  deftransaction perform(arg1, arg2) do
    # do work
  end
end
```

### Absinthe

Requests to the Absinthe plug can be grouped by the GraphQL `operationName` under the "Web" UI by adding [this plug](https://gist.github.com/itsderek23/d9435b21c9a44cd9629e93c4e8c2750e) to your pipeline.  

### HTTPoison

Download this [Demo.HTTPClient module](https://gist.github.com/itsderek23/048eaf813af4a1a31a219d75221eb7b7 (you can rename to something more fitting) into your app's `/lib` folder, then `alias Demo.HTTPClient` when calling `HTTPoison` functions:

```elixir
defmodule Demo.Web.PageController do
  use Demo.Web, :controller
  # Will route function calls to `HTTPoision` through `Demo.HTTPClient`, which times the execution of the HTTP call.
  alias Demo.HTTPClient

  def index(conn, _params) do
    # "HTTP" will appear on timeseries charts. "HTTP/get" and the url "https://cnn.com" will appear in traces.
    case HTTPClient.get("https://cnn.com") do
      {:ok, %HTTPoison.Response{} = response} ->
        # do something with response
        render(conn, "index.html")
      {:error, %HTTPoison.Error{} = error} ->
        # do something with error
        render(conn, "error.html")
    end
    HTTPClient.post("https://cnn.com", "")
    HTTPClient.get!("http://localhost:4567")
    render(conn, "index.html")
  end
end
```

### MongoDB Ecto

Download [this example MongoDB Repo module](https://gist.github.com/itsderek23/051327a152bc4d95451fd76808b8e83f) to use inplace of your existing MongoDB Repo module.


# Configuration

## Configuration Options

The Python agent can be configured via three methods:

1. Scout Config
2. Framework dependent variables
3. Environment Variables

### Scout Config
```python
from scout_apm.api import Config

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)
```
### Framework Dependent
Certain frameworks have other ways that Scout variables can be configured, such as in settings.py for Django and app.config for Flask.
See framework pages for more details.


### Environment Variables

You can also configure Scout APM via environment variables. To configure Scout via environment variables, uppercase the config key and prefix it with `SCOUT_`. For example, to set the `key` configuration via environment variables use: `export SCOUT_KEY=YOURKEY`


## Common Configurations

SettingÂ Name | Description | Default | Required
 ---- | ---- | ----- | -----
key | The organization API key. | | Yes
name  | Name of the application (ex: 'Photos App'). | | Yes
monitor  | Whether monitoring data should be reported. | `False` | Yes
revision_sha  | The Git SHA associated with this release. Used with Deploy Tracking. | [See docs](/docs/python/features#deploy-tracking) | No
errors_enabled | True or False. If true, monitor errors and send them to Scout. | `False` | Yes

## Additional Configurations
SettingÂ Name | Description | Default | Required
--- | --- | -- | ---
collect_remote_ip  | Automatically capture end user IP addresses as part of each trace's context. | `True` | No
disabled_instruments | An list of instruments that Scout should not install. If specified as an environment variable, it should be a comma-separated list. The default installed instruments can be viewed in the [agent source](https://github.com/scoutapp/scout_apm_python/tree/master/src/scout_apm/instruments). | `[]` | No
errors_ignored_exceptions | Excludes certain exceptions from being reported. | `()` | No
hostname  | The hostname the metrics should be aggregated under. | `hostname` | No
log_payload_content  | Logs the payload of the messages being sent to the core-agent and error service. This should only be enabled for debugging. | `False` | No
sample_rate | Gobal sample rate for your application. Rate should be 0.0-1.0 serving as a percentage of requests to capture (ex: `0.8` to capture 80% of requests). | `1.0` | No
endpoint_sample_rate | Sample rate for all endpoints. Overriden by individual endpoint sampling. Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `1.0` | No
job_sample_rate | Sample rate for all jobs. Overriden by individual job sampling. Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `1.0` | No
ignore_endpoints | An Array of web endpoints that Scout should not instrument. Routes that match the prefixed path (ex: `['/health', '/status']`) will be ignored by the agent. Replaces old `ignore` configuration. | `[]` | No
ignore_jobs | An Array of job names that Scout should not instrument. Jobs with exact name match will be ignored by the agent. | `[]` | No
sample_endpoints | An Array of web endpoints that Scout should sample at the provided rate (ex: `['/busy_endpoint:0.5']`). Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `[]` | No
sample_jobs | An Array of job names that Scout should sample at the provided rate (ex: `['MyJob:0.7']`). Rate should be 0.0-1.0 serving as a percentage of requests to capture. | `[]` | No
log_content_payload  | Logs the payload of the messages being sent to the core-agent and error service. This should only be enabled for debugging. | `False` | No
scm_subdirectory  | The relative path from the base of your Git repo to the directory which contains your application code. | | No
showdown_timeout_seconds  |  Maximum amount of time, in seconds, to spend at flushing outstanding events to the core agent at shutdown. Set to 0 to disable. | 2.0 |  No
uri_reporting  | By default Scout reports the URL and filtered query parameters with transaction traces and error reports. Sensitive parameters in the URL will be redacted. To exclude query params entirely, use `path`. | `filtered_params` | No


## Core Agent Configurations
There are also some configuration options that affect how the core agent process is run. Typically you don't need to change these:

SettingÂ Name | Description | Default | Required
--- | ---- | --- | ---
core_agent_dir  | Path to create the directory which will store the [Core Agent](/docs/core-agent). | `/tmp/scout_apm_core` | No
core_agent_download  | Whether to download the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_full_name | The release/url we look for when downloading the core-agent. | Auto-detected | No
core_agent_launch  | Whether to start the [Core Agent](/docs/core-agent) automatically, if needed. | `True` | No
core_agent_log_file  | The log file for the [Core Agent](/docs/core-agent) to write its logs to. If not set, it won't be written. This does not affect the logging configuration of the Python library. To change that, directly configure the python `logging` module as per [the below documentation](/docs/python/logging). Prior to version 2.13.0, this was called **log_file**. That name now works as an alias, and takes precedence to allow old configuration to continue to work. | | No
core_agent_log_level  | The log level of the [Core Agent](/docs/core-agent). This should be one of: `"trace"`, `"debug"`, `"info"`, `"warn"`, `"error"`. This does not affect the log level of the Python library. To change that, directly configure the python `logging` module as per [the below documentation](/docs/python/logging). Prior to version 2.6.0, this was called **log_level**. That name now works as an alias, and takes precedence to allow old configuration to continue to work. | `"info"` | No
core_agent_permissions  | The permission bits to set when creating the directory of the [Core Agent](/docs/core-agent). | `700` | No
core_agent_config_file  | Point to a configuration file for the [Core Agent](/docs/core-agent). This may be useful for debugging your setup with files provided by Scout APM staff. |  Prior to version 2.13.0, this was called **config_file**. That name now works as an alias, and takes precedence to allow old configuration to continue to work. | No
core_agent_triple  | If you are running a MUSL based Linux (such as ArchLinux), you may need to explicitly specify the platform triple. E.g. `x86_64-unknown-linux-musl` | Auto detected | No
core_agent_socket_path  | The path to the socket to connect to the [Core Agent](/docs/core-agent), passed to it when launching. This may be either a TCP address, in the format <code>tcp://&lt;address&gt;:&lt;port&gt;</code>, or an absolute path to create as a Unix socket. The deafult is to use TCP. Prior to version 2.16.0, this defaulted to using a Unix socket in the same directoy as the core agent. Prior to version 2.13.0, this was called **socket_path**. That name now works as an alias, and takes precedence to allow old configuration to continue to work. | `tcp://127.0.0.1:6590` | No

## Environments

It typically makes sense to treat each environment (production, staging, etc) as a separate application within Scout and ignore the development and test environments. Configure a unique app name for each environment as Scout aggregates data by the app name.

Ex:
```bash
export SCOUT_KEY=YOURKEY
export SCOUT_NAME=YOURAPPNAME (Production)
```


# Core-agent

Some of the languages instrumented by Scout depend on a standalone binary for collecting and reporting data. We call this binary the Core Agent. If the Core Agent is required for your language, the Scout agent library for that language will handle downloading, configuring, and launching the Core Agent automatically. However, you may manually manage the Core Agent through configuration options.

## Running Manually

### With Docker
Simply run the following:

**1.**

```bash
docker pull scoutapp/scoutapm
```

**2.**

```bash
docker run -p 6590:6590 --name scoutapm scoutapp/scoutapm
```

### Without Docker

**1.** Create a directory which your app has permissions to read, write and execute into (for our example we will use: /tmp but can be placed elsewhere) and change to the created directory

```bash
cd /tmp
mkdir scout_apm_core && cd "$_"
```
**2.** Download and test the core agent:

**2.1**
Download the core agent tarball
```bash
curl https://s3-us-west-1.amazonaws.com/scout-public-downloads/apm_core_agent/release/scout_apm_core-latest-x86_64-unknown-linux-musl.tgz --output core-agent-download.tgz
```

**2.2** 
Unzip the core-agent
```bash
tar -xvzf core-agent-download.tgz
```

**2.3** 
Test that core agent is executable
```bash
./core-agent
```

If everything has run successfully, you should see something similar to the following output:



**3.** Start the core agent:

```bash
./core-agent start --daemonize true --tcp 127.0.0.1:6590
```

**Note:** this will not persist past a reboot. We suggest adding the core agent to upstart, systemd, or any other processes manager you may be using.

For additional startup flags, check the in-executable help with `./core-agent start --help`

*For agents that use a core-agent version less than 1.3.0, remove the --tcp flag.*

**4.** Check to see that core agent socket is running:

```bash
./core-agent probe
```

### Configuring the language agent

You will need to configure the language agent to look in the correct location for the self hosted core-agent. Otherwise, the language agent will launch another core-agent and use this one instead.

If you are using one of the supported languages (PHP, Python, Elixir, and Node.js) with a core-agent version 1.3.0+ (released 2020/09/04) which uses a TCP socket, you will need to set the following configurations:

*   `SCOUT_CORE_AGENT_SOCKET_PATH=tcp://127.0.0.1:6590`
*   `SCOUT_CORE_AGENT_DOWNLOAD=false`
*   `SCOUT_CORE_AGENT_LAUNCH=false`

__Note:__ You can also have the core-agent as a service on a separate host:

*   `SCOUT_CORE_AGENT_SOCKET_PATH=tcp://123.456.78.90:6590`

If you are using one of the supported languages with a core-agent version less than 1.3.0, you will have to set the following configuration variables to point to the correct UNIX domain socket path (as well as disabling the agent from re-downloading and launching the core agent again):

*   `SCOUT_CORE_AGENT_SOCKET_PATH=/tmp/scout_apm_core/scout-agent.sock`
*   `SCOUT_CORE_AGENT_DOWNLOAD=false`
*   `SCOUT_CORE_AGENT_LAUNCH=false`

To check which version of the core-agent you're using, check with the #changelog for your language's agent.

While core-agent version's 1.3.0+ default to using TCP sockets, it's possible to still use UNIX domain sockets by setting the `SCOUT_CORE_AGENT_SOCKET_PATH` to the value seen above: `SCOUT_CORE_AGENT_SOCKET_PATH=/tmp/scout_apm_core/scout-agent.sock`. However, UNIX domain sockets adhere to permissions of the directory they are in. See the below section for potential issues.
### Downloading the core agent to another directory 

For core-agent versions lower than 1.3.0, by default, the core agent will be downloaded into the /tmp directory. 

However due to /tmp being as mounted as not executable, or SELinux configuration, or your umask permissions, you may not be able to execute the core-agent in that directory. To change the directory that Scout downloads to, use the configuration `SCOUT_CORE_AGENT_DIR`. 

Your app must have read, write, and execute permissions for this directory. Read your language's agent configuration reference for more detail.

### Checking if the core agent is executable 

In some cases (for core-agent versions lower than 1.3.0), the core agent won't be able to execute. You may be presented with an error message that looks similar to: 
`[Scout] Failed to launch core agent - exception core-agent exited with non-zero status. Output: sh: 1: /tmp/scout_apm_core/scout_apm_core-v1.2.9-x86_64-unknown-linux-musl/core-agent: Permission denied` 

Try following [Downloading the core agent to another directory](#downloading-the-core-agent-to-another-directory) above to see if you are able to execute the core agent in another directory to determine if there is a permissions issue with the default location. If you continue having issues, please reach out to us at [support@scoutapm.com](mailto:support@scoutapm.com). ## Available platforms and architectures Builds of the Core Agent are available for these platforms and architectures: 
* Linux i686 (glibc) 
* Linux x86-64 (glibc) 
* Linux i686 (musl) 
* Linux x86-64 (musl) 
* OSX/Darwin x86-64 

## Other languages

The Core Agent API is in our tech preview program.

Want to add tracing but Scout doesn't support your app's language? You can instrument just about anything (assuming you can communicate via a Unix Domain Socket) with Scout's [Core Agent API](https://github.com/scoutapp/core-agent-api). For information, view the [Core Agent API on GitHub](https://github.com/scoutapp/core-agent-api).

## Pinning The Core Agent

By default, all of our agents pin to the latest core-agent version that was available when the change was released (at this time the latest agents are pinned to 1.5.0). In order to update to the latest core-agent, you will need to update your agent as well.

### Self Hosting

You can download the core-agent at the following URL:

https://s3-us-west-1.amazonaws.com/scout-public-downloads/apm_core_agent/release/scout_apm_core-v1.5.0-x86_64-unknown-linux-musl.tgz

Note the ending/release, where it's "scout_apm_core-${core_agent_version}-${core_agent_triple}.tgz"

You will need to have both the core-agent binary as well as the manifest.json, which can both be found in the .tgz.

Once these have been added, you will also need to add the following environment variables:
```bash
SCOUT_CORE_AGENT_DIR=/path/to/code/scout_apm_core #(path to where the binary and manifest.json are)
SCOUT_CORE_AGENT_TRIPLE=x86_64-unknown-linux-musl
SCOUT_CORE_AGENT_VERSION=v1.5.0
SCOUT_CORE_AGENT_DOWNLOAD=false
```

*If you will be manually launching the core-agent (see above), you will also want to set `SCOUT_CORE_AGENT_LAUNCH=false`*

## Troubleshooting

The core-agent's trace logging is much more verbose than our various language agent's debug levels and can be useful in certain scenarios.

For this example, I'm going to assume you're using OSX in local, but this can be done using a linux in a local or staging environment as well -- the core-agent downloaded will need to match the correct OS.

1. Create folder to store core-agent and logs
```bash
mkdir scout_apm_core && cd "$_"
```

2. Download OSX/Darwin core-agent
```bash
curl https://s3-us-west-1.amazonaws.com/scout-public-downloads/apm_core_agent/release/scout_apm_core-latest-x86_64-unknown-linux-musl.tgz --output core-agent-download.tgz
```

*https://s3-us-west-1.amazonaws.com/scout-public-downloads/apm_core_agent/release/scout_apm_core-latest-x86_64-apple-darwin.tgz for Mac OSX users*

3. Extract contents
```bash
tar -xvzf core-agent-download.tgz
```

4. Start core-agent with trace level logging. 
__Note:__ You may need to stop the other core-agent process, if there is one, else the core-agent will fail to start.
```bash
pkill -15 'core-agent'; ./core-agent start --daemonize false --log-level trace  --tcp 127.0.0.1:6590 --log-file ./core-agent.log
```

*It's important that `daemonize` is set to `false` or we won't capture the logs*

Send a request or two to your app, stop the core-agent process (ctrl-c / SIGINT), and then send the core-agent.log file that was created in the directory to [support@scoutapm.com](mailto:support@scoutapm.com)

Once you stop this process, the previous/other daemonized core-agent process will be (re)started automatically by the language agent on the next handled request.

## Change Log

The core-agent doesn't require/receive as many updates as the top level agents (Python, PHP, Elixir, etc.) that depend upon it.

However, here are the latest releases for the core-agent:

#### [1.5.0] 2023-12-11

* Send remaining batched payloads on receiving termination signals
* Capture background job metrics for latency and allocations

#### [1.4.0] 2021-11-04

##### Added

* Added External Services (HTTP Span) Support

#### [1.3.1] 2021-09-21

##### Changed

* TARGET=aarch64-unknown-linux-gnu for ARM support

#### [1.3.0] 2020-09-04

##### Added

* Probe and Shutdown now will use TCP if available, and UnixSocket doesn't connect

##### Changed

* Socket Path will no longer be automatically determined. The UnixSocket won't
  be started unless the configuration is explicitly set.


# Django

## Installation



## Installation

The latest `scout-apm` package supports Django 3.2+.

**Older Django Versions**: Older versions of Django may be supported by previous versions of the `scout-apm` package.

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Configure Scout in your `settings.py` file:

```python
# settings.py
INSTALLED_APPS = [
    "scout_apm.django",  # should be listed first
    # ... other apps ...
]

# Scout settings
SCOUT_MONITOR = True
SCOUT_KEY = "[AVAILABLE IN THE SCOUT UI]"
SCOUT_NAME = "A FRIENDLY NAME FOR YOUR APP"
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` instead of providing these settings in `settings.py`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.


## Middleware

Scout automatically inserts its middleware into your settings on Django startup in its [`AppConfig.ready()`](https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig.ready). 

It adds one at the very start of the middleware stack, and one at the end, allowing it to profile your middleware and views. 

This normally works just fine. 

However, if you need to customize the middleware order or prevent your settings being changed, you can include the Scout middleware classes in your settings yourself. Scout will detect this and not automatically insert its middleware. 

If you do customize, your metrics will be affected. Anything included before the first *middleware timing* middleware will not be profiled by Scout at all (unless you add custom instrumentation). Anything included after the *view* middleware will be profiled as part of your view, rather than as middleware. 

To add the middleware if you're using new-style Django middleware in the [`MIDDLEWARE` setting](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-MIDDLEWARE), which was added in Django 1.10:

```python
# settings.py
MIDDLEWARE = [
    # ... any middleware to run first ...
    "scout_apm.django.middleware.MiddlewareTimingMiddleware",
    # ... your normal middleware stack ...
    "scout_apm.django.middleware.ViewTimingMiddleware",
    # ... any middleware to run last ...
]
```
To add the middleware if you're using old-style Django middleware in the [`MIDDLEWARE_SETTINGS` setting](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-MIDDLEWARE_CLASSES), which was removed in Django 2.0:

```python
# settings.py
MIDDLEWARE_CLASSES = [
    # ... any middleware to run first ...
    "scout_apm.django.middleware.OldStyleMiddlewareTimingMiddleware",
    # ... your normal middleware stack ...
    "scout_apm.django.middleware.OldStyleViewMiddleware",
    # ... any middleware to run last ...
]
```


# Elixir

## Requirements

Our Elixir agent supports Elixir 1.14+, Phoenix 1.6+ (optional), and Ecto 3.x.
We also instrument LiveView, Oban, Finch, and Tesla packages.

Optional dependencies:
* `phoenix_live_view ~> 0.18 or ~> 1.0` â Required for LiveView and HEEx instrumentation

## Installation

Tailored instructions are provided within our user interface. General instructions for a Phoenix app:

**1.** Add the `scout_apm` dependency.

Your `mix.exs` file:
```elixir
# mix.exs

 def deps do
   [{:phoenix, "~> 1.6"},
    ...
    {:scout_apm, "~> 2.0"}]
 end
```

Shell:

```bash
mix deps.get
```

**2.** Download your customized config file, placing it at `config/scout_apm.exs`.

Your customized config file is available within your Scout account. Inside the file, replace `"YourApp"` with the app name you'd like to appear within Scout.

**3.** Integrate into your Phoenix app.

Instrument Controllers. In `lib/your_app_web.ex`:

```elixir
# lib/your_app_web.ex
defmodule YourApp.Web do
  def controller do
    quote do
      use Phoenix.Controller
      use ScoutApm.Instrumentation
      ...
```
Instrument Templates. In `config/config.exs`:
```elixir
# config/config.exs
config :phoenix, :template_engines,
  eex: ScoutApm.Instruments.EExEngine,
  exs: ScoutApm.Instruments.ExsEngine,
  heex: ScoutApm.Instruments.HEExEngine
```

**4.** Integrate Ecto

In `lib/my_app/application.ex`:
```elixir
# lib/my_app/application.ex
defmodule MyApp.Application do
  use Application

  def start(_type, _args) do
    children = [
        # ...
    ]
    :ok = ScoutApm.Instruments.EctoTelemetry.attach(MyApp.Repo)
    # ...
    Supervisor.start_link(children, opts)
  end
end
```

**5.** (Optional) Attach telemetry handlers for additional instrumentation.

In your `Application.start/2` function, attach handlers for the libraries you use:
```elixir
# lib/my_app/application.ex
def start(_type, _args) do
  # Attach Scout APM telemetry handlers
  ScoutApm.Instruments.LiveViewTelemetry.attach()        # Phoenix LiveView
  ScoutApm.Instruments.ObanTelemetry.attach()             # Oban background jobs
  ScoutApm.Instruments.FinchTelemetry.attach()            # Finch/Req HTTP client
  ScoutApm.Instruments.TeslaTelemetry.attach()            # Tesla HTTP client
  ScoutApm.Instruments.PhoenixErrorTelemetry.attach()     # Error monitoring

  children = [
    # ...
  ]
  Supervisor.start_link(children, opts)
end
```

**6.** Restart your app.

```bash
mix phx.server
```

## Updating to the Newest Version

**1.** Ensure your `mix.exs` dependency entry for `scout_apm` is: `{:scout_apm, "~> 2.0"}`

**2.**
```bash
mix deps.get scout_apm
```

**3.** Recompile and deploy.

## Auto-Instrumented Libraries

Our [install instructions](#installation) walk through instrumenting the following libraries:

* Phoenix
  * controllers
  * views
  * templates (EEx, Exs, and HEEx)
* Ecto 3.x (with database metrics)
* Phoenix LiveView (via telemetry)
* Oban (via telemetry)
* Finch / Req (via telemetry â [External Services](/docs/features/external-services))
* Tesla (via telemetry â [External Services](/docs/features/external-services))

See [instrumenting common libraries](/docs/elixir/features/#custom-instrumentation) for guides on instrumenting other Elixir libraries.


# Error-monitoring

Monitoring for your site just got easier. With our powerful error monitoring service backed by our class leading APM solution, get back to what really matters by easily consolidating your error service and APM solution into one. When the error monitoring service is enabled, you will gain access to the context in which errors occur on your application. With our high fidelity overview charts as well as our detailed error tracing, you will gain insights into your app's error trends as well as how these issues arose. 

### Enabling Error Monitoring 

Error Monitoring is available to apps using PHP 7.2+. It supports automatic exception handling for sym. To enable:

This adds a dependency on php-http/discovery. For this to work, you would already need an HTTP client installed, or install a compatible client.

**1.** Update to the latest version:

```sh
pip install scout-apm --upgrade
```

Error Monitoring was released in `scout-apm` version 7.0.0. Application monitoring must be enabled to use error monitoring.

**2.** Set the `monitor` and `errors_enabled` to `True`.

```shell
export SCOUT_MONITOR=True
export SCOUT_ERRORS_ENABLED=True
```

**3.** Laravel/Lumen: See instructions below based on version.

**3.** Symfony: No conguration required, but you will need to install something comparable to `composer require php-http/httplug nyholm/psr7` to enable the PSR-18 HTTP Client auto discovery.

**4.** Deploy

### Laravel 5/6/7
In order to capture errors, in your \App\Exceptions\Handler::report function in your application:

```php
    /**
     * Report or log an exception.
     *
     * @param  \Exception  $exception
     * @return void
     */
    public function report(Exception $exception)
    {
        $this->container->make(\Scoutapm\ScoutApmAgent::class)->recordThrowable($exception); // <-- add this line
        parent::report($exception);
    }
```

### Laravel 8
In order to capture errors, in your \App\Exceptions\Handler::register function in your application:

```php
    /**
     * Register the exception handling callbacks for the application.
     *
     * @return void
     */
    public function register()
    {
        $this->reportable(function (Throwable $e) {
            $this->container->make(ScoutApmAgent::class)->recordThrowable($e);
        });
    }
```

### Lumen
In order to capture errors, in your \App\Exceptions\Handler::report function in your application:
```php
    /**
     * Report or log an exception.
     *
     * This is a great spot to send exceptions to Sentry, Bugsnag, etc.
     *
     * @param  \Throwable  $exception
     * @return void
     *
     * @throws \Exception
     */
    public function report(Throwable $exception)
    {
        app(\Scoutapm\ScoutApmAgent::class)->recordThrowable($exception);
        parent::report($exception);
    }
```

### Reporting Exceptions

Once the above configurations have been added, if an exception bubbles up to our middleware we will capture it.

However, if an error is caught, the error will never be received by our signal handler. To report this error to Scout use:

Ex:

```php
try {
  throw new RuntimeException('something went wrong');
}
catch (RuntimeException $e) {
  $this->agent->recordThrowable($e);
  $this->agent->send();
}
```

### Adding Context

Adding context to errors works exactly the same as adding context to web endpoints and background jobs. 

If you have already added context to the endpoint or background job where the error has occurred, this context will be shown on the errors page.

#### Individual Error

To add context to an individual error, such as one that is caught:

```php
try {
  throw new RuntimeException('something went wrong');
}
catch (RuntimeException $e) {
  $this->agent->addContext("Key", "Value");
  $this->agent->recordThrowable($e);
  $this->agent->send();
}
```

Visit our [custom context section](/docs/php/advanced-features/#custom-context) to learn more.

### Error Notifications
Get notified of errors before your users notify you. 

With our notification system, you can get [error notifications sent to Slack, PagerDuty, Email, Webhooks, and more](/docs/integrations#alerting).



### Troubleshooting

If you receive an error, such as:

```shell
In ScoutErrorHandling.php line 66:
                                                         
  Class "Http\Discovery\Psr18ClientDiscovery" not found  

```
You need to resolve the HTTP discovery dependency, because your installed packages do not satisfy the requirement.

For example, if you are on PHP 7.1 and need Guzzle 6, `composer require php-http/guzzle6-adapter nyholm/psr7` will fulfill the dependencies.

On PHP 7.2+, `composer require guzzlehttp/guzzle:^7.0` is already compatible.

### Not seeing errors?

Reach out to us at [support@scoutapm.com](mailto:support@scoutapm.com) for further support and [troubleshooting](/docs/python/troubleshooting) assistance


# Error-monitoring

Scout's Error Monitoring feature allows you to track, triage, and resolve Ruby application errors directly within the Scout UI. By integrating with our existing APM agent, we provide enhanced context and filtering capabilities for comprehensive error management.

## Installation



```ruby
gem 'scout_apm'
```



```yaml
common: &defaults

     # ... other Scout APM settings

     errors_enabled: true
```



Once enabled, Scout will automatically begin capturing and organizing errors from your application.


## Installation

**A** If you haven't, add the `scout_apm` gem to your gemfile.

```ruby
gem 'scout_apm'
```

**B** Configure Scout in your `scout_apm.yml` configuration file:

```yaml
common: &defaults

     # ... other Scout APM settings

     errors_enabled: true
```

**C** Deploy!

Once enabled, Scout will automatically begin capturing and organizing errors from your application.


## Configuration Options

The following configuration settings are available for error monitoring. These can be set in the `scout_apm.yml` configuration file or as environment variables with the `SCOUT_` prefix, e.g. `SCOUT_ERRORS_ENABLED`.

Only `errors_enabled` is required to enable error monitoring. The rest are optional.

Setting Name | Description | Default | Required
--- | --- | --- | ---
errors_enabled | True or false. If true, monitor errors and send them to Scout | `false` | Yes
errors_ignored_exceptions | Excludes certain exceptions from being reported | `[ActiveRecord::RecordNotFound, ActionController::RoutingError]` | No
errors_filtered_params | Filtered parameters in exceptions | `[password, s3-key]` | No
errors_env_capture | Additional environment (request.env) key, values to capture. | `[]` | No


## Custom Error Reporting

In addition to automatically capturing unhandled exceptions, Scout provides an API for manually reporting errors with custom context.

### Error Capture API

The `ScoutApm::Error.capture` method accepts up to four arguments:

```ruby
ScoutApm::Error.capture(error, context = {}, env: nil, name: nil)
```

- **error** (required): A string message or Exception object
- **context** (optional): Hash of custom context data
- **env** (optional, named): Request environment (e.g., `request.env`)
- **name** (optional, named): Custom error name (if not specified, will be named: `ScoutApm::Error::Custom`)

### Basic Usage

```ruby
# Simple string message
ScoutApm::Error.capture("Something went boom")

# With custom context, will be given default name of `ScoutApm::Error::Custom`
ScoutApm::Error.capture("Something went boom", {"user_id" => current_user.id, "action" => "checkout"})

# With full context and environment
ScoutApm::Error.capture(
  "Something went boom", 
  {"context_key" => "context_value"}, 
  env: request.env, 
  name: "BoomError"
)
```

### Rescued Exception Example

```ruby
class CheckoutController < ApplicationController
  def create
    begin
      process_payment(params[:payment_info])
    rescue PaymentGatewayError => e
      # Report the rescued error with additional context.
      # Can also capture context via the API in addition to passing it in as
      # an argument. See 'Ruby Features' for docs on context.
      ScoutApm::Context.add(company_id: @company.id)
      ScoutApm::Context.add_user(id: @user.id)
      ScoutApm::Error.capture(
        e,
        env: request.env,
        # name: "PaymentProcessingError" # Not needed, we will capture it automatically from the exception class.
      )
      
      # Handle the error gracefully for the user
      redirect_to checkout_path, alert: "Payment failed. Please try again."
    end
  end
end
```

## Error Context and Attributes

Scout automatically enriches error data with contextual information:

- **Entrypoint**: The top-level action (e.g. Controller class) where the error occurred
- **Custom Context**: All key-value pairs from any [Custom Context](/docs/ruby/features/#custom-context) that you have set
- **Request Data**: HTTP method, URI, parameters, and headers
- **User Context**: User identification and session information (when configured)

This context makes it easy to understand the circumstances that led to each error occurrence.

## Data Retention

Scout retains error data for **30 days**, and aggregate parent groups (total counts, first seen at (& sha), last error message, etc) indefinitely, providing sufficient time for analysis and resolution tracking. This retention period allows teams to:

- Identify recurring error patterns
- Analyze error trends over time
- Maintain historical context for resolved issues
- Support post-incident analysis and learning

## Integration with APM

Error monitoring seamlessly integrates with Scout's APM features:

- **Performance Context**: View error occurrences alongside performance traces
- **Endpoint Analysis**: Identify which endpoints generate the most errors
- **Critical Endpoint Errors**: Automatically prioritize errors from marked critical endpoints
- **Time Correlation**: Correlate errors with performance degradation events

For more detailed information on error management features, triage workflows, and team collaboration tools, see the main [Error Monitoring documentation](/features/error-monitoring).

## How It Works

Error monitoring is built into the Scout APM Ruby agent. When an error occurs in your Rails application, Scout automatically captures:

- Complete stack trace showing the execution path leading to the error
- Request information including URI, method, and parameters
- Application context including custom context data
- Error grouping based on error type and location

For Rails applications, Scout integrates directly with the Rails error handling system to capture both handled and unhandled exceptions.

## Not seeing errors?

Reach out to us at [support@scoutapm.com](mailto:support@scoutapm.com) for further support and [troubleshooting](/docs/python/troubleshooting) assistance


# Error-monitoring

## Installation

Enabling Scout's Error Monitoring works with your existing Scout APM setup. Error monitoring is built into the same libraries that provide APM monitoring.




**Note:** Error monitoring is available for [Ruby](/docs/ruby/error-monitoring), [Python](/docs/python/error-monitoring), [PHP](/docs/php/error-monitoring) and [Elixir](/docs/elixir/features#error-monitoring) agents.

## Installation

### Ruby/Rails

**For a Rails Application**

Error monitoring is built into the Scout APM Ruby agent.

**A** If you haven't, add the `scout_apm` gem to your gemfile.

```ruby
gem 'scout_apm'
```

**B** Configure Scout in your `scout_apm.yml` configuration file:

```yaml
common: &defaults

     # ... other Scout APM settings

     errors_enabled: true
```

**C** Deploy!

Once enabled, Scout will automatically begin capturing and organizing errors from your application.

### Python

**For a Python Application**

Error monitoring is built into the Scout APM Python agent.

**A** If you haven't already, set up [Scout APM for Python](/docs/python/).

**B** Enable error monitoring by setting the environment variable:

```bash
export SCOUT_ERRORS_ENABLED=true
```

**C** Deploy!

Once enabled, Scout will automatically begin capturing and organizing errors from your application.

### PHP

**For a PHP Application**

Error monitoring is built into the Scout APM PHP agent.

**A** Install the [Scout PHP package](https://packagist.org/packages/scoutapp/scout-apm-php) via Composer:

```bash
composer require scoutapp/scout-apm-php
```

**B** Configure and initialize Scout in your application:

```php
use Psr\Log\LoggerInterface;
use Psr\Log\LogLevel;
use Scoutapm\Agent;
use Scoutapm\Config;
use Scoutapm\Config\ConfigKey;

/** @var LoggerInterface $psrLoggerImplementation */

$agent = Agent::fromConfig(
    Config::fromArray([
        ConfigKey::APPLICATION_NAME => 'Your application name',
        ConfigKey::APPLICATION_KEY => 'your scout key',
        ConfigKey::MONITORING_ENABLED => true,
        ConfigKey::ERRORS_ENABLED => true, // <-- add this to enable error tracking
        ConfigKey::LOG_LEVEL => LogLevel::ERROR, // <-- optional: reduce logging verbosity
    ]),
    $psrLoggerImplementation
);
```

**C** Deploy!

Once enabled, Scout will automatically begin capturing and organizing errors from your application.

### Elixir

**For an Elixir/Phoenix Application**

Error monitoring is built into the Scout APM Elixir agent (v2.0+).

**A** If you haven't already, add `scout_apm` to your `mix.exs`:

```elixir
{:scout_apm, "~> 2.0"}
```

**B** Attach the Phoenix error telemetry handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Instruments.PhoenixErrorTelemetry.attach()
  # ... rest of supervision tree
end
```

**C** Deploy!

Error monitoring is enabled by default (`errors_enabled: true`). See the [Elixir features docs](/docs/elixir/features#error-monitoring) for manual error capture and further configuration options.


## Overview

Scout's Error monitoring provides comprehensive error tracking and triage capabilities designed to help development teams efficiently identify, prioritize, and resolve application issues. By integrating seamlessly with Scout APM, error data is automatically enriched with performance context, making it easier to understand the full impact of errors on your application.

Key features include:

- **Error Grouping**: Similar errors are automatically grouped together for easier monitoring
- **Smart Prioritization**: Critical endpoint errors are automatically flagged as high priority
- **Team Collaboration**: Assign errors to team members for clear ownership and organization
- **Flexible Triage**: Resolve, defer, or reactivate errors with full audit trails
- **Rich Context**: View error traces with GitHub integration for immediate code visibility
- **Bulk Operations**: Efficiently manage multiple error groups simultaneously



## Error monitoring Home

The Error monitoring home page provides a comprehensive overview of your application's error landscape. This central dashboard displays error groups - collections of similar errors that have been automatically organized for efficient monitoring.

### Error Summary

At the top of the page, you'll find key metrics for your selected timeframe:

- **Total Errors**: The complete count of error occurrences
- **New Errors**: Errors that first appeared during the selected time period
- **Critical Endpoint Errors**: Errors from endpoints marked as critical (automatically high priority)

### Error Groups

The main interface displays error groups in a sortable table with the following information:

- **Error Name/Type**: The specific error class or message
- **Location**: Where the error occurred in your codebase
- **Sparkline**: Visual representation of error frequency over time
- **Event Count**: Total occurrences and recent activity
- **Request URI**: The endpoint where errors occurred
- **Assignment**: Team members responsible for resolution
- **Priority**: Error priority level (Low, Medium, High)

### Bulk Actions

The interface supports efficient bulk operations on selected error groups:

- **Resolve**: Mark error groups as resolved, removing them from the default view
- **Assign**: Assign error groups to specific team members
- **Prioritize**: Set priority levels for multiple errors simultaneously

### Filtering and Views

Use the filtering controls to focus on specific error states:

- **Unresolved**: Show only active error groups (default view)
- **Resolved**: Display previously resolved error groups
- **All**: Show both resolved and unresolved errors

Additional filters allow you to narrow results by priority, assignment, or other criteria.

## Error Details & Triage



Clicking on any error group takes you to the detailed error view, where you can examine specific error instances and perform triage actions.

### Error Context

The error detail page provides comprehensive context for understanding and resolving issues:

- **Error Trace**: Complete stack trace showing the execution path leading to the error
- **Request Information**: Details about the HTTP request that triggered the error
- **Application Context**: Relevant application state and custom context data
- **GitHub Integration**: When enabled, view the exact code that caused the error directly in the interface

### Triage Actions

Scout provides three primary triage actions for managing errors:

#### Resolve
Mark an error group as resolved when the underlying issue has been fixed. Resolved errors are removed from the default view but remain accessible through filtering. If an error occurs after it has been resolved, it will become unresolved and considered active again. 

#### Defer
Temporarily silence an error group until a specified date and time. This is useful for:
- Known issues scheduled for future releases
- Errors that require coordination with external teams
- Non-critical issues that can be addressed during planned maintenance

To defer an error, hover over the Resolve button and select the defer option, then choose your desired date and time.

#### Reactivate
Reopen previously resolved errors if issues resurface or were prematurely closed. Errors will be automatically reactivated if a previously resolved error occurs again.

### Priority monitoring

Set error priorities to help your team focus on the most critical issues:

- **High**: Critical errors requiring immediate attention
- **Medium**: Important issues that should be addressed soon
- **Low**: Minor issues that can be resolved when time permits

### Error Exploration

Use the "Explore" button to access a comprehensive list of all individual error occurrences. Scout retains individual error data for 30 days, and aggregate parent groups indefinitely (total counts, first seen at (& sha), last error message, etc).

## Critical Endpoints

Scout's critical endpoint feature automatically elevates the priority of errors occurring on your most important application endpoints.

### Marking Critical Endpoints

To designate an endpoint as critical:

1. Navigate to the Web Endpoints view
2. Select the specific endpoint you want to mark as critical
3. Toggle the critical endpoint slider in the top-right corner of the endpoint header



### Automatic Priority Assignment

When an endpoint is marked as critical:

- All new errors from that endpoint are automatically assigned **High** priority
- This ensures immediate visibility for errors on your most important application paths

### Priority Persistence

Important notes about critical endpoint priority monitoring:

- Errors that occurred while an endpoint was critical retain their high priority even if the endpoint is later unmarked
- This ensures that historical high-priority errors maintain their status for consistent tracking
- Only newly occurring errors are affected by changes to critical endpoint status

## Retention and Data monitoring

Scout retains individual errors for **30 days**, and aggregate parent groups (total counts, first seen at (& sha), last error message, etc) indefinitely, providing sufficient time for analysis and resolution tracking. This retention period allows teams to:

- Identify recurring error patterns
- Analyze error trends over time
- Maintain historical context for resolved issues
- Support post-incident analysis and learning

## Team Collaboration

### Assignment

Assign error groups to specific team members to clarify ownership and ensure accountability:

- Select one or more error groups from the main interface
- Use the assignment dropdown to designate responsible team members
- Assignments are visible on both the main error list and individual error detail pages
- Team members can filter errors to see only those assigned to them

### Notifications and Alerting



Scout's notification system keeps teams informed about error activity through multiple channels:

- High-priority errors trigger immediate notifications
- Notifications are sent to configured notification groups and channels (not based on individual assignments)  
- Deferred errors send notifications when they become active again

#### Supported Alert Channels

Scout integrates with popular alerting and communication platforms:

- **Slack** - Get instant notifications in your team channels
- **Email** - Traditional email alerts for error notifications
- **Webhook** - Custom webhook integration for your own systems
- **PagerDuty** - Critical error escalation and incident management
- **Splunk On-Call** (formerly VictorOps) - Real-time incident response
- **Opsgenie** - Advanced alerting and on-call management

For detailed configuration and setup instructions for each platform, see the [Alerting documentation](/docs/features/alerting).

## FAQ

### How are errors grouped together?

Scout automatically groups similar errors based on the error type, location in code, and request components. This intelligent grouping helps reduce noise and allows you to focus on underlying issues rather than individual error instances.

### How do notifications work with deferred errors?

When you defer an error, Scout stops sending notifications about new occurrences until the specified date and time. Once the deferral period expires, the error group becomes active again and normal notification rules apply.

### What happens if I disable errors on a critical endpoint?

If you remove the critical endpoint designation, only new errors will be affected. Existing errors that were marked as high priority while the endpoint was critical will retain their high priority status.

### Does error tracking affect application performance?

Scout's error tracking is designed to have minimal performance impact. Error capture and reporting happen asynchronously and use efficient data structures to avoid affecting your application's response times.


# Error-monitoring

Scout's Error Monitoring feature allows you to track, triage, and resolve Python application errors directly within the Scout UI. By integrating with our existing APM agent, we provide enhanced context and filtering capabilities for comprehensive error management.

## Installation





```bash
export SCOUT_ERRORS_ENABLED=true
```



Once enabled, Scout will automatically begin capturing and organizing errors from your application.


## Installation

**A** If you haven't already, set up [Scout APM for Python](/docs/python/).

**B** Enable error monitoring by setting the environment variable:

```bash
export SCOUT_ERRORS_ENABLED=true
```

**C** Deploy!

Once enabled, Scout will automatically begin capturing and organizing errors from your application.


## Configuration Options

The following configuration settings are available for error monitoring. These can be set as environment variables with the `SCOUT_` prefix or in your application configuration.

Only `errors_enabled` is required to enable error monitoring. The rest are optional.

Setting Name | Description | Default | Required
--- | --- | --- | ---
errors_enabled | True or False. If true, monitor errors and send them to Scout. | `False` | Yes
errors_ignored_exceptions | Excludes certain exceptions from being reported. | `()` | No
errors_batch_size | Batch size of errors before sending. | `5` | No

## Custom Error Reporting

Scoutâs error monitoring will automatically capture errors raised on the Django signal `got_request_exception` and the Celery signal `task_failure`.

There is no visible effect on your application, and the error will be propagated further on.

However, if an error is caught, the error will never be received by our signal handler. To report this error to Scout use:

```python
import scout_apm.api
scout_apm.api.Error.capture(e)
```

Ex:

```python
import scout_apm.api
try:
    raise ValueError("Oh No!")
except ValueError as e:
    scout_apm.api.Error.capture(e)
```

The capture function supports a number of additional parameters to support manually instrumenting other frameworks.

* `request_path` -  The relative path for the request such as: `"/test/"`
* `request_params` - A dict representing the query string parameters. This should be JSON-serializable.
* `session` - A dict representing the session for the request. This should be JSON-serializable.
* `custom_controller` - A string that is used to identify the controller or job, such as a background task name.
* `custom_params` - A dict of any additional values that should be included with the error. These will be unassociated with the `scout_apm.api.Context`. This should be JSON-serializable.

Ex:

```python
from datetime import datetime
import scout_apm.api

# Assume request exists that contains the properties:
# path, session and GET

try:
    raise ValueError("Oh No!")
except ValueError as e:
    scout_apm.api.Error.capture(
        e,
        request_path=request.path,
        request_params=request.GET,
        request_session=request.session,
        custom_controller="broken_view",
        custom_params={"datetime": datetime.utcnow().isoformat()}
    )
```

### Adding Context

Adding context to errors works exactly the same as adding context to web endpoints and background jobs. 

If you have already added context to the endpoint or background job where the error has occurred, this context will be shown on the errors page.

#### Individual Error

To add context to an individual error, such as one that is caught:

```python
import scout_apm.api

try
    raise ValueError("Oh No!")
except ValueError as e:
    scout_apm.api.Context.add("account_id", account.id)
    scout_apm.api.Context.add("user_id", request.user.id)
    scout_apm.api.Error.capture(e)
```

Visit our [custom context section](/docs/python/advanced-features/#custom-context) to learn more.

## How It Works

Error monitoring is built into the Scout APM Python agent. When an error occurs in your Python application, Scout automatically captures:

- Complete stack trace showing the execution path leading to the error
- Request information including URI, method, and parameters
- Application context including custom context data
- Error grouping based on error type and location

Scout integrates with popular Python frameworks including Django, Flask, FastAPI, and others to capture both handled and unhandled exceptions.

## Framework Integration

### Django

For Django applications, Scout automatically integrates with Django's exception handling:

```python
# Django settings.py
INSTALLED_APPS = [
    'scout_apm.django',
    # ... other apps
]

# Enable error monitoring
import os
os.environ['SCOUT_ERRORS_ENABLED'] = 'true'
```

### Flask

For Flask applications:

```python
from scout_apm.flask import ScoutApm
import os

app = Flask(__name__)
os.environ['SCOUT_ERRORS_ENABLED'] = 'true'
ScoutApm(app)
```

### FastAPI

For FastAPI applications:

```python
from scout_apm.fastapi import ScoutMiddleware
import os

app = FastAPI()
os.environ['SCOUT_ERRORS_ENABLED'] = 'true'
app.add_middleware(ScoutMiddleware)
```

## Error Context and Attributes

Scout automatically enriches error data with contextual information:

- **Entrypoint**: The top-level view or function where the error occurred
- **Custom Context**: All key-value pairs from any custom context that you have set
- **Request Data**: HTTP method, URI, parameters, and headers
- **Framework Context**: Framework-specific context like controller names, etc.

This context makes it easy to understand the circumstances that led to each error occurrence.

## Data Retention

Scout retains individual errors for **30 days**, and aggregate parent groups (total counts, first seen at (& sha), last error message, etc) indefinitely, providing sufficient time for analysis and resolution tracking. This retention period allows teams to:

- Identify recurring error patterns
- Analyze error trends over time
- Maintain historical context for resolved issues
- Support post-incident analysis and learning

## Integration with APM

Error monitoring seamlessly integrates with Scout's APM features:

- **Performance Context**: View error occurrences alongside performance traces
- **Endpoint Analysis**: Identify which endpoints generate the most errors
- **Critical Endpoint Errors**: Automatically prioritize errors from marked critical endpoints
- **Time Correlation**: Correlate errors with performance degradation events

For more detailed information on error management features, triage workflows, and team collaboration tools, see the main [Error Monitoring documentation](/features/error-monitoring).

## Not seeing errors?

Reach out to us at [support@scoutapm.com](mailto:support@scoutapm.com) for further support and [troubleshooting](/docs/python/troubleshooting) assistance


# Error-monitoring

This page contains information on hooking up third party error monitoring solutions into Scout. 

If you're looking to receive notifications from Scout's error monitoring solution, please visit [the following docs](/docs/integrations/alerting).

## Rollbar

When the Rollbar integration is enabled, Scout displays errors from the app's associated Rollbar project alongside performance data within the Scout UI.



When the error count is in <span style="color:#fff;background:#f0592a;padding: 2px">orange</span>, a new error has appeared in the current timeframe. When the error count is in <span style="background:#ccc;padding:2px">gray</span>, older errors are continuing in this timeframe.

### Rollbar Configuration

The Rollbar configuration is an __app-specific__ integration, configured by providing a read-only Rollbar __Project Access Token__ (not an Account Access Token) in the app settings within Scout.





## Sentry

When the Sentry integration is enabled, Scout displays errors from the app's associated Sentry project alongside performance data within the Scout UI.  You can either use the hosted service found on [Sentry.io](https://www.sentry.io) or you can use the self-hosted Sentry option.



When the error count is in orange, a new error has appeared in the current timeframe. When the error count is in gray, older errors are continuing in this timeframe.

### Sentry Configuration

The Sentry configuration is an __app-specific__ integration, configured by providing a read-only Sentry __Access Token__ in the app settings within Scout.





**Note:**  If you are using the self-hosted option, please make sure to include the full URL in the base URL field.  `https://self-hosted.sentry.com/api/0`, not `selfhost.sentry.com/api/0`.

## Honeybadger

When the Honeybadger integration is enabled, Scout displays errors from the app's associated Honeybadger project alongside performance data within the Scout UI.



When the error count is in orange, a new error has appeared in the current timeframe. When the error count is in gray, older errors are continuing in this timeframe.

### Honeybadger Configuration

The Honeybadger configuration is an __app-specific__ integration, configured by providing a read-only Honeybadger __Personal API Key__ in the app settings within Scout.

This is different than the API keys found on the project, and is the API Key found on your User's profile:



Once you've entered the Honeybadger Personal API Key into the field, it should load your projects to choose from:


# Express

## Express 

Scout supports Express 4.x+.

**1.** Install the `@scout_apm/scout-apm` package:
```bash
yarn add @scout_apm/scout-apm
```        

**2.** Add to Express Middleware:
```javascript
// Require scout-apm first, before other requires
const scout = require("@scout_apm/scout-apm");
const express = require("express");

// The "main" function
async function start() {
  // Trigger the download and installation of the core-agent
  await scout.install({
    allowShutdown: true, // allow shutting down spawned scout-agent processes from this program
    monitor: true, // enable monitoring
    name: "",
    key: "",
  });

  // Initialize your express application
  const app = express();

  // Enable the app-wide scout middleware
  app.use(scout.expressMiddleware());

  // Add other middleware and routes
  // app.use( ... )
  // app.get( ... )

  // Start express
  app.start();
}

// If this script is executed directly, run the start function
if (require.main === module) { start(); } 
```
**3.** Configure Scout via ENV variables:

`export SCOUT_MONITOR=true`

`export SCOUT_KEY="[AVAILABLE IN THE SCOUT UI]"`

`export SCOUT_NAME="A FRIENDLY NAME FOR YOUR APP"`

**NOTE** Pass configuration to `scout.install` and if a scout agent instance does not exist already one will be created for you on the fly. After `await`ing or `.then`ing the `Promise` returned by `scout.install`, you can be sure that the scout agent is available and enable the middleware by calling `app.use(scout.expressMiddleware())`. If you do *not* call `scout.install({ ... })` and wait for setup to complete, the first inbound request will start the setup and eventually requests will be recorded (setup will not block requests, and recording will start when the agent has been set up).

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**4.** Deploy.

It takes just a few minutes for your data to first appear within the Scout UI.


# Faq

## Heroku

Scout runs on Heroku without any special configuration. When Scout detects that an app is being served via Heroku:

* Logging is set to `STDOUT` vs. logging to a file. Log messages are prefixed with `[Scout]` for easy filtering.
* The dyno name (ex: `web.1`) is reported vs. the dyno hostname. Dyno hostnames are dynamically generated and don't have any meaningful information.

### Configuration

Scout can be configured via environment variables. This means you can use `heroku config:set` to configure the agent. For example, you can set the application name that appears in the Scout UI with:

```bash
heroku config:set SCOUT_NAME='My Heroku App'
```

See the configuration section for more information on the available config settings and environment variable functionality.

### Using the Scout Heroku Add-on

Scout is also available as a [Heroku Add-on](https://elements.heroku.com/addons/scout). The add-on automates setting the proper Heroku config variables during the provisioning process.

### Adding the Database Addon

To get more insights into how your database is performing, check out our [Database Addon](https://devcenter.heroku.com/articles/scout#database-monitoring-addon).

## Docker

Scout runs within Docker containers without any special configuration.

However, it may be easier to dockerize the core-agent. We suggest using our [Docker image for this](/docs/core-agent#with-docker).

## Transactions

### What is a transaction
A transaction is anytime that you application handles a request or runs a background job. To get a better understanding of your transaction volume, visit your [usage page](https://scoutapm.com/usage) for more info

### Ignoring Transactions
**Note**:
*When a transaction is ignored, we will not collect metric data or traces for the request. When ignoring transactions and using sampling, data may be skewed and important traces may be missed.*

If you don't want to track the current web request or background job, at any point you can call `ignore()` to ignore it:

```php
use Scoutapm\Laravel\Facades\ScoutApm; // Laravel only: Add near the other use statements

ScoutApm::ignore()

// or if you have an $agent instance:
$agent->ignore()
```

#### Sampling
Use probability sampling to limit the number of web requests or background jobs Scout analyzes:

```php
use Scoutapm\Laravel\Facades\ScoutApm; // Laravel only: Add near the other use statements


$randomFloat = mt_rand(0, mt_getrandmax() - 1) / mt_getrandmax();

// Sample rate should range from 0-1:
// * 0: captures no requests
// * 0.9: captures 90% of requests
// * 1: captures all requests
$sampleRate = 0.9;

if ( $randomFloat > $sampleRate) {
  ScoutApm::ignore();

  // or if you have an $agent instance:
  $agent->ignore();
}
```


# Faq

## Heroku

Scout runs on Heroku without any special configuration. When Scout detects that an app is being served via Heroku:

* Logging is set to `STDOUT` vs. logging to a file. Log messages are prefixed with `[Scout]` for easy filtering.
* The dyno name (ex: `web.1`) is reported vs. the dyno hostname. Dyno hostnames are dynamically generated and don't have any meaningful information.

### Configuration

Scout can be configured via environment variables. This means you can use `heroku config:set` to configure the agent. For example, you can set the application name that appears in the Scout UI with:

```bash
heroku config:set SCOUT_NAME='My Heroku App'
```

See the configuration section for more information on the available config settings and environment variable functionality.

### Using the Scout Heroku Add-on

Scout is also available as a [Heroku Add-on](https://elements.heroku.com/addons/scout). The add-on automates setting the proper Heroku config variables during the provisioning process.

## Docker

Scout runs within Docker containers without any special configuration.

However, it may be easier to dockerize the core-agent. We suggest using our [Docker image for this](/docs/core-agent#with-docker).

## Transactions

### What is a transaction
A transaction is anytime that you application handles a request or runs a background job. To get a better understanding of your transaction volume, visit your [usage page](https://scoutapm.com/usage) for more info

### Ignoring Transactions

**Note**:
*When a transaction is ignored, we will not collect metric data or traces for the request. When ignoring transactions and using sampling, data may be skewed and important traces may be missed.*

If you don't want to track the current transaction, at any point you can call `scout.api.ignoreTransaction()` to ignore it:

```javascript
const scout = require("@scout_apm/scout-apm");

if (isHealthCheck) {
  scout.api.ignoreTransaction()
}
```

You can use this whether the transaction was started from a built-in integration or custom instrumentation.

You can also ignore a set of URL path prefixes by configuring the `ignore` setting in your `ScoutConfiguration`:

```javascript
scout.buildScoutConfiguration({
  ignore: ["/health-check/", "/admin/"],
});
```

When specifying this as an environment variable, it should be a comma-separated list:

```bash
export SCOUT_IGNORE='/health-check/,/admin/'
```


# Faq

## Heroku <img src="images/heroku.png" style="float:right;width: 150px" />

Scout runs on Heroku without any special configuration. When Scout detects that an app is being served via Heroku:

* Logging is set to `STDOUT` vs. logging to a file. Log messages are prefixed with `[Scout]` for easy filtering.
* The dyno name (ex: `web.1`) is reported vs. the dyno hostname. Dyno hostnames are dynamically generated and don't have any meaningful information.

### Configuration

Scout can be configured via environment variables. This means you can use `heroku config:set` to configure the agent. For example, you can set the application name that appears in the Scout UI with:

```bash
heroku config:set SCOUT_NAME='My Heroku App'
```

See the configuration section for more information on the available config settings and environment variable functionality.

### Using the Scout Heroku Add-on

Scout is also available as a [Heroku Add-on](https://elements.heroku.com/addons/scout). The add-on automates setting the proper Heroku config variables during the provisioning process.

## Docker <img src="images/docker.png" style="float:right;width: 150px" />

Scout runs within Docker containers without any special configuration.

It's common to configure Docker containers with environment variables. Scout can use environment variables instead of the `scout_apm.yml` config file.


## Cloud Foundry <img src="images/cf_logo.png" style="float:right;width: 150px" />

Scout runs on Cloud Foundry without any special configuration.

We suggest a few configuration changes in the `scout_apm.yml` file to best take advantage of Cloud Foundry:

1. Set `log_file_path: STDOUT` to send your the Scout APM log contents to the Loggregator.
2. Use the application name configured via Cloud Foundry to identify the app.
3. Override the hostname reported to Scout. Cloud Foundry hostnames are dynamically generated and don't have any meaningful information. We suggest using a combination of the application name and the instance index.

A sample config for Cloud Foundry that implements the above suggestions:

```yaml
common: &defaults
  key: YOUR_KEY
  monitor: true
  # use the configured application name to identify the app.
  name: <%= ENV['VCAP_APPLICATION'] ? JSON.parse(ENV['VCAP_APPLICATION'])['application_name'] : "YOUR APP NAME (#{Rails.env})" %>
  # make logs available to the Loggregator
  log_file_path: STDOUT
  # reports w/a more identifiable instance name using the application name and instance index. ex: rails-sample.0
  hostname: <%= ENV['VCAP_APPLICATION'] ? "#{JSON.parse(ENV['VCAP_APPLICATION'])['application_name']}.#{ENV['CF_INSTANCE_INDEX']}"  : Socket.gethostname %>

production:
  <<: *defaults

development:
  <<: *defaults
  monitor: false

test:
  <<: *defaults
  monitor: false

staging:
  <<: *defaults
```

## ActionController::Metal

Prior to agent version 2.1.26, an extra step was required to instrument `ActionController::Metal`
and <span style="white-space: nowrap;">`ActionController::Api`</span> controllers. After 2.1.26, this is automatic.

The previous instructions which had an explicit `include` are no longer
needed, but if that code is still in your controller, it will not harm
anything. It will be ignored by the agent and have no effect.

## Rake + Rails Runner

Scout doesn't have a dedicated API for instrumenting `rake` tasks or transactions called via `rails runner`. Instead, we suggest creating basic wrapper tasks that spawn a background job in a [framework we support](/docs/ruby/#instrumented-libraries). These jobs are automatically monitored by Scout and appear in the Scout UI under "background jobs".

For example, the following is a CronJob that triggers the execution of an `IntercomSync` background job:

```bash
10 * * * * cd /home/deploy/your_app/current && rails runner 'IntercomSync.perform_later'
```

## Sneakers

Scout doesn't instrument [Sneakers](https://github.com/jondot/sneakers) (a background processing framework for Ruby and RabbitMQ) automatically. To add Sneakers instrumentation:

* [Download the contents of this gist](https://gist.github.com/itsderek23/685c7485a3bd020b6cdd9b1d61cb847f). Place the file inside your application's `/lib` folder or similar.
* In `config/boot.rb`, add: `require File.expand_path('lib/scout_sneakers.rb', __FILE__)`
* In your `Worker` class, immediately following the `work` method, add<br/>`include ScoutApm::BackgroundJobIntegrations::Sneakers::Instruments`.

This treats calls to the `work` method as distinct transactions, named with the worker class.

Example usage:

```ruby
class BaseWorker
  include Sneakers::Worker

  def work(attributes)
    # Do work
  end
  # This MUST be included AFTER the work method is defined.
  include ScoutApm::BackgroundJobIntegrations::Sneakers::Instruments
end
```

## Overhead Considerations

Scout is built for production monitoring and is engineered to add minimal overhead. We test against several open-source benchmarks on significant releases to prevent releasing performance regressions.

There are a couple of scenarios worth mentioning where more overhead than expected may be observed.

### Enabling the detailed_middleware option

By default, Scout aggregates all middleware timings together into a single "Middleware" category. Scout can provide a detailed breakdown of middleware timings by setting `detailed_middleware: true` in the configuration settings.

This is `false` by default as instrumenting each piece of middleware adds additional overhead. It's common for Rails apps to use more than a dozen pieces of middleware. Typically, time spent in middleware is very small and isn't worth instrumenting. Additionally, most of these middleware pieces are maintained by third-parties and are thus more difficult to optimize.

### Resque Instrumentation

Since Resque works by forking a child process to run each job and exiting immediately when the job is finished, our instrumentation needs a way to aggregate the timing results and traces into a central store before reporting the information to our service. To support Resque, the Resque child process sends a simple payload to the parent which is listening via WEBRick on localhost. As long as there is one WEBRick instance listening on the configured port, then any Resque children will be able to send results back to it.

The overhead is usually small, but it is more significant than instrumenting background job frameworks like Sidekiq and DelayedJob that do not use forking. The lighter the jobs are, more overhead is incurred in the serialization and reporting to WEBRick. In our testing, for jobs that took ~18 ms each, we found that the overhead is about ~8%. If your jobs take longer than that, on average, the overhead will be lower.

## Transactions

### What is a transaction
A transaction is anytime that you application handles a request or runs a background job. To get a better understanding of your transaction volume, visit your [usage page](https://scoutapm.com/usage) for more info

### Ignoring transactions

**Note**:
*When a transaction is ignored, we will not collect metric data or traces for the request. When ignoring transactions and using sampling, data may be skewed and important traces may be missed.*

There are a couple of approaches to ignore web requests and background jobs you don't care to instrument. These approaches are listed below.

#### In your code

To selectively ignore a web request or background job in your code, add the following within the transaction:

```ruby
ScoutApm::Transaction.ignore!
```

#### Sampling configuration

There are a few [configuration options](/docs/ruby/configuration#sample_rate) that allow you to sample requests to specific web endpoints or background jobs. This is useful to reduce overall volume or ignore select endpoints or jobs entirely. By default, no sampling or ignoring is applied, and all requests are captured.

##### Sampling Precedence

More specific sampling configurations take precedence over broader ones. If `sample_endpoints` is used, requests matching those URI prefixes will always be sampled at the rate specified for the matching prefix, regardless of `endpoint_sample_rate` or `sample_rate`. All endpoints that don't match any prefixes in `sample_endpoints` will be sampled according to `endpoint_sample_rate`, regardless of `sample_rate`. Finally, `sample_rate` is the global catch-all. The same goes for backgound job sampling using `sample_jobs` and `job_sample_rate`.

The order in which endpoints are listed in `sample_endpoints` will determine the precedence. More specific endpoints should be listed before others with the same base. The rate specified for the first matching endpoint prefix will be used. For example, if you have `['/api/v1:50', '/api:90']`, requests to `/api/v1` will be sampled at 50%, and the other requests to `/api` will be sampled at 90%.

You can also disable all background jobs by setting `enable_background_jobs: false` in your configuration file. See the [configuration option](/docs/ruby/configuration#enable_background_jobs).

### Example Sampling Configurations

These configuration options could be added to your `scout_apm.yml`
#### Global Sampling of 50%
```bash
sample_rate: 50
```

#### Sampling 10% of Jobs, and 50% of Web Requests
```bash
endpoint_sample_rate: 50
job_sample_rate: 10
```

#### Sampling 10% of Jobs and 50% of Web Requests, capturing all of a specified web endpoint
```bash
endpoint_sample_rate: 50
job_sample_rate: 10
sample_endpoints: "/foo/bar:100"
```


# Faq

## Heroku

Scout runs on Heroku without any special configuration. When Scout detects that an app is being served via Heroku:

* Logging is set to `STDOUT` vs. logging to a file. Log messages are prefixed with `[Scout]` for easy filtering.
* The dyno name (ex: `web.1`) is reported vs. the dyno hostname. Dyno hostnames are dynamically generated and don't have any meaningful information.

### Configuration

Scout can be configured via environment variables. This means you can use `heroku config:set` to configure the agent. For example, you can set the application name that appears in the Scout UI with:

```bash
heroku config:set SCOUT_NAME='My Heroku App'
```

See the configuration section for more information on the available config settings and environment variable functionality.

### Using the Scout Heroku Add-on

Scout is also available as a [Heroku Add-on](https://elements.heroku.com/addons/scout). The add-on automates setting the proper Heroku config variables during the provisioning process.

### Adding the Database Addon

To get more insights into how your database is performing, check out our [Database Addon](https://devcenter.heroku.com/articles/scout#database-monitoring-addon).


## Docker

Scout runs within Docker containers without any special configuration.

However, it may be easier to dockerize the core-agent. We suggest using our [Docker image for this](/docs/core-agent#with-docker).


## Transactions

### What is a transaction
A transaction is anytime that you application handles a request or runs a background job. To get a better understanding of your transaction volume, visit your [usage page](https://scoutapm.com/usage) for more info

### Ignoring Transactions
**Note**:
*When a transaction is ignored, we will not collect metric data or traces for the request. When ignoring transactions and using sampling, data may be skewed and important traces may be missed.*

There are a couple of approaches to ignore web requests and background jobs you don't care to instrument. These approaches are listed below. 

#### By the web endpoint path name 

You can ignore requests to web endpoints that match specific paths (like `/health_check`). See the `ignore` setting in the [configuration options](/docs/elixir#ignore). 

#### In your code 
To selectively ignore a web request or background job in your code, add the following within the transaction: 
```elixir 
ScoutApm.TrackedRequest.ignore() 
```


# Faq

## Heroku

Scout runs on Heroku without any special configuration. When Scout detects that an app is being served via Heroku:

* Logging is set to `STDOUT` vs. logging to a file. Log messages are prefixed with `[Scout]` for easy filtering.
* The dyno name (ex: `web.1`) is reported vs. the dyno hostname. Dyno hostnames are dynamically generated and don't have any meaningful information.

### Configuration

Scout can be configured via environment variables. This means you can use `heroku config:set` to configure the agent. For example, you can set the application name that appears in the Scout UI with:

```bash
heroku config:set SCOUT_NAME='My Heroku App'
```

See the configuration section for more information on the available config settings and environment variable functionality.

### Using the Scout Heroku Add-on

Scout is also available as a [Heroku Add-on](https://elements.heroku.com/addons/scout). The add-on automates setting the proper Heroku config variables during the provisioning process.


### Adding the Database Addon

To get more insights into how your database is performing, check out our [Database Addon](https://devcenter.heroku.com/articles/scout#database-monitoring-addon).

## Docker

Scout runs within Docker containers without any special configuration.

However, it may be easier to dockerize the core-agent. We suggest using our [Docker image for this](/docs/core-agent#with-docker).

## Transactions

### What is a transaction
A transaction is anytime that you application handles a request or runs a background job. To get a better understanding of your transaction volume, visit your [usage page](https://scoutapm.com/usage) for more info

### Ignoring Transactions

**Note**:
*When a transaction is ignored, we will not collect metric data or traces for the request. When ignoring transactions and using sampling, data may be skewed and important traces may be missed.*

If you don't want to track the current web request or background job, at any point you can call `ignore_transaction()` to ignore it:

```python
import scout_apm.api

if is_health_check():
    scout_apm.api.ignore_transaction()
```

You can use this whether the transaction was started from a built-in integration or custom instrumentation.

You can also ignore a set of URL path prefixes by configuring the `ignore` setting:

```python
Config.set(
    ignore=["/health-check/", "/admin/"],
)
```

When specifying this as an environment variable, it should be a comma-separated list:

```bash
export SCOUT_IGNORE='/health-check/,/admin/'
```

#### Sampling

We offer a few [configuration options](/docs/python/configuration#sample_rate) that allow you to sample all transactions, or use additional configuration to specify sampling rates for specific web endpoints or background jobs. This is useful to reduce overall usage or ignore select endpoints or jobs entirely. 

##### Sampling Precedence

The more specific sampling settings take precedence over boarder ones. For example, a setting like sample_endpoints="users/debug:30" would take priority. All endpoints not matching a specific prefix will use endpoint_sample_rate if set, followed by sample_rate. The global sample_rate will default to 100 (no sampling) if not changed. sample_endpoints and/or endpoint/job_sample_rate can be higher than the global rate, which would mean you'd be getting more transactions for those endpoints relative to everything else.

### Example Sampling Configurations

#### Global Sampling of 50%
```bash
export SCOUT_SAMPLE_RATE=50
```

#### Sampling 10% of Jobs, and 50% of Web Requests
```bash
export SCOUT_ENDPOINT_SAMPLE_RATE=50
export SCOUT_JOB_SAMPLE_RATE=10
```

#### Sampling 10% of Jobs and 50% of Web Requests, capturing all of a specified web endpoint
```bash
export SCOUT_ENDPOINT_SAMPLE_RATE=50
export SCOUT_JOB_SAMPLE_RATE=10
export SCOUT_SAMPLE_ENDPOINTS="/foo/bar:100"
```


# Faq

## How we collect metrics

Scout is engineered to monitor the performance of mission-critical production applications. Here's a short overview of how this happens:

* Our agent is added as an application dependency (ex: for Ruby apps, add our gem to your Gemfile).
* The agent instruments key libraries (database access, controllers, views, etc) automatically using low-overhead instrumentation.
* Every minute, the agent connects over HTTPS through a 256-bit secure, encrypted connection and sends metrics to our servers.

## Data Retention

Scout stores 30 days of metrics and seven days of transaction traces.

## Performance Overhead

Our agent is designed to run in production environments and is extensively benchmarked to ensure it performs on high-traffic applications.

Our most recent benchmarks (_lower is better_):



If your results differ, [reach out to us at support@scoutapm.com](mailto:support@scoutapm.com).

### Call Aggregation

During a transaction, the Scout agent records each database call, each external HTTP request, each rendering of a view, and several other instrumented libraries. While each individual piece of this overall trace has a tiny memory footprint, large transactions can sometimes build up thousands and thousands of them.  

To limit our agent's memory usage, we stop recording the details of every instrument after a relatively high limit. Detailed metrics and backtraces are collected for all calls up to the limit and aggregated metrics are collected for calls over the limit.

## Security

We take the security of your code metrics extremely seriously. Keeping your data secure is fundamental to our business. Scout is nearing a decade storing critical metrics and those same fundamentals are applied here:

* All data transmitted by our agent to our servers is sent as serialized JSON over SSL.
* Our UI is only served under SSL.
* When additional data is collected for slow calls (ex: SQL queries), query parameters are sanitized before sending these to our servers.
* Our infrastructure resides in an SOC2 compliant datacenter.

### Information sent to our servers

The following data is sent to our servers from the agent:

* Timing information collected from our instrumentation
* Gems used by your application
* Transaction traces, which include:
  * The URL, including query parameters, of the slow request. This can be modified to exclude query params via the <code>uri_reporting</code> configuration option.
  * IP Address of the client initiating the request
  * Sanitized SQL query statements
* Process memory and CPU usage
* Error counts

### Git Integration

Scout only needs read-only access to your repository, but Github doesn't currently allow this - they only offer read-write permissions through their OAuth API.

Our current Git security practices:

* We don't clone your repository's code; we only pull the commit history.
* The commit history is secured on our servers according to industry best practices.
* Authentication subsystems within our application ensure your commit history is never exposed to anyone outside your account.

All that said, we suggest the following:

* You are able to view backtrace information w/o the integration. It's likely possible to even write a UserScript to open the code locally in your editor or on Github.

#### Workaround for read-only Github Access

With a few extra steps, you can grant Scout read-only access. Here's how:

* Create a team in your Github organization with read-only access to the respective application repositories.
* Create a new Github user and make them a member of that team.
* Authenticate with this user.

## AutoInstruments

### What files within a Rails app does AutoInstruments attempt to instrument?

AutoInstruments applies instrumentation to file names that match `RAILS_ROOT/app/controllers/*_controller.rb`.

### Why is AutoInstruments limited to controllers?

Adding instrumentation induces a small amount of overhead to each instrumented code expression. If we added instrumentation to every line of code within a Rails app, the overhead would be too significant on a production deployment. By limiting AutoInstruments to controllers, we're striking a balance between visibility and overhead.

### What are some examples of code expressions that are instrumented?

Below are some examples of how AutoInstrumented spans appear in traces.

```ruby
# RAILS_ROOT/app/controllers/users_controller.rb
# This file will be instrumented as its name matches `app/controllers/*_controller.rb`.
class UsersController < ApplicationController

  def index
    fetch_users # <- Appears as `fetch_users` in traces.
    if rss? || xml? # <- This is broken into 2 spans within traces: (`rss?` and `xml?`)
      formatter = proc do |row| # <- The entire block will appear under "proc do |row|..."
        row.to_json
      end
      return render_xml # <- Appears as `return render_xml`
    end
  end

  private

  def fetch_users
    return unless authorized? # <- Appears as `return unless authorized?` in traces.
    source ||= params[:source].present? # <- Appears as `params[:source].present?`
    @users = User.all(limit: 10) # <- ActiveRecord queries are instrumented w/our AR instrumentation
  end
```

### Is every method call to an AutoInstrumented code expression recorded?

Prior to storing a span, our agent checks if the span's total execution time is at least 5 ms. If the time spent is under this threshold, the span is thrown away and the time is allocated to the parent span. This decreases the amount of noise that appears in traces (spans consuming < 5ms are unlikely optimization candidates) and decreases the memory usage of the agent. Only autoinstrumented spans are thrown away - spans that are explicitly instrumented are retained.

### What do charts look like when AutoInstruments is enabled?

When AutoInstruments is enabled, a large portion of controller time will shift to AutoInstruments:



This is expected.

### How much overhead does AutoInstruments add?

When AutoInstruments is enabled, you can estimate the additional overhead by inspecting your overview chart. Measure the mean `controller` time before the deploy then `controller` + `autoinstruments` after. The difference between these numbers is the additional overhead.

### How can the overhead of AutoInstruments be reduced?

By default, the Scout agent adds AutoInstruments to every controller in your Rails app. You can exclude controllers from instrumentation, which will reduce overhead via the [`autoinstruments_ignore`](/docs/ruby/configuration#autoinstruments_ignore) option. To determine which controllers should be ignored:

1. Ensure you are running version 2.6.1 of `scout_apm` or later.
2. Adjust the Scout agent log level to `DEBUG`.
3. Restart your app.
4. After about 10 minutes run the following command inside your `RAILS_ROOT`:

```bash
grep -A20 "AutoInstrument Significant Layer Histograms" log/scout_apm.log
```

For each controller file, this will display the total number of spans recorded and the ratio of significant to total spans. Look for controllers that have a large `total` and a small percentage of `significant` spans. In the output below, it makes sense to ignore `application_controller` as only 10% of those spans are significant:

```bash
[09/23/19 07:27:52 -0600 Dereks-MacBook-Pro.local (87116)] DEBUG : AutoInstrument Significant Layer Histograms: {"/Users/dlite/projects/scout/apm/app/controllers/application_controller.rb"=>
  {:total=>545, :significant=>0.1},
 "/Users/dlite/projects/scout/apm/app/controllers/apps_controller.rb"=>
  {:total=>25, :significant=>0.56},
 "/Users/dlite/projects/scout/apm/app/controllers/checkin_controller.rb"=>
  {:total=>31, :significant=>0.39},
 "/Users/dlite/projects/scout/apm/app/controllers/status_pages_controller.rb"=>
  {:total=>2, :significant=>0.5},
 "/Users/dlite/projects/scout/apm/app/controllers/errors_controller.rb"=>
  {:total=>2, :significant=>1.0},
 "/Users/dlite/projects/scout/apm/app/controllers/insights_controller.rb"=>
  {:total=>2, :significant=>1.0}}
```

Add the following to the `common: &defaults` section of the `config/scout_apm.yml` file to avoid instrumenting `application_controller.rb`:

```yaml
common: &defaults
  auto_instruments_ignore: ['application_controller']
```

## ScoutProf
ScoutProf has been deprecated and succeeded by [AutoInstruments](/docs/features/#auto-instruments). ScoutProf is no longer supported.

## Billing

### Free Trial

We offer a no risk, fully featured, free trial. Enter a credit or debit card anytime to continue using Scout APM after the end of your trial.

### Billing Date

Your first bill is 30 days after your signup date.

### Subscription Style

We offer both monthly and annual subscriptions with varying transaction levels and capabilities. Contact support@scoutapm.com for pricing options.

## Replacing New Relic

Scout is an attractive <a href="https://scoutapm.com/newrelic-alternative" target="_blank">alternative to New Relic</a> for modern dev teams. We provide a laser-focus on getting to slow custom application code fast vs. wide breadth as debugging slow custom application code is typically the most time-intensive performance optimization work.

In many cases, Scout is able to replace New Relic as-is. However, there are cases where your app has specific needs we currently don't provide. Don't fret - here's some of the more common scenarios and our suggestions for building a monitoring stack you'll love:

* __Browser Monitoring (Real User Monitoring)__ - there are a number of dedicated tools for both Real User Monitoring (RUM) and synthetic monitoring. We've [reviewed Raygun Pulse](https://scoutapm.com/blog/real-user-monitoring-with-raygun), an attractive RUM product. You can also continue to use New Relic for browser monitoring and use Scout for application monitoring.

### Talk to us about your monitoring stack

Don't hesitate to [email us](mailto:support@scoutapm.com) if you need to talk through your monitoring stack. Monitoring is something we know and love.


# Fastapi

## Installation



## Installation

Scout supports FastAPI through the Starlette instrumentation. General instructions for a FastAPI app:

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Attach the Scout middleware to your FastAPI app:

```python
from fastapi import FastAPI
from scout_apm.api import Config
from scout_apm.async_.starlette import ScoutMiddleware

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)
app = FastAPI()
app.add_middleware(ScoutMiddleware)
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` and pass an empty dictionary to `config`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.


# Fastmcp

## Installation



## Installation

Scout APM provides automatic instrumentation for FastMCP servers to track tool executions, performance metrics, and errors. FastMCP is a Python framework for building Model Context Protocol (MCP) servers that expose tools, resources, and prompts to LLM clients.

The latest `scout-apm` package supports FastMCP 2.9.0+.

**Step A**: Install the `scout-apm` package and FastMCP:

```bash
pip install scout-apm fastmcp>=2.9.0
```

**Step B**: Configure Scout and install instrumentation in your FastMCP server:

```python
from fastmcp import FastMCP
from scout_apm.api import Config
from scout_apm.fastmcp import ScoutMiddleware

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

# Create your FastMCP server
mcp = FastMCP(name="MyServer")

# Add Scout APM middleware
mcp.add_middleware(ScoutMiddleware())

# Define your tools
@mcp.tool
def my_tool(arg: str) -> str:
    """My tool description."""
    return f"Processed: {arg}"
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` and remove the call to `Config.set`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.


## What Scout Tracks

Scout automatically captures the following information from your FastMCP tools:

- **Tool executions**: Each tool call is tracked as an operation with timing and performance metrics
- **Tool metadata**: Tags, annotations, descriptions, and custom metadata from tool definitions
- **Arguments**: Tool arguments are logged (with automatic filtering of sensitive data)
- **Errors**: Exceptions are tracked with full context and stack traces

## Operation Naming

Tool executions appear in Scout APM with the operation name format: `Controller/{tool_name}`.

For example:
- Tool named `search_database` â `Controller/search_database`
- Tool named `calculate_sum` â `Controller/calculate_sum`

## Tool Metadata

Scout APM automatically captures metadata from your tool definitions:

```python
@mcp.tool(
    name="search_products",
    description="Search the product catalog",
    tags={"catalog", "search", "products"},
    annotations={
        "readOnlyHint": True,      # Tool doesn't modify data
        "idempotentHint": True,    # Safe to retry
        "openWorldHint": True,     # Interacts with external systems
        "destructiveHint": False,  # Non-destructive
    },
    meta={
        "version": "2.0",
        "author": "product-team",
    }
)
def search_products(query: str, limit: int = 10) -> list:
    """Search for products matching the query."""
    # Implementation...
```

This metadata is captured as Scout APM tags for filtering and analysis.


# Flask

> Looking for detailed tracing to support your microservices architecture? Check out our sister app, [TelemetryHub](https://telemetryhub.com/).

## Installation



## Installation

The latest `scout-apm` package supports Flask 0.10+.

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Configure Scout inside your Flask app:

```python
from scout_apm.flask import ScoutApm

# Setup a flask 'app' as normal

# Attach ScoutApm to the Flask App
ScoutApm(app)

# Scout settings
app.config["SCOUT_MONITOR"] = True
app.config["SCOUT_KEY"] = "[AVAILABLE IN THE SCOUT UI]"
app.config["SCOUT_NAME"] = "A FRIENDLY NAME FOR YOUR APP"
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` and remove the calls to `app.config`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.


## Flask SQLAlchemy 
Instrument [`flask-sqlalchemy`](https://flask-sqlalchemy.palletsprojects.com/) queries by calling `instrument_sqlalchemy()` on your `SQLAlchemy` instance: 

```python
from flask_sqlalchemy import SQLAlchemy
from scout_apm.flask.sqlalchemy import instrument_sqlalchemy

app = ... # Your Flask app 
db = SQLAlchemy(app)
instrument_sqlalchemy(db) 
```


# Git

## GitHub

When the GitHub integration is enabled, Scout annotates several areas of the UI with additional data from the app's associated Git repository.

### Traces

Scout displays the actual code from backtraces collected from [transaction traces](/docs/features/#transaction-traces) with its Github integration. The code is annotated with the `git blame` data (the author and commit date), making it easier to track down developers most familiar with bottlenecks.



### Deploys

When the GitHub integration is enabled, Scout annotates [deploys](/docs/features/#deploy-tracing) with the associated Git branch or tag along. When hovering over a deploy, a `diff` summary is displayed. This displays the changes between the selected deploy and the previous deploy.



### Configuration


The GitHub integration is an __app-specific__ integration, authenticated via OAuth. After authenticating, choose the Git repository name and branch name used for your application.



### Missing some repositories?

When configuring the GitHub integration, you may notice that only personal repositories are shown and repositories owned by organizations are missing. Your organization is likely leveraging trusted applications. See [GitHub's docs on organization-approved applications](https://github.com/blog/1941-organization-approved-applications) for instructions approving Scout. Once Scout is listed as an approved application, the org's repositories will be available within Scout.


### GitHub Integration -- Resetting

If the repo is on the organization account, and Scout is only showing your personal repositories, what you'll need to do is go to your GitHub account's settings, then go to applications:

[https://github.com/settings/applications](https://github.com/settings/applications)

Then you will need to go over Authorized OAuth Apps, and remove Scout APM.

Once you have removed us, go back to our GitHub integration page, re-enable the integration, but this time on the form make sure to check the box saying you give us access to your parent org's repositories as well

[https://scoutapm.com/docs/integrations/git#missing-some-repositories](https://scoutapm.com/docs/integrations/git#missing-some-repositories)


# Heroku

## Installation

With our native [Heroku addon](https://elements.heroku.com/addons/scout), Scout supports a seamless integration between your Heroku application and our monitoring suite.

No additional configuration is required. Just add the addon and follow your language's _setup_ docs page.

## Switching to a Direct Account from a Heroku Addon Account
If you're currently using Scout through a Heroku Addon, it's extremely simple to switch to a direct account. Just follow these steps:

1. Sign up for Scout at [https://scoutapm.com/users/sign_up](https://scoutapm.com/users/sign_up) with a different email address from your original email address on Heroku. Some email providers like Google support adding a dynamic suffix to your email address using a '+' (e.g. your_email+scout@gmail.com)
2. Change the SCOUT_KEY Heroku environment variable to the new account's Agent Key. You can find your Agent Key at [https://scoutapm.com/settings](https://scoutapm.com/settings)
3. Downgrade your Heroku addon plan to the free plan, "Chair Lift", if you need to maintain visibility to your Heroku data.

Your APM data will now be reporting into the new direct account dashboard.


# Huey

## Bottle 

General instructions for a Bottle app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Bottle config:
```python
from scout_apm.bottle import ScoutPlugin

app = bottle.default_app()
app.config.update({
    "scout.name": "YOUR_APP_NAME",
    "scout.key": "YOUR_KEY",
    "scout.monitor": True,
})

scout = ScoutPlugin()
bottle.install(scout)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `app.config.update`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## CherryPy 

Scout supports CherryPy 18.0.0+. 

General instructions for a CherryPy app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout plugin to your app:
```python
import cherrypy

from scout_apm.api import Config
from scout_apm.cherrypy import ScoutPlugin

class Views(object):
    @cherrypy.expose
    def index(self):
        return "Hi"

app = cherrypy.Application(Views(), "/")

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
)
scout_plugin = ScoutPlugin(cherrypy.engine)
scout_plugin.subscribe()
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Dash 

[Plotly Dash](https://dash.plot.ly/) is built on top of Flask. Therefore you should use the Scout Flask integration with the underlying Flask application object. For example:

```python
import dash
from scout_apm.flask import ScoutApm

app = dash.Dash("myapp")
app.config.suppress_callback_exceptions = True
flask_app = app.server

# Setup as per Flask integration
ScoutApm(flask_app)
flask_app.config["SCOUT_NAME"] = "A FRIENDLY NAME FOR YOUR APP"
```

For full instructions, see [the Flask integration](/docs/python/flask).

## Dramatiq

cout supports Dramatiq 1.0+. Add the following to instrument Dramatiq workers:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Dramatiq broker:

```python
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from scout_apm.dramatiq import ScoutMiddleware
from scout_apm.api import Config

broker = RabbitmqBroker()
broker.add_middleware(ScoutMiddleware(), before=broker.middleware[0].__class__)

 Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="Same as Web App Name",
    monitor=True,
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Falcon

Scout supports Falcon 2.0+. General instructions for a Falcon app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout middleware to your Falcon app:
```python
import falcon
from scout_apm.falcon import ScoutMiddleware

scout_middleware = ScoutMiddleware(config={
    "key": "[AVAILABLE IN THE SCOUT UI]",
    "monitor": True,
    "name": "A FRIENDLY NAME FOR YOUR APP",
})
api = falcon.API(middleware=[ScoutMiddleware()])
# Required for accessing extra per-request information
scout_middleware.set_api(api)
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and pass an empty dictionary to `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Huey 

Scout supports Huey 2.0+. 

Add the following to instrument your Huey application:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** If you are using [Huey's Django integration](https://huey.readthedocs.io/en/latest/django.html), you only need to set up the [Django integration](/docs/python/django). Your Huey instance will be automatically instrumented.


If you're using Huey outside of the [Django integration](/docs/python/django), add Scout to your Huey instance:

```python
from huey import SqliteHuey
from scout_apm.api import Config
from scout_apm.huey import attach_scout

broker = SqliteHuey()

 Config.set(
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
    key="[AVAILABLE IN THE SCOUT UI]",
)
attach_scout(huey)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set()`.


[If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via](/docs/python/django) [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Hug 

Scout supports Hug 2.5.1+. Hug is based on Falcon so a Falcon version supported by [our integration](/docs/python/other-libraries#falcon) is also needed. 

General instructions for a Hug app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout inside your Hug app:

```python
from scout_apm.hug import integrate_scout

# Setup your Hug endpoints as usual

@hug.get("/")
def home():
    return "Welcome home."

# Integrate scout with the Hug application for this module
integrate_scout(
    __name__,
    config={
        "key": "[AVAILABLE IN THE SCOUT UI]",
        "monitor": True,
        "name": "A FRIENDLY NAME FOR YOUR APP",
    },
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the entries in `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Nameko 

General instructions for a Nameko app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure scout once in the root of your app, and add a `ScoutReporter` to each Nameko service:

```python
from scout_apm.api import Config
from scout_apm.nameko import ScoutReporter


Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

class Service(object):
    name = "myservice"

    scout = ScoutReporter()

    @http("GET", "/")
    def home(self, request):
        return "Welcome home."
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Pyramid 

General instructions for a Pyramid app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Pyramid config:

```python
import scout_apm.pyramid

if __name__ == "__main__":
    with Configurator() as config:
        config.add_settings(
            SCOUT_KEY="[AVAILABLE IN THE SCOUT UI]",
            SCOUT_MONITOR=True,
            SCOUT_NAME="A FRIENDLY NAME FOR YOUR APP"
        )
        config.include("scout_apm.pyramid")

        # Rest of your config...
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `config.add_settings`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## RQ

Scout supports RQ 1.0+. 

Do the following to instrument your RQ jobs:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Use the Scout RQ worker class.

If you're using RQ directly, you can pass the `--worker-class` argument the worker command:

```bash
rq worker --job-class scout_apm.rq.Worker myqueue
```

If you're using the [RQ Heroku pattern](https://python-rq.org/patterns/), you can change your code to use the `scout_apm.rq.HerokuWorker` class:

```python
from scout_apm.rq import HerokuWorker as Worker
```

If you're using Django-RQ, instead use the [custom worker setting](https://github.com/rq/django-rq#custom-job-and-worker-classes) to point to our custom Worker class:
```python
RQ = {
    "WORKER_CLASS": "scout_apm.rq.Worker",
}
```
If you're using your own `Worker` sub class already, you can subclass our `Worker` class:
```python
from scout_apm.rq import Worker

class MyWorker(Worker):
    # your custom behaviour here
    pass
```
Or if you're combining one or more other `Worker` classes, you can add our mixin class `scout_apm.rq.WorkerMixin`:
```python
from some.other.rq.extension import CustomWorker
from scout_apm.rq import WorkerMixin

class MyWorker(WorkerMixin, CustomWorker):
    pass
```
**3.** Configure Scout.

If you're using Django-RQ, ensure you have the [Django integration](/docs/python/django) installed, and this is handled for you.

If you're using RQ directly, create a [config file](https://python-rq.org/docs/workers/#using-a-config-file) for it that runs the Scout API's `Config.set()`:
```python
from scout_apm.api import Config
  
Config.set(
    key="YOUR_SCOUT_KEY",
    name="Same as Web App Name",
    monitor=True,
)
```
Pass the config file to `-c` argument to the worker command, as per [the documentation](https://python-rq.org/docs/workers/#using-a-config-file).

If you wish to configure Scout via environment variables, you don't need a config file. Set `SCOUT_KEY`, `SCOUT_NAME` and `SCOUT_MONITOR` instead.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**4.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Starlette 

Scout supports Starlette 0.12+. General instructions for a Starlette app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout and attach its middleware to your Starlette app:
```python
from scout_apm.api import Config
from scout_apm.async_.starlette import ScoutMiddleware
from starlette.applications import Starlette
from starlette.middleware import Middleware

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

middleware = [
 # Should be *first* in your stack, so it's the outermost and can
 # track all requests
 Middleware(ScoutMiddleware),
]

app = Starlette(middleware=middleware)
```
If you're using Starlette <0.13, which [refactored the middleware API](https://github.com/encode/starlette/pull/704), instead use `app.add_middleware(ScoutMiddleware)`. Make sure it's the last call to `add_middleware()` so that Scout is the outermost middleware.

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.


# In-depth

Before reading this section, we suggest going through our [advanced features](/docs/ruby/features) page which contains documentation on adding features that may not be automatically added -- including [Deploy Tracking](/docs/ruby/features#deploy-tracking), [Request Queueing](/docs/ruby/features#request-queueing), [Auto Instruments](/docs/ruby/features#auto-instruments) and [Custom Context](/docs/ruby/features#custom-context)


## Request Policies
By default the way that we choose which traces to collect involves a factor of 4 things:

1. Throughput through the endpoint
2. Deviation from mean response of that endpoint (for example, if the average response time is usually 100ms but this request took 500ms it's interesting)
3. Total response time
4. Time since last seen (this ensures we capture endpoints that don't have as much throughput through it)

https://github.com/scoutapp/scout_apm_ruby/tree/master/lib/scout_apm/slow_policy

In `4.0.0` we added the ability to add custom request policies. 

For example, let says you were doing some testing and wanted to report more traces for an endpoint that had changes made to it. You can add a custom request policy for this:

```ruby
# config/initializers/scout_custom_policy.rb

# values should be between 0 - 5. The max value of the percentile policy for example is 1.7
require 'scout_apm'
class AddPolicy < ScoutApm::SlowPolicy::Policy
  ENDPOINT_SCORES = { "Controller/users/index" => 2}
  # BACKGROUND_SCORES = { "Job/mailers/DigestEmail::DeliverJob" => 2}

  # Called for every tracked request (both web requests and background jobs), giving a score, to be compared with other requests of 
  # that minute to find the best traces to store details.
  def call(req)
    ENDPOINT_SCORES.fetch(req.unique_name, 0)
    
    # or for background jobs
    # BACKGROUND_SCORES.fetch(req.unique_name, 0)
  end

  # Called when a request actually gets stored as a detailed trace
  def stored!(req)
  end
end

ScoutApm::Agent.instance.context.slow_request_policy.add(AddPolicy.new(ScoutApm::Agent.instance.context)))
```

The best way to find the endpoint slug (`Controller/users/index`) is to find the endpoint name you want to capture more traces for on the endpoints page:
For Scout we are app 6, you will need to replace the app id with yours.
https://scoutapm.com/apps/6/endpoints

Then once on the endpoints page you want to capture more traces for, grab the url (for example):
https://scoutapm.com/apps/6/endpoints/YXBpL21ldHJpY3Mvc2hvdw== 

And take the base64 part at the end (`YXBpL21ldHJpY3Mvc2hvdw==`) and decode it (`api/metrics/show`) and prepend `Controller/` to it. Case does matter here: `Controller/api/metrics/show`
This will be the endpoint that you place in `ENDPOINT_SCORES` above.

This same method can be used for background jobs as well, but instead of `Controller/` it is `Job/`

## Plugins

In `2.4.11` we added the ability for transaction and periodic callbacks. 

This can be useful if you want to get additional insights into queue_time for example.

To add a transaction callback (a callback that occurs for every web request and background job):
`ScoutApm::Extensions::Config.add_transaction_callback(klass.new)`

To add a periodic callback (a callback that happens after every minute before the payload is sent):
`ScoutApm::Extensions::Config.add_periodic_callback(klass.new)`

The transaction callback will take a single param of the `payload`, while the period callback takes two params of `reporting_periods_payload`, and `metadata`

Example of logging each transaction's queue_time, duration, and transaction name:

```ruby
class LogQueueTimeCallack
  def call(payload)
    Rails.logger.info(
      msg: "ScoutApm Transaction",
      queue_time: payload.queue_time_ms,
      duration: payload.duration_ms,
      transaction_name: payload.transaction_name
    ) if payload.transaction_type_slug == "web"
  end
end
ScoutApm::Extensions::Config.add_transaction_callback(LogQueueTimeCallack.new)
```


# Index

## Scout Help Docs

Welcome to the help site for __[Scout Application Monitoring](https://scoutapm.com)__. Don't have an account? [Get started](https://scoutapm.com/info/pricing).

Browse through the sidebar, search, [email us](mailto:support@scoutapm.com), or join our [Discord](https://discord.gg/keGzRHD3pv)</a>. We're here to help.



## Overview

Scout Application Monitoring is a lightweight, production-grade application monitoring service built for modern development teams. Just embed our agent in your application: we handle the rest. 

Here's an overview of the key functionality in our application monitoring service:

### Agents

We support Ruby, Python, PHP, and Elixir apps.

Our agent is designed to run in production environments and has low overhead. Every minute, the agent transmits metrics to our service over SSL. 

There's nothing to install on your servers.

### User Interface

A complete overview of the Scout UX is available in the [features](/docs/features) area of this help site.


# Insights

Scout automatically surfaces your new n+1, slow query and memory bloat insights.

## N+1

An N+1 query is a database query pattern where N individual queries are executed to retrieve related data, as opposed to a single query, resulting in a total of N+1 queries. 

Scout analyzes your traces and shows you the trace that we have found to contain N+1s that have an impact on the user's experience:



## Memory Bloat

If a user triggers a request to your Rails application that results in a large number of object allocations (example: loading a large number of ActiveRecord objects), your app may require additional memory. The additional memory required to load the objects in memory is released back very slowly. Therefore, a single memory-hungry request will have a long-term impact on your Rails app's memory usage.

There are 3 specific features of Scout to aid in fixing memory bloat.

The Insights area of the dashboard identifies controller-actions and background jobs that have triggered significant memory increases. An overview of the object allocation breakdown by tier (ActiveRecord, ActionView, etc) is displayed on the dashboard.



## Slow Query Insights





This insight analyzes your queries in three dimensions, helping you focus on database optimizations that will most improve your app:

1. __Which queries are most impacting app performance?__ This is based on the total time consumed of each query, where time consumed is the average query latency multiplied by the query throughput.
2. __Which queries are significant bottlenecks inside web endpoints and background jobs?__ A single query that is responsible for a large percentage of the time spent in a transaction is a great place to investigate for a performance win.
3. __Which queries are consistently slow?__ These are queries that have a high average latency.

## History
In addition to the memory bloat insights, you will be able to view past memory bloat, slow query (if enabled), and N+1 insights. These insights will have a saved trace with them, and these trace have a longer retention period than our normal traces do.


# Integrations

Scout integrates with many popular 3rd party platforms and applications, such as GitHub, Slack, Sentry, and more. See our list below:

## Git


## Alerting

## Error Monitoring

## SSO


# Laravel

## Laravel 

Scout supports Laravel 5.5+.

**1.** Install the `scoutapp/scout-apm-laravel` package:

```bash
composer require scoutapp/scout-apm-laravel
```

Note that the `scout-apm-php` package will automatically be included. It does not need to be installed directly.

**2.** Install the `scoutapm` php extension (optional, recommended):
```bash
sudo pecl install scoutapm
```
Several instruments require the native extension to be included, including timing of `libcurl` and `file_get_contents`. For more information, or to compile manually, the [README](https://github.com/scoutapp/scout-apm-php-ext) has additional instructions.

**3.** Configure Scout in your `.env` file:

```bash
# Scout settings
SCOUT_MONITOR=true
SCOUT_KEY="[AVAILABLE IN THE SCOUT UI]"
SCOUT_NAME="A FRIENDLY NAME FOR YOUR APP"
```

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**4.** Add the config/scout_apm.php
```bash
php artisan vendor:publish --provider="Scoutapm\Laravel\Providers\ScoutApmServiceProvider"
```

**5.** Clear and re-cache your config: 
```bash
php artisan config:cache
```

**6.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

### Code Based Configuration

If for any reason you can't use environment based configuration, or it'd simply be easier to manage Scout in code, you can configure Scout with a Laravel config file. First ensure you have the `config/scout_apm.php` file created in step 4 above:

```bash
php artisan vendor:publish --provider="Scoutapm\Laravel\Providers\ScoutApmServiceProvider"
```

Then add any keys you want to override to the bottom of the file, following the template. The keys should be in lower case, with no prefixed `SCOUT_`. Any keys not mentioned will continue to be read from the environment.

```php
$config['name'] = 'Overriden Name';
```

Finally, deploy and remember update any cached configs.

### Middleware

Scout automatically inserts its middleware into your application on Laravel startup. It adds one at the very start of the middleware stack, and one at the end, allowing it to profile your middleware and controllers.

## Vapor
Scout will work in Vapor (serverless) environment in the same way it does a persistent environment. No additional configuration is needed other than following the steps above

### Caveats
For low throughput applications, when the execution environment freezes, the core agent (which aggregates requests for a minute then sends them to our servers) won't be able to send the payloads. During the next thawing, the core-agent will send the payloads it has had for previous times. This can lead to delays in ingestion time

Further, we have a 10 minute checkin window where we accept payloads. If the next invocation of the enivornment (thawing) occurs after 10 minutes, we won't ingest the previous payload


# Log-management

Scout's Log Management feature allows you to monitor, search, and analyze your Ruby application logs directly within the Scout UI. By integrating with our existing APM agent, we provide enhanced context and filtering capabilities.

## Installation



```ruby
gem 'scout_apm_logging'
```



```yaml
common: &defaults

     # ... other Scout APM settings

     logs_monitor: true
     logs_ingest_key: aaaa-1111-aaaa-1111 # Provided in App Logs Page
```



It takes approximately five minutes for your data to first appear within the Scout UI.


## Installation

**A** Add the `scout_apm_logging` gem to your gemfile.

```ruby
gem 'scout_apm_logging'
```

**B** Configure Scout in your `scout_apm.yml` configuration file:

```yaml
common: &defaults

     # ... other Scout APM settings

     logs_monitor: true
     logs_ingest_key: aaaa-1111-aaaa-1111 # Provided in App Logs Page
```

**C** Deploy!

It takes approximately five minutes for your data to first appear within the Scout UI.


## Configuration Options

The following configuration settings are available. These can be set in the `scout_apm.yml` configuration file or as environment variables with the `SCOUT_` prefix, e.g. `SCOUT_LOGS_INGEST_KEY`.

Only `logs_ingest_key` is required. The rest are optional.

Setting Name | Description | Default | Required
--- | --- | --- | ---
logs_ingest_key | The Ingest Key to use for logs | | Yes
logs_monitor | True or false. If true, monitor logs and send them to Scout | `false` | No
logs_capture_level | The minimum log level to capture and send to Scout | `debug` | No
log_level | Log level for the agent itself | `info` | No

## Advanced Configuration

These settings are internal and are not typically needed for normal operation, but if things like filesystem access cause issues, the following may be useful.

Setting Name | Description | Default | Required
--- | --- | --- | ---
logs_proxy_log_dir | The directory to store logs in for monitoring | `nil` | No
logs_capture_call_stack | True or false. If true, capture the call stack for each log message | `false` | No
logs_capture_log_line | True or false. If true, capture the log line for each log message | `false` | No
logs_call_stack_search_depth | The number of frames to search in the call stack | `10` | No
logs_call_stack_capture_depth | The number of frames to capture in the call stack | `10` | No
logs_method_missing_warning | True or false. If true, log a warning when `method_missing` is called | `false` | No
logs_method_missing_call_stack | True or false. If true, capture the call stack when `method_missing` is called | `false` | No
logs_config | A hash of configuration options for merging into the collector's config | `{}` | No
logs_reporting_endpoint | The endpoint to send logs to | `https://logs.scoutapm.com` | No
log_stdout | True or false. If true, log to STDOUT | `false` | No
log_stderr | True or false. If true, log to STDERR | `false` | No
log_file_path | Either a directory or `"STDOUT"` | `nil` | No
log_class | The underlying class to use for logging. Defaults to Ruby's Logger class | `Logger` | No

## How It Works

For Rails applications, if you are using 7.1+ we will add a custom logger, which has a formatter that utilizes the [OpenTelemetry Ruby SDK](https://github.com/open-telemetry/opentelemetry-ruby) to send logs to us, to the broadcast logger. For Rails applications before 7.1, we will use this same custom logger but we will also create a proxy logger which we will swap out for all instances of the old logger, and this proxy logger will log to the old logger as well as the custom one.

The logs will be available in the Scout UI for you to search and filter. We will automatically set a custom log formatter to include additional context in the logs sent to us. Your original logs will not be altered.

## Default Attributes

The Scout Logs agent enriches Rails logs with a few attributes by default:

- **entrypoint**: The top-level action (e.g. Controller class, in Rails) that the log was generated from.
- **location**: The file and line number where the log was generated.

In addition, it will capture all key-value pairs from any [Custom Context](/docs/ruby/features/#custom-context) that you have set. **This means logs can be filtered by any Custom Context attributes**.

## Data Retention

Scout retains your log data for 14 days. If you require longer-term storage, please let us know as we would like to create options for our customers, but at this point you will need to also send them to an alternative location.


# Log-management

## Installation

Our logging solution aims to "just work" with Rails, Python, and Elixir applications.

Each App can have logs enabled individually and requires a unique Ingest Key. Visit the Logs page from an App in the Scout UI to get started.




## Installation

### Ruby/Rails

**For a Rails Application**

**A** Add the `scout_apm_logging` gem to your gemfile.

**B** Configure Scout in your `scout_apm.yml` configuration file:

```yaml
common: &defaults

     # ... other Scout APM settings

     logs_monitor: true
     logs_ingest_key: aaaa-1111-aaaa-1111 # Provided in App Logs Page
```

**C** Deploy!

Further [configuration options](/docs/ruby/log-management) are available, but the above is the minimum required to get started.

### Python

**For a Python Application**

**A** Install the [Scout Python logging](https://pypi.org/project/scout-apm-logging/) package:

```bash
pip install scout-apm-logging
```

**B** Set `SCOUT_LOGS_INGEST_KEY` in your existing configuration or via an environment variable. This key is provided in the Logs page of the enabled App.

**C** Add the Scout logging handler to your [Python logging configuration](https://docs.python.org/3/library/logging.config.html). Here's an example using dictConfig:

```python
import os
from logging.config import dictConfig
from scout_apm_logging import ScoutOtelHandler

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "scout": {
            "level": "DEBUG",
            "class": "scout_apm_logging.ScoutOtelHandler",
            "service_name": "your-python-app",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {  # Root logger
            "handlers": ["console", "scout"],
            "level": "DEBUG",
        },
    },
}

# Apply the logging configuration
dictConfig(LOGGING_CONFIG)
```

This configuration attaches the `ScoutOtelHandler` to the root logger with the `DEBUG` log level, which will send all logs from internal libraries to Scout. Python logging is highly configurable, and we provide some [common configurations](/docs/python/log-management) to get you started.

### Elixir

**For an Elixir Application**

Log management is built into the Scout APM Elixir agent (v2.0+). It integrates with Elixir's built-in Logger.

**A** If you haven't already, add `scout_apm` to your `mix.exs`:

```elixir
{:scout_apm, "~> 2.0"}
```

**B** Enable log management in your config and provide your ingest key (available in the Logs page of your Scout app):

```elixir
config :scout_apm,
  logs_enabled: true,
  logs_ingest_key: "your-logs-ingest-key"
```

**C** Attach the log handler in your `Application.start/2`:

```elixir
def start(_type, _args) do
  ScoutApm.Logging.attach()
  # ... rest of supervision tree
end
```

**D** Deploy!

Logs within Scout-tracked requests are automatically enriched with request context. See the [Elixir features docs](/docs/elixir/features#log-management) for further configuration options.


## Overview

Scout's Log Management is designed with ease-of-use as a top priority. Sending logs to us and viewing them in the UI should be as simple as possible. By working with our existing agents, we can also gather more context and automatically apply it to your application logs. This gives you extra power to filter and search through your logs, and to correlate them with other performance data. Some highlights:

- Filter logs by entrypoint (i.e. Controller originating the activity)
- Filter logs by [Custom Context](/docs/features/#context) (attributes - anything you have added to the Scout APM agent)
- Fast in-memory exploration



## Functionality

Visiting the Logs page will begin loading the log records that we have received according to the timeframe you have selected, e.g. âPast 3 hours.â Logs will load from most-recent to oldest. We load 10K records initially, more can be loaded as needed. As the logs load, you can rapidly filter to desired Severity Levels and search/filter via regex applied to the message body and attributes. The time window can also be narrowed via horizontal selection (âbrushâ) on the chart. These filters apply to logs that are already loaded into the browser.

When you determine interesting lines, you can also use the pre-load filters to screen logs closer to the log storage layer, allowing you to scan longer timeframes without pulling too many records into the browser. This two-phase approach can be a powerful and flexible way to efficiently seek through a very large corpus of log records. We hope you love it!

## Filtering

### Pre-Load Filters

The Logs Filtering allows you to limit the logs that are loaded into the Logs View. These filters are applied to the logs in our storage system before loading them into the application. Filtering by time can especially reduce the amount of data processed and returned by our application. Keep in mind that rapid filtering and manipulation can be further performed within the Logs Table after the Logs have been loaded.

Logs can be filtered by:

- **Date and Time**: Using the Scout time selector, as usual.
- **Message Content**: A simple CONTAINS filter is available.
- **Attributes**: Values of any attributes that are present in the logs can be used to filter.

For Attribute filters, you will need to select the attribute key and then provide a value to filter by. We populate the selection with all the attributes of the logs we've loaded so far. See the below gif for adding the 'org_id' [custom context](/features/#context) we have added to our application as a filter.

After changing any of these filters, hitting "Load" will discard the current in-memory logs and begin loading
new data matching the filter criteria.



#### Default Attributes

The Scout Logs agent enriches Rails logs with a few attributes by default:

- **entrypoint**: The top-level action (e.g. Controller class, in Rails) that the log was generated from.
- **location**: The file and line number where the log was generated.

In addition, it will capture all key-value pairs from any [Custom Context](/ruby/features/#custom-context) that you have set. **This means logs can be filtered by any Custom Context attributes**.

### Logs List

As records are loading, the Logs List allows you to filter your log data in straightforward ways. These filters also determine the data sent to the rest of the statistics and charts on the screen, allowing you to focus on the most relevant Logs for any given visualization.

#### Severity Filter

Select any combination of severity levels to filter the logs.

#### Entrypoint Filter

The entrypoint filter allows you to filter logs pertaining to specific endpoints or background jobs. 

#### Regex Filter

The Regex Filter allows you to filter the Logs List using regex that evaluates against message content as well as log Attributes (both keys and values). We hope it lets you quickly narrow things down, whatever you might want to narrow by.


#### Loading Controls

At the top of the Logs List are a few controls that allow you to manage the loading of data into the Logs List. These controls are useful for managing the amount of data that is loaded into the Logs List at any given time.

- **Progress Info**: This section indicates the amount of data that has been returned vs scanned.
- **Loading Bar**: This bar indicates the progress of the data being loaded. You can hover over to get an approximate numerical value.
- **Pause/Resume**: These buttons allow you to pause and resume the loading of data. This is useful if you want to stop the loading of data to inspect the data that has already been loaded or if you don't want to load the default 10K Logs per load.
- **Full Screen**: This button allows you to expand the Logs List to full screen mode.

## Usage & Billing

Usage can be broken out into two categories. Write usage and read usage. Write usage is the total bytes of uncompressed data sent to our servers in OTLP format. Read usage is the number of bytes of total uncompressed data that we traversed when performing an operation.

To view your usage, click the cog in the bottom left, which will display a list of options to choose from. Within this list click "View Logs Usage". Here, you will have 14 days of both write and read usage streamed in.



For detailed configuration options and advanced setup instructions, see:

- [Ruby Log Management Setup](/docs/ruby/log-management)
- [Python Log Management Setup](/docs/python/log-management)
- [Elixir Log Management Setup](/docs/elixir/features#log-management)

## FAQ

### How does this work?

For Rails applications, if you are using 7.1+ we will add a custom logger, which has a formatter that utilizes the [OpenTelemetry Ruby SDK](https://github.com/open-telemetry/opentelemetry-ruby) to send logs to us, to the broadcast logger. For Rails applications before 7.1, we will use this same custom logger but we will also create a proxy logger which we will swap out for all instances of the old logger, and this proxy logger will log to the old logger as well as the custom one.

For Python applications, we provide a custom logging handler which wraps the [OpenTelemetry Python SDK](https://github.com/open-telemetry/opentelemetry-python). This handler integrates with your existing logging setup, and sends logs directly to Scout without requiring the Otel Collector to be installed separately.

For Elixir applications, a custom Logger handler is attached that captures log messages, enriches them with Scout APM context (request ID, transaction name, custom tags), and sends them to Scout via OTLP. Your existing Logger configuration is not modified.

The logs will be available in the Scout UI for you to search and filter. For Rails, we will automatically set a custom log formatter to include additional context in the logs sent to us. Your original logs will not be altered.
The [Ruby](https://github.com/scoutapp/scout_apm_ruby_logging), [Python](https://github.com/scoutapp/scout_apm_python_logging), and [Elixir](https://github.com/scoutapp/scout_apm_elixir) agents are open source and available on Github.

### What is the retention period on this log data?

Scout retains your log data for 14 days. If you require longer-term storage, please let us know as we would like to create options for our customers, but at this point you will need to also send them to an alternative location.

<!--
### What about PII?

Scout proactively scrubs some very obvious leaks (e.g. strings after username or password). If you need additional protection, we can offer you additional services to mitigate your risk. Please contact [support@scoutapm.com](mailto:support@scoutapm.com).
-->


# Log-management

Scout's Log Management feature allows you to monitor, search, and analyze your Python application logs directly within the Scout UI. By integrating with our existing APM agent, we provide enhanced context and filtering capabilities.

## Installation



```bash
pip install scout-apm-logging
```





```python
import os
from logging.config import dictConfig
from scout_apm_logging import ScoutOtelHandler

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "scout": {
            "level": "DEBUG",
            "class": "scout_apm_logging.ScoutOtelHandler",
            "service_name": "your-python-app",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {  # Root logger
            "handlers": ["console", "scout"],
            "level": "DEBUG",
        },
    },
}

# Apply the logging configuration
dictConfig(LOGGING_CONFIG)
```

This configuration attaches the `ScoutOtelHandler` to the root logger with the `DEBUG` log level, which will send all logs from internal libraries to Scout. Python logging is highly configurable, and we provide some common configurations below to get you started.


## Installation

**A** Install the [Scout Python logging](https://pypi.org/project/scout-apm-logging/) package:

```bash
pip install scout-apm-logging
```

**B** Set `SCOUT_LOGS_INGEST_KEY` in your existing configuration or via an environment variable. This key is provided in the Logs page of the enabled App.

**C** Add the Scout logging handler to your [Python logging configuration](https://docs.python.org/3/library/logging.config.html). Here's an example using dictConfig:

```python
import os
from logging.config import dictConfig
from scout_apm_logging import ScoutOtelHandler

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "scout": {
            "level": "DEBUG",
            "class": "scout_apm_logging.ScoutOtelHandler",
            "service_name": "your-python-app",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {  # Root logger
            "handlers": ["console", "scout"],
            "level": "DEBUG",
        },
    },
}

# Apply the logging configuration
dictConfig(LOGGING_CONFIG)
```

This configuration attaches the `ScoutOtelHandler` to the root logger with the `DEBUG` log level, which will send all logs from internal libraries to Scout. Python logging is highly configurable, and we provide some common configurations below to get you started.


## Common Configurations

By default, attaching the ScoutOtelHandler to the root logger with the DEBUG level will send all logs from internal libraries to Scout. While useful for comprehensive monitoring, this can result in a very large volume of logs, and likely more noise than signal.

Since the Python Logging agent provides a logging Handler, the source and severity of logs sent to Scout is configured via Python logging configuration.

There are many other possible logging configurations, but we hope these examples provide a useful starting point for some common needs.

### Just Your App

This is a logging configuration which only attaches the "scout" handler to a custom logger: `your_app`

```python
from logging.config import dictConfig
from scout_apm_logging import ScoutOtelHandler

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "scout": {
            "level": "DEBUG",
            "class": "scout_apm_logging.ScoutOtelHandler",
            "service_name": "your-service-name",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "your_app": {
            "handlers": ["scout"],
            "level": "DEBUG",
            "propagate": True  # True by default
        },
    },
    "root": {
        "level": "WARNING",
        "handlers": ["console"],
    },
}

dictConfig(LOGGING_CONFIG)
```

#### Key Points
1. The `root` logger is set to `WARNING` level and only uses the console handler, effectively excluding other libraries' logs from Scout.
2. Propagation means that all logs will also be handled by the root handlers, so in this case: output to the console.
3. Adding the `scout` handler to the root would mean that `WARNING` or `ERROR` logs from all libraries would send to Scout. In this case, you could add the console handler to `your_app` and set `propagate` to `False` to not double-report.

### Excluding Specific Libraries

Maybe you're okay with getting most logs from various libraries, but want to reduce noise from especially verbose libraries.

```python
### Initial configuration the same as above
...
    "loggers": {
        "your_app": {
            "handlers": ["console", "scout"],
            "level": "DEBUG",
        },
        "urllib3": {
            "level": "WARNING",
        },
        "boto3": {
            "level": "WARNING",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "scout"],
    },
}
```

#### Key Points:
1. Explicitly configuring loggers for known libraries (like urllib3 and boto3 in the example) gives you fine-grained control over their log levels.
2. Libraries that are not explicitly configured will inherit from the root logger, which is set to INFO level in this example.

Your application's logger is set to DEBUG level, ensuring you capture all necessary details from your own code.

This configuration allows you to:

- capture detailed logs from your application
- reduce noise from verbose libraries by setting their levels higher
- catch logs from unconfigured libraries at the info level

## How It Works

For Python applications, we provide a custom logging handler which wraps the [OpenTelemetry Python SDK](https://github.com/open-telemetry/opentelemetry-python). This handler integrates with your existing logging setup, and sends logs directly to Scout without requiring the Otel Collector to be installed separately.

The logs will be available in the Scout UI for you to search and filter.

## Data Retention

Scout retains your log data for 14 days. If you require longer-term storage, please let us know as we would like to create options for our customers, but at this point you will need to also send them to an alternative location.


# Logging

## Logging

Scout logs internal activity via a configured `Psr\Log\LoggerInterface`. The
Laravel instruments automatically wire up the framework's logger to the
agent's logging.

If required, you can override this by changing the container service `log`.

Scout's logging defaults to the same log level as the LoggerInterface provided,
but that can be set to a stricter level to quiet the agent's logging via the
`log_level` configuration. The underlying LoggerInterface's level will take
precedence if it is tighter than the `log_level` configuration.

### Log Levels

The possible log levels are as follows:
* `DEBUG`
* `INFO`
* `NOTICE`
* `ERROR`
* `CRITICAL`
* `ALERT`
* `EMERGENCY`

### Debug Logs

To set Scout's log level to debug, set the [log_level](/docs/php/configuration#log_level) configuration to `debug`.

Scout's log level defaults to the same log level as the LoggerInterface provided, if you aren't seeing debug log levels from Scout, you will need to lower your LoggerInterface's log level as well.


# Logging

## Logging

Scout logs internal activity via a configured logging function with the signature `(msg: string, level: LogLevel) => void`.

### Express middleware logging

To enable agent logging with the `express` middleware, your middleware should be set up like the following:

```javascript
const scout = require("@scout_apm/scout-apm");
const express = require("express");

// The "main" function of your application
async function start() {
  // Create your express application
  const app = express();

  // Install scout
  await scout.install(
    // Configuration for the scout agent
    {
      allowShutdown: true, // allow shutting down spawned scout-agent processes from this program
      monitor: true, // enable monitoring
      name: "<application name>",
      key: "<scout key>",
    },
    // Additional scout options
    {
      logFn: scout.consoleLogFn,
    }
  );

  // Enable the app-wide scout middleware
  app.use(scout.expressMiddleware());

  // ... Add other middleware/handlers ...

  app.listen(...);
}
```

If you are using [`winston`](https://www.npmjs.com/package/winston) you may build a `logFn` by passing a `winston.Logger` to the exported `scout.buildWinstonLogger` helper function:

```javascript
  logFn: scout.buildWinstonLogger(yourLogger),
```

If a `winston.Logger` instance is provided, Scout's logging defaults to the same log level as the instance, otherwise it defaults to `ERROR`. You may set the logging to a stricter level to quiet the agent's logging via the `logLevel` in the `config` sub-object (or `SCOUT_LOG_LEVEL` via ENV). The underlying LoggerInterface's level will take precedence if it is tighter than the `logLevel` configuration.

### Log Levels

The possible log levels are as follows:
* `DEBUG`
* `INFO`
* `WARN`
* `ERROR`


# Logging

> 
This page is about the Ruby agent's internal logging, if you're interested in Scout's Managed Logs for Ruby applications, you'll find that [over here](/docs/features/log-management). 

## Logs
The Ruby agent writes all of its logs to the `log/scout_apm.log` file. By default, our logging is set to `info` level logging. However, this can be tightened or loosened in the [configuration](/docs/ruby/configuration#log_level) using the `log_level` variable in the `config/scout_apm.yml` file, or via environment variable -- SCOUT_LOG_LEVEL.

### Heroku

To view Scout logs on Heroku, use: `heroku logs --tail -a your_app_name | grep [Scout]`

### Log Levels

The possible log levels are as follows:
* `DEBUG`
* `INFO`
* `WARN`
* `ERROR`
* `FATAL`


# Logging

By default, the elixir log level is set to `info`. The log level can be increase or lowered using the [log_level](/docs/elixir/configuration#log_level) variable

### Log Levels

The possible log levels are as follows:
* `DEBUG`
* `INFO`
* `WARN`
* `ERROR`

### Debug Logs

Increase the log level of `scout_apm` by setting `log_level: "debug"` in your `config/scout_apm.exs` file and restart your app.


# Logging

> 
This page is about the Python agent's internal logging, if you're interested in Scout's Managed Logs for Python applications, you'll find that [over here](/docs/features/log-management). 

## Logging

Scout logs via the built-in Python logger, which means you can add a handler to the `scout_apm` package. If you don't setup logging, use the examples below as a starting point.

In situations where you have a handler attached to the Root Logger that is catching all
logs at `DEBUG` level (perhaps set via `basicConfig`), you may want to attach a separate handler to the `scout_apm`
logger at a _higher_ level to keep it from filling up your logs with debug messages.

### Log Levels

The following log levels are available:

* CRITICAL
* ERROR
* WARNING
* INFO
* DEBUG

### Django Logging

To log Scout agent output in your Django application, copy the following into your `settings.py` file:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stdout': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z',
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'stdout',
        },
        'scout_apm': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'scout_apm_debug.log',
        },
    },
    'root': {
        'handlers': ['stdout'],
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
    },
    'loggers': {
        'scout_apm': {
            'handlers': ['scout_apm'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### Flask Logging

Add the following your Flask app:

```python
dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stdout': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z',
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'stdout',
        },
        'scout_apm': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'scout_apm_debug.log',
        },
    },
    'root': {
        'handlers': ['stdout'],
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
    },
    'loggers': {
        'scout_apm': {
            'handlers': ['scout_apm'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
})
```

If `LOGGING` is already defined, merge the above into the existing Dictionary.

### Celery Logging

Add the following to our default Celery configuration:

```python
import logging
logging.basicConfig(level='DEBUG')
```

### Custom Instrumentation logging

If you've [custom Scout instrumentation](/docs/python/features/#custom-instrumentation), add the following to record the agent logs:

```python
import logging
logging.basicConfig(level='DEBUG')
```


# Lumen

## Lumen 

Scout supports Lumen 5.5+.

### Installing the package
**1.** Install the `scoutapp/scout-apm-lumen` package:

`composer require scoutapp/scout-apm-lumen`

Note that the `scout-apm-php` package will automatically be included. It does not need to be installed directly.

**2.** Adding the service provider:

Add the ScoutApmServiceProvider to your bootstrap/app.php, for example:

```php
// $app->register(App\Providers\AppServiceProvider::class);
// $app->register(App\Providers\AuthServiceProvider::class);
// $app->register(App\Providers\EventServiceProvider::class);
$app->register(\Scoutapm\Laravel\Providers\ScoutApmServiceProvider::class);
```

Add the four middleware to your bootstrap/app.php, for example:

```php
$app->middleware([
    // These three should be as early as possible in the pipeline:
    \Scoutapm\Laravel\Middleware\SendRequestToScout::class,
    \Scoutapm\Laravel\Middleware\IgnoredEndpoints::class,
    \Scoutapm\Laravel\Middleware\MiddlewareInstrument::class,
    
    // The rest of your middleware should go here
    // ...
    
    // This middleware should come last
    \Scoutapm\Laravel\Middleware\ActionInstrument::class,
]);
```

If you wish to use the \Scoutapm\Laravel\Facades\ScoutApm facade, you should also enable facades if you did not already by uncommenting the withFacades() call in bootstrap/app.php:

```php
$app->withFacades();
```

**3.** Install the `scoutapm` php extension (optional, recommended):

```bash
sudo pecl install scoutapm
```
Several instruments require the native extension to be included, including timing of `libcurl` and `file_get_contents`. For more information, or to compile manually, the [README](https://github.com/scoutapp/scout-apm-php-ext) has additional instructions.


**4.** Configuring the agent

Configure Scout in your `.env` file:

```bash
# Scout settings
SCOUT_MONITOR=true
SCOUT_KEY="[AVAILABLE IN THE SCOUT UI]"
SCOUT_NAME="A FRIENDLY NAME FOR YOUR APP"
```

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**5.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.


# Metrics

## Overview

The overview page provides an at-a-glance, auto-refreshing view of your app's performance and resource usage (mean response time by category, 95th percentile response time, throughput, error rate, and more). You can quickly dive into endpoint activity via click-and-drag (or pinch-and-expand with a mobile device) on the overview chart.



Additionally, you can compare metrics in the overview chart and see how your app's performance compares to different time periods.

## Endpoints
See a list of all your web endpoints and view those that have the highest time consumption, most throughput, allocations, or error rates. Additionally, you can narrow in on
specific timeframes and see which endpoints had higher time consumption during overall regressed time periods.

Use the comparison to look for both individual and aggregate trend lines amongst all your endpoints.



#### Individual Endpoints
You can view metrics for specific controller-action and background job workers. There is a similar chart interaction to the App Performance Overview page, with one difference: your selection will render an updated list of transaction traces that correspond to the selected time period:


You can sort traces by response time, object allocations, date, and more.

## Background Jobs

Similar to web endpoints page, view a list of your background jobs for your application and aggregate metrics such as execution time, throughput, latency, max allocations and error rate.



## Database




When the database monitoring feature is enabled, you'll gain access to both a high-level overview of your database query performance and detailed information on specific queries. Together, these pieces make it easier to get to the source of slow query performance.



#### Database Queries Overview

The high-level view helps you identify where to start:



The chart at the top shows your app's most time-consuming queries over time. Beneath the chart, you'll find a sortable list of queries grouped by a label (for Rails apps, this is the ActiveRecord model and operation) and the caller (a web endpoint or a background job):

This high-level view is engineered to reduce the investigation time required to:

* __identify slow queries__: it's easy for queries to become more inefficient over time as the size of your data grows. Sorting queries by "95th percentile response time" and "mean response time" makes it easy to identify your slowest queries.
* __solve capacity issues__: an overloaded database can have a dramatic impact on your app's performance. Sorting the list of queries by "% time consumed" shows you which queries are consuming the most time in your database.

#### Zooming

__If there is a spike in time consumed or throughput, you can easily see what changed during that period__. Click and drag over the area of interest on the chart:



Annotations are added to the queries list when zooming:

* The change in rank, based on % time consumed, of each query. Queries that jump significantly in rank may trigger a dramatic change in database performance.
* The % change across metrics in the zoom window vs. the larger timeframe. If the % change is not significant, the metric is faded.

#### Database Events

Scout highlights significant events in database performance in the sidebar. For example, if time spent in database queries increases dramatically, you'll find an insight here. Clicking on an insight jumps to the time window referenced by the insight.

#### Database Query Details

After identifying an expensive query, you need to see where the query is called and the underlying SQL. Click on a query to reveal details:



You'll see the raw SQL and a list of individual query execution times that appeared in transaction traces. Scout collects backtraces on queries consuming more than 500 ms. If we've collected a backtrace for the query, you'll see an icon next to the timing information. Click on one of the traces to reveal that trace in a new window:



The source of that trace is immediately displayed.

## External Services
Gain deeper visibility to further drill down metrics and the time spent into your external API calls with our External Services Dashboard.


# Node

Scout's NodeJS agent supports many popular libraries to instrument middleware, request times, SQL queries, and more.
The base package is called `@scout_apm/scout-apm`. See our install instructions for more details.

Source code and issues can be found on our [`@scout_apm/scout-apm`](https://github.com/scoutapp/scout_apm_node) GitHub repository.

## Requirements

`@scout_apm/scout-apm` requires:

* [NodeJS](https://nodejs.org/)
* A POSIX operating system, such as Linux or macOS.


## Updating to the Newest Version

```sh
yarn upgrade @scout_apm/scout-apm
```

The package changelog is [available here](https://github.com/scoutapp/scout_apm_node/blob/master/CHANGELOG.md).


## Instrumented Libraries

Scout provides instrumentation for:

- [Express](https://expressjs.com)
- [Postgres](https://www.postgresql.org/) (via [`pg`](https://www.npmjs.com/package/pg))
- [MySQL](https://www.mysql.com/) (via [`mysql`](https://www.npmjs.com/package/mysql) and [`mysql2`](https://www.npmjs.com/package/mysql2))
- [Pug](https://pugjs.org)
- [Mustache](https://github.com/janl/mustache.js)
- [EJS](https://www.npmjs.com/package/ejs)

For all integrations, `scout` should be required as early as possible:

```javascript
const scout = require("@scout_apm/scout-apm");
```

Requiring `scout` before other dependencies ensures that it is set up for use with your other dependencies. For example Postgres (or some library that depends on `pg`):

```javascript
const scout = require("@scout_apm/scout-apm");
const pg = require("pg");
```

In a [Typescript](https://www.typescriptlang.org/) project, if you do not import *all* of `scout`, you will need to run `setupRequireIntegrations` with the packages you want to set up:

```javascript
import { setupRequireIntegrations } from "@scout_apm/scout-apm"; // alternatively, `import "@scout_apm/scout-apm";`
setupRequireIntegrations(["pg"]);

import { Client } from "pg";
```

### Some configuration required

The libraries below require a small number of configuration updates. Click on
the respective library for instructions.

* [Express](/docs/node/configuration/#express)

You can instrument your own code or other libraries via [custom instrumentation](/docs/node/advanced-features/#custom-instrumentation).
You can suggest additional libraries you'd like Scout to instrument [on GitHub](https://github.com/scoutapp/scout_apm_node/issues).


# Notifications

## Digest Email

At a frequency of your choice (daily or weekly), Scout crunches the numbers on your app's performance (both web endpoints and background jobs). Performance is compared to the previous week, and highlights are mentioned in the email.



The email identifies performance trends, slow outliers, and attempts to narrow down issues to a specific cause (like slow HTTP requests to another service).

## Insights Email
Similar to the digest email, choose a frequency of your choice (daily or weekly), and Scout aggregates the newest insights (N+1, Slow Query, and Memory Bloat) across all your applications.


Additionally, we also will aggregate up to 5 of the slowest web request and background job traces across all of your applications.


# Opentelemetry

[](https://telemetryhub.com/)

Scout is excited to announce that we have brought an [OpenTelemetry/observability](https://scoutapm.com/blog/what-is-opentelemetry) product to market called [TelemetryHub](https://telemetryhub.com/)!

View the three pillars of your mission critical monitoring stack -- traces, logs and metrics -- all within a single pane of glass.

## Traces
View and be able to filter down the traces that matter to you most. With both in memory filtering as well as back-end aggregation filtering, you can both quickly and easily get to the bottom of your monitoring needs.



### Trace drill down
Drill down into individual traces and spans to identify which part of the request / transaction / job / task / run is causing unexpected or undesirable behavior.



### Similar spans
Whether it be DB transaction, network requests, file reads, etc. problems usually come in bunches. Wondering whether a long DB transaction is impacting multiple parts of your application and/or service group? Look for similar spans where we have seen this attribute.



## Logs
Logging is a critical piece to any application, so why not get the most of it? Use TelemetryHub's logging tool to filter both on the backend and in memory to find that piece of information you're looking for. Whether it be a customer ID or a critical log, our filtering tool can quickly help you get to the desired information. Additionally, go directly to the trace that was associated with the log, adding more context and dimensions to your logging and allowing for quicker resolution.



## Metrics
Get quick and visual feedback on the values/metrics that matter to you most. Being able to understand how things have behaved, and seeing a trajectory can quickly help you understand where you need to go -- whether it be understanding when to increase resources, understanding anomaly occurrence, etc.



## Documentation
Get the information you want right when you need it. We have built a powerful in app (as well as external) documentation engine to get you the answers you seek. Enabling you to get the most out of your monitoring solution.



## Administration
Have many services that interact with each other and delegating from where the problem arises is a game of hot potato? No problem! 

Create as many service groups as you require with the ability to limit who has access to which service group in your organization.



## Usage
Get fast insights into the amount of data your account, or any particular service group, is utilizing. With predictive look ahead billing alerts, get notified of when it appears your usage is going to be out of bounds.



## Early Access
Interested in trying out TelemetryHub? Good news! We offer a free trial upon sign up. Learn more about the free trial and our pricing at: 
https://telemetryhub.com/plans-pricing/

Ready to jump in? View our documentation page and get started on the future of observability today:
https://app.telemetryhub.com/docs




Also, visit our blog for more information on why Scout is all in on OpenTelemetry:

[What is OpenTelemetry and Why is Scout All In?](https://scoutapm.com/blog/what-is-opentelemetry)


## Want to learn more? Interested in a demo?

Reach out to [support@scoutapm.com](mailto:support@scoutapm.com) and ask us questions about our product and where observability is heading!


# Other-libraries

## Bottle 

General instructions for a Bottle app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Bottle config:
```python
from scout_apm.bottle import ScoutPlugin

app = bottle.default_app()
app.config.update({
    "scout.name": "YOUR_APP_NAME",
    "scout.key": "YOUR_KEY",
    "scout.monitor": True,
})

scout = ScoutPlugin()
bottle.install(scout)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `app.config.update`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## CherryPy 

Scout supports CherryPy 18.0.0+. 

General instructions for a CherryPy app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout plugin to your app:
```python
import cherrypy

from scout_apm.api import Config
from scout_apm.cherrypy import ScoutPlugin

class Views(object):
    @cherrypy.expose
    def index(self):
        return "Hi"

app = cherrypy.Application(Views(), "/")

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
)
scout_plugin = ScoutPlugin(cherrypy.engine)
scout_plugin.subscribe()
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Dash 

[Plotly Dash](https://dash.plot.ly/) is built on top of Flask. Therefore you should use the Scout Flask integration with the underlying Flask application object. For example:

```python
import dash
from scout_apm.flask import ScoutApm

app = dash.Dash("myapp")
app.config.suppress_callback_exceptions = True
flask_app = app.server

# Setup as per Flask integration
ScoutApm(flask_app)
flask_app.config["SCOUT_NAME"] = "A FRIENDLY NAME FOR YOUR APP"
```

For full instructions, see [the Flask integration](/docs/python/flask).

## Dramatiq

cout supports Dramatiq 1.0+. Add the following to instrument Dramatiq workers:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Dramatiq broker:

```python
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from scout_apm.dramatiq import ScoutMiddleware
from scout_apm.api import Config

broker = RabbitmqBroker()
broker.add_middleware(ScoutMiddleware(), before=broker.middleware[0].__class__)

 Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="Same as Web App Name",
    monitor=True,
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Falcon

Scout supports Falcon 2.0+. General instructions for a Falcon app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout middleware to your Falcon app:
```python
import falcon
from scout_apm.falcon import ScoutMiddleware

scout_middleware = ScoutMiddleware(config={
    "key": "[AVAILABLE IN THE SCOUT UI]",
    "monitor": True,
    "name": "A FRIENDLY NAME FOR YOUR APP",
})
api = falcon.API(middleware=[ScoutMiddleware()])
# Required for accessing extra per-request information
scout_middleware.set_api(api)
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and pass an empty dictionary to `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Huey 

Scout supports Huey 2.0+. 

Add the following to instrument your Huey application:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** If you are using [Huey's Django integration](https://huey.readthedocs.io/en/latest/django.html), you only need to set up the [Django integration](/docs/python/django). Your Huey instance will be automatically instrumented.


If you're using Huey outside of the [Django integration](/docs/python/django), add Scout to your Huey instance:

```python
from huey import SqliteHuey
from scout_apm.api import Config
from scout_apm.huey import attach_scout

broker = SqliteHuey()

 Config.set(
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
    key="[AVAILABLE IN THE SCOUT UI]",
)
attach_scout(huey)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set()`.


[If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via](/docs/python/django) [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Hug 

Scout supports Hug 2.5.1+. Hug is based on Falcon so a Falcon version supported by [our integration](/docs/python/other-libraries#falcon) is also needed. 

General instructions for a Hug app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout inside your Hug app:

```python
from scout_apm.hug import integrate_scout

# Setup your Hug endpoints as usual

@hug.get("/")
def home():
    return "Welcome home."

# Integrate scout with the Hug application for this module
integrate_scout(
    __name__,
    config={
        "key": "[AVAILABLE IN THE SCOUT UI]",
        "monitor": True,
        "name": "A FRIENDLY NAME FOR YOUR APP",
    },
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the entries in `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Nameko 

General instructions for a Nameko app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure scout once in the root of your app, and add a `ScoutReporter` to each Nameko service:

```python
from scout_apm.api import Config
from scout_apm.nameko import ScoutReporter


Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

class Service(object):
    name = "myservice"

    scout = ScoutReporter()

    @http("GET", "/")
    def home(self, request):
        return "Welcome home."
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Pyramid 

General instructions for a Pyramid app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Pyramid config:

```python
import scout_apm.pyramid

if __name__ == "__main__":
    with Configurator() as config:
        config.add_settings(
            SCOUT_KEY="[AVAILABLE IN THE SCOUT UI]",
            SCOUT_MONITOR=True,
            SCOUT_NAME="A FRIENDLY NAME FOR YOUR APP"
        )
        config.include("scout_apm.pyramid")

        # Rest of your config...
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `config.add_settings`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## RQ

Scout supports RQ 1.0+. 

Do the following to instrument your RQ jobs:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Use the Scout RQ worker class.

If you're using RQ directly, you can pass the `--worker-class` argument the worker command:

```bash
rq worker --job-class scout_apm.rq.Worker myqueue
```

If you're using the [RQ Heroku pattern](https://python-rq.org/patterns/), you can change your code to use the `scout_apm.rq.HerokuWorker` class:

```python
from scout_apm.rq import HerokuWorker as Worker
```

If you're using Django-RQ, instead use the [custom worker setting](https://github.com/rq/django-rq#custom-job-and-worker-classes) to point to our custom Worker class:
```python
RQ = {
    "WORKER_CLASS": "scout_apm.rq.Worker",
}
```
If you're using your own `Worker` sub class already, you can subclass our `Worker` class:
```python
from scout_apm.rq import Worker

class MyWorker(Worker):
    # your custom behaviour here
    pass
```
Or if you're combining one or more other `Worker` classes, you can add our mixin class `scout_apm.rq.WorkerMixin`:
```python
from some.other.rq.extension import CustomWorker
from scout_apm.rq import WorkerMixin

class MyWorker(WorkerMixin, CustomWorker):
    pass
```
**3.** Configure Scout.

If you're using Django-RQ, ensure you have the [Django integration](/docs/python/django) installed, and this is handled for you.

If you're using RQ directly, create a [config file](https://python-rq.org/docs/workers/#using-a-config-file) for it that runs the Scout API's `Config.set()`:
```python
from scout_apm.api import Config
  
Config.set(
    key="YOUR_SCOUT_KEY",
    name="Same as Web App Name",
    monitor=True,
)
```
Pass the config file to `-c` argument to the worker command, as per [the documentation](https://python-rq.org/docs/workers/#using-a-config-file).

If you wish to configure Scout via environment variables, you don't need a config file. Set `SCOUT_KEY`, `SCOUT_NAME` and `SCOUT_MONITOR` instead.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**4.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Starlette 

Scout supports Starlette 0.12+. General instructions for a Starlette app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout and attach its middleware to your Starlette app:
```python
from scout_apm.api import Config
from scout_apm.async_.starlette import ScoutMiddleware
from starlette.applications import Starlette
from starlette.middleware import Middleware

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

middleware = [
 # Should be *first* in your stack, so it's the outermost and can
 # track all requests
 Middleware(ScoutMiddleware),
]

app = Starlette(middleware=middleware)
```
If you're using Starlette <0.13, which [refactored the middleware API](https://github.com/encode/starlette/pull/704), instead use `app.add_middleware(ScoutMiddleware)`. Make sure it's the last call to `add_middleware()` so that Scout is the outermost middleware.

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.


# Php

Our PHP agent supports PHP versions 7.2 to 8.3!
Scout's PHP agent supports many popular libraries to instrument middleware, request times, SQL queries, and more.

The base package is called `scoutapp/scout-apm-php`, Laravel instrumentation
is in the `scoutapp/scout-apm-laravel`, and Symfony instrumentation in `scoutapp/scout-apm-symfony-bundle`. See our install instructions for more details:

* [Laravel](/docs/php/laravel)
* [Symfony](/docs/php/symfony)


Source code and issues can be found on our [scout-apm-php](https://github.com/scoutapp/scout-apm-php) GitHub repository.

Requirements

`scout-apm-php` requires:

* PHP
* A POSIX operating system, such as Linux or macOS.

## Instrumented Libraries

Scout provides automatic instrumentation for:
* Laravel 5.5+
* Lumen 5.5+
* Symfony 4.0+
* PDO
* libcurl
* Predis
* PhpRedis
* ElasticSearch
* MongoDB
* Memcached

### Some configuration required

The libraries below require a small number of configuration updates. Click on
the respective library for instructions.

* [Laravel](/docs/php/laravel)
    * Middleware
    * Controllers
    * SQL queries
    * Job queues
    * Blade rendering
* [Symfony](/docs/php/symfony)
    * Controllers
    * SQL queries (Doctrine)
    * Twig rendering
    
Additionally, [Scout can also instrument request queuing time](/docs/features/#request-queuing).

You can instrument your own code or other libraries via [custom instrumentation](/docs/php/features/#custom-instrumentation).
You can suggest additional libraries you'd like Scout to instrument
[on GitHub](https://github.com/scoutapp/scout-apm-php/issues).


## Updating to the Newest Version

```sh
composer update scout-apm-laravel
```

The package changelog/release information can be [found here](https://github.com/scoutapp/scout-apm-php/releases).


# Rack

## Rack

Rack instrumentation is more explicit than Rails instrumentation, since Rack applications can take
nearly any form. After [installing our agent](/docs/ruby/), instrumenting Rack is a three step process:

1. Configuring the agent
2. Starting the agent
3. Wrapping endpoints in tracing

### Configuration

Rack apps are configured using the same approach as a Rails app: either via a `config/scout_apm.yml` config file or environment variables.

* __configuration file__: create a `config/scout_apm.yml` file under your application root directory. The file structure is outlined [here](/docs/ruby/configuration).
* __environment variables__: see our docs on configuring the agent via [environment variables](/docs/ruby/configuration).

### Starting the Agent

Add the `ScoutApm::Rack.install!` startup call as close to the spot you
`run` your Rack application as possible.  `install!`
should be called after you require other gems (ActiveRecord, Mongo, etc)
to install instrumentation for those libraries.

```ruby
# config.ru

require 'scout_apm'
ScoutApm::Rack.install!

run MyApp
```

### Adding endpoints

Wrap each endpoint in a call to `ScoutApm::Rack#transaction(name, env)`.

* `name` - an unchanging string argument for what the endpoint is. Example: `"API User Listing"`
* `env` - the rack environment hash

This may be fairly application specific in details.

Example:

```ruby
app = Proc.new do |env|
  ScoutApm::Rack.transaction("API User Listing", env) do
    User.all.to_json
    ['200', {'Content-Type' => 'application/json'}, [users]]
  end
end
```

If you run into any issues, or want advice on naming or wrapping endpoints, contact us at
support@scoutapm.com for additional help.


# Rq

## Bottle 

General instructions for a Bottle app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Bottle config:
```python
from scout_apm.bottle import ScoutPlugin

app = bottle.default_app()
app.config.update({
    "scout.name": "YOUR_APP_NAME",
    "scout.key": "YOUR_KEY",
    "scout.monitor": True,
})

scout = ScoutPlugin()
bottle.install(scout)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `app.config.update`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## CherryPy 

Scout supports CherryPy 18.0.0+. 

General instructions for a CherryPy app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout plugin to your app:
```python
import cherrypy

from scout_apm.api import Config
from scout_apm.cherrypy import ScoutPlugin

class Views(object):
    @cherrypy.expose
    def index(self):
        return "Hi"

app = cherrypy.Application(Views(), "/")

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
)
scout_plugin = ScoutPlugin(cherrypy.engine)
scout_plugin.subscribe()
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Dash 

[Plotly Dash](https://dash.plot.ly/) is built on top of Flask. Therefore you should use the Scout Flask integration with the underlying Flask application object. For example:

```python
import dash
from scout_apm.flask import ScoutApm

app = dash.Dash("myapp")
app.config.suppress_callback_exceptions = True
flask_app = app.server

# Setup as per Flask integration
ScoutApm(flask_app)
flask_app.config["SCOUT_NAME"] = "A FRIENDLY NAME FOR YOUR APP"
```

For full instructions, see [the Flask integration](/docs/python/flask).

## Dramatiq

cout supports Dramatiq 1.0+. Add the following to instrument Dramatiq workers:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Dramatiq broker:

```python
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from scout_apm.dramatiq import ScoutMiddleware
from scout_apm.api import Config

broker = RabbitmqBroker()
broker.add_middleware(ScoutMiddleware(), before=broker.middleware[0].__class__)

 Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="Same as Web App Name",
    monitor=True,
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Falcon

Scout supports Falcon 2.0+. General instructions for a Falcon app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout middleware to your Falcon app:
```python
import falcon
from scout_apm.falcon import ScoutMiddleware

scout_middleware = ScoutMiddleware(config={
    "key": "[AVAILABLE IN THE SCOUT UI]",
    "monitor": True,
    "name": "A FRIENDLY NAME FOR YOUR APP",
})
api = falcon.API(middleware=[ScoutMiddleware()])
# Required for accessing extra per-request information
scout_middleware.set_api(api)
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and pass an empty dictionary to `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Huey 

Scout supports Huey 2.0+. 

Add the following to instrument your Huey application:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** If you are using [Huey's Django integration](https://huey.readthedocs.io/en/latest/django.html), you only need to set up the [Django integration](/docs/python/django). Your Huey instance will be automatically instrumented.


If you're using Huey outside of the [Django integration](/docs/python/django), add Scout to your Huey instance:

```python
from huey import SqliteHuey
from scout_apm.api import Config
from scout_apm.huey import attach_scout

broker = SqliteHuey()

 Config.set(
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
    key="[AVAILABLE IN THE SCOUT UI]",
)
attach_scout(huey)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set()`.


[If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via](/docs/python/django) [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Hug 

Scout supports Hug 2.5.1+. Hug is based on Falcon so a Falcon version supported by [our integration](/docs/python/other-libraries#falcon) is also needed. 

General instructions for a Hug app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout inside your Hug app:

```python
from scout_apm.hug import integrate_scout

# Setup your Hug endpoints as usual

@hug.get("/")
def home():
    return "Welcome home."

# Integrate scout with the Hug application for this module
integrate_scout(
    __name__,
    config={
        "key": "[AVAILABLE IN THE SCOUT UI]",
        "monitor": True,
        "name": "A FRIENDLY NAME FOR YOUR APP",
    },
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the entries in `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Nameko 

General instructions for a Nameko app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure scout once in the root of your app, and add a `ScoutReporter` to each Nameko service:

```python
from scout_apm.api import Config
from scout_apm.nameko import ScoutReporter


Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

class Service(object):
    name = "myservice"

    scout = ScoutReporter()

    @http("GET", "/")
    def home(self, request):
        return "Welcome home."
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Pyramid 

General instructions for a Pyramid app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Pyramid config:

```python
import scout_apm.pyramid

if __name__ == "__main__":
    with Configurator() as config:
        config.add_settings(
            SCOUT_KEY="[AVAILABLE IN THE SCOUT UI]",
            SCOUT_MONITOR=True,
            SCOUT_NAME="A FRIENDLY NAME FOR YOUR APP"
        )
        config.include("scout_apm.pyramid")

        # Rest of your config...
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `config.add_settings`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## RQ

Scout supports RQ 1.0+. 

Do the following to instrument your RQ jobs:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Use the Scout RQ worker class.

If you're using RQ directly, you can pass the `--worker-class` argument the worker command:

```bash
rq worker --job-class scout_apm.rq.Worker myqueue
```

If you're using the [RQ Heroku pattern](https://python-rq.org/patterns/), you can change your code to use the `scout_apm.rq.HerokuWorker` class:

```python
from scout_apm.rq import HerokuWorker as Worker
```

If you're using Django-RQ, instead use the [custom worker setting](https://github.com/rq/django-rq#custom-job-and-worker-classes) to point to our custom Worker class:
```python
RQ = {
    "WORKER_CLASS": "scout_apm.rq.Worker",
}
```
If you're using your own `Worker` sub class already, you can subclass our `Worker` class:
```python
from scout_apm.rq import Worker

class MyWorker(Worker):
    # your custom behaviour here
    pass
```
Or if you're combining one or more other `Worker` classes, you can add our mixin class `scout_apm.rq.WorkerMixin`:
```python
from some.other.rq.extension import CustomWorker
from scout_apm.rq import WorkerMixin

class MyWorker(WorkerMixin, CustomWorker):
    pass
```
**3.** Configure Scout.

If you're using Django-RQ, ensure you have the [Django integration](/docs/python/django) installed, and this is handled for you.

If you're using RQ directly, create a [config file](https://python-rq.org/docs/workers/#using-a-config-file) for it that runs the Scout API's `Config.set()`:
```python
from scout_apm.api import Config
  
Config.set(
    key="YOUR_SCOUT_KEY",
    name="Same as Web App Name",
    monitor=True,
)
```
Pass the config file to `-c` argument to the worker command, as per [the documentation](https://python-rq.org/docs/workers/#using-a-config-file).

If you wish to configure Scout via environment variables, you don't need a config file. Set `SCOUT_KEY`, `SCOUT_NAME` and `SCOUT_MONITOR` instead.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**4.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Starlette 

Scout supports Starlette 0.12+. General instructions for a Starlette app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout and attach its middleware to your Starlette app:
```python
from scout_apm.api import Config
from scout_apm.async_.starlette import ScoutMiddleware
from starlette.applications import Starlette
from starlette.middleware import Middleware

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

middleware = [
 # Should be *first* in your stack, so it's the outermost and can
 # track all requests
 Middleware(ScoutMiddleware),
]

app = Starlette(middleware=middleware)
```
If you're using Starlette <0.13, which [refactored the middleware API](https://github.com/encode/starlette/pull/704), instead use `app.add_middleware(ScoutMiddleware)`. Make sure it's the last call to `add_middleware()` so that Scout is the outermost middleware.

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.


# Setup

Get started in under 3 minutes with our easy to install Ruby agent.
## Installation 



**Step A**: Install our gem.


In your gemfile:

```ruby
gem 'scout_apm'
```

Shell:

```bash
bundle install
```



**Step B**: Download your customized config file from https://scoutapm.com/apps/new_ruby_application_configuration, placing it at `config/scout_apm.yml`.




**Heroku Customers**: We initially provision your application using environment variables instead of the `config/scout_apm.yml`. Configuration values set via env variables will take priority over those set via yaml.




**Step C**: Deploy.




When adding Scout APM it is advised to set `monitor: true` in development as well as production,
as showing that it works in development makes things easier for the user. Additionally, the `name` should be
the same as production, but with `(development)` added to it. Also, comment that the SCOUT_KEY can 
be found in their settings page.


## Local
Testing/using Scout APM locally is as easy as following the above instructions, but setting `monitor: true` under development in your `config/scout_apm.yml`.

You may also want to denote a different app name using the `name` configuration value in development. For example:
```
development:
  <<: *defaults
  monitor: true
  name: Example (development)
```


# Setup

Get started in under 3 minutes with our easy to install Python agent.
## Installation 



## Django Installation

The latest `scout-apm` package supports Django 3.2+.

**Older Django Versions**: Older versions of Django may be supported by previous versions of the `scout-apm` package.

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Configure Scout in your `settings.py` file:

```python
# settings.py
INSTALLED_APPS = [
    "scout_apm.django",  # should be listed first
    # ... other apps ...
]

# Scout settings
SCOUT_MONITOR = True
SCOUT_KEY = "[AVAILABLE IN THE SCOUT UI]"
SCOUT_NAME = "A FRIENDLY NAME FOR YOUR APP"
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` instead of providing these settings in `settings.py`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.

## Flask Installation

The latest `scout-apm` package supports Flask 0.10+.

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Configure Scout inside your Flask app:

```python
from scout_apm.flask import ScoutApm

# Setup a flask 'app' as normal

# Attach ScoutApm to the Flask App
ScoutApm(app)

# Scout settings
app.config["SCOUT_MONITOR"] = True
app.config["SCOUT_KEY"] = "[AVAILABLE IN THE SCOUT UI]"
app.config["SCOUT_NAME"] = "A FRIENDLY NAME FOR YOUR APP"
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` and remove the calls to `app.config`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.

## Fast API Installation

Scout supports FastAPI through the Starlette instrumentation. General instructions for a FastAPI app:

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Attach the Scout middleware to your FastAPI app:

```python
from fastapi import FastAPI
from scout_apm.api import Config
from scout_apm.async_.starlette import ScoutMiddleware

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)
app = FastAPI()
app.add_middleware(ScoutMiddleware)
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` and pass an empty dictionary to `config`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.

## Celery Installation

The latest `scout-apm` package supports Celery 3.1+.

**Step A**: Install the `scout-apm` package:

```bash
pip install scout-apm
```

**Step B**: Configure Scout in your Celery application file:

```python
import scout_apm.celery
from scout_apm.api import Config
from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

# If you are using app.config_from_object() to point to your Django settings
# and have configured Scout there, configuring here is not necessary:
Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="Same as Web App Name",
    monitor=True,
)

# This attaches the instrumentation to your app and makes Scout work:
scout_apm.celery.install(app)
```

The `app` argument is optional and was added in version 2.12.0, but you should provide it for complete instrumentation.

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME`, and `SCOUT_KEY` instead of calling `Config.set`.

**Heroku Customers**: If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is additionally required.

**Step C**: Deploy.

It takes approximately five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.


## SQLAlchemy Installation

Instrument SQLAlchemy queries:

```python
from scout_apm.sqlalchemy import instrument_sqlalchemy

# Assuming something like engine = create_engine('sqlite:///:memory:', echo=True)
instrument_sqlalchemy(engine)
```


# Sinatra

## Sinatra

Instrumenting a Sinatra application is similar to instrumenting a generic [Rack application](/docs/ruby/rack).

### Configuration

The agent configuration (API key, app name, etc) follows the same process as the [Rack application config](/docs/ruby/rack).

### Starting the agent

Add the `ScoutApm::Rack.install!` startup call as close to the spot you
`run` your Sinatra application as possible.  <span style="white-space: nowrap;">`install!`</span>
should be called _after_ you require other gems (ActiveRecord, Mongo, etc).

```ruby
require './main'

require 'scout_apm'
ScoutApm::Rack.install!

run Sinatra::Application
```

### Adding endpoints

Wrap each endpoint in a call to `ScoutApm::Rack#transaction(name, env)`. For example:

```ruby
get '/' do
  ScoutApm::Rack.transaction("get /", request.env) do
    ActiveRecord::Base.connection.execute("SELECT * FROM pg_catalog.pg_tables")
    "Hello!"
  end
end
```

See our [Rack docs for adding an endpoint](/docs/ruby/rack/#adding-endpoints) for more details.


# Sqlalchemy

## Installation

Instrument SQLAlchemy queries:

```python
from scout_apm.sqlalchemy import instrument_sqlalchemy

# Assuming something like engine = create_engine('sqlite:///:memory:', echo=True)
instrument_sqlalchemy(engine)
```


# Sso

## Okta

### Setting up Okta
Once you have [reached out to Scout](mailto:support@scoutapm.com) to enable SAML for your account:

**1. Okta Setup**

In the Okta admin, create a new SAML Application:

Application Name: ScoutAPM

Single Sign on URL: https://scoutapm.com/users/auth/saml/callback

Check "Use this for Recipient URL and Destination URL"

Uncheck "Allow this app to request other SSO URLs"

Audience URI: Scout

Relay state left blank

Name ID format: Email Address

Application Username: Email

Save the metadata from Okta to a file (an XML document with your entity id, login url and certificate)

**2. Scout Setup**

Only the Scout org owner can change the SSO settings.

Log into Scout with your password

Go to the org admin screen, and select 'SSO Settings'

Upload the metadata.xml file

**3. Try it!**

In Okta, assign users to the new Scout application. Any users that Scout does not recognize will auto-create on first login.

Log out of Scout

On the login screen, after entering your email you'll see a 'Login with SAML' option, which will redirect you to Okta for authentication, and back to Scout.


# Starlette

## Bottle 

General instructions for a Bottle app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Bottle config:
```python
from scout_apm.bottle import ScoutPlugin

app = bottle.default_app()
app.config.update({
    "scout.name": "YOUR_APP_NAME",
    "scout.key": "YOUR_KEY",
    "scout.monitor": True,
})

scout = ScoutPlugin()
bottle.install(scout)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `app.config.update`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## CherryPy 

Scout supports CherryPy 18.0.0+. 

General instructions for a CherryPy app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout plugin to your app:
```python
import cherrypy

from scout_apm.api import Config
from scout_apm.cherrypy import ScoutPlugin

class Views(object):
    @cherrypy.expose
    def index(self):
        return "Hi"

app = cherrypy.Application(Views(), "/")

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
)
scout_plugin = ScoutPlugin(cherrypy.engine)
scout_plugin.subscribe()
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Dash 

[Plotly Dash](https://dash.plot.ly/) is built on top of Flask. Therefore you should use the Scout Flask integration with the underlying Flask application object. For example:

```python
import dash
from scout_apm.flask import ScoutApm

app = dash.Dash("myapp")
app.config.suppress_callback_exceptions = True
flask_app = app.server

# Setup as per Flask integration
ScoutApm(flask_app)
flask_app.config["SCOUT_NAME"] = "A FRIENDLY NAME FOR YOUR APP"
```

For full instructions, see [the Flask integration](/docs/python/flask).

## Dramatiq

cout supports Dramatiq 1.0+. Add the following to instrument Dramatiq workers:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Dramatiq broker:

```python
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from scout_apm.dramatiq import ScoutMiddleware
from scout_apm.api import Config

broker = RabbitmqBroker()
broker.add_middleware(ScoutMiddleware(), before=broker.middleware[0].__class__)

 Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="Same as Web App Name",
    monitor=True,
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Falcon

Scout supports Falcon 2.0+. General instructions for a Falcon app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Attach the Scout middleware to your Falcon app:
```python
import falcon
from scout_apm.falcon import ScoutMiddleware

scout_middleware = ScoutMiddleware(config={
    "key": "[AVAILABLE IN THE SCOUT UI]",
    "monitor": True,
    "name": "A FRIENDLY NAME FOR YOUR APP",
})
api = falcon.API(middleware=[ScoutMiddleware()])
# Required for accessing extra per-request information
scout_middleware.set_api(api)
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and pass an empty dictionary to `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Huey 

Scout supports Huey 2.0+. 

Add the following to instrument your Huey application:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** If you are using [Huey's Django integration](https://huey.readthedocs.io/en/latest/django.html), you only need to set up the [Django integration](/docs/python/django). Your Huey instance will be automatically instrumented.


If you're using Huey outside of the [Django integration](/docs/python/django), add Scout to your Huey instance:

```python
from huey import SqliteHuey
from scout_apm.api import Config
from scout_apm.huey import attach_scout

broker = SqliteHuey()

 Config.set(
    monitor=True,
    name="A FRIENDLY NAME FOR YOUR APP",
    key="[AVAILABLE IN THE SCOUT UI]",
)
attach_scout(huey)
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` instead of calling `Config.set()`.


[If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via](/docs/python/django) [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Hug 

Scout supports Hug 2.5.1+. Hug is based on Falcon so a Falcon version supported by [our integration](/docs/python/other-libraries#falcon) is also needed. 

General instructions for a Hug app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout inside your Hug app:

```python
from scout_apm.hug import integrate_scout

# Setup your Hug endpoints as usual

@hug.get("/")
def home():
    return "Welcome home."

# Integrate scout with the Hug application for this module
integrate_scout(
    __name__,
    config={
        "key": "[AVAILABLE IN THE SCOUT UI]",
        "monitor": True,
        "name": "A FRIENDLY NAME FOR YOUR APP",
    },
) 
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the entries in `config`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Nameko 

General instructions for a Nameko app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure scout once in the root of your app, and add a `ScoutReporter` to each Nameko service:

```python
from scout_apm.api import Config
from scout_apm.nameko import ScoutReporter


Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

class Service(object):
    name = "myservice"

    scout = ScoutReporter()

    @http("GET", "/")
    def home(self, request):
        return "Welcome home."
```

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## Pyramid 

General instructions for a Pyramid app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Add Scout to your Pyramid config:

```python
import scout_apm.pyramid

if __name__ == "__main__":
    with Configurator() as config:
        config.add_settings(
            SCOUT_KEY="[AVAILABLE IN THE SCOUT UI]",
            SCOUT_MONITOR=True,
            SCOUT_NAME="A FRIENDLY NAME FOR YOUR APP"
        )
        config.include("scout_apm.pyramid")

        # Rest of your config...
```
If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `config.add_settings`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

## RQ

Scout supports RQ 1.0+. 

Do the following to instrument your RQ jobs:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Use the Scout RQ worker class.

If you're using RQ directly, you can pass the `--worker-class` argument the worker command:

```bash
rq worker --job-class scout_apm.rq.Worker myqueue
```

If you're using the [RQ Heroku pattern](https://python-rq.org/patterns/), you can change your code to use the `scout_apm.rq.HerokuWorker` class:

```python
from scout_apm.rq import HerokuWorker as Worker
```

If you're using Django-RQ, instead use the [custom worker setting](https://github.com/rq/django-rq#custom-job-and-worker-classes) to point to our custom Worker class:
```python
RQ = {
    "WORKER_CLASS": "scout_apm.rq.Worker",
}
```
If you're using your own `Worker` sub class already, you can subclass our `Worker` class:
```python
from scout_apm.rq import Worker

class MyWorker(Worker):
    # your custom behaviour here
    pass
```
Or if you're combining one or more other `Worker` classes, you can add our mixin class `scout_apm.rq.WorkerMixin`:
```python
from some.other.rq.extension import CustomWorker
from scout_apm.rq import WorkerMixin

class MyWorker(WorkerMixin, CustomWorker):
    pass
```
**3.** Configure Scout.

If you're using Django-RQ, ensure you have the [Django integration](/docs/python/django) installed, and this is handled for you.

If you're using RQ directly, create a [config file](https://python-rq.org/docs/workers/#using-a-config-file) for it that runs the Scout API's `Config.set()`:
```python
from scout_apm.api import Config
  
Config.set(
    key="YOUR_SCOUT_KEY",
    name="Same as Web App Name",
    monitor=True,
)
```
Pass the config file to `-c` argument to the worker command, as per [the documentation](https://python-rq.org/docs/workers/#using-a-config-file).

If you wish to configure Scout via environment variables, you don't need a config file. Set `SCOUT_KEY`, `SCOUT_NAME` and `SCOUT_MONITOR` instead.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**4.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.

Tasks will appear in the "Background Jobs" area of the Scout UI.

## Starlette 

Scout supports Starlette 0.12+. General instructions for a Starlette app:

**1.** Install the `scout-apm` package:

```bash
pip install scout-apm
```

**2.** Configure Scout and attach its middleware to your Starlette app:
```python
from scout_apm.api import Config
from scout_apm.async_.starlette import ScoutMiddleware
from starlette.applications import Starlette
from starlette.middleware import Middleware

Config.set(
    key="[AVAILABLE IN THE SCOUT UI]",
    name="A FRIENDLY NAME FOR YOUR APP",
    monitor=True,
)

middleware = [
 # Should be *first* in your stack, so it's the outermost and can
 # track all requests
 Middleware(ScoutMiddleware),
]

app = Starlette(middleware=middleware)
```
If you're using Starlette <0.13, which [refactored the middleware API](https://github.com/encode/starlette/pull/704), instead use `app.add_middleware(ScoutMiddleware)`. Make sure it's the last call to `add_middleware()` so that Scout is the outermost middleware.

If you wish to configure Scout via environment variables, use `SCOUT_MONITOR`, `SCOUT_NAME` and `SCOUT_KEY` and remove the call to `Config.set`.

If you've installed Scout via the Heroku Addon, the provisioning process automatically sets `SCOUT_MONITOR` and `SCOUT_KEY` via [config vars](https://devcenter.heroku.com/articles/config-vars). Only `SCOUT_NAME` is required.

**3.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.


# Symfony

## Symfony 

Scout supports Symfony 4+.

**1.** Install the `scoutapp/scout-apm-symfony-bundle` bundle:

```bash
composer require scoutapp/scout-apm-symfony-bundle
```

Note that the `scout-apm-php` package will automatically be included. It does not need to be installed directly.

**2.** Install the `scoutapm` php extension (optional, recommended):

```bash
sudo pecl install scoutapm
```

Several instruments require the native extension to be included, including timing of `libcurl` and `file_get_contents`. For more information, or to compile manually, the [README](https://github.com/scoutapp/scout-apm-php-ext) has additional instructions.

**3.** Configure Scout in your `config/packages/scoutapm.xml` file:
```xml
<?xml version="1.0" ?>

<container xmlns="http://symfony.com/schema/dic/services"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:scoutapm="http://example.org/schema/dic/scout_apm"
    xsi:schemaLocation="http://symfony.com/schema/dic/services https://symfony.com/schema/dic/services/services-1.0.xsd">

    <scoutapm:config>
        <scoutapm:scoutapm
            name="my application name..."
            key="%env(SCOUT_KEY)%"
            monitor="true"
        />
    </scoutapm:config>
</container>
```
It is recommended not to commit the Scout APM key to version control. Instead, configure via environment variables, e.g. in `.env.local`:

```bash
SCOUT_KEY=your_scout_key_here
```

Since the configuration XML above uses `%env(SCOUT_KEY)%` this will be pulled in automatically.

**4.** Add the bundle to `config/bundles.php`.
```php
<?php

return [
    // ... other bundles...
    Scoutapm\ScoutApmBundle\ScoutApmBundle::class => ['all' => true],
];
```
**5.** Deploy.

It takes approximatively five minutes for your data to first appear within the Scout UI.


# Traces

## Trace Transactions

Scout collects detailed transactions across your web endpoints and background jobs automatically. The transaction traces provide a number of visual queues to direct you to hotspots. Dig into bottlenecks - down to the line-of-code, author, commit date, and deploy time - from this view.



### SQL Queries

Scout captures a sanitized version of SQL queries. Click the "SQL" button next to a call to view details.




#### Don't see an SQL button next to a database query?

Scout collects a sanitized version of SQL queries and displays these in transaction traces. To limit agent overhead sanitizing queries, we do not collect query statements with more than 16k characters.


### Code Backtraces

You'll see "CODE" buttons next to method calls that are >= 500 ms. [If you've enabled the GitHub integration](/docs/features/#github), you can see the line-of-code, associated SQL or HTTP endpoint (if applicable), author, commit date, and deploy time for the relevant slow code.



If you don't enable the GitHub integration, you'll see a backtrace.

### Trace Views

There are two displays for showing the details of a transaction trace:

* __Summary View__ - Method calls are aggregated together and ordered from most to least expensive.
* __Timeline View__ - Shows the execution order of calls as they occur during the transaction.

#### Summary View

Method calls are aggregated together and listed from most expensive to least expensive. The time displayed is the total time across all calls (not the time per-call).



#### Timeline View

See the execution order of your code.



## Trace Explorer

What was the slowest request yesterday? How has the app performed for `user@domain.com`? Which endpoints are generating the bulk of slow requests? Trace Explorer lets you quickly filter the transaction traces collected by Scout, giving you answers to your unique questions.



Trace Explorer is accessed via the "Traces" navigation link when viewing an app.

### How to use Trace Explorer

There are two main areas of Trace Explorer:

* __Dimension Histograms__ - the top portion of the page generates a histogram representation for a number of trace dimensions (the response time distribution, count of traces by endpoints, and a display for each piece of [custom context](/docs/features/#custom-context)). Selecting a specific area of a chart filters the transactions to just the selected data.
* __List of transaction traces__ - the bottom portion of the page lists the [individual traces](/docs/features/#transaction-traces). The traces are updated to reflect those that match any filtered dimensions. You can increase the height of this pane by clicking and dragging the top portion of the pane. Clicking on a trace URI opens the transaction trace in a new browser tab.

### Custom Trace Querying



From the top right of the Trace Explorer, you can select a "Dataset" of 1000 traces. These include a random "Sample", the "Slowest" traces, or those with the "Most Allocations". In addition, you can select the "Query" button to build a custom query. Here, you can query on any attribute you'd like, including custom context you've set. Only want to load traces for a specific user_id? From a certain host? Apply as many conditions as you like, and then select "Apply Filters".


# Troubleshooting

## Troubleshooting

Not seeing data? [Email support@scoutapm.com](mailto:support@scoutapm.com) with:

* A link to your app within Scout (if applicable)
* Your PHP version
* The name of the framework and version you are trying to instrument, e.g. Laravel 5.8
* [Scout debug logs](/docs/php/logging)

We typically respond within a couple of hours during the business day.

### Common Issues

Common issues while getting started:

#### Unable to launch the core agent

The Scout PHP agent attempts to automatically download and launch the `core-agent` binary. The most common issue with the core agent is that the default directory the Scout agent uses does not have the correct permissions for downloading and launching the core agent. The solution for this is to create or identify an appropriate directory that the PHP agent can use to download and execure the core agent, and indicate that in the [core_agent_dir](/docs/php/configuration#core_agent_dir) configuration directive.

All of the core agent configuration options can be found [here](/docs/php/configuration#core-agent-configurations)

You can find more in-depth information on the core agent [here](https://scoutapm.com/docs/core-agent)

#### Additional Instrumentation with the PHP Extension

The [Scout APM PHP Extension](https://github.com/scoutapp/scout-apm-php-ext) allows instrumentation of internal PHP functions that can't be done in regular PHP. While it is optional, in order to get the full amount of instrumnted library support out of the box, you may want to install the Scout PHP Extension. The Scout PHP Extension adds instrumentation for:

* Core functions: `file_get_contents`, `file_put_contents`, `fread`, `fwrite`
* Curl functions: `curl_exec`
* PDO methods: `PDO->exec`, `PDO->query`, `PDOStatement->execute`
* Predis PHP library methods
* phpredis PHP extension methods
* Memcached PHP extension methods
* Elasticsearch PHP library methods

It is easily [installed via PECL](https://github.com/scoutapp/scout-apm-php-ext#installing-from-pecl) or can be [manually compiled and installed](https://github.com/scoutapp/scout-apm-php-ext#building)

#### Compiling cURL support (Scout PHP Extension)

You will need the correct cURL libraries installed prior to compiling the Scout PHP Extension. Please refer to the extension's [Readme](https://github.com/scoutapp/scout-apm-php-ext#prerequisites-for-curl) for details.

#### Log Verbosity

In order to assist in troubleshooting and installation, the Scout PHP agent is extremely verbose by default. Once you have the Scout PHP agent working, you will likely want to reduce the log verbosity levels. Instructions can be found [here](https://github.com/scoutapp/scout-apm-php#default-log-level)

### Debug Logs

To set Scout's log level to debug, set the [log_level](/docs/php/configuration#log_level) configuration to `debug`.

Scout's log level defaults to the same log level as the LoggerInterface provided, if you aren't seeing debug log levels from Scout, you will need to lower your LoggerInterface's log level as well.

#### Core-Agent
In some cases, debug level logs from the PHP agent may not be enough, and [trace level core-agent logs](/docs/core-agent#troubleshooting) may be needed.

### Request Payloads
In certain cases, knowing the payload that is being sent to the core agent is useful for debugging. To capture the payload (the request), set `SCOUT_LOG_PAYLOAD_CONTENT=true`


# Troubleshooting

## Contacting Support

Contact us at [support@scoutapm.com](mailto:support@scoutapm.com) or message us on [Discord](https://discord.gg/keGzRHD3pv) with any comments, issues, or questions.


## Service Status

We're transparent about our uptime and service issues. If you appear to be experiencing issues with our service:

* [Check out our status site](https://status.scoutapm.com). You can subscribe to service incidents.
* [Email us](mailto:support@scoutapm.com). Our support team will get back to you right away. 


## Specific Language Troubleshooting

You can find more detailed troubleshooting pages for specific languages here:
* [Ruby Troubleshooting](https://scoutapm.com/docs/ruby/troubleshooting)
* [Python Troubleshooting](https://scoutapm.com/docs/python/troubleshooting)
* [PHP Troubleshooting](https://scoutapm.com/docs/php/troubleshooting)
* [Node.js Troubleshooting](https://scoutapm.com/docs/node/troubleshooting)
* [Elixir Troubleshooting](https://scoutapm.com/docs/elixir/troubleshooting)

## Github Troubleshooting

If you are having an issue with adding your Github repository, see our [Github Troubleshooting Doc](https://scoutapm.com/docs/integrations/git#github-integration----resetting).


# Troubleshooting

## Troubleshooting

Not seeing data? [Email support@scoutapm.com](mailto:support@scoutapm.com?subject=New%20Support%20Ticket%20%5bYour%20App%5d&body=Scout%20Link%20to%20your%20app:%20%0A%0dNodeJS%20Version:%20%0A%0dFramework:%20%0A%0dScout%20logs:%20%0A%0d) with:

* A link to your app within Scout (if applicable)
* Your NodeJS version
* The name of the framework and version you are trying to instrument, e.g. Express 4.17.0
* [Scout debug logs](/docs/node/logging)

We typically respond within a couple of hours during the business day.

#### Core-Agent
In some cases, debug level logs from the Node agent may not be enough, and [trace level core-agent logs](/docs/core-agent#troubleshooting) may be needed.


### Debug Logs

To set Scout's log level to debug, set the [SCOUT_LOG_LEVEL](/docs/node/configuration) configuration to `debug`.


# Troubleshooting

## No Data
### APM
Not seeing any data?

Using Heroku? View our [Heroku-specific troubleshooting instructions.](https://devcenter.heroku.com/articles/scout#troubleshooting)

**i.** Is [monitoring enabled](/docs/ruby/configuration#monitor) for your environment?

Sometimes this can be deliberately disabled for environments that you are intending to
test.

**1.** Is there a `log/scout_apm.log` file?

**Yes:**



Examine the log file for error messages:

```bash
tail -n1000 log/scout_apm.log | grep "Starting monitoring" -A20
```

See something noteworthy? Proceed to to the last step (#step 7). Otherwise, continue to step 2.

**No:**

The gem was never initialized by the application.

Ensure that the `scout_apm` gem is not restricted to a specific `group` in your `Gemfile`. For example, the configuration below would prevent `scout_apm` from loading in a `staging` environment:

```ruby
group :production do
  gem 'unicorn'
  gem 'scout_apm'
end
```
Jump to the last step (#step 7) if `scout_apm` is correctly configured in your `Gemfile`.

**2.** Set `log_level: debug` in your scout_apm.yml file, or `SCOUT_LOG_LEVEL=debug` if using environment variable, and restart your application.

Examine the log file for error messages:

```bash
tail -n1000 log/scout_apm.log
```

**3.** Was the `**scout_apm**` gem deployed with your application?

```bash
bundle list scout_apm
```

**4.** Did you download the config file, placing it in `**config/scout_apm.yml**`?

**5.** Did you restart the app and let it run for a while?

**6.** Are you sure the application has processed any requests?

```bash
tail -n1000 log/production.log | grep "Processing"
```

**7.** Using Unicorn?

Add the `preload_app true` directive to your Unicorn config file. [Read more](https://unicorn.bogomips.org/Unicorn/Configurator.html#method-i-preload_app) in the Unicorn docs.

**8.** Oops! Still not seeing any data? Check out the [GitHub issues](https://github.com/scoutapp/scout_apm_ruby/issues) and [send us an email](mailto:support@scoutapm.com) with the following:

*   Set `log_level: debug` in scout_apm.yml (`SCOUT_LOG_LEVEL=debug` if using environment variables)
*   The last 1000 lines of your `log/scout_apm.log` file, if the file exists:  
    `tail -n1000 log/scout_apm.log`.
*   Your application's gems `bundle list`.
*   Rails version
*   Application Server (examples: Passenger, Thin, etc.)
*   Web Server (examples: Apache, Nginx, etc.)

We typically respond within a couple of hours during the business day.

### Errors

One thing to note is that by default we don't collect errors for `ActiveRecord::RecordNotFound` as well as `ActionController::RoutingError`.

To collect these error types you will need to set [`errors_ignored_exceptions`](/docs/ruby/configuration#errors_ignored_exceptions) to an empty array:
`SCOUT_ERRORS_IGNORED_EXCEPTIONS=[]`

## Significant time spent in "Controller" or "Job"

When viewing a transaction trace, you may see time spent in the "controller" or "job" layers. This is time that falls outside of Scout's default instrumentation.

There are two options for gathering additional instrumentation:

1. [Custom Instrumentation](/docs/ruby/features#custom-instrumentation) - use our API to instrument pieces of code that are potential bottlenecks.
2. [Auto Instruments](/docs/ruby/features#auto-instruments) - Auto Instruments breaks down time spent within the controller layer. Note that Auto Instruments does not instrument background jobs.

## Missing memory metrics

Memory allocation metrics require the following:

* Ruby version 2.1+
* `scout_apm` version 2.0+

If the above requirements are not met, Scout continues to function but does not report allocation-related metrics.

## StackLevelTooDeep error

If you experience a StackLevelTooDeep error, this is due to the way different monitoring tools instrument into the various libraries.

When one library uses `alias_method` and another uses `prepend` depending on the order these gems are initialized, a circular loop can happen.

__There are two ways to fix this__:

1. make sure the `scout_apm` gem is listed in the Gemfile *above* the conflicting gem.

Fixes the StackLevelTooDeep Error:
```ruby
gem 'scout_apm'
gem 'newrelic_rpm'
```

Causes StackLevelTooDeep Error:

```ruby
gem 'newrelic_rpm'
gem 'scout_apm'
```

2. If this does not work, for Ruby agent versions greater than `5.3.0`, set `use_prepend: true` in your config/scout_apm.yaml. For Heroku customers, set `SCOUT_USE_PREPEND=true` in your environment variables.

## SimpleCov Conflict
When [auto instruments](/docs/ruby/features#auto-instruments) is enabled in the test environment (most likely being set in the `defaults` section in your scout_apm.yml file), conflicts may arise with SimpleCov. To fix this issue, [disable auto_instruments in the test environment](/docs/ruby/configuration) in either your scout_apm.yml file or via environment variables.


# Troubleshooting

## Troubleshooting


Not seeing data?

**1.** Examine your log file for any lines that match `Scout`.

Look for:

```bash
[info] Setup ScoutApm.Watcher on ScoutApm.Store
[info] Setup ScoutApm.Watcher on ScoutApm.Config
[info] Setup ScoutApm.Watcher on ScoutApm.PersistentHistogram
[info] Setup ScoutApm.Watcher on ScoutApm.Logger
[info] Setup ScoutApm.Watcher on ScoutApm.Supervisor
```

If none of the above appears, ensure `scout_apm` was added as a dependency. See the first step in the [Elixir install instructions](/elixir/#installation).

**2.** Run `mix scout.test_config` in your terminal to check for any configuration issues

**3.** Is `use ScoutApm.Instrumentation` specified in _every_ controller module you wish to instrument?

This step is frequently missed if you are using multiple controller modules. See the third step in the [Elixir install instructions](/docs/elixir/#installation).

**4.** Still stuck? Email us.

The following process helps us resolve issues faster:

*   Increase the log level of `scout_apm` by setting `log_level: "debug"` in your `config/scout_apm.exs` file and restart your app.
*   Wait five minutes, then email [support@scoutapm.com](mailto:support@scoutapm.com) your log output and the application's `mix.lock` file.

We typically respond within a couple of hours during the business day.

#### Core-Agent
In some cases, debug level logs from the Elixir agent may not be enough, and [trace level core-agent logs](/docs/core-agent#troubleshooting) may be needed.


# Troubleshooting

## Troubleshooting

Not seeing data? [Email support@scoutapm.com](mailto:support@scoutapm.com) with:

* A link to your app within Scout (if applicable)
* Your Python version
* The name of the framework and version you are trying to instrument, e.g. Flask 0.10.
* [Scout debug logs](/docs/python/logging)

We typically respond within a couple of hours during the business day.

### Debug Logs

To obtain debug level logs for Scout, please see the [Python Logging docs](/docs/python/logging)

#### Core-Agent
In some cases, debug level logs from the Python agent may not be enough, and [trace level core-agent logs](/docs/core-agent#troubleshooting) may be needed.

### Request Payloads
In certain cases, knowing the payload that is being sent to the core agent is useful for debugging. To capture the payload (the request), set `SCOUT_LOG_PAYLOAD_CONTENT=true`

