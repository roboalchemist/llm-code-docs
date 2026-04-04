# Source: https://swagger.io/docs/open-source-tools/swagger-codegen/codegen-v3/generators

# Swagger Codegen Generators
If the default generator configuration does not meet your needs, you have various options to modify or create new modules or templates.

## Modifying the client library format
Don’t like the default swagger client syntax?  Want a different language supported?  No problem!

Swagger Codegen processes handlebar templates with theHandlebars.javaengine.  You can modify our templates or make your own.

[Handlebars.java](https://github.com/jknack/handlebars.java) Take a look atswagger-codegen-generatorsfor examples. To make your own templates, create your own files and use the-tflag to specify your template folder.  It actually is that easy!

[swagger-codegen-generators](https://github.com/swagger-api/swagger-codegen-generators/tree/master/src/main/resources/handlebars) `-t` ## Making your own codegen modules
If you’re starting a project with a new language and don’t see what you need, Swagger Codegen can help you create a project to generate your own libraries:

```
1java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar meta \2  -o output/myLibrary -n myClientCodegen -p com.my.company.codegen```

This will write, in the folderoutput/myLibrary, all the files you need to get started, including aREADME.md. Once modified and compiled, you can load your library with the codegen and generate clients with your own, custom-rolled logic.

`output/myLibrary` `README.md` You would then compile your library in theoutput/myLibraryfolder withmvn packageand execute the codegen like such:

`output/myLibrary` `mvn package` ```
1java -cp output/myLibrary/target/myClientCodegen-swagger-codegen-1.0.0.jar:modules/swagger-codegen-cli/target/swagger-codegen-cli.jar io.swagger.codegen.v3.cli.SwaggerCodegen```

For Windows users, you will need to use;instead of:in the classpath, e.g.:

`;` `:` ```
1java -cp output/myLibrary/target/myClientCodegen-swagger-codegen-1.0.0.jar;modules/swagger-codegen-cli/target/swagger-codegen-cli.jar io.swagger.codegen.v3.cli.SwaggerCodegen```

Note themyClientCodegenis an option now, and you can use the usual arguments for generating your library:

`myClientCodegen` ```
1java -cp output/myLibrary/target/myClientCodegen-swagger-codegen-1.0.0.jar:modules/swagger-codegen-cli/target/swagger-codegen-cli.jar \2  io.swagger.codegen.v3.cli.SwaggerCodegen generate -l myClientCodegen\3  -i http://petstore.swagger.io/v2/swagger.json \4  -o myClient```

See alsostandalone generator development.

[standalone generator development](https://github.com/swagger-api/swagger-codegen/blob/3.0.0/standalone-gen-dev/standalone-generator-development.md) ## Generating a client from local files
If you don’t want to call your server, you can save the OpenAPI Description files into a directory and pass an argument
to the code generator like this:

```
1-i ./modules/swagger-codegen/src/test/resources/2_0/petstore.json```

`1-i./modules/swagger-codegen/src/test/resources/2_0/petstore.json` Great for creating libraries on your CI server, from theSwagger Editor… or while coding on an airplane ✈️.

[Swagger Editor](http://editor.swagger.io)