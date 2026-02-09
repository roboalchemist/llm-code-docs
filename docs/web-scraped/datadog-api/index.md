# Source: https://docs.datadoghq.com/api/latest/

## [API Reference](https://docs.datadoghq.com/api/latest/?tab=java#api-reference)
The Datadog API is an HTTP REST API. The API uses resource-oriented URLs to call the API, uses status codes to indicate the success or failure of requests, returns JSON from all requests, and uses standard HTTP response codes. Use the Datadog API to access the Datadog platform programmatically.
### [Getting started](https://docs.datadoghq.com/api/latest/?tab=java#getting-started)
Authenticate to the API with an [API key](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) using the header `DD-API-KEY`. For some endpoints, you also need an [Application key](https://docs.datadoghq.com/account_management/api-app-keys/#application-keys), which uses the header `DD-APPLICATION-KEY`.
To try out the API [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/20651290-809b13c1-4ada-46c1-af65-ab276c434068?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D20651290-809b13c1-4ada-46c1-af65-ab276c434068%26entityType%3Dcollection%26workspaceId%3Dbf049f54-c695-4e91-b879-0cad1854bafa)
**Note** : To authenticate to the Datadog API through Postman, add your Datadog API and Application key values to the **Collection variables** of the Datadog API collection.
[Using the API](https://docs.datadoghq.com/api/v1/using-the-api/) is a guide to the endpoints.
**Notes** :
  * Add your API and application key values to the **Variables** tab of the Datadog API Collection.
  * cURL code examples assume usage of BASH and GNU coreutils. On macOS, you can install coreutils with the [Homebrew package manager](https://brew.sh): `brew install coreutils`


### [Client libraries](https://docs.datadoghq.com/api/latest/?tab=java#client-libraries)
By default, the Datadog API Docs show examples in cURL. Select one of our official [client libraries](https://docs.datadoghq.com/developers/community/libraries/) languages in each endpoint to see code examples from that library. To install each library:
  * [Java](https://docs.datadoghq.com/api/latest/?tab=java)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/?tab=java)
  * [Python](https://docs.datadoghq.com/api/latest/?tab=java)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/?tab=java)
  * [Ruby](https://docs.datadoghq.com/api/latest/?tab=java)
  * [Go](https://docs.datadoghq.com/api/latest/?tab=java)
  * [Typescript](https://docs.datadoghq.com/api/latest/?tab=java)
  * [Rust](https://docs.datadoghq.com/api/latest/?tab=java)


#### Installation
Maven - Add this dependency to your project’s POM:
```
<dependency>
  <groupId>com.datadoghq</groupId>
  <artifactId>datadog-api-client</artifactId>
  <version>2.48.0</version>
  <scope>compile</scope>
</dependency>

```

Gradle - Add this dependency to your project’s build file:
```
compile "com.datadoghq:datadog-api-client:2.48.0"

```

#### Usage
```
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.Configuration;
import com.datadog.api.<VERSION>.client.api.*;
import com.datadog.api.<VERSION>.client.model.*;

```

**Note** : Replace `<VERSION>` with v1 or v2, depending on which endpoints you want to use.
#### Examples
Maven `pom.xml` for running examples:
```
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>example</artifactId>
  <version>1</version>
  <dependencies>
    <dependency>
      <groupId>com.datadoghq</groupId>
      <artifactId>datadog-api-client</artifactId>
      <version>2.48.0</version>
      <scope>compile</scope>
    </dependency>
  </dependencies>
</project>

```

Make sure that `CLASSPATH` variable contains all dependencies.
```
export CLASSPATH=$(mvn -q exec:exec -Dexec.executable=echo -Dexec.args="%classpath")

```

Gradle `build.gradle` for running examples:
```
plugins {
    id 'java'
    id 'application'
}

repositories {
    jcenter()
}

dependencies {
    implementation 'com.datadoghq:datadog-api-client:2.48.0'
}

application {
    mainClassName = 'Example.java'
}

```

Execute example by running `gradle run` command.
#### Installation
```
pip install datadog

```

#### Usage
```
import datadog

```

#### Installation
```
pip3 install datadog-api-client

```

#### Usage
```
import datadog_api_client

```

#### Installation
```
gem install dogapi

```

#### Usage
```
require 'dogapi'

```

#### Installation
```
gem install datadog_api_client -v 2.47.0

```

#### Usage
```
require 'datadog_api_client'

```

#### Installation
```
go mod init main && go get github.com/DataDog/datadog-api-client-go/v2/api/datadog

```

#### Usage
```
import (
        "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
        "github.com/DataDog/datadog-api-client-go/v2/api/datadog<VERSION>"
)

```

**Note** : Replace `<VERSION>` with `V1` or `V2`, depending on which endpoints you want to use.
#### Installation
The package is under [@datadog/datadog-api-client](https://www.npmjs.com/package/@datadog/datadog-api-client) and can be installed through NPM or Yarn:
```
# NPM
npm install @datadog/datadog-api-client

# Yarn
yarn add @datadog/datadog-api-client

```

#### Usage
```
import { <VERSION> } from 'datadog-api-client';

```

**Note** : Replace `<VERSION>` with v1 or v2, depending on which endpoints you want to use.
#### Installation
Run `cargo add datadog-api-client`, or add the following to `Cargo.toml` under `[dependencies]`:
```
datadog-api-client = "0"

```

#### Usage
Try the following snippet to validate your Datadog API key:
```
use datadog_api_client::datadog::Configuration;
use datadog_api_client::datadogV1::api_authentication::AuthenticationAPI;

#[tokio::main]
async fn main() {
    let configuration = Configuration::new();
    let api = AuthenticationAPI::with_config(configuration);
    let resp = api.validate().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Or check out the libraries directly:
[](https://github.com/DataDog/datadog-api-client-java)
[](https://github.com/DataDog/datadog-api-client-python)
[](https://github.com/DataDog/datadog-api-client-ruby)
[](https://github.com/DataDog/datadog-api-client-go)
[](https://github.com/DataDog/datadog-api-client-typescript)
[](https://github.com/DataDog/datadog-api-client-rust)
  
Trying to get started with the application instead? Check out Datadog’s general [Getting Started docs](https://docs.datadoghq.com/getting_started/application/).
## [Further reading](https://docs.datadoghq.com/api/latest/?tab=java#further-reading)
Additional helpful documentation, links, and articles:
[Using the APIDOCUMENTATION ](https://docs.datadoghq.com/api/latest/using-the-api/)[Authorization ScopesDOCUMENTATION ](https://docs.datadoghq.com/api/latest/scopes/)[Rate LimitsDOCUMENTATION ](https://docs.datadoghq.com/api/latest/rate-limits/)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4ad43077-e978-4dcf-b35d-7501c3c75011&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f27da7c9-3587-4515-9d64-f023062d9b50&pt=API%20Reference&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2F%3Ftab%3Djava&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4ad43077-e978-4dcf-b35d-7501c3c75011&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f27da7c9-3587-4515-9d64-f023062d9b50&pt=API%20Reference&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2F%3Ftab%3Djava&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=bd62d6d3-f0d6-4cb0-b8a8-e8af34396a3b&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=API%20Reference&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2F%3Ftab%3Djava&r=&lt=873&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=468350)
