# Source: https://docs.fluentd.org/language-bindings/java.md

# Source: https://docs.fluentd.org/0.12/articles/java.md

# Java

The '[fluent-logger-java](http://github.com/fluent/fluent-logger-java)' library is used to post records from Java applications to Fluentd.

This article explains how to use the fluent-logger-java library.

## Prerequisites

* Basic knowledge of Java
* Basic knowledge of Fluentd
* Java 6 or higher

## Installing Fluentd

Please refer to the following documents to install fluentd.

* [Install Fluentd with rpm Package](https://docs.fluentd.org/0.12/articles/install-by-rpm)
* [Install Fluentd with deb Package](https://docs.fluentd.org/0.12/articles/install-by-deb)
* [Install Fluentd with Ruby Gem](https://docs.fluentd.org/0.12/articles/install-by-gem)
* [Install Fluentd from source](https://docs.fluentd.org/0.12/articles/install-from-source)

## Modifying the Config File

Next, please configure Fluentd to use the [forward Input plugin](https://docs.fluentd.org/0.12/articles/broken-reference) as its data source.

```
<source>
  @type forward
  port 24224
</source>
<match fluentd.test.**>
  @type stdout
</match>
```

Please restart your agent once these lines are in place.

```
# for rpm/deb only
$ sudo /etc/init.d/td-agent restart
```

## Using fluent-logger-java

First, please add the following lines to pom.xml. The logger's revision information can be found in [CHANGES.txt](https://github.com/fluent/fluent-logger-java/blob/master/CHANGES.txt).

```
<dependencies>
  ...
  <dependency>
    <groupId>org.fluentd</groupId>
    <artifactId>fluent-logger</artifactId>
    <version>${logger.version}</version>
  </dependency>
  ...
</dependencies>
```

Next, please insert the following lines into your application. Further information regarding the API can be found [here](https://github.com/fluent/fluent-logger-java).

```
import java.util.HashMap;
import java.util.Map;
import org.fluentd.logger.FluentLogger;

public class Main {
    private static FluentLogger LOG = FluentLogger.getLogger("fluentd.test");

    public void doApplicationLogic() {
        // ...
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("from", "userA");
        data.put("to", "userB");
        LOG.log("follow", data);
        // ...
    }
}
```

Executing the script will send the logs to Fluentd.

```
$ java -jar test.jar
```

The logs should be output to `/var/log/td-agent/td-agent.log` or stdout of the Fluentd process via the [stdout Output plugin](https://docs.fluentd.org/0.12/articles/broken-reference).

## Production Deployments

### Output Plugins

Various [output plugins](https://docs.fluentd.org/0.12/articles/broken-reference) are available for writing records to other destinations:

* Examples
  * [Store Apache Logs into Amazon S3](https://docs.fluentd.org/0.12/articles/apache-to-s3)
  * [Store Apache Logs into MongoDB](https://docs.fluentd.org/0.12/articles/apache-to-mongodb)
  * [Data Collection into HDFS](https://docs.fluentd.org/0.12/articles/http-to-hdfs)
* List of Plugin References
  * [Output to Another Fluentd](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [Output to MongoDB](https://docs.fluentd.org/0.12/articles/broken-reference) or [MongoDB ReplicaSet](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [Output to Hadoop](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [Output to File](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [etc...](http://fluentd.org/plugin/)

### High-Availability Configurations of Fluentd

For high-traffic websites (more than 5 application nodes), we recommend using a high availability configuration of td-agent. This will improve data transfer reliability and query performance.

* [High-Availability Configurations of Fluentd](https://docs.fluentd.org/0.12/deployment/high-availability)

### Monitoring

Monitoring Fluentd itself is also important. The article below describes general monitoring methods for td-agent.

* [Monitoring Fluentd](https://docs.fluentd.org/0.12/deployment/monitoring)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
