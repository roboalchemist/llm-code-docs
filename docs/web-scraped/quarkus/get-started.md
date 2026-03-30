# Source: https://quarkus.io/get-started

Title: Get Started

URL Source: https://quarkus.io/get-started

Markdown Content:
### It’s a snap to be up and running with Quarkus.

Step 1
------

### Install via Command Line Interface

Open your favorite terminal and use JBang to install the Quarkus CLI. You do not need to have Java installed first.

#### For Linux, macOS, and Windows (using WSL or bash compatible shell like Cygwin or MinGW)

```
curl -Ls https://sh.jbang.dev | bash -s - trust add https://repo1.maven.org/maven2/io/quarkus/quarkus-cli/
curl -Ls https://sh.jbang.dev | bash -s - app install --fresh --force quarkus@quarkusio
```

#### For Windows using Powershell

```
iex "& { $(iwr https://ps.jbang.dev) } trust add https://repo1.maven.org/maven2/io/quarkus/quarkus-cli/"
iex "& { $(iwr https://ps.jbang.dev) } app install --fresh --force quarkus@quarkusio"
```

If it's your first time to install, you'll need to restart your shell.

#### Or, you can also install the CLI with SDKMAN!

`sdk install quarkus`

#### For more options, such as Homebrew or Chocolatey, see [the Quarkus CLI guide](https://quarkus.io/guides/cli-tooling).

Step 2
------

### Create the Getting Started Application

Run this script in your CLI:

`quarkus create && cd code-with-quarkus`

Step 3
------

### Run the Getting Started Application

Run this script in your CLI:

`quarkus dev`

#### Boom! Your Quarkus app is now running at `localhost:8080`

Step 4
------

### Live Coding with Quarkus

Quarkus makes it easy to change your code on the fly. Let's modify the [RESTful endpoint](http://localhost:8080/hello)

Open `src/main/java/org/acme/GreetingResource.java` in a text editor or your [favorite IDE](https://quarkus.io/guides/ide-tooling) and change "Hello from RESTEasy Reactive" to "Hola from RESTEasy Reactive". Then refresh the browser and see the changes.

```
@Path("/hello")
public class GreetingResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String hello() {
        return "Hello RESTEasy";
    }
}
```

#### Cool stuff right? [Learn more about Quarkus's dev mode](https://quarkus.io/guides/maven-tooling#dev-mode).

### Next Steps

Building Native Executables

Build native executables with GraalVM or Mandrel.

Continuous Testing

Learn how to use continuous testing in your Quarkus Application.

Start with Serverless

Create a portable Java API to write serverless functions deployable to AWS Lambda, Azure Functions, Knative, and more.

Quarkus Tools in Your Favorite IDE

Every developer has their favorite IDE. Learn how to use Quarkus in yours.

Writing JSON REST services

JSON is now the lingua franca between microservices. See how you can get your REST services to consume and produce JSON payloads.

Getting Started with Reactive

Learn more about developing reactive applications with Quarkus.

Deploying Quarkus Applications on Kubernetes

This guide covers how to deploy a native application on Kubernetes.

#### Want to learn more? Check out the [guides](https://quarkus.io/guides/) to continue your journey.
