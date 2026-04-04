# Source: https://docs.pinot.apache.org/release-1.4.0/integrations/metabase.md

# Source: https://docs.pinot.apache.org/integrations/metabase.md

# Metabase

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FvRCOIDWHw2IHhbzoBlGj%2Fpinot-metabase-driver-logo.png?alt=media&#x26;token=1036feb1-3467-4585-b239-315700733792" alt=""><figcaption></figcaption></figure>

This guide provides step-by-step instructions for setting up Metabase with an Apache Pinot connector. The integration allows you to visualize and explore data stored in Apache Pinot directly within Metabase dashboards.

> Note: This is a preview version. For issues or bug reports, please join slack or file github issue.

The code is available at <https://github.com/startreedata/metabase-pinot-driver> under Apache 2 license.

## Prerequisites

Ensure the following tools are installed on your system:

* Git
* Docker
* Node.js (version 22+)
* Java (version 17+)
* Clojure 1.12.1.1550
* NodeJS 22
* NPM 10
* Yarn 1.22
* Apache Pinot 1.3.0
* Metabase v0.55.7

## QuickStart

### Local Run

* Start Pinot

To be simple, use Pinot docker image to run with quickstart

```bash
docker run -d --name pinot-quickstart -p 9000:9000 -p 8000:8000 -p 8080:8080 apachepinot/pinot:latest  QuickStart -type MULTI_STAGE
```

* Download Metabase

Go to Metabase release page, find the release jar.

This quickstart uses [Metabase v0.55.7](https://github.com/metabase/metabase/releases/tag/v0.55.7) .

JAR download: <https://downloads.metabase.com/v0.55.7.x/metabase.jar>

```bash
mkdir -p /tmp/metabase
cd /tmp/metabase
wget https://downloads.metabase.com/v0.55.7.x/metabase.jar
```

* Download Pinot driver

Pinot plugins are released at <https://github.com/startreedata/metabase-pinot-driver/releases>

This QuickStart uses [Pinot Driver v1.1.0](https://github.com/startreedata/metabase-pinot-driver/releases/tag/v1.1.0)

```bash
mkdir -p /tmp/metabase/plugins
cd /tmp/metabase/plugins
wget -O pinot.metabase-driver.jar  https://github.com/startreedata/metabase-pinot-driver/releases/download/v1.1.0/pinot.metabase-driver-v1.1.0.jar
```

* Start Metabase with Pinot plugin

```bash
cd /tmp/metabase
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

Now everything should come up, you could also find the pinot plugin is loaed from the log:

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FWtIjFRaiNjD6ZHboZIPk%2Fimage.png?alt=media&#x26;token=84996782-ac60-466e-9268-8414a1490135" alt=""><figcaption></figcaption></figure>

Once Metabase is up, go to [http://localhost:3000](http://localhost:3000/) to explore it.

After the login, you can click the right side bar to Add Pinot database:

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FVyYU9VvOd2ydNC2TEr7F%2Fimage.png?alt=media&#x26;token=d97032be-3898-4f3b-b9af-fe72832f15d0" alt=""><figcaption></figcaption></figure>

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FYllnLxnMFfSo4Y8q6UiB%2Fimage.png?alt=media&#x26;token=a939738c-497e-4656-a6c4-911b36f97f63" alt=""><figcaption></figcaption></figure>

After the configuration is done, Metabase will generate some explorations automatically.\\

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FpzFQnnADJ37wQvMxcuZN%2Fimage.png?alt=media&#x26;token=0342ba5d-c3cc-425e-be00-0bda0b5d106a" alt=""><figcaption></figcaption></figure>

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2F5Rm90ewUU46I5s6Eu9RL%2Fimage.png?alt=media&#x26;token=466a0121-af19-481d-be20-d980c48161af" alt=""><figcaption></figcaption></figure>

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FVOBsP6Dbli8586KrXaI6%2Fimage.png?alt=media&#x26;token=a9da9316-b8ee-48f3-a20d-cf167e7cd708" alt=""><figcaption></figcaption></figure>

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fw8jKhYtW3bODWb6q51tl%2Fimage.png?alt=media&#x26;token=b6ebf1da-af29-480e-9607-1ff6cb4a5cee" alt=""><figcaption></figcaption></figure>

### Docker Compose

Copy below `Dockerfile` and `docker-compose.yml` to a directory, e.g. `/tmp/metabase` .

`Dockerfile:`

```docker
FROM metabase/metabase:v0.55.7

RUN mkdir -p /plugins && \
    curl -L -o /plugins/pinot.metabase-driver.jar \
    https://github.com/startreedata/metabase-pinot-driver/releases/download/v1.1.0/pinot.metabase-driver-v1.1.0.jar

ENV MB_PLUGINS_DIR=/plugins
```

`docker-compose.yml:`

```yaml
services:
  metabase:
    build: .
    container_name: metabase-pinot
    ports:
      - "3000:3000"
    environment:
      - MB_PLUGINS_DIR=/plugins
    volumes:
      - metabase_data:/metabase-data
    restart: unless-stopped

volumes:
  metabase_data:

```

Run `docker compose up` to start everything:

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FHxV7xWfjidUBI8qel4O7%2Fimage.png?alt=media&#x26;token=476514d1-20ca-4ea3-bc86-ebf64ef314e8" alt=""><figcaption></figcaption></figure>

## Advanced Options

### Authentication header

Users can enable it by expanding the advanced options, then enable `Authentication header`&#x20;

The supported `Auth Token Type`  is `Basic` or `Bearer` .

&#x20;`Auth Token Value` is a string from your admin.

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2F7NFfzKwJUN9ijSJjvbi2%2Fimage.png?alt=media&#x26;token=96357660-ad4f-412a-ab03-29de86b391b4" alt=""><figcaption></figcaption></figure>
