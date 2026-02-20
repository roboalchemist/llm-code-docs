# Source: https://selenium.dev/documentation/grid/advanced_features/external_datastore/

Title: External datastore

URL Source: https://selenium.dev/documentation/grid/advanced_features/external_datastore/

Markdown Content:
External datastore | Selenium
===============
[](https://selenium.dev/)

*   [About](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#)[About Selenium](https://selenium.dev/about)[Structure and Governance](https://selenium.dev/project)[Events](https://selenium.dev/events)[Ecosystem](https://selenium.dev/ecosystem)[History](https://selenium.dev/history)[Get Involved](https://selenium.dev/getinvolved)[Sponsors](https://selenium.dev/sponsors)[Sponsor Us](https://selenium.dev/sponsor) 
*   [Downloads](https://selenium.dev/downloads)
*   [Documentation](https://selenium.dev/documentation)
*   [Projects](https://selenium.dev/projects)
*   [Support](https://selenium.dev/support)
*   [Blog](https://selenium.dev/blog)
*   
[English](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#)
    *   [Português (Brasileiro)](https://selenium.dev/pt-br/documentation/grid/advanced_features/external_datastore/)
    *   [中文简体](https://selenium.dev/zh-cn/documentation/grid/advanced_features/external_datastore/)
    *   [日本語](https://selenium.dev/ja/documentation/grid/advanced_features/external_datastore/)

Search K

#### Registrations Open for SeleniumConf 2026 | May 06–08 | Join Us In-Person! [Register now!](https://seleniumconf.com/register/?utm_medium=Referral&utm_source=selenium.dev&utm_campaign=register)

Search K

[English](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#)
*   [Português (Brasileiro)](https://selenium.dev/pt-br/documentation/grid/advanced_features/external_datastore/)
*   [中文简体](https://selenium.dev/zh-cn/documentation/grid/advanced_features/external_datastore/)
*   [日本語](https://selenium.dev/ja/documentation/grid/advanced_features/external_datastore/)

*   [Documentation](https://selenium.dev/documentation/ "The Selenium Browser Automation Project")
    *   [Overview](https://selenium.dev/documentation/overview/ "Selenium Overview")
        *   [Components](https://selenium.dev/documentation/overview/components/ "Selenium components")
        *   [Details](https://selenium.dev/documentation/overview/details/ "A deeper look at Selenium")

    *   [WebDriver](https://selenium.dev/documentation/webdriver/)
        *   [Getting Started](https://selenium.dev/documentation/webdriver/getting_started/ "Getting started")
            *   [Install Library](https://selenium.dev/documentation/webdriver/getting_started/install_library/ "Install a Selenium library")
            *   [First Script](https://selenium.dev/documentation/webdriver/getting_started/first_script/ "Write your first Selenium script")
            *   [Using Selenium](https://selenium.dev/documentation/webdriver/getting_started/using_selenium/ "Organizing and Executing Selenium Code")

        *   [Drivers](https://selenium.dev/documentation/webdriver/drivers/ "Driver Sessions")
            *   [Options](https://selenium.dev/documentation/webdriver/drivers/options/ "Browser Options")
            *   [HTTP Client](https://selenium.dev/documentation/webdriver/drivers/http_client/ "HTTP Client Configuration")
            *   [Service](https://selenium.dev/documentation/webdriver/drivers/service/ "Driver Service Class")
            *   [Remote WebDriver](https://selenium.dev/documentation/webdriver/drivers/remote_webdriver/)

        *   [Browsers](https://selenium.dev/documentation/webdriver/browsers/ "Supported Browsers")
            *   [Chrome](https://selenium.dev/documentation/webdriver/browsers/chrome/ "Chrome specific functionality")
            *   [Edge](https://selenium.dev/documentation/webdriver/browsers/edge/ "Edge specific functionality")
            *   [Firefox](https://selenium.dev/documentation/webdriver/browsers/firefox/ "Firefox specific functionality")
            *   [Internet Explorer](https://selenium.dev/documentation/webdriver/browsers/internet_explorer/ "IE specific functionality")
            *   [Safari](https://selenium.dev/documentation/webdriver/browsers/safari/ "Safari specific functionality")

        *   [Waits](https://selenium.dev/documentation/webdriver/waits/ "Waiting Strategies")
        *   [Elements](https://selenium.dev/documentation/webdriver/elements/ "Web elements")
            *   [Locators](https://selenium.dev/documentation/webdriver/elements/locators/ "Locator strategies")
            *   [Finders](https://selenium.dev/documentation/webdriver/elements/finders/ "Finding web elements")
            *   [Interactions](https://selenium.dev/documentation/webdriver/elements/interactions/ "Interacting with web elements")
            *   [Information](https://selenium.dev/documentation/webdriver/elements/information/ "Information about web elements")
            *   [File Upload](https://selenium.dev/documentation/webdriver/elements/file_upload/)

        *   [Interactions](https://selenium.dev/documentation/webdriver/interactions/ "Browser interactions")
            *   [Navigation](https://selenium.dev/documentation/webdriver/interactions/navigation/ "Browser navigation")
            *   [Alerts](https://selenium.dev/documentation/webdriver/interactions/alerts/ "JavaScript alerts, prompts and confirmations")
            *   [Cookies](https://selenium.dev/documentation/webdriver/interactions/cookies/ "Working with cookies")
            *   [Frames](https://selenium.dev/documentation/webdriver/interactions/frames/ "Working with IFrames and frames")
            *   [Print Page](https://selenium.dev/documentation/webdriver/interactions/print_page/)
            *   [Windows](https://selenium.dev/documentation/webdriver/interactions/windows/ "Working with windows and tabs")
            *   [Virtual Authenticator](https://selenium.dev/documentation/webdriver/interactions/virtual_authenticator/)

        *   [Actions API](https://selenium.dev/documentation/webdriver/actions_api/)
            *   [Keyboard](https://selenium.dev/documentation/webdriver/actions_api/keyboard/ "Keyboard actions")
            *   [Mouse](https://selenium.dev/documentation/webdriver/actions_api/mouse/ "Mouse actions")
            *   [Pen](https://selenium.dev/documentation/webdriver/actions_api/pen/ "Pen actions")
            *   [Wheel](https://selenium.dev/documentation/webdriver/actions_api/wheel/ "Scroll wheel actions")

        *   [BiDi](https://selenium.dev/documentation/webdriver/bidi/ "BiDirectional functionality")
            *   [Logging](https://selenium.dev/documentation/webdriver/bidi/logging/ "WebDriver BiDi Logging Features")
            *   [Network](https://selenium.dev/documentation/webdriver/bidi/network/ "WebDriver BiDi Network Features")
            *   [Script](https://selenium.dev/documentation/webdriver/bidi/script/ "WebDriver BiDi Script Features")
            *   [CDP](https://selenium.dev/documentation/webdriver/bidi/cdp/ "Chrome DevTools Protocol")
                *   [Logging](https://selenium.dev/documentation/webdriver/bidi/cdp/logging/ "Chrome DevTools Logging Features")
                *   [Network](https://selenium.dev/documentation/webdriver/bidi/cdp/network/ "Chrome DevTools Network Features")
                *   [Script](https://selenium.dev/documentation/webdriver/bidi/cdp/script/ "Chrome DevTools Script Features")

            *   [W3C](https://selenium.dev/documentation/webdriver/bidi/w3c/ "BiDirectional API (W3C compliant)")
                *   [Browsing Context](https://selenium.dev/documentation/webdriver/bidi/w3c/browsing_context/)
                *   [Input](https://selenium.dev/documentation/webdriver/bidi/w3c/input/)
                *   [Log](https://selenium.dev/documentation/webdriver/bidi/w3c/log/)
                *   [Network](https://selenium.dev/documentation/webdriver/bidi/w3c/network/)
                *   [Script](https://selenium.dev/documentation/webdriver/bidi/w3c/script/)

        *   [Support Features](https://selenium.dev/documentation/webdriver/support_features/ "Support features")
            *   [Expected Conditions](https://selenium.dev/documentation/webdriver/support_features/expected_conditions/ "Waiting with Expected Conditions")
            *   [Listeners](https://selenium.dev/documentation/webdriver/support_features/listeners/ "Command Listeners")
            *   [Colors](https://selenium.dev/documentation/webdriver/support_features/colors/ "Working With Colors")
            *   [Select Lists](https://selenium.dev/documentation/webdriver/support_features/select_lists/ "Working with select list elements")
            *   [ThreadGuard](https://selenium.dev/documentation/webdriver/support_features/thread_guard/)

        *   [Troubleshooting](https://selenium.dev/documentation/webdriver/troubleshooting/ "Troubleshooting Assistance")
            *   [Errors](https://selenium.dev/documentation/webdriver/troubleshooting/errors/ "Understanding Common Errors")
                *   [Driver Location](https://selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/ "Unable to Locate Driver Error")

            *   [Logging](https://selenium.dev/documentation/webdriver/troubleshooting/logging/ "Logging Selenium commands")
            *   [Upgrade to Selenium 4](https://selenium.dev/documentation/webdriver/troubleshooting/upgrade_to_selenium_4/)

    *   [Selenium Manager](https://selenium.dev/documentation/selenium_manager/ "Selenium Manager (Beta)")
    *   [Grid](https://selenium.dev/documentation/grid/)
        *   [Getting Started](https://selenium.dev/documentation/grid/getting_started/ "Getting started with Selenium Grid")
        *   [When to Use Grid](https://selenium.dev/documentation/grid/applicability/)
        *   [Components](https://selenium.dev/documentation/grid/components/ "Selenium Grid Components")
        *   [Configuration](https://selenium.dev/documentation/grid/configuration/ "Configuration of Components")
            *   [Help](https://selenium.dev/documentation/grid/configuration/help/ "Configuration help")
            *   [CLI Options](https://selenium.dev/documentation/grid/configuration/cli_options/ "CLI options in the Selenium Grid")
            *   [TOML Options](https://selenium.dev/documentation/grid/configuration/toml_options/ "TOML configuration options")

        *   [Architecture](https://selenium.dev/documentation/grid/architecture/ "Grid architecture")
        *   [Advanced Features](https://selenium.dev/documentation/grid/advanced_features/ "Advanced features of Selenium")
            *   [Observability](https://selenium.dev/documentation/grid/advanced_features/observability/ "Observability in Selenium Grid")
            *   [GraphQL Support](https://selenium.dev/documentation/grid/advanced_features/graphql_support/ "GraphQL query support")
            *   [Endpoints](https://selenium.dev/documentation/grid/advanced_features/endpoints/ "Grid endpoints")
            *   [Customize Node](https://selenium.dev/documentation/grid/advanced_features/customize_node/ "Customizing a Node")
            *   [External datastore](https://selenium.dev/documentation/grid/advanced_features/external_datastore/)

    *   [IE Driver Server](https://selenium.dev/documentation/ie_driver_server/)
        *   [Internals](https://selenium.dev/documentation/ie_driver_server/internals/ "Internet Explorer Driver Internals")

    *   [IDE](https://selenium.dev/documentation/ide/ "Selenium IDE")
    *   [Test Practices](https://selenium.dev/documentation/test_practices/)
        *   [Design Strategies](https://selenium.dev/documentation/test_practices/design_strategies/ "Design patterns and development strategies")
        *   [Overview](https://selenium.dev/documentation/test_practices/overview/ "Overview of Test Automation")
        *   [Testing Types](https://selenium.dev/documentation/test_practices/testing_types/ "Types of Testing")
        *   [Encouraged](https://selenium.dev/documentation/test_practices/encouraged/ "Encouraged behaviors")
            *   [Page object models](https://selenium.dev/documentation/test_practices/encouraged/page_object_models/)
            *   [Domain specific language](https://selenium.dev/documentation/test_practices/encouraged/domain_specific_language/)
            *   [Generating application state](https://selenium.dev/documentation/test_practices/encouraged/generating_application_state/)
            *   [Mock external services](https://selenium.dev/documentation/test_practices/encouraged/mock_external_services/)
            *   [Improved reporting](https://selenium.dev/documentation/test_practices/encouraged/improved_reporting/)
            *   [Avoid sharing state](https://selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/)
            *   [Locators](https://selenium.dev/documentation/test_practices/encouraged/locators/ "Tips on working with locators")
            *   [Test independency](https://selenium.dev/documentation/test_practices/encouraged/test_independency/)
            *   [Consider using a fluent API](https://selenium.dev/documentation/test_practices/encouraged/consider_using_a_fluent_api/)
            *   [Fresh browser per test](https://selenium.dev/documentation/test_practices/encouraged/fresh_browser_per_test/)

        *   [Discouraged](https://selenium.dev/documentation/test_practices/discouraged/ "Discouraged behaviors")
            *   [Captchas](https://selenium.dev/documentation/test_practices/discouraged/captchas/)
            *   [File downloads](https://selenium.dev/documentation/test_practices/discouraged/file_downloads/)
            *   [HTTP response codes](https://selenium.dev/documentation/test_practices/discouraged/http_response_codes/)
            *   [Gmail, email and Facebook](https://selenium.dev/documentation/test_practices/discouraged/gmail_email_and_facebook_logins/ "Gmail, email and Facebook logins")
            *   [Test dependency](https://selenium.dev/documentation/test_practices/discouraged/test_dependency/)
            *   [Performance testing](https://selenium.dev/documentation/test_practices/discouraged/performance_testing/)
            *   [Link spidering](https://selenium.dev/documentation/test_practices/discouraged/link_spidering/)
            *   [Two Factor Authentication](https://selenium.dev/documentation/test_practices/discouraged/two_factor_authentication/)

    *   [Legacy](https://selenium.dev/documentation/legacy/)
        *   [Selenium 1](https://selenium.dev/documentation/legacy/selenium_1/ "Selenium RC (Selenium 1)")
        *   [Selenium 2](https://selenium.dev/documentation/legacy/selenium_2/)
            *   [Upgrading](https://selenium.dev/documentation/legacy/selenium_2/upgrading/ "Migrating from RC to WebDriver")
            *   [Emulations](https://selenium.dev/documentation/legacy/selenium_2/emulation/ "Backing Selenium with WebDriver")
            *   [Firefox Driver](https://selenium.dev/documentation/legacy/selenium_2/firefox_driver/ "Legacy Firefox Driver")
            *   [Grid 2](https://selenium.dev/documentation/legacy/selenium_2/grid_2/ "Selenium grid 2")
            *   [Grid Platforms](https://selenium.dev/documentation/legacy/selenium_2/grid_platforms/ "History of Grid Platforms")
            *   [Remote Server](https://selenium.dev/documentation/legacy/selenium_2/remote_server/ "Remote WebDriver standalone server")
            *   [Parallel Execution](https://selenium.dev/documentation/legacy/selenium_2/parallel_execution/ "Limitations of scaling up tests in Selenium 2")
            *   [Focus Stealing](https://selenium.dev/documentation/legacy/selenium_2/focus_stealing/ "Stealing focus from Firefox in Linux")
            *   [SSL Certs](https://selenium.dev/documentation/legacy/selenium_2/ssl_certs/ "Untrusted SSL Certificates")
            *   [Mobile](https://selenium.dev/documentation/legacy/selenium_2/mobile/ "WebDriver For Mobile Browsers")
            *   [FAQ](https://selenium.dev/documentation/legacy/selenium_2/faq/ "Frequently Asked Questions for Selenium 2")
            *   [Team](https://selenium.dev/documentation/legacy/selenium_2/team/ "Selenium 2.0 Team")

        *   [Selenium 3](https://selenium.dev/documentation/legacy/selenium_3/)
            *   [Grid 3](https://selenium.dev/documentation/legacy/selenium_3/grid_3/)
            *   [Grid Setup](https://selenium.dev/documentation/legacy/selenium_3/grid_setup/ "Setting up your own Grid 3")
            *   [Grid Components](https://selenium.dev/documentation/legacy/selenium_3/grid_components/ "Components of Grid 3")

        *   [Selenium IDE](https://selenium.dev/documentation/legacy/selenium_ide/ "Legacy Selenium IDE")
            *   [HTML Runner](https://selenium.dev/documentation/legacy/selenium_ide/html_runner/ "HTML runner")
            *   [Releases](https://selenium.dev/documentation/legacy/selenium_ide/releases/ "Legacy Selenium IDE Release Notes")

        *   [JSON Wire Protocol](https://selenium.dev/documentation/legacy/json_wire_protocol/ "JSON Wire Protocol Specification")
        *   [Desired Capabilities](https://selenium.dev/documentation/legacy/desired_capabilities/ "Legacy Selenium Desired Capabilities")
        *   [Developers](https://selenium.dev/documentation/legacy/developers/ "Legacy developer documentation")
            *   [Crazy Fun](https://selenium.dev/documentation/legacy/developers/crazy_fun_build/ "Crazy Fun Build Tool")
            *   [Buck](https://selenium.dev/documentation/legacy/developers/buck/ "Buck Build Tool")
            *   [Drivers](https://selenium.dev/documentation/legacy/developers/drivers/ "Adding new drivers to Selenium 2 code")
            *   [CI Tool](https://selenium.dev/documentation/legacy/developers/ci_tool/ "Selenium's Continuous Integration Implementation")
            *   [Summer of Code](https://selenium.dev/documentation/legacy/developers/summer_of_code/ "Google Summer of Code 2011")
            *   [Tips](https://selenium.dev/documentation/legacy/developers/tips/ "Developer Tips")
            *   [Roadmap](https://selenium.dev/documentation/legacy/developers/roadmap/ "Snapshot of Roadmaps for Selenium Releases")

    *   [About](https://selenium.dev/documentation/about/ "About this documentation")
        *   [Copyright](https://selenium.dev/documentation/about/copyright/ "Copyright and attributions")
        *   [Contributing](https://selenium.dev/documentation/about/contributing/ "Contributing to the Selenium site & documentation")
        *   [Style](https://selenium.dev/documentation/about/style/ "Style guide for Selenium documentation")
        *   [History](https://selenium.dev/documentation/about/history/ "Musings about how things came to be")

[Edit this page](https://github.com/SeleniumHQ/seleniumhq.github.io/edit/trunk/website_and_docs/content/documentation/grid/advanced_features/external_datastore.en.md)[Create documentation issue](https://github.com/SeleniumHQ/seleniumhq.github.io/issues/new?title=External%20datastore)[Create project issue](https://github.com/seleniumhq/selenium/issues/new)[Print entire section](https://www.selenium.dev/_print/documentation/grid/advanced_features/)

* * *

*   [Table of Contents](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#table-of-contents)
*   [Introduction](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#introduction)
*   [Setup](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#setup)
*   [Database backed Session Map](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#database-backed-session-map)
    *   [Steps](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#steps)

*   [Redis backed Session Map](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#redis-backed-session-map)
    *   [Steps](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#steps-1)

* * *

1.   [Documentation](https://www.selenium.dev/documentation/)
2.   [Grid](https://www.selenium.dev/documentation/grid/)
3.   [Advanced Features](https://www.selenium.dev/documentation/grid/advanced_features/)
4.   [External datastore](https://www.selenium.dev/documentation/grid/advanced_features/external_datastore/)

v4.0

External datastore
==================

Table of Contents
-----------------

*   [Introduction](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#introduction)
*   [Setup](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#setup)
*   [Database backed Session Map](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#database-backed-session-map)
    *   [Steps](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#steps)

*   [Redis backed Session Map](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#redis-backed-session-map)
    *   [Steps](https://selenium.dev/documentation/grid/advanced_features/external_datastore/#steps)

Introduction
------------

Selenium Grid allows you to persist information related to currently running sessions into an external data store. The external data store could be backed by your favourite database (or) Redis Cache system.

Setup
-----

*   [Coursier](https://get-coursier.io/docs/cli-installation) - As a dependency resolver, so that we can download maven artifacts on the fly and make them available in our classpath
*   [Docker](https://docs.docker.com/engine/install/) - To manage our PostGreSQL/Redis docker containers.

Database backed Session Map
---------------------------

For the sake of this illustration, we are going to work with PostGreSQL database.

We will spin off a PostGreSQL database as a docker container using a docker compose file.

### Steps

You can skip this step if you already have a PostGreSQL database instance available at your disposal.

*   Create a sql file named `init.sql` with the below contents:

```sql
CREATE TABLE IF NOT EXISTS sessions_map(
    session_ids varchar(256),
    session_caps text,
    session_uri varchar(256),
    session_stereotype text,
    session_start varchar(256)
 );
```

Copy

*   In the same directory as the `init.sql`, create a file named `docker-compose.yml` with its contents as below:

```yaml
version: '3.8'
services:
  db:
    image: postgres:9.6-bullseye
    restart: always
    environment:
      - POSTGRES_USER=seluser
      - POSTGRES_PASSWORD=seluser
      - POSTGRES_DB=selenium_sessions
    ports:
      - "5432:5432"
    volumes:
    - ./init.sql:/docker-entrypoint-initdb.d/init.sql
```

Copy

We can now start our database container by running:

```bash
docker-compose up -d
```

Copy

_Our database name is `selenium\_sessions` with its username and password set to `seluser`_

If you are working with an already running PostGreSQL DB instance, then you just need to create a database named `selenium_sessions` and the table `sessions_map` using the above mentioned SQL statement.

*   Create a Selenium Grid configuration file named `sessions.toml` with the below contents:

```toml
[sessions]
implementation = "org.openqa.selenium.grid.sessionmap.jdbc.JdbcBackedSessionMap"
jdbc-url = "jdbc:postgresql://localhost:5432/selenium_sessions"
jdbc-user = "seluser"
jdbc-password = "seluser"
```

Copy

_Note:_ If you plan to use an existing PostGreSQL DB instance, then replace `localhost:5432` with the actual host and port number of your instance.

*   Below is a simple shell script (let’s call it `distributed.sh`) that we will use to bring up our distributed Grid.

```bash
SE_VERSION=<current_selenium_version>
JAR_NAME=selenium-server-${SE_VERSION}.jar
PUBLISH="--publish-events tcp://localhost:4442"
SUBSCRIBE="--subscribe-events tcp://localhost:4443"
SESSIONS="--sessions http://localhost:5556"
SESSIONS_QUEUE="--sessionqueue http://localhost:5559"
echo 'Starting Event Bus'
java -jar $JAR_NAME event-bus $PUBLISH $SUBSCRIBE --port 5557 &
echo 'Starting New Session Queue'
java -jar $JAR_NAME sessionqueue --port 5559 &
echo 'Starting Sessions Map'
java -jar $JAR_NAME \
--ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-jdbc:${SE_VERSION} org.postgresql:postgresql:42.3.1) \
sessions $PUBLISH $SUBSCRIBE --port 5556 --config sessions.toml &
echo 'Starting Distributor'
java -jar $JAR_NAME  distributor $PUBLISH $SUBSCRIBE $SESSIONS $SESSIONS_QUEUE --port 5553 --bind-bus false &
echo 'Starting Router'
java -jar $JAR_NAME router $SESSIONS --distributor http://localhost:5553 $SESSIONS_QUEUE --port 4444 &
echo 'Starting Node'
java -jar $JAR_NAME node $PUBLISH $SUBSCRIBE &
```

Copy

*   At this point the current directory should contain the following files:

    *   `docker-compose.yml`
    *   `init.sql`
    *   `sessions.toml`
    *   `distributed.sh`

*   You can now spawn the Grid by running `distributed.sh` shell script and quickly run a test. You will notice that the Grid now stores session information into the PostGreSQL database.

In the line which spawns a `SessionMap` on a machine:

```bash
export SE_VERSION=<current_selenium_version>
java -jar selenium-server-${SE_VERSION}.jar \
--ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-jdbc:${SE_VERSION} org.postgresql:postgresql:42.3.1) \
sessions --publish-events tcp://localhost:4442 \
--subscribe-events tcp://localhost:4443 \
--port 5556 --config sessions.toml
```

Copy

*   The variable names from the above script have been replaced with their actual values for clarity.
*   Remember to substitute `localhost` with the actual hostname of the machine where your `Event-Bus` is running.
*   The arguments being passed to `coursier` are basically the GAV (Group Artifact Version) Maven co-ordinates of:
    *   [selenium-session-map-jdbc](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-session-map-jdbc) which is needed to help us store sessions information in database
    *   [postgresql](https://mvnrepository.com/artifact/org.postgresql/postgresql) which is needed to help us talk PostGreSQL database.

*   `sessions.toml` is the configuration file that we created earlier.

Redis backed Session Map
------------------------

We will spin off a Redis Cache docker container using a docker compose file.

### Steps

You can skip this step if you already have a Redis Cache instance available at your disposal.

*   Create a file named `docker-compose.yml` with its contents as below:

```yaml
version: '3.8'
services:
  redis:
    image: redis:bullseye
    restart: always
    ports:
      - "6379:6379"
```

Copy

We can now start our Redis container by running:

```bash
docker-compose up -d
```

Copy

*   Create a Selenium Grid configuration file named `sessions.toml` with the below contents:

```toml
[sessions]
scheme = "redis"
implementation = "org.openqa.selenium.grid.sessionmap.redis.RedisBackedSessionMap"
hostname = "localhost"
port = 6379
```

Copy

_Note:_ If you plan to use an existing Redis Cache instance, then replace `localhost` and `6379` with the actual host and port number of your instance.

*   Below is a simple shell script (let’s call it `distributed.sh`) that we will use to bring up our distributed grid.

```bash
SE_VERSION=<current_selenium_version>
JAR_NAME=selenium-server-${SE_VERSION}.jar
PUBLISH="--publish-events tcp://localhost:4442"
SUBSCRIBE="--subscribe-events tcp://localhost:4443"
SESSIONS="--sessions http://localhost:5556"
SESSIONS_QUEUE="--sessionqueue http://localhost:5559"
echo 'Starting Event Bus'
java -jar $JAR_NAME event-bus $PUBLISH $SUBSCRIBE --port 5557 &
echo 'Starting New Session Queue'
java -jar $JAR_NAME sessionqueue --port 5559 &
echo 'Starting Session Map'
java -jar $JAR_NAME \
--ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-redis:${SE_VERSION}) \
sessions $PUBLISH $SUBSCRIBE --port 5556 --config sessions.toml &
echo 'Starting Distributor'
java -jar $JAR_NAME  distributor $PUBLISH $SUBSCRIBE $SESSIONS $SESSIONS_QUEUE --port 5553 --bind-bus false &
echo 'Starting Router'
java -jar $JAR_NAME router $SESSIONS --distributor http://localhost:5553 $SESSIONS_QUEUE --port 4444 &
echo 'Starting Node'
java -jar $JAR_NAME node $PUBLISH $SUBSCRIBE &
```

Copy

*   At this point the current directory should contain the following files:

    *   `docker-compose.yml`
    *   `sessions.toml`
    *   `distributed.sh`

*   You can now spawn the Grid by running `distributed.sh` shell script and quickly run a test. You will notice that the Grid now stores session information into the Redis instance. You can perhaps make use of a Redis GUI such as [TablePlus](https://tableplus.com/) to see them (Make sure that you have setup a debug point in your test, because the values will get deleted as soon as the test runs to completion).

In the line which spawns a `SessionMap` on a machine:

```bash
export SE_VERSION=<current_selenium_version>
java -jar selenium-server-${SE_VERSION}.jar \
--ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-redis:${SE_VERSION}) \
sessions --publish-events tcp://localhost:4442 \
--subscribe-events tcp://localhost:4443 \
--port 5556 --config sessions.toml
```

Copy

*   The variable names from the above script have been replaced with their actual values for clarity.
*   Remember to substitute `localhost` with the actual hostname of the machine where your `Event-Bus` is running.
*   The arguments being passed to `coursier` are basically the GAV (Group Artifact Version) Maven co-ordinates of:
    *   [selenium-session-map-redis](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-session-map-redis) which is needed to help us store sessions information in Redis Cache.

*   `sessions.toml` is the configuration file that we created earlier.

Last modified November 15, 2022: [Docs for External Sessions Data store (#1225) (60943504fb8)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/60943504fb8c6a2e992afa291b77199d629f7ed3)

Development Partners
--------------------

[![Image 1: BrowserStack](https://selenium.dev/images/sponsors/browserstack.png)](https://www.browserstack.com/automate?utm_campaign=open-source-sponsor&utm_campaigncode=701OW000009sQwVYAU&utm_medium=partnered&utm_source=seleniumorg)

[![Image 2: Sauce Labs](https://selenium.dev/images/sponsors/saucelabs.png)](https://saucelabs.com/resources/topic-hub/selenium?utm_source=selenium&utm_medium=website&utm_campaign=selenium-sponsorship-fy25)

[![Image 3: TestMu AI (formerly LambdaTest)](https://selenium.dev/images/sponsors/testmu-ai.png)](https://www.testmuai.com/selenium-automation)

Selenium Level Sponsors
-----------------------

[![Image 4: Bright Data](https://selenium.dev/images/sponsors/bright-data.png)](https://brightdata.com/?utm_source=brand&utm_campaign=brnd-mkt_partners_selenium)

[![Image 5: Applitools](https://selenium.dev/images/sponsors/applitools.png)](https://applitools.com/)

[![Image 6: Thordata](https://selenium.dev/images/sponsors/thordata.svg)](https://www.thordata.com/?ls=waOicIkB&lk=selenium)

Support the Selenium Project
----------------------------

Learn more or view the full list of sponsors.

[Learn more](https://selenium.dev/sponsors)

*   [](https://www.linkedin.com/company/4826427/)
*   [](https://x.com/SeleniumHQ)
*   [](https://www.youtube.com/@SeleniumHQProject/)
*   [](https://mastodon.social/@seleniumHQ@fosstodon.org)
*   [](https://bsky.app/profile/seleniumconf.bsky.social)
*   [](https://groups.google.com/group/selenium-users)
*   [](https://www.youtube.com/channel/UCbDlgX_613xNMrDqCe3QNEw)

*   [](mailto:selenium@sfconservancy.org)
*   [](https://github.com/seleniumhq/selenium)
*   [](https://inviter.co/seleniumhq)
*   [](https://web.libera.chat/#selenium)
*   [](https://groups.google.com/g/selenium-developers)

[![Image 7: Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-light.svg)](https://www.netlify.com/)

© 2026 Software Freedom Conservancy All Rights Reserved
[About Selenium](https://selenium.dev/about/)
