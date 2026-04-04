# Source: https://swagger.io/docs/open-source-tools/swagger-codegen/codegen-v3/about

# Swagger Codegen
This is the Swagger Codegen project, which allows generation of API client libraries (SDK generation), server stubs and documentation automatically given anOpenAPI Description.

[OpenAPI Description](https://github.com/OAI/OpenAPI-Specification) 💚 If you would like to contribute, please refer toguidelinesand a list ofopen tasks.💚

[guidelines](https://github.com/swagger-api/swagger-codegen/blob/master/CONTRIBUTING.md) [open tasks](https://github.com/swagger-api/swagger-codegen/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) 📔 For more information, please refer to theWiki pageandFAQ📔

[Wiki page](https://github.com/swagger-api/swagger-codegen/wiki) [FAQ](https://github.com/swagger-api/swagger-codegen/wiki/FAQ) ⚠️ If the OpenAPI Description or Swagger file is obtained from an untrusted source, please make sure you’ve reviewed the artefact before using Swagger Codegen to generate the API client, server stub or documentation ascode injectionmay occur. ⚠️

[code injection](https://en.wikipedia.org/wiki/Code_injection) ## Versioning
⚠️ this document refers to version 3.X, checkherefor 2.X.

[here](./../codegen-v2/about) Both 2.X and 3.X version lines of Swagger Codegen are available and are independently maintained.

NOTES:

- Versions 2.X (io.swagger) and 3.X (io.swagger.codegen.v3) havedifferentgroup ids.
`io.swagger` `io.swagger.codegen.v3` - OpenAPI 3.0.X is supported from the 3.X version only
For full versioning info, please refer to theversioning documentation.

[versioning documentation](../versioning) ## Supported Languages and Frameworks
Here’s a summary of the supported languages/frameworks.

- API clients: “csharp”, “csharp-dotnet2”, “dart”, “go”, “java”, “javascript”, “jaxrs-cxf-client”, “kotlin-client”, “php”, “python”, “r”, “ruby” “scala”, “swift3”, “swift4”, “swift5”, “typescript-angular”, “typescript-axios”, “typescript-fetch”
API clients: “csharp”, “csharp-dotnet2”, “dart”, “go”, “java”, “javascript”, “jaxrs-cxf-client”, “kotlin-client”, “php”, “python”, “r”, “ruby” “scala”, “swift3”, “swift4”, “swift5”, “typescript-angular”, “typescript-axios”, “typescript-fetch”

- Server stubs: “aspnetcore”,
“go-server”,
“inflector”,
“java-vertx”,
“jaxrs-cxf”,
“jaxrs-cxf-cdi”,
“jaxrs-di”,
“jaxrs-jersey”,
“jaxrs-resteasy”,
“jaxrs-resteasy-eap”,
“jaxrs-spec”,
“kotlin-server”,
“micronaut”,
“nodejs-server”,
“python-flask”,
“scala-akka-http-server”,
“spring”
Server stubs: “aspnetcore”,
“go-server”,
“inflector”,
“java-vertx”,
“jaxrs-cxf”,
“jaxrs-cxf-cdi”,
“jaxrs-di”,
“jaxrs-jersey”,
“jaxrs-resteasy”,
“jaxrs-resteasy-eap”,
“jaxrs-spec”,
“kotlin-server”,
“micronaut”,
“nodejs-server”,
“python-flask”,
“scala-akka-http-server”,
“spring”

- API documentation generators: “dynamic-html”,
“html”,
“html2”,
“openapi”,
“openapi-yaml”
API documentation generators: “dynamic-html”,
“html”,
“html2”,
“openapi”,
“openapi-yaml”

To get a complete and/or realtime listing of supported languages/frameworks, you can directly query theonline generator APIor via acURLcommand.

[online generator API](https://generator3.swagger.io/index.html#/clients/languages) `cURL` ```
1curl -X 'GET' \2  'https://generator3.swagger.io/api/client/V3' \3  -H 'accept: application/json'```

`1curl -X 'GET' \2'https://generator3.swagger.io/api/client/V3' \3-H 'accept: application/json'` Check out theOpenAPI Specificationfor additional information about the OpenAPI project.

[OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) ## Compatibility
The OpenAPI Specification has undergone 3 revisions since initial creation in 2010.  Thecurrent stableversions of Swagger Codegen project have the following compatibilities with the OpenAPI Specification:

[3.0.71](https://github.com/swagger-api/swagger-codegen/releases/tag/v3.0.71) [tag v3.0.71](https://github.com/swagger-api/swagger-codegen/tree/v3.0.71) [2.4.46](https://github.com/swagger-api/swagger-codegen/releases/tag/v2.4.46) [tag v2.4.46](https://github.com/swagger-api/swagger-codegen/tree/v2.4.46) 💁 Here’s also an overview of what’s coming around the corner:

[SNAPSHOT](https://central.sonatype.com/service/rest/repository/browse/maven-snapshots/io/swagger/codegen/v3/swagger-codegen-cli/3.0.72-SNAPSHOT/) [SNAPSHOT](https://central.sonatype.com/service/rest/repository/browse/maven-snapshots/io/swagger/swagger-codegen-cli/2.4.47-SNAPSHOT/) For detailed breakdown of all versions, please see thefull compatibility listing.

[full compatibility listing](../compatibility) ## Getting Started
To get up and running with Swagger Codegen, check out the following guides and instructions:

- Prerequisites
[Prerequisites](../prerequisites) - Building
[Building](../building) - Using Docker
[Using Docker](../docker) Once you’ve your environment setup, you’re ready to start generating clients and/or servers.

As a quick example, to generate a PHP client forSwagger Petstore, please run the following:

[Swagger Petstore](http://petstore.swagger.io/v2/swagger.json) ```
1git clone https://github.com/swagger-api/swagger-codegen2cd swagger-codegen3git checkout 3.0.04mvn clean package5java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \6   -i http://petstore.swagger.io/v2/swagger.json \7   -l php \8   -o /var/tmp/php_api_client```

Note:if you’re on Windows, replace the last command with:

```
1java -jar modules\swagger-codegen-cli\target\swagger-codegen-cli.jar generate -i http://petstore.swagger.io/v2/swagger.json -l php -o c:\temp\php_api_client```

You can also download the JAR (latest release) directly frommaven.org.

[maven.org](https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.71/swagger-codegen-cli-3.0.71.jar) To get a list ofgeneraloptions available, please run:

```
1java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate --help```

`1java-jarmodules/swagger-codegen-cli/target/swagger-codegen-cli.jargenerate--help` To get a list of PHP specified options (which can be passed to the generator with a config file via the-coption), please run:

`-c` ```
1java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar config-help -l php```

`1java-jarmodules/swagger-codegen-cli/target/swagger-codegen-cli.jarconfig-help-lphp` ## Generators
### To generate a sample client library
You can build a client against the swagger samplepetstoreAPI as follows:

[petstore](http://petstore.swagger.io) ```
1./bin/java-petstore.sh```

`1./bin/java-petstore.sh` On Windows, run.\bin\windows\java-petstore.batinstead.

`.\bin\windows\java-petstore.bat` This will run the generator with this command:

```
1java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \2  -i http://petstore.swagger.io/v2/swagger.json \                               # The location of the Swagger specifcation file (JSON/YAML).3  -l java \                                                                     # The desired language for the library.4  -o samples/client/petstore/java                                               # The output destination.```

You can get the options with thegenerate --helpcommand (below only shows partial results):

`generate --help` ```
1NAME2        swagger-codegen-cli generate - Generate code with chosen lang3
4SYNOPSIS5        swagger-codegen-cli generate6                [(-a <authorization> | --auth <authorization>)]7                [--additional-properties <additional properties>...]8                [--api-package <api package>] [--artifact-id <artifact id>]9                [--artifact-version <artifact version>]10                [(-c <configuration file> | --config <configuration file>)]11                [-D <system properties>...] [--git-repo-id <git repo id>]12                [--git-user-id <git user id>] [--group-id <group id>]13                [--http-user-agent <http user agent>]14                (-i <spec file> | --input-spec <spec file>)15                [--ignore-file-override <ignore file override location>]16                [--import-mappings <import mappings>...]17                [--instantiation-types <instantiation types>...]18                [--invoker-package <invoker package>]19                (-l <language> | --lang <language>)20                [--language-specific-primitives <language specific primitives>...]21                [--library <library>] [--model-name-prefix <model name prefix>]22                [--model-name-suffix <model name suffix>]23                [--model-package <model package>]24                [(-o <output directory> | --output <output directory>)]25                [--release-note <release note>] [--remove-operation-id-prefix]26                [--reserved-words-mappings <reserved word mappings>...]27                [(-s | --skip-overwrite)]28                [(-t <template directory> | --template-dir <template directory>)]29                [--type-mappings <type mappings>...] [(-v | --verbose)]30
31OPTIONS32        -a <authorization>, --auth <authorization>33            adds authorization headers when fetching the swagger definitions34            remotely. Pass in a URL-encoded string of name:header with a comma35            separating multiple values36
37...... (results omitted)38
39        -v, --verbose40            verbose mode```

You can then compile and run the client, as well as unit tests against it:

```
1cd samples/client/petstore/java2mvn package```

`1cdsamples/client/petstore/java2mvnpackage` Other languages have petstore samples, too:

```
1./bin/android-petstore.sh2./bin/java-petstore.sh3./bin/objc-petstore.sh```

`1./bin/android-petstore.sh2./bin/java-petstore.sh3./bin/objc-petstore.sh` ### Generating libraries from your server
It’s just as easy! Use the-iflag to point to either a server or file.

`-i` 🔧 Swagger Codegen comes with a tonne of flexibility to support your code generation preferences. Checkout thegenerators documentationwhich takes you through some of the possibilities as well as showcasing how to generate from local files.

[generators documentation](../generators) ### Selective generation
You may not want to generateallmodels in your project. Likewise you may want just one or two apis to be written, or even ignore certain file formats. If that’s the case check theselective generationinstructions.

[selective generation](../generation-selective) ### Advanced Generator Customization
There are different aspects of customizing the code generator beyond just creating or modifying templates.  Each language has a supporting configuration file to handle different type mappings, or bring your own models. For more information check out theadvanced configuration docs.

[advanced configuration docs](../generators-configuration) ### Validating your OpenAPI Description
You have options. The easiest is to use ouronline validatorwhich not only will let you validate your OpenAPI file, but with the debug flag, you can see what’s wrong with your file. Check outSwagger Validatorto validate a petstore example.

[online validator](https://github.com/swagger-api/validator-badge) [Swagger Validator](http://online.swagger.io/validator/debug?url=http://petstore.swagger.io/v2/swagger.json) If you want to have validation directly on your own machine, thenSpectralis an excellent option.

[Spectral](https://stoplight.io/open-source/spectral) ### Generating dynamic html api documentation
To do so, just use the-l dynamic-htmlflag when reading a spec file.  This creates HTML documentation that is available as a single-page application with AJAX.  To view the documentation:

`-l dynamic-html` ```
1cd samples/dynamic-html/2npm install3node .```

`1cdsamples/dynamic-html/2npminstall3node.` Which launches a node.js server so the AJAX calls have a place to go.

## Workflow Integration
It’s possible to leverage Swagger Codegen directly within your preferred CI/CD workflows to streamline your auto-generation requirements. Check out theworkflows integrationguide to see information on our Maven, Gradle, and GitHub integration options. 🚀

[workflows integration](../workflow-integration) ## Online generators
If you don’t want to run and host your own code generation instance, check our ouronline generatorsinformation.

[online generators](../online-generators) ## Contributing
Please refer to thispage.

[page](https://github.com/swagger-api/swagger-codegen/blob/master/CONTRIBUTING.md) 🚧 Forswagger-codegen version 3templates and classes for code generation are being migrated toswagger-codegen-generatorsrepo. In order to know this migration process you can refer thispage.

`swagger-codegen version 3` [swagger-codegen-generators](https://github.com/swagger-api/swagger-codegen-generators) [page](https://github.com/swagger-api/swagger-codegen/wiki/Swagger-Codegen-migration-(swagger-codegen-generators-repository)) ## Security contact
Please disclose any security-related issues or vulnerabilities by emailingsecurity@swagger.io, instead of using the public issue tracker.

[security@swagger.io](mailto:security@swagger.io) ## Thank You
💚💚💚 We’d like to give a big shout out to all those who’ve contributed to Swagger Codegen, be that in raising issues, fixing bugs, authoring templates, or crafting useful content for others to benefit from. 💚💚💚