# Earthly Documentation

Source: https://docs.earthly.dev/llms-full.txt

---

# Introduction

Earthly is a build automation tool from the same era as your code. It allows you to execute all your builds in containers. This makes them self-contained, repeatable, portable and parallel. You can use Earthly to create Docker images and artifacts (e.g. binaries, packages, arbitrary files).

Earthly can run on top of popular CI systems (like [Jenkins](https://docs.earthly.dev/ci-integration/vendor-specific-guides/jenkins), [CircleCI](https://docs.earthly.dev/ci-integration/vendor-specific-guides/circle-integration), [GitHub Actions](https://docs.earthly.dev/ci-integration/vendor-specific-guides/gh-actions-integration), [AWS CodeBuild](https://docs.earthly.dev/ci-integration/vendor-specific-guides/codebuild-integration)). It is typically the layer between language-specific tooling (like maven, gradle, npm, pip, go build) and the CI build spec.

![Earthly fits between language-specific tooling and the CI](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-d10638e4183adfdc7fdff0f61f7aed2d2c055c99%2Fintegration-diagram-v2.png?alt=media\&token=839fbafa-63ae-49b9-92ca-b866c5e8f75b)

Earthly has a number of key features. It has a familiar syntax (it's like Dockerfile and Makefile had a baby). Everything runs on containers, so your builds run the same on your laptop as they run in CI or on your colleague's laptop. Strong isolation also gives you easy to use parallelism, with no strings attached. You can also import dependencies from other directories or other repositories with ease, making Earthly great for large [mono-repo builds](https://github.com/earthly/earthly/tree/main/examples/monorepo) that span a vast directory hierarchy; but also for [multi-repo setups](https://github.com/earthly/earthly/tree/main/examples/multirepo) where builds might depend on each other across repositories.

One of the key principles of Earthly is that the best build tooling of a specific language is built by the community of that language itself. Earthly does not intend to replace that tooling, but rather to leverage and augment it.

## Installation

See [installation instructions](https://earthly.dev/get-earthly).

For a full list of installation options see the [alternative installation page](https://docs.earthly.dev/docs/misc/alt-installation).

## Getting started

If you are new to Earthly, check out the [Basics page](https://docs.earthly.dev/basics), to get started.

A high-level overview is available on [the Earthly GitHub page](https://github.com/earthly/earthly).

## Quick Links

* [Earthly GitHub page](https://github.com/earthly/earthly)
* [Installation instructions](https://earthly.dev/get-earthly)
* [Earthly basics](https://docs.earthly.dev/basics)
* [Earthfile reference](https://docs.earthly.dev/docs/earthfile)
* [Earthly command reference](https://docs.earthly.dev/docs/earthly-command)
* [Configuration reference](https://docs.earthly.dev/docs/earthly-config)
* [Earthfile examples](https://docs.earthly.dev/docs/examples)
* [Best practices](https://docs.earthly.dev/best-practices)

# Learn the basics

Earthly is a build automation tool that uses docker containers to enforce build repeatability. Earthly is meant to be run on your local system and in your CI. Earthly's implicit caching and parallelism will make your builds repeatable and fast.

This tutorial will walk you through a basic example of using Earthly.

* **Introduction** <-- You are here.
* [Part 1: A simple Earthfile](https://docs.earthly.dev/basics/part-1-a-simple-earthfile)
* [Part 2: Outputs](https://docs.earthly.dev/basics/part-2-outputs)
* [Part 3: Adding dependencies With Caching](https://docs.earthly.dev/basics/part-3-adding-dependencies-with-caching)
* [Part 4: Args](https://docs.earthly.dev/basics/part-4-args)
* [Part 5: Importing](https://docs.earthly.dev/basics/part-5-importing)
* [Part 6: Using Docker In Earthly](https://docs.earthly.dev/basics/part-6-using-docker-with-earthly)
* [Final words](https://docs.earthly.dev/basics/final-words)

## Installation

We recommend you install Earthly on your computer, so you can follow along and try the examples. See the [installation instructions](https://earthly.dev/get-earthly).

## Questions & Feedback

If you have any questions, feedback or suggestions for Earthly or this tutorial feel free to reach out to us on our [Slack community](https://earthly.dev/slack) or open a [GitHub issue](https://github.com/earthly/earthly/issues). Earthly is free and open and we love and appreciate feedback and contributions from the community!

## Get Started with Earthly

We will start the first lesson with a simple Earthfile.

👉 [Part 1: A simple Earthfile](https://docs.earthly.dev/basics/part-1-a-simple-earthfile)

# Part 1: A simple Earthfile

Below you'll find a simple example of an Earthfile. All the magic of Earthly happens in the Earthfile, which you may notice is very similar to a Dockerfile. This is an intentional design decision. Existing Dockerfiles can easily be ported to Earthly by copying them to an Earthfile and tweaking them slightly.

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

Throughout this tutorial, we'll build up this example Earthfile from scratch and then add even more to it. By the end you'll have a better grasp of how Earthly works and the power and repeatability it can bring to your build process.

This tutorial focuses on using Earthly with a Go project, but you can find examples of Earthfiles for [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) at the bottom of each page.

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part1/part1 ./part1
```

### Creating Your First Earthfile

We'll slowly build up to the Earthfile we have above. Let's start with these first three lines.

`./tutorial/Earthfile`

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir
```

And some simple Hello World code in a `main.go`.

```go
package main

import "fmt"

func main() {
 fmt.Println("hello world")
}
```

Earthfiles are always named Earthfile, regardless of their location in the codebase. The Earthfile starts off with a version definition. This will tell Earthly which features to enable and which ones not to so that the build script maintains compatibility over time, even if Earthly itself is updated.

The first commands in the file are part of the `base` target and are implicitly inherited by all other targets. Targets are just sets of instructions we can call on from within the Earthfile, or when we run Earthly at the command line. Targets need an environment to run in. These environments come in the form of Docker images. In this case we are saying that all the instructions in our Earthfile will use `golang:1.15-alpine3.13`, [unless we specify otherwise](#target-environments). (More on this in a bit.)

Lastly, we change our working directory to `/go-workdir`.

### Creating Your First Targets

Earthly aims to replace Dockerfile, makefile, bash scripts and more. We can take all the setup, configuration and build steps we'd normally define in those files and put them in our Earthfile in the form of `targets`.

Let's start by defining a target to build our simple Go app. **When we run Earthly, we can tell it to execute a target by passing a plus sign (+) and then the target name.** So we'll be able to run our `build` target with `earthly +build`. More on this in the [Running the Build](#running-the-build) section.

Let's start by breaking down our first target.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example
```

The first thing we do is copy our `main.go` from the **build context** (the directory where the Earthfile resides) to the **build environment** (the containerized environment where Earthly commands are run).

Next, we run a go build command against the previously copied `main.go` file.

Finally, we save the output of the build command as an artifact. The syntax for `SAVE ARTIFACT` defaults the destination path to `/` - so our artifact will be called `/example` (it can be later referenced as `+build/example`). If we wanted to save it at a different path, we could use `SAVE ARTIFACT output/example /some/path/to/example` and refer to it later as `+build/some/path/to/example`.

Now let's create a new target called `+docker`.

```Dockerfile
docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

Here we copy the artifact `/example` produced by another target, `+build`, to the current directory within the build environment. Again this will be the working directory we set up in the `base` target at the beginning of the file. Lastly, we set the entrypoint for the resulting docker image, and then save the image.

You may notice the command `COPY +build/... ...`, which has an unfamiliar form if you're coming from Docker. This is a special type of `COPY`, which can be used to pass artifacts from one target to another. In this case, the target `build` (referenced as `+build`) produces an artifact, which has been declared with `SAVE ARTIFACT`, and the target `docker` copies that artifact in its build environment.

With Earthly you have the ability to pass such artifacts or images between targets within the same Earthfile, but also across different Earthfiles across directories or even across repositories. To read more about this, see the [target, artifact and image referencing guide](https://docs.earthly.dev/docs/guides/target-ref) or jump to [part 5](https://docs.earthly.dev/basics/part-5-importing) of this guide.

Lastly, we save the current state as a docker image, which will have the docker tag `go-example:latest`. This image is only made available to the host's docker if the entire build succeeds.

### Target Environments

Notice how we already had Go installed for both our `+build` and `+docker` targets. This is because targets inherit from the base target which for us was the `FROM golang:1.15-alpine3.13` that we set up at the top of the file. But it's worth noting that targets can define their own environments. For example:

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

npm:
    FROM node:12-alpine3.12
    WORKDIR /src
    RUN npm install
    COPY assets/ .
    RUN npm test
```

In this example, the `+build` target does not have a `FROM`, so it inherits from the base target, `golang:1.15-alpine3.13`.

The target `+npm`, on the other hand, specifies its own environment with the `FROM`command and so will run inside of a `node:12-alpine3.12` container.

### Running the build

In the example `Earthfile` we have defined two explicit targets: `+build` and `+docker`. **We can tell Earthly to execute a target by passing typing a plus sign (+) followed by the target name.** In this case our docker target calls on our build target, so we can run both with:

```bash
earthly +docker
```

The output might look like this:

![Earthly build output](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-cf08377408d70ee4b3c931c21a937b4673901915%2Fgo-example.png?alt=media\&token=0e495fc9-cb73-4395-8faf-50565acdb1df)

Notice how to the left of `|`, within the output, we can see some targets like `+base`, `+build` and `+docker` . Notice how the output is interleaved between `+docker` and `+build`. This is because the system executes independent build steps in parallel. The reason this is possible effortlessly is because only very few things are shared between the builds of the recipes and those things are declared and obvious. The rest is completely isolated.

In addition, notice how even though the base is used as part of both `build` and `docker`, it is only executed once. This is because the system deduplicates execution, where possible.

Furthermore, the fact that the `docker` target depends on the `build` target is visible within the command `COPY +build/...`. Through this command, the system knows that it also needs to build the target `+build`, in order to satisfy the dependency on the artifact.

Finally, notice how the output of the build (the docker image and the files) are only written after the build is declared a success. This is due to another isolation principle of Earthly: a build either succeeds completely or it fails altogether.

Once the build has executed, we can run the resulting docker image to try it out:

```
docker run --rm go-example:latest

# or podman
podman run --rm go-example:latest
```

#### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part1/part1 ./part1
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

build:
    # In JS, there's nothing to build in this simple form.
    # The source is also the artifact used in production.
    COPY src/index.js .
    SAVE ARTIFACT index.js /dist/index.js

docker:
    COPY +build/dist dist
    ENTRYPOINT ["node", "./dist/index.js"]
    SAVE IMAGE js-example:latest
```

The code of the app might look like this

`./src/index.js`

```js
console.log("hello world");
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part1/part1 ./part1
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    COPY build.gradle ./
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin /bin
    SAVE ARTIFACT build/install/java-example/lib /lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:latest
```

The code of the app might look like this

`./src/main/java/hello/HelloWorld.java`

```java

package hello;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

`./build.gradle`

```groovy
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'hello.HelloWorld'

jar {
    baseName = 'hello-world'
    version = '0.0.1'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part1/part1 ./part1
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM python:3
WORKDIR /code

build:
     # In Python, there's nothing to build.
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +build/src src
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:latest
```

The code of the app might look like this

`./src/hello.py`

```python
print("hello world")
```

</details>

# Part 2: Outputs

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part2) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part2/part2 ./part2
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Not All Targets Produce Output

Targets have the ability to produce output outside of the build environment. You can save files and docker images to your local machine or push them to remote repositories. Targets can also run commands that affect the local environment outside of the build, such as running database migrations, but not all targets produce output. Let's take a look at which commands produce output and how to use them.

### Saving Files

We've already seen how the command [SAVE ARTIFACT](https://docs.earthly.dev/docs/earthfile#save-artifact) copies a file or directory from the build environment into the target's artifact environment.

This gives us the ability to copy files between targets, **but it does not allow us to save any files to our local machine.**

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example

docker:
    #  COPY command copies files from the +build target
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

In order to **save the file locally** , we need to add `AS LOCAL` to the command.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

If we run this example with `earthly +build`, we'll see a `local-output` directory show up locally with a `go-example` file inside of it.

### Saving Docker Images

Saving Docker images to your local machine is easy with the `SAVE IMAGE` command.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

In this example, running `earthly +docker` will save an image named `go-example` with the tag `latest`.

```bash
~$ earthly +docker
...
~$ docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
go-example          latest    08b9f749023d   19 seconds ago   297MB

# or podman
~$ podman image ls
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
go-example          latest    08b9f749023d   19 seconds ago   297MB
```

**NOTE**

If we run a target as a reference in `FROM` or `COPY`, **outputs will not be produced**. Take this Earthfile for example.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

In this case, running `earthly +docker` will not produce any output. In other words, you will not have a `local-output/go-example` written locally, but running `earthly +build` will still produce output as expected.

The exception to this rule is the `BUILD` command. If you want to use `COPY` or `FROM` and still have Earthly create `local-output/go-example` locally, you'll need to use the `BUILD` command to do so.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    BUILD +build
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

Running `earthly +docker` in this case will now output `local-output/go-example` locally.

### The Push Flag

#### Docker Images

In addition to saving files and images locally, we can also push them to remote repositories.

```Dockerfile
docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE --push go-example:latest
```

Note that adding the `--push` flag to `SAVE IMAGE` is not enough, we'll also need to invoke push when we run earthly. `earthly --push +docker`.

**External Changes**

You can also use `--push` as part of a `RUN` command to define commands that have an effect external to the build. These kinds of effects are only allowed to take place if the entire build succeeds.

This allows you to push to remote repositories.

```Dockerfile
release:
    RUN --push --secret GITHUB_TOKEN=+secrets/GH_TOKEN github-release upload
```

```bash
earthly --push +release
```

But also allows you to do things like run database migrations.

```Dockerfile
migrate:
    FROM +build
    RUN --push bundle exec rails db:migrate
```

```bash
earthly --push +migrate
```

Or apply terraform changes

```Dockerfile
apply:
    RUN --push terraform apply -auto-approve
```

```bash
earthly --push +apply
```

**NOTE**

Just like saving files, any command that uses `--push` **will only produce output if called directly**, `earthly --push +target-with-push` **or via a** `BUILD` command. Calling a target via `FROM` or `COPY` will not invoke `--push`.

#### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part2) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part2/part2 ./part2
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

build:
    # In JS, there's nothing to build in this simple form.
    # The source is also the artifact used in production.
    COPY src/index.js .
    SAVE ARTIFACT index.js /dist/index.js AS LOCAL ./dist/index.js

docker:
    COPY +build/dist dist
    ENTRYPOINT ["node", "./dist/index.js"]
    SAVE IMAGE js-example:latest
```

The code of the app might look like this

`./src/index.js`

```js
console.log("hello world");
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part2) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part2/part2 ./part2
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    COPY build.gradle ./
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin /bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib /lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:latest
```

The code of the app might look like this

`./src/main/java/hello/HelloWorld.java`

```java

package hello;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

`./build.gradle`

```groovy
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'hello.HelloWorld'

jar {
    baseName = 'hello-world'
    version = '0.0.1'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part2) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part2/part2 ./part2
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM python:3
WORKDIR /code

build:
     # In Python, there's nothing to build.
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +build/src src
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE --push python-example:latest
```

The code of the app might look like this

`./src/hello.py`

```python
print("hello world")
```

</details>

# Part 3: Adding dependencies With Caching

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part3/part3 ./part3
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Dependencies

Now let's imagine that we want to add some dependencies to our app. In Go, that means adding `go.mod` and `go.sum`.

`./go.mod`

```go.mod
module github.com/earthly/earthly/examples/go

go 1.13

require github.com/sirupsen/logrus v1.5.0
```

`./go.sum` (empty)

```go.sum
```

The code of the app might look like this

`./main.go`

```go
package main

import "github.com/sirupsen/logrus"

func main() {
 logrus.Info("hello world")
}
```

Now we can update our Earthfile to copy in the `go.mod` and `go.sum`.

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    COPY go.mod go.sum .
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

This works, but it is inefficient because we have not made proper use of caching. In the current setup, when a file changes, the corresponding `COPY` command is re-executed without cache, causing all commands after it to also re-execute without cache.

#### Caching

If, however, we could first download the dependencies and only afterwards copy and build the code, then the cache would be reused every time we changed the code.

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    # Download deps before copying code.
    COPY go.mod go.sum .
    RUN go mod download
    # Copy and build code.
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

For a primer into Dockerfile layer caching see [this article](https://pythonspeed.com/articles/docker-caching-model/). The same principles apply to Earthfiles.

### Reusing Dependencies

In some cases, the dependencies might be used in more than one build target. For this use case, we might want to separate dependency downloading and reuse it. For this reason, let's consider breaking this out into a separate target called `+deps`. We can then inherit from `+deps` by using the command `FROM +deps`.

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    # Output these back in case go mod download changes them.
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum

build:
    FROM +deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part3/part3 ./part3
```

Note that in our case, only the JavaScript version has an example where `FROM +deps` is used in more than one place: both in `build` and in `docker`. Nevertheless, all versions show how dependencies may be separated.

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

deps:
    COPY package.json ./
    COPY package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./package-lock.json

build:
    FROM +deps
    COPY src src
    RUN mkdir -p ./dist && cp ./src/index.html ./dist/
    RUN npx webpack
    SAVE ARTIFACT dist /dist AS LOCAL dist

docker:
    FROM +deps
    COPY +build/dist ./dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./dist"]
    SAVE IMAGE js-example:latest
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part3/part3 ./part3
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

deps:
    COPY build.gradle ./
    RUN gradle build

build:
    FROM +deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:latest
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part3/part3 ./part3
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM python:3
WORKDIR /code

deps:
    RUN pip install wheel
    COPY requirements.txt ./
    RUN pip wheel -r requirements.txt --wheel-dir=wheels
    SAVE ARTIFACT wheels /wheels

build:
    FROM +deps
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +deps/wheels wheels
    COPY +build/src src
    COPY requirements.txt ./
    RUN pip install --no-index --find-links=wheels -r requirements.txt
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:latest
```

</details>

# Part 4: Args

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part4/part4 ./part4
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Just Like Docker...Mostly

`ARG`s in Earthly work similar to `ARG`s in Dockerfiles, however there are a few differences when it comes to scope. Also, Earthly has a number of [built in `ARG`s](https://docs.earthly.dev/docs/earthfile/builtin-args) that are available to use.

Let's say we wanted to have the option to pass in a tag for our Docker image when we run `earthly +docker`.

```Dockerfile
docker:
    ARG tag='latest'
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:$tag
```

In our `+docker` target we can create an `ARG` called tag. In this case, we give it a default value of `latest`. If we do not provide a default value the default will be an empty string.

Then, down in our `SAVE IMAGE` command, we are able to reference the `ARG` with `$` followed by the `ARG` name.

Now we can take advantage of this when we run Earthly.

```bash
earthly +docker --tag='my-new-image-tag'
```

In this case `my-new-image-tag` will override the default value and become the new tag for our docker image. If we hadn't passed in a value for tag, then the default `latest` would have been used.

```bash
earthly +docker
# tag for image will be 'latest'
```

#### Passing ARGs in FROM, BUILD, and COPY

We can also pass `ARG`s when referencing a target inside an Earthfile. Using the `FROM` and `BUILD` commands, this looks pretty similar to what we did above on the command line.

```Dockerfile
docker:
    ARG tag='latest'
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:$tag

with-build:
    BUILD +docker --tag='my-new-image-tag'

with-from:
    FROM +docker --tag='my-new-image-tag'
```

We can also pass `ARG`s when using the `COPY` command, though the syntax is a little different.

```Dockerfile
build:
    ARG version
    COPY main.go .
    RUN go build -o output/example-$version main.go
    SAVE ARTIFACT output/example-$version AS LOCAL local-output/go-example

with-copy:
    COPY (+build/example --version='1.0') .
```

### Builtin `ARG`s

There are a number of builtin `ARG`s that Earthly offers. You can read about a [complete list of them](https://docs.earthly.dev/docs/earthfile/builtin-args), but for now, let's take a look at how they work.

**In order to use Earthly builtin `ARG`s they need to be pre-declared.** Once you do that, you can use them just like any other `ARG`.

```Dockerfile
ARG USERARCH
RUN echo $USERARCH
```

In this case we've declared the `ARG` `USERARCH` which is a builtin that holds the processor architecture the target is being built from.

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part4/part4 ./part4
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

deps:
    COPY package.json ./
    COPY package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./package-lock.json

build:
    FROM +deps
    COPY src src
    RUN mkdir -p ./dist && cp ./src/index.html ./dist/
    RUN npx webpack
    SAVE ARTIFACT dist /dist AS LOCAL dist

docker:
    FROM +deps
    ARG tag='latest'
    COPY +build/dist ./dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./dist"]
    SAVE IMAGE js-example:$tag
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part4/part4 ./part4
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

deps:
    COPY build.gradle ./
    RUN gradle build

build:
    FROM +deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ARG tag='latest'
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:$tag
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part4/part4 ./part4
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM python:3
WORKDIR /code

deps:
    RUN pip install wheel
    COPY requirements.txt ./
    RUN pip wheel -r requirements.txt --wheel-dir=wheels
    SAVE ARTIFACT wheels /wheels

build:
    FROM +deps
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +deps/wheels wheels
    COPY +build/src src
    COPY requirements.txt ./
    ARG tag='latest'
    RUN pip install --no-index --find-links=wheels -r requirements.txt
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:$tag
```

</details>

# Part 5: Importing

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part5/part5 ./part5
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Calling on Targets From Other Earthfiles

So far we've seen how the `FROM` command in Earthly has the ability to reference another target's image as its base image, like in the case below where the `+build` target uses the image from the `+deps` target.

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    # Output these back in case go mod download changes them.
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum

build:
    FROM +deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

```

But `FROM` also has the ability to import targets from Earthfiles in different directories. Let's say we have a directory structure like this.

```
.
├── services
|   └── service-one
|       ├── Earthfile (containing +deps)
|       ├── go.mod
|       └── go.sum
├── main.go
└── Earthfile

```

We can use a target in the Earthfile in `/services/service-one` from inside the Earthfile in the root of our directory. NOTE: relative paths must use `./` or `../`.

`./services/service-one/Earthfile`

```Dockerfile

VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    # Output these back in case go mod download changes them.
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum
```

`./Earthfile`

```Dockerfile
build:
    FROM ./services/service-one+deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

This code tells `FROM` that there is another Earthfile in the `services/service-one` directory and that the Earthfile contains a target called `+deps`. In this case, if we were to run `+build` Earthly is smart enough to go into the subdirectory, run the `+deps` target in that Earthfile, and then use it as the base image for `+build`.

We can also reference an Earthfile in another repo, which works in a similar way. If the reference does not begin with one of `/`, `./`, or `../`, then earthly treats it as a repository. See [the reference](https://github.com/earthly/earthly/blob/docs-0.6/docs/earthfile/README.md#from) for details.

```Dockerfile
build:
    FROM github.com/example/project+remote-target
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

### Importing Whole Projects

In addition to importing single targets from other files, we can also import an entire Earthfile with the `IMPORT` command. This is helpful if there are several targets in a separate Earthfile that you want access to in your current file. It also allows you to create an alias.

```Dockerfile
VERSION 0.6
IMPORT ./services/service-one AS my_service
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    FROM my_service+deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

In this example, we assume there is a `./services/service-one` directory that contains its own Earthfile. We import it and then use the `AS` keyword to give it an alias.

Then, in our `+build` target we can inherit from any target in the imported Earthfile by passing `alias+target-name`. In this case the Earthfile in the service directory has a target named `+deps`.

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part5/part5 ./part5
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

build:
    FROM ./services/service-one+deps
    COPY src src
    RUN mkdir -p ./dist && cp ./src/index.html ./dist/
    RUN npx webpack
    SAVE ARTIFACT dist /dist AS LOCAL dist

docker:
    FROM +deps
    ARG tag='latest'
    COPY +build/dist ./dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./dist"]
    SAVE IMAGE js-example:$tag
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part5/part5 ./part5
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    FROM ./services/service-one+deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ARG tag='latest'
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:$tag
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part5/part5 ./part5
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM python:3
WORKDIR /code

build:
    FROM ./services/service-one+deps
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +deps/wheels wheels
    COPY +build/src src
    COPY requirements.txt ./
    ARG tag='latest'
    RUN pip install --no-index --find-links=wheels -r requirements.txt
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:$tag
```

</details>

# Part 6: Using Docker In Earthly

To copy the files for [this example ( Part 6 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part6) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part6/part6 ./part6
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### The `WITH DOCKER` Command

You may find that you need to run Docker commands inside of a target. For those cases Earthly offers `WITH DOCKER`. `WITH DOCKER` will initialize a Docker daemon that can be used in the context of a `RUN` command.

Whenever you need to use `WITH DOCKER` we recommend (though it is not required) that you use Earthly's own Docker in Docker (dind) image: `earthly/dind:alpine`.

Notice `WITH DOCKER` creates a block of code that has an `END` keyword. Everything that happens within this block is going to take place within our `earthly/dind:alpine` container.

#### Pulling an Image

```Dockerfile
hello:
    FROM earthly/dind:alpine
    WITH DOCKER --pull hello-world
        RUN docker run hello-world
    END

```

You can see in the command above that we can pass a flag to `WITH DOCKER` telling it to pull an image from Docker Hub. We can pass other flags to [load in artifacts built by other targets](#loading-an-image) `--load` or even images defined by [docker-compose](#a-real-world-example) `--compose`. These images will be available within the context of `WITH DOCKER`'s docker daemon.

#### Loading an Image

We can load in an image created by another target with the `--load` flag.

```Dockerfile
my-hello-world:
    FROM ubuntu
    CMD echo "hello world"
    SAVE IMAGE my-hello:latest

hello:
    FROM earthly/dind:alpine
    WITH DOCKER --load hello:latest=+my-hello-world
        RUN docker run hello:latest
    END
```

### A Real World Example

One common use case for `WITH DOCKER` is running integration tests that require other services. In this case we need to set up a redis service for our tests. For this we can user a `docker-compose.yml`.

`docker-compose.yml`

```yml
version: "3"

services:
  redis:
    container_name: local-redis
    image: redis:6.0-alpine
    ports:
      - 127.0.0.1:6379:6379
    hostname: redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:6379"]
      interval: 1s
      timeout: 10s
      retries: 5
    networks:
      - go/part6_default

networks:
  go/part6_default:
```

`main.go`

```go
package main

import (
 "github.com/sirupsen/logrus"
)

var howCoolIsEarthly = "IceCool"

func main() {
 logrus.Info("hello world")
}
```

`main_integration_test.go`

```go
package main

import (
 "context"
 "testing"

 "github.com/go-redis/redis/v8"
 "github.com/stretchr/testify/require"
)

func TestIntegration(t *testing.T) {
 ctx := context.Background()
 rdb := redis.NewClient(&redis.Options{
  Addr:     "redis:6379",
  Password: "", // no password set
  DB:       0,  // use default DB
 })

 err := rdb.Set(ctx, "howCoolIsEarthly", howCoolIsEarthly, 0).Err()
 if err != nil {
  panic(err)
 }

 resultFromDB, err := rdb.Get(ctx, "howCoolIsEarthly").Result()
 if err != nil {
  panic(err)
 }
 require.Equal(t, howCoolIsEarthly, resultFromDB)
}
```

```Dockerfile
VERSION 0.6
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum

test-setup:
    FROM +deps
    COPY main.go .
    COPY main_integration_test.go .
    ENV CGO_ENABLED=0
    ENTRYPOINT [ "go", "test", "github.com/earthly/earthly/examples/go"]
    SAVE IMAGE test:latest

integration-tests:
    FROM earthly/dind:alpine
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml --load tests:latest=+test-setup
        RUN docker run --network=default_go/part6_default tests:latest
    END
```

When we use the `--compose` flag, Earthly will start up the services defined in the `docker-compose` file for us. In this case, we built a separate image that copies in our test files and uses the command to run the tests as its `ENTRYPOINT`. We can then load this image into our `WITH DOCKER` command. Note that loading an image will not run it by default, we need to explicitly run the image after we load it.

You'll need to use `--allow-privileged` (or `-P` for short) to run this example.

```bash
earthly --allow-privileged +integration-tests
```

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 6 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part6) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part6/part6 ./part6
```

In this example, we use `WITH DOCKER` to run a frontend app and backend api together using Earthly.

The App

`./app/package.json`

```json
{
  "name": "example-js",
  "version": "0.0.1",
  "description": "Hello world",
  "private": true,
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "MPL-2.0",
  "devDependencies": {
    "webpack": "^4.42.1",
    "webpack-cli": "^3.3.11"
  },
  "dependencies": {
    "http-server": "^0.12.1"
  }
}
```

`./app/package-lock.json` (empty)

```json
```

The code of the app might look like this

`./app/src/index.js`

```js
async function getUsers() {

  const response = await fetch('http://0.0.0.0:3080/api/users');
  return await response.json();

}

function component() {
  const element = document.createElement('div');
  getUsers()
    .then( users => {
      element.innerHTML = `hello world <b>${users[0].first_name} ${users[0].last_name}</b>`
    })

 return element;
}

document.body.appendChild(component());
```

`./app/src/index.html`

```html
<!doctype html>
<html>

<head>
    <title>Getting Started</title>
</head>

<body>
    <script src="./main.js"></script>
</body>

</html>
```

And our api.

`./api/package.json`

```json
{
  "name": "api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.17.1",
    "http-proxy-middleware": "^1.0.4",
    "pg": "^8.7.3"
  }
}
```

`./api/package-lock.json` (empty)

```json
```

`./api/server.js`

```js
const express = require('express');
const path = require('path');
const cors = require("cors");
const app = express(),
bodyParser = require("body-parser");
port = 3080;

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../my-app/build')));

app.use(cors());

const users = [
  {
    'first_name': 'Lee',
    'last_name' : 'Earth'
  }
]

app.get('/api/users', (req, res) => {
  console.log('api/users called!')
  res.json(users);
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server listening on the port::${port}`);
});
```

The `Earthfile` is at the root of the directory.

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

app-deps:
    COPY ./app/package.json ./
    COPY ./app/package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./app/package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./app/package-lock.json

build-app:
    FROM +app-deps
    COPY ./app/src ./app/src
    RUN mkdir -p ./app/dist && cp ./app/src/index.html ./app/dist/
    RUN cd ./app && npx webpack
    SAVE ARTIFACT ./app/dist /dist AS LOCAL ./app/dist

app-docker:
    FROM +app-deps
    ARG tag='latest'
    COPY +build-app/dist ./app/dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./app/dist"]
    SAVE IMAGE js-example:$tag

api-deps:
    COPY ./api/package.json ./
    COPY ./api/package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./api/package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./api/package-lock.json

api-docker:
    FROM +api-deps
    ARG tag='latest'
    COPY ./api/server.js .
    RUN pwd
    RUN ls
    EXPOSE 3080
    ENTRYPOINT ["node", "server.js"]
    SAVE IMAGE js-api:$tag

# Run your app and api side by side
app-with-api:
    FROM earthly/dind:alpine
    RUN apk add curl
    WITH DOCKER \
        --load app:latest=+app-docker \
        --load api:latest=+api-docker
        RUN docker run -d -p 3080:3080 api && \
            docker run -d -p 8080:8080 app  && \
            sleep 5 && \
            curl 0.0.0.0:8080 | grep 'Getting Started' && \
            curl 0.0.0.0:3080/api/users | grep 'Earth'
    END

```

Now you can run `earthly -P +app-with-api` to run the app and api side-by-side.

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 6 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part6) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part6/part6 ./part6
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

deps:
    COPY build.gradle ./
    RUN gradle build

build:
    FROM +deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ARG tag='latest'
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:$tag

with-postgresql:
    FROM earthly/dind:alpine
   COPY ./docker-compose.yml .
   RUN apk update
   RUN apk add postgresql-client
   WITH DOCKER --compose docker-compose.yml --load app:latest=+docker
      RUN while ! pg_isready --host=localhost --port=5432; do sleep 1; done ;\
       docker run --network=default_java/part6_default app
   END

```

`docker-compose.yml`

```yml
version: "3.9"
   
services:
  db:
    image: postgres
    container_name: db
    hostname: postgres
    environment:
      - POSTGRES_DB=test_db
      - POSTGRES_USER=earthly
      - POSTGRES_PASSWORD=password
    ports:
      - 127.0.0.1:5432:5432
    networks:
      - java/part6_default

networks:
  java/part6_default:


```

The code of the app might look like this

`./src/main/java/hello/HelloWorld.java`

```java

package postgresclient;

import org.joda.time.LocalTime;
import java.sql.Connection;
import java.sql.DriverManager;


public class PostgreSQLJDBC {
   public static void main(String args[]) {
      Connection c = null;
      try {
         Class.forName("org.postgresql.Driver");
         c = DriverManager
            .getConnection("jdbc:postgresql://postgres:5432/test_db",
            "earthly", "password");
      } catch (Exception e) {
         e.printStackTrace();
         System.err.println(e.getClass().getName()+": "+e.getMessage());
         System.exit(0);
      }
      System.out.println("Opened database successfully");
   }
}
```

`./build.gradle`

```groovy
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'postgresclient.PostgreSQLJDBC'

repositories {
    mavenCentral()
}

jar {
    baseName = 'hello-world'
    version = '0.0.1'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8

dependencies {
    compile "joda-time:joda-time:2.2"
    compile(group: 'org.postgresql', name: 'postgresql', version: '42.3.3')
    testCompile "junit:junit:4.12"
}

```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 7 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part7) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part7/part7 ./part7
```

`./tests/test_db_connection.py`

```python
import unittest
import psycopg2

class MyIntegrationTests(unittest.TestCase):

    def test_db_connection_active(self):
        connection = psycopg2.connect(
            host="postgres",
            database="test_db",
            user="earthly",
            password="password")
        
        self.assertEqual(connection.closed, 0)

if __name__ == '__main__':
    unittest.main()
```

```yml
version: "3.9"
   
services:
  db:
    image: postgres
    container_name: db
    hostname: postgres
    environment:
      - POSTGRES_DB=test_db
      - POSTGRES_USER=earthly
      - POSTGRES_PASSWORD=password
    ports:
      - 5432:5432
    networks:
      - python/part6_default

networks:
  python/part6_default:
```

`./Earthfile`

```Dockerfile
VERSION 0.6
FROM python:3
WORKDIR /code

build:
  COPY ./requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .

run-tests:
    FROM earthly/dind:alpine
    COPY ./docker-compose.yml .
    COPY ./tests ./tests
    RUN apk update
    RUN apk add postgresql-client
    WITH DOCKER --compose docker-compose.yml --load app:latest=+docker
        RUN while ! pg_isready --host=localhost --port=5432; do sleep 1; done ;\
          docker run --network=default_python/part6_default app python3 ./tests/test_db_connection.py
    END
```

</details>

# Final words

Congratulations, you completed the Earthly tutorial!

Learning Earthly does not stop here. Discover more of what Earthly can do by exploring the documentation.

**Recommended reading:**

* [The Earthfile reference](https://docs.earthly.dev/docs/earthfile)
* [The **earthly command** reference](https://docs.earthly.dev/docs/earthly-command)
* [Guides](https://tinyurl.com/2p8cpnxv)
* [Examples using Earthly](https://docs.earthly.dev/docs/examples)
* [Best practices](https://docs.earthly.dev/best-practices)

**More examples:**

* [Examples directory on GitHub](https://github.com/earthly/earthly/tree/main/examples)
* [Go](https://github.com/earthly/earthly/tree/main/examples/go)
* [JavaScript](https://github.com/earthly/earthly/tree/main/examples/js)
* [Java](https://github.com/earthly/earthly/tree/main/examples/java)
* [Python](https://github.com/earthly/earthly/tree/main/examples/python)

## Questions & Feedback

If you have any questions, feedback or suggestions for Earthly or this tutorial feel free to reach out to us on our [Slack community](https://earthly.dev/slack) or open a [GitHub issue](https://github.com/earthly/earthly/issues). Earthly is free and open and we love and appreciate feedback and contributions from the community!

## Go back

* [Introduction](https://docs.earthly.dev/basics)
* [Part 1: A simple Earthfile](https://docs.earthly.dev/basics/part-1-a-simple-earthfile)
* [Part 2: Outputs](https://docs.earthly.dev/basics/part-2-outputs)
* [Part 3: Adding dependencies With Caching](https://docs.earthly.dev/basics/part-3-adding-dependencies-with-caching)
* [Part 4: Args](https://docs.earthly.dev/basics/part-4-args)
* [Part 5: Importing](https://docs.earthly.dev/basics/part-5-importing)
* [Part 6: Using Docker In Earthly](https://docs.earthly.dev/basics/part-6-using-docker-with-earthly)
* **Final words** <-- You are here.

# Best practices

Although Earthly has been designed to be unambiguous about what command to use for the job, writing Earthfiles can sometimes still be tricky, when it comes to nuances. As you try to accomplish certain tasks, you may find that sometimes the same result can be achieved using more than one technique. Or so it might seem.

Below we list some of the best practices that we have found to be useful in designing Earthly builds, with a focus on certain commands or techniques that seem similar, but aren't really, but also on some key points that we have seen newcomers stumble into.

## Table of contents

* [Earthfile-specific](#earthfile-specific)
  * [`COPY` only the minimal amount of files. Avoid copying `.git`](#copy-only-the-minimal-amount-of-files.-avoid-copying-.git)
  * [`ENV` for image env vars, `ARG` for build configurability](#env-for-image-env-vars-arg-for-build-configurability)
  * [Use cross-repo references, and avoid `GIT CLONE` if possible](#use-cross-repo-references-and-avoid-git-clone-if-possible)
  * [`GIT CLONE` vs `RUN git clone`](#git-clone-vs-run-git-clone)
  * [`IF [...]` vs `RUN if [...]`](#if-...-vs-run-if-...)
  * [`FOR ... IN ...` vs `RUN for ... in ...`](#for-...-in-...-vs-run-for-...-in-...)
  * [Pattern: Optionally `LOCALLY`](#pattern-optionally-locally)
  * [Pattern: Deciding on a base image based on a condition](#pattern-deciding-on-a-base-image-based-on-a-condition)
  * [Use `RUN --push` for deployment commands](#use-run-push-for-deployment-commands)
  * [Use `--secret`, not `ARG`s to pass secrets to the build](#use-secret-not-args-to-pass-secrets-to-the-build)
  * [Avoid copying secrets to the build environment](#avoid-copying-secrets-to-the-build-environment)
  * [Do not pass Earthly dependencies from one target to another via the local file system or via an external registry](#do-not-pass-earthly-dependencies-from-one-target-to-another-via-the-local-file-system-or-via-an-external-registry)
  * [Use `WITH DOCKER --pull`](#use-with-docker-pull)
  * [Style: Define the high-level targets at the top of the Earthfile](#style-define-the-high-level-targets-at-the-top-of-the-earthfile)
  * [Use `COPY +my-target/...` to pass files to and from `LOCALLY` targets](#use-copy-+my-target-...-to-pass-files-to-and-from-locally-targets)
  * [Use `WITH DOCKER --load=+my-target` to pass images to `LOCALLY` targets](#use-with-docker-load-+my-target-to-pass-images-to-locally-targets)
  * [Avoid non-deterministic behavior](#avoid-non-deterministic-behavior)
  * [Use `COPY --dir` to copy multiple directories](#use-copy-dir-to-copy-multiple-directories)
  * [Use separate images for build and production](#use-separate-images-for-build-and-production)
  * [Use `SAVE ARTIFACT ... AS LOCAL ...` for generated code, not `LOCALLY`](#use-save-artifact-...-as-local-...-for-generated-code-not-locally)
  * [Multi-line strings](#multi-line-strings)
  * [Multi-line commands](#multi-line-commands)
  * [Copying files from outside the build context](#copying-files-from-outside-the-build-context)
  * [Repository structure: Place build logic as close to the relevant code as possible](#repository-structure-place-build-logic-as-close-to-the-relevant-code-as-possible)
  * [Repository structure: Do not place all Earthfiles in a dedicated directory](#repository-structure-do-not-place-all-earthfiles-in-a-dedicated-directory)
  * [Pattern: Pass-through artifacts or images](#pattern-pass-through-artifacts-or-images)
  * [Use `earthly/dind`](#use-earthly-dind)
  * [Pattern: Saving artifacts resulting from a `WITH DOCKER`](#pattern-saving-artifacts-resulting-from-a-with-docker)
* [Usage-specific](#usage-specific)
  * [Use `--ci` when running in CI](#use-ci-when-running-in-ci)
  * [Avoid `LOCALLY` and other non-strict commands](#avoid-locally-and-other-non-strict-commands)
  * [Pattern: Push on the `main` branch only](#pattern-push-on-the-main-branch-only)
  * [Do not expose cache image tags publicly if the cache contains private code or dependencies](#do-not-expose-cache-image-tags-publicly-if-the-cache-contains-private-code-or-dependencies)
  * [Technique: Use `earthly -i` to debug failures](#technique-use-earthly-i-to-debug-failures)
  * [Run everything in a single Earthly invocation, do not wrap Earthly](#run-everything-in-a-single-earthly-invocation-do-not-wrap-earthly)
  * [Use `RUN --ssh` for passing host SSH keys to builds](#use-run-ssh-for-passing-host-ssh-keys-to-builds)
  * [Future: Saving an artifact even if the build fails](#future-saving-an-artifact-even-if-the-build-fails)

## Earthfile-specific

### `COPY` only the minimal amount of files. Avoid copying `.git`

A typical mistake is to `COPY` entire large directories into the build environment and only using a subset of the files within them. Or worse, copying the entire repository (which might also include `.git`) for no good reason.

```Dockerfile
# Avoid
COPY . .
COPY * ./
```

The problem with this is that many of the files copied are not actually used during the build, however Earthly will react to changes to them, causing it to reuse cache inefficiently. It's not an issue of file size (though sometimes that too can hurt performance). It is much of an issue of re-executing build commands that wouldn't have to be re-executed.

```Dockerfile
# Avoid
COPY . .
RUN go mod download
RUN go build ...
```

In the above example, changing the project's `README.md` or running `git fetch` might cause slow commands like `go mod download` to be re-executed.

Earthly uses `COPY` commands (among other things) to mark certain files as inputs to the build. If any file included in a `COPY` changes, then the build will continue from that `COPY` command onwards. For this reason, you want to be as specific as possible when including files in a `COPY` command. In some cases, you might even have to list files individually.

Here are some possible ways to improve the above example:

```Dockerfile
# Better
COPY go.mod go.sum ./*.go ./
RUN go mod download
RUN go build ...
```

The above is better, as it avoids reacting to changes in `.git` or to unrelated files, like `README.md`. However, this can be arranged even better, to avoid downloading all the dependencies on every `*.go` file change.

```Dockerfile
# Best
COPY go.mod go.sum ./
RUN go mod download
COPY ./*.go ./
RUN go build ...
```

An additional way in which you can improve the precision of the `COPY` command is to use the [`.earthlyignore`](https://docs.earthly.dev/docs/earthfile/earthlyignore) file. Note, however, that this is best left as a last resort, as new files added to the project (that may be irrelevant to builds) would need to be manually added to `.earthlyignore`, which may be error-prone. It is much better to have to include every new file manually into the build (by adding it to a `COPY` command), than to exclude every new file manually (by adding it to the `.earthlyignore`), as whenever any such new file *must* be included, then the build would typically fail, making it harder to make a mistake compared to the opposite.

### `ENV` for image env vars, `ARG` for build configurability

`ENV` variables and `ARG` variables seem similar, however they are meant for different use-cases. Here is a breakdown of the differences, as well as how they differ from the Dockerfile-specific `ARG` command:

|                                                                                     | `ENV` | `ARG` | Dockerfile `ARG` |
| ----------------------------------------------------------------------------------- | ----- | ----- | ---------------- |
| Available as an env-var in the same target                                          | ✅     | ✅     | ❌                |
| Available for expanding within non-RUN commands                                     | ❌     | ✅     | ✅                |
| Stored in the final image as an env-var                                             | ✅     | ❌     | ❌                |
| Inherited via `FROM`                                                                | ✅     | ❌     | ❌                |
| Can be overridden when calling a build                                              | ❌     | ✅     | ✅                |
| Can be propagated to other targets (via `BUILD +target --<key>=<value>` or similar) | ❌     | ✅     | N/A              |

As you can see, the key situation where `ENV` is needed is when you want the value to be stored as part of the final image's configuration. This causes any `FROM` or `docker run` using that image to inherit the value.

However, if the use-case is build configurability, then `ARG` is the way to achieve that.

### Use cross-repo references, and avoid `GIT CLONE` if possible

Earthly provides rich set of features to allow working with and across Git repositories. It is recommended to use Earthly [cross-repository references](https://docs.earthly.dev/docs/guides/target-ref) rather than `GIT CLONE` or `RUN git clone`, whenever possible.

Here is an example.

Repo 1:

```
repo 1
├── README.md
└── my-file.txt
```

Repo 2:

```Dockerfile
# Bad
VERSION 0.6
FROM alpine:3.15
WORKDIR /work
print-file:
    GIT CLONE git@github.com:my-co/repo-1.git
    RUN echo my-file.txt
```

This might be addressed in the following way:

Repo 1:

```
repo 1
├── README.md
├── Earthfile
└── my-file.txt
```

```Dockerfile
# Repo 1 Earthfile
VERSION 0.6
FROM alpine:3.15
WORKDIR /work
file:
    COPY ./my-file.txt ./
    SAVE ARTIFACT ./my-file.txt
```

Repo 2:

```Dockerfile
# Repo 2 Earthfile
VERSION 0.6
IMPORT github.com/my-co/repo-1
FROM alpine:3.15
WORKDIR /work
print-file:
    COPY repo-1+file/my-file.txt ./
    RUN echo my-file.txt
```

There are multiple benefits to using cross-repository references in this manner:

* The build of repo 1 can evolve to more than just passing a file to another repository. It may be possible to also export generated code, artifacts, base images or full microservice images in the future, if they are needed.
* It is clearer about which files are actually needed externally, as they are declared via `SAVE ARTIFACT`. This makes the code more readable and maintainable. The fact that an artifact is saved during a build constitutes an explicit API of the repository.

Of course, the down-side is that repo 1 requires an Earthfile to be added, and that might not always be feasible. It's possible that repo 1 is controlled by another team, or that it is entirely external to the company. In such cases, `GIT CLONE` might help to provide a faster, yet imperfect solution.

Another use-case where `GIT CLONE` is better suited is when the operation needs to take place on the whole source repository. For example, performing Git operations, such as tagging, creating branches, or merging.

Finally, here is a comparison between cross-repo references and `GIT CLONE`:

|                                                            | Cross-repo reference                                | `GIT CLONE`                                                 |
| ---------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------- |
| Example                                                    | `FROM github.com/my-co/my-proj:my-branch+my-target` | `GIT CLONE --branch=my-branch git@github.com:my-co/my-proj` |
| Earthly can pass-through SSH agent access from the host    | ✅                                                   | ✅                                                           |
| Access to HTTPS repositories can be configured in Earthly  | ✅                                                   | ✅                                                           |
| Can specify branch or tag                                  | ✅ - via `:<branch>`                                 | ✅ - via `--branch`                                          |
| Source configurable via `ARG`s                             | ✅                                                   | ✅                                                           |
| Protocol-agnostic referencing                              | ✅                                                   | ❌ - can be `ssh://`, `https://`, `git@github.com` etc       |
| Clear declaration of the dependency                        | ✅ - source repo needs to expose it in the Earthfile | ❌                                                           |
| Can be used without modifications to the source repository | ❌ - requires Earthfile                              | ✅                                                           |
| Can operate on the repository itself                       | ❌ - possible, but not designed for this             | ✅                                                           |

### `GIT CLONE` vs `RUN git clone`

Earthly has a built-in `GIT CLONE` instruction that can be used to clone a Git repository. It is recommended that `GIT CLONE` is used rather than `RUN git clone`, for a few reasons:

* Earthly treats `GIT CLONE` as a first-class input (BuildKit source). As such, Earthly caches the repository internally and downloading only incremental differences on changes.
* Earthly is commit hash-aware, so it'll be able to detect when the build needs to take place versus when there are no changes to be made and the cache can be reused. If a change takes place in the source repository, `RUN git clone` would not be able to detect that, as it is not recognized as an input. So it would naively reuse the cache when it shouldn't.
* `GIT CLONE` will pass-through Earthly settings for [authentication](https://docs.earthly.dev/docs/guides/auth), such as SSH agent access and/or HTTPS credentials.

`GIT CLONE` does have some limitations, however. It only performs a shallow clone, it does not have the branch information, it does not have origin information, and it does not have the tags downloaded. Even in such cases, it might be better to attempt to reintroduce the information after a `GIT CLONE`, whenever possible, in order to gain the caching benefits.

When this proves to be too difficult, or impossible, and you really need to perform a custom `RUN git clone`, consider using both in conjunction, to gain the hash awareness benefits.

```Dockerfile
# Bad
RUN git clone git@github.com/my-co/my-proj
WORKDIR my-proj
RUN ls
```

```Dockerfile
# Good
GIT CLONE git@github.com/my-co/my-proj my-proj
WORKDIR my-proj
RUN ls
```

```Dockerfile
# Ok, if you have no choice
ARG git_url="git@github.com/my-co/my-proj"
GIT CLONE "$git_url" my-proj
ARG git_hash=$(cd my-proj; git rev-parse HEAD)
RUN rm -rf my-proj &&\
    git clone "$git_url" my-proj &&\
    cd my-proj &&\
    git checkout "$git_hash"
WORKDIR my-proj
RUN ls
```

Finally, here is a comparison between `GIT CLONE` and `RUN git clone`:

|                                                                         | `GIT CLONE`                                           | `RUN git clone`                                       |
| ----------------------------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| Earthfiles can be protocol-agnostic                                     | ❌ - can be `ssh://`, `https://`, `git@github.com` etc | ❌ - can be `ssh://`, `https://`, `git@github.com` etc |
| Can configure access in Earthly, to keep Earthfiles agnostic            | ✅                                                     | ❌                                                     |
| Earthly can pass-through SSH agent access from the host                 | ✅                                                     | ✅ - but it requires `RUN --ssh`                       |
| Access to HTTPS repositories can be configured in Earthly               | ✅                                                     | ❌ - but possible to pass credentials via secrets      |
| Cache-aware - incremental pulls                                         | ✅                                                     | ❌                                                     |
| Commit hash-aware - rebuild when there are changes in remote repository | ✅                                                     | ❌                                                     |

### `IF [...]` vs `RUN if [...]`

Earthly 0.6 introduces the conditional `IF` command, which allows for complex control flow within Earthly recipes. However, there is also the possibility of using the shell `if` command to accomplish similar behavior. Which one should you use? Here is a quick comparison:

|                                                         | `IF` | `RUN if` |
| ------------------------------------------------------- | ---- | -------- |
| Can execute any command as the expression               | ✅    | ✅        |
| Can use mounts and secrets                              | ✅    | ✅        |
| Can use ARGs                                            | ✅    | ✅        |
| Expression can be cached                                | ✅    | ✅        |
| Body runs in the same layer as the condition expression | ❌    | ✅        |
| Body can include any Earthly command                    | ✅    | ❌        |

As you can see, `IF` is more powerful in that it can include other Earthly commands within it, allowing for rich conditional behavior. Examples might include optionally saving images, using different base images depending on a set of conditions, initializing `ARG`s with varying values.

`RUN if`, however is often simpler, and it only uses one layer.

As a best practice, it is recommended to use `RUN if` whenever possible (e.g. only `RUN` commands would be involved), to encourage simplicity, and otherwise to use `IF`.

### `FOR ... IN ...` vs `RUN for ... in ...`

As is the case with `IF` vs `RUN if`, there is a similar debate for the Earthly builtin command `FOR` vs `RUN for`. Here is a quick comparison of the two 'for' flavors:

|                                                      | `FOR` | `RUN for` |
| ---------------------------------------------------- | ----- | --------- |
| Can execute any command as the expression            | ✅     | ✅         |
| Can use mounts and secrets                           | ✅     | ✅         |
| Can use ARGs                                         | ✅     | ✅         |
| Expression can be cached                             | ✅     | ✅         |
| Can iterate over a constant list                     | ✅     | ✅         |
| Can iterate over a list resulting from an expression | ✅     | ✅         |
| Body runs in the same layer as the for expression    | ❌     | ✅         |
| Body can include any Earthly command                 | ✅     | ❌         |

Similar to the `IF` vs `RUN if` comparison, `FOR` is more powerful in that it can include other Earthly commands within it, allowing for rich iteration behavior. Examples might include iterating over a list of directories in a monorepo and calling Earthly targets within them, performing `SAVE IMAGE` over a list of container image tags.

`RUN for`, however is often simpler, and it only uses one layer.

As a best practice, it is recommended to use `RUN for` whenever possible (e.g. only `RUN` commands would be involved), to encourage simplicity, and otherwise to use `FOR`.

### Pattern: Optionally `LOCALLY`

In certain cases, it may be desirable to execute certain targets on the host machine, rather than in the sandboxed build environment, for debugging purposes. However, we need most of the targets to execute in strict mode in CI. The solution to this is to use a target that can be optionally executed via `LOCALLY`. Here is an example:

Suppose we wanted the following target to be executed on against the host's Docker daemon:

```Dockerfile
FROM earthly/dind:alpine
WORKDIR /app
COPY docker-compose.yml ./
WITH DOCKER --compose docker-compose.yml \
        --service db \
        --load=+integration-test
    RUN docker-compose up integration
END
```

We could therefore have an equivalent `LOCALLY` target:

```Dockerfile
LOCALLY
WITH DOCKER --compose docker-compose.yml \
        --service db \
        --load=+integration-test
    RUN docker-compose up integration
END
```

However, the code duplication is not ideal and will result in the two recipes to drift apart over time.

It is possible to use an `ARG` to decide on whether to execute the target on the host or not:

```Dockerfile
FROM alpine:3.15
ARG run_locally=false
IF [ "$run_locally" = "true" ]
    LOCALLY
ELSE
    FROM earthly/dind:alpine
    WORKDIR /app
    COPY docker-compose.yml ./
END
WITH DOCKER --compose docker-compose.yml \
        --service db \
        --load=+integration-test
    RUN docker-compose up integration
END
```

Now, to run locally, you can execute `earthly +my-target --run_locally=true`, otherwise `earthly +my-target` will execute in the sandboxed environment (the same way it executes in CI).

### Pattern: Deciding on a base image based on a condition

In some cases, it is useful to switch up which base image to use depending on the result of an `IF` expression. For example, let's assume that the company provided Go image only supports the `linux/amd64` platform, and therefore, you'd like to use the official golang image when ARM (`linux/arm64`) is detected. Here's how this can be achieved:

```Dockerfile
FROM alpine:3.15
ARG TARGETPLATFORM
IF [ "$TARGETPLATFORM" = "linux/arm64" ]
    FROM golang:1.16
ELSE
    FROM my-company/golang:1.16
END
```

This will cause the execution of consecutive `FROM`s within the same target. This is completely valid. On encountering another `FROM` expression, the current build environment is reset and another fresh root is initialized, containing the specified images data.

### Use `RUN --push` for deployment commands

If the result of a build needs to be pushed to an external service (or storage provider) and the destination is not an image registry, then you will need to use a custom push command (as opposed to a `SAVE IMAGE --push`).

To execute a custom push command, you can simply use a regular `RUN` command together with the `--push` flag. The `--push` will ensure that:

* The command is only executed when Earthly is in push mode (`earthly --push`)
* No cache is reused for that specific command, causing it to execute every time
* The command is executed during the push phase of the build, ensuring that everything else (e.g. testing) has completed successfully first

Let's look at an example of using the [github-release utility](https://github.com/github-release/github-release) to perform a push to GitHub Releases.

```Dockerfile
# Bad, and dangerous
RUN --no-cache --secret GITHUB_TOKEN github-release upload ...
```

`RUN --no-cache` should be avoided for this use-case, as it has some potentially dangerous downsides:

* The upload command may be executed in parallel with any testing (meaning that tests might not pass yet the upload may still complete)
* The upload will execute even when earthly is not invoked in `--push` mode.

To address this issue, it is advisable to use `RUN --push` instead.

```Dockerfile
# Good
RUN --push --secret GITHUB_TOKEN github-release upload ...
```

### Use `--secret`, not `ARG`s to pass secrets to the build

If a build requires the usage of secrets, it is strongly recommended that you use the builtin secrets constructs, such as `earthly --secret`, [Earthly Cloud Secrets](https://docs.earthly.dev/earthly-cloud/cloud-secrets), and `RUN --secret`.

Using `ARG`s for passing secrets is strongly discouraged, as the secrets will be leaked in build logs, the build cache and the possibly in published images.

### Avoid copying secrets to the build environment

Even when using the proper builtin constructs for handling secrets, it is possible to then copy secrets in the build environment, which cause secrets to be leaked to a remote build cache, or to published images.

A simple example of how this may be possible:

```Dockerfile
# Bad
RUN --secret MY_SECRET echo "secret: $MY_SECRET" > /app/secret.txt
```

While this seems innocuous and possibly uncommon, consider the following, which on the face of it might look like a good idea:

```Dockerfile
# Bad
RUN --secret AWS_ACCESS_KEY_ID --secret AWS_SECRET_ACCESS_KEY echo "[default]\naws_access_key_id=$AWS_ACCESS_KEY_ID\naws_secret_access_key=$AWS_SECRET_ACCESS_KEY" > /root/.aws/credentials
RUN aws ec2 describe-images
```

Another negative example is copying the local credentials file:

```Dockerfile
# Bad
aws-creds:
    LOCALLY
    RUN cp "$HOME"/.aws/credentials ./.aws-creds
    SAVE ARTIFACT ./.aws-creds

do-something-with-aws:
    FROM ...
    COPY +aws-creds/.aws-creds /root/.aws/credentials
    RUN aws ec2 describe-images
```

The correct way to handle secrets that need to exist as files is to either mount them as secret files in the first place:

```Dockerfile
# Best
RUN --mount=type=secret,target=/root/.aws/credentials,id=AWS_CREDENTIALS \
    aws ec2 describe-images
```

This way, the credentials are never stored in the stored environment - they are only mounted during the execution of the `RUN` command.

Or, if you really have no choice, you may copy the secrets temporarily, but you **have** to remove them in the same layer:

```Dockerfile
# Ok, but error prone
RUN --secret AWS_ACCESS_KEY_ID --secret AWS_SECRET_ACCESS_KEY echo "[default]\naws_access_key_id=$AWS_ACCESS_KEY_ID\naws_secret_access_key=$AWS_SECRET_ACCESS_KEY" > /root/.aws/credentials ;\
    aws ec2 describe-images ;\
    rm /root/.aws/credentials
```

This should be avoided if possible, as it is error prone and might get secrets leaked if the `rm` is forgotten, or if the removal is performed under a separate `RUN` command.

```Dockerfile
# Bad: removal takes place in a separate layer, which means that the secrets will be leaked to the cache
RUN --secret AWS_ACCESS_KEY_ID --secret AWS_SECRET_ACCESS_KEY echo "[default]\naws_access_key_id=$AWS_ACCESS_KEY_ID\naws_secret_access_key=$AWS_SECRET_ACCESS_KEY" > /root/.aws/credentials
RUN aws ec2 describe-images
RUN rm /root/.aws/credentials
```

### Do not pass Earthly dependencies from one target to another via the local file system or via an external registry

If you are new to Earthly, you may be tempted to save an artifact locally in one target and then to retrieve it another one.

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +build
dep:
    ...
    SAVE ARTIFACT my-artifact.jar AS LOCAL ./build/my-artifact.jar
build:
    ...
    COPY ./build/my-artifact.jar ./
    ...
```

This will not actually work, as in Earthly all output takes place only at the end of a successful build. Meaning that when `+build` starts, the artifact would not have been output yet. In fact, `+dep` and `+build` will run completely parallel anyway - as Earthly does not know of a dependency between them.

The proper way to achieve this is to use [artifact references](https://docs.earthly.dev/docs/guides/target-ref).

```Dockerfile
# Good
all:
    BUILD +build
dep:
    ...
    SAVE ARTIFACT my-artifact.jar
build:
    ...
    COPY +dep/my-artifact.jar ./
    ...
```

Notice that `+dep` no longer needs to save the file locally. Also, the `COPY` command no longer references the file from the local file system. It has been replaced with an artifact reference from the target `+dep`. This reference will tell Earthly that these two targets depend on each other and will therefore schedule the relevant parts to run sequentially.

Notice also that in our `+all` target, we no longer have to call both `+dep` and `+build`. The system will automatically infer that when building `+build`, `+dep` is also required.

Another example of what you should **not** do is to pass Earthly images via between targets via an external registry.

```Dockerfile
# Bad
all:
    BUILD +dep-img
    BUILD +test
dep-img:
    ...
    SAVE IMAGE --push my-co/my-image:latest
test:
    WITH DOCKER
        RUN docker run my-co/my-image:latest
    END
```

```Dockerfile
# Also bad
all:
    BUILD +test
dep-img:
    ...
    SAVE IMAGE --push my-co/my-image:latest
test:
    BUILD +dep-img # This still does not work
    WITH DOCKER
        RUN docker run my-co/my-image:latest
    END
```

Similarly, in this case, pushing of the image takes place at the end of the build, which means that when `+test` runs, it will not have the image available, unless it has been pushed in a previous execution (which means that the image may be stale).

To fix this, we need to use `WITH DOCKER --load` and a [target reference](https://docs.earthly.dev/docs/guides/target-ref):

```Dockerfile
# Good
all:
    BUILD +test
dep-img:
    ...
    SAVE IMAGE my-co/my-image:latest
test:
    WITH DOCKER --load=+dep-img
        RUN docker run my-co/my-image:latest
    END
```

The `--load` instruction will inform Earthly that the two targets depend on each other and will therefore build the image and load it into the Docker daemon provided by `WITH DOCKER`.

### Use `WITH DOCKER --pull`

When referencing an external image in the body of a `WITH DOCKER` block, it is important to declare it via `WITH DOCKER --pull`, for a few reasons:

* The image will be cached as part of buildkit, allowing for faster builds. This is especially important as `WITH DOCKER` wipes the state of the Docker daemon (including its cache) after every run.
* The Daemon within `WITH DOCKER` is not logged into registries. Your local Docker login config is not propagated to the daemon. This means that you may run into issues when trying to pull images from private registries, but also, DockerHub rate limiting may prevent you from pulling images consistently from public repositories.

```Dockerfile
# Bad: Image hello-world needs to be pulled every time and is not part of the Earthly-managed cache.
WITH DOCKER
   RUN docker run hello-world
END
```

```Dockerfile
# Good
WITH DOCKER --pull hello-world
   RUN docker run hello-world
END
```

If you use `WITH DOCKER --compose`, Earthly will automatically pull images declared in the compose file for you, as long as they are not already being loaded from another target via `WITH DOCKER --load`. So in this case, you do not need to declare those image with `WITH DOCKER --pull`.

### Style: Define the high-level targets at the top of the Earthfile

High-level targets are those targets that are meant to be executed directly by the user on the command-line or via the CI.

As software engineers, we read code more often than we write it. As a matter of style, it is recommended to declare the higher-level targets at the top of the Earthfile, to help with the usability of the Earthfile. This will help fellow engineers who have not worked on the Earthfile to quickly find the relevant targets to use in their day-to-day development.

It also helps a reader to consume the Earthfile starting from the top, forming a high-level picture first, then gradually going deeper and deeper to lower-level logic.

### Use `COPY +my-target/...` to pass files to and from `LOCALLY` targets

When using `LOCALLY`, it is tempting to skip on using Earthly constructs for passing files between targets. However, this can be problematic.

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +build
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
build:
    COPY ./my-artifact.txt ./
    ...
```

This setup may actually work, but it has a key issue: the order of `+dep` and `+build` is not guaranteed. So in some runs, the file `./my-artifact.txt` will be created before the `+build` target is executed, and in some runs it will be created after.

To fix this race condition, you need to use an [artifact reference](https://docs.earthly.dev/docs/guides/target-ref), to ensure that Earthly is aware of the dependency between the two targets:

```Dockerfile
# Good
all:
    BUILD +build
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt
build:
    COPY +dep/my-artifact.txt ./
    ...
```

Here is another example of the reverse (copying a file to a `LOCALLY` target):

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +run-locally
dep:
    FROM alpine:3.15
    WORKDIR /work
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt AS LOCAL ./build/my-artifact.txt
run-locally:
    LOCALLY
    RUN echo ./build/my-artifact.txt
```

The mistake here is relying on `SAVE ARTIFACT ... AS LOCAL ...` for the transfer of the artifact to the `LOCALLY` target. As Earthly outputs are written at the end of the build, the target `+run-locally` will not have the file in time (or it might have it from a previous run only, meaning that it might be stale).

Here is how to fix this:

```Dockerfile
# Good
all:
    BUILD +run-locally
dep:
    FROM alpine:3.15
    WORKDIR /work
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt
run-locally:
    LOCALLY
    COPY +dep/my-artifact.txt ./build/my-artifact.txt
    RUN echo ./build/my-artifact.txt
```

The `COPY` command using an artifact reference will inform Earthly of the dependency between the two targets, and will therefore cause the transfer of artifact between the two properly.

And finally, here is another common mistake, when passing files between two `LOCALLY` targets:

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +run-locally
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt AS LOCAL ./build/my-artifact.txt
run-locally:
    LOCALLY
    RUN echo ./build/my-artifact.txt
```

```Dockerfile
# Also bad
all:
    BUILD +run-locally
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt AS LOCAL ./build/my-artifact.txt
run-locally:
    BUILD +dep # Order still not guaranteed
    LOCALLY
    RUN echo ./build/my-artifact.txt
```

Here, the mistake is that the order of operations is not guaranteed. Earthly does not know that the two targets depend on each other, and therefore might decide to run them out of order. It might work sometimes, but it is not guaranteed that it will work every time.

To address this, again, the relationship between the two targets should be declared via `COPY` and an artifact reference.

```Dockerfile
# Good
all:
    BUILD +run-locally
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt
run-locally:
    LOCALLY
    COPY +dep/my-artifact.txt ./build/my-artifact.txt
    RUN echo ./build/my-artifact.txt
```

### Use `WITH DOCKER --load=+my-target` to pass images to `LOCALLY` targets

Earthly is able to output Docker images to the local Docker daemon at the end of each build. However, when requiring an image for a `LOCALLY` target, the image needs to be output in the *middle* of the build.

```Dockerfile
# Bad
all:
    BUILD +build-img
    BUILD +run-img
build-img:
    ...
    SAVE IMAGE my-co/my-img:latest
run-img:
    LOCALLY
    RUN docker run my-co/my-img:latest
```

The above will not work as the output will take place at the end of the build only. In addition, Earthly is unaware that there is a dependency between the two targets. To address this, we need to use `WITH DOCKER --load` and a [target reference](https://docs.earthly.dev/docs/guides/target-ref):

```Dockerfile
# Good
all:
    BUILD +run-img
build-img:
    ...
    SAVE IMAGE my-co/my-img:latest
run-img:
    LOCALLY
    WITH DOCKER --load=+build-img
        RUN docker run my-co/my-img:latest
    END
```

The `--load` instruction will inform Earthly of the dependency and will therefore cause the image to be output right before the `WITH DOCKER` `RUN` command executes.

### Avoid non-deterministic behavior

It is generally recommended to avoid any non-deterministic behavior when designing Earthly builds. This may include:

* Introducing time-stamps in builds or in tags
* Generating unique IDs
* Initializing `ARG` with values that include randomness

The main reason to avoid non-deterministic behavior is to ensure that builds are repeatable, and to maximize the use of cache. If an intermediate step leads to the same result as a previous run, Earthly may be able to reuse further computation performed previously.

Many compilers, code generators and other tools might not be deterministic and there may be no way around it. Earthly still functions correctly in these cases, however there may be occasions where the cache is not fully utilized to its potential.

### Use `COPY --dir` to copy multiple directories

The classical Dockerfile `COPY` command differs from the unix `cp` in that it will copy directory *contents*, not the directories themselves. This requires that copying multiple directories to be split across multiple lines:

```Dockerfile
# Avoid: too verbose
COPY dir-1 dir-1
COPY dir-2 dir-2
COPY dir-3 dir-3
```

This is repetitive and uses more cache layers than should be necessary.

Earthly introduces a setting, `COPY --dir`, which makes `COPY` behave more like `cp` and less like the Dockerfile `COPY`. The `--dir` flag can be used therefore to copy multiple directories in a single command:

```Dockerfile
# Good
COPY --dir dir-1 dir-2 dir-3 ./
```

### Use separate images for build and production

To keep production images small, it is advisable to start from a new base image and to install only production-required dependencies and then to copy in only the final built binaries or packages. This technique may vary from language to language, depending on the ecosystem-specific tooling.

An an example, for Go, you might have a development image, that contains the entire Go development tools, including the `go` binary. After the application binary has been built via `go build`, there is no longer a need for the `go` binary. So the production image should not contain it. Here is an example:

```Dockerfile
# Avoid: production image is bloated
FROM go:1.16
RUN apk add ... # development + production dependencies
build:
    COPY ...
    RUN go mod download
    COPY ...
    RUN go build ... -o /usr/bin/app
    ENTRYPOINT ["/usr/bin/app"]
    SAVE IMAGE my-production-image:latest
```

Here is a way to address this:

```Dockerfile
# Good
FROM go:1.16
RUN apk add ... # development dependencies
build:
    COPY ...
    RUN go mod download
    COPY ...
    RUN go build ... -o ./build/app
    SAVE ARTIFACT ./build/app
image:
    FROM alpine:3.15 # start afresh
    RUN apk add ... # production dependencies only
    COPY +build/app /usr/bin/app
    ENTRYPOINT ["/usr/bin/app"]
    SAVE IMAGE my-production-image:latest
```

### Use `SAVE ARTIFACT ... AS LOCAL ...` for generated code, not `LOCALLY`

Many programming tools require the generation of code. The generated code is often used in completing a build, but also it might be required for IDEs to perform code completion. For this reason, it's often preferable that generated code is also output as local files during development.

It is recommended that any generated code is saved via `SAVE ARTIFACT ... AS LOCAL ...` via regular Earthly targets, rather than via running the generation command in `LOCALLY`. There are multiple reasons for this:

* Executing commands via `LOCALLY` loses the repeatability benefits. This means that the same command could end up generating different code, depending on the system it is being run on. Differences in the environment, such as the version of code generator installed (e.g. `protoc`), or certain environment variables (e.g. `GOPATH`) could cause the generated code to be different.
* The logic to generate code via `LOCALLY` will not be usable in the CI, as the CI script would typically enable `--strict` mode.
* If the code generation workflow requires that the generated code is committed to the repository and then used in a subsequent earthly build, it is possible that due to human error, changes will be made to the input files, without the generated code to be updated correctly. If a problem or an incompatibility is introduced in this manner, it will only show up later, for other people when they try to generate the code themselves. In worse cases, it may even go unnoticed and end up in production.

### Multi-line strings

To specify a multi-line string in Earthly, you can simply start quotes on one line and end them on another.

```Dockerfile
# Bad
RUN echo "this is a" > /tmp/file
RUN echo "multi-line string" >> /tmp/file
RUN echo "that goes" >> /tmp/file
RUN echo "on" >> /tmp/file
RUN echo "and on" >> /tmp/file
ARG MULTILINE_STRING=$(cat /tmp/file)
```

```Dockerfile
# Good
ARG MULTILINE_STRING="this is a
multi-line string
that goes
on
and on"
```

### Multi-line commands

To execute commands that may span multiple lines, you can use the line continuation character (`\`). Remember to chain multiple shell commands via `&&` in order to correctly exit if one of the commands fails.

```Dockerfile
RUN go build ... && \
    if [ "$FOO" = "bar" ]; then \
        echo "spaghetti" > ./default-food.txt ;\
    fi
```

### Copying files from outside the build context

It is generally advisable to avoid copying files outside of the build context. If a file is required from a sibling directory, or from a parent directory, it is recommended that those files are exported via `SAVE ARTIFACT` and then copied over using an artifact reference.

```
├── dir1
|   └── some-file.txt
└── dir2
    ├── other-files...
    └── Earthfile
```

```Dockerfile
# ./dir2/Earthfile
# Bad: does not work
COPY ../dir1/some-file.txt ./
```

In the above example, the file `some-file.txt` is copied from the sibling directory `dir1`. This will not work in Earthly as the file is not in the build context of `./dir2/Earthfile` (the build context in this case is `./dir2`). To address this issue, we can create an Earthfile in `dir1` that exports the file `some-file.txt` as an artifact.

```
├── dir1
|   ├── some-file.txt
|   └── Earthfile
└── dir2
    ├── other-files...
    └── Earthfile
```

```Dockerfile
# ./dir1/Earthfile
VERSION 0.6
FROM alpine:3.15
WORKDIR /work
file:
    COPY some-file.txt ./
    SAVE ARTIFACT ./some-file.txt
```

```Dockerfile
# ./dir2/Earthfile
# Good
COPY ../dir1+file/some-file.txt ./
```

The passing of the file as an artifact will also help create a build API of `dir1`, where all the files required outside of it are explicitly exported.

If a file is needed and there is no good way of adding an Earthfile to the directory containing it (e.g. a common file from the user's home directory), then an option is to use `LOCALLY`.

```Dockerfile
file:
    LOCALLY
    SAVE ARTIFACT $HOME/some-file.txt
do-something:
    COPY +file/some-file.txt ./
```

Note, however, that `LOCALLY` is not allowed in `--strict` mode (or in `--ci` mode), as it introduces a dependency from the host machine, which may interfere with the repeatability property of the build.

Although performing a `COPY ../` is not possible in Earthly today, there are some rare, but valid use-cases for this functionality. This is being discussed in GitHub issue [#1221](https://github.com/earthly/earthly/issues/1221).

### Repository structure: Place build logic as close to the relevant code as possible

When designing builds, it is advisable to place lower-level build logic closer to the code that it is building. This can be achieved by splitting Earthly builds across multiple Earthfiles, and placing some of the Earthfiles deeper inside the directory structure. The lower-level Earthfiles can then export artifacts and/or images via `SAVE ARTIFACT` or `SAVE IMAGE` commands, respectively. Those artifacts can then be referenced in higher-level Earthfiles via artifact and target references (`COPY ./deep/dir+some-target/an/artifact ...`, `FROM ./some/path+my-target`).

This allows for low coupling between modules within your code and creates a "build API" for your directories, whereby all externally accessible artifacts are exposed explicitly.

As one example, you might find the [monorepo example](https://github.com/earthly/earthly/tree/main/examples/monorepo) to be a useful case-study. However, even when a repository contains a single project, you might still find it useful to split logic across multiple Earthfiles. An example might be including Protocol Buffers generation logic inside the subdirectory containing the `.proto` files, in its own Earthfile.

For a real-world example, you can also take a look at Earthly's own build, where several Earthfiles are scattered across the repository to help organize build logic across modules, very much like regular code. Here are some examples:

* [`ast/parser`](https://github.com/earthly/earthly/tree/main/ast/parser) - Earthfile contains the logic for generating Go source code based on an ANTLR grammar.
* [`ast/parser/tests`](https://github.com/earthly/earthly/tree/main/ast/tests) - Earthfile contains logic for running AST-specific tests.
* [`buildkitd`](https://github.com/earthly/earthly/tree/main/buildkitd) - Earthfile contains the logic for building the Earthly buildkit image.
* [`tests`](https://github.com/earthly/earthly/tree/main/tests) - Earthfile contains logic for executing e2e tests.
* [`release/**/`](https://github.com/earthly/earthly/tree/main/release) - Multiple Earthfiles contain logic used for the release of Earthly.
* [The main Earthfile](https://tinyurl.com/yt3d3cx6) - ties everything together, referencing the various targets across the sub-directories.

### Repository structure: Do not place all Earthfiles in a dedicated directory

A common practice when using Dockerfiles is to place all Dockerfiles in a special directory of the repository.

```
# Pattern common for Dockerfiles, but should be avoided for Earthfiles
├── app1-src-dir
|   └── ...
├── app2-src-dir
|   └── ...
├── app3-src-dir
|   └── ...
└── services
    ├── app1.Dockerfile
    ├── app2.Dockerfile
    └── app3.Dockerfile
```

And then running `docker build -f ./services/app1.Dockerfile ./app1-src-dir ...` and so on.

In Earthly, however, this is an anti-pattern, for a couple reasons:

* Every repository using Earthly should have a common structure, to help the user navigate the build. The convention is that Earthfiles are as close to the code as possible, with some high-level targets exposed in the root of the repository, or the root of the directory containing the code for a specific app. Having this convention helps the users who have not written the Earthfiles to quickly be able to browse around and understand the build, at least at a high level.
* Cross-directory and cross-repository references will point to directories where the user expects an Earthfile to be present, and then to a specific target or UDC within that Earthfile. It is important for this discoverability to be available to anyone browsing the build code and understanding the connections between Earthfiles.

For these reasons, Earthly does not support placing all Earthfiles in a single directory, nor the equivalent of a `docker build -f` option.

### Pattern: Pass-through artifacts or images

If a target acts as a wrapper for another target and that other target produces artifacts, you may find it useful for the wrapper to also emit the same artifacts. Consider the following example of the target `+build-for-windows`:

```Dockerfile
# No pass-through artifacts
VERSION 0.6
FROM alpine:3.15
build:
    ARG some_arg=...
    ARG another_arg=...
    ARG os=linux
    RUN ...
    SAVE ARTIFACT ./output
build-for-windows:
    BUILD +build --some_arg=... --another_arg=... --os=windows
```

```Dockerfile
# With pass-through artifacts
VERSION 0.6
FROM alpine:3.15
build:
    ARG some_arg=...
    ARG another_arg=...
    ARG os=linux
    RUN ...
    SAVE ARTIFACT ./output
build-for-windows:
    COPY (+build --some_arg=... --another_arg=... --os=windows) ./
    SAVE ARTIFACT ./*
```

The fact that `+build-for-windows` itself exports the artifacts means that it can be referenced directly in other targets as `COPY +build-for-windows/output ./`.

Similarly, if a target emits an image, then that image can be also emitted by a wrapping target like so:

```Dockerfile
# No pass-through image
VERSION 0.6
FROM alpine:3.15
build:
    ARG some_arg=...
    ARG another_arg=...
    RUN ...
    SAVE IMAGE some-intermediate-image:latest
build-wrapper:
    BUILD +build --some_arg=... --another_arg=...
```

```Dockerfile
# With pass-through image
VERSION 0.6
FROM alpine:3.15
build:
    ARG some_arg=...
    ARG another_arg=...
    RUN ...
    SAVE IMAGE some-intermediate-image:latest
build-wrapper:
    FROM +build --some_arg=... --another_arg=...
    SAVE IMAGE i-can-give-this-another-name:latest
```

This allows for `+build-wrapper` to reuse the logic in `+build`, but ultimately to create an image that is saved under a different name. This can then be used in a `WITH DOCKER --load` statement directly (whereas if there was no image pass-through, then `+build-wrapper` couldn't have been used).

### Use `earthly/dind`

When using `WITH DOCKER`, it is recommended that you use the official `earthly/dind` image (preferably `:alpine`) for running Docker-in-Docker. Earthly's `WITH DOCKER` requires that the Docker engine is installed already in the image it is running in.

If Docker engine is not detected, `WITH DOCKER` will need to first install it - it usually does so automatically - however, the cache will be inefficient. Consider the following example:

```Dockerfile
# Avoid
integration-test:
    FROM some-other-image:latest
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml
        RUN ...
    END
```

Let's assume that `some-other-image:latest` does not already have Docker engine installed. This means that on the `WITH DOCKER` line, Earthly will add a hidden installation step, to add Docker engine. This takes some time to execute, but it will work.

The problem, however, will be apparent when there is a change (no matter how small) to `docker-compose.yml`. That will cause the build to re-execute without cache from the `COPY` command onwards, meaning that the installation of Docker engine will be repeated.

A simple way to fix this is to use an earthly-provided [UDC](https://docs.earthly.dev/docs/guides/udc) to install Docker engine before the `COPY` command. Please note that this particular UDC is fastest when ran on top of an alpine-based image.

```Dockerfile
# Better
integration-test:
    FROM some-other-image:latest
    DO github.com/earthly/lib+INSTALL_DIND
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml
        RUN ...
    END
```

The best supported option, however, is to use the `earthly/dind` image, if possible.

```Dockerfile
# Best - if possible
integration-test:
    FROM earthly/dind:alpine
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml
        RUN ...
    END
```

### Pattern: Saving artifacts resulting from a `WITH DOCKER`

In Earthly, `WITH DOCKER` starts up a transient Docker daemon for that specific instruction and then shuts it down and completely wipes its data afterwards. That does not mean, however, that you cannot export any information from it (or from any container running within), to be used in another part of the build. Although you may not run any non-`RUN` commands within `WITH DOCKER`, you can still use `SAVE ARTIFACT` (and any other command) after the `WITH DOCKER` instruction. The Docker daemon's data is wiped - but the rest of the build environment remains intact.

```Dockerfile
WITH DOCKER ...
    RUN docker run -v ./screenshots:/screenshots ... && \
        docker logs ... >./full-logs.txt && \
        docker inspect ... >./some-docker-state.json
END
SAVE ARTIFACT ./screenshots
SAVE ARTIFACT ./full-logs.txt
SAVE ARTIFACT ./some-docker-state.json
```

## Usage-specific

### Use `--ci` when running in CI

Build scripts serve slightly different purposes when they are run in CI compared to when they are executed for local development. Most of the logic is similar (hence Earthly attempts to unify the two concepts in a single syntax), but there are some small differences.

For example, for development purposes, you may use commands such as `LOCALLY`, which cause Earthly to be less repeatable, and yet might satisfy very much needed use-cases that are typically out of scope of a CI build.

In addition, in CI it is much more likely that shared caching will be needed, while outputting artifacts and images in the CI's host environment itself would not be needed.

For these reasons, Earthly comes with the `--ci` flag, which simply expands to `--no-output --use-inline-cache --save-inline-cache --strict`. The `--ci` flag therefore, prevents the use of commands that are not repeatable, enables inline caching and disables outputting artifacts and images on the CI host.

### Avoid `LOCALLY` and other non-strict commands

Certain Earthly functionality is only meant to be used for local development only. Most such commands do not fully abide by the Earthly spirit of repeatable builds, however, for certain specific development use-cases they are needed and therefore Earthly provides them. When Earthly is used in `--strict` mode (`earthly --strict +my-target` or `earthly --ci +my-target`), the usage of these commands is not allowed.

For this reason, it is recommended to avoid using these commands as much as possible, as doing so will:

1. Cause Earthly to behave in a non-repeatable way across other platforms, as it will rely on host-specific environment configuration.
2. Disable caching.
3. Cause the specific targets to not work at all when `--ci` is passed in.

An example of a command that is not allowed in strict mode is `LOCALLY`. The `LOCALLY` command skips the sandboxing of the build and executes all commands directly on the host machine.

Examples of valid cases where `LOCALLY` may be used are:

* installing dependencies on the host machine (e.g. to help IDEs provide better suggestions)
* executing tests on the host docker daemon, to help with inspection and debugging
* executing development commands which would otherwise require copying very large amounts of files to the sandboxed build environment

Note, however, that none of these cases are needed in a CI environment, and ultimately these commands are not regularly tested by a CI, which means they may break more frequently.

### Pattern: Push on the `main` branch only

When using Earthly in a sandboxed CI, it may be useful to perform pushes on occasion, in order to populate shared caches. In addition, image pushes might also help developers to grab pre-built images for local use for various development workflows.

Pushing too often can result in slowing down builds due to the upload time, while pushing too infrequently results in stale cache or stale development images.

A good balance is often to perform pushes on the `main` branch only, and to disable any pushing on PR builds. Although the `main` build will be slower, it will allow for maximum use of cache in PR builds, without the slowdown of further pushes.

Main branch build: `earthly --ci --push +target`. PR build: `earthly --ci +target`.

The push option can also be configured via the env var `EARTHLY_PUSH`, which may be easier to manipulate in your CI of choice.

A more extreme case of this idea can be to use explicit maximum cache: `earthly --ci --push --remote-cache=.... --max-remote-cache +target`. The idea, again is to tradeoff performance on the `main` branch, for the benefit of faster PR builds. Whether this is actually beneficial needs to be measured on a project-by-project basis, however.

### Do not expose cache image tags publicly if the cache contains private code or dependencies

When using shared caching, Earthly has the ability to save some intermediate information about the build in a Docker registry of choice. Note, however, that the intermediate cache may also contain private code or dependencies, which could be exposed via the cache in some cases. Even if the final image only contains compiled binaries, it may still be possible to access intermediate layers that lead to the fully compiled binaries - some of which may contain private code or dependencies.

As such, when working on a closed-source project, it is advisable to only use private image repositories to prevent any code leaks.

### Technique: Use `earthly -i` to debug failures

In Earthly it is possible to drop into the container of a failed step to diagnose the failure better. To turn on this setting you can use the `-i` flag: `earthly -i +my-target`. Once dropped into the container's shell, you may use the up arrow to pre-populate the previously failed command should you wish to retry it or amend it. To exit the shell, press `Ctrl+D`.

### Run everything in a single Earthly invocation, do not wrap Earthly

Historically, build scripts have been constructed by cobbling up multiple technologies together: Makefiles, Bash scripts, Dockerfiles, Python scripts, Ruby scripts, and so on. The possibilities are endless, but also the readability and maintainability of the scripts suffer.

Earthly has been designed with a few key goals in mind:

* Repeatability - the builds should just work on another system
* Readability - the builds should be understandable by any team member on the team, without much effort
* A universal CI script - a script that contains all the information needed for the CI to perform a complete build

In this spirit, Earthly has been designed to not require any wrapping around it. Here are some examples of antipatterns:

* **Antipattern**: Earthly is called repeatedly in a single script in order to process intermediate results and then pass those results to later invocations.
* **Antipattern**: Downloading dependencies outside of Earthly and then copying them in.
* **Antipattern**: Performing a build without `--push` and then repeating the same build, but with `--push` enabled.
* **Antipattern**: Computing the value of an `ARG` outside of Earthly and then calling Earthly with that value.
* **Antipattern**: Running `earthly` in a bash `for` loop, to process multiple targets as separate builds.
* **Antipattern**: Running `earthly` repeatedly, rather than using an `all` target encapsulating all the targets needed to be built.
* **Antipattern**: Running `earthly` repeatedly with `--no-cache`, to control the order of a deployment, instead of using `RUN --push` adequately.

All of the above should be avoided as they hinder repeatability and/or they are abusing Earthly features in ways Earthly was not designed for. If a wrapping script is used outside of Earthly, it means that the script is not containerized, which means that the script is susceptible to host environment nuances.

The differences can be somewhat surprising: `make` and `sed` can be different on a Mac compared to a Linux machine, for example. Various linux distributions might have different versions of `bash` installed. Environment variables could play surprising roles. Causes for inconsistencies can sip in from anywhere, making builds more difficult to maintain.

To keep your build scripts uniform across projects (and thus more readable) and to keep them repeatable, it is best if `earthly` is used directly and with minimal argument overrides.

### Use `RUN --ssh` for passing host SSH keys to builds

Earthly provides a way to pass-through access to your host's SSH keys to the build, by proxying the host's ssh-agent connection inside the build. This may be useful if you need to access private repositories where you authenticate with SSH. An example of such a case might be downloading Go dependencies from private repositories:

```Dockerfile
RUN --ssh go mod download
```

### Future: Saving an artifact even if the build fails

We are aware of the lack of capability here. Please follow GitHub issues [#988](https://github.com/earthly/earthly/issues/988) and [#587](https://github.com/earthly/earthly/issues/587) for updates.

There are currently workarounds for this (see [this comment](https://github.com/earthly/earthly/issues/988#issuecomment-870504677) and [this comment](https://github.com/earthly/earthly/issues/988#issuecomment-981088796)), however they have significant limitations.

# Guides

# Authenticating Git and image registries

This page guides you through passing Git and Docker authentication to Earthly builds, to empower related Earthly features, like `GIT CLONE` or `FROM`.

{% hint style="danger" %}
**Important**

This page is NOT about passing Git or Docker credentials for your own custom commands within builds. For those cases, use the [`RUN --secret`](https://docs.earthly.dev/earthfile#run) feature.
{% endhint %}

## Git authentication

A number of Earthly features use Git credentials to perform remote Git operations:

* Resolving a build context when referencing remote targets
* The `GIT CLONE` command

There are two possible ways to pass Git authentication to Earthly builds:

* Via SSH agent socket (for SSH-based authentication)
* Via username-password (usually for HTTPS Git URLs)

#### Auto authentication

Earthly defaults to an `auto` authentication mode, where ssh-based authentication is automatically attempted, and falls back to https-based cloning.

{% hint style="info" %}
If you are having trouble accessing a private repository and want to use ssh-based authentication, first make sure `ssh-agent` is running and the `SSH_AUTH_SOCK` environment variable is set. If not, you can start it with `eval $(ssh-agent)`.

Next make sure your private key has been added by running `ssh-add <path to key>`.
{% endhint %}

For users who want explicit control over git authentication, the following sections explain how.

#### SSH agent socket

Earthly uses the environment variable `SSH_AUTH_SOCK` to detect where the SSH agent socket is located and mounts that socket to the BuildKit daemon container. (As an exception, on Mac, Docker's compatibility SSH auth socket is used instead).

If you need to override the SSH agent socket, you can set the environment variable `EARTHLY_SSH_AUTH_SOCK`, or use the `--ssh-auth-sock` flag to point to an alternative SSH agent.

In order for the SSH agent to have the right credentials available, make sure you run `ssh-add` before executing Earthly builds.

Another key setting is the `auth` mode for the git site that hosts the repository. By default earthly automatically default to `ssh` authentication if the ssh auth agent is running and has at least 1 key loaded, otherwise `earthly` will fallback to using non-authenticated HTTPS.

Sites can be explicitly added to the [earthly config file](https://docs.earthly.dev/docs/earthly-config) under the git section in order to override the auto-authentication mode:

```yaml
git:
    git.example.com:
        auth: ssh
        user: git
```

#### Username-password authentication

Username-password based authentication can be configured in the [earthly config file](https://docs.earthly.dev/docs/earthly-config) under the git section:

```yaml
git:
    github.com:
        auth: https
        user: <username>
        password: <password>
    gitlab.com:
        auth: https
        user: <username>
        password: <password>
```

If no `user` or `password` are found, earthly will check for entries under [`~/.netrc`](https://everything.curl.dev/usingcurl/netrc).

**Global override via environment variables (deprecated)**

Alternatively, environment variables can be set which will be override all host entries from the config file:

* `GIT_USERNAME`
* `GIT_PASSWORD`

However, environment variable authentication are now deprecated in favor of using the configuration file instead.

#### Self-hosted and private Git Repositories

Currently, `github.com`, `gitlab.com`, and `bitbucket.org` have been tested as SCM providers. Without any host-specific configuration, Earthly first attempts to perform a clone over SSH on the default SSH port (22), and will fallback to HTTPS, followed by HTTP. In the event access can only be established over HTTP, Earthly will refuse to send credentials due to the insecure nature of HTTP.

Earthly can be configured to use a non-standard SSH port, by using the `port` config option:

```yaml
git:
    ghe.internal.mycompany.com:
        auth: ssh
        user: git
        port: 2222
```

When Earthly encounters a remote reference such as `ghe.internal.mycompany.com/user/repo+some-target`, the git repository will be cloned using an explicit SSH scheme, for example: `git clone ssh://git@ghe.internal.mycompany.com:2222/user/repo.git`.

The explicit ssh-scheme is an absolute path on the server's file-system; if the git repositories are located in a different location (e.g. `/var/git/...`), a `prefix` configuration option can be specified.

{% hint style="info" %}
**Remapping Git Repositories Paths Using Regular Expressions**

The `port` and `prefix` configuration options are the preferred way to configure self-hosted git repositories; however prior to the introduction of these options, it was suggested to use a regular expression and substitution pattern:

```yaml
git:
    ghe.internal.mycompany.com:
        pattern: 'ghe.internal.mycompany.com/([^/]+)/([^/]+)'
        substitute: 'ssh://git@ghe.internal.mycompany.com:22/$1/$2.git'
        auth: ssh
```

{% endhint %}

## Docker authentication

Docker credentials are used in Earthly for inheriting from private images (via `FROM`) and for pushing images (via `SAVE IMAGE --push`).

Docker authentication works automatically out of the box. It uses the same Docker libraries to infer the location of the credentials on the system and optionally invoke any necessary credentials store helper to decrypt them.

### Manually

All you have to do as a user is issue the command

```bash
docker login --username <username>
```

before issuing earthly commands, if you have not already done so in the past. If you run into troubles, [you can find out more about `docker login` here](https://docs.docker.com/engine/reference/commandline/login/).

### Credential Helpers

Docker can use various credential helpers to automatically generate and use credentials on your behalf. These are usually created by cloud providers to allow Docker to authenticate using the cloud providers own credentials.

You can see examples of configuring Docker to use these, and working with Earthly here:

* [Pushing and Pulling Images with AWS ECR](https://docs.earthly.dev/docs/guides/configuring-registries/aws-ecr)
* [Pushing and Pulling Images with GCP Artifact Registry](https://docs.earthly.dev/docs/guides/configuring-registries/gcp-artifact-registry)
* [Pushing and Pulling Images with Azure ACR](https://docs.earthly.dev/docs/guides/configuring-registries/azure-acr)

## See also

* The [earthly command reference](https://docs.earthly.dev/docs/earthly-command)

# Target, artifact and command referencing

This page describes the different types of references used in Earthly:

* Target references: `<project-ref>+my-target`
* Artifact references: `<project-ref>+my-target/my-artifact.bin`
* Image references (same as target references)
* Command references: `<project-ref>+MY_COMMAND`
* Project references (the prefix of the above references): `github.com/foo/bar`, `./my/local/path`

## Target reference

Target references point to an Earthly target. They have the general form

`<project-ref>+<target>`

Target references distinguish themselves from command references (see below) by having a name in all-lower-case, kebab-case (e.g. `+my-target`).

Here are some examples:

* `+build`
* `./js+deps`
* `github.com/earthly/earthly:v0.1.0+earthly`

## Artifact reference

Artifact references are similar to target references, except that they have an artifact path at the end. It has the following form

`<target-ref>/<artifact-path>`

Here are some examples:

* `+build/my-artifact`
* `+build/some/artifact/deep/in/a/dir`
* `./js+build/dist`
* `github.com/earthly/earthly:v0.1.0+earthly/earthly`

## Image reference

Because there can only be one image per target, image references have the exact same format as target references.

The only difference is the context where they are used. For example, a `FROM` command takes an image reference. While a `BUILD` command takes a target reference.

## Command reference

Command references point to a user-defined command (UDC) in an Earthfile. They have the general form

`<project-ref>+<command>`

Command references distinguish themselves from target references by having a name in all-caps, snake-case (e.g. `+MY_COMMAND`).

Here are some examples:

* `+COMPILE`
* `./js+NPM_INSTALL`
* `github.com/earthly/earthly:v0.1.0+DOWNLOAD_DIND`

For more information on UDCs, see the [User-defined commands guide](https://docs.earthly.dev/docs/guides/udc).

## Project references

![Target and artifact reference syntax](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-5dbefb8f66b7a76b7ac0f0c62adbecbac88bc5b3%2Fref-infographic-v2.png?alt=media\&token=dff92a05-5b02-4a29-a9b1-6c351e54626b)

Project references appear in target, artifact and command references. They point to the Earthfile containing the respective target, artifact or command. Below are the different types of project references available in Earthly.

### Local, internal

The simplest form, is where a target, command or artifact is referenced from the same Earthfile. In this case, the project reference is simply **the empty string**. Here are some examples of this type of project reference being used in various other references:

| Project ref        | Target ref       | Artifact ref                     | Command ref       |
| ------------------ | ---------------- | -------------------------------- | ----------------- |
| (**empty string**) | `+<target-name>` | `+<target-name>/<artifact-path>` | `+<command-name>` |
| (**empty string**) | `+build`         | `+build/out.bin`                 | `+COMPILE`        |

In this form, Earthly will look for the target within the same Earthfile. We call this type of referencing local, internal. Local, because it comes from the same system, and internal, because it is within the same Earthfile.

### Local, external

Another form, is where a target, command or artifact is referenced from a different directory. In this form, the path to that directory is specified before `+`. It must always start with either `./`, `../` or `/`, on any operating system (including Windows). Example:

| Project ref             | Target ref                            | Artifact ref                                          | Command ref                            |
| ----------------------- | ------------------------------------- | ----------------------------------------------------- | -------------------------------------- |
| `./path/to/another/dir` | `./path/to/another/dir+<target-name>` | `./path/to/another/dir+<target-name>/<artifact-path>` | `./path/to/another/dir+<command-name>` |
| `./js`                  | `./js+build`                          | `./js+build/out.bin`                                  | `./js+COMPILE`                         |

It is recommended that relative paths are used, for portability reasons: the working directory checked out by different users will be different, making absolute paths infeasible in most cases.

### Remote

Another form of a project reference is the remote form. In this form, the recipe and the build context are imported from a remote location. It has the following form:

| Project ref                                                 | Target ref                                                                | Artifact ref                                                                              | Command ref                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `<vendor>/<namespace>/<project>/path/in/project[:some-tag]` | `<vendor>/<namespace>/<project>/path/in/project[:some-tag]+<target-name>` | `<vendor>/<namespace>/<project>/path/in/project[:some-tag]+<target-name>/<artifact-path>` | `<vendor>/<namespace>/<project>/path/in/project[:some-tag]+<command-name>` |
| `github.com/earthly/earthly/buildkitd`                      | `github.com/earthly/earthly/buildkitd+build`                              | `github.com/earthly/earthly/buildkitd+build/out.bin`                                      | `github.com/earthly/earthly/buildkitd+COMPILE`                             |
| `github.com/earthly/earthly:v0.1.0`                         | `github.com/earthly/earthly:v0.1.0+build`                                 | `github.com/earthly/earthly:v0.1.0+build/out.bin`                                         | `github.com/earthly/earthly:v0.1.0+COMPILE`                                |

### Import reference

Finally, the last form of project referencing is an import reference. Import references may only exist after an `IMPORT` command, which helps resolve the reference to a full project reference of the types above.

| Import command                                | Project ref      | Target ref                     | Artifact ref                                   | Command ref                     |
| --------------------------------------------- | ---------------- | ------------------------------ | ---------------------------------------------- | ------------------------------- |
| `IMPORT <full-project-ref> AS <import-alias>` | `<import-alias>` | `<import-alias>+<target-name>` | `<import-alias>+<target-name>/<artifact-path>` | `<import-alias>+<command-name>` |
| `IMPORT github.com/earthly/earthly/buildkitd` | `buildkitd`      | `buildkitd+build`              | `buildkitd+build/out.bin`                      | `buildkitd+COMPILE`             |
| `IMPORT github.com/earthly/earthly:v0.1.0`    | `earthly`        | `earthly+build`                | `earthly+build/out.bin`                        | `earthly+COMPILE`               |

Here is an example in an Earthfile:

```Dockerfile
IMPORT github.com/earthly/earthly/buildkitd

...

BUILD buildkitd+buildkitd
```

## Implicit Base Target Reference

All Earthfiles start with a base recipe. This is the only recipe which does not have an explicit target name - the name is always implied to be `base`. All other target implicitly inherit from `base`. You can imagine that all recipes start with an implicit `FROM +base`

```
# base recipe
FROM golang:1.15-alpine3.13
WORKDIR /go-example

build:
    # implicit FROM +base
    RUN echo "Hello World"
```

## Canonical form

Most references have a canonical form. It is essentially the remote form of the same target, with repository and tag inferred. The canonical form can be useful as a universal identifier for a target.

For example, depending on where the files are stored, the `+build` target could have the canonical form `github.com/some-user/some-project/some/deep/dir:master+build`, where `github.com/some-user/some-project` was inferred as the Git location, based on the Git remote called `origin`, and `/some/deep/dir` was inferred as the sub-directory where `+build` exists within that repository. The Earthly tag is inferred using the following algorithm:

* If the current HEAD has at least one Git tag, then use the first Git tag listed by Git, otherwise
* If the repository is not in detached HEAD mode, use the current branch, otherwise
* Use the current Git hash.

If no Git context is detected by Earthly, then the target does not have a canonical form.

# Build arguments and secrets

## Introduction

One of the core features of Earthly is support for build arguments. Build arguments can be used to dynamically set environment variables inside the context of [RUN commands](https://docs.earthly.dev/earthfile#run).

Build arguments can be passed between targets or from the command line. They encourage writing generic Earthfiles and ultimately promote greater code-reuse.

Additionally, Earthly defines secrets which are similar to build arguments, but are exposed as environment variables when explicitly allowed.

## A Quick Example

Arguments are declared with the [ARG](https://docs.earthly.dev/earthfile#arg) keyword.

Let's consider a "hello world" example that allows us to change who is being greeted (e.g. hello banana, hello eggplant etc). We will create a hello target that accepts the `name` argument:

```Dockerfile
VERSION 0.6
FROM alpine:latest

hello:
    ARG name
    RUN echo "hello $name"
```

Then we will specify a value for the `name` argument on the command line when we invoke `earthly`:

```bash
earthly +hello --name=world
```

This will output

```
    buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
alpine:latest | --> Load metadata linux/arm64
         +foo | --> FROM alpine:latest
         +foo | [██████████] 100% resolve docker.io/library/alpine:latest@sha256:21a3deaa0d32a8057914f36584b5288d2e5ecc984380bc0118285c70fa8c9300
         +foo | name=world
         +foo | --> RUN echo "hello $name"
         +foo | hello world
       output | --> exporting outputs
```

If we re-run `earthly +hello --name=world`, we will see that the echo command is cached (and won't re-display the hello world text):

```
+foo | *cached* --> RUN echo "hello $name"
```

## Default values

Arguments may also have default values, which may be either constant or dynamic. For example, the following target will greet the name identified by the arg `name` (which has a default value of John), with the current time:

```Dockerfile
hello:
   ARG time=$(date +%H:%M)
   ARG name=John
   RUN echo "hello $name, it is $time"
```

```
alpine:latest | --> Load metadata linux/arm64
        +base | --> FROM alpine:latest
        +base | [██████████] 100% resolve docker.io/library/alpine:latest@sha256:21a3deaa0d32a8057914f36584b5288d2e5ecc984380bc0118285c70fa8c9300
       +hello | --> ARG time = RUN $(date +%H:%M)
       +hello | --> RUN echo "hello $name, it is $time"
       +hello | hello John, it is 23:21
       output | --> exporting outputs
```

If an arg has no default value, then the default value is the empty string.

## Overriding Argument Values

Argument values can be set multiple ways:

1. On the command line

   The value can be directly specified on the command line (as shown in the previous example):

   ```
   earthly +hello --HELLO=world --FOO=bar
   ```

2. From environment variables

   Similar to above, except that the value is an environment variable:

   ```bash
   export HELLO="world"
   export FOO="bar"
   earthly +hello --HELLO="$HELLO" --FOO="$FOO"
   ```

3. Via the `EARTHLY_BUILD_ARGS` environment variable

   The value can also be set via the `EARTHLY_BUILD_ARGS` environment variable.

   ```bash
   export EARTHLY_BUILD_ARGS="HELLO=world,FOO=bar"
   earthly +hello
   ```

   This may be useful if you have a set of build args that you'd like to always use and would prefer not to have to specify them on the command line every time. The `EARTHLY_BUILD_ARGS` environment variable may also be stored in your `~/.bashrc` file, or some other shell-specific startup script.
4. From a `.env` file

   It is also possible to create an `.env` file to contain the build arguments to pass to earthly. First create an `.env` file with:

   ```
   name=eggplant
   ```

   Then simply run earthly:

   ```bash
   earthly +hello
   ```

## Passing Argument values to targets

Build arguments can also be set when calling build targets. If multiple build arguments values are defined for the same argument name, Earthly will build the target for each value; this makes it easy to configure a "build matrix" within Earthly.

For example, we can create a new `greetings` target which calls `+hello` multiple times:

```dockerfile
greetings:
    BUILD +hello \
        --name=world \
        --name=banana \
        --name=eggplant
```

Then when we call `earthly +greetings`, earthly will call `+hello` three times:

```
     buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
 alpine:latest | --> Load metadata linux/amd64
         +base | --> FROM alpine:latest
         +base | [██████████] resolve docker.io/library/alpine:latest@sha256:69e70a79f2d41ab5d637de98c1e0b055206ba40a8145e7bddb55ccc04e13cf8f ... 100%
        +hello | name=banana
        +hello | --> RUN echo "hello $name"
        +hello | name=eggplant
        +hello | --> RUN echo "hello $name"
        +hello | name=world
        +hello | --> RUN echo "hello $name"
        +hello | hello banana
        +hello | hello eggplant
        +hello | hello world
        output | --> exporting outputs
```

In addition to the `BUILD` command, build args can also be used with `FROM`, `COPY`, `WITH DOCKER --load` and a number of other commands:

```Dockerfile
BUILD +hello --name=world
COPY (+hello/file.txt --name=world) ./
FROM +hello --name=world
WITH DOCKER --load=(+hello --name=world)
  ...
END
```

Another way to pass build args is by specifying a dynamic value, delimited by `$(...)`. For example, in the following, the value of the arg `name` will be set as the output of the shell command `echo world` (which, of course is simply `world`):

```Dockerfile
BUILD +hello --name=$(echo world)
```

## Passing secrets to RUN commands

Secrets are similar to build arguments; however, they are *not* defined in targets, but instead are explicitly defined for each `RUN` command that is permitted to access them.

Here's an example Earthfile that accesses a secret stored under `+secrets/passwd` and exposes it under the environment variable `mypassword`:

```dockerfile
FROM alpine:latest
hush:
    RUN --secret mypassword=+secrets/passwd echo "my password is $mypassword"
```

If the environment variable name is identical to the secret ID. For example to accesses a secret stored under `+secrets/passwd` and exposes it under the environment variable `passwd` you can use the shorthand :

```dockerfile
FROM alpine:latest
hush:
    RUN --secret passwd echo "my password is $passwd"
```

{% hint style="info" %}
It's also possible to temporarily mount a secret as a file:

```dockerfile
RUN --mount type=secret,target=/root/mypassword,id=+secrets/passwd echo "my password is $(cat /root/mypassword)"
```

The file will not be saved to the image snapshot.
{% endhint %}

## Setting secret values

The value for `+secrets/passwd` in examples above must then be supplied when earthly is invoked.

This is possible in a few ways:

1. Directly, on the command line:

   ```bash
   earthly --secret passwd=itsasecret +hush
   ```

2. Via an environment variable:

   ```bash
   export passwd=itsasecret
   earthly --secret passwd +hush
   ```

   If the value of the secret is omitted on the command line Earthly will lookup the environment variable with that name.
3. Via the environment variable `EARTHLY_SECRETS`

   ```bash
   export EARTHLY_SECRETS="passwd=itsasecret"
   earthly +hush
   ```

   Multiple secrets can be specified by separating them with a comma.
4. Via the `.env` file.

   Create a `.env` file in the same directory where you plan to run `earthly` from. Its contents should be:

   ```
   passwd=itsasecret
   ```

   Then simply run earthly:

   ```bash
   earthly +hello
   ```

5. Via cloud-based secrets. This option helps share secrets within a wider team. To read more about this see the [cloud-based secrets guide](https://docs.earthly.dev/earthly-cloud/cloud-secrets).

Regardless of the approach chosen from above, once earthly is invoked, in our example, it will output:

```
+hush | --> RUN echo "my password is $mypassword"
+hush | my password is itsasecret
```

{% hint style="info" %}

#### How Arguments and Secrets affect caching

Commands in earthly must be re-evaluated when the command itself changes (e.g. `echo "hello $name"` is changed to `echo "greetings $name"`), or when one of its inputs has changed (e.g. `--name=world` is changed to `--name=banana`). Earthly creates a hash based on both the contents of the command and the contents of all defined arguments of the target build context.

However, in the case of secrets, the contents of the secret *is not* included in the hash; therefore, if the contents of a secret changes, Earthly is unable to detect such a change, and thus the command will not be re-evaluated.
{% endhint %}

## Storage of local secrets

Earthly stores the contents of command-line-supplied secrets in memory on the localhost. When a `RUN` command that requires a secret is evaluated by BuildKit, the BuildKit daemon will request the secret from the earthly command-line process and will temporarily mount the secret inside the runc container that is evaluating the `RUN` command. Once the command finishes the secret is unmounted. It will not persist as an environment variable within the saved container snapshot. Secrets will be kept in-memory until the earthly command exits.

Earthly also supports cloud-based shared secrets which can be stored in the cloud. Secrets are never stored in the cloud unless a user creates an earthly account and explicitly calls the `earthly secrets set ...` command to transmit the secret to the earthly cloud-based secrets server. For more information about cloud-based secrets, check out our [cloud-based secrets management guide](https://docs.earthly.dev/earthly-cloud/cloud-secrets).

# User-defined commands (UDCs)

User-defined commands (UDCs) are templates (much like functions in regular programming languages), which can be used to define a series of steps to be executed in sequence. In other words, it is a way to import common build steps which can be reused in multiple contexts.

Unlike targets, UDCs inherit the (1) build context and (2) the build environment from the caller. Meaning that

1. Any local `COPY` operation will use the directory where the calling Earthfile exists, as the source.
2. Any files, directories and dependencies created by a previous step of the caller are available to the UDC to operate on; and any file changes resulting from executing the UDC commands are passed back to the caller as part of the build environment.

Thus, when importing and reusing UDCs across a complex build, it is very much like reusing libraries in a regular programming language.

## Usage

UDCs are defined similarly to regular targets, with a couple of exceptions: the name is in all-uppercase, snake-case and the recipe must start with `COMMAND`. For example:

```Dockerfile
MY_COPY:
    COMMAND
    ARG src
    ARG dest=./
    ARG recursive=false
    RUN cp $(if $recursive =  "true"; then printf -- -r; fi) "$src" "$dest"
```

This UDC can be invoked from a target via `DO`

```Earthfile
build:
    FROM alpine:3.15
    WORKDIR /udc-example
    RUN echo "hello" >./foo
    DO +MY_COPY --src=./foo --dest=./bar
    RUN cat ./bar # prints "hello"
```

A few things to note about this example:

* The definition of `MY_COPY` does not contain a `FROM` so the build environment it operates in is the build environment of the caller.
* This means that `+MY_COPY` has access to the file `./foo`.
* Although the copy file operation is performed within `+MY_COPY`, its effects are seen in the environment of the caller - so the resulting `./bar` is available to the caller.

## Scope

UDCs create their own `ARG` scope, which is distinct from the caller. Any `ARG` that needs to be passed from the caller needs to be passed explicitly via `DO +COMMAND --<build-arg-key>=<build-arg-value>`, as in the following example.

```Dockerfile
build:
    ARG var=value-in-build
    # prints "something-else"
    DO +PRINT_VAR
    # prints "value-in-build"
    DO +PRINT_VAR --var=$var

PRINT_VAR:
    COMMAND
    ARG var=something-else
    RUN echo "$var"
```

Global imports and global args are inherited from the `base` target of the same Earthfile where the command is defined in (this may be distinct from the `base` target of the caller).

```Dockerfile
VERSION 0.6

ARG a_global_var=value-in-global

build:
    # prints "value-in-global"
    DO +PRINT_VAR

PRINT_VAR:
    COMMAND
    RUN echo "$a_global_var"
```

## Targets vs UDCs

Earthly targets and UDCs are Earthly's core primitives for organizing build recipes. They encapsulate build logic, and from afar they look pretty similar. However, the use-cases for each are vastly different.

In general, targets are used to produce specific build results, while UDCs are used as a way to reuse build logic, when certain commands are repeated in multiple places. UDCs work like functions or methods in an imperative programming language. Much like function calls it's helpful to imagine UDCs being executed by being inlined into the call site but in a separate variable scope.

As a real-world analogy, targets are more like factories, while UDCs are more like components that are used to put together factories.

Here is a comparison of the two primitives:

|                                                                                                 | Targets                                                          | UDCs                                                                        |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Represents a collection of Earthly commands                                                     | ✅                                                                | ✅                                                                           |
| Can reference other targets in its body                                                         | ✅                                                                | ✅                                                                           |
| Can reference other UDCs in its body                                                            | ✅                                                                | ✅                                                                           |
| Build context                                                                                   | The directory where the Earthfile resides                        | Inherited from the caller                                                   |
| Build environment, when no `FROM` is specified                                                  | Inherited from the base of its own Earthfile                     | Inherited from the caller                                                   |
| `IMPORT` statements                                                                             | Inherited from the base of its own Earthfile                     | Inherited from the base of its own Earthfile                                |
| `ARG` context                                                                                   | Creates its own scope                                            | Creates its own scope                                                       |
| Requires that `ARG`s be passed in explicitly                                                    | ✅                                                                | ✅                                                                           |
| Global `ARG` context                                                                            | Inherited from the base of its own Earthfile                     | Inherited from the base of its own Earthfile                                |
| Can output artifacts                                                                            | ✅                                                                | ❌ - can issue `SAVE ARTIFACT`, but it's the caller that emits the artifacts |
| Can output images                                                                               | ✅                                                                | ❌ - can issue `SAVE IMAGE`, but it's the caller that emits the images       |
| Can be called via `earthly` CLI                                                                 | ✅                                                                | ❌                                                                           |
| Can be used via in conjunction with an `IMPORT` (`IMPORT github.com/my-co/my-proj/some-import`) | ✅ - `FROM some-import+my-target`                                 | ✅ - `DO some-import+MY_UDC`                                                 |
| Commands that can reference it                                                                  | `FROM`, `BUILD`, `COPY`, `WITH DOCKER --load`, `FROM DOCKERFILE` | `DO`                                                                        |

# Managing cache

Earthly cache works similarly to Dockerfile layer-based caching. In fact, the same [technology](https://github.com/moby/buildkit) is used underneath.

## Cache layers

Many Earthfile commands create cache layers. A cache layer may be reused in a future build, if the conditions under which it is created are the same.

Examples of commands which create layers are `COPY` and `RUN`.

One of the main things influencing the conditions are "sources". Sources are created through commands like `COPY` and `GIT CLONE`. `RUN`, however, is not a source, even if the command itself involves downloading content from an external location. This means that a `RUN` command, on its own, would always be cached if it has been run under the same circumstances previously (except for the `RUN --push` variant).

For a primer into Dockerfile caching see [this article](https://pythonspeed.com/articles/docker-caching-model/). The same principles apply to Earthfiles.

## Cache location

Earthly cache is persisted in a docker volume called `earthly-cache` on your system. When Earthly starts for the first time, it brings up a BuildKit daemon in a Docker container, which initializes the `earthly-cache` volume. The volume is managed by Earthly's BuildKit daemon and there is a regular garbage-collection for old cache.

{% hint style="info" %}

#### Checking current cache size

You can check the current size of the cache by running:

```bash
sudo du -h /var/lib/docker/volumes/earthly-cache | tail -n 1
```

{% endhint %}

## Specifying cache size limit

The default cache size is adaptable depending on available space on your system. If you would like to limit the cache size more aggressively, you can specify a different limit by modifying the `cache_size_mb` and/or `cache_size_pct` settings in the [configuration](https://docs.earthly.dev/docs/earthly-config). For example:

```yaml
global:
  cache_size_mb: 10000
  cache_size_pct: 70
```

## Resetting cache

The cache can be safely deleted manually, if the daemon is not running

```bash
docker stop earthly-buildkitd
docker rm earthly-buildkitd
docker volume rm earthly-cache
```

However, it is easier to simply use the command

```bash
earthly prune --reset
```

which restarts the daemon and resets the contents of the cache volume.

## See also

* [Advanced local caching techniques](https://docs.earthly.dev/docs/guides/advanced-local-caching)
* [Remote caching](https://docs.earthly.dev/docs/remote-caching)

# Advanced local caching

In this article we're going to discuss various caching techniques that may be used to optimize your builds. For a primer on the basics of caching, see the [page on managing cache](https://docs.earthly.dev/docs/guides/cache).

We will discuss a specific example where dependencies are cached using multiple techniques. Let's take the following build for instance

```Dockerfile
# Earthfile

VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    COPY build.gradle ./
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin /bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib /lib AS LOCAL build/lib
```

If we ran this every time we changed the code, then the build would end up downloading all the dependencies specified in Gradle every single time. Here is how this can be improved.

### Option 1: Layer-based caching

One option is to use layer-based caching to first download all dependencies and only afterwards to copy the code and build it. Thus, when the code changes, the cache is bust after the step where we download dependencies.

```Dockerfile
# Earthfile

VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    # First, copy gradle build spec and download dependencies.
    COPY build.gradle ./
    RUN gradle build
    # Then copy code and build it.
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin /bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib /lib AS LOCAL build/lib
```

This technique is the most simple and most robust technique, however it does not always cover all situations efficiently.

### Option 2: Mount-based caching (advanced)

Consider, for instance, a situation where the dependencies themselves change frequently. For example, in Java, if the build has `SNAPSHOT` dependencies (and/or are marked in Gradle as `changing = true`), then it needs to download the latest version available for those frequently.

For these cases, the build could use a cache mount. A cache mount is a volume that gets attached to a `RUN` command and is persisted and shared between runs.

```Dockerfile
# Earthfile

VERSION 0.6
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    COPY build.gradle ./
    COPY src src
    RUN --mount=type=cache,target=/root/.gradle/caches \
        gradle build && \
        gradle install
    SAVE ARTIFACT build/install/java-example/bin /bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib /lib AS LOCAL build/lib
```

This allows the Gradle command to reuse dependencies downloaded in a previous run and would only download new and updated dependencies, if any apply. It would not download everything from scratch again.

Although this approach works for many situations, it also has some possible downsides. For example, removing a dependency from the gradle spec, will not remove it from the cache. A mild problem can be that the cache becomes bloated over time. A worse possible problem can surface due to build inconsistencies created by the contents of the cache. Although some build tools are smart enough to ignore those cached dependencies if they have been removed from the spec, the behavior will vary from tool to tool and from language to language. In some cases, the build may continue to use a cached but removed dependency, yet if the build is executed on another system, it breaks or behaves differently.

To manage these situations you can elect to reset the cache of a build, by simply running the build again with the flag `--no-cache`: `earthly --no-cache +build`. Or, you can eliminate the entire cache altogether using [`earthly prune`](https://docs.earthly.dev/earthly-command#earthly-prune).

Cache mounts are a leaky abstraction on top of the Earthly base principles by which nothing is shared. Although they are necessary to help optimize builds in some situations, care must be taken of possible edge cases whereby a build behaves differently because of the cache mount alone.

To help minimize such edge cases, Earthly only shares cache mounts between repeated builds of the *same target*, **and** only if *the build args are the same between invocations*. For more information see the [`RUN --mount` option reference](https://docs.earthly.dev/earthfile#run).

# Using Docker in Earthly

This guide walks through using Docker commands in Earthly.

## Basic usage

In order to use Docker commands (such as `docker run`), Earthly makes available isolated Docker daemons which are started and stopped on-demand. The reason for using isolated instances of Docker daemons is such that no preexisting Docker state (e.g. images, containers, networks, volumes) can influence the way the build executes. This allows Earthly to achieve high degrees of reproducibility.

Here is a quick example of running a hello-world docker container via `docker run` in Earthly:

```Dockerfile
hello:
    FROM earthly/dind:alpine
    WITH DOCKER --pull hello-world
        RUN docker run hello-world
    END
```

Let's break it down.

`FROM earthly/dind:alpine` inherits from an Earthly-supported docker-in-docker (dind) image. This is recommended, because `WITH DOCKER` requires all the Docker binaries (not just the client) to be present in the build environment.

`WITH DOCKER ... END` starts a Docker daemon for the purpose of running Docker commands against it. At the end of the execution, this also terminates the daemon and permanently deletes all of its data (e.g. daemon cached images).

`--pull hello-world` pulls the image `hello-world` from the Docker Hub. This option could have been replaced with the more traditional `docker pull hello-world`. However, the Earthly variant additionally stores the image in the Earthly cache, so that the actual pull is performed only if the image changes. Because the daemon cache is cleared after each run, `docker pull` would not achieve the same.

`RUN docker run hello-world` executes the `docker run` command in the context of the daemon created by `WITH DOCKER`.

## Loading images built by Earthly

A typical use of Docker in Earthly is running an image that has been built via Earthly itself. To achieve that, the option `WITH DOCKER --load ...=...` can be used. Here is an example:

```Dockerfile
build:
    ...
    ENTRYPOINT ...
    SAVE IMAGE my-image:latest

smoke-test:
    FROM earthly/dind:alpine
    WITH DOCKER --load test:latest=+build
        RUN docker run test:latest
    END
```

`--load test:latest=+build` takes the image produced by the target `+build` and loads it into the Docker daemon created by `WITH DOCKER` as the image with the tag `test:latest`. The tag can then be used to reference this image in other docker commands, such as `docker run`.

Notice that the image name produced as output is `my-image:latest`. This image name is not available in the `WITH DOCKER` environment, however, as it is only used to tag for use outside of Earthly. The name `test:latest` is used instead.

## Running docker-compose

It is possible to run `docker-compose` via `WITH DOCKER`, either explicitly, simply by running the `docker-compose` tool, or implicitly, via the `--compose` flag. The `--compose` flag allows you to specify a Docker compose stack that needs to be brought up before the execution of the `RUN` command. For example:

```Dockerfile
FROM earthly/dind:alpine
WITH DOCKER \
        --compose docker-compose.yml \
        --service db \
        --service api
    RUN docker run some-integration-test:latest
END
```

Using the `--compose` flag has the added benefit that any images needed by the compose stack will be automatically added to the pull list by Earthly, thus using cache efficiently.

## Performance

It's recommended to use the `earthly/dind:alpine` image for running docker-in-docker. See the best-practices' section on using [with docker](https://docs.earthly.dev/best-practices#use-earthly-dind) for more details.

## Integration testing

For more information on integration testing and working with service dependencies see our [tutorial on integration testing in Earthly](https://docs.earthly.dev/docs/guides/integration).

## Limitations of Docker in Earthly

The current implementation of Docker in Earthly has a number of limitations:

* Only one `RUN` command is allowed within the `WITH DOCKER` clause. The reason for this is that only one cache layer is used for the entire clause. You can, however, chain multiple shell commands together within a single `RUN` command. For example:

  ```Dockerfile
  WITH DOCKER
      RUN command1 && \
          command2 && \
          command3 && \
          ...
  END
  ```

* It is recommended that the target containing the `WITH DOCKER` clause inherits from a supported Docker-in-Docker (dind) image such as `earthly/dind:alpine` or `earthly/dind:ubuntu`. If your build requires the use of an alternative environment as part of a test (e.g. to run commands like `sbt test` or `go test` together with a docker-compose stack), consider placing the test itself in a Docker image, then loading that image via `--load` and running the test as a Docker container.
* If you do not use an officially supported Docker-in-Docker image, Earthly will attempt to install Docker in whatever image you have chosen. This has the drawback of not being able to use cache efficiently and is not recommended for performance reasons.
* To maximize the use of cache, all external images used should be declared via the options `--pull` or `--compose`. Even though commands such as `docker run` automatically pull an image if it is not found locally, it will do so every single time the `WITH DOCKER` clause is executed, due to Docker caching not being preserved between runs. Pre-declaring the images ensures that they are properly cached by Earthly to minimize unnecessary redownloads.
* `docker build` cannot be used to build Dockerfiles. However, the Earthly command `FROM DOCKERFILE` can be used instead. See [alternative to docker build](#alternative-to-docker-build) below.
* The state of the Docker daemon within Earthly cannot be inspected on the host (e.g. for debugging purposes). For example, if a `docker-compose` stack fails, you cannot execute commands like `docker-compose logs` or `docker logs` on the host. However, you may use the interactive mode to drop into a shell within the build environment and execute such commands there. For more information, see the [debugging guide](https://docs.earthly.dev/docs/guides/debugging).
* It is currently not possible to mount `/var/run/docker.sock` in order to use the host Docker daemon. This goes against Earthly's principles of keeping execution repeatable. Mounting the Docker socket may cause builds to depend on the host Daemon state (e.g. pre-cached images) in ways that may not be obvious or easy to reproduce if the build were executed in another environment.

## Alternatives to Docker in Earthly

It is not always necessary to execute docker commands within an Earthly build. Certain operations can be replicated with Earthly constructs.

### Alternative to docker run

In certain cases, simple `docker run` invocations can be replaced by a simple [`RUN --entrypoint`](https://docs.earthly.dev/earthfile#entrypoint). For example, the following:

```Dockerfile
FROM docker:19.03.13-dind
WITH DOCKER --pull hello-world
    RUN docker run hello-world
END
```

Can be rewritten as

```Dockerfile
FROM hello-world
RUN --entrypoint
```

This, of course, has limitations, such as not being able to mount volumes the same way `docker run -v ...` could (instead, a `COPY` command could be used); or not being able to run multiple containers in parallel. However, when appropriate, it can simplify a build definition.

### Alternative to docker build

Running `docker build` within Earthly is discouraged, as it has a number of key limitations:

* Layer caching does not work. This is because `WITH DOCKER` does not preserve Docker cache between runs (other than `--pull`).
* Once an image is created, it cannot be exported as a build output in a form other than a TAR archive (e.g. it cannot be automatically loaded onto the host Docker daemon).

Instead of executing `docker build`, it is advisable to use the Earthly command `FROM DOCKERFILE`. For example, the command `docker build -t my-image:latest .` can be emulated by:

```Dockerfile
FROM DOCKERFILE .
SAVE IMAGE my-image:latest
```

## See also

* Reference for [`WITH DOCKER`](https://docs.earthly.dev/earthfile#with-docker)
* [Debugging techniques](https://docs.earthly.dev/docs/guides/debugging)
* [Tutorial on integration testing in Earthly](https://docs.earthly.dev/docs/guides/integration)

# Integration Testing

Running unit tests in a build pipeline is relatively simple. By definition, unit tests have no external dependencies. Things get more interesting when we want to test how our service integrates with other services and external systems. A service may have dependencies on external file systems, on databases, on external message queues, or other services. An ergonomic and effective development environment should have simple ways to construct and run integration tests. It should be easy to run these tests locally on the developer machine and in the build pipeline.

\*\* This guide will take an existing application with integration tests and show how they can be easily run inside earthly, both in the local development environment as well as in the build pipeline. \*\*

## Prerequisites

*This integration approach can work with most applications and development stacks. See* [*examples*](https://github.com/earthly/earthly/tree/main/examples) *for guidance on using earthly in other languages.*

### Our Application

The application we start with is simple. It returns the first 5 countries alphabetically via standard out. It has unit tests and integration tests. The integration tests require a datastore with the correct data in place.

### The Basic Earthfile

We start with a simple Earthfile that can build and create a docker image for our app. See the [Basics guide](https://docs.earthly.dev/basics) for more details, as well as examples in many programming languages.

See the [Basics Guide](https://docs.earthly.dev/basics) for more details on these steps, including how they might differ in Go, JavaScript, Java, and Python.

## In-App Integration Testing

Since our service has a docker-compose file of dependencies, running integration tests is easy.

Our integration target needs to copy in our source code and our Dockerfile and then inside a `WITH DOCKER` start the tests:

```Dockerfile
integration-test:
    FROM +project-files
    COPY src src
    COPY docker-compose.yml ./ 
    WITH DOCKER --compose docker-compose.yml
        RUN while ! pg_isready --host=localhost --port=5432 --dbname=iso3166 --username=postgres; do sleep 1; done ;\
            sbt it:test
    END
```

The `WITH DOCKER` has a `--compose` flag that we use to start up our docker-compose and run our integration tests in that context.

We can now run our tests both locally and in the CI pipeline, in a reproducible way:

```bash
> earthly -P +integration-test
+integration-test | Creating local-postgres ... done
+integration-test | Creating local-postgres-ui ... done
+integration-test | +integration-test | [info] Loading settings for project scala-example-build from plugins.sbt ...
+integration-test | [info] DatabaseIntegrationTest:
+integration-test | [info] A table
+integration-test | [info] - should have country data
+integration-test | [info] Run completed in 7 seconds, 923 milliseconds.
+integration-test | [info] Tests: succeeded 1, failed 0, canceled 0, ignored 0, pending 0
+integration-test | Stopping local-postgres-ui ... done
+integration-test | Stopping local-postgres    ... done
+integration-test | Removing local-postgres-ui ... done
+integration-test | Removing local-postgres    ... done
+integration-test | Removing network scala-example_default
+integration-test | Target github.com/earthly/earthly-example-scala/integration:main+integration-test built successfully
...
```

This means that if an integration test fails in the build pipeline, you can easily reproduce it locally.

## End to End Integration Tests

Our first integration test used was part of the service we were testing. This is one way to exercise integration code paths. Another useful form of integration testing is end-to-end testing. In this form of integration testing, we start up the application and test it from the outside.

In our simplified case example, with a single code path, a test that verifies the application starts and produces the desired output is sufficient.

Output: We can then run this and check that our application with its dependencies, produces the correct output.

```Dockerfile
> earthly -P +smoke-test
+smoke-test | --> WITH DOCKER RUN for i in {1..30}; do nc -z localhost 5432 && break; sleep 1; done; docker run --network=host earthly/examples:integration
+smoke-test | Loading images...
+smoke-test | Loaded image: aa8y/postgres-dataset:iso3166
+smoke-test | Loaded image: adminer:latest
+smoke-test | Loaded image: earthly/examples:integration
+smoke-test | ...done
+smoke-test | Creating network "scala-example_default" with the default driver
+smoke-test | Creating local-postgres ... done
+smoke-test | Creating local-postgres-ui ... done
+smoke-test | +smoke-test | The first 5 countries alphabetically are: Afghanistan, Albania, Algeria, American Samoa, Andorra
+smoke-test | Stopping local-postgres-ui ... done
+smoke-test | Stopping local-postgres    ... done
+smoke-test | Removing local-postgres-ui ... done
+smoke-test | Removing local-postgres    ... done
+smoke-test | Removing network scala-example_default
+smoke-test | Target github.com/earthly/earthly-example-scala/integration:main+smoke-test built successfully
=========================== SUCCESS ===========================
...
```

## Bringing It All Together

Adding these testing targets to an all target, we now can unit test, integration test, and dockerize and push our software in a single command. Using this approach, integration tests that fail sporadically for environmental reasons and can't be reproduced consistently should be a thing of the past.

```Dockerfile
all:
  BUILD +build
  BUILD +unit-test
  BUILD +integration-test
  BUILD +smoke-test
```

```bash
> earthly -P +all
...
+all | Target github.com/earthly/earthly-example-scala/integration:main+all built successfully
=========================== SUCCESS ===========================
```

There we have it, a reproducible integration process. If you have questions about the example, [ask](https://gitter.im/earthly-room/community)

## See also

* [Docker In Earthly](https://docs.earthly.dev/docs/guides/docker-in-earthly)
* [Source code for example](https://github.com/earthly/earthly/tree/main/examples/integration-test)
* [Integration Testing vs Unit Testing](https://blog.earthly.dev/unit-vs-integration/)

# Debugging techniques

Traditional debugging of errors during image builds often require a developer to place various print commands through out the build commands to help reason about the state of the system before the failure occurs. This can be slow and cumbersome.

Earthly provides an interactive mode which gives you access to a root shell when an error occurs, which we'll cover in this guide.

Let's consider a test example that prints out a randomly generated phrase:

```Dockerfile
# Earthfile

VERSION 0.6
FROM python:3
WORKDIR /code

test:
  RUN curl https://raw.githubusercontent.com/jsvine/markovify/master/test/texts/sherlock.txt > /sherlock.txt
  COPY generate_phrase.py .
  RUN pip3 install markovify
  RUN python3 generate_phrase.py
```

and our python code:

```Python
# generate_phrase.py

import markovify
text = open('sherlock.txt').read()
text_model = markovify.Text(text)
print(text_model.make_sentence())
```

Now we can run it with `earthly +test`, and we'll see a failure has occurred:

```
=========================== FAILURE ===========================
+test *failed* | --> RUN python3 generate_phrase.py
+test *failed* | Traceback (most recent call last):
+test *failed* |   File "generate_phrase.py", line 3, in <module>
+test *failed* |     text = open('sherlock.txt').read()
+test *failed* | FileNotFoundError: [Errno 2] No such file or directory: 'sherlock.txt'
+test *failed* | Command /bin/sh -c python3 generate_phrase.py failed with exit code 1
+test *failed* | +test *failed* | ERROR: Command exited with non-zero code: RUN python3 generate_phrase.py
Error: solve side effects: solve: failed to solve: rpc error: code = Unknown desc = executor failed running [/bin/sh -c  /usr/bin/earth_debugger /bin/sh -c 'python3 generate_phrase.py']: buildkit-runc did not terminate successfully
```

Why can't it find the sherlock.txt file? Let's re-run `earthly` with the `--interactive` (or `-i`) flag: `earthly -i +test`

This time we see a slightly different message:

```
+test | --> RUN python3 generate_phrase.py
+test | Traceback (most recent call last):
+test |   File "generate_phrase.py", line 3, in <module>
+test |     text = open('sherlock.txt').read()
+test | FileNotFoundError: [Errno 2] No such file or directory: 'sherlock.txt'
+test | Command /bin/sh -c python3 generate_phrase.py failed with exit code 1
+test | Entering interactive debugger (**Warning: only a single debugger per host is supported**)
+test | root@buildkitsandbox:/code#
```

This time rather than exiting, earthly will drop us into an interactive root shell within the container of the build environment. This root shell will allow us to execute arbitrary commands within the container to figure out the problem:

```
root@buildkitsandbox:/code# ls
generate_phrase.py
root@buildkitsandbox:/code# find / | grep sherlock.txt
/sherlock.txt
root@buildkitsandbox:/code# ls /
bin  boot  code  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  sherlock.txt  srv sys  tmp  usr  var
root@buildkitsandbox:/code# ls /sherlock.txt
/sherlock.txt
```

Ah ha! the corpus text file was located in the root directory rather than under `/code`. We can try moving it manually to see if that fixes the problem:

```
root@buildkitsandbox:/code# mv /sherlock.txt /code/.
root@buildkitsandbox:/code# python3 generate_phrase.py
I struck him down with the servants and with the lantern and left a fragment in the midst of my work during the last three years, although he has cruelly wronged.
```

At this point we know what needs to be done to fix the test, so we can type exit (or ctrl-D), to exit the interactive shell.

```
+test | time="2020-09-16T22:23:53Z" level=error msg="failed to read from ptmx: read /dev/ptmx: input/output error"
+test | time="2020-09-16T22:23:53Z" level=error msg="failed to read data from conn: read tcp 127.0.0.1:36672->127.0.0.1:5000: use of closed network connection"
+test | ERROR: Command exited with non-zero code: RUN python3 generate_phrase.py
```

Note that even though we fixed the problem during debugging, the image will not have been saved, so we must go back to our Earthfile and fix the problem there:

```Dockerfile
# Earthfile

VERSION 0.6
FROM python:3
WORKDIR /code

test:
  RUN curl https://raw.githubusercontent.com/jsvine/markovify/master/test/texts/sherlock.txt > /code/sherlock.txt
  COPY generate_phrase.py .
  RUN pip3 install markovify
  RUN python3 generate_phrase.py
```

## Debugging integration tests

Let's consider a more complicated example where we are running integration tests within an embedded docker setup:

```Dockerfile
# Earthfile

VERSION 0.6

server:
  COPY server.py .

test:
  FROM docker:19.03.12-dind
  RUN apk add curl
  WITH DOCKER --load server:latest=+server
    RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep hello
  END

```

and our server.py code:

```Python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
```

Let's fire up our integration test with `earthly -P -i +test`:

```
buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
+base | --> FROM python:3
context | --> local context .
+base | resolve docker.io/library/python:3@sha256:e9b7e3b4e9569808066c5901b8a9ad315a9f14ae8d3949ece22ae339fff2cad0 100%
context | transferring .: 100%
+base | *cached* --> WORKDIR /code
+server | *cached* --> COPY server.py .
+test | --> FROM docker:19.03.12-dind
+test | resolve docker.io/library/docker:19.03.12-dind@sha256:674f1f40ff7c8ac14f5d8b6b28d8fb1f182647ff75304d018003f1e21a0d8771 100%
+test | *cached* --> RUN apk add curl
+test | --> WITH DOCKER RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep hello
+test | Loading images...
+test | Loaded image: server:latest
+test | ...done
+test | 1dc054c647cb75bde4897a2828edb095739cb9f864ed203ed2ddb54e62554aad
+test | Command /bin/sh -c docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep hello failed with exit code 1
+test | Entering interactive debugger (**Warning: only a single debugger per host is supported**)
```

There was a failure checking that the server output contained the string `hello`; let's see what is going on:

```
/ # docker ps -a
CONTAINER ID        IMAGE               COMMAND               CREATED             STATUS              PORTS               NAMES
b8a31c54dd17        server:latest       "python3 server.py"   5 seconds ago       Up 4 seconds                            frosty_rhodes
```

The good news is our server container is running; let's see what happens when we try to connect to it:

```
/ # curl -s localhost:8000
Hello, world!/ 
```

Ah ha! The problem is our test is expecting a lowercase `h`, so we can fix our grep to look for an uppercase `H`:

```Dockerfile
# Earthfile

VERSION 0.6

server:
  COPY server.py .

test:
  FROM docker:19.03.12-dind
  RUN apk add curl
  WITH DOCKER --load server:latest=+server
    RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep Hello
  END
```

Then when we re-run our test we get:

```
+test | --> WITH DOCKER RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep Hello
+test | Loading images...
+test | Loaded image: server:latest
+test | ...done
+test | cb5299ae03cd17cfb2b528f01268ccf59761feec036cb313a3e969930d6f0815
+test | Hello, world!
+test | Target +test built successfully
=========================== SUCCESS ===========================
```

With the use of the interactive debugger; we were able to examine the state of the embedded containerized

## Demo

[![asciicast](https://asciinema.org/a/361170.svg)](https://asciinema.org/a/361170?speed=2)

## Final tips

If you ever want to jump into an interactive debugging session at any point in your Earthfile, you can simply add a command that will fail such as:

```
  RUN false
```

and run earthly with the `--interactive` (or `-i`) flag.

Hopefully you won't run into failures, but if you do the interactive debugger may help you discover the root cause more easily. Happy coding.

# Multi-platform builds

Earthly has the ability to perform builds for multiple platforms, in parallel. This page walks through setting up your system to support emulation as well as through a few simple examples of how to use this feature.

Currently only `linux` is supported as the build platform OS. Building with Windows containers will be available in a future version of Earthly.

By default, builds are performed on the same processor architecture as available on the host natively. Using the `--platform` flag across various Earthfile commands or as part of the `earthly` command, it is possible to override the build platform and thus be able to execute builds on non-native processor architectures. Execution of non-native binaries can be performed via QEMU emulation.

In some cases, execution of the build itself does not need to happen on the target architecture, through cross-compilation features of the compiler. Examples of languages that support cross-compilation are Go and Rust. This approach may be more beneficial in many cases, as there is no need to install QEMU and also, the build is more performant.

## Prerequisites for emulation

In order to execute emulated build steps (usually `RUN`), QEMU needs to be installed and set up. This will allow you perform Earthly builds on non-native platforms, but also incidentally, to run Docker images on your host system through `docker run --platform=...`.

### Windows and Mac

On Mac and on Windows, the Docker Desktop app comes with QEMU readily installed and ready to go, so no special consideration is necessary.

### Linux

On Linux, QEMU needs to be installed manually. On Ubuntu, this can be achieved by running:

```bash
sudo apt-get install qemu-system binfmt-support qemu-user-static
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker stop earthly-buildkitd || true
```

The `docker run` command above enables execution of different multi-architecture containers by QEMU and `binfmt_misc`. It only needs to be run once.

### GitHub Actions

To make use of emulation in GitHub Actions, the following step needs to be included in every job that performs a multi-platform build:

```yaml
jobs:
    <job-name>:
        steps:
            -
                name: Set up QEMU
                id: qemu
                uses: docker/setup-qemu-action@v1
                with:
                    image: tonistiigi/binfmt:latest
                    platforms: all
            - uses: actions/checkout@v3
            - ...
```

## Performing multi-platform builds

In order to execute builds for multiple platforms, the execution may be parallelized through the repeated use of the `BUILD --platform` flag. For example:

```Dockerfile
build-all-platforms:
    BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build

build:
    ...
```

If the `+build` target were invoked without the use of any flag, Earthly would simply perform the build on the native architecture of the host system.

However, invoking the target `+build-all-platforms` causes `+build` to execute twice, in parallel: one time on `linux/amd64` and another time on `linux/arm/v7`.

You may also override the target platform when issuing the `earthly` build command. For example:

```bash
earthly --platform=linux/arm64 +build
```

This would cause the build to execute on the `linux/arm64` architecture.

## Saving multi-platform images

The easiest way to include platform information as part of a build is through the use of `FROM --platform`. For example:

```Dockerfile
FROM --platform=linux/arm/v7 alpine:3.15
```

If multiple targets create an image with the same name, but for different platforms, the images will be merged into a multi-platform image during export. For example:

```Dockerfile
build-all-platforms:
    BUILD +build-amd64
    BUILD +build-arm-v7

build-amd64:
    FROM --platform=linux/amd64 alpine:3.15
    ...
    SAVE IMAGE --push org/myimage:latest

build-arm-v7:
    FROM --platform=linux/arm/v7 alpine:3.15
    ...
    SAVE IMAGE --push org/myimage:latest
```

When `earthly --push +build-all-platforms` is executed, the build will push a multi-manifest image to the Docker registry. The manifest will contain two images: one for `linux/amd64` and one for `linux/arm/v7`. This works as such because both targets that save images use the exact same Docker tag for the image.

Of course, in some situations, the build steps are the same (except they run on different platform), so the two definitions can be merged like so:

```Dockerfile
build-all-platforms:
    BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build

build:
    FROM alpine:3.15
    ...
    SAVE IMAGE --push org/myimage:latest
```

A more complete version of this example is available in [examples/multiplatform](https://github.com/earthly/earthly/tree/main/examples/multiplatform) in GitHub. You may try out this example without cloning by running

```bash
earthly github.com/earthly/earthly/examples/multiplatform:main+all
docker run --rm earthly/examples:multiplatform
docker run --rm earthly/examples:multiplatform_linux_amd64
docker run --rm earthly/examples:multiplatform_linux_arm_v7
```

{% hint style="info" %}
**Note**

As of the time of writing this article, the `docker` CLI has limited support for working with multi-manifest images locally. For this reason, when exporting an image to the local Docker daemon, Earthly provides the different architectures as different Docker tags.

For example, the above build would yield locally:

* `org/myimage:latest`
* `org/myimage:latest_linux_amd64` (the same as `org/myimage:latest` if running on a `linux/amd64` host)
* `org/myimage:latest_linux_arm_v7`

The additional Docker tags are only available for use on the local system. When pushing an image to a Docker registry, it is pushed as a single multi-manifest image.
{% endhint %}

## Creating multi-platform images without emulation

Building multi-platform images does not necessarily require that execution of the build itself takes place on the target platform. Through the use of cross-compilation, it is possible to obtain target-platform binaries compiled on the host-native platform. At the end, these binaries may be placed in a final image which is marked for a specific platform.

Note, however, that not all programming languages have support for cross-compilation. The applicability of this approach may be limited as a result. Examples of languages that *can* cross-compile for other platforms are Go and Rust.

Here is an example where a multi-platform image can be created without actually executing any `RUN` on the target platform (and therefore emulation is not necessary):

```Dockerfile
build-all-platforms:
    BUILD +build-amd64
    BUILD +build-arm-v7

build:
    FROM golang:1.15-alpine3.13
    WORKDIR /example
    ARG GOOS=linux
    ARG GOARCH=amd64
    ARG GOARM
    COPY main.go ./
    RUN go build -o main main.go
    SAVE ARTIFACT ./main

build-amd64:
    FROM --platform=linux/amd64 alpine:3.15
    COPY +build/main ./example/main
    ENTRYPOINT ["/example/main"]
    SAVE IMAGE --push org/myimage:latest

build-arm-v7:
    FROM --platform=linux/arm/v7 alpine:3.15
    COPY \
        --platform=linux/amd64 \
        (+build/main --GOARCH=arm --GOARM=v7) ./example/main
    ENTRYPOINT ["/example/main"]
    SAVE IMAGE --push org/myimage:latest
```

The key here is the use of the `COPY` commands. The execution of the target `+build` may take place on the host platform (in this case, `linux/amd64`) and yet produce binaries for either `amd64` or `arm/v7`. Since there is no `RUN` command as part of the `+build-arm-v7` target, no emulation is necessary.

## Making use of builtin platform args

A number of [builtin build args](https://docs.earthly.dev/docs/earthfile/builtin-args) are made available to be used in conjunction with multi-platform builds:

* `TARGETPLATFORM` (eg `linux/arm/v7`)
* `TARGETOS` (eg `linux`)
* `TARGETARCH` (eg `arm`)
* `TARGETVARIANT` (eg `v7`)

Here is an example of how the build described above could be simplified through the use of these build args:

```Dockerfile
build-all-platforms:
    BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build-image

build:
    FROM golang:1.15-alpine3.13
    WORKDIR /example
    ARG GOOS=linux
    ARG GOARCH=amd64
    ARG VARIANT
    COPY main.go ./
    RUN GOARM=${VARIANT#"v"} go build -o main main.go
    SAVE ARTIFACT ./main

build-image:
    ARG TARGETPLATFORM
    ARG TARGETARCH
    ARG TARGETVARIANT
    FROM --platform=$TARGETPLATFORM alpine:3.15
    COPY \
        --platform=linux/amd64 \
        (+build/main --GOARCH=$TARGETARCH --VARIANT=$TARGETVARIANT) ./example/main
    ENTRYPOINT ["/example/main"]
    SAVE IMAGE --push org/myimage:latest
```

The code of this example is available in [examples/multiplatform-cross-compile](https://github.com/earthly/earthly/tree/main/examples/multiplatform-cross-compile) in GitHub. You may try out this example without cloning by running

```bash
earthly github.com/earthly/earthly/examples/multiplatform-cross-compile:main+build-all-platforms
```

### USER platform args

Additional `USER` [builtin build args](https://docs.earthly.dev/docs/earthfile/builtin-args) can be used to determine the architecture of the host that called `earthly`. This can be useful to determine if cross-platform emulation was used.

* `USERPLATFORM` (eg `linux/amd64`)
* `USEROS` (eg `linux`)
* `USERARCH` (eg `amd64`)
* `USERVARIANT` (eg \`\`; an empty string for non-arm platforms)

## Emulation and WITH DOCKER

Please note that `WITH DOCKER` has an important limitation for cross-platform builds: the target containing `WITH DOCKER` needs to be executing on the native architecture of the host system. The images being run within `WITH DOCKER` can be of any architecture, however.

In other words, the following will **NOT** work on amd64:

```Dockerfile
build:
    FROM --platform=linux/arm64 earthly/dind
    WITH DOCKER --pull=earthly/examples:multiplatform
        RUN docker run earthly/examples:multiplatform
    END
```

However, the following will:

```
build:
    FROM earthly/dind
    WITH DOCKER --pull=earthly/examples:multiplatform
        RUN docker run --platform=linux/arm64 earthly/examples:multiplatform
    END
```

The reason for this is that behind the scenes `WITH DOCKER` starts up an isolated Docker daemon running within a container, and docker-in-docker is not yet supported in a QEMU environment.

# Podman

[Podman](https://podman.io/) is an alternative to docker; it's a daemonless container engine for developing, managing and running OCI containers on a Linux system. Podman also works on Mac using a [podman machine](https://docs.podman.io/en/latest/markdown/podman-machine.1.html).

## Prerequisites

* [Install podman](https://podman.io/getting-started/installation)
* Mac: ensure a [podman machine](https://docs.podman.io/en/latest/markdown/podman-machine.1.html) is running.
* Linux: for [multi-platform builds](https://docs.earthly.dev/docs/guides/multi-platform), install [qemu-user-static](https://github.com/multiarch/qemu-user-static).
* [WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker) requires rootful mode.
  * Linux: run with `sudo` (i.e., `sudo earthly -P +with-docker-target`)
  * Mac: run a [rootful machine](https://docs.podman.io/en/latest/markdown/podman-machine-set.1.html#rootful).

## Getting started

When earthly starts a check is done to determine what frontend is available. By default, earthly will attempt to use docker and then fall back to podman. If you wish to change the behavior of the startup check, run the following command:

```bash
# Configure earthly to use podman
earthly config global.container_frontend podman-shell

# Configure earthly to use docker
earthly config global.container_frontend docker-shell
```

You can verify the command worked by checking the `~/.earthly/config.yml` file and verifying it contains a `container_frontend` entry.

```bash
> cat ~/.earthly/config.yml
global:
    container_frontend: podman-shell
```

Then, you can run a basic hello world example to see earthly using the appropriate container frontend.

```bash
> earthly github.com/earthly/hello-world:main+hello
 1. Init 🚀
————————————————————————————————————————————————————————————————————————————————

           buildkitd | Starting buildkit daemon as a podman container (earthly-buildkitd)...
           buildkitd | ...Done
```

If instead you see `No frontend initialized`, and you're using Mac, it may mean your podman machine is not running.

## Known limitations / troubleshooting

### Builds running slowly

There are a few steps you should take to rule out common performance bottlenecks.

#### Mac: check podman resources

At the time of writing this, podman machines use a single core and 2GB of RAM by default. Depending on what you're doing you may need more resources.

Resources can be adjusted by using one of these commands:

```bash
# Initialize a new default machine with 5 CPUs, 128GB disk space, 8196 MB of memory, and start it
podman machine init --now --cpus 5 --disk-size 128 --memory 8196 

# Adjust the current default podman machine to use 5 CPUs, 128GB disk space, and 8196 MB of memory
podman machine stop ; podman machine set --cpus 5 --disk-size 128 --memory 8196 && podman machine start
```

### Mac: check machine architecture

Running `podman version` will display the specifications of your podman client and server (machine). You should ensure the architecture in OS/Arch is the same between client and server. This will rule out emulation as a performance bottleneck.

The output may look like this:

```bash
> podman version
Client:       Podman Engine
Version:      4.2.1
API Version:  4.2.1
Go Version:   go1.18.6
Built:        Tue Sep  6 13:16:02 2022
OS/Arch:      darwin/arm64

Server:       Podman Engine
Version:      4.2.0
API Version:  4.2.0
Go Version:   go1.18.4
Built:        Thu Aug 11 08:43:11 2022
OS/Arch:      linux/arm64
```

In this example, the client us running on an M1 Mac and both the client and server are using arm64.

### Check graph driver

Running `podman info --debug` will show your current podman configuration. VFS and other drivers can perform poorly when compared to overlay and [are not recommended by the podman community](https://github.com/containers/podman/issues/13226). Ensure overlay is used by looking for the following in the podman info output:

```bash
> podman info --debug

...
graphDriverName: overlay  # or something similar
...
```

### Mac: docker-credential-desktop: executable file not found in $PATH

This error typically occurs when switching from docker desktop to podman without docker installed. There may be a lingering configuration file that will be read by the attachable used to authenticate calls to buildkit.

To fix this issue, try removing or renaming the `~/.docker/config.json` file.

### Earthly CLI - no frontend initialized

Seeing the error on startup means the check for podman has failed.

```bash
> earthly github.com/earthly/hello-world:main+hello
 1. Init 🚀
————————————————————————————————————————————————————————————————————————————————

            frontend | No frontend initialized.
```

Ensure you have correctly installed podman and, if you are using a Mac, the podman machine is running.

```bash
> podman machine start
```

### Rootless podman

Running podman in rootless mode is not supported due to the [earthly/dind](https://hub.docker.com/r/earthly/dind) and [earthly/buildkit](https://hub.docker.com/r/earthly/buildkitd) because they [require privileged access](https://docs.earthly.dev/docs/guides/using-the-earthly-docker-images/buildkit-standalone#requirements). Specifically, [WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker) will fail. You must use `sudo` on Linux or [set your podman machine to rootful mode on Mac](https://docs.podman.io/en/latest/markdown/podman-machine-set.1.html#rootful) to use [WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker).

### Podman within WITH DOCKER

[WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker) starts a container with a docker installation. You can only use the podman CLI in the RUN statement if you specify [LOCALLY](https://docs.earthly.dev/best-practices#pattern-optionally-locally) to run it on the host machine; otherwise, you will need to use the docker CLI.

```bash
docker-locally:
   LOCALLY
   WITH DOCKER
     RUN podman ps
   END
```

```bash
docker:
   WITH DOCKER
     RUN docker ps
   END
```

### Cross-image targets

You need to configure QEMU if you are running a cross-platform target. If you haven't properly configured QEMU you will receive an error message containing the following message:

```bash
> earthly +cross-platform
...
exec /bin/sh: exec format error
...
```

We've found installing [qemu-user-static](https://github.com/multiarch/qemu-user-static) will allow cross-platform targets tun run on Linux.

```bash
> apt-get install qemu-user-static
# or
> yum install qemu-user-static
```

### crun: open executable: Permission denied: OCI permission denied

This can happen if you attempt to run (or the `ENTRYPOINT` references) a binary without the execution permission. <https://github.com/containers/podman/issues/9377> <https://github.com/signalwire/freeswitch/pull/1748>

# Configuring registries

# AWS ECR

## Introduction

The AWS Elastic Container Registry (ECR) is a hosted docker repository that requires extra configuration for day-to-day use. This configuration is not typical of other repositories, and there are some considerations to account for when using it with Earthly. This guide will walk you through creating an Earthfile, building an image, and pushing it to ECR.

This guide assumes you have already installed the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), and [created a new repository named hello-earthly](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.15

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
```

## Install and Configure the ECR Credential Helper

ECR does not issue permanent credentials. Instead, it relies on your AWS credentials to issue docker credentials. You can follow [instructions to log in with generated credentials](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login.html), but the process will need to be repeated every 12 hours. In practice, this often means lots of glue code in your CI pipeline to keep credentials up to date.

[AWS has released a credential helper to ease logging into ECR](https://github.com/awslabs/amazon-ecr-credential-helper). It may be that you already have the credential helper installed, since it has been included with Docker Desktop as of version [2.4.0.0](https://docs.docker.com/docker-for-windows/release-notes/#docker-desktop-community-2400). If not, you can follow installation instructions on their GitHub repository here. Here is a sample `.docker/config.json` to enable the usage of this helper:

```
{
        "credHelpers": {
                "<aws_account_id>.dkr.ecr.<region>.amazonaws.com": "ecr-login"
        }
}

```

## IAM

Ensure that you have correct permissions to push the images. The ECR helper is aware of the `AWS_PROFILE` variable; and can work under an assumed role. Here is a minimum set of privileges needed to push to ECR from Earthly:

```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AllowPushPull",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::<aws_account_id>:user/push-pull-user",
                ]
            },
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload"
            ]
        }
    ]
}
```

Additional [examples](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) for policy configuration.

## Run the Target

With the helper installed, no special To build and push an image, simply execute the build target. Don't forget the `--push` flag!

```
❯ earthly --push +build
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
         alpine:3.15 | --> Load metadata linux/amd64
               +base | --> FROM alpine:3.15
               +base | [██████████] resolve docker.io/library/alpine:3.15@sha256:0bd0e9e03a022c3b0226667621da84fc9bf562a9056130424b5bfbd8bcb0397f ... 100%
              +build | --> RUN echo "Hello from Earthly!" > motd
              output | --> exporting outputs
              output | [██████████] exporting layers ... 100%
              output | [██████████] exporting manifest sha256:9ab4df74dafa2a71d71e39e1af133d110186698c78554ab000159cfa92081de4 ... 100%
              output | [██████████] exporting config sha256:6feef98708c14c000a6489a2a99315a5328c2c16091851ae10438b53f655d042 ... 100%
              output | [██████████] pushing layers ... 100%
              output | [██████████] pushing manifest for <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love ... 100%
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================
Loaded image: <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
              +build | Image +build as <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love (pushed)

```

## Pulling Images

Using this credential helper; you can also pull images without any special handling in an Earthfile:

```
FROM earthly/dind:alpine-main

run:
    WITH DOCKER --pull <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
        RUN docker run <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
    END
```

And here is how you would run it:

```
❯ earthly -P +run
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
 earthly/dind:alpine | --> Load metadata linux/amd64
4/hello-earthly:with-love | --> Load metadata linux/amd64
4/hello-earthly:with-love | --> DOCKER PULL <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
4/hello-earthly:with-love | [██████████] resolve <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love@sha256:9ab4df74dafa2a71d71e39e1af133d110186698c78554ab000159cfa92081de4 ... 100%
               +base | --> FROM earthly/dind:alpine
               +base | [██████████] resolve docker.io/earthly/dind:alpine@sha256:2cef4089960efe028de40721749e3ec6eba9f471562bf10681de729287bd78fb ... 100%
                +run | *cached* --> WITH DOCKER (install deps)
                +run | *cached* --> WITH DOCKER RUN docker run <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
              output | --> exporting outputs
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================
```

## Troubleshooting

### Basic Credentials Not Found

If you get a message saying `basic credentials not found`; your distribution may not have the most recent version installed. A simple workaround is to simply prepend `AWS_SDK_LOAD_CONFIG=true` to your Earthly invocation. This will force the helper to use the SDK over built-in config when executing. You can track this [issue](https://github.com/awslabs/amazon-ecr-credential-helper/issues/232).

### 401 Unauthorized

Double-check your AWS credentials, to ensure you have the correct ones set up. `aws configure` can help you do this. Also, check IAM to ensure you have the correct permissions (see the [IAM](#iam) section above). Finally, if you use IAM assumed roles, ensure that you have assumed the correct role in your terminal session.

If these are in order, the same fix from [Basic Credentials Not Found](#basic-credentials-not-found) may help.

If you are using a [pull-through-cache](https://docs.earthly.dev/ci-integration/pull-through-cache), the ECR credential helper may cause 401 failures when fetching metadata from the mirrored registry. You can solve this by manually logging in, instead of using the credential helper. Here is an example of logging in manually:

```
aws ecr get-login-password | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
```

# GCP Artifact Registry

## Introduction

The GCP Artifact Registry is a hosted docker repository that requires extra configuration for day-to-day use. This configuration is not typical of other repositories, and there are some considerations to account for when using it with Earthly. This guide will walk you through creating an Earthfile, building an image, and pushing it to Artifact Registry.

[Artifact Registry is the successor to the GCP Container Registry (GCR)](https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr). It can accommodate more than just Docker images, but those are beyond the scope of this guide. Most of what we detail here applies to GCR as well, it will just require some [small tweaks](https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr#compare).

This guide assumes you have already installed the [`gcloud` CLI tool](https://cloud.google.com/sdk/docs/install), [enabled the Artifact Repository API](https://console.cloud.google.com/flows/enableapi?apiid=artifactregistry.googleapis.com\&redirect=https://cloud.google.com/artifact-registry/docs/docker/quickstart), and [created a new repository named `hello-earthly`](https://console.cloud.google.com/artifacts).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.15

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
```

## Configure the Artifact Repository Credential Helper

Artifact Repository does not issue permanent credentials. Instead, it relies on your Google credentials to issue Docker credentials. To this end, Google has built-in a credential helper to the `gcloud` CLI tool. `gcloud` can update your `.docker/config.json` on its own by running `gcloud auth configure-docker <region>-docker.pkg.dev`. Here is a sample entry it might create:

```
 {
    "credHelpers": {
        "<region>-docker.pkg.dev": "gcloud"
  }
}

```

## IAM

Ensure that you have correct permissions to push and pull the images. Please reference the [GCP documentation](https://cloud.google.com/artifact-registry/docs/access-control#grant) to ensure you have the correct permissions set. You will need to add the `Artifact Registry Reader` and `Artifact Registry Writer` roles to complete the tasks in this guide.

If you are using GCR; keep in mind that the needed permissions are based on the GCP storage permissions. We used the `Storage Admin` permissions to complete the guide with GCR.

Service Accounts also work with Earthly. Rather than `gcloud init`, simply log in using the Google-provided key like this:

```
RUN gcloud auth activate-service-account --key-file /test/key.json
```

## Run the Target

With the helper installed, no special To build and push an image, simply execute the build target. Don't forget the `--push` flag!

```
❯ earthly --push +build
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
         alpine:3.15 | --> Load metadata linux/amd64
               +base | --> FROM alpine:3.15
               +base | [██████████] resolve docker.io/library/alpine:3.15@sha256:0bd0e9e03a022c3b0226667621da84fc9bf562a9056130424b5bfbd8bcb0397f ... 100%
              +build | --> RUN echo "Hello from Earthly!" > motd
              output | --> exporting outputs
              output | [██████████] exporting layers ... 100%
              output | [██████████] exporting manifest sha256:08f310b4520418a60f7c12b168167ea22b886bc03d43ab87058e959ef5c14cf2 ... 100%
              output | [██████████] exporting config sha256:8a54361d584a6a51f0136b9ae1526aba8f99cc0a1583954b0f206d3a472eaac9 ... 100%
              output | [██████████] pushing layers ... 100%
              output | [██████████] pushing manifest for <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love ... 100%
              output | [██████████] sending tarballs ... 100%
2bc1eb057e55: Loading layer [==================================================>]     187B/187B
=========================== SUCCESS ===========================
Loaded image: <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
              +build | Image +build as <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love (pushed)


```

## Pulling Images

Using this credential helper; you can also pull images without any special handling in an Earthfile:

```
FROM earthly/dind:alpine-main

run:
    WITH DOCKER --pull <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
        RUN docker run <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
    END
```

And here is how you would run it:

```
❯ earthly -P +run
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
  e/dind:alpine-main | --> Load metadata linux/amd64
u/e/h/hello-earthly:with-love | --> Load metadata linux/amd64
u/e/h/hello-earthly:with-love | --> DOCKER PULL <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
u/e/h/hello-earthly:with-love | [          ] resolve <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love@sha256:08f310b4520418a60f7c12b168167ea22b886bc03d43ab87058e959ef5c14cf2 ... 0%                               [██████████] resolve <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love@sha256:08f310b4520418a60f7c12b168167ea22b886bc03d43ab87058e959ef5c14cf2 ... 100%
               +base | --> FROM earthly/dind:alpine-main
               +base | [██████████] resolve docker.io/earthly/dind:alpine-main@sha256:09f497f0114de1f3ac6ce2da05568fcb50b0a4fd8b9025ed7c67dc952d092766 ... 100%
                +run | *cached* --> WITH DOCKER (install deps)
                +run | *cached* --> WITH DOCKER RUN docker run <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
              output | --> exporting outputs
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================

```

# Azure ACR

## Introduction

The Azure Container Registry (ACR) is a hosted docker repository that requires extra configuration for day-to-day use. This configuration is not typical of other repositories, and there are some considerations to account for when using it with Earthly. This guide will walk you through creating an Earthfile, building an image, and pushing it to ACR.

This guide assumes you have already installed the [Azure CLI tool](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli), and [created a new repository named `helloearthly`](https://portal.azure.com/?quickstart=true#create/Microsoft.ContainerRegistry).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.15

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push helloearthly.azurecr.io/hello-earthly:with-love
```

## Login and Configure the ACR Credential Helper

ACR does not issue permanent credentials. Instead, it relies on your Azure AD credentials to issue Docker credentials. As an individual user, you will need to log into your repository first:

```
❯ az acr login --name helloearthly
Login Succeeded
```

After logging in, the [ACR Credential Helper](https://github.com/Azure/acr-docker-credential-helper) will help keep your credentials up to date, as long as it is invoked again before your already issued credentials expire. When all this is complete, your `.docker/config.json` might look like this:

```
{
 "auths": {
  "helloearthly.azurecr.io": {
   "auth": "...",
   "identitytoken": "..."
  }
 },
 "credsStore": "acr-linux"
}
```

ACR boasts many other methods of logging in, including [Service Principals](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal) and [admin accounts](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-authentication#admin-account). Note that the admin account method is not recommended for production usage. Please follow the relevant guides to authenticate if you wish to use one of these other methods.

## RBAC

Ensure that you have correct permissions to push and pull the images. Please reference the [ACR RBAC documentation](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-roles) to ensure you have the correct permissions set. To complete all the activities in this guide, you will need to have at least the `AcrPush` role.

Earthly also works with Service Principals; and these do not require `az acr login`. You can simply login directly with `docker` like this:

```
RUN --secret AZ_USERNAME=+secrets/earthly-technologies/azure/ci-cd-username \
    --secret AZ_PASSWORD=+secrets/earthly-technologies/azure/ci-cd-password \
    docker login helloearthly.azurecr.io --username $AZ_USERNAME --password $AZ_PASSWORD
```

## Run the Target

Once you are logged in, and have the optional credential helper installed, then you are ready to use Earthly to access images in ACR. To build and push an image, simply execute the build target. Don't forget the `--push` flag!

```
❯ ../earthly/earthly --push --no-cache +build
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
         alpine:3.15 | --> Load metadata linux/amd64
               +base | --> FROM alpine:3.15
               +base | [██████████] resolve docker.io/library/alpine:3.15@sha256:0bd0e9e03a022c3b0226667621da84fc9bf562a9056130424b5bfbd8bcb0397f ... 100%
              +build | --> RUN echo "Hello from Earthly!" > motd
              output | --> exporting outputs
              output | [██████████] exporting layers ... 100%
              output | [██████████] exporting manifest sha256:02df2d4600094d5550f7475b868ce9bb17d6c3a529e9669a453bbba7b2cdb659 ... 100%
              output | [██████████] exporting config sha256:722368416f5de51291ce937feac2c246d66dff351678968b1b6ebc533ceaaa0c ... 100%
              output | [██████████] pushing layers ... 100%
              output | [██████████] pushing manifest for helloearthly.azurecr.io/hello-earthly:with-love ... 100%
              output | [██████████] sending tarballs ... 100%
824d26cf8432: Loading layer [==================================================>]     192B/192B
=========================== SUCCESS ===========================
Loaded image: helloearthly.azurecr.io/hello-earthly:with-love
              +build | Image +build as helloearthly.azurecr.io/hello-earthly:with-love (pushed)
```

## Pulling Images

By logging in and optionally installing the credential helper; you can also pull images without any special handling in an Earthfile:

```
FROM earthly/dind:alpine-main

run:
    WITH DOCKER --pull helloearthly.azurecr.io/hello-earthly:with-love
        RUN docker run helloearthly.azurecr.io/hello-earthly:with-love
    END
```

And here is how you would run it:

```
❯ earthly -P +run
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
  e/dind:alpine-main | --> Load metadata linux/amd64
h/hello-earthly:with-love | --> Load metadata linux/amd64
h/hello-earthly:with-love | --> DOCKER PULL helloearthly.azurecr.io/hello-earthly:with-love
h/hello-earthly:with-love | [██████████] resolve helloearthly.azurecr.io/hello-earthly:with-love@sha256:02df2d4600094d5550f7475b868ce9bb17d6c3a529e9669a453bbba7b2cdb659 ... 100%
               +base | --> FROM earthly/dind:alpine-main
               +base | [██████████] resolve docker.io/earthly/dind:alpine-main@sha256:09f497f0114de1f3ac6ce2da05568fcb50b0a4fd8b9025ed7c67dc952d092766 ... 100%
                +run | *cached* --> WITH DOCKER (install deps)
                +run | --> WITH DOCKER RUN docker run helloearthly.azurecr.io/hello-earthly:with-love
                +run | Loading images...
                +run | Loaded image: helloearthly.azurecr.io/hello-earthly:with-love
                +run | ...done
                +run | Hello from Earthly!
              output | --> exporting outputs
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================
```

## Troubleshooting

### 401 (authentication required)

Re-run `az acr login --name` to log in again and refresh your credentials. Azure recommends that you run this at the beginning o each automated script; keep this in mind for your CI runs.

# Self-signed certificates

This guide will demonstrate the use of a private registry using self-signed certificates in conjunction with Earthly.

For information about configuring the registry itself, see the [Docker Registry deployment documentation](https://docs.docker.com/registry/deploying/).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.15

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push <registry-hostname>/hello-earthly:with-love
```

## Add certificates to Earthly

Set the following configuration options in your [Earthly config](https://docs.earthly.dev/docs/earthly-config).

```yaml
global:
  buildkit_additional_args: ["-v", "<absolute-path-to-ca-file>:/etc/config/add.ca"]
  buildkit_additional_config: |
    [registry."<registry-hostname>"]
      ca=["/etc/config/add.ca"]
```

Where `<absolute-path-to-ca-file>` is the location of the CA certificate you wish to add and `<registry-hostname>` is the hostname of the registry. The quotes are not a mistake, and should be left in.

## Insecure registries

For testing purposes, you can also define insecure registries for Earthly to access. Note that the non-test use of insecure registries is strongly discouraged due to the risk of man-in-the-middle (MITM) attacks.

To configure Earthly to use an insecure registry, use the following [Earthly config](https://docs.earthly.dev/docs/earthly-config) settings.

```yaml
global:
  buildkit_additional_config: |
    [registry."<registry-hostname>"]
      insecure = true
```

In addition, you will need to specify the `--insecure` flag in any `SAVE IMAGE` command. Again, the quotes are not a mistake, and should be left in.

```
FROM alpine:3.15

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push --insecure <registry-hostname>/hello-earthly:with-love
```

{% hint style="danger" %}
**Note**

The `http` and `insecure` settings are typically mutually exclusive. Setting `insecure=true` should only be used when the registry is https and is configured with an insecure certificate. Setting `http=true` is only for the case where a standard http-based registry is used (i.e. no SSL encryption). If both are set buildkit will attempt to connect to the registry using either http (port 80), or https (port 443).
{% endhint %}

## Other BuildKit options

Other settings for configuring registries in Earthly via [BuildKit options](https://github.com/moby/buildkit/blob/master/docs/buildkitd.toml.md) can be seen below.

```yaml
global:
  buildkit_additional_config: |
    [registry."<registry-hostname>"]
      mirrors = ["<mirror>"]
      http = true|false
      insecure = true|false
      ca=["<ca-path-pem>"]
      [[registry."<registry-hostname>".keypair]]
        key="<key-path-pem>"
        cert="<cert-path-pem>"
```

# Using the Earthly Docker Images

# earthly/earthly

This image contains `earthly`, `buildkit`, and some extra configuration to enable the two to work together. All that's missing is your source code! This image is mainly intended for use in containerized CI scenarios, or where maintaining a persistent installation of `earthly` isn't possible.

### Tags

* `v0.6.30`, `latest`
* `v0.6.29`
* `v0.6.28`

### Quickstart

Want to just get started? Here are a couple sample `docker run` commands that cover the most common use-cases:

#### Simple Usage with Docker Socket

This example shows how to use the Earthly container in conjunction with a Docker socket that Earthly can use to start up the Buildkit daemon.

```bash
docker run -t -v $(pwd):/workspace -v /var/run/docker.sock:/var/run/docker.sock -e NO_BUILDKIT=1 earthly/earthly:v0.6.30 +for-linux
```

Here's a quick breakdown:

* `-t` tells Docker to emulate a TTY. This makes the `earthly` log output colorized.
* `-v $(pwd):/workspace` mounts the source code into the conventional location within the docker container. Earthly is executed from this directory when starting the container. Any artifacts saved within this folder remain on your local machine.
* `-v /var/run/docker.sock:/var/run/docker.sock` mounts the Docker socket such that Earthly can start Buildkit as a Docker container in the host's Docker.
* `-e NO_BUILDKIT=1` tells the Earthly container not to start en embedded buildkit. A Buildkit daemon will instead be started via the Docker socket provided.
* `+for-linux` is the target to be invoked. All arguments specified after the image tag will be passed to `earthly`.

#### Simple Usage with Embedded Buildkit

This example shows how the Earthly image can start a Buildkit daemon within the same container. A Docker socket is not needed in this case, however the container will need to be run with the `--privileged` flag.

```bash
docker run --privileged -t -v $(pwd):/workspace -v earthly-tmp:/tmp/earthly:rw earthly/earthly:v0.6.30 +for-linux
```

Here's a quick breakdown:

* `--privileged` is required when you are using the internal, embedded `buildkit`. This is because `buildkit` currently requires it for OverlayFS support and for network configuration.
* `-t` tells Docker to emulate a TTY. This makes the `earthly` log output colorized.
* `-v $(pwd):/workspace` mounts the source code into the conventional location within the docker container. Earthly is executed from this directory when starting the container. Any artifacts saved within this folder remain on your local machine.
* `-v earthly-tmp:/tmp/earthly:rw` mounts (and creates, if necessary) the `earthly-tmp` Docker volume into the containers `/tmp/earthly`. This is used as a temporary/working directory for `buildkitd` during builds.
* `+for-linux` is the target to be invoked. All arguments specified after the image tag will be passed to `earthly`.

#### Usage with Satellites and No Local Code

This example utilizes an [Earthly Satellite](https://docs.earthly.dev/earthly-cloud/satellites) to perform builds. The code to be built is downloaded directly from GitHub.

```bash
docker run -t -e NO_BUILDKIT=1 -e EARTHLY_TOKEN=<my-token> earthly/earthly:v0.6.30 --ci --org <my-org> --sat <my-sat> github.com/earthly/earthly+for-linux
```

Here's what this does:

* `-e EARTHLY_TOKEN=<my-token>` passes along an Earthly token such that Earthly can access satellites. This token can be created via `earthly account create-token`.
* `--org <my-org>` specifies the organization that the satellite belongs to.
* `--sat <my-sat>` specifies the satellite to use.
* `github.com/earthly/earthly+for-linux` specifies the target to build. This target is located on GitHub, and will be pulled from the Satellite.

#### Usage for non-build commands

This example shows how to use the Earthly container to run non-build commands. This is useful for running commands like `earthly account`, or `earthly secret`.

```bash
docker run -t -e NO_BUILDKIT=1 -e EARTHLY_TOKEN=<my-token> earthly/earthly:v0.6.30 account list-tokens
```

```bash
docker run -t -e NO_BUILDKIT=1 -e EARTHLY_TOKEN=<my-token> earthly/earthly:v0.6.30 secret get foo
```

### Using This Image

#### Requirements

There are a couple requirements this image expects you to follow when using it. These requirements streamline usage of the image and save configuration effort.

**Privileged Mode**

If you are using the embedded `buildkitd`, then this image needs to be run as a privileged container. This is because `buildkitd` needs appropriate access to use `overlayfs`.

**`/tmp/earthly`**

Because this folder sees *a lot* of traffic, its important that it remains fast. We *strongly* recommend using a Docker volume for mounting `/tmp/earthly`. If you do not, `buildkitd` can consume excessive disk space, operate very slowly, or it might not function correctly.

In some environments, not mounting `/tmp/earthly` as a Docker volume results in the following error:

```
--> WITH DOCKER RUN --privileged ...
...
rm: can't remove '/var/earthly/dind/...': Resource busy
```

**Source Mounting**

Because `earthly` is running inside a container, it does not have access to your source code unless you grant it. This image expects to find a valid `Earthfile` in the working directory, which is set by default to `/workspace`.

**DOCKER\_HOST**

This image *does* include a functional Docker CLI, but does not include a full Docker daemon. If your `Earthfile` requires a Docker daemon of any sort, you will need to provide it through this environment variable.

If your daemon is on the same host as this container, you can also volume mount your hosts docker daemon using `-v /var/run/docker.sock:/var/run/docker.sock`. Note that this will cause `earthly` to use your hosts Docker daemon, and could lead to name conflicts if multiple copies of this image are run on the same host.

**-t**

This is the easiest way to ensure you get the nice, colorized output from `earthly`. Alternatively, you could provide the `FORCE_COLOR` environment variable.

#### Supported Environment Variables

| Variable Name                         | Default Values                 | Description                                                                                                                                                                                                   |
| ------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GLOBAL\_CONFIG                        |                                | Any valid YAML for the top-level `global` key in `config.yml`. Example: `{disable_analytics: true, local_registry_host: 'tcp://127.0.0.1:8371'}`                                                              |
| GIT\_CONFIG                           |                                | Any valid YAML for the top-level `git` key in `config.yml`. Example: `{example: {pattern: 'example.com/([^/]+)', substitute: 'ssh://git@example.com:2222/var/git/repos/$1.git', auth: ssh}}`                  |
| NO\_BUILDKIT                          |                                | Disables the embedded Buildkit daemon.                                                                                                                                                                        |
| DOCKER\_HOST                          | `/var/run/docker.sock`         | From Docker's CLI.                                                                                                                                                                                            |
| BUILDKIT\_HOST                        | `tcp://<hostname>:8372`        | The address of your BuildKit host. Use this when you have a remote `buildkitd` you would like to connect to.                                                                                                  |
| EARTHLY\_ADDITIONAL\_BUILDKIT\_CONFIG |                                | Additional `buildkitd` config to append to the generated configuration file.                                                                                                                                  |
| BUILDKIT\_TCP\_TRANSPORT\_ENABLED     |                                | Required to be set to `true` when using an external `buildkitd` via `BUILDKIT_HOST`. `true` when using the embedded `buildkitd`.                                                                              |
| BUILDKIT\_TLS\_ENABLED                |                                | Required when using an external `buildkitd` via `BUILDKITD_HOST`, and the external `buildkitd` requires mTLS. You will also need to mount certificates into the right place (`/etc/.earthly/certs`).          |
| CNI\_MTU                              | MTU of first default interface | Set this when we autodetect the MTU incorrectly. The device used for autodetection can be shown by the command `ip route show \| grep default \| cut -d' ' -f5 \| head -n 1`                                  |
| EARTHLY\_RESET\_TMP\_DIR              | `false`                        | Cleans out `/tmp/earthly` before running, if set to `true`. Useful when you host-mount an temporary directory across runs.                                                                                    |
| NETWORK\_MODE                         | `cni`                          | Specifies the networking mode of `buildkitd`. Default uses a CNI bridge network, configured with the `CNI_MTU`.                                                                                               |
| CACHE\_SIZE\_MB                       | `0`                            | How big should the `buildkitd` cache be allowed to get, in MiB? A value of 0 sets the cache size to "adaptive", causing BuildKit to detect the available size of the system and choose a limit automatically. |
| GIT\_URL\_INSTEAD\_OF                 |                                | Configure `git config --global url.<url>.insteadOf` rules to be used by `buildkitd`.                                                                                                                          |
| IP\_TABLES                            |                                | Override which binary (`iptables_nft` or `iptables_legacy`) is used for configuring `ip_tables`. Only set this if autodetection fails for your platform.                                                      |

# earthly/buildkitd

This image contains `buildkit` with some Earthly-specific setup. This is what Earthly will start when using a local daemon. You can also start it up yourself and use it as a remote/shared BuildKit daemon.

*Note that versions of this container have only ever been tested with their corresponding version of `earthly`.* Mismatched versions are unsupported.

### Tags

* `v0.6.30`, `latest`
* `v0.6.29`
* `v0.6.28`

### Quickstart

Want to just get started? Here are a couple sample `docker run` commands that cover the most common use-cases:

#### Simple Usage (Use Locally)

```bash
docker run --privileged -t -v earthly-tmp:/tmp/earthly:rw earthly/buildkitd:v0.6.30
```

Heres a quick breakdown:

* `--privileged` is required. This is because `earthly` needs some privileged `buildkit` functionality.
* `-t` tells Docker to emulate a TTY. This makes the `buildkit` log output colorized.
* `-v earthly-tmp:/tmp/earthly:rw` mounts (and creates, if necessary) the `earthly-tmp` Docker volume into the containers `/tmp/earthly`. This is used as a temporary/working directory for `buildkitd` during builds.

Assuming you are running this on your machine, you could use this `buildkitd` by setting `EARTHLY_BUILDKIT_HOST=docker-container://<container-name>`, or by specifying the appropriate values in `config.yml`.

#### Usage (Use As Remote)

```bash
docker run --privileged -t -v earthly-tmp:/tmp/earthly:rw -e BUILDKIT_TCP_TRANSPORT_ENABLED=true -p 8372:8372 earthly/buildkitd:v0.6.30
```

Omitting the options already discussed from the simple example:

* `-e BUILDKIT_TCP_TRANSPORT_ENABLED=true` makes `buildkitd` listen on a TCP port instead of a Unix socket.
* `-p 8372:8372` forwards the hosts port 8372 to the containers port 8372. When using TCP, `buildkit` will always listen on 8372, but you can configure the apparent port by forwarding a different port on your host.

Assuming you ran this on another machine named `fast-builder`, you could use this remote `buildkitd` by setting `EARTHLY_BUILDKIT_HOST=tcp://fast-builder:8372`, or by specifying the address in your `config.yml`.

### Using This Image

#### Requirements

**Privileged Mode**

This image needs to be run as a privileged container. This is because `buildkitd` needs appropriate access to start and run additional containers itself via `runc`.

**`/tmp/earthly`**

Because this folder sees *a lot* of traffic, its important that it remains fast. We *strongly* recommend using a Docker volume for mounting `/tmp/earthly`. If you do not, `buildkitd` can consume excessive disk space, operate very slowly, or it might not function correctly.

In some environments, not mounting `/tmp/earthly` as a Docker volume results in the following error:

```
--> WITH DOCKER RUN --privileged ...
...
rm: can't remove '/var/earthly/dind/...': Resource busy
```

**External Usage**

To use this image externally, it requires you to forward a port on your machine to the containers port 8372. You will need to ensure that external access to the machine on the port you chose is possible as well.

When using this container locally with `earthly`, please note that setting `EARTHLY_BUILDKIT_HOST` values with hosts `127.0.0.1`, `::1/128`, or `localhost` are considered local and will result in Earthly attempting to manage the BuildKit container itself. Consider using your hostname, or another alternative name in these cases.

#### Supported Environment Variables

| Variable Name                         | Default Values                 | Description                                                                                                                                                                  |
| ------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EARTHLY\_ADDITIONAL\_BUILDKIT\_CONFIG |                                | Additional `buildkitd` config to append to the generated configuration file.                                                                                                 |
| BUILDKIT\_TCP\_TRANSPORT\_ENABLED     |                                | Set to `true` when the `buildkitd` instance is going to be used remotely                                                                                                     |
| BUILDKIT\_TLS\_ENABLED                |                                | Set to `true` when the `buildkitd` instance will require mTLS from the clients. You will also need to mount certificates into the right place (`/etc/*.pem`).                |
| CNI\_MTU                              | MTU of first default interface | Set this when we autodetect the MTU incorrectly. The device used for autodetection can be shown by the command `ip route show \| grep default \| cut -d' ' -f5 \| head -n 1` |
| EARTHLY\_RESET\_TMP\_DIR              | `false`                        | Cleans out `/tmp/earthly` before running, if set to `true`. Useful when you host-mount an temporary directory across runs.                                                   |
| NETWORK\_MODE                         | `cni`                          | Specifies the networking mode of `buildkitd`. Default uses a CNI bridge network, configured with the `CNI_MTU`.                                                              |
| CACHE\_SIZE\_MB                       | `0`                            | How big should the `buildkitd` cache be allowed to get, in MiB? 0 is unbounded.                                                                                              |
| GIT\_URL\_INSTEAD\_OF                 |                                | Configure `git config --global url.<url>.insteadOf` rules used by `buildkitd`                                                                                                |
| IP\_TABLES                            |                                | Override which binary (`iptables_nft` or `iptables_legacy`) is used for configuring `ip_tables`. Only set this if autodetection fails for your platform.                     |

# Remote runners

Earthly supports running builds remotely via remote runners. Remote runners allow you to benefit from sharing the cache with other users of that remote runner. This is especially useful in CI environments where you want to share the cache between runs.

## Benefits

Typical use cases for remote runners include:

* Speeding up CI builds in sandboxed CI environments such as GitHub Actions, GitLab, CircleCI, and others. Most CI build times are improved by a factor of 2-4X via Satellites.
* Executing builds on AMD64/Intel architecture natively when working from an Apple Silicon machine (Apple M1/M2).
* Sharing compute and cache with coworkers or with the CI.
* Benefiting from high-bandwidth internet access from the cloud, thus allowing for fast downloads of dependencies and fast pushes for deployments. This is particularly useful if operating from a location with slow internet.
* Using Earthly from environments where privileged access or docker-in-docker are not supported. Note that the remote runner itself still requires privileged access.

## How remote runners work

When using remote runners, even though the build executes remotely, the following pieces of functionality are still available:

* Build logs are streamed to your local machine in real-time, just as if you were running the build locally
* Outputs (images and artifacts) resulting from the build, if any, are transferred back to your local machine
* Commands under `LOCALLY` execute on your local machine
* Secrets available locally, including Docker/Podman credentials are passed to the satellite whenever needed by the build
* Any images to be pushed are pushed directly from the satellite, using any Docker/Podman credentials available on the local system.

## Get started

To get started with remote runners managed by Earthly, check out [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites).

To get started with self-managed remote runners, see

* The [remote buildkit page](https://docs.earthly.dev/ci-integration/remote-buildkit)
* The [Kubernetes setup page](https://docs.earthly.dev/ci-integration/vendor-specific-guides/kubernetes)

# Remote caching

Earthly has the ability to share cache between different isolated CI runs and even with developers via remote caching. This page goes through the available features, common use-cases and situations where remote caching is most useful.

Remote caching is made possible by storing intermediate steps of a build in a cloud-based Docker registry. This cache can then be downloaded on another machine in order to skip common parts.

Note that there is yet another way to share cache between builds, via [Earthly Remote Runners](https://docs.earthly.dev/docs/remote-runners) (a commercial version of remote runners is [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites)). Using the cache of a remote runner is easier to manage, because there is no upload or download step (the cache is always there, available instantly) and no additional experimentation is required (everything is automatically cached without the need to experiment). This page only covers remote shared caching through the use of a registry.

## Types of remote cache

Earthly makes available two types of remote caching:

* [Inline cache](#inline-cache)
* [Explicit cache](#explicit-cache-advanced) (advanced)

For a summary of the differences see [comparison between inline and explicit cache](#comparison-between-inline-and-explicit-cache).

### Compatibility with major registry providers

Not all registries support the needed manifest formats to allow the usage of each kind of cache. Here is a compatibility matrix for many popular registries:

| Registry                  | Supports Inline Cache | Supports Explicit Cache | Notes                                                                                 |
| ------------------------- | :-------------------: | :---------------------: | ------------------------------------------------------------------------------------- |
| AWS ECR                   |           ✅           |            ❌            | <https://github.com/aws/containers-roadmap/issues/876>                                |
| Google GCR                |           ✅           |            ❌            |                                                                                       |
| Google Artifact Registry  |           ✅           |            ✅            |                                                                                       |
| Azure ACR                 |           ✅           |            ✅            |                                                                                       |
| Docker Hub                |           ✅           |            ✅            |                                                                                       |
| GitHub Container Registry |           ✅           |            ✅            |                                                                                       |
| GitLab Container Registry |           ✅           |            ✅            |                                                                                       |
| Self-Hosted `registry:2`  |           ✅           |            ✅            |                                                                                       |
| JFrog Artifactory         |           ✅           |            ✅            | Only versions > 7.31.10 work, due to <https://www.jfrog.com/jira/browse/RTFACT-26179> |

### Inline cache

Inline caching is the easiest to configure. It essentially makes use of any image already being pushed to the registry and adds some very small metadata (a few KiB) as part of its configuration about how Earthly is able to reuse that image for future runs.

The key benefit of this approach is that you get the upload for free if you anyway push images to the registry.

#### How to use inline caching

In order to enable inline caching, simply add `--ci` in your invocation of `earthly` in your CI, or `--use-inline-cache` on individual developer's machines. If the `--push` command is also specified, the use of the cache will be read-write.

In CI, read-only inline cache (typically in PR builds):

```bash
earthly --ci +some-target
```

In CI, read-write inline cache (typically in master/main branch builds):

```bash
earthly --ci --push +some-target
```

On developer's computer (optional):

```bash
earthly --use-inline-cache +some-target
```

The options mentioned above are also available as environment variables. See [Earthly command reference](https://docs.earthly.dev/docs/earthly-command) for more information.

The way this works underneath is that Earthly uses `SAVE IMAGE --push` declarations as source and destination for any inline cache.

In case different Docker tags are used in branch or PR builds, it is possible to use additional cache sources via [`SAVE IMAGE --cache-from=...`](https://docs.earthly.dev/earthfile#save-image). This may be useful so that PR builds are able to use the main branch cache. Here is a simple example:

```Dockerfile
FROM ...
...
ARG BRANCH=master
SAVE IMAGE --cache-from=mycompany/myimage:master --push mycompany/myimage:$BRANCH
```

{% hint style="info" %}
The `--ci` flag will enable, among other things, both `--use-inline-cache` and `--save-inline-cache` flags. The `--use-inline-cache` flag is required to enable importing existing caches, and the `--save-inline-cache` flag is required to enable exporting images to the remote cache.

Since `VERSION 0.6` the inline cache is only exported to images [that are connected to the initial target through a chain of BUILD commands](https://docs.earthly.dev/docs/earthfile#build).
{% endhint %}

#### Optimizing inline cache performance

Inline caching is very easy to use, however it can also turn out to be ineffective for some builds. One limitation is that only the layers that end up in uploaded images are actually used. Certain intermediate layers (e.g. targets only used for compiling binaries) will not exist.

If you find that certain steps could benefit from being cached but are not, you may consider creating additional images for those steps specifically. All you need to do is add the following at the end. Use a Docker tag that is not used for anything else.

```Dockerfile
SAVE IMAGE --push <docker-tag>
```

Note however that adding more images to the build results in additional time spent uploading them. Disregard the performance of the very first upload, as a fresh push is always less performant because there is no commonality with any previous run.

#### Example of using inline caching

Good example uses of inline caching are the Earthly [C++](https://github.com/earthly/earthly/tree/main/examples/cpp) and [Scala](https://github.com/earthly/earthly/tree/main/examples/scala) samples.

In the C++ case, a lot of computation is saved as a result of the `apt-get install` command. Reusing the cache improves performance by a factor of 4X.

In the Scala case, time is saved from processing the dependencies, resulting in a 3X performance improvement.

In both cases, a major benefit is that we are anyway pushing the images to the cloud via the `SAVE IMAGE --push` commands. So there is no performance penalty on the cache upload side. The command that would be used in the CI to execute the builds together with inline caching is

```bash
earthly --ci --push +docker
```

### Explicit cache (advanced)

Explicit caching requires that you dedicate a Docker tag specifically for cache storage. Unlike inline caching, this tag is not meant to be used for anything else. For this reason, uploading the cache is an added step that takes additional time.

#### How to use explicit caching

To enable explicit caching, use the flag `--remote-cache=...` to specify the Docker tag to use as cache. Make sure that this Docker tag is not used for anything else (e.g. DO NOT use `myimage:latest`, in case `latest` is used in a critical workflow).

For example, if the Docker tag used for explicit caching is `mycompany/myimage:cache`, then the flag can be used as follows.

In CI, read-only inline cache (typically in PR builds):

```bash
earthly --ci --remote-cache=mycompany/myimage:cache +some-target
```

In CI, read-write inline cache (typically in master/main branch builds):

```bash
earthly --ci --remote-cache=mycompany/myimage:cache --push +some-target
```

On developer's computer (optional):

```bash
earthly --remote-cache=mycompany/myimage:cache +some-target
```

The options mentioned above are also available as environment variables. See [Earthly command reference](https://docs.earthly.dev/docs/earthly-command) for more information.

{% hint style="info" %}
**Note**

If a project has multiple CI pipelines or `earthly` invocations, it is recommended to use different `--remote-cache` Docker tags for each pipeline or invocation. This will prevent the cache from being overwritten in ways in which it makes it less effective.
{% endhint %}

{% hint style="info" %}
**Note**

It is currently not possible to push both inline and explicit caches in a single run.
{% endhint %}

#### Optimizing explicit cache performance (advanced)

Explicit caching works by storing a cache containing all the layers of the final target, plus any target containing `SAVE IMAGE --push ...`. If additional targets need to be added as part of the cache, it is possible to add `SAVE IMAGE --cache-hint` (no Docker tag necessary) at the end, in order to mark them for explicit caching.

```Dockerfile
deps:
  COPY go.mod go.sum ./
  RUN go mod download
  SAVE IMAGE --cache-hint
```

Making use of explicit caching effectively may not always be possible. Sometimes the overhead of uploading and redownloading the cache defeats the purpose of gaining build performance. Oftentimes, multiple iterations of trial-and-error need to be attempted in order to optimize its effectiveness. Keep in mind that caching compute-heavy targets is more likely to yield results, rather than download-heavy targets.

As an additional setting available, Earthly can be instructed to save all intermediary steps as part of the explicit cache. The setting `--max-remote-cache` can be used to enable this. Note that this results in large uploads and is usually not very effective. An example where this feature is useful, however, is when you would like to optimize CI run times in PRs, and are willing to sacrifice CI run times in default branch builds. This can be achieved by enabling `--push` and `--max-remote-cache` on the default branch builds only.

#### Example of using explicit caching

A good example of using explicit caching is this [integration test example](https://github.com/earthly/earthly/tree/main/examples/integration-test). The target `+project-files` is perfect for introducing a cache hint via `SAVE IMAGE --cache-hint`. The processing that takes place as part of installing Scala and compiling the dependencies is sufficiently compute-intensive to save \~2 min from the total build time in CI. In addition, these dependencies change rarely enough that the cache can be utilized consistently.

A typical invocation of the build to make use of the explicit cache:

```bash
earthly --ci --remote-cache=mycompany/integration-example:cache --push +all
```

### Comparison between inline and explicit cache

Inline and explicit caching have similar traits, but they also have a number of fundamental differences.

The key similarity is that both types of caches make use of Docker tags being pushed to an image registry in order to store the cache.

The most important difference is that inline caching relies on image uploads that are already being made. And as such, the cache may be split across multiple separate images. Every `SAVE IMAGE --push` command adds more cacheable targets in the form of separate images. However, in the case of explicit caching, the entire cache is stored as part of a single Docker tag and every `SAVE IMAGE --cache-hint` command adds more cacheable targets within the image. This final image containing all the explicit cache cannot be used for anything else. So as a user, you incur the performance cost of both the upload and the subsequent download.

Below is a summary of the different characteristics of each type of cache.

#### Key takeaways for inline caching

* Cache is embedded within images that are already being pushed. No new layers are added to the images, only a few KiB of metadata.
* Very easy to use (just add `--ci` to your `earthly` invocations in CI)
* It is usually effective right away, with little modifications
* Typically you incur the performance cost only for the subsequent download. Upload is for free if you are pushing images anyway
* By default, caches only the images being pushed
* You can add more cache via additional `SAVE IMAGE --push <docker-tag>` commands

#### Key takeaways for explicit caching

* Cache is uploaded as part of a new Docker tag that should not be used for anything else
* The only available choice if no images are already pushed during the build
* More control over what is being cached and what is not. However it often requires some level of experimentation to get right.
* Incur the performance cost for both the upload and the download
* By default, caches only the layers of the target being built, and not of any other referenced targets
* You can cache additional targets by adding `SAVE IMAGE --cache-hint` commands

## When to use remote caching

There are several situations where remote caching can provide a significant performance boost. The following are only a few examples of how to get a feel for its usefulness.

### Compute-heavy vs Download-heavy

In general remote caching is very useful when there is a significant computation overhead during the execution of your build. Assuming that the inputs of that computation do not change regularly, then remote caching could be a good candidate. If a time-consuming operation, however, is not compute-heavy, but rather download-heavy, then remote caching may not be as effective (it's one download versus another).

As an example of this distinction, consider the use of the `apk` tool shipped in `alpine` images. Installing packages via `apk` is download-heavy, but usually not very compute-heavy, and so using remote caching to offset `apk` download times might not be as effective. On the other hand, consider `apt-get` tool shipped in `ubuntu` images. Besides performing downloads, `apt-get` also performs additional post-download steps which tend to be compute-intensive. For this reason, remote caching is usually very effective here.

Similarly to the comparison between `apk` and `apt-get`, similar remarks can be made about the various language-specific dependency management tools. Some will be pure download-based (e.g. `go mod download`), while others will be a mix of download and computation (.e.g `sbt`).

### An intermediate result is small and doesn't change much

An area where remote caching is particularly impactful are cases where a rare-changing prerequisite downloads many dependencies and/or performs intensive computation, but the end result is relatively small (e.g. a single binary). Passing this prerequisite over the wire as part of the remote caching is very fast (especially if the downloads required to generate it are not used anywhere else), whereas regenerating it requires a lot of work.

### Monorepo and Polyrepo setups

An excellent example of the above are typical inter-project dependencies. Regardless of whether your layout is a monorepo or a polyrepo, if projects reference artifacts or images from each other, then whatever tools used to generate those artifacts or images are usually not required across projects. In such cases it is possible to prevent entire target trees of downloads and computation and simply download the final result using the remote cache.

A simple way to visualize this use-case is comparing the performance of a build that takes place behind a `FROM +some-target` instruction versus just using the previously built image directly. If `+some-target` has a `SAVE IMAGE --push myimage:latest` instruction, then the performance becomes almost the same to using `FROM myimage:latest` directly.

### CIs that operate in a sandbox

Modern CIs execute in a sandbox. They start with a blank slate and need to download and regenerate everything from scratch. Examples of such CIs: GitHub Actions, Circle CI, DroneCI, GitLab CI. Such CIs benefit greatly from being able to share precomputed steps between runs.

If, however, you are using a CI which reuses the same environment (e.g. Jenkins, BuildKite - depending on how they are configured), then simply relying on the local cache is enough.

### Remote caching for developers

It is possible to use cache in read-only mode for developers to speed up local development. This can be achieved by enabling read-write remote caching in CI and read-only cache for individual developers. Since all Earthly cache is kept in Docker registries, managing access to the cache can be controlled by managing access to individual Docker images.

Note however that there is small performance penalty for regularly checking the remote registry on every run.

## Alternatives

An alternative to using remote caching is to use [Earthly Remote Runners](https://docs.earthly.dev/docs/remote-runners) (a commercial version of remote runners is [Earthly Satellites](https://github.com/earthly/earthly/blob/docs-0.6/docs/cloud/satelllites.md)). Remote runners execute the build remotely, and this allows the cache to be located in close proximity to the execution, which is very efficient. Satellites are also significantly easier to set up, as the caching just works and there is no need for additional experimentation.

# Earthfile reference

Earthfiles are comprised of a series of target declarations and recipe definitions. Earthfiles are named `Earthfile`, regardless of their location in the codebase.

Earthfiles have the following rough structure:

```
<base-recipe>
...

<target-name>:
    <recipe>
    ...

<target-name>:
    <recipe>
    ...

<command-name>:
    <recipe>
    ...
```

Each recipe contains a series of commands, which are defined below. For an introduction into Earthfiles, see the [Basics page](https://docs.earthly.dev/basics).

## FROM

#### Synopsis

* `FROM <image-name>`
* `FROM [--platform <platform>] [--allow-privileged] <target-ref> [--<build-arg-key>=<build-arg-value>...]`

#### Description

The `FROM` command initializes a new build environment and sets the base image for subsequent instructions. It works similarly to the classical [Dockerfile `FROM` instruction](https://docs.docker.com/engine/reference/builder/#from), but it has the added ability to use another [target](https://docs.earthly.dev/docs/guides/target-ref#target-reference)'s image as the base image.

Examples:

* Classical reference: `FROM alpine:latest`
* Local reference: `FROM +another-target`
* Relative reference: `FROM ./subdirectory+some-target` or `FROM ../otherdirectory+some-target`
* Absolute reference: `FROM /absolute/path+some-target`
* Remote reference from a public or [private](https://docs.earthly.dev/docs/guides/auth) git repository: `FROM github.com/example/project+remote-target`

The `FROM` command does not mark any saved images or artifacts of the referenced target for output, nor does it mark any push commands of the referenced target for pushing. For that, please use [`BUILD`](#build).

{% hint style="info" %}
**Note**

The `FROM ... AS ...` form available in the classical Dockerfile syntax is not supported in Earthfiles. Instead, define a new Earthly target. For example, the following Dockerfile

```Dockerfile
# Dockerfile

FROM alpine:3.15 AS build
# ... instructions for build

FROM build as another
# ... further instructions inheriting build

FROM busybox as yet-another
COPY --from=build ./a-file ./
```

can become

```Dockerfile
# Earthfile

build:
    FROM alpine:3.15
    # ... instructions for build
    SAVE ARTIFACT ./a-file

another:
    FROM +build
    # ... further instructions inheriting build

yet-another:
    FROM busybox
    COPY +build/a-file ./
```

{% endhint %}

#### Options

**`--<build-arg-key>=<build-arg-value>`**

Sets a value override of `<build-arg-value>` for the build arg identified by `<build-arg-key>`. See also [BUILD](#build) for more details about build args.

**`--platform <platform>`**

Specifies the platform to build on.

For more information see the [multi-platform guide](https://docs.earthly.dev/docs/guides/multi-platform).

**`--allow-privileged`**

Allows remotely-referenced targets to request privileged capabilities; this flag has no effect when referencing local targets.

Additionally, for privileged capabilities, earthly must be invoked on the command line with the `--allow-privileged` (or `-P`) flag.

For example, consider two Earthfiles, one hosted on a remote GitHub repo:

```Dockerfile
# github.com/earthly/example
FROM alpine:latest
elevated-target:
    RUN --privileged echo do something requiring privileged access.
```

and a local Earthfile:

```Dockerfile
FROM alpine:latest
my-target:
    FROM --allow-privileged github.com/earthly/example+elevated-target
    # ... further instructions inheriting remotely referenced Earthfile
```

then one can build `my-target` by invoking earthly with the `--allow-privileged` (or `-P`) flag:

```bash
earthly --allow-privileged +my-target
```

**`--build-arg <key>=<value>` (deprecated)**

This option is deprecated. Use `--<build-arg-key>=<build-arg-value>` instead.

## RUN

#### Synopsis

* `RUN [--push] [--entrypoint] [--privileged] [--secret <env-var>=<secret-ref>] [--ssh] [--mount <mount-spec>] [--] <command>` (shell form)
* `RUN [[<flags>...], "<executable>", "<arg1>", "<arg2>", ...]` (exec form)

#### Description

The `RUN` command executes commands in the build environment of the current target, in a new layer. It works similarly to the [Dockerfile `RUN` command](https://docs.docker.com/engine/reference/builder/#run), with some added options.

The command allows for two possible forms. The *exec form* runs the command executable without the use of a shell. The *shell form* uses the default shell (`/bin/sh -c`) to interpret the command and execute it. In either form, you can use a `\` to continue a single `RUN` instruction onto the next line.

When the `--entrypoint` flag is used, the current image entrypoint is used to prepend the current command.

To avoid any ambiguity regarding whether an argument is a `RUN` flag option or part of the command, the delimiter `--` may be used to signal the parser that no more `RUN` flag options will follow.

#### Options

**`--push`**

Marks the command as a "push command". Push commands are only executed if all other non-push instructions succeed. In addition, push commands are never cached, thus they are executed on every applicable invocation of the build.

Push commands are not run by default. Add the `--push` flag to the `earthly` invocation to enable pushing. For example

```bash
earthly --push +deploy
```

Push commands were introduced to allow the user to define commands that have an effect external to the build. This kind of effects are only allowed to take place if the entire build succeeds. Good candidates for push commands are uploads of artifacts to artifactories, commands that make a change to an external environment, like a production or staging environment.

Note that non-push commands are not allowed to follow a push command within a recipe.

**`--no-cache`**

Force the command to run every time; ignoring any cache. Any commands following the invocation of `RUN --no-cache`, will also ignore the cache. If `--no-cache` is used as an option on the `RUN` statement within a `WITH DOCKER` statement, all commands after the `WITH DOCKER` will also ignore the cache.

**`--entrypoint`**

Prepends the currently defined entrypoint to the command.

This option is useful for replacing `docker run` in a traditional build environment. For example, a command like

```bash
docker run --rm -v "$(pwd):/data" cytopia/golint .
```

Might become the following in an Earthfile

```Dockerfile
FROM cytopia/goling
COPY . /data
RUN --entrypoint .
```

**`--privileged`**

Allows the command to use privileged capabilities.

Note that privileged mode is not enabled by default. In order to use this option, you need to additionally pass the flag `--allow-privileged` (or `-P`) to the `earthly` command. Example:

```bash
earthly --allow-privileged +some-target
```

**`--secret <env-var>=<secret-ref> | <secret-id>`**

Makes available a secret, in the form of an env var (its name is defined by `<env-var>`), to the command being executed. If you only specify `<secret-id>`, the name of the env var will be `<secret-id>` and its value the value of `<secret-id>`.

The `<secret-ref>` needs to be of the form `+secrets/<secret-id>`, where `<secret-id>` is the identifier passed to the `earthly` command when passing the secret: `earthly --secret <secret-id>=<value>`.

Here is an example that showcases both syntaxes:

```Dockerfile
release:
    RUN --push --secret GITHUB_TOKEN=+secrets/GH_TOKEN github-release upload
release-short:
    RUN --push --secret GITHUB_TOKEN github-release upload
```

```bash
earthly --secret GH_TOKEN="the-actual-secret-token-value" +release
earthly --secret GITHUB_TOKEN="the-actual-secret-token-value" +release-short
```

An empty string is also allowed for `<secret-ref>`, allowing for optional secrets, should it need to be disabled.

```Dockerfile
release:
    ARG SECRET_ID=+secrets/GH_TOKEN
    RUN --push --secret GITHUB_TOKEN=$SECRET_ID github-release upload
release-short:
    ARG SECRET_ID=GITHUB_TOKEN
    RUN --push --secret $SECRET_ID github-release upload
```

```bash
earthly +release --SECRET_ID=""
earthly +release-short --SECRET_ID=""
```

It is also possible to mount a secret as a file with `RUN --mount type=secret,id=+secret/secret-id,target=/path/of/secret,mode=0400`. See `--mount` below.

For more information on how to use secrets see the [build arguments and secrets guide](https://docs.earthly.dev/docs/guides/build-args). See also the [Cloud secrets guide](https://docs.earthly.dev/earthly-cloud/cloud-secrets).

**`--ssh`**

Allows a command to access the ssh authentication client running on the host via the socket which is referenced by the environment variable `SSH_AUTH_SOCK`.

Here is an example:

```Dockerfile
RUN mkdir -p ~/.ssh && \
    echo 'github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==' >> ~/.ssh/known_hosts && \
    echo 'gitlab.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsj2bNKTBSpIYDEGk9KxsGh3mySTRgMtXL583qmBpzeQ+jqCMRgBqB98u3z++J1sKlXHWfM9dyhSevkMwSbhoR8XIq/U0tCNyokEi/ueaBMCvbcTHhO7FcwzY92WK4Yt0aGROY5qX2UKSeOvuP4D6TPqKF1onrSzH9bx9XUf2lEdWT/ia1NEKjunUqu1xOB/StKDHMoX4/OKyIzuS0q/T1zOATthvasJFoPrAjkohTyaDUz2LN5JoH839hViyEG82yB+MjcFV5MU3N1l1QL3cVUCh93xSaua1N85qivl+siMkPGbO5xR/En4iEY6K2XPASUEMaieWVNTRCtJ4S8H+9' >> ~/.ssh/known_hosts
RUN --ssh git config --global url."git@github.com:".insteadOf "https://github.com/" && \
    go mod download
```

**`--mount <mount-spec>`**

Mounts a file or directory in the context of the build environment.

The `<mount-spec>` is defined as a series of comma-separated list of key-values. The following keys are allowed

| Key       | Description                                                                                                | Example                |
| --------- | ---------------------------------------------------------------------------------------------------------- | ---------------------- |
| `type`    | The type of the mount. Currently only `cache`, `tmpfs`, and `secret` are allowed.                          | `type=cache`           |
| `target`  | The target path for the mount.                                                                             | `target=/var/lib/data` |
| `mode`    | The permission of the mounted file, in octal format (the same format the chmod unix command line expects). | `mode=0400`            |
| `id`      | The secret ID for the contents of the `target` file, only applicable for `type=secret`.                    | `id=+secrets/password` |
| `sharing` | The sharing mode (`locked`, `shared`, `private`) for the cache mount, only applicable for `type=cache`.    | `sharing=shared`       |

For cache mounts, the sharing mode can be one of the following:

* `locked` (default) - the cache mount is locked for the duration of the execution, other concurrent builds will wait for the lock to be released.
* `shared` - the cache mount is shared between all concurrent builds.
* `private` - if another concurrent build attempts to use the cache, a new (empty) cache will be created for the concurrent build.

**Examples:**

Persisting cache for a single `RUN` command, even when its dependencies change:

```Dockerfile
ENV GOCACHE=/go-cache
RUN --mount=type=cache,target=/go-cache go build main.go
```

{% hint style="warning" %}
Note that mounts cannot be shared between targets, nor can they be shared within the same target, if the build-args differ between invocations.
{% endhint %}

Mounting a secret as a file:

```Dockerfile
RUN --mount=type=secret,id=+secrets/netrc,target=/root/.netrc curl https://example.earthly.dev/restricted/example-file-that-requires-auth > data
```

The contents of the secret `/root/.netrc` file can then be specified from the command line as:

```bash
earthly --secret netrc="machine example.earthly.dev login myusername password mypassword" +base
```

or by passing the contents of an existing file from the host filesystem:

```bash
earthly --secret-file netrc="$HOME/.netrc" +base
```

**`--interactive` / `--interactive-keep`**

Opens an interactive prompt during the target build. An interactive prompt must:

1. Be the last issued command in the target, with the exception of `SAVE IMAGE` commands. This also means that you cannot `FROM` a target containing a `RUN --interactive`.
2. Be the only `--interactive` target within the run.
3. Not be within a `LOCALLY`-designated target.

**Examples:**

Start an interactive python REPL:

```Dockerfile
python:
    FROM alpine:3.15
    RUN apk add python
    RUN --interactive python
```

Start `bash` to tweak an image by hand. Changes made will be included:

```Dockerfile
build:
    FROM alpine:3.15
    RUN apk add bash
    RUN --interactive-keep bash
```

## COPY

#### Synopsis

* `COPY [options...] <src>... <dest>` (classical form)
* `COPY [options...] <src-artifact>... <dest>` (artifact form)
* `COPY [options...] (<src-artifact> --<build-arg-key>=<build-arg-value>...) <dest>` (artifact form with build args)

#### Description

The command `COPY` allows copying of files and directories between different contexts.

The command may take a couple of possible forms. In the *classical form*, `COPY` copies files and directories from the build context into the build environment - in this form, it works similarly to the [Dockerfile `COPY` command](https://docs.docker.com/engine/reference/builder/#copy). In the *artifact form*, `COPY` copies files or directories (also known as "artifacts" in this context) from the artifact environment of other build targets into the build environment of the current target. Either form allows the use of wildcards for the sources.

The parameter `<src-artifact>` is an [artifact reference](https://docs.earthly.dev/guides/target-ref#artifact-reference) and is generally of the form `<target-ref>/<artifact-path>`, where `<target-ref>` is the reference to the target which needs to be built in order to yield the artifact and `<artifact-path>` is the path within the artifact environment of the target, where the file or directory is located. The `<artifact-path>` may also be a wildcard.

The `COPY` command does not mark any saved images or artifacts of the referenced target for output, nor does it mark any push commands of the referenced target for pushing. For that, please use [`BUILD`](#build).

The classical form of the `COPY` command differs from Dockerfiles in two cases:

* URL sources are not yet supported.
* Absolute paths are not supported - sources in the current directory cannot be referenced with a leading `/`

{% hint style="info" %}
**Note**

To prevent Earthly from copying unwanted files, you may specify file patterns to be excluded from the build context using an [`.earthlyignore`](https://docs.earthly.dev/docs/earthfile/earthlyignore) file. This file has the same syntax as a [`.dockerignore` file](https://docs.docker.com/engine/reference/builder/#dockerignore-file).
{% endhint %}

#### Options

**`--dir`**

The option `--dir` changes the behavior of the `COPY` command to copy the directories themselves, rather than the contents of the directories. It allows the command to behave similarly to a `cp -r` operation on a unix system. This allows the enumeration of several directories to be copied over on a single line (and thus, within a single layer). For example, the following two are equivalent with respect to what is being copied in the end (but not equivalent with respect to the number of layers used).

```Dockerfile
COPY dir1 dir1
COPY dir2 dir2
COPY dir3 dir3
```

```Dockerfile
COPY --dir dir1 dir2 dir3 ./
```

If the directories were copied without the use of `--dir`, then their contents would be merged into the destination.

**`--<build-arg-key>=<build-arg-value>`**

Sets a value override of `<build-arg-value>` for the build arg identified by `<build-arg-key>`, when building the target containing the mentioned artifact. See also [BUILD](#build) for more details about the build arg options.

Note that build args and the artifact references they apply to need to be surrounded by parenthesis:

```Dockerfile
COPY (+target1/artifact --arg1=foo --arg2=bar) ./dest/path
```

**`--keep-ts`**

Instructs Earthly to not overwrite the file creation timestamps with a constant.

**`--keep-own`**

Instructs Earthly to keep file ownership information. This applies only to the *artifact form* and has no effect otherwise.

{% hint style="info" %}
Note that you must include the flag in the corresponding `SAVE ARTIFACT --keep-own ...` command, if using *artifact form*.
{% endhint %}

**`--if-exists`**

Only copy source if it exists; if it does not exist, earthly will simply ignore the COPY command and won't treat any missing sources as failures.

**`--from`**

Although this option is present in classical Dockerfile syntax, it is not supported by Earthfiles. You may instead use a combination of `SAVE ARTIFACT` and `COPY` *artifact form* commands to achieve similar effects. For example, the following Dockerfile

```Dockerfile
# Dockerfile
COPY --from=some-image /path/to/some-file.txt ./
```

... would be equivalent to `final-target` in the following Earthfile

```Dockerfile
# Earthfile
intermediate:
    FROM some-image
    SAVE ARTIFACT /path/to/some-file.txt

final-target:
    COPY +intermediate/some-file.txt ./
```

**`--platform <platform>`**

In *artifact form*, it specifies the platform to build the artifact on.

For more information see the [multi-platform guide](https://docs.earthly.dev/docs/guides/multi-platform).

**`--allow-privileged`**

Same as [`FROM --allow-privileged`](#allow-privileged).

**`--build-arg <key>=<value>` (deprecated)**

The option `--build-arg` is deprecated. Use `--<build-arg-key>=<build-arg-value>` instead.

#### Examples

Assuming the following directory tree, of a folder named `test`:

```
test
  └── file
```

Here is how the following copy commands will behave:

```
# Copies the contents of the test directory.
# To access the file, it would be found at ./file
COPY test .

# Also copies the contents of the test directory.
# To access the file, it would be found at ./file
COPY test/* .

# Copies the whole test folder.
# To access the file, it would be found at ./test/file
COPY --dir test .
```

One can also copy from other Earthfile targets:

```
FROM alpine:3.15
dummy-target:
    RUN echo aGVsbG8= > encoded-data
    SAVE ARTIFACT encoded-data
example:
    COPY +dummy-target/encoded-data .
    RUN cat encoded-data | base64 -d
```

Parentheses are required when passing build-args:

```
FROM alpine:3.15
RUN apk add coreutils # required for base32 binary
dummy-target:
    ARG encoder="base64"
    RUN echo hello | $encoder > encoded-data
    SAVE ARTIFACT encoded-data
example:
    COPY ( +dummy-target/encoded-data --encoder=base32 ) .
    RUN cat encoded-data | base32 -d
```

For detailed examples demonstrating how other scenarios may function, please see our [test suite](https://github.com/earthly/earthly/blob/main/tests/copy.earth).

## ARG

#### Synopsis

* `ARG [--required] <name>[=<default-value>]` (constant form)
* `ARG [--required] <name>=$(<default-value-expr>)` (dynamic form)

#### Description

The command `ARG` declares a variable (or arg) with the name `<name>` and with an optional default value `<default-value>`. If no default value is provided, then empty string is used as the default value.

This command works similarly to the [Dockerfile `ARG` command](https://docs.docker.com/engine/reference/builder/#arg), with a few differences regarding the scope and the predefined args (called builtin args in Earthly). The variable's scope is always limited to the recipe of the current target or command and only from the point it is declared onward. For more information regarding builtin args, see the [builtin args page](https://docs.earthly.dev/docs/earthfile/builtin-args).

In its *constant form*, the arg takes a default value defined as a constant string. If the `<default-value>` is not provided, then the default value is an empty string. In its *dynamic form*, the arg takes a default value defined as an expression. The expression is evaluated at run time and its result is used as the default value. The expression is interpreted via the default shell (`/bin/sh -c`) within the build environment.

If an `ARG` is defined in the `base` target of the Earthfile, then it becomes a global `ARG` and it is made available to every other target or command in that file, regardless of their base images used.

The value of an arg can be overridden either from the `earthly` command

```bash
earthly <target-ref> --<name>=<override-value>
```

or from a command from another target, when implicitly or explicitly invoking the target containing the `ARG`

```Dockerfile
BUILD <target-ref> --<name>=<override-value>
COPY (<target-ref>/<artifact-path> --<name>=<override-value>) <dest-path>
FROM <target-ref> --<name>=<override-value>
```

for example

```Dockerfile
BUILD +binary --NAME=john
COPY (+binary/bin --NAME=john) ./
FROM +docker-image --NAME=john
```

For more information on how to use build args see the [build arguments and secrets guide](https://docs.earthly.dev/docs/guides/build-args). A number of builtin args are available and are pre-filled by Earthly. For more information see [builtin args](https://docs.earthly.dev/docs/earthfile/builtin-args).

#### Options

**`--required`**

A required `ARG` must be provided at build time and can never have a default value. Required args can help eliminate cases where the user has unexpectedly set an `ARG` to `""`.

```
target-required:
    # user must supply build arg for target
    ARG --required NAME

build-linux:
    # or explicitly supply in build command
    BUILD +target-required --NAME=john
```

{% hint style="info" %}
Earthly, by default, only supports dynamic values which start with the `$(...)` shell-out syntax -- passing a value such as `--name="the honourable $(whoami)"` will fail to execute the `whoami` program.

This behaviour can be changed with the experimental [`VERSION` `--shell-out-anywhere` feature flag](https://docs.earthly.dev/docs/features#feature-flags). This feature additionally allows shelling-out in *any* earthly command.
{% endhint %}

## SAVE ARTIFACT

#### Synopsis

* `SAVE ARTIFACT [--keep-ts] [--keep-own] [--if-exists] [--force] <src> [<artifact-dest-path>] [AS LOCAL <local-path>]`

#### Description

The command `SAVE ARTIFACT` copies a file, a directory, or a series of files and directories represented by a wildcard, from the build environment into the target's artifact environment.

If `AS LOCAL ...` is also specified, it additionally marks the artifact to be copied to the host at the location specified by `<local-path>`, once the build is deemed as successful. Note that local artifacts are only produced by targets that are run directly with `earthly`, or when invoked using [`BUILD`](#build).

If `<artifact-dest-path>` is not specified, it is inferred as `/`.

Files within the artifact environment are also known as "artifacts". Once a file has been copied into the artifact environment, it can be referenced in other places of the build (for example in a `COPY` command), using an [artifact reference](https://docs.earthly.dev/guides/target-ref#artifact-reference).

{% hint style="info" %}
**Hint**

In order to inspect the contents of an artifacts environment, you can run

```bash
earthly --artifact +<target>/* ./output/
```

This command dumps the contents of the artifact environment of the target `+<target>` into a local directory called `output`, which can be inspected directly.
{% endhint %}

{% hint style="danger" %}
**Important**

Note that there is a distinction between a *directory artifact* and *file artifact* when it comes to local output. When saving an artifact locally, a directory artifact will **replace** the destination entirely, while a file (or set of files) artifact will be copied **into** the destination directory.

```Dockerfile
# This will wipe ./destination and replace it with the contents of the ./my-directory artifact.
SAVE ARTIFACT ./my-directory AS LOCAL ./destination
# This will merge the contents of ./my-directory into ./destination.
SAVE ARTIFACT ./my-directory/* AS LOCAL ./destination
```

{% endhint %}

{% hint style="danger" %}
**Important**

As of [`VERSION 0.6`](#version), local artifacts are only saved [if they are connected to the initial target through a chain of `BUILD` commands](#what-is-being-output-and-pushed).
{% endhint %}

#### Options

**`--keep-ts`**

Instructs Earthly to not overwrite the file creation timestamps with a constant.

**`--keep-own`**

Instructs Earthly to keep file ownership information.

**`--if-exists`**

Only save artifacts if they exists; if not, earthly will simply ignore the SAVE ARTIFACT command and won't treat any missing sources as failures.

**`--force`**

Force save operations which may be unsafe, such as writing to (or overwriting) a file or directory on the host filesystem located outside of the context of the directory containing the Earthfile.

#### Examples

Assuming the following directory tree, of a folder named `test`:

```
test
  └── file

```

Here is how the following `SAVE ARTIFACT ... AS LOCAL` commands will behave:

```
WORKDIR base
COPY test .

# This will copy the base folder into the output directory.
# You would find file at out-dot/base/file.
SAVE ARTIFACT . AS LOCAL out-dot/

# This will copy the contents of the base folder into the output directory.
# You would find sub-file at out-glob/file. Note the base directory is not in the output.
SAVE ARTIFACT ./* AS LOCAL out-glob/
```

For detailed examples demonstrating how other scenarios may function, please see our [test suite](https://github.com/earthly/earthly/blob/main/tests/file-copying.earth).

## SAVE IMAGE

#### Synopsis

* `SAVE IMAGE [--cache-from=<cache-image>] [--push] <image-name>...` (output form)
* `SAVE IMAGE --cache-hint` (cache hint form)

#### Description

In the *output form*, the command `SAVE IMAGE` marks the current build environment as the image of the target and assigns one or more output image names.

In the *cache hint form*, it instructs Earthly that the current target should be included as part of the explicit cache. For more information see the [remote caching guide](https://docs.earthly.dev/docs/remote-caching).

{% hint style="info" %}
**Assigning multiple image names**

The `SAVE IMAGE` command allows you to assign more than one image name:

```Dockerfile
SAVE IMAGE my-image:latest my-image:1.0.0 my-example-registry.com/another-image:latest
```

Or

```Dockerfile
SAVE IMAGE my-image:latest
SAVE IMAGE my-image:1.0.0
SAVE IMAGE my-example-registry.com/another-image:latest
```

{% endhint %}

{% hint style="danger" %}
**Important**

As of [`VERSION 0.6`](#version), the `--referenced-save-only` feature flag is enabled by default. Images are only saved [if they are connected to the initial target through a chain of `BUILD` commands](#what-is-being-output-and-pushed).
{% endhint %}

#### Options

**`--push`**

The `--push` options marks the image to be pushed to an external registry after it has been loaded within the docker daemon available on the host.

If inline caching is enabled, the `--push` option also instructs Earthly to use the specified image names as cache sources.

The actual push is not executed by default. Add the `--push` flag to the earthly invocation to enable pushing. For example

```bash
earthly --push +docker-image
```

**`--cache-from=<cache-image>`**

Adds additional cache sources to be used when `--use-inline-cache` is enabled. For more information see the [remote caching guide](https://docs.earthly.dev/docs/remote-caching).

**`--cache-hint`**

Instructs Earthly that the current target should be included as part of the explicit cache. For more information see the [remote caching guide](https://docs.earthly.dev/docs/remote-caching).

## BUILD

#### Synopsis

* `BUILD [--platform <platform>] [--allow-privileged] <target-ref> [--<build-arg-name>=<build-arg-value>...]`

#### Description

The command `BUILD` instructs Earthly to additionally invoke the build of the target referenced by `<target-ref>`, where `<target-ref>` follows the rules defined by [target referencing](https://docs.earthly.dev/guides/target-ref#target-reference). The invocation will mark any images, or artifacts saved by the referenced target for local output (assuming local output is enabled), and any push commands issued by the referenced target for pushing (assuming pushing is enabled).

{% hint style="info" %}
**What is being output and pushed**

In Earthly v0.6+, what is being output and pushed is determined either by the main target being invoked on the command-line directly, or by targets directly connected to it via a chain of `BUILD` calls. Other ways to reference a target, such as `FROM`, `COPY`, `WITH DOCKER --load` etc, do not contribute to the final set of outputs or pushes.

If you are referencing a target via some other command, such as `COPY` and you would like for the outputs or pushes to be included, you can issue an equivalent `BUILD` command in addition to the `COPY`. For example

```Dockerfile
my-target:
    COPY --platform=linux/amd64 (+some-target/some-file.txt --FOO=bar) ./
```

Should be amended with the following additional `BUILD` call:

```Dockerfile
my-target:
    BUILD --platform=linux/amd64 +some-target --FOO=bar
    COPY --platform=linux/amd64 (+some-target/some-file.txt --FOO=bar) ./
```

This, however, assumes that the target `+my-target` is itself connected via a `BUILD` chain to the main target being built. If that is not the case, additional `BUILD` commands should be issued higher up the hierarchy.
{% endhint %}

#### Options

**`--<build-arg-key>=<build-arg-value>`**

Sets a value override of `<build-arg-value>` for the build arg identified by `<build-arg-key>`.

The override value of a build arg may be a constant string

```
--SOME_ARG="a constant value"
```

or an expression involving other build args

```
--SOME_ARG="a value based on other args, like $ANOTHER_ARG and $YET_ANOTHER_ARG"
```

or a dynamic expression, based on the output of a command executed in the context of the build environment.

```
--SOME_ARG=$(find /app -type f -name '*.php')
```

Dynamic expressions are delimited by `$(...)`.

**`--platform <platform>`**

Specifies the platform to build on.

This flag may be repeated in order to instruct the system to perform the build for multiple platforms. For example

```Dockerfile
build-all-platforms:
    BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build
```

For more information see the [multi-platform guide](https://docs.earthly.dev/docs/guides/multi-platform).

**`--allow-privileged`**

Same as [`FROM --allow-privileged`](#allow-privileged).

**`--build-arg <build-arg-key>=<build-arg-value>` (deprecated)**

This option is deprecated. Please use `--<build-arg-key>=<build-arg-value>` instead.

## VERSION

#### Synopsis

* `VERSION [options...] <version-number>`

#### Description

The command `VERSION` identifies which set of features to enable in Earthly while handling the corresponding Earthfile. The `VERSION` command is currently optional; however will become mandatory in a future version of Earthly. When specified, `VERSION` must be the first command in the Earthfile.

| Version number | enabled features                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------- |
| `0.5`          | *initial functionality will be preserved*                                                                           |
| `0.6`          | `--use-copy-include-patterns --referenced-save-only --for-in --require-force-for-unsafe-saves --no-implicit-ignore` |

#### Options

Individual features may be enabled by setting the corresponding feature flag. New features start off as experimental, which is why they are disabled by default. Once a feature reaches maturity, it will be enabled by default under a new version number.

All features are described in [the version-specific features reference](https://docs.earthly.dev/docs/earthfile/features).

## GIT CLONE

#### Synopsis

* `GIT CLONE [--branch <git-ref>] [--keep-ts] <git-url> <dest-path>`

#### Description

The command `GIT CLONE` clones a git repository from `<git-url>`, optionally referenced by `<git-ref>`, into the build environment, within the `<dest-path>`.

In contrast to an operation like `RUN git clone <git-url> <dest-path>`, the command `GIT CLONE` is cache-aware and correctly distinguishes between different git commit IDs when deciding to reuse a previous cache or not. In addition, `GIT CLONE` can also use [Git authentication configuration](https://docs.earthly.dev/docs/guides/auth) passed on to `earthly`, whereas `RUN git clone` would require additional secrets passing, if the repository is not publicly accessible.

#### Options

**`--branch <git-ref>`**

Points the `HEAD` to the git reference specified by `<git-ref>`. If this option is not specified, then the remote `HEAD` is used instead.

**`--keep-ts`**

Instructs Earthly to not overwrite the file creation timestamps with a constant.

## FROM DOCKERFILE

#### Synopsis

* `FROM DOCKERFILE [options...] <context-path>`

#### Description

The `FROM DOCKERFILE` command initializes a new build environment, inheriting from an existing Dockerfile. This allows the use of Dockerfiles in Earthly builds.

The `<context-path>` is the path where the Dockerfile build context exists. By default, it is assumed that a file named `Dockerfile` exists in that directory. The context path can be either a path on the host system, or an [artifact reference](https://docs.earthly.dev/guides/target-ref#artifact-reference), pointing to a directory containing a `Dockerfile`.

#### Options

**`-f <dockerfile-path>`**

Specify an alternative Dockerfile to use. The `<dockerfile-path>` can be either a path on the host system, relative to the current Earthfile, or an [artifact reference](https://docs.earthly.dev/guides/target-ref#artifact-reference) pointing to a Dockerfile.

{% hint style="info" %}
It is possible to split the `Dockerfile` and the build context across two separate [artifact references](https://docs.earthly.dev/guides/target-ref#artifact-reference):

```Dockerfile
FROM alpine

mybuildcontext:
    WORKDIR /mydata
    RUN echo mydata > myfile
    SAVE ARTIFACT /mydata

mydockerfile:
    RUN echo "
FROM busybox
COPY myfile .
RUN cat myfile" > Dockerfile
    SAVE ARTIFACT Dockerfile

docker:
    FROM DOCKERFILE -f +mydockerfile/Dockerfile +mybuildcontext/mydata/*
    SAVE IMAGE testimg:latest
```

Note that `+mybuildcontext/mydata` on its own would copy the directory *and* its contents; where as `+mybuildcontext/mydata/*` is required to copy all of the contents from within the `mydata` directory ( without copying the wrapping `mydata` directory).

If both the `Dockerfile` and build context are inside the same target, one must reference the same target twice, e.g. `FROM DOCKERFILE -f +target/dir/Dockerfile +target/dir`.
{% endhint %}

**`--build-arg <key>=<value>`**

Sets a value override of `<value>` for the Dockerfile build arg identified by `<key>`. This option is similar to the `docker build --build-arg <key>=<value>` option.

**`--target <target-name>`**

In a multi-stage Dockerfile, sets the target to be used for the build. This option is similar to the `docker build --target <target-name>` option.

**`--platform <platform>`**

Specifies the platform to build on.

For more information see the [multi-platform guide](https://docs.earthly.dev/docs/guides/multi-platform).

## WITH DOCKER

#### Synopsis

```Dockerfile
WITH DOCKER [--pull <image-name>] [--load <image-name>=<target-ref>] [--compose <compose-file>]
            [--service <compose-service>] [--allow-privileged]
  <commands>
  ...
END
```

#### Description

The clause `WITH DOCKER` initializes a Docker daemon to be used in the context of a `RUN` command. The Docker daemon can be pre-loaded with a set of images using options such as `-pull` and `--load`. Once the execution of the `RUN` command has completed, the Docker daemon is stopped and all of its data is deleted, including any volumes and network configuration. Any other files that may have been created are kept, however.

The clause `WITH DOCKER` automatically implies the `RUN --privileged` flag.

The `WITH DOCKER` clause only supports the command [`RUN`](#run). Other commands (such as `COPY`) need to be run either before or after `WITH DOCKER ... END`. In addition, only one `RUN` command is permitted within `WITH DOCKER`. However, multiple shell commands may be stringed together using `;` or `&&`.

A typical example of a `WITH DOCKER` clause might be:

```Dockerfile
FROM earthly/dind:alpine
WORKDIR /test
COPY docker-compose.yml ./
WITH DOCKER \
        --compose docker-compose.yml \
        --load image-name:latest=(+some-target --SOME_BUILD_ARG=value) \
        --load another-image-name:latest=+another-target \
        --pull some-image:latest
    RUN docker run ... && \
        docker run ... && \
        ...
END
```

For more examples, see the [Docker in Earthly guide](https://docs.earthly.dev/docs/guides/docker-in-earthly) and the [Integration testing guide](https://docs.earthly.dev/docs/guides/integration).

For information on using `WITH DOCKER` with podman see the [Podman guide](https://docs.earthly.dev/docs/guides/podman)

{% hint style="info" %}
**Note**

For performance reasons, it is recommended to use a Docker image that already contains `dockerd`. If `dockerd` is not found, Earthly will attempt to install it.

Earthly provides officially supported images such as `earthly/dind:alpine` and `earthly/dind:ubuntu` to be used together with `WITH DOCKER`.
{% endhint %}

#### Options

**`--pull <image-name>`**

Pulls the Docker image `<image-name>` from a remote registry and then loads it into the temporary Docker daemon created by `WITH DOCKER`.

This option may be repeated in order to provide multiple images to be pulled.

{% hint style="info" %}
**Note**

It is recommended that you avoid issuing `RUN docker pull ...` and use `WITH DOCKER --pull ...` instead. The classical `docker pull` command does not take into account Earthly caching and so it would redownload the image much more frequently than necessary.
{% endhint %}

**`--load <image-name>=<target-ref>`**

Builds the image referenced by `<target-ref>` and then loads it into the temporary Docker daemon created by `WITH DOCKER`. The image can be referenced as `<image-name>` within `WITH DOCKER`.

`<target-ref>` may be a simple target reference (`+some-target`), or a target reference with a build arg `(+some-target --SOME_BUILD_ARG=value)`.

This option may be repeated in order to provide multiple images to be loaded.

The `WITH DOCKER --load` option does not mark any saved images or artifacts of the referenced target for local output, nor does it mark any push commands of the referenced target for pushing. For that, please use [`BUILD`](#build).

**`--compose <compose-file>`**

Loads the compose definition defined in `<compose-file>`, adds all applicable images to the pull list and starts up all applicable compose services within.

This option may be repeated, thus having the same effect as repeating the `-f` flag in the `docker-compose` command.

**`--service <compose-service>`**

Specifies which compose service to pull and start up. If no services are specified and `--compose` is used, then all services are pulled and started up.

This option can only be used if `--compose` has been specified.

This option may be repeated in order to specify multiple services.

**`--platform <platform>`**

Specifies the platform for any referenced `--load` and `--pull` images.

For more information see the [multi-platform guide](https://docs.earthly.dev/docs/guides/multi-platform).

**`--allow-privileged`**

Same as [`FROM --allow-privileged`](#allow-privileged).

**`--build-arg <key>=<value>` (deprecated)**

This option is deprecated. Please use `--load <image-name>=(<target-ref> --<build-arg-key>=<build-arg-value>)` instead.

## IF

#### Synopsis

* ```
  IF [<condition-options>...] <condition>
    <if-block>
  END
  ```

* ```
  IF [<condition-options>...] <condition>
    <if-block>
  ELSE
    <else-block>
  END
  ```

* ```
  IF [<condition-options>...] <condition>
    <if-block>
  ELSE IF [<condition-options>...] <condition>
    <else-if-block>
  ...
  ELSE
    <else-block>
  END
  ```

#### Description

The `IF` clause can perform varying commands depending on the outcome of one or more conditions. The expression passed as part of `<condition>` is evaluated by running it in the build environment. If the exit code of the expression is zero, then the block of that condition is executed. Otherwise, the control continues to the next `ELSE IF` condition (if any), or if no condition returns a non-zero exit code, the control continues to executing the `<else-block>`, if one is provided.

A very common pattern is to use the POSIX shell `[ ... ]` conditions. For example the following marks port `8080` as exposed if the file `./foo` exists.

```Dockerfile
IF [ -f ./foo ]
  EXPOSE 8080
END
```

{% hint style="info" %}
**Note**

Performing a condition requires that a `FROM` (or a from-like command, such as `LOCALLY`) has been issued before the condition itself.

For example, the following is NOT a valid Earthfile.

```Dockerfile
# NOT A VALID EARTHFILE.
ARG base=alpine
IF [ "$base" = "alpine" ]
    FROM alpine:3.15
ELSE
    FROM ubuntu:20.04
END
```

The reason this is invalid is because the `IF` condition is actually running the `/usr/bin/[` executable to test if the condition is true or false, and therefore requires that a valid build environment has been initialized.

Here is how this might be fixed.

```Dockerfile
ARG base=alpine
FROM busybox
IF [ "$base" = "alpine" ]
    FROM alpine:3.15
ELSE
    FROM ubuntu:20.04
END
```

By initializing the build environment with `FROM busybox`, the `IF` condition can execute on top of the `busybox` image.
{% endhint %}

{% hint style="danger" %}
**Important**

Changes to the filesystem in any of the conditions are not preserved. If a file is created as part of a condition, then that file will not be present in the build environment for any subsequent commands.
{% endhint %}

#### Options

**`--privileged`**

Same as [`RUN --privileged`](#privileged).

**`--ssh`**

Same as [`RUN --ssh`](#ssh).

**`--no-cache`**

Same as [`RUN --no-cache`](#no-cache).

**`--mount <mount-spec>`**

Same as [`RUN --mount <mount-spec>`](#mount-less-than-mount-spec-greater-than).

**`--secret <env-var>=<secret-ref>`**

Same as [`RUN --secret <env-var>=<secret-ref>`](#secret-less-than-env-var-greater-than-less-than-secret-ref-greater-than).

## FOR

Enable via `VERSION 0.6`.

#### Synopsis

* ```
  FOR [<options>...] <variable-name> IN <expression>
    <for-block>
  END
  ```

#### Description

The `FOR` clause can iterate over the items resulting from the expression `<expression>`. On each iteration, the value of `<variable-name>` is set to the current item in the iteration and the block of commands `<for-block>` is executed in the context of that variable set as a build arg.

The expression may be either a constant list of items (e.g. `foo bar buz`), or the output of a command (e.g. `$(echo foo bar buz)`), or a parameterized list of items (e.g. `foo $BARBUZ`). The result of the expression is then tokenized using the list of separators provided via the `--sep` option. If unspecified, the separator list defaults to `[tab]`, `[new line]` and `[space]` (`\t\n` ).

{% hint style="danger" %}
**Important**

Changes to the filesystem in expressions are not preserved. If a file is created as part of a `FOR` expression, then that file will not be present in the build environment for any subsequent commands.
{% endhint %}

#### Examples

As an example, `FOR` may be used to iterate over a list of files for compilation

```Dockerfile
FOR file IN $(ls)
  RUN gcc "${file}" -o "${file}.o" -c
END
```

As another example, `FOR` may be used to iterate over a set of directories in a monorepo and invoking targets within them.

```Dockerfile
FOR dir IN $(ls -d */)
  BUILD "./$dir+build"
END
```

#### Options

**`--sep <separator-list>`**

The list of separators to use when tokenizing the output of the expression. If unspecified, the separator list defaults to `[tab]`, `[new line]` and `[space]` (`\t\n` ).

**`--privileged`**

Same as [`RUN --privileged`](#privileged).

**`--ssh`**

Same as [`RUN --ssh`](#ssh).

**`--no-cache`**

Same as [`RUN --no-cache`](#no-cache).

**`--mount <mount-spec>`**

Same as [`RUN --mount <mount-spec>`](#mount-less-than-mount-spec-greater-than).

**`--secret <env-var>=<secret-ref>`**

Same as [`RUN --secret <env-var>=<secret-ref>`](#secret-less-than-env-var-greater-than-less-than-secret-ref-greater-than).

## WAIT (experimental)

{% hint style="info" %}
**Note**

The `WAIT` command is experimental and must be enabled via `VERSION --wait-block 0.6`.
{% endhint %}

#### Synopsis

* ```
  WAIT
    <wait-block>
  END
  ```

#### Description

The `WAIT` clause executes the encapsulated commands and waits for them to complete. This includes pushing and outputting local artifacts -- a feature which can be used to control the order of interactions with the outside world.

Even though the `WAIT` clause limits parallelism by forcing everything within it to finish executing before continuing, the commands **within** a `WAIT` block execute in parallel.

#### Examples

As an example, multiple `WAIT` blocks can be used; the first block builds and pushes to a remote registry (in parallel), then a second `WAIT` block can be used to execute a script which requires those images to exist in the remote registry:

```Dockerfile
myimage:
  ...
  SAVE IMAGE --push user/img:tag

myotherimage:
  ...
  SAVE IMAGE --push user/otherimg:tag

WAIT
  BUILD +myimg
  BUILD +myotherimg
END
WAIT
  RUN --push ./deploy ...
END
```

One can also use a `WAIT` block to control the order in which a `SAVE ARTIFACT ... AS LOCAL` command is executed:

```Dockerfile
RUN ./generate > data
WAIT
  SAVE ARTIFACT data AS LOCAL output/data
END
RUN ./test data # even if this fails, data will have been output
```

## CACHE (beta)

{% hint style="info" %}
**Note**

The `CACHE` command is in beta and must be enabled via `VERSION --use-cache-command 0.6`.
{% endhint %}

#### Synopsis

* ```
  CACHE [--sharing <sharing-mode>] <mountpoint>
  ```

#### Description

The `CACHE` command creates a cache mountpoint at `<mountpoint>` in the build environment. The cache mountpoint is a directory which is shared between the instances of the same build target. The contents of the cache mountpoint are preserved between builds, and can be used to share data across builds.

At the end of the target, the contents of the cache mountpoint are persisted as an additional layer in the image. This means that the contents are available to subsequent targets in the same build using `FROM`, or to any saved images `SAVE IMAGE`.

#### Options

**`--sharing <sharing-mode>`**

The sharing mode for the cache mount, from one of the following:

* `locked` (default) - the cache mount is locked for the duration of the execution, other concurrent builds will wait for the lock to be released.
* `shared` - the cache mount is shared between all concurrent builds.
* `private` - if another concurrent build attempts to use the cache, a new (empty) cache will be created for the concurrent build.

## LOCALLY

#### Synopsis

* `LOCALLY`

#### Description

The `LOCALLY` command can be used in place of a `FROM` command, which will cause earthly to execute all commands under the target directly on the host system, rather than inside a container. Commands within a `LOCALLY` target will never be cached. This feature should be used with caution as locally run commands have no guarantee they will behave the same on different systems.

Only `RUN` commands are supported under a `LOCALLY` defined target; furthermore only `RUN`'s `--push` flag is supported.

`RUN` commands have access to the environment variables which are exposed to the `earthly` command; however, the commands are executed within a working directory which is set to the location of the referenced Earthfile and not where the `earthly` command is run from.

For example, the following Earthfile will display the current user, hostname, and directory where the Earthfile is stored:

```Dockerfile
whoami:
    LOCALLY
    RUN echo "I am currently running under $USER on $(hostname) under $(pwd)"
```

{% hint style="info" %}
**Note**

In Earthly, outputting images and artifacts locally takes place only at the end of a successful build. In order to use such images or artifacts in `LOCALLY` targets, they need to be referenced correctly.

For images, use the `--load` option under `WITH DOCKER`:

```Dockerfile
my-image:
    FROM alpine 3.13
    ...
    SAVE IMAGE my-example-image

a-locally-example:
    LOCALLY
    WITH DOCKER --load=+my-image
        RUN docker run --rm my-example-image
    END
```

Do NOT use `BUILD` for using images in `LOCALLY` targets:

```Dockerfile
# INCORRECT - do not use!
my-image:
    FROM alpine 3.13
    ...
    SAVE IMAGE my-example-image

a-locally-example:
    LOCALLY
    BUILD +my-image
    # The image will not be available here because the local export of the
    # image only takes place at the end of an entire successful build.
    RUN docker run --rm my-example-image
```

For artifacts, use `COPY`, the same way you would in a regular target:

```Dockerfile
my-artifact:
    FROM alpine 3.13
    ...
    SAVE ARTIFACT ./my-example-artifact

a-locally-example:
    LOCALLY
    COPY +my-artifact/my-example-artifact ./
    RUN cat ./my-example-artifact
```

Do NOT use `SAVE ARTIFACT ... AS LOCAL` and `BUILD` for referencing artifacts in `LOCALLY` targets:

```Dockerfile
# INCORRECT - do not use!
my-artifact:
    FROM alpine 3.13
    ...
    SAVE ARTIFACT ./my-example-artifact AS LOCAL ./my-example-artifact

a-locally-example:
    LOCALLY
    BUILD +my-artifact
    # The artifact will not be available here because the local export of the
    # artifact only takes place at the end of an entire successful build.
    RUN cat ./my-example-artifact
```

{% endhint %}

## COMMAND

#### Synopsis

* `COMMAND`

#### Description

The command `COMMAND` marks the beginning of a user-defined command (UDC) definition. UDCs are templates (much like functions in regular programming languages), which can be used to define a series of steps to be executed in sequence. In order to reference and execute a UDC, you may use the command [`DO`](#do).

Unlike performing a `BUILD +target`, UDCs inherit the build context and the build environment from the caller.

UDCs create their own `ARG` scope, which is distinct from the caller. Any `ARG` that needs to be passed from the caller needs to be passed explicitly via `DO +COMMAND --<build-arg-key>=<build-arg-value>`.

Global imports and global args are inherited from the `base` target of the same Earthfile where the command is defined in (this may be distinct from the `base` target of the caller).

For more information see the [User-defined commands guide](https://docs.earthly.dev/docs/guides/udc).

## DO

#### Synopsis

* `DO [--allow-privileged] <command-ref> [--<build-arg-key>=<build-arg-value>...]`

#### Description

The command `DO` expands and executes the series of commands contained within a user-defined command (UDC) [referenced by `<command-ref>`](https://docs.earthly.dev/guides/target-ref#command-reference).

Unlike performing a `BUILD +target`, UDCs inherit the build context and the build environment from the caller.

UDCs create their own `ARG` scope, which is distinct from the caller. Any `ARG` that needs to be passed from the caller needs to be passed explicitly via `DO +COMMAND --<build-arg-key>=<build-arg-value>`.

For more information see the [User-defined commands guide](https://docs.earthly.dev/docs/guides/udc).

#### Options

**`--allow-privileged`**

Same as [`FROM --allow-privileged`](#allow-privileged).

## IMPORT

#### Synopsis

* `IMPORT [--allow-privileged] <project-ref> [AS <alias>]`

#### Description

The command `IMPORT` aliases a project reference (`<project-ref>`) that can be used in subsequent [target, artifact or command references](https://docs.earthly.dev/docs/guides/target-ref).

If not provided, the `<alias>` is inferred automatically as the last element of the path provided in `<project-ref>`. For example, if `<project-ref>` is `github.com/foo/bar/buz:v1.2.3`, then the alias is inferred as `buz`.

The `<project-ref>` can be a reference to any directory other than `.`. If the reference ends in `..`, then mentioning `AS <alias>` is mandatory.

If an `IMPORT` is defined in the `base` target of the Earthfile, then it becomes a global `IMPORT` and it is made available to every other target or command in that file, regardless of their base images used.

For more information see the [target, artifact and command references guide](https://docs.earthly.dev/docs/guides/target-ref).

#### Options

**`--allow-privileged`**

Similar to [`FROM --allow-privileged`](#allow-privileged), extend the ability to request privileged capabilities to all invocations of the imported alias.

## CMD (same as Dockerfile CMD)

#### Synopsis

* `CMD ["executable", "arg1", "arg2"]` (exec form)
* `CMD ["arg1, "arg2"]` (as default arguments to the entrypoint)
* `CMD command arg1 arg2` (shell form)

#### Description

The command `CMD` sets default arguments for an image, when executing as a container. It works the same way as the [Dockerfile `CMD` command](https://docs.docker.com/engine/reference/builder/#cmd).

## LABEL (same as Dockerfile LABEL)

#### Synopsis

* `LABEL <key>=<value> <key>=<value> ...`

#### Description

The `LABEL` command adds label metadata to an image. It works the same way as the [Dockerfile `LABEL` command](https://docs.docker.com/engine/reference/builder/#label).

## EXPOSE (same as Dockerfile EXPOSE)

#### Synopsis

* `EXPOSE <port> <port> ...`
* `EXPOSE <port>/<protocol> <port>/<protocol> ...`

#### Description

The `EXPOSE` command marks a series of ports as listening ports within the image. It works the same way as the [Dockerfile `EXPOSE` command](https://docs.docker.com/engine/reference/builder/#expose).

## ENV (same as Dockerfile ENV)

#### Synopsis

* `ENV <key> <value>`
* `ENV <key>=<value>`

#### Description

The `ENV` command sets the environment variable `<key>` to the value `<value>`. It works the same way as the [Dockerfile `ENV` command](https://docs.docker.com/engine/reference/builder/#env).

{% hint style="info" %}
**Note**

Do not use the `ENV` command for secrets used during the build. All `ENV` values used during the build are persisted within the image itself. See the [`RUN --secret` option](#run) to pass secrets to build instructions.
{% endhint %}

## ENTRYPOINT (same as Dockerfile ENTRYPOINT)

#### Synopsis

* `ENTRYPOINT ["executable", "arg1", "arg2"]` (exec form)
* `ENTRYPOINT command arg1 arg2` (shell form)

#### Description

The `ENTRYPOINT` command sets the default command or executable to be run when the image is executed as a container. It works the same way as the [Dockerfile `ENTRYPOINT` command](https://docs.docker.com/engine/reference/builder/#entrypoint).

## VOLUME (same as Dockerfile VOLUME)

#### Synopsis

* `VOLUME <path-to-target-mount> <path-to-target-mount> ...`
* `VOLUME ["<path-to-target-mount>", <path-to-target-mount> ...]`

#### Description

The `VOLUME` command creates a mount point at the specified path and marks it as holding externally mounted volumes. It works the same way as the [Dockerfile `VOLUME` command](https://docs.docker.com/engine/reference/builder/#volume).

## USER (same as Dockerfile USER)

#### Synopsis

* `USER <user>[:<group>]`
* `USER <UID>[:<GID>]`

#### Description

The `USER` command sets the user name (or UID) and optionally the user group (or GID) to use when running the image and also for any subsequent instructions in the build recipe. It works the same way as the [Dockerfile `USER` command](https://docs.docker.com/engine/reference/builder/#user).

## WORKDIR (same as Dockerfile WORKDIR)

#### Synopsis

* `WORKDIR <path-to-dir>`

#### Description

The `WORKDIR` command sets the working directory for following commands in the recipe. The working directory is also persisted as the default directory for the image. If the directory does not exist, it is automatically created. This command works the same way as the [Dockerfile `WORKDIR` command](https://docs.docker.com/engine/reference/builder/#workdir).

## HEALTHCHECK (same as Dockerfile HEALTHCHECK)

#### Synopsis

* `HEALTHCHECK NONE` (disable health checking)
* `HEALTHCHECK [--interval=DURATION] [--timeout=DURATION] [--start-period=DURATION] [--retries=N] CMD command arg1 arg2` (check container health by running command inside the container)

#### Description

The `HEALTHCHECK` command tells Docker how to test a container to check that it is still working. It works the same way as the [Dockerfile `HEALTHCHECK` command](https://docs.docker.com/engine/reference/builder/#healthcheck), with the only exception that the exec form of this command is not yet supported.

#### Options

**`--interval=DURATION`**

Sets the time interval between health checks. Defaults to `30s`.

**`--timeout=DURATION`**

Sets the timeout for a single run before it is considered as failed. Defaults to `30s`.

**`--start-period=DURATION`**

Sets an initialization time period in which failures are not counted towards the maximum number of retries. Defaults to `0s`.

**`--retries=N`**

Sets the number of retries before a container is considered `unhealthy`. Defaults to `3`.

## HOST (experimental)

{% hint style="info" %}
**Note**

The `HOST` command is experimental and must be enabled by enabling the `--use-host-command` flag, e.g.

```Dockerfile
VERSION --use-host-command 0.6
```

{% endhint %}

#### Synopsis

* `HOST <hostname> <ip>`

#### Description

The `HOST` command creates a hostname entry (under `/etc/hosts`) that causes `<hostname>` to resolve to the specified `<ip>` address.

## SHELL (not supported)

The classical [`SHELL` Dockerfile command](https://docs.docker.com/engine/reference/builder/#shell) is not yet supported. Use the *exec form* of `RUN`, `ENTRYPOINT` and `CMD` instead and prepend a different shell.

## ADD (not supported)

The classical [`ADD` Dockerfile command](https://docs.docker.com/engine/reference/builder/#add) is not yet supported. Use [COPY](#copy) instead.

## ONBUILD (not supported)

The classical [`ONBUILD` Dockerfile command](https://docs.docker.com/engine/reference/builder/#onbuild) is not supported.

## STOPSIGNAL (not supported)

The classical [`STOPSIGNAL` Dockerfile command](https://docs.docker.com/engine/reference/builder/#stopsignal) is not yet supported.

# Builtin args

Builtin args are variables with values automatically filled-in by Earthly.

The value of a builtin arg can never be overridden. However, you can always have an additional `ARG`, which takes as the default value, the value of the builtin arg. The additional arg can be overridden. Example

```Dockerfile
ARG EARTHLY_TARGET_TAG
ARG TAG=$EARTHLY_TARGET_TAG
SAVE IMAGE --push some/name:$TAG
```

{% hint style="danger" %}
**Important**

In contrast to Dockerfile predefined args, Earthly builtin args need to be pre-declared before they can be used. For example

```Dockerfile
ARG EARTHLY_TARGET
RUN echo "The current target is $EARTHLY_TARGET"
```

{% endhint %}

The following builtin args are available

| Name                                  | Description                                                                                                                                                                                                                                                      | Example value                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EARTHLY_TARGET`                      | The canonical reference of the current target.                                                                                                                                                                                                                   | For example, for a target named `foo`, which exists on `john/work` branch, in a repository at `github.com/bar/buz`, in a subdirectory `src`, the canonical reference would be `github.com/bar/buz/src:john/work+foo`. For more information about canonical references, see [target referencing](https://docs.earthly.dev/docs/guides/target-ref). |
| `EARTHLY_TARGET_PROJECT`              | The project part of the canonical reference of the current target.                                                                                                                                                                                               | For the example above, the canonical project would be `github.com/bar/buz/src:john`                                                                                                                                                                                                                                                               |
| `EARTHLY_TARGET_PROJECT_NO_TAG`       | The project part of the canonical reference of the current target, but without the tag.                                                                                                                                                                          | For the example above, this would be `github.com/bar/buz/src`                                                                                                                                                                                                                                                                                     |
| `EARTHLY_TARGET_NAME`                 | The name part of the canonical reference of the current target.                                                                                                                                                                                                  | For the example above, the name would be `foo`                                                                                                                                                                                                                                                                                                    |
| `EARTHLY_TARGET_TAG`                  | The tag part of the canonical reference of the current target. Note that if the target has no [canonical form](https://docs.earthly.dev/guides/target-ref#canonical-form), the value is an empty string.                                                         | For the example above, the tag would be `john/work`                                                                                                                                                                                                                                                                                               |
| `EARTHLY_TARGET_TAG_DOCKER`           | The tag part of the canonical reference of the current target, sanitized for safe use as a docker tag. This is guaranteed to be a valid docker tag, even if no canonical form exists, in which case, `latest` is used.                                           | For the example above, the docker tag would be `john_work`                                                                                                                                                                                                                                                                                        |
| `EARTHLY_GIT_HASH`                    | The git hash detected within the build context directory. If no git directory is detected, then the value is an empty string. Take care when using this arg, as the frequently changing git hash may be cause for not using the cache.                           | `41cb5666ade67b29e42bef121144456d3977a67a`                                                                                                                                                                                                                                                                                                        |
| `EARTHLY_GIT_SHORT_HASH`              | The first 8 characters of the git hash detected within the build context directory. If no git directory is detected, then the value is an empty string. Take care when using this arg, as the frequently changing git hash may be cause for not using the cache. | `41cb5666`                                                                                                                                                                                                                                                                                                                                        |
| `EARTHLY_GIT_ORIGIN_URL`              | The git URL detected within the build context directory. If no git directory is detected, then the value is an empty string. Please note that this may be inconsistent, depending on whether an HTTPS or SSH URL was used.                                       | `git@github.com:bar/buz.git` or `https://github.com/bar/buz.git`                                                                                                                                                                                                                                                                                  |
| `EARTHLY_GIT_PROJECT_NAME`            | The git project name from within the git URL detected within the build context directory. If no git directory is detected, then the value is an empty string.                                                                                                    | `bar/buz`                                                                                                                                                                                                                                                                                                                                         |
| `EARTHLY_GIT_COMMIT_TIMESTAMP`        | The committer timestamp, as unix seconds, of the git commit detected within the build context directory. If no git directory is detected, then the value is an empty string.                                                                                     | `1626881847`                                                                                                                                                                                                                                                                                                                                      |
| `EARTHLY_GIT_COMMIT_AUTHOR_TIMESTAMP` | The author timestamp, as unix seconds, of the git commit detected within the build context directory. If no git directory is detected, then the value is an empty string.                                                                                        | `1626881847`                                                                                                                                                                                                                                                                                                                                      |
| `EARTHLY_VERSION` \*                  | The version of Earthly currently running.                                                                                                                                                                                                                        | `v0.6.2`                                                                                                                                                                                                                                                                                                                                          |
| `EARTHLY_BUILD_SHA` \*                | The git hash of the commit which built the currently running version of Earthly.                                                                                                                                                                                 | `1a9eda7a83af0e2ec122720e93ff6dbe9231fc0c`                                                                                                                                                                                                                                                                                                        |
| `TARGETPLATFORM`                      | The target platform the target is being built for.                                                                                                                                                                                                               | `linux/arm/v7`, `linux/amd64`, `linux/arm64`                                                                                                                                                                                                                                                                                                      |
| `TARGETOS`                            | The target OS the target is being built for.                                                                                                                                                                                                                     | `linux`                                                                                                                                                                                                                                                                                                                                           |
| `TARGETARCH`                          | The target processor architecture the target is being built for.                                                                                                                                                                                                 | `arm`, `amd64`, `arm64`                                                                                                                                                                                                                                                                                                                           |
| `TARGETVARIANT`                       | The target processor architecture variant the target is being built for.                                                                                                                                                                                         | `v7`                                                                                                                                                                                                                                                                                                                                              |
| `EARTHLY_SOURCE_DATE_EPOCH`           | The timestamp, as unix seconds, of the git commit detected within the build context directory. If no git directory is detected, then the value is `0` (the unix epoch)                                                                                           | `1626881847`, `0`                                                                                                                                                                                                                                                                                                                                 |
| `USERPLATFORM`                        | The platform the target is being built from.                                                                                                                                                                                                                     | `linux/arm/v7`, `linux/amd64`, `darwin/arm64`                                                                                                                                                                                                                                                                                                     |
| `USEROS`                              | The OS the target is being built from.                                                                                                                                                                                                                           | `linux`, `darwin`                                                                                                                                                                                                                                                                                                                                 |
| `USERARCH`                            | The processor architecture the target is being built from.                                                                                                                                                                                                       | `arm`, `amd64`, `arm64`                                                                                                                                                                                                                                                                                                                           |
| `USERVARIANT`                         | The processor architecture variant the target is being built from.                                                                                                                                                                                               | `v7`                                                                                                                                                                                                                                                                                                                                              |

* requires use of [feature-flag](https://docs.earthly.dev/docs/earthfile/features), for example: `VERSION --earthly-version-arg 0.6`.

{% hint style="info" %}
**Note**

The classical Dockerfile predefined args are currently not available in Earthly.
{% endhint %}

# Excluding patterns

When a build takes place, the `earthly` command sends any necessary local build contexts to the BuildKit daemon. In order to avoid sending unwanted files, you may exclude certain patterns by specifying an `.earthlyignore` file.

The `.earthlyignore` file must be present in the same directory as the target being built.

The syntax of the `.earthlyignore` file is the same as the syntax of a [`.dockerignore` file](https://docs.docker.com/engine/reference/builder/#dockerignore-file). Behind the scenes, the matching is performed using the Go [`filepath.Match`](https://golang.org/pkg/path/filepath/#Match) function.

Patterns of files to exclude from the build context are specified as one pattern per line, with empty lines or lines starting with `#` being ignored. Each pattern has the following syntax:

```
pattern:
 { term }
term:
 '*'         matches any sequence of non-Separator characters
 '?'         matches any single non-Separator character
 '[' [ '^' ] { character-range } ']'
             character class (must be non-empty)
 c           matches character c (c != '*', '?', '\\', '[')
 '\\' c      matches character c

character-range:
 c           matches character c (c != '\\', '-', ']')
 '\\' c      matches character c
 lo '-' hi   matches character c for lo <= c <= hi
```

{% hint style="info" %}
**Note**

Currently `.earthlyignore` is only applied to local targets. If an `.earthlyignore` file is specified within the context of a remote target, it will be silently ignored and exclusions would not take place.
{% endhint %}

# Version-specific features

Earthly makes use of feature flags to release new and experimental features. Some features must be explicitly enabled to use them.

Earthly uses [semantic versioning](http://semver.org/); once a new feature has reached stability, a new major or minor version of Earthly will be released with the feature enabled by default.

## Specifying Version and features

Each Earthfile should list the current earthly version it depends on using the [`VERSION`](https://docs.earthly.dev/docs/earthfile/..#version) command. The `VERSION` command was first introduced under `0.5` and is optional as of `0.6`; however, it will become mandatory in a future version.

```Dockerfile
VERSION [<flags>...] <version-number>
```

### Example

To Future-proof Earthfiles it is recommended to add a `VERSION` command. Consider a case where an Earthfile is developed against earthly `v0.5.23` and makes use of the experimental `FOOBAR` command, the first line of the Earthfile should be:

```Dockerfile
VERSION --foobar 0.5
```

This will ensure that backwards-breaking features that are introduced in a later version will not change how this Earthfile is interpreted.

In a future release (e.g. `0.X`), the `FOOBAR` command **might** be promoted from the *experimental* stage to *stable* stage, at that point, version `0.X` would automatically set the `--foobar` flag to `true`, and the Earthfile could be updated to require version `0.X` (or later), and could be rewritten as `VERSION 0.X`.

## Feature flags

| Feature flag                       | status       | description                                                                                                 |
| ---------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| `--use-copy-include-patterns`      | 0.6          | Speeds up COPY transfers                                                                                    |
| `--referenced-save-only`           | 0.6          | Changes the behavior of SAVE commands in a significant way                                                  |
| `--for-in`                         | 0.6          | Enables support for `FOR ... IN ...` commands                                                               |
| `--require-force-for-unsafe-saves` | 0.6          | Requires `--force` for saving artifacts locally outside the Earthfile's directory                           |
| `--no-implicit-ignore`             | 0.6          | Eliminates implicit `.earthlyignore` entries, such as `Earthfile` and `.tmp-earthly-out`                    |
| `--earthly-version-arg`            | Beta         | Enables builtin ARGs: `EARTHLY_VERSION` and `EARTHLY_BUILD_SHA`                                             |
| `--shell-out-anywhere`             | Experimental | Allows shelling-out in any earthly command (including in the middle of `ARG`)                               |
| `--use-registry-for-with-docker`   | Experimental | Makes use of the embedded BuildKit Docker registry (instead of tar files) for `WITH DOCKER` loads and pulls |

Note that the features flags are disabled by default in Earthly versions lower than the version listed in the "status" column above.

**`--use-copy-include-patterns`**

*Speeds up COPY transfers.*

When enabled, Earthly will only send the files listed for the specific [`COPY`](https://docs.earthly.dev/docs/earthfile/..#copy) command. Without this feature, Earthly sends the entire directory of files excluding files listed in the [`.earthlyignore` file](https://docs.earthly.dev/docs/earthfile/earthlyignore).

**`--referenced-save-only`**

*Changes the behavior of SAVE commands in a significant way*

When enabled, Earthly will output artifacts resulting from `SAVE ARTIFACT ... AS LOCAL ...` and images resulting from `SAVE IMAGE` and also execute `RUN --push` commands only if they are connected to the main target through a chain of `BUILD` commands.

For example, chains like these will produce outputs (and possibly push, if enabled):

* main target -> `SAVE`
* main target -> `BUILD -> SAVE`
* main target -> `BUILD -> BUILD -> SAVE`
* main target -> `BUILD -> BUILD -> BUILD -> SAVE`

While chains like these will NOT produce outputs nor would they push:

* main target -> `FROM -> SAVE`
* main target -> `COPY -> SAVE`
* main target -> `FROM -> BUILD -> SAVE`
* main target -> `BUILD -> FROM -> SAVE`
* main target -> `BUILD -> BUILD -> COPY -> SAVE`

This works the same regardless of whether the targets in the chain are remote or local.

When this feature is **disabled**, Earthly will output artifacts and images regardless of whether they are connected to the main target through a chain of `BUILD` commands, however the outputs will be subject to the following rules:

* All `SAVE ARTIFACT ... AS LOCAL ...`, with local Earthfiles will be output
* `SAVE ARTIFACT ... AS LOCAL ...` produced in remote targets will not be output
* All images with tag names (both local and remote Earthfiles) will be output
* No image will be pushed or `RUN --push` command will be executed if the target is remote

**`--for-in`**

*Enables support for `FOR ... IN ...` commands*

When enabled, Earthly will allow the use of `FOR ... IN ...` commands.

# The earthly command

## earthly

#### Synopsis

* Target form

  ```
  earthly [options...] <target-ref> [build-args...]
  ```

* Artifact form

  ```
  earthly [options...] --artifact|-a <target-ref>/<artifact-path> [<dest-path>]
  earthly [options...] --artifact|-a (<target-ref>/<artifact-path> [build-args...]) [<dest-path>]
  ```

* Image form

  ```
  earthly [options...] --image <target-ref> [build-args...]
  ```

#### Description

The command executes a build referenced by `<target-ref>` (*target form* and *image form*) or `<artifact-ref>` (*artifact form*). In the *target form*, the referenced target and its dependencies are built. In the *artifact form*, the referenced artifact and its dependencies are built, but only the specified artifact is output. The output path of the artifact can be optionally overridden by `<dest-path>`. In the *image form*, the image produced by the referenced target and its dependencies are built, but only the specified image is output.

If a BuildKit daemon has not already been started, and the option `--buildkit-host` is not specified, this command also starts up a container named `earthly-buildkitd` to act as a build daemon.

The execution has four phases:

* Init
* Build
* Push (optional - disabled by default)
* Local output (optional - enabled by default)

During the init phase the configuration is interpreted and the BuildKit daemon is started (if applicable). During the build phase, the referenced target and all its direct or indirect dependencies are executed. During the push phase, when enabled, Earthly performs image pushes and it also runs `RUN --push` commands. During the local output phase, all applicable artifacts with an `AS LOCAL` specification are written to the specified output location, and all applicable docker images are loaded onto the host's docker daemon.

If the build phase does not succeed, no output is produced and no push instruction is executed. In this case, the command exits with a non-zero exit code.

#### Target and Artifact Reference

The `<target-ref>` can reference both local and remote targets.

**Local Reference**

`+<target-name>` will reference a target in the local Earthfile in the current directory.

`<local-path>+<target-name>` will reference a local Earthfile in a different directory as specified by `<local-path>`, which must start with `./`, `../`, or `/`.

**Remote Reference**

`<gitvendor>/<namespace>/<project>/path/in/project[:some-tag]+<target-name>` will access a remote git repository.

**Artifact Reference**

The `<artifact-ref>` can reference artifacts built by targets. `<target-ref>/<artifact-path>` will reference a build target's artifact.

**Examples**

See the [Target, artifact, and image referencing guide](https://docs.earthly.dev/docs/guides/target-ref) for more details and examples.

#### Build args

Synopsis:

* Target form `earthly <target-ref> [--<build-arg-key>=<build-arg-value>...]`
* Artifact form `earthly --artifact (<target-ref>/<artifact-path> [--<build-arg-key>=<build-arg-value>...]) <dest-path>`
* Image form `earthly --image <target-ref> [--<build-arg-key>=<build-arg-value>...]`

Also available as an env var setting: `EARTHLY_BUILD_ARGS="<build-arg-key>=<build-arg-value>,<build-arg-key>=<build-arg-value>,..."`.

Build arg overrides may be specified as part of the Earthly command. The value of the build arg `<build-arg-key>` is set to `<build-arg-value>`.

In the target and image forms the build args are passed after the target reference. For example `earthly +some-target --NAME=john --SPECIES=human`. In the artifact form, the build args are passed immediately after the artifact reference, however they are surrounded by parenthesis, similar to a [`COPY` command](https://docs.earthly.dev/earthfile#copy). For example `earthly --artifact (+some-target/some-artifact --NAME=john --SPECIES=human) ./dest/path/`.

The build arg overrides only apply to the target being called directly and any other target referenced as part of the same Earthfile. Build arg overrides, will not apply to targets referenced from other directories or other repositories.

For more information about build args see the [`ARG` Earthfile command](https://docs.earthly.dev/earthfile#arg).

#### Environment Variables and .env File

As specified under the [options section](#options), all flag options have an environment variable equivalent, which can be used as an alternative.

Furthermore, additional environment variables are also read from a file named `.env`, if one exists in the current directory. The syntax of the `.env` file is of the form

```.env
<NAME_OF_ENV_VAR>=<value>
...
```

as one variable per line, without any surrounding quotes. If quotes are included, they will become part of the value. Lines beginning with `#` are treated as comments. Blank lines are allowed. Here is a simple example:

```.env
# Settings
EARTHLY_ALLOW_PRIVILEGED=true
MY_SETTING=a setting which contains spaces

# Secrets
MY_SECRET=MmQ1MjFlY2UtYzhlNi00YjJkLWI5YTMtNjIzNzJmYjcwOTJk
ANOTHER_SECRET=MjA5YjU2ZTItYmIxOS00MDQ3LWFlNzYtNmQ5NGEyZDFlYTQx
```

{% hint style="info" %}
**Note**

The directory used for loading the `.env` file is the directory where `earthly` is called from and not necessarily the directory where the Earthfile is located in.
{% endhint %}

The additional environment variables specified in the `.env` file are loaded by `earthly` in three distinct ways:

* **Setting options for `earthly` itself** - the settings are loaded if they match the environment variable equivalent of an `earthly` option.
* **Build args** - the settings are passed on to the build and are used to override any [`ARG`](https://docs.earthly.dev/earthfile#arg) declaration.
* **Secrets** - the settings are passed on to the build to be referenced via the [`RUN --secret`](https://docs.earthly.dev/earthfile#secret-less-than-env-var-greater-than-less-than-secret-ref-greater-than) option.

{% hint style="danger" %}
**Important**

The `.env` file is meant for settings which are specific to the local environment the build executes in. These settings may cause inconsistencies in the way the build executes on different systems, leading to builds that are difficult to reproduce. Keep the contents of `.env` files to a minimum to avoid such issues.
{% endhint %}

#### Global Options

**`--config <path>`**

Also available as an env var setting: `EARTHLY_CONFIG=<path>`.

Overrides the earthly [configuration file](https://docs.earthly.dev/docs/earthly-config), defaults to `~/.earthly/config.yml`.

**`--installation-name <name>`**

Also available as an env var setting: `EARTHLY_INSTALLATION_NAME=<name>`.

Overrides the Earthly installation name. The installation name is used for the Buildkit Daemon name, the cache volume name, the configuration directory (`~/.<installation-name>`) and for the ports used by Buildkit. Using multiple installation names on the same system allows Earthly to run as multiple isolated instances, each with its own configuration, cache and daemon. Defaults to `earthly`.

**`--ssh-auth-sock <path-to-sock>`**

Also available as an env var setting: `EARTHLY_SSH_AUTH_SOCK=<path-to-sock>`.

Sets the path to the SSH agent sock, which can be used for SSH authentication. SSH authentication is used by Earthly in order to perform git clone's underneath.

On Linux systems, this setting defaults to the value of the env var $SSH\_AUTH\_SOCK. On most systems, the env var `SSH_AUTH_SOCK` env var is already set if an SSH agent is running.

On Mac systems, this setting defaults to `/run/host-services/ssh-auth.sock` to match recommendation in [the official Docker documentation](https://docs.docker.com/docker-for-mac/osxfs/#ssh-agent-forwarding).

For more information see the [Authentication page](https://docs.earthly.dev/docs/guides/auth).

**`--auth-token <value>`**

Also available as an env var setting: `EARTHLY_TOKEN=<value>`.

Force Earthly account login to authenticate with supplied token.

**`--verbose`**

Also available as an env var setting: `EARTHLY_VERBOSE=1`.

Enables verbose logging.

**`--git-username <git-user>` (deprecated)**

Also available as an env var setting: `GIT_USERNAME=<git-user>`.

This option is now deprecated. Please use the [configuration file](https://docs.earthly.dev/docs/earthly-config) instead.

**`--git-password <git-pass>` (deprecated)**

Also available as an env var setting: `GIT_PASSWORD=<git-pass>`.

This option is now deprecated. Please use the [configuration file](https://docs.earthly.dev/docs/earthly-config) instead.

**`--git-url-instead-of <git-instead-of>` (obsolete)**

Also used to be available as an env var setting: `GIT_URL_INSTEAD_OF=<git-instead-of>`.

This option is now obsolete. By default, `earthly` will automatically switch from ssh to HTTPS when no keys are found or the ssh-agent isn't running. Please use the [configuration file](https://docs.earthly.dev/docs/earthly-config) to override the default behavior.

#### Build Options

Build options are specific to executing Earthly builds; they are simply listed in this section for readability, and can be supplied as global options.

**`--secret|-s <secret-id>[=<value>]`**

Also available as an env var setting: `EARTHLY_SECRETS="<secret-id>=<value>,<secret-id>=<value>,..."`.

Passes a secret with ID `<secret-id>` to the build environments. If `<value>` is not specified, then the value becomes the value of the environment variable with the same name as `<secret-id>`.

The secret can be referenced within Earthfile recipes as `RUN --secret <arbitrary-env-var-name>=+secrets/<secret-id>`. For more information see the [`RUN --secret` Earthfile command](https://docs.earthly.dev/earthfile#run).

**`--secret-file <secret-id>=<path>`**

Also available as an env var setting: `EARTHLY_SECRET_FILES="<secret-id>=<path>,<secret-id>=<path>,..."`.

Loads the contents of a file located at `<path>` into a secret with ID `<secret-id>` for use within the build environments.

The secret can be referenced within Earthfile recipes as `RUN --secret <arbitrary-env-var-name>=+secrets/<secret-id>`. For more information see the [`RUN --secret` Earthfile command](https://docs.earthly.dev/earthfile#run).

**`--push`**

Also available as an env var setting: `EARTHLY_PUSH=true`.

Instructs Earthly to push any docker images declared with the `--push` flag to remote docker registries and to run any `RUN --push` commands. For more information see the [`SAVE IMAGE` Earthfile command](https://docs.earthly.dev/earthfile#save-image) and the [`RUN --push` Earthfile command](https://docs.earthly.dev/earthfile#run).

Pushing only happens during the output phase, and only if the build has succeeded.

**`--no-output`**

Also available as an env var setting: `EARTHLY_NO_OUTPUT=true`.

Instructs Earthly not to output any images or artifacts. This option cannot be used with the *artifact form* or the *image form*.

**`--output`**

Also available as an env var setting: `EARTHLY_OUTPUT=true`.

Allow artifacts or images to be output, even when running under --ci mode.

**`--no-cache`**

Also available as an env var setting: `EARTHLY_NO_CACHE=true`.

Instructs Earthly to ignore any cache when building. It does, however, continue to store new cache formed as part of the build (to be possibly used on future invocations).

**`--allow-privileged|-P`**

Also available as an env var setting: `EARTHLY_ALLOW_PRIVILEGED=true`.

Permits the build to use the --privileged flag in RUN commands. For more information see the [`RUN --privileged` command](https://docs.earthly.dev/earthfile#run).

**`--use-inline-cache`**

Also available as an env var setting: `EARTHLY_USE_INLINE_CACHE=true`

Enables use of inline cache, if available. Any `SAVE IMAGE --push` command is used to inform the system of possible inline cache sources. For more information see the [remote caching guide](https://docs.earthly.dev/docs/remote-caching).

**`--save-inline-cache`**

Also available as an env var setting: `EARTHLY_SAVE_INLINE_CACHE=true`

Enables embedding inline cache in any pushed images. This cache can be used on other systems, if enabled via `--use-inline-cache`. For more information see the [remote caching guide](https://docs.earthly.dev/docs/remote-caching).

**`--remote-cache <image-tag>`**

Also available as an env var setting: `EARTHLY_REMOTE_CACHE=<image-tag>`

Enables use of explicit cache. The provided `<image-tag>` is used for storing and retrieving the cache to/from a Docker registry. Storing explicit cache is only enabled if the option `--push` is also passed in. For more information see the [remote caching guide](https://docs.earthly.dev/docs/remote-caching).

**`--max-remote-cache`**

Also available as an env var setting: `EARTHLY_MAX_REMOTE_CACHE=true`

Enables storing all intermediate layers as part of the explicit cache. Note that this setting is rarely effective due to the excessive upload overhead. For more information see the [remote caching guide](https://docs.earthly.dev/docs/remote-caching).

**`--ci`**

Also available as an env var setting: `EARTHLY_CI=true`

In *target mode*, this option is an alias for

```
--use-inline-cache --save-inline-cache --no-output --strict
```

In *artifact* and *image modes* , this option is an alias for

```
--use-inline-cache --save-inline-cache
```

**`--platform <platform>`**

Also available as an env var setting: `EARTHLY_PLATFORMS=<platform>`.

Sets the platform to build for.

{% hint style="info" %}
**Note**

It is not yet possible to specify multiple platforms through this flag. You may, however, use a wrapping target and a `BUILD` command in your Earthfile:

```Dockerfile
build-all-platforms:
  BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build

build:
  ...
```

{% endhint %}

**`--build-arg <key>[=<value>]` (deprecated)**

This option has been deprecated in favor of the new build arg syntax `earthly <target-ref> --<key>=<value>`.

Also available as an env var setting: `EARTHLY_BUILD_ARGS="<key>=<value>,<key>=<value>,..."`.

Overrides the value of the build arg `<key>`. If `<value>` is not specified, then the value becomes the value of the environment variable with the same name as `<key>`. For more information see the [`ARG` Earthfile command](https://docs.earthly.dev/earthfile#arg).

**`--interactive|-i`**

Also available as an env var setting: `EARTHLY_INTERACTIVE=true`.

Enable interactive debugging mode. By default when a `RUN` command fails, earthly will display the error and exit. If the interactive mode is enabled and an error occurs, an interactive shell is presented which can be used for investigating the error interactively. Due to technical limitations, only a single interactive shell can be used on the system at any given time.

**`--strict`**

Disallow usage of features that may create unrepeatable builds.

#### Log formatting options

These options can only be set via environment variables, and have no command line equivalent.

| Variable                 | Usage                                                                                                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| NO\_COLOR                | `NO_COLOR=1` disables the use of color.                                                                                                                                                                |
| FORCE\_COLOR             | `FORCE_COLOR=1` forces the use of color.                                                                                                                                                               |
| EARTHLY\_TARGET\_PADDING | `EARTHLY_TARGET_PADDING=n` will set the column to the width of `n` characters. If a name is longer than `n`, its path will be truncated and remaining extra length will cause the column to go ragged. |
| EARTHLY\_FULL\_TARGET    | `EARTHLY_FULL_TARGET=1` will always print the full target name, and leave the target name column ragged.                                                                                               |

## earthly prune

#### Synopsis

* Standard form

  ```
  earthly [options] prune [--all|-a]
  ```

* Reset form

  ```
  earthly [options] prune --reset
  ```

#### Description

The command `earthly prune` eliminates Earthly cache. In the *standard form* it issues a prune command to the BuildKit daemon. In the *reset form* it restarts the BuildKit daemon, instructing it to completely delete the cache directory on startup, thus forcing it to start from scratch.

#### Options

**`--all|-a`**

Instructs earthly to issue a "prune all" command to the BuildKit daemon.

**`--reset`**

Restarts the BuildKit daemon and completely resets the cache directory.

## earthly config

#### Synopsis

```
earthly [options] config [key] [value]
```

#### Description

Manipulates values in `~/.earthly/config.yml`. It does its best to preserve existing formatting and comments. `[value]` must be a valid YAML literal for the given `[key]`.

#### Options

**`--help`**

Prints help text, along with some examples.

**`[key] --help`**

Prints help for the specific key, including what it is used for and what kind of value it needs to be.

#### Examples

Set your cache size:

```
config global.cache_size_mb 1234
```

Set additional BuildKit args, using a YAML array:

```
config global.buildkit_additional_args ['userns', '--host']
```

Set a key containing a period:

```
config git."example.com".password hunter2
```

Set up a whole custom git repository for a server called example.com, using a single-line YAML literal:

* which stores git repos under /var/git/repos/name-of-repo.git
* allows access over ssh
* using port 2222
* sets the username to git
* is recognized to earthly as example.com/name-of-repo

```
config git "{example: {pattern: 'example.com/([^/]+)', substitute: 'ssh://git@example.com:2222/var/git/repos/\$1.git', auth: ssh, user: git}}"
```

The above command yields the following config file:

```yaml
git:
    example:
        pattern: example.com/([^/]+)
        substitute: ssh://git@example.com:2222/var/git/repos/$1.git
        auth: ssh
        user: git
```

## earthly account

Contains sub-commands for registering and administration an Earthly account.

#### earthly account register

**Synopsis**

* ```
  earthly account register --email <email>
  earthly account register --email <email> --token <email-verification-token> [--password <password>] [--public-key <public-key>] [--accept-terms-conditions-privacy]
  ```

**Description**

Register for an Earthly account. Registration is done in two steps: first run the register command with only the --email argument, this will then send an email to the supplied email address with a registration token (which is used to verify your email address), second re-run the register command with both the --email and --token arguments to complete the registration process.

#### earthly account login

**Synopsis**

* ```
  earthly [options] account login
  earthly [options] account login --email <email>
  earthly [options] account login --email <email> --password <password>
  earthly [options] account login --token <token>
  ```

**Description**

Login to an existing Earthly account. If no email or token is given, earthly will attempt to login using [registered public keys](https://docs.earthly.dev/docs/misc/public-key-auth).

#### earthly account logout

**Synopsis**

* ```
  earthly [options] account logout
  ```

**Description**

Removes cached login information from `~/.earthly/auth.token`.

#### earthly account list-keys

**Synopsis**

* ```
  earthly account list-keys
  ```

**Description**

Lists all public keys that are authorized to login to the current Earthly account.

#### earthly account add-key

**Synopsis**

* ```
  earthly account add-key [<public-key>]
  ```

**Description**

Authorize a new public key to login to the current Earthly account. If `key` is omitted, an interactive prompt is displayed to select a public key to add.

#### earthly account remove-key

**Synopsis**

* ```
  earthly account remove-key <public-key>
  ```

**Description**

Removes an authorized public key from accessing the current Earthly account.

#### earthly account list-tokens

**Synopsis**

* ```
  earthly account list-tokens
  ```

**Description**

List account tokens associated with Earthly account. A token is useful for environments where the ssh-agent is not accessible (e.g. a CI system).

#### earthly account create-token

**Synopsis**

* ```
  earthly account create-token [--write] [--expiry <expiry>] <token-name>
  ```

**Description**

Creates a new authentication token. A read-only token is created by default, If the `--write` flag is specified the token will have read+write access. The token will expire in 1 year from creation date unless a different date is supplied via the `--expiry` option.

{% hint style="info" %}
It is then possible to `export EARTHLY_TOKEN=...`, which will force earthly to use this token for all authentication (overriding any other currently-logged in sessions).
{% endhint %}

#### earthly account remove-token

**Synopsis**

* ```
  earthly account remove-token <token>
  ```

**Description**

Removes a token from the current Earthly account.

## earthly org

Contains sub-commands for creating and managing Earthly organizations.

#### earthly org create

**Synopsis**

* ```
  earthly org create <org-name>
  ```

**Description**

Create a new organization, which can be used to share secrets between different user accounts.

#### earthly org list

**Synopsis**

* ```
  earthly org list
  ```

**Description**

List all organizations the current account is a member, or administrator of.

#### earthly org list-permissions

**Synopsis**

* ```
  earthly org list-permissions <org-name>
  ```

**Description**

List all accounts and the paths they have permission to access under a particular organization.

#### earthly org invite

**Synopsis**

* ```
  earthly org invite [--write] <org-path> <email> [<email>, ...]
  ```

**Description**

Invites a user into an organization; `<org-path>` can either be a top-level org access by granting permission on `/<org-name>/`, or finer-grained access can be granted to a subpath e.g. `/<org-name>/path/to/share/`. By default users are granted read-only access unless the `--write` flag is given.

#### earthly org revoke

**Synopsis**

* ```
  earthly org revoke <org-path> <email> [<email>, ...]
  ```

**Description**

Revokes a previously invited user from an organization.

## earthly secrets

Contains sub-commands for creating and managing Earthly secrets.

#### earthly secrets set

**Synopsis**

* ```
  earthly secrets set <path> <value>
  earthly secrets set --file <local-path> <path>
  ```

**Description**

Stores a secret in the secrets store

#### earthly secrets get

**Synopsis**

* ```
  earthly secrets get [-n] <path>
  ```

**Description**

Retrieve a secret from the secrets store. If `-n` is given, no newline is printed after the contents of the secret.

#### earthly secrets ls

**Synopsis**

* ```
  earthly secrets ls [<path>]
  ```

**Description**

List secrets the current account has access to.

#### earthly secrets rm

**Synopsis**

* ```
  earthly secrets rm <path>
  ```

**Description**

Removes a secret from the secrets store.

## earthly bootstrap

#### Synopsis

* ```
  earthly bootstrap
  ```

#### Description

Performs initialization tasks needed for `earthly` to function correctly. This command can be re-run to fix broken setups. It is recommended to run this with sudo.

#### Options

**`--no-buildkit`**

Skips setting up the BuildKit container during bootstrapping. If needed, it will also be performed when a build is ran.

**`--with-autocomplete`**

Installs shell autocompletions during bootstrap. Requires `sudo` to install them correctly.

## earthly --help

#### Synopsis

* ```
  earthly --help
  ```

* ```
  earthly <command> --help
  ```

#### Description

Prints help information about earthly.

## earthly --version

#### Synopsis

* ```
  earthly --version
  ```

#### Description

Prints version information about earthly.

# Configuration reference

Global configuration values for earthly can be stored on disk in the configuration file.

By default, earthly reads the configuration file `~/.earthly/config.yml`; however, it can also be overridden with the `--config` command flag option.

## Format

The earthly config file is a [YAML](https://yaml.org/) formatted file that looks like:

```yaml
global:
  cache_size_mb: <cache_size_mb>
git:
    global:
        url_instead_of: <url_instead_of>
    <site>:
        auth: https|ssh
        user: <username>
        password: <password>
    <site2>:
        ...
```

Example:

```yaml
global:
    cache_size_mb: 20000
git:
    global:
        url_instead_of: "git@example.com:=https://localmirror.example.com/"
    github.com:
        auth: https
        user: alice
        password: itsasecret
```

{% hint style="info" %}
**Tip**

To quickly change a configuration item via the `earthly` command, you can use [`earthly config`](https://docs.earthly.dev/earthly-command#earthly-config).

```bash
earthly config <key> <value>
```

For example

```bash
earthly config global.cache_size_mb 20000
```

{% endhint %}

## Global configuration reference

### cache\_size\_mb

Specifies the total size of the BuildKit cache, in MB. The BuildKit daemon uses this setting to configure automatic garbage collection of old cache. Setting this to 0, either explicitly or by omission, will cause buildkit to use its internal default of 10% of the root filesystem.

### cache\_size\_pct

Specifies the total size of the BuildKit cache, as a percentage (0-100) of the total filesystem size. When used in combination with `cache_size_mb`, the lesser of the two values will be used. This limit is ignored when set to 0.

### secret\_provider (experimental)

A custom user-supplied program to call which returns a secret for use by earthly. The secret identifier is passed as the first argument to the program.

If no secret is found, the program can instruct earthly to continue searching for secrets under `.env`, by exiting with a status code of `2`, all other non-zero status codes will cause earthly to exit.

For example, if you have:

```yaml
config:
  secret_provider: my-secret-provider
```

and `my-secret-provider` (which is accessible on your `PATH`):

```bash
#!/bin/sh
set -e

if [ "$1" = "mysecret" ]; then
    echo -n "open sesame"
    exit 0
fi

exit 2
```

Then when earthly encounters a command that requires a secret, such as

```Dockerfile
RUN --secret mysecret echo "the passphrase is $mysecret."
```

earthly will request the secret for `mysecret` by calling `my-secret_provider mysecret`.

{% hint style="info" %}
**Note**

All stdout data will be used as the secret value, including whitespace (and newlines). You may want to use `echo -n` to prevent returning a newline.

Any data sent to stderr will be displayed on the earthly console, this makes it possible to insert commands such as `echo >&2 "here is some debug text"` without affecting the contents of the secret.
{% endhint %}

### disable\_analytics

When set to true, disables collecting command line analytics; otherwise, earthly will report anonymized analytics for invocation of the earthly command. For more information see the [data collection page](https://docs.earthly.dev/docs/misc/data-collection).

### disable\_log\_sharing

When set to true, disables sharing build logs after each build. This setting applies to logged-in users only.

### conversion\_parallelism

The number of concurrent converters for speeding up build targets that use blocking commands like `IF`, `WITH DOCKER --load`, `FROM DOCKERFILE` and others.

### buildkit\_max\_parallelism

The maximum parallelism configured for the buildkit daemon workers. The default is 20.

{% hint style="info" %}
**Note**

Set this configuration to a lower value if your machine is resource constrained and performs poorly when running too many builds in parallel.
{% endhint %}

### buildkit\_additional\_args

This option allows you to pass additional options to Docker when starting up the Earthly BuildKit daemon. For example, this can be used to bypass user namespacing like so:

```yaml
global:
  buildkit_additional_args: ["--userns", "host"]
```

### buildkit\_additional\_config

This option allows you to pass additional options to BuildKit. For example, this can be used to specify additional CA certificates:

```yaml
global:
  buildkit_additional_args: ["-v", "<absolute-path-to-ca-file>:/etc/config/add.ca"]
  buildkit_additional_config: |
    [registry."<registry-hostname>"]
      ca=["/etc/config/add.ca"]
```

### cni\_mtu

Allows overriding Earthly's automatic MTU detection. This is used when configuring the BuildKit internal CNI network. MTU must be between 64 and 65,536.

### ip\_tables

Allows overriding Earthly's automatic `ip_tables` module detection. Valid choices are `iptables-legacy` or `iptables-nft`.

### no\_loop\_device (obsolete)

This option is obsolete and it is ignored. Earthly no longer uses a loop device for its cache.

### cache\_path (obsolete)

This option is obsolete and it is ignored. Earthly cache has moved to a Docker volume. For more information see the [page on managing cache](https://docs.earthly.dev/docs/guides/cache).

### Frontend configuration

This option allows you to specify what supported frontend you are using (Docker / Podman). By default, Earthly will attempt to discover the frontend in this order: Docker -> Podman -> None

For Docker:

```yaml
global:
  container_frontend: docker-shell
```

For Podman:

```yaml
global:
  container_frontend: podman-shell
```

You can use the following command to set the configuration option using the earthly CLI:

```bash
# Docker
earthly config 'global.container_frontend' 'docker-shell'

# Podman
earthly config 'global.container_frontend' 'podman-shell'
```

## Git configuration reference

All git configuration is contained under site-specific options.

### site-specific options

#### site

The git repository hostname. For example `github.com`, or `gitlab.com`

#### auth

Either `ssh`, `https`, or `auto` (default). If `https` is specified, user and password fields are used to authenticate over HTTPS when pulling from git for the corresponding site. If `auto` is specified earthly will use `ssh` when the ssh-agent is running and has at least one key loaded, and will fallback to using `https` when no ssh-keys are present.

See the [Authentication guide](https://docs.earthly.dev/docs/guides/auth) for a guide on setting up authentication.

#### user

The HTTPS username to use when auth is set to `https`. This setting is ignored when auth is `ssh`.

#### password

The HTTPS password to use when auth is set to `https`. This setting is ignored when auth is `ssh`.

#### strict\_host\_key\_checking

The `strict_host_key_checking` option can be used to control access to ssh-based repos whose key is not known or has changed. Strict host key checking is enabled by default, setting it to `false` disables host key checking. This setting is only used when auth is `ssh`.

{% hint style="info" %}
**Tip**

Disabling strict host key checking is a bad security practice (as it makes a man-in-the-middle attack possible). Instead, it's recommended to record the host's ssh key to `~/.ssh/known_hosts`; this can be done by running

```bash
ssh-keyscan <hostname> >> ~/.ssh/known_hosts
```

{% endhint %}

#### port

Connect using a non-standard git port, e.g. `2222`.

#### prefix

The `prefix` option is used to indicate where git repositories are stored on the server, e.g. `/var/git/`.

#### pattern

A regular expression defined to match git URLs, defaults to the `<site>/([^/]+)/([^/]+)`. For example if the site is `github.com`, then the default pattern will match `github.com/<user>/<repo>`.

See the [Authentication guide](https://docs.earthly.dev/docs/guides/auth) for a guide on setting up authentication with self-hosted git repositories.

See the [RE2 docs](https://github.com/google/re2/wiki/Syntax) for a complete definition of the supported regular expression syntax.

#### substitute

If specified, a regular expression substitution will be performed to determine which URL is cloned by git. Values like `$1`, `$2`, ... will be replaced with matched subgroup data. If no substitute is given, a URL will be created based on the requested SSH authentication mode.

See the [Authentication guide](https://docs.earthly.dev/docs/guides/auth) for a guide on setting up authentication with self-hosted git repositories.

# Examples

## Examples of CI integration

Examples of integrating Earthly into various CI systems can be found on the following pages:

* [Circle CI](https://docs.earthly.dev/ci-integration/vendor-specific-guides/circle-integration)
* [GitHub Actions](https://docs.earthly.dev/ci-integration/vendor-specific-guides/gh-actions-integration)
* [AWS CodeBuild](https://docs.earthly.dev/ci-integration/vendor-specific-guides/codebuild-integration)
* [Jenkins](https://docs.earthly.dev/ci-integration/vendor-specific-guides/jenkins)
* [Kubernetes](https://docs.earthly.dev/ci-integration/vendor-specific-guides/kubernetes)

For more general information on CI systems not listed above, see the [CI integration guide](https://docs.earthly.dev/ci-integration/overview).

## Example Earthfiles

In this section, you will find some examples of Earthfiles to familiarize yourself with Earthly.

The code for all the examples is available in the [examples GitHub directory](https://github.com/earthly/earthly/tree/main/examples).

### Examples from the Basics tutorial

If you are new to Earthly, you may find the [Basics tutorial](https://docs.earthly.dev/basics) helpful.

* [tutorial](https://github.com/earthly/earthly/tree/main/examples/tutorial)
  * [go](https://github.com/earthly/earthly/tree/main/examples/tutorial/go)
  * [js](https://github.com/earthly/earthly/tree/main/examples/tutorial/js)
  * [java](https://github.com/earthly/earthly/tree/main/examples/tutorial/java)
  * [python](https://github.com/earthly/earthly/tree/main/examples/tutorial/python)

### Examples by language

Please note that these examples, although similar, are distinct from the ones used in the [tutorial](https://github.com/earthly/earthly/tree/main/examples/tutorial).

* [c](https://github.com/earthly/earthly/tree/main/examples/c)
* [cobol](https://github.com/earthly/earthly/tree/main/examples/cobol)
* [cpp](https://github.com/earthly/earthly/tree/main/examples/cpp)
* [dotnet](https://github.com/earthly/earthly/tree/main/examples/dotnet)
* [elixir](https://github.com/earthly/earthly/tree/main/examples/elixir)
* [go](https://github.com/earthly/earthly/tree/main/examples/go)
* [java](https://github.com/earthly/earthly/tree/main/examples/java)
* [js](https://github.com/earthly/earthly/tree/main/examples/js)
* [python](https://github.com/earthly/earthly/tree/main/examples/python)
* [ruby](https://github.com/earthly/earthly/tree/main/examples/ruby)
* [ruby-on-rails](https://github.com/earthly/earthly/tree/main/examples/ruby-on-rails)
* [rust](https://github.com/earthly/earthly/tree/main/examples/rust)
* [scala](https://github.com/earthly/earthly/tree/main/examples/scala)
* [typescript-node](https://github.com/earthly/earthly/tree/main/examples/typescript-node)

### Examples by use-cases

* [integration-test](https://github.com/earthly/earthly/tree/main/examples/integration-test) - shows how `WITH DOCKER` and `docker-compose` can be used to start up services and then run an integration test suite.
* [monorepo](https://github.com/earthly/earthly/tree/main/examples/monorepo) - shows how multiple sub-projects can be co-located in a single repository and how the build can be fragmented across these.
* [multirepo](https://github.com/earthly/earthly/tree/main/examples/multirepo) - shows how artifacts from multiple repositories can be referenced in a single build. See also the `grpc` example for a more extensive use-case.

### Examples by Earthly features

* [import](https://github.com/earthly/earthly/tree/main/examples/import) - shows how to use the `IMPORT` command to alias project references.
* [cutoff-optimization](https://github.com/earthly/earthly/tree/main/examples/cutoff-optimization) - shows that if an intermediate artifact does not change, then the rest of the build will use the cache, even if the source has changed.
* [multiplatform](https://github.com/earthly/earthly/tree/main/examples/multiplatform) - shows how Earthly can execute builds and create images for multiple platforms, using QEMU emulation.
* [multiplatform-cross-compile](https://github.com/earthly/earthly/tree/main/examples/multiplatform-cross-compile) - shows has through the use of cross-compilation, you can create images for multiple platforms, without using QEMU emulation.

### Examples by use of other technologies

* [grpc](https://github.com/earthly/earthly/tree/main/examples/grpc) - shows how to use Earthly to compile a protobuf grpc definition into protobuf code for both a Go-based server, and a python-based client, in a multirepo setup.
* [terraform](https://github.com/earthly/earthly/tree/main/examples/terraform) - shows how Terraform could be used from Earthly.

### Other

* [readme](https://github.com/earthly/earthly/tree/main/examples/readme) - some sample code we used in our README.
* [tests](https://github.com/earthly/earthly/tree/main/tests) - a suite of tests Earthly uses to ensure that its features are working correctly.

### Earthly's own build

As a distinct example of a complete build, you can take a look at Earthly's own build. Earthly builds itself, and the build files are available on GitHub:

* [Earthfile](https://tinyurl.com/yt3d3cx6) - the root build file
* [buildkitd/Earthfile](https://tinyurl.com/yvnpuru7) - the build of the Buildkit daemon
* [AST/parser/Earthfile](https://tinyurl.com/2k3u4vty) - the build of the parser, which generates .go files
* [tests/Earthfile](https://tinyurl.com/2p8ws579) - system and smoke tests
* [contrib/earthfile-syntax-highlighting/Earthfile](https://tinyurl.com/yp4y6byn) - the build of the VS Code extension

To invoke Earthly's build, check out the code and then run the following in the root of the repository

```bash
earthly +all
```

[![asciicast](https://asciinema.org/a/313845.svg)](https://asciinema.org/a/313845)

# Misc

# Alternative installation

## Alternative Installation

This page outlines alternative installation instructions for the `earthly` build tool. The main instructions that most users need are available on the [installation instructions page](https://earthly.dev/get-earthly).

### Prerequisites

* [Docker](https://docs.docker.com/install/) or [Podman](https://docs.podman.io/en/latest/)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* (*Windows only*) [Docker WSL 2 backend](https://docs.docker.com/docker-for-windows/wsl/) or [Podman WSL2 backend](https://github.com/containers/podman/blob/main/docs/tutorials/podman-for-windows.md)

### Install earthly

Download the binary relevant to your platform from [the releases page](https://github.com/earthly/earthly/releases), rename it to `earthly` and place it in your `bin`.

To initialize the installation, including adding auto-completion for your shell, run

```bash
sudo earthly bootstrap --with-autocomplete
```

and then restart your shell.

#### CI

For instructions on how to install `earthly` for CI use, see the [CI integration guide](https://github.com/earthly/earthly/blob/docs-0.6/docs/alt-installation/ci-integration/overview.md).

#### Installing from Earthly repositories (**beta**)

{% hint style="danger" %}
**Important**

Our rpm and deb repositories are currently in **Beta** stage.

* Check the [GitHub tracking issue](https://github.com/earthly/earthly/issues/986) for any known problems.
* Give us feedback on [Slack](https://earthly.dev/slack).
  {% endhint %}

Earthly can be installed for Debian and RedHat based Linux distributions via the Earthly deb and rpm repositories.

All of our binaries are signed with our [PGP key](https://pkg.earthly.dev/earthly.pgp); which has the fingerprint:

```
5816 B221 3DD1 CEB6 1FC9 52BA B118 5ECA 33F8 EB64
```

**Debian-based repositories (including Ubuntu)**

Debian-based Linux users (e.g. Debian, Ubuntu, Mint, etc) can use our apt repo to install Earthly.

Before installing Earthly, you must first set up the Earthly apt repo.

1. Update apt and install required tools to support https-based apt repos:

   ```bash
   sudo apt-get update
   sudo apt-get install \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg \
      lsb-release
   ```

2. Download Earthly's GPG key:

   ```bash
   curl -fsSL https://pkg.earthly.dev/earthly.pgp | sudo gpg --dearmor -o /usr/share/keyrings/earthly-archive-keyring.gpg
   ```

3. Setup the stable repo:

   ```bash
   echo \
     "deb [arch=amd64 signed-by=/usr/share/keyrings/earthly-archive-keyring.gpg] https://pkg.earthly.dev/deb \
     stable main" | sudo tee /etc/apt/sources.list.d/earthly.list > /dev/null
   ```

4. Install Earthly:

   ```bash
   sudo apt-get update
   sudo apt-get install earthly
   ```

**Fedora repositories**

Fedora users can use our rpm repo to install Earthly.

1. Install plugins required to manage DNF repositories:

   ```bash
   sudo dnf -y install dnf-plugins-core
   ```

2. Add the Earthly repo to your system:

   ```bash
   sudo dnf config-manager \
       --add-repo \
       https://pkg.earthly.dev/earthly.repo
   ```

3. Install Earthly:

   ```bash
   sudo dnf install earthly
   ```

**CentOS repositories**

CentOS users can use our rpm repo to install Earthly.

1. Install utils required to manage yum repositories:

   ```bash
   sudo yum install -y yum-utils
   ```

2. Add the Earthly repo to your system:

   ```bash
   sudo yum-config-manager \
       --add-repo \
       https://pkg.earthly.dev/earthly.repo
   ```

3. Install Earthly:

   ```bash
   sudo yum install earthly
   ```

#### Native Windows

{% hint style="danger" %}
**Important**

Our native Windows release is currently in the **Experimental** stage.

* The release ships with known issues. Many things work, but some don't.
* Check the [GitHub tracking issue](https://github.com/earthly/earthly/issues/1031) for any known problems.
* Give us feedback on [Slack](https://earthly.dev/slack).
  {% endhint %}

To install the Windows release, simply [download](https://github.com/earthly/earthly/releases/latest/download/earthly-windows-amd64.exe) the binary (or from our [release page](https://github.com/earthly/earthly/releases/latest/)); and ensure it is within your `PATH`.

To add `earthly.exe` to your `PATH` environment variable:

1. Search and select: System (Control Panel)
2. Click the Advanced system settings link.
3. Click Environment Variables. In the "System Variables" section, select the PATH environment variable and click Edit.
   * If the PATH environment variable does not exist, click New.
4. In the Edit window, specify the value of the PATH environment variable, and Click OK.
5. Close and reopen any existing terminal windows, so they will pick up the new `PATH`.

If you are going to mostly be working from a WSL2 prompt in Windows, you might want to consider following the Linux instructions for installation. This will help prevent any cross-subsystem file transfers and keep your builds fast. Note that the "original" WSL is unsupported.

#### macOS Binary

While installing `earthly` via Homebrew is the recommended approach, you can also download a binary directly. This may be useful when using `earthly` on a Mac in CI scenarios.

* [M1 Binary](https://github.com/earthly/earthly/releases/latest/download/earthly-darwin-arm64)
* [x64 Binary](https://github.com/earthly/earthly/releases/latest/download/earthly-darwin-amd64)

When using a precompiled binary, you may need to add an exception to Gatekeeper. [Follow Apple's instructions to add this exception](https://support.apple.com/guide/mac-help/apple-cant-check-app-for-malicious-software-mchleab3a043/mac).

#### Installing from source

To install from source, see the [contributing page](https://github.com/earthly/earthly/blob/main/CONTRIBUTING.md).

### Configuration

If you use SSH-based git authentication, then your git credentials will just work with Earthly. Read more about [git auth](https://github.com/earthly/earthly/blob/docs-0.6/docs/alt-installation/guides/auth.md).

For a full list of configuration options, see the [Configuration reference](https://github.com/earthly/earthly/blob/docs-0.6/docs/alt-installation/earthly-config/earthly-config.md)

### Verify installation

To verify that the installation works correctly, you can issue a simple build of an existing hello-world project

```bash
earthly github.com/earthly/hello-world:main+hello
```

You should see the output

```
github.com/earthly/hello-world:main+hello | --> RUN [echo 'Hello, world!']
github.com/earthly/hello-world:main+hello | Hello, world!
github.com/earthly/hello-world:main+hello | Target github.com/earthly/hello-world:main+hello built successfully
=========================== SUCCESS ===========================
```

## Uninstall

To remove earthly, run the following commands:

### macOS users

```bash
brew uninstall earthly
rm -rf ~/.earthly
docker rm --force earthly-buildkitd
docker volume rm --force earthly-cache
```

### Linux and WSL2 users

```bash
rm /usr/local/bin/earthly
rm /usr/share/bash-completion/completions/earthly
rm /usr/local/share/zsh/site-functions/_earthly
rm -rf ~/.earthly
docker rm --force earthly-buildkitd
docker volume rm --force earthly-cache
```

# Data collection

By default, Earthly collects anonymized data which we use for measuring performance of the earthly command.

## Installation ID

Earthly will create a universally unique installation ID (UUID v4) under `~/.earthly/install_id`, which is used to track each installation. This ID is randomly created and does not contain any personal data.

## Anonymized data

In addition to the installation ID, earthly will also collect a one-way-hash of the git repository name.

## CI platform

Earthly applies some heuristics to determine if it is running in a CI system, and will report which CI system is detected (e.g. GitHub Actions, Circle CI, Travis CI, Jenkins, etc).

## Command and exit code

Earthly will report which command was run (e.g. build, prune, etc), the execution time, and corresponding exit code. Command line arguments are *not* captured.

## Disabling analytics

To disable the collection of data, set the `disable_analytics` option to `true` under the global config file `~/.earthly/config.yml`.

For example:

```yaml
global:
    disable_analytics: true
```

This option is documented in the [Earthly configuration file page](https://docs.earthly.dev/docs/earthly-config).

# Definitions

This page presents some common terms used throughout the earthly documentation. Understanding these terms with help you understand how to use earthly.

* **Earthly** - the build automation system as a whole
* **`earthly`** - the CLI tool used to interact with Earthly
* **Earthfile** - a file (named literally `Earthfile`) which contains a series of targets and their respective recipes
* **buildkitd** - a [daemon built by the Docker team](https://github.com/moby/buildkit) and used by Earthly to execute builds. It executes LLB, the same low-level primitives used when building Dockerfiles. The buildkitd daemon is started automatically in a docker container, by `earthly`, when executing builds.
* **recipe** - a specific series of build steps
* **target** - the label used to identify a recipe. 'Target' is also used to refer to a build of a specific target.
* **build context** - the main directory made available to the build for copying files from
* **artifact** - a file resulting from executing a target (not all targets have artifacts)
* **image** - a docker image resulting from executing a target (not all targets have images)

## See also

* The [Earthfile reference](https://docs.earthly.dev/docs/earthfile)
* The [earthly command reference](https://docs.earthly.dev/docs/earthly-command)

# Public key authentication

Earthly provides public-key based authentication (in addition to traditional username and password authentication). This guide details how it works.

## What is public-key authentication

Public key authentication provides greater security compared to password authentication; it is achieved by using [asymmetric cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography).

A user generates a pair of private and public keys; the public key is publicly distributed to anyone who wishes to send an encrypted message that only the holder of the private key can decrypt. It is important that you **never share your private key**, otherwise anyone could use it to access data that is only intended for you.

Similarly, it is possible to sign data using your private key -- any user who has your public key can use it to verify the message was signed by you (or anyone who has access to your private key).

For these reasons, it is crucial that your private key remains private -- as a result, **earthly will never store, or transmit your private key**.

## How does earthly implement public-key authentication

Earthly accounts can be associated with any number of public keys (both `ssh-rsa`, and `ssh-ed25519` public keys are supported). These public keys are stored on the earthly server, in a database that mimics the `~/.ssh/authorized_keys` file one typically finds on a server.

The client first connects to the earthly server over a https connection; the client responds with a [cryptographically-secure random](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator) blob of data. The client then passes that blob of data to the [ssh-agent](https://en.wikipedia.org/wiki/Ssh-agent) process, which must be running on your local host. This connection occurs by using the local unix-socket as set by the `SSH_AUTH_SOCK` environment variable. The ssh-agent signs the blob of data, and returns the signature -- **earthly will never read your private keys directly**.

This signature is sent to the earthly server; if the signature can be verified using a registered public key, then the server responds with a [JSON Web Token (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token) which is used for the duration of your session.

# Overview

Continuous Integration systems are as varied as the companies that use them. Fortunately, Earthly is flexible enough to fit into most (and where we don't, let us know!). This document serves as a starting point to configuring Earthly in your CI environment.

Setting up Earthly is as easy as three steps:

1. [Installing Dependencies](#dependencies)
2. [Installing Earthly](#installation)
3. [Configuration](#configuration)

We also have instructions for [specific CI systems](#examples); and special-case instructions for other scenarios (explore the "CI Integrations" category.)

## Dependencies

Earthly has two software dependencies: `docker` and `git`. Because `earthly` will not install these for you, please ensure they are present before proceeding. These tools are very common, so many environments will already have them installed. If you choose to use our prebuilt containers, these dependencies are already included.

`docker` is used to glean information about the containerization environment, and manage our `earthly-buildkitd` daemon. It is also used to do things like save images locally on your machine after they have been built by Earthly. To install `docker`, use the most recent versions [directly from Docker](https://docs.docker.com/engine/install/#server). The versions packaged for many distributions tend to fall behind.

`git` is used to help fetch remote targets, and also provides metadata for Earthly during your build. To install `git`, [you can typically use your distributions package manager](https://git-scm.com/download/linux).

## Installation

Once you have ensured that the dependencies are available, you'll need to install `earthly` itself.

### Option 1: Direct install

This is the simplest method for adding `earthly` to your CI. It will work best on dedicated computers, or in scripted/auto-provisioned build environments. You can pin it to a specific version like so:

```shell
wget https://github.com/earthly/earthly/releases/download/v0.6.30/earthly-linux-amd64 -O /usr/local/bin/earthly && \
chmod +x /usr/local/bin/earthly && \
/usr/local/bin/earthly bootstrap
```

It is recommended to install `earthly` as part of the new host's configuration, and not as part of your build. This will speed up your builds, since you do not need to download `earthly` each time; and it will also provide stability in case a future version of `earthly` changes the behavior of a command.

Don't forget to run `earthly bootstrap` when you are done to finish configuration!

### Option 2: Image

If a local installation isn't possible, Earthly currently offers two official images:

* [`earthly/earthly`](https://hub.docker.com/r/earthly/earthly), which is a 1-stop shop. It includes a built-in `earthly-buildkitd` daemon, and accepts a target to be built as a parameter. It requires a mount for your source code, and an accessible `DOCKER_HOST`.
* [`earthly/buildkitd`](https://hub.docker.com/r/earthly/buildkitd), which is the same `earthly-buildkitd` container that `earthly` will run on your host. This is useful in more advanced configurations, such as [remotely sharing](https://docs.earthly.dev/ci-integration/remote-buildkit) a single `buildkitd` machine across many workers, or isolating the privileged parts of builds. This feature is experimental.

If you need to provide additional configuration or tools, [consider building your own image for CI](https://docs.earthly.dev/ci-integration/build-an-earthly-ci-image).

## Configuration

While `earthly` is fairly configurable by itself, it also depends on the configuration of its dependencies. In a CI environment, you will need to ensure all of them are configured correctly.

### Git

If you plan to build any private, or otherwise secure repositories, `git` will need to be configured to have access to these repositories. Please see our [documentation for how to configure access](https://docs.earthly.dev/docs/guides/auth#git-authentication).

### Docker

Like `git`, `docker` also needs to be configured to have access to any private repositories referenced in the `Earthfiles` you want to build. Please our [documentation for how to log in](https://docs.earthly.dev/docs/guides/auth#docker-authentication), and our examples for pushing to many popular repositories.

If your private registry can use a [credential helper](https://docs.docker.com/engine/reference/commandline/login/#credential-helpers), configure it according to your vendor's instructions. `earthly` can also make use of these to provide access when needed. If you need help configuring `docker` for use with Earthly, see our [guides on configuring many popular registries](https://docs.earthly.dev/docs/guides/configuring-registries) for details.

Finally, the `earthly-buildkitd` daemon requires running in `--privileged` mode, which means that the `docker` daemon needs to be configured to allow this as well. Rootless configurations are currently unsupported.

### Earthly

`earthly` has quite a few configuration options that can either be set through a configuration file or environment variables. See our [configuration reference](https://docs.earthly.dev/docs/earthly-config) for a complete list of options.

You can also configure `earthly` by using the [`earthly config` command](https://docs.earthly.dev/docs/earthly-command#earthly-config) from within a script. This can be useful for some dynamic configuration.

Some options that may make sense in a CI environment are:

| Variable                   | Description                                                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `CNI_MTU`                  | In some environments, the MTU externally may be different than the MTU on the internal CNI network, causing the internet to be unavailable. This lets you configure the internal network for when `earthly` auto-configures the MTU incorrectly. |
| `NO_COLOR` / `FORCE_COLOR` | Lets you force on/off the ANSI color codes. Use this when `earthly` misinterprets the presence of a terminal. Set either one to `1` to enable or disable colors.                                                                                 |
| `EARTHLY_BUILDKIT_HOST`    | Use this when you have an external BuildKit instance you would like to use instead of the one `earthly` manages.                                                                                                                                 |

Earthly also has some special command-line switches to ensure best practices are followed within your CI. These come *highly* recommended. Enable these with the [`--ci`](https://docs.earthly.dev/docs/earthly-command#--ci) option, which is shorthand for [`--save-inline-cache`](https://docs.earthly.dev/docs/earthly-command#save-inline-cache) [`--strict`](https://docs.earthly.dev/docs/earthly-command#strict) [`--no-output`](https://docs.earthly.dev/docs/earthly-command#no-output).

Earthly also has a special [`--push`](https://docs.earthly.dev/docs/earthfile#push) option that can be used when invoking a target. In a CI, you may want to ensure this flag is present to push images or run commands that are not typically done as part of a normal development workflow.

If you would like to do cross-platform builds, you will need to install some [`binfmt_misc`](https://github.com/multiarch/qemu-user-static) entries. This can be done by running: `docker run --rm --privileged multiarch/qemu-user-static --reset -p yes`. This installs the needed entries and `qemu-user-static` binaries on your system. This will need to be repeated on each physical box (only once, since its a kernel level change, and the kernel is shared across containers).

To share secrets with `earthly`, use the [`--secret`](https://docs.earthly.dev/docs/earthfile#secret-less-than-env-var-greater-than-less-than-secret-ref-greater-than) option to inject secrets into your builds. You could also use our [cloud secrets](https://docs.earthly.dev/earthly-cloud/cloud-secrets), for a more seamless experience.

### Networking & Security

Upon invocation, `earthly` depends on the availability of an `earthly-buildkit` daemon to perform its build. This daemon has some networking and security considerations.

Large builds can generate many `docker` pull requests for certain images. You can set up and use a [pull through cache](https://docs.earthly.dev/ci-integration/pull-through-cache) to circumvent this.

If `earthly` is running on a dedicated host, the only consideration to take is the ability to run the container in a `--privileged` mode. Typical installations *should* support this out of the box. We also support running under user namespaces, [when `earthly` is configured to start the `earthly-buildkit` container with the `--userns host` option](https://docs.earthly.dev/docs/earthly-config#buildkit_additional_args). Rootless configurations are currently unsupported.

If `earthly` is connecting to a remote `earthly-buildkitd`, then you will need to take additional steps. See this article for [running a remote BuildKit instance](https://docs.earthly.dev/ci-integration/remote-buildkit).

## Examples

Below are links to CI systems that we have more specific information for. If you run into anything in your CI that wasn't covered here, we would love to add it to our documentation. Pull requests are welcome!

* [Jenkins](https://docs.earthly.dev/ci-integration/vendor-specific-guides/jenkins)
* [Kubernetes](https://docs.earthly.dev/ci-integration/vendor-specific-guides/kubernetes)
* [Circle CI](https://docs.earthly.dev/ci-integration/vendor-specific-guides/circle-integration)
* [AWS CodeBuild](https://docs.earthly.dev/ci-integration/vendor-specific-guides/codebuild-integration)
* [GitHub Actions](https://docs.earthly.dev/ci-integration/vendor-specific-guides/gh-actions-integration)
* [Google Cloud Build](https://docs.earthly.dev/ci-integration/vendor-specific-guides/google-cloud-build)
* [GitLab CI/CD](https://docs.earthly.dev/ci-integration/vendor-specific-guides/gitlab-integration)
* [Woodpecker CI](https://docs.earthly.dev/ci-integration/vendor-specific-guides/woodpecker-integration)

# Use the Earthly CI Image

## Introduction

This guide is intended to help you use the Earthly image for your containerized CI workflows.

## Prerequisites

The `earthly/earthly` image requires that it is run as `--privileged`, or alternatively, it is run without the embedded Buildkit daemon (`NO_BUILDKIT=1`).

## Getting Started

Please see the reference documentation of the [`earthly/earthly` image on DockerHub](https://hub.docker.com/r/earthly/earthly).

It is recommended that the `earthly/earthly` image is used with a pinned version when used in the context of a CI, in order to avoid accidental future breakage as `earthly` evolves.

#### Using `/usr/bin/earthly-entrypoint.sh` as the entrypoint

The `earthly/earthly` image comes with an entrypoint that first starts up BuildKit and then issues an `earthly` command that makes use of it. You may use the image just as you would use `earthly` itself otherwise. Any arguments are passed into the `earthly` command directly.

{% hint style="danger" %}
**Important**

Note that using the `earthly` binary as the entrypoint will not start up BuildKit within the same container and will instead attempt to use the Docker Daemon (assuming one is available via `/var/run/docker.sock`) to start up BuildKit.
{% endhint %}

#### Remote Daemon

An alternative option is to use the `earthly/earthly` image in conjunction with a remote BuildKit Daemon. You may use the environment variable `BUILDKIT_HOST` to specify the hostname of the remote BuildKit Daemon. When this environment variable is set, the `earthly/earthly` image will not attempt to start BuildKit and will instead use the remote BuildKit Daemon.

You may also use the `earthly/earthly` image to run a build against an Earthly Satellite. To achieve this you can pass along an `EARTHLY_TOKEN` environment variable, along with the command-line flags `--sat` and `--org`, to point the build to a specific satellite.

For more details on using remote execution, [see our guide on remote Buildkit](https://docs.earthly.dev/ci-integration/remote-buildkit) or the [introduction to Satellites](https://docs.earthly.dev/earthly-cloud/satellites).

#### Mounting the source code

The image expects the source code of the application you are building in the current working directory (by default `/workspace`). You will need to copy or mount the necessary files to that directory prior to invoking the entrypoint.

```bash
docker run --privileged --rm -v "$PWD":/workspace earthly/earthly:v0.6.30 +my-target
```

Or, if you would like to use an alternative directory:

```bash
docker run --privileged --rm -v "$PWD":/my-dir -w /my-dir earthly/earthly:v0.6.30 +my-target
```

Alternatively, you may rely on Earthly to perform a git clone, by using the remote target reference format. For example:

```bash
docker run --privileged --rm earthly/earthly:v0.6.30 github.com/foo/bar:my-branch+target
```

#### `NO_BUILDKIT` Environment Variable

As the embedded Buildkit daemon requires `--privileged`, for some operations you may be able to use the `NO_BUILDKIT=1` environment variable to disable the embedded Buildkit daemon. This is especially useful when running against a remote buildkit (like a Satellite), or when not performing a build as part of the command (like when using `earthly account`).

## An important note about running the image

When running the built image in your CI of choice, if you're not using a remote daemon, Earthly will start Buildkit within the same container. In this case, it is important to ensure that the directory used by Buildkit to cache the builds is mounted as a Docker volume. Failing to do so may result in excessive disk usage, slow builds, or Earthly not functioning properly.

{% hint style="danger" %}
**Important**

We *strongly* recommend using a Docker volume for mounting `/tmp/earthly`. If you do not, Buildkit can consume excessive disk space, operate very slowly, or it might not function correctly.
{% endhint %}

In some environments, not mounting `/tmp/earthly` as a Docker volume results in the following error:

```
--> WITH DOCKER RUN --privileged ...
...
rm: can't remove '/var/earthly/dind/...': Resource busy
```

For more information, see the [documentation for `earthly/earthly` on DockerHub](https://hub.docker.com/r/earthly/earthly).

# Build your own Earthly CI Image

## Introduction

This guide is intended to help you create your own Docker image with Earthly inside it for your containerized CI workflows.

## Getting Started

There are two ways to build a containerized CI image with Earthly:

* Extending the `earthly/earthly` image with an external runner/agent
* Adding Earthly to an existing image

This guide will cover both approaches to constructing your image.

### Extending The `earthly/earthly` Image

This is the recommended approach when adopting Earthly into your containerized CI. Start by basing your custom image on ours:

```docker
FROM earthly/earthly:v0.6.30
RUN ... # Add your agent, certificates, tools...
```

When extending our image, be sure to pin to a specific version to avoid accidental future breakage as `earthly` evolves.

The `earthly/earthly` image is Alpine Linux based. To add tools to the image, you can use `apk`:

```docker
apk add --no-cache my-cool-tool
```

If you are adding a tool from outside the Alpine Linux repositories, test it to ensure it is compatible. Alpine uses `musl`, which *can* create incompatibilities with some software.

Also, you should embed any configuration that your Earthly image might need (to avoid having it in your build scripts, or mounted from a host somewhere). You can do this in-line with the [`earthly config` command](https://docs.earthly.dev/docs/earthly-command#earthly-config).

### Adding Earthly To An Existing Image

This section will cover adding Earthly to an existing image when:

* Docker-In-Docker is configured for the base image
* Earthly will be connecting to a remote `earthly/buildkitd` instance

While it is possible to configure a locally-ran `earthly/buildkitd` instance within an image (it's how `earthly/earthly` works), the steps and tweaks are beyond the scope of this guide.

#### Docker-In-Docker

In this setup, Earthly will be allowed to manage an instance of its `earthly/buildkitd` daemon over a live Docker socket.

To enable this, simply follow the installation instructions within your Dockerfile/Earthfile as you would on any other host. An example of installing this can be found below.

```docker
RUN wget https://github.com/earthly/earthly/releases/download/v0.6.30/earthly-linux-amd64 -O /usr/local/bin/earthly && \
    chmod +x /usr/local/bin/earthly && \
    /usr/local/bin/earthly bootstrap
```

As with the Docker containers, be sure to pin the version in the download URL to avoid any accidental future breakage. Assuming Docker is also installed and available, you should be able to invoke Earthly without any additional configuration.

#### Remote Daemon

When connecting to a remote daemon, follow the Docker-In-Docker installation instructions above to get the binary. Then you'll need to issue a few `earthly config` commands to ensure the container is set up to automatically use the remote daemon. It might look something like this:

```docker
RUN earthly config global.buildkit_host buildkit_host: 'tcp://myhost:8372'
```

For more details on using a remote BuildKit daemon, [see our guide](https://docs.earthly.dev/ci-integration/remote-buildkit).

## cgroups v2 Considerations

When cgroups v2 is detected by the `earthly/earthly` image's default entrypoint, it moves it's process under an isolated cgroup. If a different entrypoint is used (i.e. a custom user supplied script), the root process must be moved into a separate cgroup, for example:

```bash
if [ -f "/sys/fs/cgroup/cgroup.controllers" ]; then
    echo "detected cgroups v2; moving pid $$ to subgroup"

    # move the process under a new cgroup to prevent buildkitd/entrypoint.sh
    # from getting a "sh: write error: Resource busy" error while enabling controllers
    # via echo +pids > /sys/fs/cgroup/cgroup.subtree_control
    mkdir -p /sys/fs/cgroup/my-entrypoint
    echo "$$" > /sys/fs/cgroup/my-entrypoint/cgroup.procs
fi
```

If this step is not performed before the buildkitd process starts up, buildkitd will be unable to initialize it's own cgroup (due to the container's root cgroup already having processes directly under it), and will fail with the error: `sh: write error: Resource busy`.

## An important note about running the image

When running the built image in your CI of choice, if you're not using a remote daemon, Earthly will start Buildkit within the same container. In this case, it is important to ensure that the directory used by Buildkit to cache the builds is mounted as a Docker volume. Failing to do so may result in excessive disk usage, slow builds, or Earthly not functioning properly.

{% hint style="danger" %}
**Important**

We *strongly* recommend using a Docker volume for mounting `/tmp/earthly`. If you do not, Buildkit can consume excessive disk space, operate very slowly, or it might not function correctly.
{% endhint %}

In some environments, not mounting `/tmp/earthly` as a Docker volume results in the following error:

```
--> WITH DOCKER RUN --privileged ...
...
rm: can't remove '/var/earthly/dind/...': Resource busy
```

In EKS, users reported that mounting an EBS volume, instead of a Kubernetes `emptyDir` worked.

This part of our documentation needs improvement. If you have a Kubernetes-based setup, please [let us know](https://earthly.dev/slack) how you have mounted `/tmp/earthly` and whether `WITH DOCKER` worked well for you.

For more information, see the [documentation for `earthly/earthly` on DockerHub](https://hub.docker.com/r/earthly/earthly).

# Pull-Through Cache

## Introduction

Docker Hub, Quay, and other registry providers have pull limits, and costs associated with using them. Running large builds (or many small builds, frequently) may incur costs, rate limiting, or both. This guide will help you set up your own "pull-through" cache to reduce network traffic, and bypass the limitations imposed by registry providers.

## What Is A Pull Through Cache?

A pull through cache is a registry mirror that contains no images. When your client checks the registry for an image, the registry will either:

* Give an existing response from its cache; thereby avoiding egress (or a pull) from your registry,
* Or pull the image and its metadata from the registry on your behalf; caching it for later use.

## Running A Pull-Through Cache

To run a cache, you'll need the ability to deploy a persistent service, somewhere. This could be a dedicated instance with Docker installed, or a container in your Kubernetes cluster.

There are multiple ways to setup a registry -- Docker, for example, has a [guide for using the registry as a pull through cache](https://docs.docker.com/registry/recipes/mirror), as well as documentation for the [available options](https://docs.docker.com/registry/configuration/), and other details under the [registry image](https://hub.docker.com/_/registry).

Documenting all the possible ways to setup a pull through cache is beyond the scope of this document; however, it does include a [quick getting-started section](#insecure-docker-hub-cache-example) for those who wish to run an insecure pull through cache.

### Configuration & Tips

#### Set Up Mirror Authentication

Pull-through caches run *unsecured* by default. Add an `htpasswd` file for basic authentication, at a minimum:

```yaml
auth:
  htpasswd:
    realm: basic-realm
    path: /auth/htpasswd
```

#### Set Up Mirror TLS

Adding TLS is also highly recommended. you can bring your own certificates, or use the built-in LetsEncrypt support:

```yaml
http:
  tls:
    letsencrypt:
      cachefile: /certs/cachefile
      email: me@example.com
      hosts: [my.cool.mirror.horse]
```

The currently shipping `library/registry` image does not support the DNS-01 challenge yet, and [some of the LetsEncrypt challenge support is getting out of date](https://github.com/distribution/distribution/issues/3041). If you need this, there is a [tracking issue](https://github.com/docker/distribution-library-image/issues/96); We have had success by [building the binary ourselves](https://github.com/earthly/registry/blob/3f06d1fc5d7f456b63b870b2851fd18cd2098dcf/Earthfile#L3-L11) and replacing it in the image that Docker ships.

#### Use An Insecure Mirror

By default, Earthly expects your mirror to be using TLS. While this is not recommended, you can use an unsecured mirror by specifying the following config in the `buildkit_additional_config` setting:

```yaml
global:
  buildkit_additional_config: |
    [registry."<upstream>"]
      mirrors = ["<mirror>"]

    [registry."<mirror>"]
      insecure = true
```

Where `<mirror>` is the host/port of your mirror, and `<upstream>` is the address of the registry you are intending to mirror.

## Insecure Docker Hub Cache Example

This section contains a quick-start guide for running an insecure pull through cache using docker's `registry` container.

This guide assumes you are running on a trusted network with one computer acting as a server, and the other as your development workstation.

In these examples, we will assume the server has an IP set to `192.168.0.80`.

### Setting up the pull through cache

First connect to the server where you will be running the cache (e.g. `ssh 192.168.0.80`), and create a file under `~/.docker-registry-config.yml` containing:

```yaml
version: 0.1
log:
  fields:
    service: registry
storage:
  cache:
    blobdescriptor: inmemory
  filesystem:
    rootdirectory: /var/lib/registry
http:
  addr: :5000
  headers:
    X-Content-Type-Options: [nosniff]
health:
  storagedriver:
    enabled: true
    interval: 10s
    threshold: 3
proxy:
  remoteurl: https://registry-1.docker.io
  username: [username]
  password: [password]
```

*Note that you'll need to replace `[username]` and `[password]` with your dockerhub credentials.*

Next, start the registry container with:

```bash
docker run --rm --network host -d --name docker-registry -v $HOME/.docker-registry-config.yml:/root/config.yml registry.hub.docker.com/library/registry:2 registry serve /root/config.yml
```

You can then verify the registry is running by tailing logs with:

```bash
docker logs --follow docker-registry
```

{% hint style="info" %}
You may want to leave a second terminal window open to display the logs while you work on the following sections; this will make it more obvious when the cache is being used.
{% endhint %}

The rest of the guide focus on configuring your workstation to use this cache.

### Configuring Docker to Use the Cache

To configure docker to use this cache as a mirror, edit the `/etc/docker/daemon.json` file, and add:

```json
{
  "registry-mirrors" : ["http://192.168.0.80:5000"]
}
```

Then restart docker:

```bash
sudo service docker restart
```

Next you should be able to pull an image (e.g. `docker pull alpine:3.15`), which should use the cache.

#### Verifying the Cache is Actually Working (Optional)

If you want to verify the cache is working, you can block access to dockerhub on your workstation by adding

```
0.0.0.0 index.docker.io auth.docker.io registry-1.docker.io dseasb33srnrn.cloudfront.net production.cloudflare.docker.com
```

to your `/etc/hosts` file.

If `/etc/docker/daemon.json` was not correctly configured, you should see an error such as:

```
Error response from daemon: Get "https://registry-1.docker.io/v2/": dial tcp 0.0.0.0:443: connect: connection refused
```

If the cache is correctly configured, the pull command should work, and you should see logs on your server under the docker-registry container:

```
192.168.0.126 - - [22/Mar/2022:19:10:39 +0000] "HEAD /v2/library/alpine/manifests/3.15 HTTP/1.1" 200 1638 "" "docker/20.10.12 go/go1.16.12 git-commit/459d0df kernel/5.13.0-35-generic os/linux arch/amd64 UpstreamClient(Docker-Client/20.10.12 \\(linux\\))"
```

### Configuring Earthly to Use the Cache

To configure earthly to use the cache, you must edit `~/.earthly/config.yml` to include:

```yaml
global:
  buildkit_additional_config: |
    [registry."docker.io"]
      mirrors = ["192.168.0.80:5000"]
    [registry."192.168.0.80:5000"]
      insecure = true
```

The next time earthly is run, it will detect the configuration change and will restart the `earthly-buildkitd` container to reflect these settings.

You can force these settings to be applied, and verify the mirror appears in the buildkit config by running:

```bash
earthly bootstrap && docker exec earthly-buildkitd cat /etc/buildkitd.toml
```

# Remote BuildKit

## Introduction

In some cases, you may want to run a remote instance of [`earthly/buildkitd`](https://hub.docker.com/r/earthly/buildkitd). This guide is intended to help you identify if you might benefit from this configuration, and to help you set it up correctly.

If you are looking for a way to use remote runners without the complexities of managing them yourself, you may want to consider [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites): remote runners managed by Earthly.

### Why Remote?

Running a remote daemon is a unique feature of Earthly. It allows the build to happen elsewhere; even when executing it from your local development machine. However, it is not always the best option. Before setting up a remote daemon, first look into Earthly's shared caching capabilities and see if those can get you the boost you need. In our experience, [remote caching](https://docs.earthly.dev/docs/remote-caching) is usually enough.

However, there are instances where a remote daemon can make the most sense. Here are some examples:

* You have a single, powerful build machine you would like to share with your development team
* There is data closer to a remote machine than your development/CI environment, so you bring the build to the data
* You are using Earthly in Kubernetes, and want to isolate the containers doing the actual building because they require privileged mode
* You want to share a build machine (or cluster) with your CI environment and your developers
* Your local computer does not have the capabilities to build the software (`docker`/`dockerd` is missing, or you lack sufficient privileges, or it is simply not powerful enough)

### Running Remote BuildKit

To run a remote BuildKit instance, deploy and configure the image [`earthly/buildkitd`](https://hub.docker.com/r/earthly/buildkitd).

#### Networking

A remote daemon should be reachable by all clients intending to use it. Earthly uses ports `8371-8373` to communicate, so these should be open and available.

#### Mounts

**`/tmp/earthly`**

This path within the container is the location that Buildkit uses for storing the cache. Because this folder sees *a lot* of traffic, its important that it remains fast.

{% hint style="danger" %}
**Important**

We *strongly* recommend using a Docker volume for mounting `/tmp/earthly`. If you do not, `buildkitd` can consume excessive disk space, operate very slowly, or it might not function correctly.
{% endhint %}

In some environments, not mounting `/tmp/earthly` as a Docker volume results in the following error:

```
--> WITH DOCKER RUN --privileged ...
...
rm: can't remove '/var/earthly/dind/...': Resource busy
```

In EKS, users reported that mounting an EBS volume, instead of a Kubernetes `emptyDir` worked.

This part of our documentation needs improvement. If you have a Kubernetes-based setup, please [let us know](https://earthly.dev/slack) how you have mounted `EARTHLY_TMP_DIR` and whether `WITH DOCKER` worked well for you.

#### Daemon

To configure an `earthly/buildkitd` daemon as a remotely available daemon, you will need to start the container yourself. See our [configuration docs](https://docs.earthly.dev/docs/earthly-config) for more details on all the options available; but here are the ones you need to know:

**`BUILDKIT_TCP_TRANSPORT_ENABLED`**

This will configure `buildkitd` to listen on port `8372`. If you would like it to be externally available on a different port, you will need to handle that at the port mapping level. TCP is required for remotely sharing a daemon.

**`BUILDKIT_TLS_ENABLED`**

Set this to `true` for all daemons that will handle production workloads. This daemon *by design* is an arbitrary code execution machine, and running it without any kind of mTLS configuration is not recommended.

Make sure you mount your certificates and keys in the correct location (`/etc/*.pem`).

For complete details, see the [documentation for `earthly/buildkitd` on DockerHub](https://hub.docker.com/r/earthly/buildkitd).

#### Client

Normally, Earthly will try to start and manage its own `earthly/buildkitd` daemon. However, when relying on a remote `earthly/buildkitd` instance, Earthly will not attempt to manage this daemon. Here are the configuration options needed to use a remote instance:

**`buildkit_host`**

This is the address of the remote daemon. It should look something like this: `tcp://my-cool-remote-daemon:8372`. If the hostname is considered to be a "local" one, Earthly will fall back to the Local-Remote behaviors described below. For reference; all IPv6 Loopback addresses, `127.0.0.1`, and `[localhost](http://localhost)` are considered to be "local". The machine's hostname is not considered "local".

**`tlsca` / `tlscert` / `tlskey`**

These are the paths to the certificates and keys used by the client when communicating with an mTLS-enabled daemon. These paths are relative to the Earthly config (usually `~/.earthly/config.yaml`, unless absolute paths are specified.

**`tls_enabled`**

Set this to `true` when using TLS is desired.

### Local-Remote

It is also possible to use the remote protocols (TCP and mTLS) locally, while still letting Earthly manage the daemon container. You can do this by enabling mTLS(`tls_enabled`).

By doing this, Earthly will (optionally) generate its own certificates, and connect to the daemon using `tcp://127.0.0.1:8372`. This is a great way to test some of the remote capabilities without having to generate certificates or manage a separate machine.

# Vendor-Specific Guides

# Jenkins

## Overview

Jenkins has multiple modes of operation, and each of them require some consideration when installing Earthly. These modes include:

* Standalone, dedicated runners
* Ephemeral cloud runners

### Compatibility

Earthly has been tested with Jenkins in a standalone runner configuration, and using the Docker Cloud provider.

### Resources

* [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
* [Docker Cloud Plugin](https://plugins.jenkins.io/docker-plugin/)
* [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/)

## Setup (Standalone)

This should not differ in any meaningful way from the steps outlined in the [overview](https://docs.earthly.dev/ci-integration/overview).

## Setup (Docker Cloud)

Assuming you are following the steps outlined in the [overview](https://docs.earthly.dev/ci-integration/overview), here are the additional things you need to configure:

### Dependencies

Ensure that the Docker Cloud provider is installed and has a Docker daemon available. The Cloud provider does not provide a daemon.

### Installation

You'll need to [create your own runner image](https://docs.earthly.dev/ci-integration/build-an-earthly-ci-image). Heres an example of what this might look like, when basing your runner off our `earthly/earthly` image:

```docker
ARG VERSION=4.9
RUN apk add --update --no-cache curl bash git git-lfs openssh-client openssl procps \
  && curl --create-dirs -fsSLo /usr/share/jenkins/agent.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/agent.jar \
  && ln -sf /usr/share/jenkins/agent.jar /usr/share/jenkins/slave.jar \
  && apk del curl
```

`VERSION` is the version of the Jenkins runner to install.

### Configuration

Set `DOCKER_HOST` to point at a Docker daemon. This can easily be passed through by checking "Expose Docker Host" in the runner template configuration.

## Additional Notes

`earthly` misinterprets the Jenkins environment as a terminal. To hide the ANSI color codes, set `NO_COLOR` to `1`.

## Example

{% hint style="danger" %}
**Note**

This example is not production ready, and is intended to showcase configuration needed to get Earthly off the ground. If you run into any issues, or need help, [don't hesitate to reach out](https://github.com/earthly/earthly/issues/new)!
{% endhint %}

You can find our [Jenkins example on GitHub](https://github.com/earthly/ci-examples/tree/main/jenkins).

To run it yourself, clone the [`ci-examples` repository](https://github.com/earthly/ci-examples), and then run (from the root of the repository):

```go
earthly ./jenkins+start
```

This will start a local Jenkins server, minimally configured to spawn `earthly` builds using the Docker cloud plugin.

To run a build in this demo, you will need to configure a build pipeline. To do that, we have an [example project with a Jenkinsfile](https://github.com/earthly/ci-example-project). To configure the build pipeline for the example project:

* Open the Jenkins demo by going to [`http://localhost:8000`](http://localhost:8080/)
* Click "New Item", on the left

![Jenkins Dashboard with "New Item" highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-a3c78a2f3fc1b7c01948c0af5afb9dff68a3b832%2FJenkins1.png?alt=media\&token=8495fce5-6b8e-49bb-b57f-5188efe8ddba)

* Choose "Pipeline", give it a name (we chose "test"), and click "OK".

![Setting up a new build named test, configured as a Jenkins pipeline](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-c19da450d4ced10665975091f71d1428fde3068a%2FJenkins2.png?alt=media\&token=49995cd3-a3e6-46b8-afbb-f2431137a6cb)

* Scroll down to the "Pipeline" section.
* Make the following changes:
  * Choose "Pipeline script from SCM" for the Definition
  * Choose "Git" as the SCM, once the option appears
  * Set the repository URL to [`https://github.com/earthly/ci-example-project`](https://github.com/earthly/ci-example-project)
  * Set the branch specifier to `*/main`

![Configuring all the SCM options for the build](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-9cb6cb853ddff24260c7c0537c7adc52c89e2123%2FJenkins3.png?alt=media\&token=53c50e46-5a1a-466f-beb9-d1639b5c5d2c)

* Once those changes are made, click "Save". Jenkins will navigate to the Pipelines' main page. Once there, click "Build Now"

![Jenkins Dashboard for the example build, with "Build Now" highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-658373b8da1329a16dc8475ac6cd874f4fc4b478%2FJenkins4.png?alt=media\&token=1c72569f-b9dc-4183-8065-953e555dc6bb)

* Find the build in your build history, and watch it go!

![Console output in Jenkins from the test build](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-c5fc322f475f328bc2811f3f51f630c2de03ee88%2FJenkins5.png?alt=media\&token=15172bf6-e278-407a-8b41-a0f49340f10f)

### Notes

If you broke the example environment, you can run `earthly ./jenkins+cleanup` to clean up before trying to run again from scratch.

#### TLS

The example purposely runs a Docker-In-Docker (DIND) container without TLS for simplicity. This is *not* a recommended configuration. [Configuring TLS inside Docker.](https://docs.docker.com/engine/security/protect-access/#use-tls-https-to-protect-the-docker-daemon-socket)

To allow the `docker` client to access a daemon protected with TLS, you will need to add Jenkins credentials. Add the client key, certificate, and the server CA certificate as a credential. In our example, using the Docker Cloud provider, you can add them by choosing "Manage Jenkins", then "Manage Nodes and Clouds", and finally "Configure Clouds". Then, choose the cloud to configure for TLS, and click the "Add" button here:

![Configuring Docker credentials in Jenkins](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-e9eb085606c725a68c81ba87548dd274faa87613%2FJenkins6.png?alt=media\&token=0ab7bb30-fe14-42f4-9984-709044636053)

Also, ensure that you are using the correct port for TLS. In this image of our example cloud, we are using port `2375`, which is traditionally the insecure port for a `docker` daemon. In a TLS environment, `docker` expects port `2376`.

If you are using an external `earthly-buildkitd` with Jenkins, [you should be using mTLS](https://docs.earthly.dev/ci-integration/remote-buildkit). You will need to add the keys and certificates used there as credentials too.

# Circle CI

Here is an example of a Circle CI build, where we build the Earthly target `+build`.

```yml
# .circleci/config.yml

version: 2.1
jobs:
  build:
    machine:
      image: ubuntu-2004:2023.02.1
    steps:
      - checkout
      - run: docker login --username "$DOCKERHUB_USERNAME" --password "$DOCKERHUB_TOKEN"
      - run: "sudo /bin/sh -c 'wget https://github.com/earthly/earthly/releases/download/v0.6.30/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly'"
      - run: earthly --version
      - run: earthly --ci --push +build
```

For a complete guide on CI integration see the [CI integration guide](https://docs.earthly.dev/ci-integration/overview).

# GitHub Actions

Here is an example a GitHub Actions build, where we build the Earthly target `+build`.

```yml
# .github/workflows/ci.yml

name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      DOCKERHUB_USERNAME: ${{ secrets.DOCKERHUB_USERNAME }}
      DOCKERHUB_TOKEN: ${{ secrets.DOCKERHUB_TOKEN }}
      FORCE_COLOR: 1
    steps:
    - uses: actions/checkout@v3
    - name: Put back the git branch into git (Earthly uses it for tagging)
      run: |
        branch=""
        if [ -n "$GITHUB_HEAD_REF" ]; then
          branch="$GITHUB_HEAD_REF"
        else
          branch="${GITHUB_REF##*/}"
        fi
        git checkout -b "$branch" || true
    - name: Docker Login
      run: docker login --username "$DOCKERHUB_USERNAME" --password "$DOCKERHUB_TOKEN"
    - name: Download latest earthly
      run: "sudo /bin/sh -c 'wget https://github.com/earthly/earthly/releases/download/v0.6.30/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly'"
    - name: Earthly version
      run: earthly --version
    - name: Run build
      run: earthly --ci --push +build
```

For a complete guide on CI integration see the [CI integration guide](https://docs.earthly.dev/ci-integration/overview).

{% hint style="danger" %}

### actions/checkout ref argument

The example deliberately does not use the [`ref`](https://github.com/actions/checkout#checkout-a-different-branch) `actions/checkout@v3` option, as it can lead to inconsistent builds where a user chooses to re-run an older commit which is no longer at the head of the branch.
{% endhint %}

# AWS CodeBuild

Here is an example of an AWS CodeBuild build, where we build the Earthly target `+build`.

{% hint style="info" %}
**Note**

Ensure when you're creating your CodeBuild Project that you enable the `Privileged` flag in order to allow Earthly build Docker images.
{% endhint %}

```yml
# ./buildspec.yml
version: 0.2

phases:
  install:
    commands:
      - wget https://github.com/earthly/earthly/releases/download/v0.6.30/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly
  pre_build:
    commands:
      - echo Logging into Docker
      - docker login --username "$DOCKERHUB_USERNAME" --password "$DOCKERHUB_TOKEN"
  build:
    commands:
      - earthly --version
      - earthly --ci --push +build
```

For a complete guide on CI integration see the [CI integration guide](https://docs.earthly.dev/ci-integration/overview).

# Kubernetes

## Overview

Kubernetes isn't a CI per-se, but it *can* serve as the underpinning for many modern CI systems. As such, this example serves as a bare-bones example to base your implementations on.

### Compatibility

`earthly` has been tested with the all-in-one `earthly/earthly` mode, and works as long as the pod runs in a `privileged` mode.

It has also been tested with a *single* remote `earthly/buildkitd` running in `privileged` mode, and an `earthly/earthly` pod running without any additional security concerns. This configuration is considered experimental. See [these additional instructions](https://docs.earthly.dev/ci-integration/remote-buildkit).

Multi-node `earthly/buildkitd` configurations are currently unsupported.

### Resources

* [Kubernetes Documentation](https://kubernetes.io/docs/home/supported-doc-versions/)
* [Kubernetes Taints & Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)

## Setup (`earthly/earthly` Only)

This is the recommended approach when using Earthly within Kubernetes. Assuming you are following the steps outlined in the [overview](https://docs.earthly.dev/ci-integration/overview), here are the additional things you need to configure:

### Dependencies

Your Kubernetes cluster needs to allow `privileged` mode pods. It's possible to use a separate instance group, along with Taints and Tolerations to effectively segregate these pods.

### Installation

The default image from `earthly/earthly` should be sufficient. If you need additional tools or configuration, you can [create your own runner image](https://docs.earthly.dev/ci-integration/build-an-earthly-ci-image).

### Configuration

In some instances, notably when using [Calico](https://www.tigera.io/project-calico/) within your cluster, the MTU of the clusters network may end up mismatched with the internal CNI network, preventing external communication. You can set this through the `CNI_MTU` environment variable to force a match.

`earthly/earthly` currently requires the use of privileged mode. Use this in your container spec to enable it:

```yaml
securityContext:
  privileged: true
```

The `earthly/earthly` container will operate best when provided with decent storage for intermediate operations. Mount a volume like this:

```yaml
volumeMounts:
  - mountPath: /tmp/earthly
    name: buildkitd-temp
...
volumes:
  - name: buildkitd-temp
    emptyDir: {} # Or other volume type
```

The location within the container for this temporary folder is configurable with the `EARTHLY_TMP_DIR` environment variable.

The `earthly/earthly` image will expect to find the source code (with `Earthfile`) rooted in the default working directory, which is set to `/workspace`.

## Setup (Remote `earthly/buildkitd`)

{% hint style="danger" %}
**Note**

This an *experimental* configuration.
{% endhint %}

It is possible to run multiple `earthly/buildkitd` instances in Kubernetes, for larger deployments. Follow the configuration instructions for using the `earthly/earthly` image above.

There are some caveats that come with this kind of a setup, though:

1. Some local cache is not available across instances, so it may take a while for the cache to become "warm".
2. Builds that occur across multiple instances simultaneously may fail in odd ways. This is not supported.
3. The TLS configuration needs to be shared across the entire fleet.

### Configuration

To mitigate some of the issues, it is recommended to run in a "sticky" mode to keep builds pinned to a single instance for the duration. You can see how to do this in our example:

```yaml
# Use session affinity to prevent "roaming" across multiple buildkit instances; if needed.
sessionAffinity: ClientIP
sessionAffinityConfig:
  clientIP:
    timeoutSeconds: 600 # This should be longer than your build.
```

## Example

{% hint style="danger" %}
**Note**

This example is not production ready, and is intended to showcase configuration needed to get Earthly off the ground. If you run into any issues, or need help, [don't hesitate to reach out](https://github.com/earthly/earthly/issues/new)!
{% endhint %}

See our [Kubernetes examples](https://github.com/earthly/ci-examples/tree/main/kubernetes).

To run it yourself, first you will need to install some prerequisites on your machine. This example requires `kind` and `kubectl` to be installed on your system. Here are some links to installation instructions:

* [`kind` Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
* [Install `kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl)

When you are ready, clone the [`ci-examples` repository](https://github.com/earthly/ci-examples), and then run (from the root of the repository):

```go
earthly ./kubernetes+start
```

Running this target will:

* Create a `kind` cluster named `earthlydemo-aio`
* Create & watch a `job` that runs an `earthly` build

When the example is complete, the cluster is left up and intact for exploration and experimentation. If you would like to clean up the cluster when complete, run (again from the root of the repository):

```go
earthly ./kubernetes+clean
```

# Google Cloud Build

## Overview

Google's Cloud Build is a popular, hosted build platform with deep integrations into the Google Cloud ecosystem. It includes native support for containerized builds, as well as other build scenarios. This guide will cover the use of Earthly within the `cloudbuild.yaml` spec (though it should be easily ported over to the `json` format if desired).

### Compatibility

Earthly itself is able to run as expected within Cloud Build, including privileged mode features like `WITH DOCKER`. However, Application Default Credentials are not available, so any `gcloud` or `gsutil` commands within your `Earthfile` will require additional manual configuration via a service account.

### Resources

* [Getting Started With Cloud Build](https://cloud.google.com/build/docs/quickstart-build)
* [Authenticating As A Service Account](https://cloud.google.com/docs/authentication/production)
* [`cloudbuild.yaml` Specification](https://cloud.google.com/build/docs/build-config-file-schema)
* [Creating and Managing build triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers)

## Setup

Depending on your needs and existing infrastructure, there may be additional configuration needed in your Google Cloud environment.

### Dependencies

Ensure that your repositories are connected to Cloud Build. [Google has a fantastic walkthrough for this](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo).

### Configuration

{% hint style="danger" %}
**Note**

If you do not intend to use any Google Cloud utilities or capabilities within your build, this service account configuration is optional.
{% endhint %}

Begin by following [Google's instructions to create a service account](https://cloud.google.com/docs/authentication/production#create_service_account). These instructions are partially duplicated below, with some screenshots for completeness.

Start by creating a build service account. Go to the "Create service account" page in the "IAM & Admin" API section, choose the appropriate project, and fill out the step 1 "Service account details". When you are done, click "Create and Continue".

![Step One of configuring a new Google Cloud Service account, with account name and description fields](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-6b8a0bf7ea67b718a7430539da16478aa9dd3565%2Fgoogle-cloud-build-1.png?alt=media\&token=3f25a3dc-c093-41e9-b7f6-6d7938bcca4c)

The creation steps should now ask you for a role to use in your build. The needs for each build are different; so examine your needs, and take care to grant the least privilege needed for your build. One reasonable starting point might be the [default Cloud Build service account permissions](https://cloud.google.com/build/docs/cloud-build-service-account#default_permissions_of_service_account).

![Step two of configuring a new Google Cloud Service account, with a chosen role selected](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-9bc9ad4c3d82bf1faeadb1ac1ad09fb0e82526b1%2Fgoogle-cloud-build-2.png?alt=media\&token=c015a76f-1fc2-4999-afad-67eb874a1cf4)

Click "Done". The console should navigate you to a list of service accounts within the project. At this point, the account should be created, but we still need to create an account key. To do this, click on the email address for this service account in the list.

![The Google Cloud list view of service accounts, with our new account highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-9f17636d754f996101781b0104755d60368b7b19%2Fgoogle-cloud-build-3.png?alt=media\&token=7c735c9c-f9e7-4314-b553-cb81c7f2f590)

Then select "Keys" from the top navigation.

![The top nav of the service account drilldown, with the keys tab highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-57f5282cc128d5afc6e15bda5519cc1504d2b402%2Fgoogle-cloud-build-4.png?alt=media\&token=78be8daa-4158-48b4-8f97-ba39c98f79b9)

Click "Add Key", and then "Create New Key". Choose "JSON" as the key format, and click create. This will download the key to your computer, and you should see it in the list of keys.

![The list view of available keys for a Google Cloud service account](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-333efab4fe36f79e2408247ad6d274315ca1b635%2Fgoogle-cloud-build-5.png?alt=media\&token=bab23c8e-a23c-420a-ade2-6f7257dbab92)

Stash the key in your secret management utility of choice. You'll need to make this key available to your build at runtime. For the rest of our example, we will be using Earthly's [Cloud Secrets](https://docs.earthly.dev/earthly-cloud/cloud-secrets).

Often, external secrets management requires some kind of bootstrapping secret (or additional integration) to allow you to access the rest of the secrets in your store. Earthly is no different. We will keep our `EARTHLY_TOKEN` in [Googles Secret Manager](https://cloud.google.com/build/docs/securing-builds/use-secrets) for ease of use.

{% hint style="danger" %}
**Note**

It is also possible to perform these steps via the CLI; the steps are [also detailed in Googles instructions](https://cloud.google.com/docs/authentication/production#command-line). It can also be automated using much of the same steps.
{% endhint %}

## Additional Notes

`earthly` misinterprets the Cloud Build environment as a terminal. To hide the ANSI color codes, set `NO_COLOR` to `1`.

## Example

{% hint style="danger" %}
**Note**

This example is not production ready, and is intended to showcase configuration needed to get Earthly off the ground. If you run into any issues, or need help, [don't hesitate to reach out](https://github.com/earthly/earthly/issues/new)!
{% endhint %}

You can find our [`cloudbuild.yaml`](https://github.com/earthly/ci-example-project/blob/main/cloudbuild.yaml) and the [`Earthfile`](https://github.com/earthly/ci-example-project/blob/main/Earthfile) used on GitHub.

Start by adding a new [Trigger](https://console.cloud.google.com/cloud-build/triggers). Triggers are the things that link changes in your source code with new instances of builds in Cloud Build. Start by clicking on "Create Trigger".

![The triggers page for a project, with "Create Trigger" highlighted.](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-ec0f92b14914a703efed1e7f3383c887c9b45575%2Fgoogle-cloud-build-6.png?alt=media\&token=989f56b9-ae77-4e68-89ab-0d9cad32707e)

Fill out the "Name", "Description", and "Event" sections for this trigger, as they make sense for your project. For our example (and for ease of testing) we will be using the "Manual Invocation" trigger here.

![Creating a trigger for Google Cloud Build, specifying a name, description, and trigger event](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-b59bb46f4c7f82908fc52ad6208aa1e97f98b597%2Fgoogle-cloud-build-7.png?alt=media\&token=bbbf5210-03d0-4b1a-8675-a1dec4f627c3)

Configure your source repository. If you do not see your desired repository in the drop down list, follow [Google's instructions to add it](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo).

![Creating a trigger for Google Cloud Build, specifying a repository and branch name](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-26f3379d5ee5efd5bcb4de90527e90bbcd129d48%2Fgoogle-cloud-build-8.png?alt=media\&token=aa1c81be-c19d-4706-819b-e9d117334bc7)

Finally, fill in the "Configuration" section. For Earthly, you can only use the "Cloud Build configuration file", as Earthly itself will *also* be running containers. Our example will also be using an embedded [`cloudbuild.yaml`](https://github.com/earthly/ci-example-project/blob/main/cloudbuild.yaml).

![Creating a trigger for Google Cloud Build, specifying the configuration, including cloudbuild location and configuration type](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-f645f6e9dcd5fd8f663709fc4d65eb975cbbfd1d%2Fgoogle-cloud-build-9.png?alt=media\&token=a86862a9-7b3e-4e1b-9fee-fe7007c9dff2)

Click "Done" and you will be navigated back to the Triggers list view. To test the build, click "Run" since we chose a manual trigger only:

![Google Cloud Build Trigger list, with the manual run button highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-396675a7d42eb1e6976876efc21cc53b84299209%2Fgoogle-cloud-build-10.png?alt=media\&token=18e5269b-a46c-4c91-a884-03bae967faa0)

Running this build will use the [`cloudbuild.yaml`](https://github.com/earthly/ci-example-project/blob/main/cloudbuild.yaml) file in our sample repository. This file is also a key part of the build, so lets break this down as well.

[The first step](https://github.com/earthly/ci-example-project/blob/ea44992b020b52cb5a46920d5d11d4b8389ce19d/cloudbuild.yaml#L2-L6) simply uses the [all-in-one Earthly image](https://hub.docker.com/r/earthly/earthly) to do a simple build.

```yaml
  - id: 'build'
    name: 'earthly/earthly:v0.5.24'
    args:
      - --allow-privileged
      - +docker
```

[The second step](https://github.com/earthly/ci-example-project/blob/ea44992b020b52cb5a46920d5d11d4b8389ce19d/cloudbuild.yaml#L8-L13) runs a sample, Google Cloud Build only example to show how you would use an external service account to do things that normally requires credentials.

```yaml
  - id: 'gcp-test'
    name: 'earthly/earthly:v0.5.24'
    args:
      - +gcp-cloudbuild
    secretEnv:
      - 'EARTHLY_TOKEN'
```

The secret environment variable bootstraps the Earthly secret store, and we can load it from Google's Secret Store like this:

```yaml
availableSecrets:
  secretManager:
  - versionName: projects/earthly-jupyterlab/secrets/EARTHLY_TOKEN/versions/2
    env: 'EARTHLY_TOKEN'
```

# GitLab CI/CD

This example uses [GitLab CI/CD](https://docs.gitlab.com/ee/ci/) to build the Earthly target `+build`.

```yml
# .gitlab-ci.yml

services:
  - docker:dind

variables:
  DOCKER_HOST: tcp://docker:2375
  FORCE_COLOR: 1
  EARTHLY_EXEC_CMD: "/bin/sh"

image: earthly/earthly:v0.6.30

before_script:
    - earthly bootstrap
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

earthly:
  stage: build
  script:
    - earthly --ci --push -P +build
```

A full example is available [on GitLab](https://gitlab.com/earthly-technologies/earthly-demo).

For a complete guide on CI integration see the [CI integration guide](https://docs.earthly.dev/ci-integration/overview).

# Woodpecker CI

This example uses [Woodpecker CI](https://woodpecker-ci.org/) to build the Earthly target `+build`.

## Configuration

The project needs to be [trusted](https://woodpecker-ci.org/docs/usage/project-settings#trusted) to grant the capabilities like mounting volumes (required for the docker socket). We also need to include the `earthly/earthly` image in the list of images that are allowed to run in [privileged mode](https://woodpecker-ci.org/docs/administration/server-config#woodpecker_escalate)

```yml
#.woodpecker.yml
pipeline:
  earthly:
    image: earthly/earthly:v0.6.30
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - FORCE_COLOR=1
      - EARTHLY_EXEC_CMD="/bin/sh" 
    secrets: [REGISTRY, REGISTRY_USER, REGISTRY_PASSWORD]
    commands:
     - docker login -u $${REGISTRY_USER} -p $${REGISTRY_PASSWORD} $${REGISTRY}
     - earthly bootstrap
     - earthly --ci --push -P +build
```

For a complete guide on CI integration see the [CI integration guide](https://docs.earthly.dev/ci-integration/overview).

# Overview

Earthly Cloud is a collection of features that enrich the Earthly experience via cloud-based services. These include:

* [Earthly Cloud Secrets](https://docs.earthly.dev/earthly-cloud/cloud-secrets): A secret management system that allows you to store secrets in a cloud-based service and use them across builds.
* [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites): Cloud-based Buildkit instances managed by the Earthly team.
* **Earthly CI** (coming soon): A cloud-based continuous integration / continuous delivery system that allows you to continuously build your code in the cloud.

## Getting started

### Creating an account

To get started with Earthly Cloud, you'll need to register an Earthly account. You can do so by visiting [Earthly CI](https://ci.earthly.dev), or by using the CLI as described below.

```bash
earthly account register --email <email>
```

An email will be sent to you containing a verification token. Next run:

```bash
earthly account register --email <email> --token <token>
```

This command will prompt you to set a password, and to optionally register a public-key for password-less authentication.

### Creating or joining an Earthly org

An Earthly org allows you to share projects, secrets, satellites and pipelines with colleagues. To create an Earthly org you can run:

```bash
earthly org create <org-name>
```

To invite another user to join your org, run:

```bash
earthly org invite /<org-name>/ <email>
```

Note the slashes around the org name. Also, please note that **the user must have an account on Earthly before they can be invited**. (This is a temporary limitation which will be addressed in the future.)

You can join an Earthly org by following the steps outlined in the invitation email sent to you by an Earthly admin.

# Cloud secrets

## Cloud Secrets

{% hint style="danger" %}
**Important**

This feature is currently in **Experimental** stage

* The feature may break, be changed drastically with no warning, or be removed altogether in future versions of Earthly.
* Check the [GitHub tracking issue](https://github.com/earthly/earthly/issues/575) for any known problems.
* Give us feedback on [Slack](https://earthly.dev/slack) in the `#cloud-secrets` channel.
  {% endhint %}

Earthly has the ability to use secure cloud-based storage for build secrets. This page goes through the basic setup and usage examples.

Cloud secrets can be used to share secrets between team members or across multiple computers and a CI systems.

### Introduction

This document covers the use of cloud-hosted secrets. It builds upon the understanding of [build arguments and locally-supplied secrets](https://docs.earthly.dev/docs/guides/build-args).

### Managing secrets

In order to be able to use cloud secrets, you need to first register an Earthly cloud account and create an Earthly org. Follow the steps in the [Earthly Cloud overview](https://github.com/earthly/earthly/blob/docs-0.6/docs/overview.md#getting-started) to get started.

#### Interacting with the private user secret store from the command line

Each user has a non-sharable private user space which can be referenced by `/user/...`; this can be thought of as your home directory. To view this workspace, try running:

```bash
earthly secrets ls
earthly secrets ls /user
```

Secrets are referenced by a path, and can contain up to 512 bytes.

#### Setting a value

To set a secret value, use the `secrets set` command:

```bash
earthly secrets set /user/my_key 'hello world'
```

#### Getting a value

To view a secret value, use the `secrets get` command:

```bash
earthly secrets ls /user
earthly secrets get /user/my_key
```

### Using cloud secrets in builds

Cloud secrets can be referenced in an Earthfile, in a similar way to [locally-defined secrets](https://docs.earthly.dev/docs/guides/build-args).

Consider the Earthfile:

```Dockerfile
FROM alpine:latest

build:
    RUN --secret MY_KEY=+secrets/user/my_key echo $MY_KEY
    SAVE IMAGE myimage:latest
```

The env variable `MY_KEY` will be set with the value stored under your private `/user/my_key` secret.

You can build it via:

```bash
earthly +build
```

{% hint style="info" %}

#### Naming of local and cloud-based secrets

The only difference between the naming of locally-supplied and cloud-based secrets is that cloud secrets will contain two or more slashes since all cloud secrets must start with a `+secrets/<user or organization>/` prefix, whereas locally-defined secrets will only start with the `+secrets/` suffix, followed by a single name which cannot contain slashes.
{% endhint %}

### Sharing secrets

To share secrets between teams, an organization must first be created:

```bash
earthly org create <org-name>
```

Then additional users can be invited into the organization:

```bash
earthly org invite /<org-name>/ <email>
```

By default this will grant the invited user read privileges to all keys under the organization. It's also possible to use the `--write` flag to grant write permission too. Additionally, the permissions can be set to lower paths.

#### Sharing example

Alice and Bob sign up for earthly accounts using <alice@example.com> and <bob@example.com> respectively:

```bash
earthly account register --email alice@example.com --token ...
earthly account register --email bob@example.com --token ...
```

Alice then creates an organization called hush-co:

```bash
earthly org create hush-co
```

Alice then creates a secret under the `project-zulu` sub directory:

```bash
earthly secrets set /hush-co/project-zulu/transponder-code peanut
```

Alice then grants Bob read permission on all of `project-zulu`:

```bash
earthly org invite /hush-co/project-zulu/ bob@example.com
```

Bob now has permission to everything under the `/hush-co/project-zulu/` directory. If he runs

```bash
earthly secrets ls /hush-co/
```

he will see:

```
/hush-co/project-zulu/transponder-code
```

However if Alice were to create any secrets outside of `project-zulu`, Bob would not be able to list or retrieve them.

### Using cloud secrets in CI

To reference secrets from a CI environment, you can make use of the password or ssh-key authentication referenced under the login/logout section, or you can generate an authentication token by running:

```bash
earthly account create-token [--write] <token-name>
```

This token can then be exported as

```bash
EARTHLY_TOKEN=...
```

Which will then force Earthly to use that token when accessing secrets. This is useful for cases where running an ssh-agent is impractical.

## Security Details

The Earthly command uses HTTPS to communicate with the cloud secrets server. The server encrypts all secrets using OpenPGP's implementation of AES256 before storing it in a database. We use industry-standard security practices for managing our encryption keys in the cloud. For more information see our [Security page](https://earthly.dev/security).

Secrets are presented to BuildKit in a similar fashion as [locally-supplied secrets](https://github.com/earthly/earthly/blob/docs-0.6/docs/cloud/build-args.md#storage-of-secrets): When BuildKit encounters a `RUN` command that requires a secret, the BuildKit daemon will request the secret from the earthly command-line process -- `earthly` will then make a request to earthly's cloud storage server (along with the auth token); once the server returns the secret, that secret will be passed to BuildKit.

## Feedback

The secrets store is still an experimental feature, we would love to hear feedback in our [Slack](https://earthly.dev/slack) community.

# Satellites

This feature is part of the Earthly Satellites paid plan.

{% hint style="danger" %}
**Important**

This feature is currently in **Beta** stage

* The feature may break or change significantly in future versions of Earthly.
* Give us feedback on
  * [Slack](https://earthly.dev/slack)
  * [GitHub issues](https://github.com/earthly/earthly/issues)
  * [Emailing support](mailto:support+satellite@earthly.dev)
    {% endhint %}

Earthly Satellites are [remote runner](https://docs.earthly.dev/docs/remote-runners) instances managed by the Earthly team. They allow you to perform builds in the cloud, while retaining cache between runs.

When using Earthly Satellites, even though the build executes remotely, the following pieces of functionality are still available:

* Build logs are streamed to your local machine in real-time, just as if you were running the build locally
* Outputs (images and artifacts) resulting from the build, if any, are transferred back to your local machine
* Commands under `LOCALLY` execute on your local machine
* Secrets available locally, including Docker/Podman credentials are passed to the satellite whenever needed by the build
* Any images to be pushed are pushed directly from the satellite, using any Docker/Podman credentials available on the local system.

![Satellite workflow](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-88377a6a131c29cdeddb74e992025c9c5e979ab3%2Fsatellite-workflow.png?alt=media\&token=74bece2d-d162-4916-8e8a-690a672a0abd)

Earthly Satellite instances come with their own cache volume. This means that performing builds repeatedly on the same satellite will result in faster builds. This can be especially useful when using Satellites from a sandboxed CI environment, where cache from previous builds would not otherwise be available. Below is a comparison with Earthly's [Shared remote cache features](https://docs.earthly.dev/docs/remote-caching).

| Cache characteristic                                         | Satellite      | Shared Cache                                         |
| ------------------------------------------------------------ | -------------- | ---------------------------------------------------- |
| Storage location                                             | Satellite      | A container registry of your choice                  |
| Proximity to compute                                         | ✅ Same machine | ❌ Performing upload/download is required             |
| Just works, no configuration necessary                       | ✅ Yes          | ❌ Requires experimentation with the various settings |
| Concurrent access                                            | ✅ Yes          | 🟡 Concurrent read access only                       |
| Retains entire cache of the build                            | ✅ Yes          | ❌ Usually no, due to prohibitive upload time         |
| Retains cache for multiple historical builds                 | ✅ Yes          | ❌ No, only one build retained                        |
| Cache mounts (`RUN --mount type=cache` and `CACHE`) included | ✅ Yes          | ❌ No                                                 |

## Benefits

Typical use cases for Earthly Satellites include:

* Speeding up CI builds in sandboxed CI environments such as GitHub Actions, GitLab, CircleCI, and others. Most CI build times are improved by a factor of 2-4X via Satellites.
* Executing builds on AMD64/Intel architecture natively when working from an Apple Silicon machine (Apple M1/M2).
* Sharing compute and cache with coworkers or with the CI.
* Benefiting from high-bandwidth internet access from the satellite, thus allowing for fast downloads of dependencies and fast pushes for deployments. This is particularly useful if operating from a location with slow internet.
* Using Earthly in environments where privileged access or docker-in-docker are not supported.

## Security

As builds often handle sensitive pieces of data, Satellites are designed with security in mind. Here are some of Earthly's security considerations:

* Satellite instances run in isolated VMs, with restricted local networking, and are only accessible by users you invite onto the platform.
* Network communication and data at rest is secured using industry state of the art practices.
* The cache is not shared between satellites.
* Secrets used as part of the build are only kept in-memory temporarily, unless they are part of the [Earthly Cloud Secrets storage](https://docs.earthly.dev/earthly-cloud/cloud-secrets), in which case they are encrypted at rest.
* In addition, Earthly is pursuing SOC 2 compliance. SOC 2 Type I ETA Fall 2022, SOC 2 Type II ETA Summer 2023.
* To read more about Earthly's security practices please see the [Security page](https://earthly.dev/security).

## Getting started

### 1. Register an account and create an org

Follow the steps in the [Earthly Cloud overview](https://docs.earthly.dev/overview#getting-started) to register an account and create an org.

### 2. Purchase a Satellites Plan

Satellites are now a paid feature and require a valid subscription to begin using. The subscription includes a 14-day free trial which can be canceled before any payment is made. Visit the [pricing page](https://earthly.dev/pricing) for more billing details.

[**Click here to start your subscription**](https://buy.stripe.com/8wM9Es4BT4Vvb4YbIJ)

Once you've submitted your details on the checkout page, you will receive an email with further instructions. Please reply or [send us an email](mailto:support+satellite@earthly.dev) with your org name from step 1 in order for us to activate the Satellites feature on your account.

### 3. Ensure that you have the latest version of Earthly

Because this feature is under heavy development right now, it is very important that you use the latest version of Earthly available.

**On Linux**, simply repeat the [installation steps](https://earthly.dev/get-earthly) to upgrade.

**On Mac**, you can perform:

```bash
brew update
brew upgrade earthly/earthly/earthly
```

### 4. Launch a new satellite

To launch a new satellite, run:

```bash
earthly sat launch <satellite-name>
```

The Satellite name can be any arbitrary string.

If you are part of multiple Earthly organizations, you may have to specify the org name under which you would like to launch the satellite:

```bash
earthly sat --org <org-name> launch <satellite-name>
```

Once the satellite is created it will be automatically selected for use as part of your builds. The selection takes place by Earthly adding some information in your Earthly config file (usually located under `~/.earthly/config.yml`).

### 5. Run a build

To execute a build using the newly created satellite, simply run Earthly like you always have. For example:

```bash
earthly +my-target
```

Because the satellite has been automatically selected in the step above, the build will be executed on it.

To go back to using your local machine for builds, you may "unselect" the satellite by running:

```bash
earthly sat unselect
```

You can always go back to using the satellite by running:

```bash
earthly sat select <satellite-name>
```

Or, you can use a satellite only for a specific build, even if it is not selected:

```bash
earthly --sat <satellite-name> +my-target
```

Conversely, if a satellite is currently selected, but you want to execute a build on your local machine, you can use the `--no-sat` flag:

```bash
earthly --no-sat +my-target
```

For more information on using satellites, see the [Using satellites page](https://docs.earthly.dev/earthly-cloud/satellites/using).

### 6. Invite your team

A final optional step is to invite your team to use the satellite. This can be done by running:

```bash
earthly org invite /<org-name>/ <email>
```

Note the slashes around the org name. Also, please note that **the user must have an account on Earthly before they can be invited**. (This is a temporary limitation which will be addressed in the future.)

Once a user has been invited, you can forward them a link to the page [Using Satellites](https://docs.earthly.dev/earthly-cloud/satellites/using) for them to get started.

## Managing Satellites

For more information on managing satellites, see the [Managing Satellites page](https://docs.earthly.dev/earthly-cloud/satellites/managing).

## Satellite specs

Satellites are currently only available in one size, and it has the following specs:

* 4 CPUs
* 16 GB of RAM
* 90 GB of cache storage
* 5 Gib internet bandwidth

## Using Satellites in CI

A key benefit of using satellites in a CI environment is that the cache is shared between runs. This results in significant speedups in CIs that would otherwise have to start from scratch each time.

{% hint style="danger" %}
**Note**

If a satellite is shared between multiple CI pipelines, it is possible that it becomes overloaded by too many parallel builds. For best performance, you can create a dedicated satellite for each CI pipeline.
{% endhint %}

To get started with using Earthly Satellites in CI, you can create a login token for access.

First, run

```bash
earthly account create-token <token-name>
```

to create your login token.

Copy and paste the value into an environment variable called `EARTHLY_TOKEN` in your CI environment.

Then as part of your CI script, just run

```bash
earthly sat select <satellite-name>
```

before running your Earthly targets.

## Known limitations

* Satellites currently require a manual re-launch in order to get updated to the latest version available.

  ```bash
  earthly sat rm <satellite-name>
  earthly sat launch <satellite-name>
  ```

* The output phase (the phase in which a satellite outputs build results back to the local machine) is slower than it could be. To work around this issue, you can make use of the `--no-output` flag (assuming that local outputs are not needed). You can even use `--no-output` in conjunction with `--push`. We are working on ways in which local outputs can be synchronized more intelligently such that only a diff is transferred over the network.
* A user can only be invited into an Earthly org if they already have a user account. This is a temporary limitation which will be addressed in the future.
* Satellites in conjunction with `--save-inline-cache` or `--use-inline-cache` is currently unsupported. When using `--ci`, the options `--save-inline-cache` and `--use-inline-cache` will not be implicitly enabled when using Satellites.

If you run into any issues please let us know either via [Slack](https://earthly.dev/slack), [GitHub issues](https://github.com/earthly/earthly/issues) or by [emailing support](mailto:support+satellite@earthly.dev).

# Managing Satellites

This feature is part of the Earthly Satellites paid plan.

{% hint style="danger" %}
**Important**

This feature is currently in **Beta** stage

* The feature may break or change significantly in future versions of Earthly.
* Give us feedback on
  * [Slack](https://earthly.dev/slack)
  * [GitHub issues](https://github.com/earthly/earthly/issues)
  * [Emailing support](mailto:support+satellite@earthly.dev)
    {% endhint %}

This page describes how to manage [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites).

## Prerequisites

In order to manage Earthly Satellites, you must have an Earthly account and an Earthly organization, and you must request access to the Satellite private beta program. For more information, see the [Earthly Cloud overview](https://docs.earthly.dev/earthly-cloud/overview) and the [Satellites page](https://docs.earthly.dev/earthly-cloud/satellites).

## Managing Satellites

### Launching and removing satellites

To launch a new satellite, run:

```bash
earthly sat launch <satellite-name>
```

The Satellite name can be any arbitrary string.

If you are part of multiple Earthly organizations, you may have to specify the org name under which you would like to launch the satellite:

```bash
earthly sat --org <org-name> launch <satellite-name>
```

Once the satellite is created it will be automatically selected for use as part of your builds. The selection takes place by Earthly adding some information in your Earthly config file (usually located under `~/.earthly/config.yml`).

To remove a satellite, you can run:

```bash
earthly sat rm <satellite-name>
```

### Listing satellites

To list the satellites available in your organization, run:

```bash
earthly sat ls
```

### Selecting a satellite

Selecting a satellite causes Earthly to use that satellite for any builds from that point onwards.

To select a satellite for use, run:

```bash
earthly sat select <satellite-name>
```

### Unselecting a satellite

Unselecting a satellite will cause Earthly to run builds locally from that point onwards.

To unselect a satellite, run:

```bash
earthly sat unselect
```

### Checking status of a satellite

Checking the status of a satellite allows you to view information about a satellite's current state, including whether it is being used right now, how much cache space has been used, version information and other information.

To check the status of a satellite, you can run:

```bash
earthly sat inspect <satellite-name>
```

Here is some example output of an inspect command:

```
Connecting to core-test...
Version github.com/earthly/buildkit v0.6.21 7a6f9e1ab2a3a3ddec5f9e612ef390af218a32bd
Platforms: linux/amd64 (native) linux/amd64/v2 linux/amd64/v3 linux/amd64/v4 linux/arm64 linux/riscv64 linux/ppc64le linux/s390x linux/386 linux/mips64le linux/mips64 linux/arm/v7 linux/arm/v6
Utilization: 0 other builds, 0/12 op load
GC stats: 9.0 GB cache, avg GC duration 275ms, all-time GC duration 2.754s, last GC duration 0s, last cleared 0 B
Instance state: Operational
Currently selected: No
```

### Clearing cache

To clear the cache of a satellite, run the following while a satellite is selected:

```bash
earthly prune -a
```

### Upgrading a satellite

Currently, satellites do not have an auto-update mechanism built in. In order to get a newer version of a satellite, you need to manually remove and re-launch the satellite. Note that this operation resets the cache.

```bash
earthly sat rm <satellite-name>
earthly sat launch <satellite-name>
```

The newly launched satellite will always get the latest version available.

### Managing instance state

To save costs, satellites automatically enter a **sleep** state after 30 min of inactivity. While a satellite is asleep, you are not billed for any compute minutes.

The satellite will automatically **wake up** when a new build is started while it's in a sleep state. This is visible during the `Init` phase of the Earthly log.

If you want more fine-grain control over your Satellite's state, you can also manually put it to sleep using the command:

```bash
earthly sat sleep <satellite-name>
```

Similarly, a Satellite can be manually woken up using:

```bash
earthly sat wake <satellite-name>
```

Note that the [`inspect`](#checking-status-of-a-satellite) command will show you if a Satellite is currently awake or asleep.

### Inviting a user to use a satellite

Currently, all users who are part of an organization are allowed to use any satellite in the organization. To invite another user to join your org, run:

```bash
earthly org invite /<org-name>/ <email>
```

Note the slashes around the org name. Also, please note that **the user must have an account on Earthly before they can be invited**. (This is a temporary limitation which will be addressed in the future.)

Once a user has been invited, you can forward them a link to the page [Using Satellites](https://docs.earthly.dev/earthly-cloud/satellites/using) for them to get started.

### Satellite IP address

The source IP address of the satellite for all internet traffic is `35.160.176.56`. This can be used for granting access to private resources or to production environments.

# Using Satellites

This feature is part of the Earthly Satellites paid plan.

{% hint style="danger" %}
**Important**

This feature is currently in **Beta** stage

* The feature may break or change significantly in future versions of Earthly.
* Give us feedback on
  * [Slack](https://earthly.dev/slack)
  * [GitHub issues](https://github.com/earthly/earthly/issues)
  * [Emailing support](mailto:support+satellite@earthly.dev)
    {% endhint %}

This page describes how to use [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites).

## Prerequisites

In order to use Earthly Satellites, you must have an Earthly account and you must be a member of an Earthly organization. For more information, see the [Earthly Cloud overview](https://docs.earthly.dev/earthly-cloud/overview) and the [Satellites page](https://docs.earthly.dev/earthly-cloud/satellites).

If you are new to Earthly or to Earthly Cloud, you must:

* [Download and Install Earthly](https://earthly.dev/get-earthly). As Earthly Satellites is under active development, it is strongly recommended that you ensure that you have the very latest version of Earthly installed.

  **On Linux**, simply repeat the [installation steps](https://earthly.dev/get-earthly) to upgrade to the latest version of Earthly, if you installed Earthly some time ago.

  **On Mac**, you can perform:

  ```bash
  brew update
  brew upgrade earthly/earthly/earthly
  ```

* Create an account by visiting the [Earthly CI website](https://ci.earthly.dev/) to log in with GitHub or by using `earthly account register --email <email>` in your terminal.
* Either [create an Earthly organization](https://docs.earthly.dev/earthly-cloud/overview), or ask your Earthly admin to add you to an existing organization. In order to be added to an existing Earthly organization you need to first create an Earthly account as described above. To verify that you are part of an organization you can run:

  ```bash
  earthly org ls
  ```

  You should see an output similar to:

  ```
  /<org-name>/  member
  ```

## Background

Earthly Satellites allow Earthly to execute builds in the cloud seamlessly. You execute build commands in the terminal, like you always have (for example, `earthly +build`), and Earthly takes care of running the build in the cloud in real time, instead of your local machine.

It uploads parts of your working directory, passes along any secrets, executes the build in the cloud while streaming the build log in real-time back to you, and then downloads the resulting build images and artifacts back to your computer.

For more information about how Earthly Satellites work, see the [Satellites page](https://docs.earthly.dev/earthly-cloud/satellites).

## Using satellites

When you are added to an Earthly organization, you get access to its satellites. To view the satellites currently available in the organization, you can run:

```bash
earthly sat ls
```

If you are part of multiple organizations, you may need to specify the organization name too:

```bash
earthly sat --org <org-name> ls
```

### Selecting a satellite

In order to start using satellites, you can select one for use. Selecting a satellite causes Earthly to use that satellite for any builds from that point onwards.

```bash
earthly sat select <satellite-name>
```

Any build performed after selecting a satellite will be performed in the cloud on that satellite. You will notice that the output of the build contains information about the satellite that is being used:

```
$ earthly +build

 1. Init 🚀
————————————————————————————————————————————————————————————————————————————————

Note: the interactive debugger, interactive RUN commands, and inline caching do not yet work on Earthly Satellites.

The following feature flags are recommended for use with Satellites and will be auto-enabled:
  --new-platform, --use-registry-for-with-docker

           satellite | Connecting to core-test...
           satellite | ...Done
           satellite | Version github.com/earthly/buildkit v0.6.21 7a6f9e1ab2a3a3ddec5f9e612ef390af218a32bd
           satellite | Info: Buildkit version (v0.6.21) is different from Earthly version (prerelease)
           satellite | Platforms: linux/amd64 (native) linux/amd64/v2 linux/amd64/v3 linux/amd64/v4 linux/arm64 linux/riscv64 linux/ppc64le linux/s390x linux/386 linux/mips64le linux/mips64 linux/arm/v7 linux/arm/v6
           satellite | Utilization: 0 other builds, 0/12 op load
           satellite | GC stats: 9.0 GB cache, avg GC duration 275ms, all-time GC duration 2.754s, last GC duration 0s, last cleared 0 B

...
```

To go back to using your local machine for builds, instead of the satellite, you can unselect the satellite by running:

```bash
earthly sat unselect
```

### Specifying a satellite for one build only

If a satellite is not currently selected, you can still use it for a specific build by using the `--sat` flag.

```bash
earthly --sat <satellite-name> +build
```

Conversely, if a satellite is currently selected, you can choose to use the local machine for a specific build using the `--no-sat` flag.

```bash
earthly --no-sat +build
```

### Managing performance

As satellites run the execution in the cloud, behind the scenes, they require upload of the current directory contents that may be needed as part of the build, and download of the results of the build. This is performed automatically by Earthly, however, if the file transfers are large and/or if the network bandwidth is low, the performance impact can be noticeable.

Oftentimes, you will find that running a build with the flag `--no-output` executes significantly faster. This flag disables downloading the build results from the satellite at the end of a build.

The `--no-output` flag can still be combined with `--push`, thus allowing Earthly Satellites to be used as a highly performant deployment tool.

# Introduction

Earthly is a super simple CI/CD framework that gives you repeatable builds that you write once and run anywhere; has a simple, instantly recognizable syntax; and works with every language, framework, and build tool. With Earthly, you can create Docker images and build artifacts (e.g. binaries, packages, and arbitrary files).

Earthly can run locally or on top of popular CI systems – such as [Jenkins](https://docs.earthly.dev/ci-integration/vendor-specific-guides/jenkins), [CircleCI](https://docs.earthly.dev/ci-integration/vendor-specific-guides/circle-integration), [GitHub Actions](https://docs.earthly.dev/ci-integration/vendor-specific-guides/gh-actions-integration), [AWS CodeBuild](https://docs.earthly.dev/ci-integration/vendor-specific-guides/codebuild-integration), [Google Cloud Build](https://docs.earthly.dev/ci-integration/vendor-specific-guides/google-cloud-build), and [GitLab CI/CD](https://docs.earthly.dev/ci-integration/vendor-specific-guides/gitlab-integration)). It typically acts as the layer between language-specific tooling (such as maven, gradle, npm, pip, and go build) and the CI build spec.

![Earthly fits between language-specific tooling and the CI](https://3102854999-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fyi347RZ02JXdgz9BJx5u%2Fuploads%2Fgit-blob-d10638e4183adfdc7fdff0f61f7aed2d2c055c99%2Fintegration-diagram-v2.png?alt=media)

Earthly's key features/benefits are:

* **🔁 Repeatable Builds** Earthly runs all builds in containers, making them self-contained, isolated, repeatable, and portable. When you write a build, you know it will execute correctly no matter where it runs – your laptop, a colleague’s laptop, or any CI. You don’t have to configure language-specific tooling, install additional dependencies, or complicate your build scripts to ensure they are compatible with different OSs. Earthly gives you consistent, repeatable builds regardless of where they run.
* **❤️ Super Simple**\
  Earthly’s syntax is easy to write and understand. Most engineers can read an Earthfile instantly, without prior knowledge of Earthly. We combined some of the best ideas from Dockerfiles and Makefiles into one specification *– like Dockerfile and Makefile had a baby*.
* **🛠 Compatible with Every Language, Framework, and Build Tool**\
  One of the key principles of Earthly is that the best build tooling for a specific language is built by the community of that language itself. Earthly does not intend to replace any language-specific build tooling, but rather to leverage and augment them. Earthly works with the compilers and build tools you use. If it runs on Linux, it runs on Earthly. And you don’t have to rewrite your existing builds or replace your `package.json`, `go.mod`, `build.gradle`, or `Cargo.toml` files. You can use Earthly as a wrapper around your existing tooling and still get Earthly’s repeatable builds, parallel execution, and build caching.
* **🏘 Great for Monorepos and Polyrepos**\
  Earthly is great for both [monorepos](https://github.com/earthly/earthly/tree/main/examples/monorepo) and [polyrepos](https://github.com/earthly/earthly/tree/main/examples/multirepo). You can split your build logic across multiple Earthfiles, placing some deeper inside the directory structure or even in other repositories. Referencing targets from other Earthfiles is easy regardless of where they are stored. So you can organize your build logic however makes the most sense for your project.
* **💨 Fast Builds**\
  Earthly automatically executes build targets in parallel and makes maximum use of cache. This makes builds fast. Earthly also has powerful shared caching capabilities that speed up builds frequently run across a team or in sandboxed environments, such as Earthly Satellites, GitHub Actions, or your CI.\
  \
  If your build has multiple steps, Earthly will:
  1. Build a directed acyclic graph (DAG).
  2. Isolate execution of each step.
  3. Run independent steps in parallel.
  4. Cache results for future use.
* **♻️ Reuse, Don't Repeat**\
  Never have to write the same code in multiple builds again. With Earthly, you can reuse targets, artifacts, and images across multiple Earthfiles, even ones in other repositories, in a single line. Earthly is cache-aware, based on the individual hashes of each file, and has shared caching capabilities. So you can create a vast and efficient build hierarchy that only executes the minimum required steps.

## Earthly Cloud

Earthly Cloud is a cloud-based build automation platform that allows you to run your Earthly builds in the cloud, and is compatible with any CI. Earthly Cloud gives teams repeatable pipelines that run exactly the same in CI as on your laptop; has an automatic and instantly available build cache that makes builds faster; and is super simple to use.

Earthly is better when you're logged in to Earthly Cloud, and Earthly Cloud has a generous free tier that includes additional capabilities like:

* Sharing cache with your team
* Remote build runners
* Shared logs
* Shared secrets

To get started, visit the [Earthly Cloud sign up](https://cloud.earthly.dev/login) page.

## Installation

The best way to install Earthly is by [visiting Earthly Cloud and signing up for free](https://cloud.earthly.dev/login).

If you prefer not to create an online account, you can also install and use Earthly locally without an account. See the [installation instructions](https://earthly.dev/get-earthly).

For a full list of installation options see the [alternative installation page](https://docs.earthly.dev/docs/misc/alt-installation).

## Getting started

If you are new to Earthly, check out the [Basics page](https://docs.earthly.dev/basics), to get started.

A high-level overview is available on [the Earthly GitHub page](https://github.com/earthly/earthly).

## Quick Links

* [Earthly GitHub page](https://github.com/earthly/earthly)
* [Earthly Cloud Login](https://cloud.earthly.dev/login)
* [Earthly basics](https://docs.earthly.dev/basics)
* [Earthfile reference](https://docs.earthly.dev/docs/earthfile)
* [Earthly command reference](https://docs.earthly.dev/docs/earthly-command)
* [Configuration reference](https://docs.earthly.dev/docs/earthly-config)
* [Earthfile examples](https://docs.earthly.dev/docs/examples)
* [Best practices](https://docs.earthly.dev/docs/guides/best-practices)
* [Earthly Cloud documentation](https://docs.earthly.dev/earthly-cloud/overview)

# Install Earthly

## Log In and Install

To install the Earthly CLI on your machine, [head over to Earthly Cloud and get started for free](https://cloud.earthly.dev/login).

The logged-in experience gives you access to the following additional features:

* Logs sharing
* [Earthly Cloud Secrets](https://docs.earthly.dev/earthly-cloud/cloud-secrets)
* [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites) (6,000 minutes/month free)

## Install without Logging In

If you prefer to install Earthly without logging in, head over to the [Get Earthly page](https://earthly.dev/get-earthly).

# Learn the basics

Earthly is a build automation tool that uses docker containers to enforce build repeatability. Earthly is meant to be run on your local system and in your CI. Earthly's implicit caching and parallelism will make your builds repeatable and fast.

This tutorial will walk you through a basic example of using Earthly.

## Earthly is better logged in

A better, interactive version of this tutorial is available in Earthly Cloud. Get started with Earthly Cloud for free by visiting the [sign up](https://cloud.earthly.dev/login) page.

## Table of Contents

* **Introduction** <-- You are here.
* [Part 1: A simple Earthfile](https://docs.earthly.dev/basics/part-1-a-simple-earthfile)
* [Part 2: Outputs](https://docs.earthly.dev/basics/part-2-outputs)
* [Part 3: Adding dependencies With Caching](https://docs.earthly.dev/basics/part-3-adding-dependencies-with-caching)
* [Part 4: Args](https://docs.earthly.dev/basics/part-4-args)
* [Part 5: Importing](https://docs.earthly.dev/basics/part-5-importing)
* [Part 6: Using Docker In Earthly](https://docs.earthly.dev/basics/part-6-using-docker-with-earthly)
* [Part 7: Using remote runners](https://docs.earthly.dev/basics/part-7-using-remote-runners)
* [Part 8: Using Earthly in CI](https://docs.earthly.dev/basics/part-8a-using-earthly-in-your-current-ci)
* [Final words](https://docs.earthly.dev/basics/final-words)

## Installation

We recommend you install Earthly on your computer, so you can follow along and try the examples. See the [installation instructions](https://earthly.dev/get-earthly).

## Questions & Feedback

If you have any questions, feedback or suggestions for Earthly or this tutorial feel free to reach out to us on our [Slack community](https://earthly.dev/slack) or open a [GitHub issue](https://github.com/earthly/earthly/issues). Earthly is free and open and we love and appreciate feedback and contributions from the community!

## Get Started with Earthly

We will start the first lesson with a simple Earthfile.

👉 [Part 1: A simple Earthfile](https://docs.earthly.dev/basics/part-1-a-simple-earthfile)

# Part 1: A simple Earthfile

Below you'll find a simple example of an Earthfile. All the magic of Earthly happens in the Earthfile, which you may notice is very similar to a Dockerfile. This is an intentional design decision. Existing Dockerfiles can easily be ported to Earthly by copying them to an Earthfile and tweaking them slightly.

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

Throughout this tutorial, we'll build up this example Earthfile from scratch and then add even more to it. By the end you'll have a better grasp of how Earthly works and the power and repeatability it can bring to your build process.

This tutorial focuses on using Earthly with a Go project, but you can find examples of Earthfiles for [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) at the bottom of each page.

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part1/part1 ./part1
```

### Creating Your First Earthfile

We'll slowly build up to the Earthfile we have above. Let's start with these first three lines.

`./tutorial/Earthfile`

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir
```

And some simple Hello World code in a `main.go`.

```go
package main

import "fmt"

func main() {
 fmt.Println("hello world")
}
```

Earthfiles are always named Earthfile, regardless of their location in the codebase. The Earthfile starts off with a version definition. This will tell Earthly which features to enable and which ones not to so that the build script maintains compatibility over time, even if Earthly itself is updated.

The first commands in the file are part of the `base` target and are implicitly inherited by all other targets. Targets are just sets of instructions we can call on from within the Earthfile, or when we run Earthly at the command line. Targets need an environment to run in. These environments come in the form of Docker images. In this case we are saying that all the instructions in our Earthfile will use `golang:1.15-alpine3.13`, [unless we specify otherwise](#target-environments). (More on this in a bit.)

Lastly, we change our working directory to `/go-workdir`.

### Creating Your First Targets

Earthly aims to replace Dockerfile, makefile, bash scripts and more. We can take all the setup, configuration and build steps we'd normally define in those files and put them in our Earthfile in the form of `targets`.

Let's start by defining a target to build our simple Go app. **When we run Earthly, we can tell it to execute a target by passing a plus sign (+) and then the target name.** So we'll be able to run our `build` target with `earthly +build`. More on this in the [Running the Build](#running-the-build) section.

Let's start by breaking down our first target.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example
```

The first thing we do is copy our `main.go` from the **build context** (the directory where the Earthfile resides) to the **build environment** (the containerized environment where Earthly commands are run).

Next, we run a go build command against the previously copied `main.go` file.

Finally, we save the output of the build command as an artifact. The syntax for `SAVE ARTIFACT` defaults the destination path to `/` - so our artifact will be called `/example` (it can be later referenced as `+build/example`). If we wanted to save it at a different path, we could use `SAVE ARTIFACT output/example /some/path/to/example` and refer to it later as `+build/some/path/to/example`.

Now let's create a new target called `+docker`.

```Dockerfile
docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

Here we copy the artifact `/example` produced by another target, `+build`, to the current directory within the build environment. Again this will be the working directory we set up in the `base` target at the beginning of the file. Lastly, we set the entrypoint for the resulting docker image, and then save the image.

You may notice the command `COPY +build/... ...`, which has an unfamiliar form if you're coming from Docker. This is a special type of `COPY`, which can be used to pass artifacts from one target to another. In this case, the target `build` (referenced as `+build`) produces an artifact, which has been declared with `SAVE ARTIFACT`, and the target `docker` copies that artifact in its build environment.

With Earthly you have the ability to pass such artifacts or images between targets within the same Earthfile, but also across different Earthfiles across directories or even across repositories. To read more about this, see the [importing guide](https://docs.earthly.dev/docs/guides/importing) or jump to [part 5](https://docs.earthly.dev/basics/part-5-importing) of this guide.

Lastly, we save the current state as a docker image, which will have the docker tag `go-example:latest`. This image is only made available to the host's docker if the entire build succeeds.

### Target Environments

Notice how we already had Go installed for both our `+build` and `+docker` targets. This is because targets inherit from the base target which for us was the `FROM golang:1.15-alpine3.13` that we set up at the top of the file. But it's worth noting that targets can define their own environments. For example:

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

npm:
    FROM node:12-alpine3.12
    WORKDIR /src
    RUN npm install
    COPY assets/ .
    RUN npm test
```

In this example, the `+build` target does not have a `FROM`, so it inherits from the base target, `golang:1.15-alpine3.13`.

The target `+npm`, on the other hand, specifies its own environment with the `FROM`command and so will run inside of a `node:12-alpine3.12` container.

### Running the build

In the example `Earthfile` we have defined two explicit targets: `+build` and `+docker`. **We can tell Earthly to execute a target by passing typing a plus sign (+) followed by the target name.** In this case our docker target calls on our build target, so we can run both with:

```bash
earthly +docker
```

The output might look like this:

![Earthly build output](https://3102854999-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fyi347RZ02JXdgz9BJx5u%2Fuploads%2Fgit-blob-cf08377408d70ee4b3c931c21a937b4673901915%2Fgo-example.png?alt=media)

Notice how to the left of `|`, within the output, we can see some targets like `+base`, `+build` and `+docker` . Notice how the output is interleaved between `+docker` and `+build`. This is because the system executes independent build steps in parallel. The reason this is possible effortlessly is because only very few things are shared between the builds of the recipes and those things are declared and obvious. The rest is completely isolated.

In addition, notice how even though the base is used as part of both `build` and `docker`, it is only executed once. This is because the system deduplicates execution, where possible.

Furthermore, the fact that the `docker` target depends on the `build` target is visible within the command `COPY +build/...`. Through this command, the system knows that it also needs to build the target `+build`, in order to satisfy the dependency on the artifact.

Finally, notice how the output of the build (the docker image and the files) are only written after the build is declared a success. This is due to another isolation principle of Earthly: a build either succeeds completely or it fails altogether.

Once the build has executed, we can run the resulting docker image to try it out:

```
docker run --rm go-example:latest

# or podman
podman run --rm go-example:latest
```

#### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part1/part1 ./part1
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

build:
    # In JS, there's nothing to build in this simple form.
    # The source is also the artifact used in production.
    COPY src/index.js .
    SAVE ARTIFACT index.js /dist/index.js

docker:
    COPY +build/dist dist
    ENTRYPOINT ["node", "./dist/index.js"]
    SAVE IMAGE js-example:latest
```

The code of the app might look like this

`./src/index.js`

```js
console.log("hello world");
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part1/part1 ./part1
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    COPY build.gradle ./
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin /bin
    SAVE ARTIFACT build/install/java-example/lib /lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:latest
```

The code of the app might look like this

`./src/main/java/hello/HelloWorld.java`

```java

package hello;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

`./build.gradle`

```groovy
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'hello.HelloWorld'

jar {
    baseName = 'hello-world'
    version = '0.0.1'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 1 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part1) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part1/part1 ./part1
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM python:3
WORKDIR /code

build:
     # In Python, there's nothing to build.
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +build/src src
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:latest
```

The code of the app might look like this

`./src/hello.py`

```python
print("hello world")
```

</details>

# Part 2: Outputs

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part2) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part2/part2 ./part2
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Not All Targets Produce Output

Targets have the ability to produce output outside of the build environment. You can save files and docker images to your local machine or push them to remote repositories. Targets can also run commands that affect the local environment outside of the build, such as running database migrations, but not all targets produce output. Let's take a look at which commands produce output and how to use them.

### Saving Files

We've already seen how the command [SAVE ARTIFACT](https://docs.earthly.dev/docs/earthfile#save-artifact) copies a file or directory from the build environment into the target's artifact environment.

This gives us the ability to copy files between targets, **but it does not allow us to save any files to our local machine.**

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example

docker:
    #  COPY command copies files from the +build target
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

In order to **save the file locally** , we need to add `AS LOCAL` to the command.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

If we run this example with `earthly +build`, we'll see a `local-output` directory show up locally with a `go-example` file inside of it.

### Saving Docker Images

Saving Docker images to your local machine is easy with the `SAVE IMAGE` command.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

In this example, running `earthly +docker` will save an image named `go-example` with the tag `latest`.

```bash
~$ earthly +docker
...
~$ docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
go-example          latest    08b9f749023d   19 seconds ago   297MB

# or podman
~$ podman image ls
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
go-example          latest    08b9f749023d   19 seconds ago   297MB
```

**NOTE**

If we run a target as a reference in `FROM` or `COPY`, **outputs will not be produced**. Take this Earthfile for example.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

In this case, running `earthly +docker` will not produce any output. In other words, you will not have a `local-output/go-example` written locally, but running `earthly +build` will still produce output as expected.

The exception to this rule is the `BUILD` command. If you want to use `COPY` or `FROM` and still have Earthly create `local-output/go-example` locally, you'll need to use the `BUILD` command to do so.

```Dockerfile
build:
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    BUILD +build
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

Running `earthly +docker` in this case will now output `local-output/go-example` locally.

### The Push Flag

#### Docker Images

In addition to saving files and images locally, we can also push them to remote repositories.

```Dockerfile
docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE --push go-example:latest
```

Note that adding the `--push` flag to `SAVE IMAGE` is not enough, we'll also need to invoke push when we run earthly. `earthly --push +docker`.

**External Changes**

You can also use `--push` as part of a `RUN` command to define commands that have an effect external to the build. These kinds of effects are only allowed to take place if the entire build succeeds.

This allows you to push to remote repositories.

```Dockerfile
release:
    RUN --push --secret GITHUB_TOKEN=GH_TOKEN github-release upload
```

```bash
earthly --push +release
```

But also allows you to do things like run database migrations.

```Dockerfile
migrate:
    FROM +build
    RUN --push bundle exec rails db:migrate
```

```bash
earthly --push +migrate
```

Or apply terraform changes

```Dockerfile
apply:
    RUN --push terraform apply -auto-approve
```

```bash
earthly --push +apply
```

**NOTE**

Just like saving files, any command that uses `--push` **will only produce output if called directly**, `earthly --push +target-with-push` **or via a** `BUILD` command. Calling a target via `FROM` or `COPY` will not invoke `--push`.

#### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part2) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part2/part2 ./part2
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

build:
    # In JS, there's nothing to build in this simple form.
    # The source is also the artifact used in production.
    COPY src/index.js .
    SAVE ARTIFACT index.js /dist/index.js AS LOCAL ./dist/index.js

docker:
    COPY +build/dist dist
    ENTRYPOINT ["node", "./dist/index.js"]
    SAVE IMAGE js-example:latest
```

The code of the app might look like this

`./src/index.js`

```js
console.log("hello world");
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part2) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part2/part2 ./part2
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    COPY build.gradle ./
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin /bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib /lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:latest
```

The code of the app might look like this

`./src/main/java/hello/HelloWorld.java`

```java

package hello;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

`./build.gradle`

```groovy
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'hello.HelloWorld'

jar {
    baseName = 'hello-world'
    version = '0.0.1'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 2 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part2) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part2/part2 ./part2
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM python:3
WORKDIR /code

build:
     # In Python, there's nothing to build.
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +build/src src
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE --push python-example:latest
```

The code of the app might look like this

`./src/hello.py`

```python
print("hello world")
```

</details>

# Part 3: Adding dependencies With Caching

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part3/part3 ./part3
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Dependencies

Now let's imagine that we want to add some dependencies to our app. In Go, that means adding `go.mod` and `go.sum`.

`./go.mod`

```go.mod
module github.com/earthly/earthly/examples/go

go 1.13

require github.com/sirupsen/logrus v1.5.0
```

`./go.sum` (empty)

```go.sum
```

The code of the app might look like this

`./main.go`

```go
package main

import "github.com/sirupsen/logrus"

func main() {
 logrus.Info("hello world")
}
```

Now we can update our Earthfile to copy in the `go.mod` and `go.sum`.

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    COPY go.mod go.sum .
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

This works, but it is inefficient because we have not made proper use of caching. In the current setup, when a file changes, the corresponding `COPY` command is re-executed without cache, causing all commands after it to also re-execute without cache.

#### Caching

If, however, we could first download the dependencies and only afterwards copy and build the code, then the cache would be reused every time we changed the code.

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    # Download deps before copying code.
    COPY go.mod go.sum .
    RUN go mod download
    # Copy and build code.
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

For a primer into Dockerfile layer caching see [this article](https://pythonspeed.com/articles/docker-caching-model/). The same principles apply to Earthfiles.

### Reusing Dependencies

In some cases, the dependencies might be used in more than one build target. For this use case, we might want to separate dependency downloading and reuse it. For this reason, let's consider breaking this out into a separate target called `+deps`. We can then inherit from `+deps` by using the command `FROM +deps`.

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    # Output these back in case go mod download changes them.
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum

build:
    FROM +deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

docker:
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:latest
```

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part3/part3 ./part3
```

Note that in our case, only the JavaScript version has an example where `FROM +deps` is used in more than one place: both in `build` and in `docker`. Nevertheless, all versions show how dependencies may be separated.

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

deps:
    COPY package.json ./
    COPY package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./package-lock.json

build:
    FROM +deps
    COPY src src
    RUN mkdir -p ./dist && cp ./src/index.html ./dist/
    RUN npx webpack
    SAVE ARTIFACT dist /dist AS LOCAL dist

docker:
    FROM +deps
    COPY +build/dist ./dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./dist"]
    SAVE IMAGE js-example:latest
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part3/part3 ./part3
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

deps:
    COPY build.gradle ./
    RUN gradle build

build:
    FROM +deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:latest
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 3 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part3) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part3/part3 ./part3
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM python:3
WORKDIR /code

deps:
    RUN pip install wheel
    COPY requirements.txt ./
    RUN pip wheel -r requirements.txt --wheel-dir=wheels
    SAVE ARTIFACT wheels /wheels

build:
    FROM +deps
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +deps/wheels wheels
    COPY +build/src src
    COPY requirements.txt ./
    RUN pip install --no-index --find-links=wheels -r requirements.txt
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:latest
```

</details>

# Part 4: Args

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part4/part4 ./part4
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Just Like Docker...Mostly

`ARG`s in Earthly work similar to `ARG`s in Dockerfiles, however there are a few differences when it comes to scope. Also, Earthly has a number of [built in `ARG`s](https://docs.earthly.dev/docs/earthfile/builtin-args) that are available to use.

Let's say we wanted to have the option to pass in a tag for our Docker image when we run `earthly +docker`.

```Dockerfile
docker:
    ARG tag='latest'
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:$tag
```

In our `+docker` target we can create an `ARG` called tag. In this case, we give it a default value of `latest`. If we do not provide a default value the default will be an empty string.

Then, down in our `SAVE IMAGE` command, we are able to reference the `ARG` with `$` followed by the `ARG` name.

Now we can take advantage of this when we run Earthly.

```bash
earthly +docker --tag='my-new-image-tag'
```

In this case `my-new-image-tag` will override the default value and become the new tag for our docker image. If we hadn't passed in a value for tag, then the default `latest` would have been used.

```bash
earthly +docker
# tag for image will be 'latest'
```

#### Passing ARGs in FROM, BUILD, and COPY

We can also pass `ARG`s when referencing a target inside an Earthfile. Using the `FROM` and `BUILD` commands, this looks pretty similar to what we did above on the command line.

```Dockerfile
docker:
    ARG tag='latest'
    COPY +build/example .
    ENTRYPOINT ["/go-workdir/example"]
    SAVE IMAGE go-example:$tag

with-build:
    BUILD +docker --tag='my-new-image-tag'

with-from:
    FROM +docker --tag='my-new-image-tag'
```

We can also pass `ARG`s when using the `COPY` command, though the syntax is a little different.

```Dockerfile
build:
    ARG version
    COPY main.go .
    RUN go build -o output/example-$version main.go
    SAVE ARTIFACT output/example-$version AS LOCAL local-output/go-example

with-copy:
    COPY (+build/example --version='1.0') .
```

### Builtin `ARG`s

There are a number of builtin `ARG`s that Earthly offers. You can read about a [complete list of them](https://docs.earthly.dev/docs/earthfile/builtin-args), but for now, let's take a look at how they work.

**In order to use Earthly builtin `ARG`s they need to be pre-declared.** Once you do that, you can use them just like any other `ARG`.

```Dockerfile
ARG USERARCH
RUN echo $USERARCH
```

In this case we've declared the `ARG` `USERARCH` which is a builtin that holds the processor architecture the target is being built from.

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part4/part4 ./part4
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

deps:
    COPY package.json ./
    COPY package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./package-lock.json

build:
    FROM +deps
    COPY src src
    RUN mkdir -p ./dist && cp ./src/index.html ./dist/
    RUN npx webpack
    SAVE ARTIFACT dist /dist AS LOCAL dist

docker:
    FROM +deps
    ARG tag='latest'
    COPY +build/dist ./dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./dist"]
    SAVE IMAGE js-example:$tag
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part4/part4 ./part4
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

deps:
    COPY build.gradle ./
    RUN gradle build

build:
    FROM +deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ARG tag='latest'
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:$tag
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 4 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part4) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part4/part4 ./part4
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM python:3
WORKDIR /code

deps:
    RUN pip install wheel
    COPY requirements.txt ./
    RUN pip wheel -r requirements.txt --wheel-dir=wheels
    SAVE ARTIFACT wheels /wheels

build:
    FROM +deps
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +deps/wheels wheels
    COPY +build/src src
    COPY requirements.txt ./
    ARG tag='latest'
    RUN pip install --no-index --find-links=wheels -r requirements.txt
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:$tag
```

</details>

# Part 5: Importing

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part5/part5 ./part5
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### Calling on Targets From Other Earthfiles

So far we've seen how the `FROM` command in Earthly has the ability to reference another target's image as its base image, like in the case below where the `+build` target uses the image from the `+deps` target.

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    # Output these back in case go mod download changes them.
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum

build:
    FROM +deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example

```

But `FROM` also has the ability to import targets from Earthfiles in different directories. Let's say we have a directory structure like this.

```
.
├── services
|   └── service-one
|       ├── Earthfile (containing +deps)
|       ├── go.mod
|       └── go.sum
├── main.go
└── Earthfile

```

We can use a target in the Earthfile in `/services/service-one` from inside the Earthfile in the root of our directory. NOTE: relative paths must use `./` or `../`.

`./services/service-one/Earthfile`

```Dockerfile

VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    # Output these back in case go mod download changes them.
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum
```

`./Earthfile`

```Dockerfile
build:
    FROM ./services/service-one+deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

This code tells `FROM` that there is another Earthfile in the `services/service-one` directory and that the Earthfile contains a target called `+deps`. In this case, if we were to run `+build` Earthly is smart enough to go into the subdirectory, run the `+deps` target in that Earthfile, and then use it as the base image for `+build`.

We can also reference an Earthfile in another repo, which works in a similar way. If the reference does not begin with one of `/`, `./`, or `../`, then earthly treats it as a repository. See [the reference](https://docs.earthly.dev/docs/earthfile#from) for details.

```Dockerfile
build:
    FROM github.com/example/project+remote-target
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

### Importing Whole Projects

In addition to importing single targets from other files, we can also import an entire Earthfile with the `IMPORT` command. This is helpful if there are several targets in a separate Earthfile that you want access to in your current file. It also allows you to create an alias.

```Dockerfile
VERSION 0.7
IMPORT ./services/service-one AS my_service
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

build:
    FROM my_service+deps
    COPY main.go .
    RUN go build -o output/example main.go
    SAVE ARTIFACT output/example AS LOCAL local-output/go-example
```

In this example, we assume there is a `./services/service-one` directory that contains its own Earthfile. We import it and then use the `AS` keyword to give it an alias.

Then, in our `+build` target we can inherit from any target in the imported Earthfile by passing `alias+target-name`. In this case the Earthfile in the service directory has a target named `+deps`.

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part5/part5 ./part5
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

build:
    FROM ./services/service-one+deps
    COPY src src
    RUN mkdir -p ./dist && cp ./src/index.html ./dist/
    RUN npx webpack
    SAVE ARTIFACT dist /dist AS LOCAL dist

docker:
    FROM +deps
    ARG tag='latest'
    COPY +build/dist ./dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./dist"]
    SAVE IMAGE js-example:$tag
```

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part5/part5 ./part5
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

build:
    FROM ./services/service-one+deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ARG tag='latest'
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:$tag
```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 5 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part5) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part5/part5 ./part5
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM python:3
WORKDIR /code

build:
    FROM ./services/service-one+deps
    COPY src src
    SAVE ARTIFACT src /src

docker:
    COPY +deps/wheels wheels
    COPY +build/src src
    COPY requirements.txt ./
    ARG tag='latest'
    RUN pip install --no-index --find-links=wheels -r requirements.txt
    ENTRYPOINT ["python3", "./src/hello.py"]
    SAVE IMAGE python-example:$tag
```

</details>

# Part 6: Using Docker In Earthly

To copy the files for [this example ( Part 6 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/go/part6) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/go:main+part6/part6 ./part6
```

Examples in [Python](#more-examples), [JavaScript](#more-examples) and [Java](#more-examples) are at the bottom of this page.

### The `WITH DOCKER` Command

You may find that you need to run Docker commands inside a target. For those cases Earthly offers `WITH DOCKER`. `WITH DOCKER` will initialize a Docker daemon that can be used in the context of a `RUN` command.

Whenever you need to use `WITH DOCKER` we recommend (though it is not required) that you use Earthly's own Docker in Docker (dind) image: `earthly/dind:alpine-3.18-docker-23.0.6-r4`.

Notice `WITH DOCKER` creates a block of code that has an `END` keyword. Everything that happens within this block is going to take place within our `earthly/dind:alpine-3.18-docker-23.0.6-r4` container.

#### Pulling an Image

```Dockerfile
hello:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    WITH DOCKER --pull hello-world
        RUN docker run hello-world
    END

```

You can see in the command above that we can pass a flag to `WITH DOCKER` telling it to pull an image from Docker Hub. We can pass other flags to [load in artifacts built by other targets](#loading-an-image) `--load` or even images defined by [docker-compose](#a-real-world-example) `--compose`. These images will be available within the context of `WITH DOCKER`'s docker daemon.

#### Loading an Image

We can load in an image created by another target with the `--load` flag.

```Dockerfile
my-hello-world:
    FROM ubuntu
    CMD echo "hello world"
    SAVE IMAGE my-hello:latest

hello:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    WITH DOCKER --load hello:latest=+my-hello-world
        RUN docker run hello:latest
    END
```

### A Real World Example

One common use case for `WITH DOCKER` is running integration tests that require other services. In this case we need to set up a redis service for our tests. For this we can user a `docker-compose.yml`.

`docker-compose.yml`

```yml
version: "3"

services:
  redis:
    container_name: local-redis
    image: redis:6.0-alpine
    ports:
      - 127.0.0.1:6379:6379
    hostname: redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:6379"]
      interval: 1s
      timeout: 10s
      retries: 5
    networks:
      - go/part6_default

networks:
  go/part6_default:
```

`main.go`

```go
package main

import (
 "github.com/sirupsen/logrus"
)

var howCoolIsEarthly = "IceCool"

func main() {
 logrus.Info("hello world")
}
```

`main_integration_test.go`

```go
package main

import (
 "context"
 "testing"

 "github.com/go-redis/redis/v8"
 "github.com/stretchr/testify/require"
)

func TestIntegration(t *testing.T) {
 ctx := context.Background()
 rdb := redis.NewClient(&redis.Options{
  Addr:     "redis:6379",
  Password: "", // no password set
  DB:       0,  // use default DB
 })

 err := rdb.Set(ctx, "howCoolIsEarthly", howCoolIsEarthly, 0).Err()
 if err != nil {
  panic(err)
 }

 resultFromDB, err := rdb.Get(ctx, "howCoolIsEarthly").Result()
 if err != nil {
  panic(err)
 }
 require.Equal(t, howCoolIsEarthly, resultFromDB)
}
```

```Dockerfile
VERSION 0.7
FROM golang:1.15-alpine3.13
WORKDIR /go-workdir

deps:
    COPY go.mod go.sum ./
    RUN go mod download
    SAVE ARTIFACT go.mod AS LOCAL go.mod
    SAVE ARTIFACT go.sum AS LOCAL go.sum

test-setup:
    FROM +deps
    COPY main.go .
    COPY main_integration_test.go .
    ENV CGO_ENABLED=0
    ENTRYPOINT ["go", "test", "github.com/earthly/earthly/examples/go"]
    SAVE IMAGE test:latest

integration-tests:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml --load tests:latest=+test-setup
        RUN docker run --network=default_go/part6_default tests:latest
    END
```

When we use the `--compose` flag, Earthly will start up the services defined in the `docker-compose` file for us. In this case, we built a separate image that copies in our test files and uses the command to run the tests as its `ENTRYPOINT`. We can then load this image into our `WITH DOCKER` command. Note that loading an image will not run it by default, we need to explicitly run the image after we load it.

You'll need to use `--allow-privileged` (or `-P` for short) to run this example.

```bash
earthly --allow-privileged +integration-tests
```

### More Examples

<details>

<summary>JavaScript</summary>

To copy the files for [this example ( Part 6 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/js/part6) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/js:main+part6/part6 ./part6
```

In this example, we use `WITH DOCKER` to run a frontend app and backend api together using Earthly.

The App

`./app/package.json`

```json
{
  "name": "example-js",
  "version": "0.0.1",
  "description": "Hello world",
  "private": true,
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "MPL-2.0",
  "devDependencies": {
    "webpack": "^4.42.1",
    "webpack-cli": "^3.3.11"
  },
  "dependencies": {
    "http-server": "^0.12.1"
  }
}
```

`./app/package-lock.json` (empty)

```json
```

The code of the app might look like this

`./app/src/index.js`

```js
async function getUsers() {

  const response = await fetch('http://0.0.0.0:3080/api/users');
  return await response.json();

}

function component() {
  const element = document.createElement('div');
  getUsers()
    .then( users => {
      element.innerHTML = `hello world <b>${users[0].first_name} ${users[0].last_name}</b>`
    })

 return element;
}

document.body.appendChild(component());
```

`./app/src/index.html`

```html
<!doctype html>
<html>

<head>
    <title>Getting Started</title>
</head>

<body>
    <script src="./main.js"></script>
</body>

</html>
```

And our api.

`./api/package.json`

```json
{
  "name": "api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.17.1",
    "http-proxy-middleware": "^1.0.4",
    "pg": "^8.7.3"
  }
}
```

`./api/package-lock.json` (empty)

```json
```

`./api/server.js`

```js
const express = require('express');
const path = require('path');
const cors = require("cors");
const app = express(),
bodyParser = require("body-parser");
port = 3080;

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../my-app/build')));

app.use(cors());

const users = [
  {
    'first_name': 'Lee',
    'last_name' : 'Earth'
  }
]

app.get('/api/users', (req, res) => {
  console.log('api/users called!')
  res.json(users);
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server listening on the port::${port}`);
});
```

The `Earthfile` is at the root of the directory.

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM node:13.10.1-alpine3.11
WORKDIR /js-example

app-deps:
    COPY ./app/package.json ./
    COPY ./app/package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./app/package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./app/package-lock.json

build-app:
    FROM +app-deps
    COPY ./app/src ./app/src
    RUN mkdir -p ./app/dist && cp ./app/src/index.html ./app/dist/
    RUN cd ./app && npx webpack
    SAVE ARTIFACT ./app/dist /dist AS LOCAL ./app/dist

app-docker:
    FROM +app-deps
    ARG tag='latest'
    COPY +build-app/dist ./app/dist
    EXPOSE 8080
    ENTRYPOINT ["/js-example/node_modules/http-server/bin/http-server", "./app/dist"]
    SAVE IMAGE js-example:$tag

api-deps:
    COPY ./api/package.json ./
    COPY ./api/package-lock.json ./
    RUN npm install
    # Output these back in case npm install changes them.
    SAVE ARTIFACT package.json AS LOCAL ./api/package.json
    SAVE ARTIFACT package-lock.json AS LOCAL ./api/package-lock.json

api-docker:
    FROM +api-deps
    ARG tag='latest'
    COPY ./api/server.js .
    RUN pwd
    RUN ls
    EXPOSE 3080
    ENTRYPOINT ["node", "server.js"]
    SAVE IMAGE js-api:$tag

# Run your app and api side by side
app-with-api:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    RUN apk add curl
    WITH DOCKER \
        --load app:latest=+app-docker \
        --load api:latest=+api-docker
        RUN docker run -d -p 3080:3080 api && \
            docker run -d -p 8080:8080 app  && \
            sleep 5 && \
            curl 0.0.0.0:8080 | grep 'Getting Started' && \
            curl 0.0.0.0:3080/api/users | grep 'Earth'
    END

```

Now you can run `earthly -P +app-with-api` to run the app and api side-by-side.

</details>

<details>

<summary>Java</summary>

To copy the files for [this example ( Part 6 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/java/part6) run

```bash
mkdir tutorial
cd tutorial
earthly --artifact github.com/earthly/earthly/examples/tutorial/java:main+part6/part6 ./part6
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM openjdk:8-jdk-alpine
RUN apk add --update --no-cache gradle
WORKDIR /java-example

deps:
    COPY build.gradle ./
    RUN gradle build

build:
    FROM +deps
    COPY src src
    RUN gradle build
    RUN gradle install
    SAVE ARTIFACT build/install/java-example/bin AS LOCAL build/bin
    SAVE ARTIFACT build/install/java-example/lib AS LOCAL build/lib

docker:
    COPY +build/bin bin
    COPY +build/lib lib
    ARG tag='latest'
    ENTRYPOINT ["/java-example/bin/java-example"]
    SAVE IMAGE java-example:$tag

with-postgresql:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    COPY ./docker-compose.yml .
    RUN apk update
    RUN apk add postgresql-client
    WITH DOCKER --compose docker-compose.yml --load app:latest=+docker
        RUN while ! pg_isready --host=localhost --port=5432; do sleep 1; done ;\
            docker run --network=default_java/part6_default app
    END

```

`docker-compose.yml`

```yml
version: "3.9"
   
services:
  db:
    image: postgres
    container_name: db
    hostname: postgres
    environment:
      - POSTGRES_DB=test_db
      - POSTGRES_USER=earthly
      - POSTGRES_PASSWORD=password
    ports:
      - 127.0.0.1:5432:5432
    networks:
      - java/part6_default

networks:
  java/part6_default:


```

The code of the app might look like this

`./src/main/java/hello/HelloWorld.java`

```java

package postgresclient;

import org.joda.time.LocalTime;
import java.sql.Connection;
import java.sql.DriverManager;


public class PostgreSQLJDBC {
   public static void main(String args[]) {
      Connection c = null;
      try {
         Class.forName("org.postgresql.Driver");
         c = DriverManager
            .getConnection("jdbc:postgresql://postgres:5432/test_db",
            "earthly", "password");
      } catch (Exception e) {
         e.printStackTrace();
         System.err.println(e.getClass().getName()+": "+e.getMessage());
         System.exit(0);
      }
      System.out.println("Opened database successfully");
   }
}
```

`./build.gradle`

```groovy
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'postgresclient.PostgreSQLJDBC'

repositories {
    mavenCentral()
}

jar {
    baseName = 'hello-world'
    version = '0.0.1'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8

dependencies {
    compile "joda-time:joda-time:2.2"
    compile(group: 'org.postgresql', name: 'postgresql', version: '42.3.3')
    testCompile "junit:junit:4.12"
}

```

</details>

<details>

<summary>Python</summary>

To copy the files for [this example ( Part 6 )](https://github.com/earthly/earthly/tree/main/examples/tutorial/python/part6) run

```bash
earthly --artifact github.com/earthly/earthly/examples/tutorial/python:main+part6/part6 ./part6
```

`./tests/test_db_connection.py`

```python
import unittest
import psycopg2

class MyIntegrationTests(unittest.TestCase):

    def test_db_connection_active(self):
        connection = psycopg2.connect(
            host="postgres",
            database="test_db",
            user="earthly",
            password="password")
        
        self.assertEqual(connection.closed, 0)

if __name__ == '__main__':
    unittest.main()
```

```yml
version: "3.9"
   
services:
  db:
    image: postgres
    container_name: db
    hostname: postgres
    environment:
      - POSTGRES_DB=test_db
      - POSTGRES_USER=earthly
      - POSTGRES_PASSWORD=password
    ports:
      - 5432:5432
    networks:
      - python/part6_default

networks:
  python/part6_default:
```

`./Earthfile`

```Dockerfile
VERSION 0.7
FROM python:3
WORKDIR /code

build:
    COPY ./requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .

run-tests:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    COPY ./docker-compose.yml .
    COPY ./tests ./tests
    RUN apk update
    RUN apk add postgresql-client
    WITH DOCKER --compose docker-compose.yml --load app:latest=+docker
        RUN while ! pg_isready --host=localhost --port=5432; do sleep 1; done ;\
          docker run --network=default_python/part6_default app python3 ./tests/test_db_connection.py
    END
```

</details>

# Part 7: Using remote runners

Earthly has the ability to run builds both locally and remotely. In this section, we will explore how to use remote runners to perform builds on remote machines.

### Remote Runners

Earthly is able to use remote runners for performing builds on remote machines. When Earthly uses a remote runner, the inputs of the build are picked up from the local environment, then the execution takes place remotely, including any pushes (`RUN --push` commands, and `SAVE IMAGE --push` commands), but any local outputs are sent back to the local environment. All this takes place while your local Earthly process still provides the logs of the build in real time locally.

Remote runners are especially useful in a few specific circumstances:

* You want to **reuse cache between CI runs** to dramatically speed up builds (more on this in part 8).
* You want to **share compute and cache with coworkers** and/or with the CI.
* You have **a build that requires a lot of resources**, and you want to run it on a machine with more resources than your local machine.
* You have **a build that requires running on a specific CPU architecture** natively.
* You have **a slow internet connection**.

There are two types of remote runners:

* Earthly Satellites (managed by Earthly; free up to 6,000 minutes/month; get started now by visiting the [sign up](https://cloud.earthly.dev/login) page)
* Remote Buildkit (free, self-hosted)

#### Using Earthly Satellites

Earthly Satellites are remote runners managed by the Earthly team.

To get started, first you need to [sign up for Earthly Cloud](https://cloud.earthly.dev/login) for free.

Then, you can select the org that you are part of, and create a satellite.

```bash
earthly org select <my-org>
earthly sat launch my-satellite
```

Once a satellite has been launched it is automatically selected for use. If you ever need to switch the satellite yourself, you can use the command...

```bash
earthly sat select my-satellite
```

Additionally, you can go back to performing local builds with the command...

```bash
earthly sat unselect
```

And then run Earthly builds as usual.

```bash
earthly +my-target
```

Or, you can use a satellite as part of the build without selecting first

```bash
earthly --sat my-satellite +my-target
```

For more information, check out the [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites) page.

#### Using a Remote Buildkit

To run your own remote Buildkit, you can follow the instructions on the [remote Buildkit page](https://docs.earthly.dev/ci-integration/remote-buildkit).

#### Secrets and remote builds

When running remote builds, some operations might require access to secrets. For example, if you are pushing images to a private registry, or if you are logged in to DockerHub to prevent rate limiting. Earthly will automatically pass the credentials from your local machine to the remote runner.

Any secret that is available locally, including Docker/Podman credentials, will be passed to the remote runner whenever needed by the build.

For more information about secrets, see the [Args and secrets page](https://docs.earthly.dev/docs/guides/build-args) and the [authenticating Git and image registries page](https://docs.earthly.dev/docs/guides/auth).

# Part 8a: Using Earthly in your current CI

In this section, we will explore how to use Earthly in a CI system, such as GitHub Actions.

For more information on how to use Earthly in other CIs such as GitLab, Jenkins, or CircleCI, you can check out the [CI Integration page](https://docs.earthly.dev/ci-integration/overview).

### Using Earthly in Your Current CI

To use Earthly in a CI, you typically encode the following steps in your CI's build configuration:

1. Download and install Earthly
2. Set up any credentials needed for the build
3. Log in to image registries, such as DockerHub
4. Run Earthly

As part of this, you may need to set up credentials for Earthly Cloud, if you are using Earthly Satellites or Earthly Secrets. For this, you can use the following command:

```bash
earthly account create-token my-ci-token
```

Finally, here is a complete example of how to run Earthly in GitHub Actions:

```yaml
# .github/workflows/ci.yml

name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      DOCKERHUB_USERNAME: ${{ secrets.DOCKERHUB_USERNAME }}
      DOCKERHUB_TOKEN: ${{ secrets.DOCKERHUB_TOKEN }}
      EARTHLY_TOKEN: ${{ secrets.EARTHLY_TOKEN }}
      FORCE_COLOR: 1
    steps:
    - uses: earthly/actions/setup-earthly@v1
      with:
        version: v0.7.23
    - uses: actions/checkout@v2
    - name: Docker Login
      run: docker login --username "$DOCKERHUB_USERNAME" --password "$DOCKERHUB_TOKEN"
    - name: Run build
      run: earthly --org <org-name> --sat <satellite-name> --ci --push +build
```

Here is an explanation of the steps above:

* The action `earthly/actions/setup-earthly@v1` downloads and installs Earthly. Running this action is similar to running the Earthly installation one-liner `sudo /bin/sh -c 'wget https://github.com/earthly/earthly/releases/download/v0.7.23/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly'`
* The command `docker login` performs a login to the DockerHub registry. This is required, to prevent rate-limiting issues when using popular base images.
* The command `earthly --org ... --sat ... --ci --push +build` executes the build. The `--ci` flag is used here, in order to force the use of `--strict` mode. In `--strict` mode, Earthly prevents the use of features that make the build less repeatable and also disables local outputs -- because artifacts and images resulting from the build are not needed within the CI environment. Any outputs should be pushed via `RUN --push` or `SAVE IMAGE --push` commands. The flags `--org` and `--sat` allow you to select the organization and satellite to use for the build. If no satellite is specified, the build will be executed in the CI environment itself, with limited caching.

For more information about integrating Earthly with other CI systems, you can check out the [CI Integration page](https://docs.earthly.dev/ci-integration/overview).

# Final words

Congratulations, you completed the Earthly tutorial!

Learning Earthly does not stop here. Discover more of what Earthly can do by exploring the documentation.

**Recommended reading:**

* [The Earthfile reference](https://docs.earthly.dev/docs/earthfile)
* [The **earthly command** reference](https://docs.earthly.dev/docs/earthly-command)
* [Guides](https://tinyurl.com/2p8cpnxv)
* [Examples using Earthly](https://docs.earthly.dev/docs/examples)
* [Best practices](https://docs.earthly.dev/docs/guides/best-practices)
* [Earthly Cloud](https://cloud.earthly.dev/)

**More examples:**

* [Examples directory on GitHub](https://github.com/earthly/earthly/tree/main/examples)
* [Go](https://github.com/earthly/earthly/tree/main/examples/go)
* [JavaScript](https://github.com/earthly/earthly/tree/main/examples/js)
* [Java](https://github.com/earthly/earthly/tree/main/examples/java)
* [Python](https://github.com/earthly/earthly/tree/main/examples/python)

## Questions & Feedback

If you have any questions, feedback or suggestions for Earthly or this tutorial feel free to reach out to us on our [Slack community](https://earthly.dev/slack) or open a [GitHub issue](https://github.com/earthly/earthly/issues). Earthly is free and open and we love and appreciate feedback and contributions from the community!

## Go back

* [Introduction](https://docs.earthly.dev/basics)
* [Part 1: A simple Earthfile](https://docs.earthly.dev/basics/part-1-a-simple-earthfile)
* [Part 2: Outputs](https://docs.earthly.dev/basics/part-2-outputs)
* [Part 3: Adding dependencies With Caching](https://docs.earthly.dev/basics/part-3-adding-dependencies-with-caching)
* [Part 4: Args](https://docs.earthly.dev/basics/part-4-args)
* [Part 5: Importing](https://docs.earthly.dev/basics/part-5-importing)
* [Part 6: Using Docker In Earthly](https://docs.earthly.dev/basics/part-6-using-docker-with-earthly)
* [Part 7: Using remote runners](https://docs.earthly.dev/basics/part-7-using-remote-runners)
* [Part 8: Using Earthly in CI](https://docs.earthly.dev/basics/part-8a-using-earthly-in-your-current-ci)
* **Final words** <-- You are here.

# Featured guides

Earthly works with any programming language, as shown in our extensive collection of [examples](https://docs.earthly.dev/docs/examples). However, we are now working on a series of [language-specific libraries](https://docs.earthly.dev/docs/earthly-lib) that make Earthly that much easier to use with various languages and frameworks. To that end, we are starting with [Rust](https://docs.earthly.dev/featured-guides/rust).

If you are just starting out, the [onboarding tutorial in Earthly Cloud](https://cloud.earthly.dev/login) is a great way to get introduced to Earthly.

# Rust

This page will help you use Earthly if you are using Rust.

## Step 1: Import the Rust library

To get started, import the rust library as shown below. Note that the `--global-cache` flag is currently required to allow for adequate caching of the Rust toolchain. This flag will be implied in a future release.

```Dockerfile
VERSION --global-cache 0.7

IMPORT github.com/earthly/lib/rust:2.2.11 AS rust
```

## Step 2: Initialize the Rust toolchain

Next, initialize the Rust toolchain via `rust+INIT`. This will install any necessary dependencies that `rust+CARGO` needs underneath.

```Dockerfile
install:
  FROM rust:1.73.0-bookworm
  RUN apt-get update -qq
  RUN apt-get install --no-install-recommends -qq autoconf autotools-dev libtool-bin clang cmake bsdmainutils
  RUN rustup component add clippy
  RUN rustup component add rustfmt
  # Call +INIT before copying the source file to avoid installing depencies every time source code changes. 
  # This parametrization will be used in future calls to functions of the library
  DO rust+INIT --keep_fingerprints=true
```

## Step 3: Build your Rust project

Now you can build your Rust project. Collect the necessary sources and call `rust+CARGO` to build your project.

```Dockerfile
source:
  FROM +install
  COPY --keep-ts Cargo.toml Cargo.lock ./
  COPY --keep-ts --dir package1 package2  ./

build:
  FROM +source
  DO rust+CARGO --args="build --release" --output="release/[^/\.]+"
  SAVE ARTIFACT ./target/release/*
```

Notice the need for the `--keep-ts` flag when copying the source files. This is necessary to ensure that the timestamps of the source files are preserved such that Rust's incremental compilation works correctly.

Additionally, because cargo does not make a good distinction between intermediate and final artifacts, we use the `--output` flag to specify which files should be extracted from the cache at the end of the operation.

## Finally

For a complete Earthfile example on how to use Rust in Earthly, visit the [rust example directory on GitHub](https://github.com/earthly/earthly/tree/main/examples/rust).

See also the reference documentation for [lib/rust](https://github.com/earthly/lib/tree/main/rust), to understand the different parameters used with `rust+INIT` and `rust+CARGO`.

# Guides

# Importing

Importing in Earthly is how multiple build components (targets, artifacts, functions, Earthfiles) can be interconnected to compose complex build setups while reusing build code. This page describes the syntax and semantics of importing in Earthly.

## Cheat sheet

Here's a quick cheat sheet for the syntax of importing in Earthly. The sections below go into more detail on each of these.

![Import syntax](https://3102854999-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fyi347RZ02JXdgz9BJx5u%2Fuploads%2Fgit-blob-c0de3ce611c82453a14ac3404b0f435797d074fe%2Fimport-cheat-sheet.png?alt=media)

## Import basics

Let's start with a few simple examples.

### Importing within the same Earthfile

When importing a target from the same Earthfile, the import reference is simply the name of the target being imported, with a `+` in front. For example:

```Dockerfile
target1:
    RUN echo "Hello World"

target2:
    BUILD +target1
```

If you want to import an artifact, the import reference is the target reference, followed by a `/`, followed by the path to the artifact. For example:

```Dockerfile
target1:
    RUN echo "Hello World" > out.txt
    SAVE ARTIFACT out.txt

target2:
    COPY +my-target/out.txt ./
```

### Importing from other repositories

When importing from other repositories, making use of the `IMPORT` command helps to keep the Earthfile clean and readable. The `IMPORT` command takes an Earthfile reference, and optionally an import alias. For example:

```Dockerfile
IMPORT github.com/earthly/hello-world:main AS hello-world

...

my-target:
    BUILD hello-world+hello
    COPY hello-world+hello/hello.txt ./
```

In this example, the target `my-target` uses the import alias `hello-world` to reference a GitHub repository called `github.com/earthly/hello-world`, and the target `hello` within that repository. The `AS hello-world` part is optional, and is only needed if the import alias is different from the repository name.

`BUILD` is used used to simply issue the build of the referenced target. Commands like `COPY` or `FROM` can be used to import artifacts or images, respectively.

### Importing from other directories

Importing from other directories is similar to importing from other repositories. The only difference is that the Earthfile reference is a relative path to the directory containing the Earthfile. For example:

```Dockerfile
IMPORT ./some/other/dir AS other-dir

my-target:
    BUILD other-dir+my-target
    COPY other-dir+my-target/out.txt ./
```

### Inline imports

Importing can also be done inline, without the need for an `IMPORT` command. This is useful for importing a single target or artifact from a remote repository. For example:

```Dockerfile
BUILD github.com/earthly/hello-world:main+hello
COPY ./some/other/dir+my-target/out.txt ./
```

## Referencing syntax

This subsection goes through the different types of references that Earthly uses:

* Earthfile references `github.com/foo/bar`, `./my/local/path`
* Target references: `<earthfile-ref>+my-target`
* Artifact references: `<earthfile-ref>+my-target/my-artifact.bin`
* Image references (same as target references)
* Function references: `<earthfile-ref>+MY_FUNCTION`

## Target reference

Target references point to an Earthly target. They have the general form

`<earthfile-ref>+<target>`

Target references distinguish themselves from function references (see below) by having a name in all-lower-case, kebab-case (e.g. `+my-target`).

Here are some examples:

* `+build`
* `./js+deps`
* `github.com/earthly/earthly:v0.7.23+earthly`
* `my-import+build`

## Artifact reference

Artifact references are similar to target references, except that they have an artifact path at the end. It has the following form

`<target-ref>/<artifact-path>`

Here are some examples:

* `+build/my-artifact`
* `+build/some/artifact/deep/in/a/dir`
* `./js+build/dist`
* `github.com/earthly/earthly:v0.7.23+earthly/earthly`
* `my-import+build/my-artifact`

## Image reference

Because there can only be one image per target, image references have the exact same format as target references.

The only difference is the context where they are used. For example, a `FROM` command takes an image reference. While a `BUILD` command takes a target reference.

## Function reference

Function references point to a [function](https://docs.earthly.dev/docs/guides/functions) in an Earthfile. They have the general form

`<earthfile-ref>+<function>`

Function references distinguish themselves from target references by having a name in all-caps, snake-case (e.g. `+MY_FUNCTION`).

Here are some examples:

* `+COMPILE`
* `./js+NPM_INSTALL`
* `github.com/earthly/earthly:v0.7.23+DOWNLOAD_DIND`
* `my-import+COMPILE`

For more information on functions, see the [Functions Guide](https://docs.earthly.dev/docs/guides/functions).

## Earthfile references

Earthfile references appear in target, artifact and function references. They point to the Earthfile containing the respective target, artifact or function. Below are the different types of Earthfile references available in Earthly.

### Local, internal

The simplest form, is where a target, function or artifact is referenced from the same Earthfile. In this case, the Earthfile reference is simply **the empty string**. Here are some examples of this type of Earthfile reference being used in various other references:

| Earthfile ref      | Target ref       | Artifact ref                     | Function ref       |
| ------------------ | ---------------- | -------------------------------- | ------------------ |
| (**empty string**) | `+<target-name>` | `+<target-name>/<artifact-path>` | `+<function-name>` |
| (**empty string**) | `+build`         | `+build/out.bin`                 | `+COMPILE`         |

In this form, Earthly will look for the target within the same Earthfile. We call this type of referencing local, internal. Local, because it comes from the same system, and internal, because it is within the same Earthfile.

### Local, external

Another form, is where a target, function or artifact is referenced from a different directory. In this form, the path to that directory is specified before `+`. It must always start with either `./`, `../` or `/`, on any operating system (including Windows). Example:

| Earthfile ref           | Target ref                            | Artifact ref                                          | Function ref                            |
| ----------------------- | ------------------------------------- | ----------------------------------------------------- | --------------------------------------- |
| `./path/to/another/dir` | `./path/to/another/dir+<target-name>` | `./path/to/another/dir+<target-name>/<artifact-path>` | `./path/to/another/dir+<function-name>` |
| `./js`                  | `./js+build`                          | `./js+build/out.bin`                                  | `./js+COMPILE`                          |

It is recommended that relative paths are used, for portability reasons: the working directory checked out by different users will be different, making absolute paths infeasible in most cases.

### Remote

Another form of a Earthfile reference is the remote form. In this form, the recipe and the build context are imported from a remote location. It has the following form:

| Earthfile ref                                               | Target ref                                                                | Artifact ref                                                                              | Function ref                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `<vendor>/<namespace>/<project>/path/in/project[:some-tag]` | `<vendor>/<namespace>/<project>/path/in/project[:some-tag]+<target-name>` | `<vendor>/<namespace>/<project>/path/in/project[:some-tag]+<target-name>/<artifact-path>` | `<vendor>/<namespace>/<project>/path/in/project[:some-tag]+<function-name>` |
| `github.com/earthly/earthly/buildkitd`                      | `github.com/earthly/earthly/buildkitd+build`                              | `github.com/earthly/earthly/buildkitd+build/out.bin`                                      | `github.com/earthly/earthly/buildkitd+COMPILE`                              |
| `github.com/earthly/earthly:v0.7.23`                        | `github.com/earthly/earthly:v0.7.23+build`                                | `github.com/earthly/earthly:v0.7.23+build/out.bin`                                        | `github.com/earthly/earthly:v0.7.23+COMPILE`                                |

### Import reference

Finally, the last form of Earthfile referencing is an import reference. Import references may only exist after an `IMPORT` command, which helps resolve the reference to a full Earthfile reference of the types above.

| Import command                                  | Earthfile ref    | Target ref                     | Artifact ref                                   | Function ref                     |
| ----------------------------------------------- | ---------------- | ------------------------------ | ---------------------------------------------- | -------------------------------- |
| `IMPORT <full-earthfile-ref> AS <import-alias>` | `<import-alias>` | `<import-alias>+<target-name>` | `<import-alias>+<target-name>/<artifact-path>` | `<import-alias>+<function-name>` |
| `IMPORT github.com/earthly/earthly/buildkitd`   | `buildkitd`      | `buildkitd+build`              | `buildkitd+build/out.bin`                      | `buildkitd+COMPILE`              |
| `IMPORT github.com/earthly/earthly:v0.7.23`     | `earthly`        | `earthly+build`                | `earthly+build/out.bin`                        | `earthly+COMPILE`                |

Here is an example in an Earthfile:

```Dockerfile
IMPORT github.com/earthly/earthly/buildkitd

...

BUILD buildkitd+buildkitd
```

## Implicit Base Target Reference

All Earthfiles start with a base recipe. This is the only recipe which does not have an explicit target name - the name is always implied to be `base`. All other target implicitly inherit from `base`. You can imagine that all recipes start with an implicit `FROM +base`

```
# base recipe
FROM golang:1.15-alpine3.13
WORKDIR /go-example

build:
    # implicit FROM +base
    RUN echo "Hello World"
```

## Canonical form

Most references have a canonical form. It is essentially the remote form of the same target, with repository and tag inferred. The canonical form can be useful as a universal identifier for a target.

For example, depending on where the files are stored, the `+build` target could have the canonical form `github.com/some-user/some-project/some/deep/dir:master+build`, where `github.com/some-user/some-project` was inferred as the Git location, based on the Git remote called `origin`, and `/some/deep/dir` was inferred as the sub-directory where `+build` exists within that repository. The Earthly tag is inferred using the following algorithm:

* If the current HEAD has at least one Git tag, then use the first Git tag listed by Git, otherwise
* If the repository is not in detached HEAD mode, use the current branch, otherwise
* Use the current Git hash.

If no Git context is detected by Earthly, then the target does not have a canonical form.

# Build arguments and secrets

## Introduction

One of the core features of Earthly is support for build arguments. Build arguments can be used to dynamically set environment variables inside the context of [RUN commands](https://docs.earthly.dev/earthfile#run).

Build arguments can be passed between targets or from the command line. They encourage writing generic Earthfiles and ultimately promote greater code-reuse.

Additionally, Earthly defines secrets which are similar to build arguments, but are exposed as environment variables when explicitly allowed.

## A Quick Example

Arguments are declared with the [ARG](https://docs.earthly.dev/earthfile#arg) keyword.

Let's consider a "hello world" example that allows us to change who is being greeted (e.g. hello banana, hello eggplant etc). We will create a hello target that accepts the `name` argument:

```Dockerfile
VERSION 0.7
FROM alpine:latest

hello:
    ARG name
    RUN echo "hello $name"
```

Then we will specify a value for the `name` argument on the command line when we invoke `earthly`:

```bash
earthly +hello --name=world
```

This will output

```
    buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
alpine:latest | --> Load metadata linux/arm64
         +foo | --> FROM alpine:latest
         +foo | [██████████] 100% resolve docker.io/library/alpine:latest@sha256:21a3deaa0d32a8057914f36584b5288d2e5ecc984380bc0118285c70fa8c9300
         +foo | name=world
         +foo | --> RUN echo "hello $name"
         +foo | hello world
       output | --> exporting outputs
```

If we re-run `earthly +hello --name=world`, we will see that the echo command is cached (and won't re-display the hello world text):

```
+foo | *cached* --> RUN echo "hello $name"
```

## Default values

Arguments may also have default values, which may be either constant or dynamic. For example, the following target will greet the name identified by the arg `name` (which has a default value of John), with the current time:

```Dockerfile
hello:
   ARG time=$(date +%H:%M)
   ARG name=John
   RUN echo "hello $name, it is $time"
```

```
alpine:latest | --> Load metadata linux/arm64
        +base | --> FROM alpine:latest
        +base | [██████████] 100% resolve docker.io/library/alpine:latest@sha256:21a3deaa0d32a8057914f36584b5288d2e5ecc984380bc0118285c70fa8c9300
       +hello | --> ARG time = RUN $(date +%H:%M)
       +hello | --> RUN echo "hello $name, it is $time"
       +hello | hello John, it is 23:21
       output | --> exporting outputs
```

If an arg has no default value, then the default value is the empty string.

## Overriding Argument Values

Argument values can be set multiple ways:

1. On the command line

   The value can be directly specified on the command line (as shown in the previous example):

   ```
   earthly +hello --HELLO=world --FOO=bar
   ```

2. From environment variables

   Similar to above, except that the value is an environment variable:

   ```bash
   export HELLO="world"
   export FOO="bar"
   earthly +hello --HELLO="$HELLO" --FOO="$FOO"
   ```

3. Via the `EARTHLY_BUILD_ARGS` environment variable

   The value can also be set via the `EARTHLY_BUILD_ARGS` environment variable.

   ```bash
   export EARTHLY_BUILD_ARGS="HELLO=world,FOO=bar"
   earthly +hello
   ```

   This may be useful if you have a set of build args that you'd like to always use and would prefer not to have to specify them on the command line every time. The `EARTHLY_BUILD_ARGS` environment variable may also be stored in your `~/.bashrc` file, or some other shell-specific startup script.
4. From an `.arg` file

   It is also possible to create an `.arg` file to contain the build arguments to pass to earthly. First create an `.arg` file with:

   ```
   name=eggplant
   ```

   Then simply run earthly:

   ```bash
   earthly +hello
   ```

## Passing Argument values to targets

Build arguments can also be set when calling build targets. If multiple build arguments values are defined for the same argument name, Earthly will build the target for each value; this makes it easy to configure a "build matrix" within Earthly.

For example, we can create a new `greetings` target which calls `+hello` multiple times:

```dockerfile
greetings:
    BUILD +hello \
        --name=world \
        --name=banana \
        --name=eggplant
```

Then when we call `earthly +greetings`, earthly will call `+hello` three times:

```
     buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
 alpine:latest | --> Load metadata linux/amd64
         +base | --> FROM alpine:latest
         +base | [██████████] resolve docker.io/library/alpine:latest@sha256:69e70a79f2d41ab5d637de98c1e0b055206ba40a8145e7bddb55ccc04e13cf8f ... 100%
        +hello | name=banana
        +hello | --> RUN echo "hello $name"
        +hello | name=eggplant
        +hello | --> RUN echo "hello $name"
        +hello | name=world
        +hello | --> RUN echo "hello $name"
        +hello | hello banana
        +hello | hello eggplant
        +hello | hello world
        output | --> exporting outputs
```

In addition to the `BUILD` command, build args can also be used with `FROM`, `COPY`, `WITH DOCKER --load` and a number of other commands:

```Dockerfile
BUILD +hello --name=world
COPY (+hello/file.txt --name=world) ./
FROM +hello --name=world
WITH DOCKER --load=(+hello --name=world)
  ...
END
```

Another way to pass build args is by specifying a dynamic value, delimited by `$(...)`. For example, in the following, the value of the arg `name` will be set as the output of the shell command `echo world` (which, of course is simply `world`):

```Dockerfile
BUILD +hello --name=$(echo world)
```

## Passing secrets to RUN commands

Secrets are similar to build arguments; however, they are *not* defined in targets, but instead are explicitly defined for each `RUN` command that is permitted to access them.

Here's an example Earthfile that accesses a secret stored under `passwd` and exposes it under the environment variable `mypassword`:

```dockerfile
FROM alpine:latest
hush:
    RUN --secret mypassword=passwd echo "my password is $mypassword"
```

If the environment variable name is identical to the secret ID. For example to accesses a secret stored under `passwd` and exposes it under the environment variable `passwd` you can use the shorthand :

```dockerfile
FROM alpine:latest
hush:
    RUN --secret passwd echo "my password is $passwd"
```

{% hint style="info" %}
It's also possible to temporarily mount a secret as a file:

```dockerfile
RUN --mount type=secret,target=/root/mypassword,id=passwd echo "my password is $(cat /root/mypassword)"
```

The file will not be saved to the image snapshot.
{% endhint %}

## Setting secret values

The value for `passwd` in examples above must then be supplied when earthly is invoked.

This is possible in a few ways:

1. Directly, on the command line:

   ```bash
   earthly --secret passwd=itsasecret +hush
   ```

2. Via an environment variable:

   ```bash
   export passwd=itsasecret
   earthly --secret passwd +hush
   ```

   If the value of the secret is omitted on the command line Earthly will lookup the environment variable with that name.
3. Via the environment variable `EARTHLY_SECRETS`

   ```bash
   export EARTHLY_SECRETS="passwd=itsasecret"
   earthly +hush
   ```

   Multiple secrets can be specified by separating them with a comma.
4. Via the `.secret` file.

   Create a `.secret` file in the same directory where you plan to run `earthly` from. Its contents should be:

   ```
   passwd=itsasecret
   ```

   Then simply run earthly:

   ```bash
   earthly +hello
   ```

5. Via cloud-based secrets. This option helps share secrets within a wider team. To read more about this see the [cloud-based secrets guide](https://docs.earthly.dev/earthly-cloud/cloud-secrets).

Regardless of the approach chosen from above, once earthly is invoked, in our example, it will output:

```
+hush | --> RUN echo "my password is $mypassword"
+hush | my password is itsasecret
```

{% hint style="info" %}

#### How Arguments and Secrets affect caching

Commands in earthly must be re-evaluated when the command itself changes (e.g. `echo "hello $name"` is changed to `echo "greetings $name"`), or when one of its inputs has changed (e.g. `--name=world` is changed to `--name=banana`). Earthly creates a hash based on both the contents of the command and the contents of all defined arguments of the target build context.

However, in the case of secrets, the contents of the secret *is not* included in the hash; therefore, if the contents of a secret changes, Earthly is unable to detect such a change, and thus the command will not be re-evaluated.
{% endhint %}

## Storage of local secrets

Earthly stores the contents of command-line-supplied secrets in memory on the localhost. When a `RUN` command that requires a secret is evaluated by BuildKit, the BuildKit daemon will request the secret from the earthly command-line process and will temporarily mount the secret inside the runc container that is evaluating the `RUN` command. Once the command finishes the secret is unmounted. It will not persist as an environment variable within the saved container snapshot. Secrets will be kept in-memory until the earthly command exits.

Earthly also supports cloud-based shared secrets which can be stored in the cloud. Secrets are never stored in the cloud unless a user creates an earthly account and explicitly calls the `earthly secrets set ...` command to transmit the secret to the earthly cloud-based secrets server. For more information about cloud-based secrets, check out our [cloud-based secrets management guide](https://docs.earthly.dev/earthly-cloud/cloud-secrets).

# Functions

{% hint style="danger" %}
**UDCs have been renamed to Functions**

Functions used to be called UDCs (User Defined Commands). Earthly 0.7 still uses `COMMAND` for declaring functions, but the keyword is deprecated and will be replaced by `FUNCTION` in Earthly 0.8.
{% endhint %}

Earthly Functions are reusable sets of instructions that can be inserted in targets or other functions. In other words, it is a way to import common build steps which can be reused in multiple contexts.

Unlike targets, functions inherit the (1) build context and (2) the build environment from the caller. Meaning that

1. Any local `COPY` operation will use the directory where the calling Earthfile exists, as the source.
2. Any files, directories and dependencies created by a previous step of the caller are available to the function to operate on; and any file changes resulting from executing the function's commands are passed back to the caller as part of the build environment.

Thus, when importing and reusing functions across a complex build, it is very much like reusing libraries in a regular programming language.

## Usage

Functions are defined similarly to regular targets, with a couple of exceptions: the name is in ALL\_UPPERCASE\_SNAKE\_CASE and the recipe must start with `COMMAND` (Note: this keyword will be replaced with `FUNCTION` in Earthly 0.8). For example:

```Dockerfile
MY_COPY:
    COMMAND
    ARG src
    ARG dest=./
    ARG recursive=false
    RUN cp $(if $recursive =  "true"; then printf -- -r; fi) "$src" "$dest"
```

This function can be invoked from a target via `DO`

```Earthfile
build:
    FROM alpine:3.18
    WORKDIR /function-example
    RUN echo "hello" >./foo
    DO +MY_COPY --src=./foo --dest=./bar
    RUN cat ./bar # prints "hello"
```

A few things to note about this example:

* The definition of `MY_COPY` does not contain a `FROM` so the build environment it operates in is the build environment of the caller.
* This means that `+MY_COPY` has access to the file `./foo`.
* Although the copy file operation is performed within `+MY_COPY`, its effects are seen in the environment of the caller - so the resulting `./bar` is available to the caller.

## Scope

Functions create their own `ARG` scope, which is distinct from the caller. Any `ARG` that needs to be passed from the caller needs to be passed explicitly via `DO +COMMAND --<build-arg-key>=<build-arg-value>`, as in the following example.

```Dockerfile
build:
    ARG var=value-in-build
    # prints "something-else"
    DO +PRINT_VAR
    # prints "value-in-build"
    DO +PRINT_VAR --var=$var

PRINT_VAR:
    COMMAND
    ARG var=something-else
    RUN echo "$var"
```

Global imports and global args are inherited from the `base` target of the same Earthfile where the command is defined in (this may be distinct from the `base` target of the caller).

```Dockerfile
VERSION 0.7

ARG --global a_global_var=value-in-global

build:
    # prints "value-in-global"
    DO +PRINT_VAR

PRINT_VAR:
    COMMAND
    RUN echo "$a_global_var"
```

## Targets vs Functions

Targets and functions are Earthly's core primitives for organizing build recipes. They encapsulate build logic, and from afar they look pretty similar. However, the use-cases for each are vastly different.

In general, targets are used to produce specific build results, while functions are used as a way to reuse build logic, when certain commands are repeated in multiple places. As a real-world analogy, targets are more like factories, while functions are more like components that are used to put together factories.

Here is a comparison of the two primitives:

|                                                | Targets                                                          | Functions                                                                   |
| ---------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Represents a collection of Earthly commands    | ✅                                                                | ✅                                                                           |
| Can reference other targets in its body        | ✅                                                                | ✅                                                                           |
| Can reference other functions in its body      | ✅                                                                | ✅                                                                           |
| Build context                                  | The directory where the Earthfile resides                        | Inherited from the caller                                                   |
| Build environment, when no `FROM` is specified | Inherited from the base of its own Earthfile                     | Inherited from the caller                                                   |
| `IMPORT` statements                            | Inherited from the base of its own Earthfile                     | Inherited from the base of its own Earthfile                                |
| `ARG` context                                  | Creates its own scope                                            | Creates its own scope                                                       |
| Requires that `ARG`s be passed in explicitly   | ✅                                                                | ✅                                                                           |
| Global `ARG` context                           | Inherited from the base of its own Earthfile                     | Inherited from the base of its own Earthfile                                |
| Can output artifacts                           | ✅                                                                | ❌ - can issue `SAVE ARTIFACT`, but it's the caller that emits the artifacts |
| Can output images                              | ✅                                                                | ❌ - can issue `SAVE IMAGE`, but it's the caller that emits the images       |
| Can be called via `earthly` CLI                | ✅                                                                | ❌                                                                           |
| Can be used in conjunction with an `IMPORT`    | ✅ - `FROM some-import+my-target`                                 | ✅ - `DO some-import+MY_FUNCTION`                                            |
| Commands that can reference it                 | `FROM`, `BUILD`, `COPY`, `WITH DOCKER --load`, `FROM DOCKERFILE` | `DO`                                                                        |

# Using Docker in Earthly

This guide walks through using Docker commands in Earthly.

## Basic usage

In order to use Docker commands (such as `docker run`), Earthly makes available isolated Docker daemons which are started and stopped on-demand. The reason for using isolated instances of Docker daemons is such that no preexisting Docker state (e.g. images, containers, networks, volumes) can influence the way the build executes. This allows Earthly to achieve high degrees of reproducibility.

Here is a quick example of running a `hello-world` docker container via `docker run` in Earthly:

```Dockerfile
hello:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    WITH DOCKER --pull hello-world
        RUN docker run hello-world
    END
```

Let's break it down.

`FROM earthly/dind:alpine-3.18-docker-23.0.6-r4` inherits from an Earthly-supported docker-in-docker (dind) image. This is recommended, because `WITH DOCKER` requires all the Docker binaries (not just the client) to be present in the build environment.

`WITH DOCKER ... END` starts a Docker daemon for the purpose of running Docker commands against it. At the end of the execution, this also terminates the daemon and permanently deletes all of its data (e.g. daemon cached images).

`--pull hello-world` pulls the image `hello-world` from the Docker Hub. This option could have been replaced with the more traditional `docker pull hello-world`. However, the Earthly variant additionally stores the image in the Earthly cache, so that the actual pull is performed only if the image changes. Because the daemon cache is cleared after each run, `docker pull` would not achieve the same.

`RUN docker run hello-world` executes the `docker run` command in the context of the daemon created by `WITH DOCKER`.

## Loading images built by Earthly

A typical use of Docker in Earthly is running an image that has been built via Earthly itself. To achieve that, the option `WITH DOCKER --load ...=...` can be used. Here is an example:

```Dockerfile
build:
    ...
    ENTRYPOINT ...
    SAVE IMAGE my-image:latest

smoke-test:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    WITH DOCKER --load test:latest=+build
        RUN docker run test:latest
    FROM earthly/dind:alpine
    WITH DOCKER --load +build
        RUN docker run my-image:latest
    END
```

`--load +build` takes the image produced by the target `+build` and loads it into the Docker daemon created by `WITH DOCKER`.

## Running docker-compose

It is possible to run `docker-compose` via `WITH DOCKER`, either explicitly, simply by running the `docker-compose` tool, or implicitly, via the `--compose` flag. The `--compose` flag allows you to specify a Docker compose stack that needs to be brought up before the execution of the `RUN` command. For example:

```Dockerfile
FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
COPY docker-compose.yml ./
WITH DOCKER \
        --compose docker-compose.yml \
        --service db \
        --service api
    RUN docker run some-integration-test:latest
END
```

Using the `--compose` flag has the added benefit that any images needed by the compose stack will be automatically added to the pull list by Earthly, thus using cache efficiently.

## Performance

It's recommended to use the `earthly/dind:alpine-3.18-docker-23.0.6-r4` image for running docker-in-docker. See the best-practices' section on using [with docker](https://docs.earthly.dev/docs/best-practices#use-earthly-dind) for more details.

In cases when using `earthly/dind` is not possible, Earthly will attempt to install Docker in the image you have chosen. This has the drawback of not being able to use cache efficiently and is not recommended for performance reasons.

Another option is to use the Earthly UDC `INSTALL_DIND`. This will install Docker in the build environment, but you can control at what point in the build it happens, thus being able to optimize your cache use. For example:

```Dockerfile
FROM my-image:latest
DO github.com/earthly/lib+INSTALL_DIND
COPY ./docker-compose.yml ./
WITH DOCKER ...
    ...
END
```

In the above example, the `INSTALL_DIND` command is executed before the `COPY` command, thus ensuring that the Docker installation is cached and reused for subsequent builds when the file `docker-compose.yml` changes.

## Integration testing

For more information on integration testing and working with service dependencies see our [tutorial on integration testing in Earthly](https://docs.earthly.dev/docs/guides/integration).

## Limitations of Docker in Earthly

The current implementation of Docker in Earthly has a number of limitations:

* Only one `RUN` command is allowed within the `WITH DOCKER` clause. The reason for this is that only one cache layer is used for the entire clause. You can, however, chain multiple shell commands together within a single `RUN` command. For example:

  ```Dockerfile
  WITH DOCKER
      RUN command1 && \
          command2 && \
          command3 && \
          ...
  END
  ```

* It is recommended that the target containing the `WITH DOCKER` clause inherits from a supported Docker-in-Docker (dind) image such as `earthly/dind:alpine-3.18-docker-23.0.6-r4` or `earthly/dind:ubuntu-23.04-docker-24.0.5-1`. If your build requires the use of an alternative environment as part of a test (e.g. to run commands like `sbt test` or `go test` together with a docker-compose stack), consider placing the test itself in a Docker image, then loading that image via `--load` and running the test as a Docker container.
* If you do not use an officially supported Docker-in-Docker image, Earthly will attempt to install Docker in whatever image you have chosen. This has the drawback of not being able to use cache efficiently and is not recommended for performance reasons.
* To maximize the use of cache, all external images used should be declared via the options `--pull` or `--compose`. Even though commands such as `docker run` automatically pull an image if it is not found locally, it will do so every single time the `WITH DOCKER` clause is executed, due to Docker caching not being preserved between runs. Pre-declaring the images ensures that they are properly cached by Earthly to minimize unnecessary redownloads.
* `docker build` cannot be used to build Dockerfiles. However, the Earthly command `FROM DOCKERFILE` can be used instead. See [alternative to docker build](#alternative-to-docker-build) below.
* The state of the Docker daemon within Earthly cannot be inspected on the host (e.g. for debugging purposes). For example, if a `docker-compose` stack fails, you cannot execute commands like `docker-compose logs` or `docker logs` on the host. However, you may use the interactive mode to drop into a shell within the build environment and execute such commands there. For more information, see the [debugging guide](https://docs.earthly.dev/docs/guides/debugging).
* It is currently not possible to mount `/var/run/docker.sock` in order to use the host Docker daemon. This goes against Earthly's principles of keeping execution repeatable. Mounting the Docker socket may cause builds to depend on the host Daemon state (e.g. pre-cached images) in ways that may not be obvious or easy to reproduce if the build were executed in another environment.
* Creating external networks (the default docker behavior), will sometimes fail and produce 100% packet loss; however **internal** networks do no have this issue. Use `docker network create --internal ...` or the `internal: true` compose option instead. See [#3495](https://github.com/earthly/earthly/issues/3495) for details.

## Alternatives to Docker in Earthly

It is not always necessary to execute docker commands within an Earthly build. Certain operations can be replicated with Earthly constructs.

### Alternative to docker run

In certain cases, simple `docker run` invocations can be replaced by a simple [`RUN --entrypoint`](https://docs.earthly.dev/earthfile#entrypoint). For example, the following:

```Dockerfile
FROM docker:19.03.13-dind
WITH DOCKER --pull hello-world
    RUN docker run hello-world
END
```

Can be rewritten as

```Dockerfile
FROM hello-world
RUN --entrypoint
```

This, of course, has limitations, such as not being able to mount volumes the same way `docker run -v ...` could (instead, a `COPY` command could be used); or not being able to run multiple containers in parallel. However, when appropriate, it can simplify a build definition.

### Alternative to docker build

Running `docker build` within Earthly is discouraged, as it has a number of key limitations:

* Layer caching does not work. This is because `WITH DOCKER` does not preserve Docker cache between runs (other than `--pull`).
* Once an image is created, it cannot be exported as a build output in a form other than a TAR archive (e.g. it cannot be automatically loaded onto the host Docker daemon).

Instead of executing `docker build`, it is advisable to use the Earthly command `FROM DOCKERFILE`. For example, the command `docker build -t my-image:latest .` can be emulated by:

```Dockerfile
FROM DOCKERFILE .
SAVE IMAGE my-image:latest
```

## See also

* Reference for [`WITH DOCKER`](https://docs.earthly.dev/earthfile#with-docker)
* [Debugging techniques](https://docs.earthly.dev/docs/guides/debugging)
* [Tutorial on integration testing in Earthly](https://docs.earthly.dev/docs/guides/integration)

# Multi-platform builds

Earthly has the ability to perform builds for multiple platforms, in parallel. This page walks through setting up your system to support emulation as well as through a few simple examples of how to use this feature.

Currently only `linux` is supported as the build platform OS. Building with Windows containers will be available in a future version of Earthly.

By default, builds are performed on the same architecture as the runner's native architecture. Using the `--platform` flag across various Earthfile commands or as part of the `earthly` command, it is possible to override the build platform and thus be able to execute builds on non-native processor architectures. Execution of non-native binaries can be performed via QEMU emulation.

In some cases, execution of the build itself does not need to happen on the target architecture, through cross-compilation features of the compiler. Examples of languages that support cross-compilation are Go and Rust. This approach may be more beneficial in many cases, as there is no need to install QEMU and also, the build is more performant.

## Prerequisites for emulation

In order to execute emulated build steps (usually `RUN`), QEMU needs to be installed and set up. This will allow you to perform Earthly builds on non-native platforms, but also incidentally, to run Docker images on your host system through `docker run --platform=...`.

### Windows and Mac

On Mac and on Windows, the Docker Desktop app comes with QEMU readily installed and ready to go, so no special consideration is necessary.

### Apple Silicon (M1 & M2 processors)

Docker for Mac on M1 and M2-based systems uses Rosetta for x86/amd64 emulation. This is **not enabled** by default. To enable it, go to Docker Desktop, open Settings, then Features in Development, and check the box next to "Use Rosetta for x86/amd64 emulation". This will enable emulation for all x86/amd64 containers, including Earthly builds.

![Enabling Rosetta emulation on Apple Silicon-based systems](https://3102854999-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fyi347RZ02JXdgz9BJx5u%2Fuploads%2Fgit-blob-2c174a582ef699995d5e8c617f47048af9d6a46e%2Frosetta.png?alt=media)

### Linux

On Linux, QEMU needs to be installed manually. On Ubuntu, this can be achieved by running:

```bash
sudo apt-get install qemu-system binfmt-support qemu-user-static
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker stop earthly-buildkitd || true
```

The `docker run` command above enables execution of different multi-architecture containers by QEMU and `binfmt_misc`. It only needs to be run once.

### GitHub Actions

To make use of emulation in GitHub Actions, the following step needs to be included in every job that performs a multi-platform build:

```yaml
jobs:
  <job-name>:
    steps:
      - name: Set up QEMU
        id: qemu
        uses: docker/setup-qemu-action@v1
        with:
          image: tonistiigi/binfmt:latest
          platforms: all
      - uses: actions/checkout@v3
      - ...
```

## Performing multi-platform builds

In order to execute builds for multiple platforms, the execution may be parallelized through the repeated use of the `BUILD --platform` flag. For example:

```Dockerfile
build-all-platforms:
    BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build

build:
    ...
```

If the `+build` target were invoked without the use of any flag, Earthly would simply perform the build on the native architecture of the host system.

However, invoking the target `+build-all-platforms` causes `+build` to execute twice, in parallel: one time on `linux/amd64` and another time on `linux/arm/v7`.

You may also override the target platform when issuing the `earthly` build command. For example:

```bash
earthly --platform=linux/arm64 +build
```

This would cause the build to execute on the `linux/arm64` architecture.

## Saving multi-platform images

The easiest way to include platform information as part of a build is through the use of `FROM --platform`. For example:

```Dockerfile
FROM --platform=linux/arm/v7 alpine:3.18
```

If multiple targets create an image with the same name, but for different platforms, the images will be merged into a multi-platform image during export. For example:

```Dockerfile
build-all-platforms:
    BUILD +build-amd64
    BUILD +build-arm-v7

build-amd64:
    FROM --platform=linux/amd64 alpine:3.18
    ...
    SAVE IMAGE --push org/myimage:latest

build-arm-v7:
    FROM --platform=linux/arm/v7 alpine:3.18
    ...
    SAVE IMAGE --push org/myimage:latest
```

When `earthly --push +build-all-platforms` is executed, the build will push a multi-manifest image to the Docker registry. The manifest will contain two images: one for `linux/amd64` and one for `linux/arm/v7`. This works as such because both targets that save images use the exact same Docker tag for the image.

Of course, in some situations, the build steps are the same (except they run on different platform), so the two definitions can be merged like so:

```Dockerfile
build-all-platforms:
    BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build

build:
    FROM alpine:3.18
    ...
    SAVE IMAGE --push org/myimage:latest
```

A more complete version of this example is available in [examples/multiplatform](https://github.com/earthly/earthly/tree/main/examples/multiplatform) in GitHub. You may try out this example without cloning by running

```bash
earthly github.com/earthly/earthly/examples/multiplatform:main+all
docker run --rm earthly/examples:multiplatform
docker run --rm earthly/examples:multiplatform_linux_amd64
docker run --rm earthly/examples:multiplatform_linux_arm_v7
```

{% hint style="info" %}
**Note**

As of the time of writing this article, the `docker` CLI has limited support for working with multi-manifest images locally. For this reason, when exporting an image to the local Docker daemon, Earthly provides the different architectures as different Docker tags.

For example, the above build would yield locally:

* `org/myimage:latest`
* `org/myimage:latest_linux_amd64` (the same as `org/myimage:latest` if running on a `linux/amd64` host)
* `org/myimage:latest_linux_arm_v7`

The additional Docker tags are only available for use on the local system. When pushing an image to a Docker registry, it is pushed as a single multi-manifest image.
{% endhint %}

## Creating multi-platform images without emulation

Building multi-platform images does not necessarily require that execution of the build itself takes place on the target platform. Through the use of cross-compilation, it is possible to obtain target-platform binaries compiled on the host-native platform. At the end, these binaries may be placed in a final image which is marked for a specific platform.

Note, however, that not all programming languages have support for cross-compilation. The applicability of this approach may be limited as a result. Examples of languages that *can* cross-compile for other platforms are Go and Rust.

Here is an example where a multi-platform image can be created without actually executing any `RUN` on the target platform (and therefore emulation is not necessary):

```Dockerfile
build-all-platforms:
    BUILD +build-amd64
    BUILD +build-arm-v7

build:
    FROM golang:1.15-alpine3.13
    WORKDIR /example
    ARG GOOS=linux
    ARG GOARCH=amd64
    ARG GOARM
    COPY main.go ./
    RUN go build -o main main.go
    SAVE ARTIFACT ./main

build-amd64:
    FROM --platform=linux/amd64 alpine:3.18
    COPY +build/main ./example/main
    ENTRYPOINT ["/example/main"]
    SAVE IMAGE --push org/myimage:latest

build-arm-v7:
    FROM --platform=linux/arm/v7 alpine:3.18
    COPY \
        --platform=linux/amd64 \
        (+build/main --GOARCH=arm --GOARM=v7) ./example/main
    ENTRYPOINT ["/example/main"]
    SAVE IMAGE --push org/myimage:latest
```

The key here is the use of the `COPY` commands. The execution of the target `+build` may take place on the host platform (in this case, `linux/amd64`) and yet produce binaries for either `amd64` or `arm/v7`. Since there is no `RUN` command as part of the `+build-arm-v7` target, no emulation is necessary.

## Making use of builtin platform args

A number of [builtin build args](https://docs.earthly.dev/docs/earthfile/builtin-args) are made available to be used in conjunction with multi-platform builds:

* `TARGETPLATFORM` (eg `linux/arm/v7`)
* `TARGETOS` (eg `linux`)
* `TARGETARCH` (eg `arm`)
* `TARGETVARIANT` (eg `v7`)

Here is an example of how the build described above could be simplified through the use of these build args:

```Dockerfile
build-all-platforms:
    BUILD --platform=linux/amd64 --platform=linux/arm/v7 +build-image

build:
    FROM golang:1.15-alpine3.13
    WORKDIR /example
    ARG GOOS=linux
    ARG GOARCH=amd64
    ARG VARIANT
    COPY main.go ./
    RUN GOARM=${VARIANT#"v"} go build -o main main.go
    SAVE ARTIFACT ./main

build-image:
    ARG TARGETPLATFORM
    ARG TARGETARCH
    ARG TARGETVARIANT
    FROM --platform=$TARGETPLATFORM alpine:3.18
    COPY \
        --platform=linux/amd64 \
        (+build/main --GOARCH=$TARGETARCH --VARIANT=$TARGETVARIANT) ./example/main
    ENTRYPOINT ["/example/main"]
    SAVE IMAGE --push org/myimage:latest
```

The code of this example is available in [examples/multiplatform-cross-compile](https://github.com/earthly/earthly/tree/main/examples/multiplatform-cross-compile) in GitHub. You may try out this example without cloning by running

```bash
earthly github.com/earthly/earthly/examples/multiplatform-cross-compile:main+build-all-platforms
```

### USER platform args

Additional `USER` [builtin build args](https://docs.earthly.dev/docs/earthfile/builtin-args) can be used to determine the architecture of the host that called `earthly`. This can be useful to determine if cross-platform emulation was used.

* `USERPLATFORM` (eg `linux/amd64`)
* `USEROS` (eg `linux`)
* `USERARCH` (eg `amd64`)
* `USERVARIANT` (eg \`\`; an empty string for non-arm platforms)

## Emulation and WITH DOCKER

Please note that `WITH DOCKER` has an important limitation for cross-platform builds: the target containing `WITH DOCKER` needs to be executing on the native architecture of the runner. The images being run within `WITH DOCKER` can be of any architecture, however.

In other words, the following will **NOT** work on amd64:

```Dockerfile
# Does not work!
build:
    FROM --platform=linux/arm64 earthly/dind
    WITH DOCKER --pull=earthly/examples:multiplatform
        RUN docker run earthly/examples:multiplatform
    END
```

However, the following will:

```
build:
    FROM earthly/dind
    WITH DOCKER --pull=earthly/examples:multiplatform
        RUN docker run --platform=linux/arm64 earthly/examples:multiplatform
    END
```

The reason for this is that behind the scenes `WITH DOCKER` starts up an isolated Docker daemon running within a container, and docker-in-docker is not yet supported in a QEMU environment.

# Authenticating Git and image registries

This page guides you through passing Git and Docker authentication to Earthly builds, to empower related Earthly features, like `GIT CLONE` or `FROM`.

{% hint style="danger" %}
**Important**

This page is NOT about passing Git or Docker credentials for your own custom commands within builds. For those cases, use the [`RUN --secret`](https://docs.earthly.dev/earthfile#run) feature.
{% endhint %}

## Git authentication

A number of Earthly features use Git credentials to perform remote Git operations:

* Resolving a build context when referencing remote targets
* The `GIT CLONE` command

There are two possible ways to pass Git authentication to Earthly builds:

* Via SSH agent socket (for SSH-based authentication)
* Via username-password (usually for HTTPS Git URLs)

#### Auto authentication

Earthly defaults to an `auto` authentication mode, where ssh-based authentication is automatically attempted, and falls back to https-based cloning.

{% hint style="info" %}
If you are having trouble accessing a private repository and want to use ssh-based authentication, first make sure `ssh-agent` is running and the `SSH_AUTH_SOCK` environment variable is set. If not, you can start it with `eval $(ssh-agent)`.

Next make sure your private key has been added by running `ssh-add <path to key>`.
{% endhint %}

For users who want explicit control over git authentication, the following sections explain how.

#### SSH agent socket

Earthly uses the environment variable `SSH_AUTH_SOCK` to detect where the SSH agent socket is located and mounts that socket to the BuildKit daemon container. (As an exception, on Mac, Docker's compatibility SSH auth socket is used instead).

If you need to override the SSH agent socket, you can set the environment variable `EARTHLY_SSH_AUTH_SOCK`, or use the `--ssh-auth-sock` flag to point to an alternative SSH agent.

In order for the SSH agent to have the right credentials available, make sure you run `ssh-add` before executing Earthly builds.

Another key setting is the `auth` mode for the git site that hosts the repository. By default earthly automatically default to `ssh` authentication if the ssh auth agent is running and has at least 1 key loaded, otherwise `earthly` will fallback to using non-authenticated HTTPS.

Sites can be explicitly added to the [earthly config file](https://docs.earthly.dev/docs/earthly-config) under the git section in order to override the auto-authentication mode:

```yaml
git:
    git.example.com:
        auth: ssh
        user: git
```

#### Username-password authentication

Username-password based authentication can be configured in the [earthly config file](https://docs.earthly.dev/docs/earthly-config) under the git section:

```yaml
git:
    github.com:
        auth: https
        user: <username>
        password: <password>
    gitlab.com:
        auth: https
        user: <username>
        password: <password>
```

If no `user` or `password` are found, earthly will check for entries under [`~/.netrc`](https://everything.curl.dev/usingcurl/netrc).

**Global override via environment variables (deprecated)**

Alternatively, environment variables can be set which will be override all host entries from the config file:

* `GIT_USERNAME`
* `GIT_PASSWORD`

However, environment variable authentication are now deprecated in favor of using the configuration file instead.

#### Self-hosted and private Git Repositories

Currently, `github.com`, `gitlab.com`, and `bitbucket.org` have been tested as SCM providers. Without any host-specific configuration, Earthly first attempts to perform a clone over SSH on the default SSH port (22), and will fallback to HTTPS, followed by HTTP. In the event access can only be established over HTTP, Earthly will refuse to send credentials due to the insecure nature of HTTP.

Earthly can be configured to use a non-standard SSH port, by using the `port` config option:

```yaml
git:
    ghe.internal.mycompany.com:
        auth: ssh
        user: git
        port: 2222
```

When Earthly encounters a remote reference such as `ghe.internal.mycompany.com/user/repo+some-target`, the git repository will be cloned using an explicit SSH scheme, for example: `git clone ssh://git@ghe.internal.mycompany.com:2222/user/repo.git`.

The explicit ssh-scheme is an absolute path on the server's file-system; if the git repositories are located in a different location (e.g. `/var/git/...`), a `prefix` configuration option can be specified.

{% hint style="info" %}
**Remapping Git Repositories Paths Using Regular Expressions**

The `port` and `prefix` configuration options are the preferred way to configure self-hosted git repositories; however prior to the introduction of these options, it was suggested to use a regular expression and substitution pattern:

```yaml
git:
    ghe.internal.mycompany.com:
        pattern: 'ghe.internal.mycompany.com/([^/]+)/([^/]+)'
        substitute: 'ssh://git@ghe.internal.mycompany.com:22/$1/$2.git'
        auth: ssh
```

{% endhint %}

#### GitLab Subgroups

Earthly, by default, assumes git repos are stored under two levels (i.e. `<org>/<path>.git`). A regular expression must be configured in order to support sub groups:

```yaml
git:
    gitlab.com:
        pattern: 'gitlab.com/(example-org)/([^/]+)/([^/]+)'
        substitute: 'git@gitlab.com:$1/$2/$3.git'
        auth: ssh
```

Where `example-org` is the name of your GitLab organisation. Note that the `(` and `)` parenthesis are required, as they are used to assign the matched value to the `$1`, `$2`, ... values.

The pattern will depend on how your subgroups are setup; if you use a mix of 2 and 3 level groupings, you will have to configure them separately:

```yaml
git:
    gitlab.com/example-org/projecta:
        pattern: 'gitlab.com/(example-org)/(project-a)/([^/]+)'
        substitute: 'git@gitlab.com:$1/$2/$3.git'
        auth: ssh

    gitlab.com example-org catch-all:
        pattern: 'gitlab.com/(example-org)/([^/]+)'
        substitute: 'git@gitlab.com:$1/$2.git'
        auth: ssh
```

When a `pattern` is used, the key of the git configuration is simply used by log messages, it is **not** used for any matching.

Note that patterns are evaluated from the top to the bottom, subgroup specific configurations should be listed first.

#### Debugging tips

You can run earthly with `--verbose`, which will provide debugging messages to help understand how a remote earthly reference is transformed into a git URL for cloning.

You can additionally enable low-level git debugging in buildkit, by adding the following to your `~/.earthly/config.yml`:

```yaml
global:
  buildkit_additional_args: [ '-e', 'BUILDKIT_DEBUG_GIT=1' ]
```

The buildkit logs can be displayed with `docker logs earthly-buildkitd`.

## Docker authentication

Docker credentials are used in Earthly for inheriting from private images (via `FROM`) and for pushing images (via `SAVE IMAGE --push`).

Docker authentication works automatically out of the box. It uses the same Docker libraries to infer the location of the credentials on the system and optionally invoke any necessary credentials store helper to decrypt them.

### Manually

All you have to do as a user is issue the command

```bash
docker login --username <username>
```

before issuing earthly commands, if you have not already done so in the past. If you run into troubles, [you can find out more about `docker login` here](https://docs.docker.com/engine/reference/commandline/login/).

### Credential Helpers

Docker can use various credential helpers to automatically generate and use credentials on your behalf. These are usually created by cloud providers to allow Docker to authenticate using the cloud providers own credentials.

You can see examples of configuring Docker to use these, and working with Earthly here:

* [Pushing and Pulling Images with AWS ECR](https://docs.earthly.dev/docs/guides/configuring-registries/aws-ecr)
* [Pushing and Pulling Images with GCP Artifact Registry](https://docs.earthly.dev/docs/guides/configuring-registries/gcp-artifact-registry)
* [Pushing and Pulling Images with Azure ACR](https://docs.earthly.dev/docs/guides/configuring-registries/azure-acr)

## See also

* The [earthly command reference](https://docs.earthly.dev/docs/earthly-command)

# Integration Testing

Running unit tests in a build pipeline is relatively simple. By definition, unit tests have no external dependencies. Things get more interesting when we want to test how our service integrates with other services and external systems. A service may have dependencies on external file systems, on databases, on external message queues, or other services. An ergonomic and effective development environment should have simple ways to construct and run integration tests. It should be easy to run these tests locally on the developer machine and in the build pipeline.

\*\* This guide will take an existing application with integration tests and show how they can be easily run inside earthly, both in the local development environment as well as in the build pipeline. \*\*

## Prerequisites

*This integration approach can work with most applications and development stacks. See* [*examples*](https://github.com/earthly/earthly/tree/main/examples) *for guidance on using earthly in other languages.*

### Our Application

The application we start with is simple. It returns the first 5 countries alphabetically via standard out. It has unit tests and integration tests. The integration tests require a datastore with the correct data in place.

### The Basic Earthfile

We start with a simple Earthfile that can build and create a docker image for our app. See the [Basics guide](https://docs.earthly.dev/basics) for more details, as well as examples in many programming languages.

See the [Basics Guide](https://docs.earthly.dev/basics) for more details on these steps, including how they might differ in Go, JavaScript, Java, and Python.

## In-App Integration Testing

Since our service has a docker-compose file of dependencies, running integration tests is easy.

Our integration target needs to copy in our source code and our Dockerfile and then inside a `WITH DOCKER` start the tests:

```Dockerfile
integration-test:
    FROM +project-files
    COPY src src
    COPY docker-compose.yml ./ 
    WITH DOCKER --compose docker-compose.yml
        RUN while ! pg_isready --host=localhost --port=5432 --dbname=iso3166 --username=postgres; do sleep 1; done ;\
            sbt it:test
    END
```

The `WITH DOCKER` has a `--compose` flag that we use to start up our docker-compose and run our integration tests in that context.

We can now run our tests both locally and in the CI pipeline, in a reproducible way:

```bash
> earthly -P +integration-test
+integration-test | Creating local-postgres ... done
+integration-test | Creating local-postgres-ui ... done
+integration-test | +integration-test | [info] Loading settings for project scala-example-build from plugins.sbt ...
+integration-test | [info] DatabaseIntegrationTest:
+integration-test | [info] A table
+integration-test | [info] - should have country data
+integration-test | [info] Run completed in 7 seconds, 923 milliseconds.
+integration-test | [info] Tests: succeeded 1, failed 0, canceled 0, ignored 0, pending 0
+integration-test | Stopping local-postgres-ui ... done
+integration-test | Stopping local-postgres    ... done
+integration-test | Removing local-postgres-ui ... done
+integration-test | Removing local-postgres    ... done
+integration-test | Removing network scala-example_default
+integration-test | Target github.com/earthly/earthly-example-scala/integration:main+integration-test built successfully
...
```

This means that if an integration test fails in the build pipeline, you can easily reproduce it locally.

## End to End Integration Tests

Our first integration test used was part of the service we were testing. This is one way to exercise integration code paths. Another useful form of integration testing is end-to-end testing. In this form of integration testing, we start up the application and test it from the outside.

In our simplified case example, with a single code path, a test that verifies the application starts and produces the desired output is sufficient.

Output: We can then run this and check that our application with its dependencies, produces the correct output.

```Dockerfile
> earthly -P +smoke-test
+smoke-test | --> WITH DOCKER RUN for i in {1..30}; do nc -z localhost 5432 && break; sleep 1; done; docker run --network=host earthly/examples:integration
+smoke-test | Loading images...
+smoke-test | Loaded image: aa8y/postgres-dataset:iso3166
+smoke-test | Loaded image: adminer:latest
+smoke-test | Loaded image: earthly/examples:integration
+smoke-test | ...done
+smoke-test | Creating network "scala-example_default" with the default driver
+smoke-test | Creating local-postgres ... done
+smoke-test | Creating local-postgres-ui ... done
+smoke-test | +smoke-test | The first 5 countries alphabetically are: Afghanistan, Albania, Algeria, American Samoa, Andorra
+smoke-test | Stopping local-postgres-ui ... done
+smoke-test | Stopping local-postgres    ... done
+smoke-test | Removing local-postgres-ui ... done
+smoke-test | Removing local-postgres    ... done
+smoke-test | Removing network scala-example_default
+smoke-test | Target github.com/earthly/earthly-example-scala/integration:main+smoke-test built successfully
=========================== SUCCESS ===========================
...
```

## Bringing It All Together

Adding these testing targets to an all target, we now can unit test, integration test, and dockerize and push our software in a single command. Using this approach, integration tests that fail sporadically for environmental reasons and can't be reproduced consistently should be a thing of the past.

```Dockerfile
all:
  BUILD +build
  BUILD +unit-test
  BUILD +integration-test
  BUILD +smoke-test
```

```bash
> earthly -P +all
...
+all | Target github.com/earthly/earthly-example-scala/integration:main+all built successfully
=========================== SUCCESS ===========================
```

There we have it, a reproducible integration process. If you have questions about the example, [ask](https://gitter.im/earthly-room/community)

## See also

* [Docker In Earthly](https://docs.earthly.dev/docs/guides/docker-in-earthly)
* [Source code for example](https://github.com/earthly/earthly/tree/main/examples/integration-test)
* [Integration Testing vs Unit Testing](https://blog.earthly.dev/unit-vs-integration/)

# Debugging techniques

Traditional debugging of errors during image builds often require a developer to place various print commands through out the build commands to help reason about the state of the system before the failure occurs. This can be slow and cumbersome.

Earthly provides an interactive mode which gives you access to a root shell when an error occurs, which we'll cover in this guide.

Let's consider a test example that prints out a randomly generated phrase:

```Dockerfile
# Earthfile

VERSION 0.7
FROM python:3
WORKDIR /code

test:
  RUN curl https://raw.githubusercontent.com/jsvine/markovify/master/test/texts/sherlock.txt > /sherlock.txt
  COPY generate_phrase.py .
  RUN pip3 install markovify
  RUN python3 generate_phrase.py
```

and our python code:

```Python
# generate_phrase.py

import markovify
text = open('sherlock.txt').read()
text_model = markovify.Text(text)
print(text_model.make_sentence())
```

Now we can run it with `earthly +test`, and we'll see a failure has occurred:

```
=========================== FAILURE ===========================
+test *failed* | --> RUN python3 generate_phrase.py
+test *failed* | Traceback (most recent call last):
+test *failed* |   File "generate_phrase.py", line 3, in <module>
+test *failed* |     text = open('sherlock.txt').read()
+test *failed* | FileNotFoundError: [Errno 2] No such file or directory: 'sherlock.txt'
+test *failed* | Command /bin/sh -c python3 generate_phrase.py failed with exit code 1
+test *failed* | +test *failed* | ERROR: Command exited with non-zero code: RUN python3 generate_phrase.py
Error: solve side effects: solve: failed to solve: rpc error: code = Unknown desc = executor failed running [/bin/sh -c  /usr/bin/earth_debugger /bin/sh -c 'python3 generate_phrase.py']: buildkit-runc did not terminate successfully
```

Why can't it find the sherlock.txt file? Let's re-run `earthly` with the `--interactive` (or `-i`) flag: `earthly -i +test`

This time we see a slightly different message:

```
+test | --> RUN python3 generate_phrase.py
+test | Traceback (most recent call last):
+test |   File "generate_phrase.py", line 3, in <module>
+test |     text = open('sherlock.txt').read()
+test | FileNotFoundError: [Errno 2] No such file or directory: 'sherlock.txt'
+test | Command /bin/sh -c python3 generate_phrase.py failed with exit code 1
+test | Entering interactive debugger (**Warning: only a single debugger per host is supported**)
+test | root@buildkitsandbox:/code#
```

This time rather than exiting, earthly will drop us into an interactive root shell within the container of the build environment. This root shell will allow us to execute arbitrary commands within the container to figure out the problem:

```
root@buildkitsandbox:/code# ls
generate_phrase.py
root@buildkitsandbox:/code# find / | grep sherlock.txt
/sherlock.txt
root@buildkitsandbox:/code# ls /
bin  boot  code  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  sherlock.txt  srv sys  tmp  usr  var
root@buildkitsandbox:/code# ls /sherlock.txt
/sherlock.txt
```

Ah ha! the corpus text file was located in the root directory rather than under `/code`. We can try moving it manually to see if that fixes the problem:

```
root@buildkitsandbox:/code# mv /sherlock.txt /code/.
root@buildkitsandbox:/code# python3 generate_phrase.py
I struck him down with the servants and with the lantern and left a fragment in the midst of my work during the last three years, although he has cruelly wronged.
```

At this point we know what needs to be done to fix the test, so we can type exit (or ctrl-D), to exit the interactive shell.

```
+test | time="2020-09-16T22:23:53Z" level=error msg="failed to read from ptmx: read /dev/ptmx: input/output error"
+test | time="2020-09-16T22:23:53Z" level=error msg="failed to read data from conn: read tcp 127.0.0.1:36672->127.0.0.1:5000: use of closed network connection"
+test | ERROR: Command exited with non-zero code: RUN python3 generate_phrase.py
```

Note that even though we fixed the problem during debugging, the image will not have been saved, so we must go back to our Earthfile and fix the problem there:

```Dockerfile
# Earthfile

VERSION 0.7
FROM python:3
WORKDIR /code

test:
  RUN curl https://raw.githubusercontent.com/jsvine/markovify/master/test/texts/sherlock.txt > /code/sherlock.txt
  COPY generate_phrase.py .
  RUN pip3 install markovify
  RUN python3 generate_phrase.py
```

## Debugging integration tests

Let's consider a more complicated example where we are running integration tests within an embedded docker setup:

```Dockerfile
# Earthfile

VERSION 0.7

server:
  COPY server.py .

test:
  FROM docker:19.03.12-dind
  RUN apk add curl
  WITH DOCKER --load server:latest=+server
    RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep hello
  END

```

and our server.py code:

```Python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
```

Let's fire up our integration test with `earthly -P -i +test`:

```
buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
+base | --> FROM python:3
context | --> local context .
+base | resolve docker.io/library/python:3@sha256:e9b7e3b4e9569808066c5901b8a9ad315a9f14ae8d3949ece22ae339fff2cad0 100%
context | transferring .: 100%
+base | *cached* --> WORKDIR /code
+server | *cached* --> COPY server.py .
+test | --> FROM docker:19.03.12-dind
+test | resolve docker.io/library/docker:19.03.12-dind@sha256:674f1f40ff7c8ac14f5d8b6b28d8fb1f182647ff75304d018003f1e21a0d8771 100%
+test | *cached* --> RUN apk add curl
+test | --> WITH DOCKER RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep hello
+test | Loading images...
+test | Loaded image: server:latest
+test | ...done
+test | 1dc054c647cb75bde4897a2828edb095739cb9f864ed203ed2ddb54e62554aad
+test | Command /bin/sh -c docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep hello failed with exit code 1
+test | Entering interactive debugger (**Warning: only a single debugger per host is supported**)
```

There was a failure checking that the server output contained the string `hello`; let's see what is going on:

```
/ # docker ps -a
CONTAINER ID        IMAGE               COMMAND               CREATED             STATUS              PORTS               NAMES
b8a31c54dd17        server:latest       "python3 server.py"   5 seconds ago       Up 4 seconds                            frosty_rhodes
```

The good news is our server container is running; let's see what happens when we try to connect to it:

```
/ # curl -s localhost:8000
Hello, world!/ 
```

Ah ha! The problem is our test is expecting a lowercase `h`, so we can fix our grep to look for an uppercase `H`:

```Dockerfile
# Earthfile

VERSION 0.7

server:
  COPY server.py .

test:
  FROM docker:19.03.12-dind
  RUN apk add curl
  WITH DOCKER --load server:latest=+server
    RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep Hello
  END
```

Then when we re-run our test we get:

```
+test | --> WITH DOCKER RUN docker run --rm -d --network=host server:latest python3 server.py && sleep 5 && curl -s localhost:8000 | grep Hello
+test | Loading images...
+test | Loaded image: server:latest
+test | ...done
+test | cb5299ae03cd17cfb2b528f01268ccf59761feec036cb313a3e969930d6f0815
+test | Hello, world!
+test | Target +test built successfully
=========================== SUCCESS ===========================
```

With the use of the interactive debugger; we were able to examine the state of the embedded containerized

## Demo

[![asciicast](https://asciinema.org/a/361170.svg)](https://asciinema.org/a/361170?speed=2)

## Final tips

If you ever want to jump into an interactive debugging session at any point in your Earthfile, you can simply add a command that will fail such as:

```
  RUN false
```

and run earthly with the `--interactive` (or `-i`) flag.

Hopefully you won't run into failures, but if you do the interactive debugger may help you discover the root cause more easily. Happy coding.

# Podman

[Podman](https://podman.io/) is an alternative to docker; it's a daemonless container engine for developing, managing and running OCI containers on a Linux system. Podman also works on Mac using a [podman machine](https://docs.podman.io/en/latest/markdown/podman-machine.1.html).

## Prerequisites

* [Install podman](https://podman.io/getting-started/installation)
* Mac: ensure a [podman machine](https://docs.podman.io/en/latest/markdown/podman-machine.1.html) is running.
* Linux: for [multi-platform builds](https://docs.earthly.dev/docs/guides/multi-platform), install [qemu-user-static](https://github.com/multiarch/qemu-user-static).
* [WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker) requires rootful mode.
  * Linux: run with `sudo` (i.e., `sudo earthly -P +with-docker-target`)
  * Mac: run a [rootful machine](https://docs.podman.io/en/latest/markdown/podman-machine-set.1.html#rootful).

## Getting started

When earthly starts a check is done to determine what frontend is available. By default, earthly will attempt to use docker and then fall back to podman. If you wish to change the behavior of the startup check, run the following command:

```bash
# Configure earthly to use podman
earthly config global.container_frontend podman-shell

# Configure earthly to use docker
earthly config global.container_frontend docker-shell
```

You can verify the command worked by checking the `~/.earthly/config.yml` file and verifying it contains a `container_frontend` entry.

```bash
> cat ~/.earthly/config.yml
global:
    container_frontend: podman-shell
```

Then, you can run a basic hello world example to see earthly using the appropriate container frontend.

```bash
> earthly github.com/earthly/hello-world:main+hello
 1. Init 🚀
————————————————————————————————————————————————————————————————————————————————

           buildkitd | Starting buildkit daemon as a podman container (earthly-buildkitd)...
           buildkitd | ...Done
```

If instead you see `No frontend initialized`, and you're using Mac, it may mean your podman machine is not running.

## Known limitations / troubleshooting

### Builds running slowly

There are a few steps you should take to rule out common performance bottlenecks.

#### Mac: check podman resources

At the time of writing this, podman machines use a single core and 2GB of RAM by default. Depending on what you're doing you may need more resources.

Resources can be adjusted by using one of these commands:

```bash
# Initialize a new default machine with 5 CPUs, 128GB disk space, 8196 MB of memory, and start it
podman machine init --now --cpus 5 --disk-size 128 --memory 8196 

# Adjust the current default podman machine to use 5 CPUs, 128GB disk space, and 8196 MB of memory
podman machine stop ; podman machine set --cpus 5 --disk-size 128 --memory 8196 && podman machine start
```

### Mac: check machine architecture

Running `podman version` will display the specifications of your podman client and server (machine). You should ensure the architecture in OS/Arch is the same between client and server. This will rule out emulation as a performance bottleneck.

The output may look like this:

```bash
> podman version
Client:       Podman Engine
Version:      4.2.1
API Version:  4.2.1
Go Version:   go1.18.6
Built:        Tue Sep  6 13:16:02 2022
OS/Arch:      darwin/arm64

Server:       Podman Engine
Version:      4.2.0
API Version:  4.2.0
Go Version:   go1.18.4
Built:        Thu Aug 11 08:43:11 2022
OS/Arch:      linux/arm64
```

In this example, the client us running on an M1 Mac and both the client and server are using arm64.

### Check graph driver

Running `podman info --debug` will show your current podman configuration. VFS and other drivers can perform poorly when compared to overlay and [are not recommended by the podman community](https://github.com/containers/podman/issues/13226). Ensure overlay is used by looking for the following in the podman info output:

```bash
> podman info --debug

...
graphDriverName: overlay  # or something similar
...
```

### Mac: docker-credential-desktop: executable file not found in $PATH

This error typically occurs when switching from docker desktop to podman without docker installed. There may be a lingering configuration file that will be read by the attachable used to authenticate calls to buildkit.

To fix this issue, try removing or renaming the `~/.docker/config.json` file.

### Earthly CLI - no frontend initialized

Seeing the error on startup means the check for podman has failed.

```bash
> earthly github.com/earthly/hello-world:main+hello
 1. Init 🚀
————————————————————————————————————————————————————————————————————————————————

            frontend | No frontend initialized.
```

Ensure you have correctly installed podman and, if you are using a Mac, the podman machine is running.

```bash
> podman machine start
```

### Rootless podman

Running podman in rootless mode is not supported due to the [earthly/dind](https://hub.docker.com/r/earthly/dind) and [earthly/buildkit](https://hub.docker.com/r/earthly/buildkitd) because they [require privileged access](https://docs.earthly.dev/docs/guides/using-the-earthly-docker-images/buildkit-standalone#requirements). Specifically, [WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker) will fail. You must use `sudo` on Linux or [set your podman machine to rootful mode on Mac](https://docs.podman.io/en/latest/markdown/podman-machine-set.1.html#rootful) to use [WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker).

### Podman within WITH DOCKER

[WITH DOCKER](https://docs.earthly.dev/docs/earthfile#with-docker) starts a container with a docker installation. You can only use the podman CLI in the RUN statement if you specify [LOCALLY](https://docs.earthly.dev/best-practices#pattern-optionally-locally) to run it on the host machine; otherwise, you will need to use the docker CLI.

```bash
docker-locally:
   LOCALLY
   WITH DOCKER
     RUN podman ps
   END
```

```bash
docker:
   WITH DOCKER
     RUN docker ps
   END
```

### Cross-image targets

You need to configure QEMU if you are running a cross-platform target. If you haven't properly configured QEMU you will receive an error message containing the following message:

```bash
> earthly +cross-platform
...
exec /bin/sh: exec format error
...
```

We've found installing [qemu-user-static](https://github.com/multiarch/qemu-user-static) will allow cross-platform targets tun run on Linux.

```bash
> apt-get install qemu-user-static
# or
> yum install qemu-user-static
```

### crun: open executable: Permission denied: OCI permission denied

This can happen if you attempt to run (or the `ENTRYPOINT` references) a binary without the execution permission. <https://github.com/containers/podman/issues/9377> <https://github.com/signalwire/freeswitch/pull/1748>

# Configuring registries

# AWS ECR

## Introduction

The AWS Elastic Container Registry (ECR) is a hosted docker repository that requires extra configuration for day-to-day use. This configuration is not typical of other repositories, and there are some considerations to account for when using it with Earthly. This guide will walk you through creating an Earthfile, building an image, and pushing it to ECR.

This guide assumes you have already installed the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), and [created a new repository named hello-earthly](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.18

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
```

## Install and Configure the ECR Credential Helper

ECR does not issue permanent credentials. Instead, it relies on your AWS credentials to issue docker credentials. You can follow [instructions to log in with generated credentials](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login.html), but the process will need to be repeated every 12 hours. In practice, this often means lots of glue code in your CI pipeline to keep credentials up to date.

[AWS has released a credential helper to ease logging into ECR](https://github.com/awslabs/amazon-ecr-credential-helper). It may be that you already have the credential helper installed, since it has been included with Docker Desktop as of version [2.4.0.0](https://docs.docker.com/docker-for-windows/release-notes/#docker-desktop-community-2400). If not, you can follow installation instructions on their GitHub repository here. Here is a sample `.docker/config.json` to enable the usage of this helper:

```
{
        "credHelpers": {
                "<aws_account_id>.dkr.ecr.<region>.amazonaws.com": "ecr-login"
        }
}

```

## IAM

Ensure that you have correct permissions to push the images. The ECR helper is aware of the `AWS_PROFILE` variable; and can work under an assumed role. Here is a minimum set of privileges needed to push to ECR from Earthly:

```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AllowPushPull",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::<aws_account_id>:user/push-pull-user",
                ]
            },
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload"
            ]
        }
    ]
}
```

Additional [examples](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) for policy configuration.

## Run the Target

With the helper installed, no special To build and push an image, simply execute the build target. Don't forget the `--push` flag!

```
❯ earthly --push +build
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
         alpine:3.18 | --> Load metadata linux/amd64
               +base | --> FROM alpine:3.18
               +base | [██████████] resolve docker.io/library/alpine:3.18@sha256:0bd0e9e03a022c3b0226667621da84fc9bf562a9056130424b5bfbd8bcb0397f ... 100%
              +build | --> RUN echo "Hello from Earthly!" > motd
              output | --> exporting outputs
              output | [██████████] exporting layers ... 100%
              output | [██████████] exporting manifest sha256:9ab4df74dafa2a71d71e39e1af133d110186698c78554ab000159cfa92081de4 ... 100%
              output | [██████████] exporting config sha256:6feef98708c14c000a6489a2a99315a5328c2c16091851ae10438b53f655d042 ... 100%
              output | [██████████] pushing layers ... 100%
              output | [██████████] pushing manifest for <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love ... 100%
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================
Loaded image: <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
              +build | Image +build as <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love (pushed)

```

## Pulling Images

Using this credential helper; you can also pull images without any special handling in an Earthfile:

```
FROM earthly/dind:alpine-3.18-docker-23.0.6-r4

run:
    WITH DOCKER --pull <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
        RUN docker run <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
    END
```

And here is how you would run it:

```
❯ earthly -P +run
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
 earthly/dind:alpine-3.18-docker-23.0.6-r4 | --> Load metadata linux/amd64
4/hello-earthly:with-love | --> Load metadata linux/amd64
4/hello-earthly:with-love | --> DOCKER PULL <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
4/hello-earthly:with-love | [██████████] resolve <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love@sha256:9ab4df74dafa2a71d71e39e1af133d110186698c78554ab000159cfa92081de4 ... 100%
               +base | --> FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
               +base | [██████████] resolve docker.io/earthly/dind:alpine-3.18-docker-23.0.6-r4@sha256:2cef4089960efe028de40721749e3ec6eba9f471562bf10681de729287bd78fb ... 100%
                +run | *cached* --> WITH DOCKER (install deps)
                +run | *cached* --> WITH DOCKER RUN docker run <aws_account_id>.dkr.ecr.<region>.amazonaws.com/hello-earthly:with-love
              output | --> exporting outputs
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================
```

## Troubleshooting

### Basic Credentials Not Found

If you get a message saying `basic credentials not found`; your distribution may not have the most recent version installed. A simple workaround is to simply prepend `AWS_SDK_LOAD_CONFIG=true` to your Earthly invocation. This will force the helper to use the SDK over built-in config when executing. You can track this [issue](https://github.com/awslabs/amazon-ecr-credential-helper/issues/232).

### 401 Unauthorized

Double-check your AWS credentials, to ensure you have the correct ones set up. `aws configure` can help you do this. Also, check IAM to ensure you have the correct permissions (see the [IAM](#iam) section above). Finally, if you use IAM assumed roles, ensure that you have assumed the correct role in your terminal session.

If these are in order, the same fix from [Basic Credentials Not Found](#basic-credentials-not-found) may help.

If you are using a [pull-through-cache](https://docs.earthly.dev/ci-integration/pull-through-cache), the ECR credential helper may cause 401 failures when fetching metadata from the mirrored registry. You can solve this by manually logging in, instead of using the credential helper. Here is an example of logging in manually:

```
aws ecr get-login-password | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
```

# GCP Artifact Registry

## Introduction

The GCP Artifact Registry is a hosted docker repository that requires extra configuration for day-to-day use. This configuration is not typical of other repositories, and there are some considerations to account for when using it with Earthly. This guide will walk you through creating an Earthfile, building an image, and pushing it to Artifact Registry.

[Artifact Registry is the successor to the GCP Container Registry (GCR)](https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr). It can accommodate more than just Docker images, but those are beyond the scope of this guide. Most of what we detail here applies to GCR as well, it will just require some [small tweaks](https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr#compare).

This guide assumes you have already installed the [`gcloud` CLI tool](https://cloud.google.com/sdk/docs/install), [enabled the Artifact Repository API](https://console.cloud.google.com/flows/enableapi?apiid=artifactregistry.googleapis.com\&redirect=https://cloud.google.com/artifact-registry/docs/docker/quickstart), and [created a new repository named `hello-earthly`](https://console.cloud.google.com/artifacts).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.18

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
```

## Configure the Artifact Repository Credential Helper

Artifact Repository does not issue permanent credentials. Instead, it relies on your Google credentials to issue Docker credentials. To this end, Google has built-in a credential helper to the `gcloud` CLI tool. `gcloud` can update your `.docker/config.json` on its own by running `gcloud auth configure-docker <region>-docker.pkg.dev`. Here is a sample entry it might create:

```
 {
    "credHelpers": {
        "<region>-docker.pkg.dev": "gcloud"
  }
}

```

## IAM

Ensure that you have correct permissions to push and pull the images. Please reference the [GCP documentation](https://cloud.google.com/artifact-registry/docs/access-control#grant) to ensure you have the correct permissions set. You will need to add the `Artifact Registry Reader` and `Artifact Registry Writer` roles to complete the tasks in this guide.

If you are using GCR; keep in mind that the needed permissions are based on the GCP storage permissions. We used the `Storage Admin` permissions to complete the guide with GCR.

Service Accounts also work with Earthly. Rather than `gcloud init`, simply log in using the Google-provided key like this:

```
RUN gcloud auth activate-service-account --key-file /test/key.json
```

## Run the Target

With the helper installed, no special To build and push an image, simply execute the build target. Don't forget the `--push` flag!

```
❯ earthly --push +build
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
         alpine:3.18 | --> Load metadata linux/amd64
               +base | --> FROM alpine:3.18
               +base | [██████████] resolve docker.io/library/alpine:3.18@sha256:0bd0e9e03a022c3b0226667621da84fc9bf562a9056130424b5bfbd8bcb0397f ... 100%
              +build | --> RUN echo "Hello from Earthly!" > motd
              output | --> exporting outputs
              output | [██████████] exporting layers ... 100%
              output | [██████████] exporting manifest sha256:08f310b4520418a60f7c12b168167ea22b886bc03d43ab87058e959ef5c14cf2 ... 100%
              output | [██████████] exporting config sha256:8a54361d584a6a51f0136b9ae1526aba8f99cc0a1583954b0f206d3a472eaac9 ... 100%
              output | [██████████] pushing layers ... 100%
              output | [██████████] pushing manifest for <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love ... 100%
              output | [██████████] sending tarballs ... 100%
2bc1eb057e55: Loading layer [==================================================>]     187B/187B
=========================== SUCCESS ===========================
Loaded image: <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
              +build | Image +build as <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love (pushed)


```

## Pulling Images

Using this credential helper; you can also pull images without any special handling in an Earthfile:

```
FROM earthly/dind:alpine-main

run:
    WITH DOCKER --pull <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
        RUN docker run <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
    END
```

And here is how you would run it:

```
❯ earthly -P +run
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
  e/dind:alpine-main | --> Load metadata linux/amd64
u/e/h/hello-earthly:with-love | --> Load metadata linux/amd64
u/e/h/hello-earthly:with-love | --> DOCKER PULL <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
u/e/h/hello-earthly:with-love | [          ] resolve <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love@sha256:08f310b4520418a60f7c12b168167ea22b886bc03d43ab87058e959ef5c14cf2 ... 0%                               [██████████] resolve <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love@sha256:08f310b4520418a60f7c12b168167ea22b886bc03d43ab87058e959ef5c14cf2 ... 100%
               +base | --> FROM earthly/dind:alpine-main
               +base | [██████████] resolve docker.io/earthly/dind:alpine-main@sha256:09f497f0114de1f3ac6ce2da05568fcb50b0a4fd8b9025ed7c67dc952d092766 ... 100%
                +run | *cached* --> WITH DOCKER (install deps)
                +run | *cached* --> WITH DOCKER RUN docker run <region>-docker.pkg.dev/<project>/hello-earthly/hello-earthly:with-love
              output | --> exporting outputs
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================

```

# Azure ACR

## Introduction

The Azure Container Registry (ACR) is a hosted docker repository that requires extra configuration for day-to-day use. This configuration is not typical of other repositories, and there are some considerations to account for when using it with Earthly. This guide will walk you through creating an Earthfile, building an image, and pushing it to ACR.

This guide assumes you have already installed the [Azure CLI tool](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli), and [created a new repository named `helloearthly`](https://portal.azure.com/?quickstart=true#create/Microsoft.ContainerRegistry).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.18

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push helloearthly.azurecr.io/hello-earthly:with-love
```

## Login and Configure the ACR Credential Helper

ACR does not issue permanent credentials. Instead, it relies on your Azure AD credentials to issue Docker credentials. As an individual user, you will need to log into your repository first:

```
❯ az acr login --name helloearthly
Login Succeeded
```

After logging in, the [ACR Credential Helper](https://github.com/Azure/acr-docker-credential-helper) will help keep your credentials up to date, as long as it is invoked again before your already issued credentials expire. When all this is complete, your `.docker/config.json` might look like this:

```
{
 "auths": {
  "helloearthly.azurecr.io": {
   "auth": "...",
   "identitytoken": "..."
  }
 },
 "credsStore": "acr-linux"
}
```

ACR boasts many other methods of logging in, including [Service Principals](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal) and [admin accounts](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-authentication#admin-account). Note that the admin account method is not recommended for production usage. Please follow the relevant guides to authenticate if you wish to use one of these other methods.

## RBAC

Ensure that you have correct permissions to push and pull the images. Please reference the [ACR RBAC documentation](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-roles) to ensure you have the correct permissions set. To complete all the activities in this guide, you will need to have at least the `AcrPush` role.

Earthly also works with Service Principals; and these do not require `az acr login`. You can simply login directly with `docker` like this:

```
RUN --secret AZ_USERNAME=earthly-technologies/azure/ci-cd-username \
    --secret AZ_PASSWORD=earthly-technologies/azure/ci-cd-password \
    docker login helloearthly.azurecr.io --username $AZ_USERNAME --password $AZ_PASSWORD
```

## Run the Target

Once you are logged in, and have the optional credential helper installed, then you are ready to use Earthly to access images in ACR. To build and push an image, simply execute the build target. Don't forget the `--push` flag!

```
❯ ../earthly/earthly --push --no-cache +build
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
         alpine:3.18 | --> Load metadata linux/amd64
               +base | --> FROM alpine:3.18
               +base | [██████████] resolve docker.io/library/alpine:3.18@sha256:0bd0e9e03a022c3b0226667621da84fc9bf562a9056130424b5bfbd8bcb0397f ... 100%
              +build | --> RUN echo "Hello from Earthly!" > motd
              output | --> exporting outputs
              output | [██████████] exporting layers ... 100%
              output | [██████████] exporting manifest sha256:02df2d4600094d5550f7475b868ce9bb17d6c3a529e9669a453bbba7b2cdb659 ... 100%
              output | [██████████] exporting config sha256:722368416f5de51291ce937feac2c246d66dff351678968b1b6ebc533ceaaa0c ... 100%
              output | [██████████] pushing layers ... 100%
              output | [██████████] pushing manifest for helloearthly.azurecr.io/hello-earthly:with-love ... 100%
              output | [██████████] sending tarballs ... 100%
824d26cf8432: Loading layer [==================================================>]     192B/192B
=========================== SUCCESS ===========================
Loaded image: helloearthly.azurecr.io/hello-earthly:with-love
              +build | Image +build as helloearthly.azurecr.io/hello-earthly:with-love (pushed)
```

## Pulling Images

By logging in and optionally installing the credential helper; you can also pull images without any special handling in an Earthfile:

```
FROM earthly/dind:alpine-main

run:
    WITH DOCKER --pull helloearthly.azurecr.io/hello-earthly:with-love
        RUN docker run helloearthly.azurecr.io/hello-earthly:with-love
    END
```

And here is how you would run it:

```
❯ earthly -P +run
           buildkitd | Found buildkit daemon as docker container (earthly-buildkitd)
  e/dind:alpine-main | --> Load metadata linux/amd64
h/hello-earthly:with-love | --> Load metadata linux/amd64
h/hello-earthly:with-love | --> DOCKER PULL helloearthly.azurecr.io/hello-earthly:with-love
h/hello-earthly:with-love | [██████████] resolve helloearthly.azurecr.io/hello-earthly:with-love@sha256:02df2d4600094d5550f7475b868ce9bb17d6c3a529e9669a453bbba7b2cdb659 ... 100%
               +base | --> FROM earthly/dind:alpine-main
               +base | [██████████] resolve docker.io/earthly/dind:alpine-main@sha256:09f497f0114de1f3ac6ce2da05568fcb50b0a4fd8b9025ed7c67dc952d092766 ... 100%
                +run | *cached* --> WITH DOCKER (install deps)
                +run | --> WITH DOCKER RUN docker run helloearthly.azurecr.io/hello-earthly:with-love
                +run | Loading images...
                +run | Loaded image: helloearthly.azurecr.io/hello-earthly:with-love
                +run | ...done
                +run | Hello from Earthly!
              output | --> exporting outputs
              output | [██████████] sending tarballs ... 100%
=========================== SUCCESS ===========================
```

## Troubleshooting

### 401 (authentication required)

Re-run `az acr login --name` to log in again and refresh your credentials. Azure recommends that you run this at the beginning o each automated script; keep this in mind for your CI runs.

# Self-signed certificates

This guide will demonstrate the use of a private registry using self-signed certificates in conjunction with Earthly.

For information about configuring the registry itself, see the [Docker Registry deployment documentation](https://docs.docker.com/registry/deploying/).

## Create an Earthfile

No special considerations are needed in the Earthfile itself. You can use `SAVE IMAGE` just like any other repository.

```
FROM alpine:3.18

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push <registry-hostname>/hello-earthly:with-love
```

## Add certificates to Earthly

Set the following configuration options in your [Earthly config](https://docs.earthly.dev/docs/earthly-config).

```yaml
global:
  buildkit_additional_args: ["-v", "<absolute-path-to-ca-file>:/etc/config/add.ca"]
  buildkit_additional_config: |
    [registry."<registry-hostname>"]
      ca=["/etc/config/add.ca"]
```

Where `<absolute-path-to-ca-file>` is the location of the CA certificate you wish to add and `<registry-hostname>` is the hostname of the registry. The quotes are not a mistake, and should be left in.

## Insecure registries

For testing purposes, you can also define insecure registries for Earthly to access. Note that the non-test use of insecure registries is strongly discouraged due to the risk of man-in-the-middle (MITM) attacks.

To configure Earthly to use an insecure registry, use the following [Earthly config](https://docs.earthly.dev/docs/earthly-config) settings.

```yaml
global:
  buildkit_additional_config: |
    [registry."<registry-hostname>"]
      insecure = true
```

In addition, you will need to specify the `--insecure` flag in any `SAVE IMAGE` command. Again, the quotes are not a mistake, and should be left in.

```
FROM alpine:3.18

build:
    RUN echo "Hello from Earthly!" > motd
    ENTRYPOINT cat motd
    SAVE IMAGE --push --insecure <registry-hostname>/hello-earthly:with-love
```

{% hint style="danger" %}
**Note**

The `http` and `insecure` settings are typically mutually exclusive. Setting `insecure=true` should only be used when the registry is https and is configured with an insecure certificate. Setting `http=true` is only for the case where a standard http-based registry is used (i.e. no SSL encryption). If both are set buildkit will attempt to connect to the registry using either http (port 80), or https (port 443).
{% endhint %}

## Other BuildKit options

Other settings for configuring registries in Earthly via [BuildKit options](https://github.com/moby/buildkit/blob/master/docs/buildkitd.toml.md) can be seen below.

```yaml
global:
  buildkit_additional_config: |
    [registry."<registry-hostname>"]
      mirrors = ["<mirror>"]
      http = true|false
      insecure = true|false
      ca=["<ca-path-pem>"]
      [[registry."<registry-hostname>".keypair]]
        key="<key-path-pem>"
        cert="<cert-path-pem>"
```

# Using the Earthly Docker Images

# earthly/earthly

This image contains `earthly`, `buildkit`, and some extra configuration to enable the two to work together. All that's missing is your source code! This image is mainly intended for use in containerized CI scenarios, or where maintaining a persistent installation of `earthly` isn't possible.

### Tags

Currently, the `latest` tag is `v0.7.23`.\
For other available tags, please check out <https://hub.docker.com/r/earthly/earthly/tags>

### Quickstart

Want to just get started? Here are a couple sample `docker run` commands that cover the most common use-cases:

#### Simple Usage with Docker Socket

This example shows how to use the Earthly container in conjunction with a Docker socket that Earthly can use to start up the Buildkit daemon.

```bash
docker run -t -v $(pwd):/workspace -v /var/run/docker.sock:/var/run/docker.sock -e NO_BUILDKIT=1 earthly/earthly:v0.7.23 +for-linux
```

Here's a quick breakdown:

* `-t` tells Docker to emulate a TTY. This makes the `earthly` log output colorized.
* `-v $(pwd):/workspace` mounts the source code into the conventional location within the docker container. Earthly is executed from this directory when starting the container. Any artifacts saved within this folder remain on your local machine.
* `-v /var/run/docker.sock:/var/run/docker.sock` mounts the Docker socket such that Earthly can start Buildkit as a Docker container in the host's Docker.
* `-e NO_BUILDKIT=1` tells the Earthly container not to start en embedded buildkit. A Buildkit daemon will instead be started via the Docker socket provided.
* `+for-linux` is the target to be invoked. All arguments specified after the image tag will be passed to `earthly`.

#### Simple Usage with Embedded Buildkit

This example shows how the Earthly image can start a Buildkit daemon within the same container. A Docker socket is not needed in this case, however the container will need to be run with the `--privileged` flag.

```bash
docker run --privileged -t -v $(pwd):/workspace -v earthly-tmp:/tmp/earthly:rw earthly/earthly:v0.7.23 +for-linux
```

Here's a quick breakdown:

* `--privileged` is required when you are using the internal, embedded `buildkit`. This is because `buildkit` currently requires it for OverlayFS support and for network configuration.
* `-t` tells Docker to emulate a TTY. This makes the `earthly` log output colorized.
* `-v $(pwd):/workspace` mounts the source code into the conventional location within the docker container. Earthly is executed from this directory when starting the container. Any artifacts saved within this folder remain on your local machine.
* `-v earthly-tmp:/tmp/earthly:rw` mounts (and creates, if necessary) the `earthly-tmp` Docker volume into the containers `/tmp/earthly`. This is used as a temporary/working directory for `buildkitd` during builds.
* `+for-linux` is the target to be invoked. All arguments specified after the image tag will be passed to `earthly`.

#### Usage with Satellites and No Local Code

This example utilizes an [Earthly Satellite](https://docs.earthly.dev/earthly-cloud/satellites) to perform builds. The code to be built is downloaded directly from GitHub.

```bash
docker run -t -e NO_BUILDKIT=1 -e EARTHLY_TOKEN=<my-token> earthly/earthly:v0.7.23 --ci --org <my-org> --sat <my-sat> github.com/earthly/earthly+for-linux
```

Here's what this does:

* `-e EARTHLY_TOKEN=<my-token>` passes along an Earthly token such that Earthly can access satellites. This token can be created via `earthly account create-token`.
* `--org <my-org>` specifies the organization that the satellite belongs to.
* `--sat <my-sat>` specifies the satellite to use.
* `github.com/earthly/earthly+for-linux` specifies the target to build. This target is located on GitHub, and will be pulled from the Satellite.

#### Usage for non-build commands

This example shows how to use the Earthly container to run non-build commands. This is useful for running commands like `earthly account`, or `earthly secret`.

```bash
docker run -t -e NO_BUILDKIT=1 -e EARTHLY_TOKEN=<my-token> earthly/earthly:v0.7.23 account list-tokens
```

```bash
docker run -t -e NO_BUILDKIT=1 -e EARTHLY_TOKEN=<my-token> earthly/earthly:v0.7.23 secret get foo
```

### Using This Image

#### Requirements

There are a couple requirements this image expects you to follow when using it. These requirements streamline usage of the image and save configuration effort.

**Privileged Mode**

If you are using the embedded `buildkitd`, then this image needs to be run as a privileged container. This is because `buildkitd` needs appropriate access to use `overlayfs`.

**`/tmp/earthly`**

Because this folder sees *a lot* of traffic, its important that it remains fast. We *strongly* recommend using a Docker volume for mounting `/tmp/earthly`. If you do not, `buildkitd` can consume excessive disk space, operate very slowly, or it might not function correctly.

In some environments, not mounting `/tmp/earthly` as a Docker volume results in the following error:

```
--> WITH DOCKER RUN --privileged ...
...
rm: can't remove '/var/earthly/dind/...': Resource busy
```

**Source Mounting**

Because `earthly` is running inside a container, it does not have access to your source code unless you grant it. This image expects to find a valid `Earthfile` in the working directory, which is set by default to `/workspace`.

**DOCKER\_HOST**

This image *does* include a functional Docker CLI, but does not include a full Docker daemon. If your `Earthfile` requires a Docker daemon of any sort, you will need to provide it through this environment variable.

If your daemon is on the same host as this container, you can also volume mount your hosts docker daemon using `-v /var/run/docker.sock:/var/run/docker.sock`. Note that this will cause `earthly` to use your hosts Docker daemon, and could lead to name conflicts if multiple copies of this image are run on the same host.

**-t**

This is the easiest way to ensure you get the nice, colorized output from `earthly`. Alternatively, you could provide the `FORCE_COLOR` environment variable.

#### Supported Environment Variables

| Variable Name                         | Default Values                 | Description                                                                                                                                                                                                   |
| ------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GLOBAL\_CONFIG                        |                                | Any valid YAML for the top-level `global` key in `config.yml`. Example: `{disable_analytics: true, local_registry_host: 'tcp://127.0.0.1:8371'}`                                                              |
| GIT\_CONFIG                           |                                | Any valid YAML for the top-level `git` key in `config.yml`. Example: `{example: {pattern: 'example.com/([^/]+)', substitute: 'ssh://git@example.com:2222/var/git/repos/$1.git', auth: ssh}}`                  |
| NO\_BUILDKIT                          |                                | Disables the embedded Buildkit daemon.                                                                                                                                                                        |
| DOCKER\_HOST                          | `/var/run/docker.sock`         | From Docker's CLI.                                                                                                                                                                                            |
| BUILDKIT\_HOST                        | `tcp://<hostname>:8372`        | The address of your BuildKit host. Use this when you have a remote `buildkitd` you would like to connect to.                                                                                                  |
| EARTHLY\_ADDITIONAL\_BUILDKIT\_CONFIG |                                | Additional `buildkitd` config to append to the generated configuration file.                                                                                                                                  |
| BUILDKIT\_TCP\_TRANSPORT\_ENABLED     |                                | Required to be set to `true` when using an external `buildkitd` via `BUILDKIT_HOST`. `true` when using the embedded `buildkitd`.                                                                              |
| BUILDKIT\_TLS\_ENABLED                |                                | Required when using an external `buildkitd` via `BUILDKITD_HOST`, and the external `buildkitd` requires mTLS. You will also need to mount certificates into the right place (`/etc/.earthly/certs`).          |
| CNI\_MTU                              | MTU of first default interface | Set this when we autodetect the MTU incorrectly. The device used for autodetection can be shown by the command `ip route show \| grep default \| cut -d' ' -f5 \| head -n 1`                                  |
| EARTHLY\_RESET\_TMP\_DIR              | `false`                        | Cleans out `/tmp/earthly` before running, if set to `true`. Useful when you host-mount an temporary directory across runs.                                                                                    |
| NETWORK\_MODE                         | `cni`                          | Specifies the networking mode of `buildkitd`. Default uses a CNI bridge network, configured with the `CNI_MTU`.                                                                                               |
| CACHE\_SIZE\_MB                       | `0`                            | How big should the `buildkitd` cache be allowed to get, in MiB? A value of 0 sets the cache size to "adaptive", causing BuildKit to detect the available size of the system and choose a limit automatically. |
| GIT\_URL\_INSTEAD\_OF                 |                                | Configure `git config --global url.<url>.insteadOf` rules to be used by `buildkitd`.                                                                                                                          |
| IP\_TABLES                            |                                | Override which binary (`iptables_nft` or `iptables_legacy`) is used for configuring `ip_tables`. Only set this if autodetection fails for your platform.                                                      |

# earthly/buildkitd

This image contains `buildkit` with some Earthly-specific setup. This is what Earthly will start when using a local daemon. You can also start it up yourself and use it as a remote/shared BuildKit daemon.

*Note that versions of this container have only ever been tested with their corresponding version of `earthly`.* Mismatched versions are unsupported.

### Tags

Currently, the `latest` tag is `v0.7.23`.\
For other available tags, please check out <https://hub.docker.com/r/earthly/buildkitd/tags>

### Quickstart

Want to just get started? Here are a couple sample `docker run` commands that cover the most common use-cases:

#### Simple Usage (Use Locally)

```bash
docker run --privileged -t -v earthly-tmp:/tmp/earthly:rw earthly/buildkitd:v0.7.19
```

Heres a quick breakdown:

* `--privileged` is required. This is because `earthly` needs some privileged `buildkit` functionality.
* `-t` tells Docker to emulate a TTY. This makes the `buildkit` log output colorized.
* `-v earthly-tmp:/tmp/earthly:rw` mounts (and creates, if necessary) the `earthly-tmp` Docker volume into the containers `/tmp/earthly`. This is used as a temporary/working directory for `buildkitd` during builds.

Assuming you are running this on your machine, you could use this `buildkitd` by setting `EARTHLY_BUILDKIT_HOST=docker-container://<container-name>`, or by specifying the appropriate values in `config.yml`.

#### Usage (Use As Remote)

```bash
docker run --privileged -t -v earthly-tmp:/tmp/earthly:rw -e BUILDKIT_TCP_TRANSPORT_ENABLED=true -p 8372:8372 earthly/buildkitd:v0.7.19
```

Omitting the options already discussed from the simple example:

* `-e BUILDKIT_TCP_TRANSPORT_ENABLED=true` makes `buildkitd` listen on a TCP port instead of a Unix socket.
* `-p 8372:8372` forwards the hosts port 8372 to the containers port 8372. When using TCP, `buildkit` will always listen on 8372, but you can configure the apparent port by forwarding a different port on your host.

Assuming you ran this on another machine named `fast-builder`, you could use this remote `buildkitd` by setting `EARTHLY_BUILDKIT_HOST=tcp://fast-builder:8372`, or by specifying the address in your `config.yml`.

### Using This Image

#### Requirements

**Privileged Mode**

This image needs to be run as a privileged container. This is because `buildkitd` needs appropriate access to start and run additional containers itself via `runc`.

**`/tmp/earthly`**

Because this folder sees *a lot* of traffic, its important that it remains fast. We *strongly* recommend using a Docker volume for mounting `/tmp/earthly`. If you do not, `buildkitd` can consume excessive disk space, operate very slowly, or it might not function correctly.

In some environments, not mounting `/tmp/earthly` as a Docker volume results in the following error:

```
--> WITH DOCKER RUN --privileged ...
...
rm: can't remove '/var/earthly/dind/...': Resource busy
```

**External Usage**

To use this image externally, it requires you to forward a port on your machine to the containers port 8372. You will need to ensure that external access to the machine on the port you chose is possible as well.

When using this container locally with `earthly`, please note that setting `EARTHLY_BUILDKIT_HOST` values with hosts `127.0.0.1`, `::1/128`, or `localhost` are considered local and will result in Earthly attempting to manage the BuildKit container itself. Consider using your hostname, or another alternative name in these cases.

#### Supported Environment Variables

| Variable Name                         | Default Values                 | Description                                                                                                                                                                  |
| ------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EARTHLY\_ADDITIONAL\_BUILDKIT\_CONFIG |                                | Additional `buildkitd` config to append to the generated configuration file.                                                                                                 |
| BUILDKIT\_TCP\_TRANSPORT\_ENABLED     |                                | Set to `true` when the `buildkitd` instance is going to be used remotely                                                                                                     |
| BUILDKIT\_TLS\_ENABLED                |                                | Set to `true` when the `buildkitd` instance will require mTLS from the clients. You will also need to mount certificates into the right place (`/etc/*.pem`).                |
| CNI\_MTU                              | MTU of first default interface | Set this when we autodetect the MTU incorrectly. The device used for autodetection can be shown by the command `ip route show \| grep default \| cut -d' ' -f5 \| head -n 1` |
| EARTHLY\_RESET\_TMP\_DIR              | `false`                        | Cleans out `/tmp/earthly` before running, if set to `true`. Useful when you host-mount an temporary directory across runs.                                                   |
| NETWORK\_MODE                         | `cni`                          | Specifies the networking mode of `buildkitd`. Default uses a CNI bridge network, configured with the `CNI_MTU`.                                                              |
| CACHE\_SIZE\_MB                       | `0`                            | How big should the `buildkitd` cache be allowed to get, in MiB? 0 is unbounded.                                                                                              |
| GIT\_URL\_INSTEAD\_OF                 |                                | Configure `git config --global url.<url>.insteadOf` rules used by `buildkitd`                                                                                                |
| IP\_TABLES                            |                                | Override which binary (`iptables_nft` or `iptables_legacy`) is used for configuring `ip_tables`. Only set this if autodetection fails for your platform.                     |

# Best practices

Although Earthly has been designed to be unambiguous about what command to use for the job, writing Earthfiles can sometimes still be tricky, when it comes to nuances. As you try to accomplish certain tasks, you may find that sometimes the same result can be achieved using more than one technique. Or so it might seem.

Below we list some of the best practices that we have found to be useful in designing Earthly builds, with a focus on certain commands or techniques that seem similar, but aren't really, but also on some key points that we have seen newcomers stumble into.

## Table of contents

* [Earthfile-specific](#earthfile-specific)
  * [`COPY` only the minimal amount of files. Avoid copying `.git`](#copy-only-the-minimal-amount-of-files.-avoid-copying-.git)
  * [`ENV` for image env vars, `ARG` for build configurability](#env-for-image-env-vars-arg-for-build-configurability)
  * [Use cross-repo references, and avoid `GIT CLONE` if possible](#use-cross-repo-references-and-avoid-git-clone-if-possible)
  * [`GIT CLONE` vs `RUN git clone`](#git-clone-vs-run-git-clone)
  * [`IF [...]` vs `RUN if [...]`](#if-...-vs-run-if-...)
  * [`FOR ... IN ...` vs `RUN for ... in ...`](#for-...-in-...-vs-run-for-...-in-...)
  * [Pattern: Optionally `LOCALLY`](#pattern-optionally-locally)
  * [Pattern: Deciding on a base image based on a condition](#pattern-deciding-on-a-base-image-based-on-a-condition)
  * [Use `RUN --push` for deployment commands](#use-run-push-for-deployment-commands)
  * [Use `--secret`, not `ARG`s to pass secrets to the build](#use-secret-not-args-to-pass-secrets-to-the-build)
  * [Avoid copying secrets to the build environment](#avoid-copying-secrets-to-the-build-environment)
  * [Do not pass Earthly dependencies from one target to another via the local file system or via an external registry](#do-not-pass-earthly-dependencies-from-one-target-to-another-via-the-local-file-system-or-via-an-external-registry)
  * [Use `WITH DOCKER --pull`](#use-with-docker-pull)
  * [Style: Define the high-level targets at the top of the Earthfile](#style-define-the-high-level-targets-at-the-top-of-the-earthfile)
  * [Use `COPY +my-target/...` to pass files to and from `LOCALLY` targets](#use-copy-+my-target-...-to-pass-files-to-and-from-locally-targets)
  * [Use `WITH DOCKER --load=+my-target` to pass images to `LOCALLY` targets](#use-with-docker-load-+my-target-to-pass-images-to-locally-targets)
  * [Avoid non-deterministic behavior](#avoid-non-deterministic-behavior)
  * [Use `COPY --dir` to copy multiple directories](#use-copy-dir-to-copy-multiple-directories)
  * [Use separate images for build and production](#use-separate-images-for-build-and-production)
  * [Use `SAVE ARTIFACT ... AS LOCAL ...` for generated code, not `LOCALLY`](#use-save-artifact-...-as-local-...-for-generated-code-not-locally)
  * [Multi-line strings](#multi-line-strings)
  * [Multi-line commands](#multi-line-commands)
  * [Copying files from outside the build context](#copying-files-from-outside-the-build-context)
  * [Repository structure: Place build logic as close to the relevant code as possible](#repository-structure-place-build-logic-as-close-to-the-relevant-code-as-possible)
  * [Repository structure: Do not place all Earthfiles in a dedicated directory](#repository-structure-do-not-place-all-earthfiles-in-a-dedicated-directory)
  * [Pattern: Pass-through artifacts or images](#pattern-pass-through-artifacts-or-images)
  * [Use `earthly/dind`](#use-earthly-dind)
  * [Pattern: Saving artifacts resulting from a `WITH DOCKER`](#pattern-saving-artifacts-resulting-from-a-with-docker)
* [Usage-specific](#usage-specific)
  * [Use `--ci` when running in CI](#use-ci-when-running-in-ci)
  * [Avoid `LOCALLY` and other non-strict commands](#avoid-locally-and-other-non-strict-commands)
  * [Pattern: Push on the `main` branch only](#pattern-push-on-the-main-branch-only)
  * [Do not expose cache image tags publicly if the cache contains private code or dependencies](#do-not-expose-cache-image-tags-publicly-if-the-cache-contains-private-code-or-dependencies)
  * [Technique: Use `earthly -i` to debug failures](#technique-use-earthly-i-to-debug-failures)
  * [Run everything in a single Earthly invocation, do not wrap Earthly](#run-everything-in-a-single-earthly-invocation-do-not-wrap-earthly)
  * [Use `RUN --ssh` for passing host SSH keys to builds](#use-run-ssh-for-passing-host-ssh-keys-to-builds)
  * [Use SAVE IMAGE to always cache](#use-save-image-to-always-cache)
  * [Future: Saving an artifact even if the build fails](#future-saving-an-artifact-even-if-the-build-fails)

## Earthfile-specific

### `COPY` only the minimal amount of files. Avoid copying `.git`

A typical mistake is to `COPY` entire large directories into the build environment and only using a subset of the files within them. Or worse, copying the entire repository (which might also include `.git`) for no good reason.

```Dockerfile
# Avoid
COPY . .
COPY * ./
```

The problem with this is that many of the files copied are not actually used during the build, however Earthly will react to changes to them, causing it to reuse cache inefficiently. It's not an issue of file size (though sometimes that too can hurt performance). It is much of an issue of re-executing build commands that wouldn't have to be re-executed.

```Dockerfile
# Avoid
COPY . .
RUN go mod download
RUN go build ...
```

In the above example, changing the project's `README.md` or running `git fetch` might cause slow commands like `go mod download` to be re-executed.

Earthly uses `COPY` commands (among other things) to mark certain files as inputs to the build. If any file included in a `COPY` changes, then the build will continue from that `COPY` command onwards. For this reason, you want to be as specific as possible when including files in a `COPY` command. In some cases, you might even have to list files individually.

Here are some possible ways to improve the above example:

```Dockerfile
# Better
COPY go.mod go.sum ./*.go ./
RUN go mod download
RUN go build ...
```

The above is better, as it avoids reacting to changes in `.git` or to unrelated files, like `README.md`. However, this can be arranged even better, to avoid downloading all the dependencies on every `*.go` file change.

```Dockerfile
# Best
COPY go.mod go.sum ./
RUN go mod download
COPY ./*.go ./
RUN go build ...
```

An additional way in which you can improve the precision of the `COPY` command is to use the [`.earthlyignore`](https://docs.earthly.dev/docs/earthfile/earthlyignore) file. Note, however, that this is best left as a last resort, as new files added to the project (that may be irrelevant to builds) would need to be manually added to `.earthlyignore`, which may be error-prone. It is much better to have to include every new file manually into the build (by adding it to a `COPY` command), than to exclude every new file manually (by adding it to the `.earthlyignore`), as whenever any such new file *must* be included, then the build would typically fail, making it harder to make a mistake compared to the opposite.

### `ENV` for image env vars, `ARG` for build configurability

`ENV` variables and `ARG` variables seem similar, however they are meant for different use-cases. Here is a breakdown of the differences, as well as how they differ from the Dockerfile-specific `ARG` command:

|                                                                                     | `ENV` | `ARG` | Dockerfile `ARG` |
| ----------------------------------------------------------------------------------- | ----- | ----- | ---------------- |
| Available as an env-var in the same target                                          | ✅     | ✅     | ❌                |
| Available for expanding within non-RUN commands                                     | ❌     | ✅     | ✅                |
| Stored in the final image as an env-var                                             | ✅     | ❌     | ❌                |
| Inherited via `FROM`                                                                | ✅     | ❌     | ❌                |
| Can be overridden when calling a build                                              | ❌     | ✅     | ✅                |
| Can be propagated to other targets (via `BUILD +target --<key>=<value>` or similar) | ❌     | ✅     | N/A              |

As you can see, the key situation where `ENV` is needed is when you want the value to be stored as part of the final image's configuration. This causes any `FROM` or `docker run` using that image to inherit the value.

However, if the use-case is build configurability, then `ARG` is the way to achieve that.

### Use cross-repo references, and avoid `GIT CLONE` if possible

Earthly provides rich set of features to allow working with and across Git repositories. It is recommended to use Earthly [cross-repository references](https://docs.earthly.dev/docs/guides/importing) rather than `GIT CLONE` or `RUN git clone`, whenever possible.

Here is an example.

Repo 1:

```
repo 1
├── README.md
└── my-file.txt
```

Repo 2:

```Dockerfile
# Bad
VERSION 0.7
FROM alpine:3.18
WORKDIR /work
print-file:
    GIT CLONE git@github.com:my-co/repo-1.git
    RUN echo my-file.txt
```

This might be addressed in the following way:

Repo 1:

```
repo 1
├── README.md
├── Earthfile
└── my-file.txt
```

```Dockerfile
# Repo 1 Earthfile
VERSION 0.7
FROM alpine:3.18
WORKDIR /work
file:
    COPY ./my-file.txt ./
    SAVE ARTIFACT ./my-file.txt
```

Repo 2:

```Dockerfile
# Repo 2 Earthfile
VERSION 0.7
IMPORT github.com/my-co/repo-1
FROM alpine:3.18
WORKDIR /work
print-file:
    COPY repo-1+file/my-file.txt ./
    RUN echo my-file.txt
```

There are multiple benefits to using cross-repository references in this manner:

* The build of repo 1 can evolve to more than just passing a file to another repository. It may be possible to also export generated code, artifacts, base images or full microservice images in the future, if they are needed.
* It is clearer about which files are actually needed externally, as they are declared via `SAVE ARTIFACT`. This makes the code more readable and maintainable. The fact that an artifact is saved during a build constitutes an explicit API of the repository.

Of course, the down-side is that repo 1 requires an Earthfile to be added, and that might not always be feasible. It's possible that repo 1 is controlled by another team, or that it is entirely external to the company. In such cases, `GIT CLONE` might help to provide a faster, yet imperfect solution.

Another use-case where `GIT CLONE` is better suited is when the operation needs to take place on the whole source repository. For example, performing Git operations, such as tagging, creating branches, or merging.

Finally, here is a comparison between cross-repo references and `GIT CLONE`:

|                                                            | Cross-repo reference                                | `GIT CLONE`                                                 |
| ---------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------- |
| Example                                                    | `FROM github.com/my-co/my-proj:my-branch+my-target` | `GIT CLONE --branch=my-branch git@github.com:my-co/my-proj` |
| Earthly can pass-through SSH agent access from the host    | ✅                                                   | ✅                                                           |
| Access to HTTPS repositories can be configured in Earthly  | ✅                                                   | ✅                                                           |
| Can specify branch or tag                                  | ✅ - via `:<branch>`                                 | ✅ - via `--branch`                                          |
| Source configurable via `ARG`s                             | ✅                                                   | ✅                                                           |
| Protocol-agnostic referencing                              | ✅                                                   | ❌ - can be `ssh://`, `https://`, `git@github.com` etc       |
| Clear declaration of the dependency                        | ✅ - source repo needs to expose it in the Earthfile | ❌                                                           |
| Can be used without modifications to the source repository | ❌ - requires Earthfile                              | ✅                                                           |
| Can operate on the repository itself                       | ❌ - possible, but not designed for this             | ✅                                                           |

### `GIT CLONE` vs `RUN git clone`

Earthly has a built-in `GIT CLONE` instruction that can be used to clone a Git repository. It is recommended that `GIT CLONE` is used rather than `RUN git clone`, for a few reasons:

* Earthly treats `GIT CLONE` as a first-class input (BuildKit source). As such, Earthly caches the repository internally and downloading only incremental differences on changes.
* Earthly is commit hash-aware, so it'll be able to detect when the build needs to take place versus when there are no changes to be made and the cache can be reused. If a change takes place in the source repository, `RUN git clone` would not be able to detect that, as it is not recognized as an input. So it would naively reuse the cache when it shouldn't.
* `GIT CLONE` will pass-through Earthly settings for [authentication](https://docs.earthly.dev/docs/guides/auth), such as SSH agent access and/or HTTPS credentials.

`GIT CLONE` does have some limitations, however. It only performs a shallow clone, it does not have the branch information, it does not have origin information, and it does not have the tags downloaded. Even in such cases, it might be better to attempt to reintroduce the information after a `GIT CLONE`, whenever possible, in order to gain the caching benefits.

When this proves to be too difficult, or impossible, and you really need to perform a custom `RUN git clone`, consider using both in conjunction, to gain the hash awareness benefits.

```Dockerfile
# Bad
RUN git clone git@github.com/my-co/my-proj
WORKDIR my-proj
RUN ls
```

```Dockerfile
# Good
GIT CLONE git@github.com/my-co/my-proj my-proj
WORKDIR my-proj
RUN ls
```

```Dockerfile
# Ok, if you have no choice
ARG git_url="git@github.com/my-co/my-proj"
GIT CLONE "$git_url" my-proj
ARG git_hash=$(cd my-proj; git rev-parse HEAD)
RUN rm -rf my-proj &&\
    git clone "$git_url" my-proj &&\
    cd my-proj &&\
    git checkout "$git_hash"
WORKDIR my-proj
RUN ls
```

{% hint style="info" %}
**Note**

The final "if you have no choice" example contains an `ARG` shell-out, which will be set to the latest git sha; this is done so that if the git repository doesn't contain any new commits between multiple runs, the `ARG git_hash` value will stay constant, and will allow earthly to skip over the `RUN` command; whereas a `RUN --no-cache` command will be run each time even if the `ARG git_hash` value has never changed.
{% endhint %}

Finally, here is a comparison between `GIT CLONE` and `RUN git clone`:

|                                                                         | `GIT CLONE`                                           | `RUN git clone`                                       |
| ----------------------------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| Earthfiles can be protocol-agnostic                                     | ❌ - can be `ssh://`, `https://`, `git@github.com` etc | ❌ - can be `ssh://`, `https://`, `git@github.com` etc |
| Can configure access in Earthly, to keep Earthfiles agnostic            | ✅                                                     | ❌                                                     |
| Earthly can pass-through SSH agent access from the host                 | ✅                                                     | ✅ - but it requires `RUN --ssh`                       |
| Access to HTTPS repositories can be configured in Earthly               | ✅                                                     | ❌ - but possible to pass credentials via secrets      |
| Cache-aware - incremental pulls                                         | ✅                                                     | ❌                                                     |
| Commit hash-aware - rebuild when there are changes in remote repository | ✅                                                     | ❌                                                     |

### `IF [...]` vs `RUN if [...]`

Earthly 0.6 introduces the conditional `IF` command, which allows for complex control flow within Earthly recipes. However, there is also the possibility of using the shell `if` command to accomplish similar behavior. Which one should you use? Here is a quick comparison:

|                                                         | `IF` | `RUN if` |
| ------------------------------------------------------- | ---- | -------- |
| Can execute any command as the expression               | ✅    | ✅        |
| Can use mounts and secrets                              | ✅    | ✅        |
| Can use ARGs                                            | ✅    | ✅        |
| Expression can be cached                                | ✅    | ✅        |
| Body runs in the same layer as the condition expression | ❌    | ✅        |
| Body can include any Earthly command                    | ✅    | ❌        |

As you can see, `IF` is more powerful in that it can include other Earthly commands within it, allowing for rich conditional behavior. Examples might include optionally saving images, using different base images depending on a set of conditions, initializing `ARG`s with varying values.

`RUN if`, however is often simpler, and it only uses one layer.

As a best practice, it is recommended to use `RUN if` whenever possible (e.g. only `RUN` commands would be involved), to encourage simplicity, and otherwise to use `IF`.

### `FOR ... IN ...` vs `RUN for ... in ...`

As is the case with `IF` vs `RUN if`, there is a similar debate for the Earthly builtin command `FOR` vs `RUN for`. Here is a quick comparison of the two 'for' flavors:

|                                                      | `FOR` | `RUN for` |
| ---------------------------------------------------- | ----- | --------- |
| Can execute any command as the expression            | ✅     | ✅         |
| Can use mounts and secrets                           | ✅     | ✅         |
| Can use ARGs                                         | ✅     | ✅         |
| Expression can be cached                             | ✅     | ✅         |
| Can iterate over a constant list                     | ✅     | ✅         |
| Can iterate over a list resulting from an expression | ✅     | ✅         |
| Body runs in the same layer as the for expression    | ❌     | ✅         |
| Body can include any Earthly command                 | ✅     | ❌         |

Similar to the `IF` vs `RUN if` comparison, `FOR` is more powerful in that it can include other Earthly commands within it, allowing for rich iteration behavior. Examples might include iterating over a list of directories in a monorepo and calling Earthly targets within them, performing `SAVE IMAGE` over a list of container image tags.

`RUN for`, however is often simpler, and it only uses one layer.

As a best practice, it is recommended to use `RUN for` whenever possible (e.g. only `RUN` commands would be involved), to encourage simplicity, and otherwise to use `FOR`.

### Pattern: Optionally `LOCALLY`

In certain cases, it may be desirable to execute certain targets on the host machine, rather than in the sandboxed build environment, for debugging purposes. However, we need most of the targets to execute in strict mode in CI. The solution to this is to use a target that can be optionally executed via `LOCALLY`. Here is an example:

Suppose we wanted the following target to be executed on against the host's Docker daemon:

```Dockerfile
FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
WORKDIR /app
COPY docker-compose.yml ./
WITH DOCKER --compose docker-compose.yml \
        --service db \
        --load=+integration-test
    RUN docker-compose up integration
END
```

We could therefore have an equivalent `LOCALLY` target:

```Dockerfile
LOCALLY
WITH DOCKER --compose docker-compose.yml \
        --service db \
        --load=+integration-test
    RUN docker-compose up integration
END
```

However, the code duplication is not ideal and will result in the two recipes to drift apart over time.

It is possible to use an `ARG` to decide on whether to execute the target on the host or not:

```Dockerfile
FROM alpine:3.18
ARG run_locally=false
IF [ "$run_locally" = "true" ]
    LOCALLY
ELSE
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    WORKDIR /app
    COPY docker-compose.yml ./
END
WITH DOCKER --compose docker-compose.yml \
        --service db \
        --load=+integration-test
    RUN docker-compose up integration
END
```

Now, to run locally, you can execute `earthly +my-target --run_locally=true`, otherwise `earthly +my-target` will execute in the sandboxed environment (the same way it executes in CI).

### Pattern: Deciding on a base image based on a condition

In some cases, it is useful to switch up which base image to use depending on the result of an `IF` expression. For example, let's assume that the company provided Go image only supports the `linux/amd64` platform, and therefore, you'd like to use the official golang image when ARM (`linux/arm64`) is detected. Here's how this can be achieved:

```Dockerfile
FROM alpine:3.18
ARG TARGETPLATFORM
IF [ "$TARGETPLATFORM" = "linux/arm64" ]
    FROM golang:1.16
ELSE
    FROM my-company/golang:1.16
END
```

This will cause the execution of consecutive `FROM`s within the same target. This is completely valid. On encountering another `FROM` expression, the current build environment is reset and another fresh root is initialized, containing the specified images data.

### Use `RUN --push` for deployment commands

If the result of a build needs to be pushed to an external service (or storage provider) and the destination is not an image registry, then you will need to use a custom push command (as opposed to a `SAVE IMAGE --push`).

To execute a custom push command, you can simply use a regular `RUN` command together with the `--push` flag. The `--push` will ensure that:

* The command is only executed when Earthly is in push mode (`earthly --push`)
* No cache is reused for that specific command, causing it to execute every time
* The command is executed during the push phase of the build, ensuring that everything else (e.g. testing) has completed successfully first

Let's look at an example of using the [github-release utility](https://github.com/github-release/github-release) to perform a push to GitHub Releases.

```Dockerfile
# Bad, and dangerous
RUN --no-cache --secret GITHUB_TOKEN github-release upload ...
```

`RUN --no-cache` should be avoided for this use-case, as it has some potentially dangerous downsides:

* The upload command may be executed in parallel with any testing (meaning that tests might not pass yet the upload may still complete)
* The upload will execute even when earthly is not invoked in `--push` mode.

To address this issue, it is advisable to use `RUN --push` instead.

```Dockerfile
# Good
RUN --push --secret GITHUB_TOKEN github-release upload ...
```

### Use `--secret`, not `ARG`s to pass secrets to the build

If a build requires the usage of secrets, it is strongly recommended that you use the builtin secrets constructs, such as `earthly --secret`, [Earthly Cloud Secrets](https://docs.earthly.dev/earthly-cloud/cloud-secrets), and `RUN --secret`.

Using `ARG`s for passing secrets is strongly discouraged, as the secrets will be leaked in build logs, the build cache and the possibly in published images.

### Avoid copying secrets to the build environment

Even when using the proper builtin constructs for handling secrets, it is possible to then copy secrets in the build environment, which cause secrets to be leaked to a remote build cache, or to published images.

A simple example of how this may be possible:

```Dockerfile
# Bad
RUN --secret MY_SECRET echo "secret: $MY_SECRET" > /app/secret.txt
```

While this seems innocuous and possibly uncommon, consider the following, which on the face of it might look like a good idea:

```Dockerfile
# Bad
RUN --secret AWS_ACCESS_KEY_ID --secret AWS_SECRET_ACCESS_KEY echo "[default]\naws_access_key_id=$AWS_ACCESS_KEY_ID\naws_secret_access_key=$AWS_SECRET_ACCESS_KEY" > /root/.aws/credentials
RUN aws ec2 describe-images
```

Another negative example is copying the local credentials file:

```Dockerfile
# Bad
aws-creds:
    LOCALLY
    RUN cp "$HOME"/.aws/credentials ./.aws-creds
    SAVE ARTIFACT ./.aws-creds

do-something-with-aws:
    FROM ...
    COPY +aws-creds/.aws-creds /root/.aws/credentials
    RUN aws ec2 describe-images
```

The correct way to handle secrets that need to exist as files is to either mount them as secret files in the first place:

```Dockerfile
# Best
RUN --mount=type=secret,target=/root/.aws/credentials,id=AWS_CREDENTIALS \
    aws ec2 describe-images
```

This way, the credentials are never stored in the stored environment - they are only mounted during the execution of the `RUN` command.

Or, if you really have no choice, you may copy the secrets temporarily, but you **have** to remove them in the same layer:

```Dockerfile
# Ok, but error prone
RUN --secret AWS_ACCESS_KEY_ID --secret AWS_SECRET_ACCESS_KEY echo "[default]\naws_access_key_id=$AWS_ACCESS_KEY_ID\naws_secret_access_key=$AWS_SECRET_ACCESS_KEY" > /root/.aws/credentials ;\
    aws ec2 describe-images ;\
    rm /root/.aws/credentials
```

This should be avoided if possible, as it is error prone and might get secrets leaked if the `rm` is forgotten, or if the removal is performed under a separate `RUN` command.

```Dockerfile
# Bad: removal takes place in a separate layer, which means that the secrets will be leaked to the cache
RUN --secret AWS_ACCESS_KEY_ID --secret AWS_SECRET_ACCESS_KEY echo "[default]\naws_access_key_id=$AWS_ACCESS_KEY_ID\naws_secret_access_key=$AWS_SECRET_ACCESS_KEY" > /root/.aws/credentials
RUN aws ec2 describe-images
RUN rm /root/.aws/credentials
```

### Do not pass Earthly dependencies from one target to another via the local file system or via an external registry

If you are new to Earthly, you may be tempted to save an artifact locally in one target and then to retrieve it another one.

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +build
dep:
    ...
    SAVE ARTIFACT my-artifact.jar AS LOCAL ./build/my-artifact.jar
build:
    ...
    COPY ./build/my-artifact.jar ./
    ...
```

This will not actually work, as in Earthly all output takes place only at the end of a successful build. Meaning that when `+build` starts, the artifact would not have been output yet. In fact, `+dep` and `+build` will run completely parallel anyway - as Earthly does not know of a dependency between them.

The proper way to achieve this is to use [artifact references](https://docs.earthly.dev/docs/guides/importing).

```Dockerfile
# Good
all:
    BUILD +build
dep:
    ...
    SAVE ARTIFACT my-artifact.jar
build:
    ...
    COPY +dep/my-artifact.jar ./
    ...
```

Notice that `+dep` no longer needs to save the file locally. Also, the `COPY` command no longer references the file from the local file system. It has been replaced with an artifact reference from the target `+dep`. This reference will tell Earthly that these two targets depend on each other and will therefore schedule the relevant parts to run sequentially.

Notice also that in our `+all` target, we no longer have to call both `+dep` and `+build`. The system will automatically infer that when building `+build`, `+dep` is also required.

Another example of what you should **not** do is to pass Earthly images via between targets via an external registry.

```Dockerfile
# Bad
all:
    BUILD +dep-img
    BUILD +test
dep-img:
    ...
    SAVE IMAGE --push my-co/my-image:latest
test:
    WITH DOCKER
        RUN docker run my-co/my-image:latest
    END
```

```Dockerfile
# Also bad
all:
    BUILD +test
dep-img:
    ...
    SAVE IMAGE --push my-co/my-image:latest
test:
    BUILD +dep-img # This still does not work
    WITH DOCKER
        RUN docker run my-co/my-image:latest
    END
```

Similarly, in this case, pushing of the image takes place at the end of the build, which means that when `+test` runs, it will not have the image available, unless it has been pushed in a previous execution (which means that the image may be stale).

To fix this, we need to use `WITH DOCKER --load` and a [target reference](https://docs.earthly.dev/docs/guides/importing):

```Dockerfile
# Good
all:
    BUILD +test
dep-img:
    ...
    SAVE IMAGE my-co/my-image:latest
test:
    WITH DOCKER --load=+dep-img
        RUN docker run my-co/my-image:latest
    END
```

The `--load` instruction will inform Earthly that the two targets depend on each other and will therefore build the image and load it into the Docker daemon provided by `WITH DOCKER`.

### Use `WITH DOCKER --pull`

When referencing an external image in the body of a `WITH DOCKER` block, it is important to declare it via `WITH DOCKER --pull`, for a few reasons:

* The image will be cached as part of buildkit, allowing for faster builds. This is especially important as `WITH DOCKER` wipes the state of the Docker daemon (including its cache) after every run.
* The Daemon within `WITH DOCKER` is not logged into registries. Your local Docker login config is not propagated to the daemon. This means that you may run into issues when trying to pull images from private registries, but also, DockerHub rate limiting may prevent you from pulling images consistently from public repositories.

```Dockerfile
# Bad: Image hello-world needs to be pulled every time and is not part of the Earthly-managed cache.
WITH DOCKER
   RUN docker run hello-world
END
```

```Dockerfile
# Good
WITH DOCKER --pull hello-world
   RUN docker run hello-world
END
```

If you use `WITH DOCKER --compose`, Earthly will automatically pull images declared in the compose file for you, as long as they are not already being loaded from another target via `WITH DOCKER --load`. So in this case, you do not need to declare those image with `WITH DOCKER --pull`.

### Style: Define the high-level targets at the top of the Earthfile

High-level targets are those targets that are meant to be executed directly by the user on the command-line or via the CI.

As software engineers, we read code more often than we write it. As a matter of style, it is recommended to declare the higher-level targets at the top of the Earthfile, to help with the usability of the Earthfile. This will help fellow engineers who have not worked on the Earthfile to quickly find the relevant targets to use in their day-to-day development.

It also helps a reader to consume the Earthfile starting from the top, forming a high-level picture first, then gradually going deeper and deeper to lower-level logic.

### Use `COPY +my-target/...` to pass files to and from `LOCALLY` targets

When using `LOCALLY`, it is tempting to skip on using Earthly constructs for passing files between targets. However, this can be problematic.

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +build
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
build:
    COPY ./my-artifact.txt ./
    ...
```

This setup may actually work, but it has a key issue: the order of `+dep` and `+build` is not guaranteed. So in some runs, the file `./my-artifact.txt` will be created before the `+build` target is executed, and in some runs it will be created after.

To fix this race condition, you need to use an [artifact reference](https://docs.earthly.dev/docs/guides/importing), to ensure that Earthly is aware of the dependency between the two targets:

```Dockerfile
# Good
all:
    BUILD +build
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt
build:
    COPY +dep/my-artifact.txt ./
    ...
```

Here is another example of the reverse (copying a file to a `LOCALLY` target):

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +run-locally
dep:
    FROM alpine:3.18
    WORKDIR /work
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt AS LOCAL ./build/my-artifact.txt
run-locally:
    LOCALLY
    RUN echo ./build/my-artifact.txt
```

The mistake here is relying on `SAVE ARTIFACT ... AS LOCAL ...` for the transfer of the artifact to the `LOCALLY` target. As Earthly outputs are written at the end of the build, the target `+run-locally` will not have the file in time (or it might have it from a previous run only, meaning that it might be stale).

Here is how to fix this:

```Dockerfile
# Good
all:
    BUILD +run-locally
dep:
    FROM alpine:3.18
    WORKDIR /work
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt
run-locally:
    LOCALLY
    COPY +dep/my-artifact.txt ./build/my-artifact.txt
    RUN echo ./build/my-artifact.txt
```

The `COPY` command using an artifact reference will inform Earthly of the dependency between the two targets, and will therefore cause the transfer of artifact between the two properly.

And finally, here is another common mistake, when passing files between two `LOCALLY` targets:

```Dockerfile
# Bad
all:
    BUILD +dep
    BUILD +run-locally
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt AS LOCAL ./build/my-artifact.txt
run-locally:
    LOCALLY
    RUN echo ./build/my-artifact.txt
```

```Dockerfile
# Also bad
all:
    BUILD +run-locally
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt AS LOCAL ./build/my-artifact.txt
run-locally:
    BUILD +dep # Order still not guaranteed
    LOCALLY
    RUN echo ./build/my-artifact.txt
```

Here, the mistake is that the order of operations is not guaranteed. Earthly does not know that the two targets depend on each other, and therefore might decide to run them out of order. It might work sometimes, but it is not guaranteed that it will work every time.

To address this, again, the relationship between the two targets should be declared via `COPY` and an artifact reference.

```Dockerfile
# Good
all:
    BUILD +run-locally
dep:
    LOCALLY
    RUN echo "Hello World" > ./my-artifact.txt
    SAVE ARTIFACT ./my-artifact.txt
run-locally:
    LOCALLY
    COPY +dep/my-artifact.txt ./build/my-artifact.txt
    RUN echo ./build/my-artifact.txt
```

### Use `WITH DOCKER --load=+my-target` to pass images to `LOCALLY` targets

Earthly is able to output Docker images to the local Docker daemon at the end of each build. However, when requiring an image for a `LOCALLY` target, the image needs to be output in the *middle* of the build.

```Dockerfile
# Bad
all:
    BUILD +build-img
    BUILD +run-img
build-img:
    ...
    SAVE IMAGE my-co/my-img:latest
run-img:
    LOCALLY
    RUN docker run my-co/my-img:latest
```

The above will not work as the output will take place at the end of the build only. In addition, Earthly is unaware that there is a dependency between the two targets. To address this, we need to use `WITH DOCKER --load` and a [target reference](https://docs.earthly.dev/docs/guides/importing):

```Dockerfile
# Good
all:
    BUILD +run-img
build-img:
    ...
    SAVE IMAGE my-co/my-img:latest
run-img:
    LOCALLY
    WITH DOCKER --load=+build-img
        RUN docker run my-co/my-img:latest
    END
```

The `--load` instruction will inform Earthly of the dependency and will therefore cause the image to be output right before the `WITH DOCKER` `RUN` command executes.

### Avoid non-deterministic behavior

It is generally recommended to avoid any non-deterministic behavior when designing Earthly builds. This may include:

* Introducing time-stamps in builds or in tags
* Generating unique IDs
* Initializing `ARG` with values that include randomness

The main reason to avoid non-deterministic behavior is to ensure that builds are repeatable, and to maximize the use of cache. If an intermediate step leads to the same result as a previous run, Earthly may be able to reuse further computation performed previously.

Many compilers, code generators and other tools might not be deterministic and there may be no way around it. Earthly still functions correctly in these cases, however there may be occasions where the cache is not fully utilized to its potential.

### Use `COPY --dir` to copy multiple directories

The classical Dockerfile `COPY` command differs from the unix `cp` in that it will copy directory *contents*, not the directories themselves. This requires that copying multiple directories to be split across multiple lines:

```Dockerfile
# Avoid: too verbose
COPY dir-1 dir-1
COPY dir-2 dir-2
COPY dir-3 dir-3
```

This is repetitive and uses more cache layers than should be necessary.

Earthly introduces a setting, `COPY --dir`, which makes `COPY` behave more like `cp` and less like the Dockerfile `COPY`. The `--dir` flag can be used therefore to copy multiple directories in a single command:

```Dockerfile
# Good
COPY --dir dir-1 dir-2 dir-3 ./
```

### Use separate images for build and production

To keep production images small, it is advisable to start from a new base image and to install only production-required dependencies and then to copy in only the final built binaries or packages. This technique may vary from language to language, depending on the ecosystem-specific tooling.

An an example, for Go, you might have a development image, that contains the entire Go development tools, including the `go` binary. After the application binary has been built via `go build`, there is no longer a need for the `go` binary. So the production image should not contain it. Here is an example:

```Dockerfile
# Avoid: production image is bloated
FROM go:1.16
RUN apk add ... # development + production dependencies
build:
    COPY ...
    RUN go mod download
    COPY ...
    RUN go build ... -o /usr/bin/app
    ENTRYPOINT ["/usr/bin/app"]
    SAVE IMAGE my-production-image:latest
```

Here is a way to address this:

```Dockerfile
# Good
FROM go:1.16
RUN apk add ... # development dependencies
build:
    COPY ...
    RUN go mod download
    COPY ...
    RUN go build ... -o ./build/app
    SAVE ARTIFACT ./build/app
image:
    FROM alpine:3.18 # start afresh
    RUN apk add ... # production dependencies only
    COPY +build/app /usr/bin/app
    ENTRYPOINT ["/usr/bin/app"]
    SAVE IMAGE my-production-image:latest
```

### Use `SAVE ARTIFACT ... AS LOCAL ...` for generated code, not `LOCALLY`

Many programming tools require the generation of code. The generated code is often used in completing a build, but also it might be required for IDEs to perform code completion. For this reason, it's often preferable that generated code is also output as local files during development.

It is recommended that any generated code is saved via `SAVE ARTIFACT ... AS LOCAL ...` via regular Earthly targets, rather than via running the generation command in `LOCALLY`. There are multiple reasons for this:

* Executing commands via `LOCALLY` loses the repeatability benefits. This means that the same command could end up generating different code, depending on the system it is being run on. Differences in the environment, such as the version of code generator installed (e.g. `protoc`), or certain environment variables (e.g. `GOPATH`) could cause the generated code to be different.
* The logic to generate code via `LOCALLY` will not be usable in the CI, as the CI script would typically enable `--strict` mode.
* If the code generation workflow requires that the generated code is committed to the repository and then used in a subsequent earthly build, it is possible that due to human error, changes will be made to the input files, without the generated code to be updated correctly. If a problem or an incompatibility is introduced in this manner, it will only show up later, for other people when they try to generate the code themselves. In worse cases, it may even go unnoticed and end up in production.

### Multi-line strings

To specify a multi-line string in Earthly, you can simply start quotes on one line and end them on another.

```Dockerfile
# Bad
RUN echo "this is a" > /tmp/file
RUN echo "multi-line string" >> /tmp/file
RUN echo "that goes" >> /tmp/file
RUN echo "on" >> /tmp/file
RUN echo "and on" >> /tmp/file
ARG MULTILINE_STRING=$(cat /tmp/file)
```

```Dockerfile
# Good
ARG MULTILINE_STRING="this is a
multi-line string
that goes
on
and on"
```

### Multi-line commands

To execute commands that may span multiple lines, you can use the line continuation character (`\`). Remember to chain multiple shell commands via `&&` in order to correctly exit if one of the commands fails.

```Dockerfile
RUN go build ... && \
    if [ "$FOO" = "bar" ]; then \
        echo "spaghetti" > ./default-food.txt ;\
    fi
```

### Copying files from outside the build context

It is generally advisable to avoid copying files outside of the build context. If a file is required from a sibling directory, or from a parent directory, it is recommended that those files are exported via `SAVE ARTIFACT` and then copied over using an artifact reference.

```
├── dir1
|   └── some-file.txt
└── dir2
    ├── other-files...
    └── Earthfile
```

```Dockerfile
# ./dir2/Earthfile
# Bad: does not work
COPY ../dir1/some-file.txt ./
```

In the above example, the file `some-file.txt` is copied from the sibling directory `dir1`. This will not work in Earthly as the file is not in the build context of `./dir2/Earthfile` (the build context in this case is `./dir2`). To address this issue, we can create an Earthfile in `dir1` that exports the file `some-file.txt` as an artifact.

```
├── dir1
|   ├── some-file.txt
|   └── Earthfile
└── dir2
    ├── other-files...
    └── Earthfile
```

```Dockerfile
# ./dir1/Earthfile
VERSION 0.7
FROM alpine:3.18
WORKDIR /work
file:
    COPY some-file.txt ./
    SAVE ARTIFACT ./some-file.txt
```

```Dockerfile
# ./dir2/Earthfile
# Good
COPY ../dir1+file/some-file.txt ./
```

The passing of the file as an artifact will also help create a build API of `dir1`, where all the files required outside of it are explicitly exported.

If a file is needed and there is no good way of adding an Earthfile to the directory containing it (e.g. a common file from the user's home directory), then an option is to use `LOCALLY`.

```Dockerfile
file:
    LOCALLY
    SAVE ARTIFACT $HOME/some-file.txt
do-something:
    COPY +file/some-file.txt ./
```

Note, however, that `LOCALLY` is not allowed in `--strict` mode (or in `--ci` mode), as it introduces a dependency from the host machine, which may interfere with the repeatability property of the build.

Although performing a `COPY ../` is not possible in Earthly today, there are some rare, but valid use-cases for this functionality. This is being discussed in GitHub issue [#1221](https://github.com/earthly/earthly/issues/1221).

### Repository structure: Place build logic as close to the relevant code as possible

When designing builds, it is advisable to place lower-level build logic closer to the code that it is building. This can be achieved by splitting Earthly builds across multiple Earthfiles, and placing some of the Earthfiles deeper inside the directory structure. The lower-level Earthfiles can then export artifacts and/or images via `SAVE ARTIFACT` or `SAVE IMAGE` commands, respectively. Those artifacts can then be referenced in higher-level Earthfiles via artifact and target references (`COPY ./deep/dir+some-target/an/artifact ...`, `FROM ./some/path+my-target`).

This allows for low coupling between modules within your code and creates a "build API" for your directories, whereby all externally accessible artifacts are exposed explicitly.

As one example, you might find the [monorepo example](https://github.com/earthly/earthly/tree/main/examples/monorepo) to be a useful case-study. However, even when a repository contains a single project, you might still find it useful to split logic across multiple Earthfiles. An example might be including Protocol Buffers generation logic inside the subdirectory containing the `.proto` files, in its own Earthfile.

For a real-world example, you can also take a look at Earthly's own build, where several Earthfiles are scattered across the repository to help organize build logic across modules, very much like regular code. Here are some examples:

* [`ast/parser`](https://github.com/earthly/earthly/tree/main/ast/parser) - Earthfile contains the logic for generating Go source code based on an ANTLR grammar.
* [`ast/parser/tests`](https://github.com/earthly/earthly/tree/main/ast/tests) - Earthfile contains logic for running AST-specific tests.
* [`buildkitd`](https://github.com/earthly/earthly/tree/main/buildkitd) - Earthfile contains the logic for building the Earthly buildkit image.
* [`tests`](https://github.com/earthly/earthly/tree/main/tests) - Earthfile contains logic for executing e2e tests.
* [`release/**/`](https://github.com/earthly/earthly/tree/main/release) - Multiple Earthfiles contain logic used for the release of Earthly.
* [The main Earthfile](https://tinyurl.com/yt3d3cx6) - ties everything together, referencing the various targets across the sub-directories.

### Repository structure: Do not place all Earthfiles in a dedicated directory

A common practice when using Dockerfiles is to place all Dockerfiles in a special directory of the repository.

```
# Pattern common for Dockerfiles, but should be avoided for Earthfiles
├── app1-src-dir
|   └── ...
├── app2-src-dir
|   └── ...
├── app3-src-dir
|   └── ...
└── services
    ├── app1.Dockerfile
    ├── app2.Dockerfile
    └── app3.Dockerfile
```

And then running `docker build -f ./services/app1.Dockerfile ./app1-src-dir ...` and so on.

In Earthly, however, this is an anti-pattern, for a couple reasons:

* Every repository using Earthly should have a common structure, to help the user navigate the build. The convention is that Earthfiles are as close to the code as possible, with some high-level targets exposed in the root of the repository, or the root of the directory containing the code for a specific app. Having this convention helps the users who have not written the Earthfiles to quickly be able to browse around and understand the build, at least at a high level.
* Cross-directory and cross-repository references will point to directories where the user expects an Earthfile to be present, and then to a specific target or function within that Earthfile. It is important for this discoverability to be available to anyone browsing the build code and understanding the connections between Earthfiles.

For these reasons, Earthly does not support placing all Earthfiles in a single directory, nor the equivalent of a `docker build -f` option.

### Pattern: Pass-through artifacts or images

If a target acts as a wrapper for another target and that other target produces artifacts, you may find it useful for the wrapper to also emit the same artifacts. Consider the following example of the target `+build-for-windows`:

```Dockerfile
# No pass-through artifacts
VERSION 0.7
FROM alpine:3.18
build:
    ARG some_arg=...
    ARG another_arg=...
    ARG os=linux
    RUN ...
    SAVE ARTIFACT ./output
build-for-windows:
    BUILD +build --some_arg=... --another_arg=... --os=windows
```

```Dockerfile
# With pass-through artifacts
VERSION 0.7
FROM alpine:3.18
build:
    ARG some_arg=...
    ARG another_arg=...
    ARG os=linux
    RUN ...
    SAVE ARTIFACT ./output
build-for-windows:
    COPY (+build --some_arg=... --another_arg=... --os=windows) ./
    SAVE ARTIFACT ./*
```

The fact that `+build-for-windows` itself exports the artifacts means that it can be referenced directly in other targets as `COPY +build-for-windows/output ./`.

Similarly, if a target emits an image, then that image can be also emitted by a wrapping target like so:

```Dockerfile
# No pass-through image
VERSION 0.7
FROM alpine:3.18
build:
    ARG some_arg=...
    ARG another_arg=...
    RUN ...
    SAVE IMAGE some-intermediate-image:latest
build-wrapper:
    BUILD +build --some_arg=... --another_arg=...
```

```Dockerfile
# With pass-through image
VERSION 0.7
FROM alpine:3.18
build:
    ARG some_arg=...
    ARG another_arg=...
    RUN ...
    SAVE IMAGE some-intermediate-image:latest
build-wrapper:
    FROM +build --some_arg=... --another_arg=...
    SAVE IMAGE i-can-give-this-another-name:latest
```

This allows for `+build-wrapper` to reuse the logic in `+build`, but ultimately to create an image that is saved under a different name. This can then be used in a `WITH DOCKER --load` statement directly (whereas if there was no image pass-through, then `+build-wrapper` couldn't have been used).

### Use `earthly/dind`

When using `WITH DOCKER`, it is recommended that you use the official `earthly/dind` image (preferably `:alpine`) for running Docker-in-Docker. Earthly's `WITH DOCKER` requires that the Docker engine is installed already in the image it is running in.

If Docker engine is not detected, `WITH DOCKER` will need to first install it - it usually does so automatically - however, the cache will be inefficient. Consider the following example:

```Dockerfile
# Avoid
integration-test:
    FROM some-other-image:latest
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml
        RUN ...
    END
```

Let's assume that `some-other-image:latest` does not already have Docker engine installed. This means that on the `WITH DOCKER` line, Earthly will add a hidden installation step, to add Docker engine. This takes some time to execute, but it will work.

The problem, however, will be apparent when there is a change (no matter how small) to `docker-compose.yml`. That will cause the build to re-execute without cache from the `COPY` command onwards, meaning that the installation of Docker engine will be repeated.

A simple way to fix this is to use an earthly-provided [function](https://docs.earthly.dev/docs/guides/functions) to install Docker engine before the `COPY` command. Please note that this particular function is fastest when ran on top of an alpine-based image.

```Dockerfile
# Better
integration-test:
    FROM some-other-image:latest
    DO github.com/earthly/lib+INSTALL_DIND
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml
        RUN ...
    END
```

The best supported option, however, is to use the `earthly/dind` image, if possible.

```Dockerfile
# Best - if possible
integration-test:
    FROM earthly/dind:alpine-3.18-docker-23.0.6-r4
    COPY docker-compose.yml ./
    WITH DOCKER --compose docker-compose.yml
        RUN ...
    END
```

### Pattern: Saving artifacts resulting from a `WITH DOCKER`

In Earthly, `WITH DOCKER` starts up a transient Docker daemon for that specific instruction and then shuts it down and completely wipes its data afterwards. That does not mean, however, that you cannot export any information from it (or from any container running within), to be used in another part of the build. Although you may not run any non-`RUN` commands within `WITH DOCKER`, you can still use `SAVE ARTIFACT` (and any other command) after the `WITH DOCKER` instruction. The Docker daemon's data is wiped - but the rest of the build environment remains intact.

```Dockerfile
WITH DOCKER ...
    RUN docker run -v ./screenshots:/screenshots ... && \
        docker logs ... >./full-logs.txt && \
        docker inspect ... >./some-docker-state.json
END
SAVE ARTIFACT ./screenshots
SAVE ARTIFACT ./full-logs.txt
SAVE ARTIFACT ./some-docker-state.json
```

## Usage-specific

### Use `--ci` when running in CI

Build scripts serve slightly different purposes when they are run in CI compared to when they are executed for local development. Most of the logic is similar (hence Earthly attempts to unify the two concepts in a single syntax), but there are some small differences.

For example, for development purposes, you may use commands such as `LOCALLY`, which cause Earthly to be less repeatable, and yet might satisfy very much needed use-cases that are typically out of scope of a CI build.

In addition, in CI it is much more likely that shared caching will be needed, while outputting artifacts and images in the CI's host environment itself would not be needed.

For these reasons, Earthly comes with the `--ci` flag, which simply expands to `--no-output --use-inline-cache --save-inline-cache --strict`. The `--ci` flag therefore, prevents the use of commands that are not repeatable, enables inline caching and disables outputting artifacts and images on the CI host.

### Avoid `LOCALLY` and other non-strict commands

Certain Earthly functionality is only meant to be used for local development only. Most such commands do not fully abide by the Earthly spirit of repeatable builds, however, for certain specific development use-cases they are needed and therefore Earthly provides them. When Earthly is used in `--strict` mode (`earthly --strict +my-target` or `earthly --ci +my-target`), the usage of these commands is not allowed.

For this reason, it is recommended to avoid using these commands as much as possible, as doing so will:

1. Cause Earthly to behave in a non-repeatable way across other platforms, as it will rely on host-specific environment configuration.
2. Disable caching.
3. Cause the specific targets to not work at all when `--ci` is passed in.

An example of a command that is not allowed in strict mode is `LOCALLY`. The `LOCALLY` command skips the sandboxing of the build and executes all commands directly on the host machine.

Examples of valid cases where `LOCALLY` may be used are:

* installing dependencies on the host machine (e.g. to help IDEs provide better suggestions)
* executing tests on the host docker daemon, to help with inspection and debugging
* executing development commands which would otherwise require copying very large amounts of files to the sandboxed build environment

Note, however, that none of these cases are needed in a CI environment, and ultimately these commands are not regularly tested by a CI, which means they may break more frequently.

### Pattern: Push on the `main` branch only

When using Earthly in a sandboxed CI, it may be useful to perform pushes on occasion, in order to populate shared caches. In addition, image pushes might also help developers to grab pre-built images for local use for various development workflows.

Pushing too often can result in slowing down builds due to the upload time, while pushing too infrequently results in stale cache or stale development images.

A good balance is often to perform pushes on the `main` branch only, and to disable any pushing on PR builds. Although the `main` build will be slower, it will allow for maximum use of cache in PR builds, without the slowdown of further pushes.

Main branch build: `earthly --ci --push +target`. PR build: `earthly --ci +target`.

The push option can also be configured via the env var `EARTHLY_PUSH`, which may be easier to manipulate in your CI of choice.

A more extreme case of this idea can be to use explicit maximum cache: `earthly --ci --push --remote-cache=.... --max-remote-cache +target`. The idea, again is to tradeoff performance on the `main` branch, for the benefit of faster PR builds. Whether this is actually beneficial needs to be measured on a project-by-project basis, however.

### Do not expose cache image tags publicly if the cache contains private code or dependencies

When using shared caching, Earthly has the ability to save some intermediate information about the build in a Docker registry of choice. Note, however, that the intermediate cache may also contain private code or dependencies, which could be exposed via the cache in some cases. Even if the final image only contains compiled binaries, it may still be possible to access intermediate layers that lead to the fully compiled binaries - some of which may contain private code or dependencies.

As such, when working on a closed-source project, it is advisable to only use private image repositories to prevent any code leaks.

### Technique: Use `earthly -i` to debug failures

In Earthly it is possible to drop into the container of a failed step to diagnose the failure better. To turn on this setting you can use the `-i` flag: `earthly -i +my-target`. Once dropped into the container's shell, you may use the up arrow to pre-populate the previously failed command should you wish to retry it or amend it. To exit the shell, press `Ctrl+D`.

### Run everything in a single Earthly invocation, do not wrap Earthly

Historically, build scripts have been constructed by cobbling up multiple technologies together: Makefiles, Bash scripts, Dockerfiles, Python scripts, Ruby scripts, and so on. The possibilities are endless, but also the readability and maintainability of the scripts suffer.

Earthly has been designed with a few key goals in mind:

* Repeatability - the builds should just work on another system
* Readability - the builds should be understandable by any team member on the team, without much effort
* A universal CI script - a script that contains all the information needed for the CI to perform a complete build

In this spirit, Earthly has been designed to not require any wrapping around it. Here are some examples of antipatterns:

* **Antipattern**: Earthly is called repeatedly in a single script in order to process intermediate results and then pass those results to later invocations.
* **Antipattern**: Downloading dependencies outside of Earthly and then copying them in.
* **Antipattern**: Performing a build without `--push` and then repeating the same build, but with `--push` enabled.
* **Antipattern**: Computing the value of an `ARG` outside of Earthly and then calling Earthly with that value.
* **Antipattern**: Running `earthly` in a bash `for` loop, to process multiple targets as separate builds.
* **Antipattern**: Running `earthly` repeatedly, rather than using an `all` target encapsulating all the targets needed to be built.
* **Antipattern**: Running `earthly` repeatedly with `--no-cache`, to control the order of a deployment, instead of using `RUN --push` adequately.

All of the above should be avoided as they hinder repeatability and/or they are abusing Earthly features in ways Earthly was not designed for. If a wrapping script is used outside of Earthly, it means that the script is not containerized, which means that the script is susceptible to host environment nuances.

The differences can be somewhat surprising: `make` and `sed` can be different on a Mac compared to a Linux machine, for example. Various linux distributions might have different versions of `bash` installed. Environment variables could play surprising roles. Causes for inconsistencies can sip in from anywhere, making builds more difficult to maintain.

To keep your build scripts uniform across projects (and thus more readable) and to keep them repeatable, it is best if `earthly` is used directly and with minimal argument overrides.

### Use `RUN --ssh` for passing host SSH keys to builds

Earthly provides a way to pass-through access to your host's SSH keys to the build, by proxying the host's ssh-agent connection inside the build. This may be useful if you need to access private repositories where you authenticate with SSH. An example of such a case might be downloading Go dependencies from private repositories:

```Dockerfile
RUN --ssh go mod download
```

### Use SAVE IMAGE to always cache

The simplicity of Earthly comes from its ability to cache build steps that do not need to be rerun. There are times, though, when you have more insight into the build process than Earthly does and may need to manually manage the cache for certain steps. Using an image push is an advanced technique that lets you tell Earthly, **"I want to always cache this step."**

For example, consider the Earthly Blog's Earthfile, which has a base image that installs Pandoc, among other utilities:

```Dockerfile
base:
    FROM ruby:2.7
    ARG TARGETARCH
    WORKDIR /site
    ...
    RUN apt-get install pandoc  pandocfilters -y

build:
    FROM +base
    # Build blog
```

Typically, installing Pandoc from source can take up to 30 minutes. When cached, the blog build process takes about 5 minutes, but without the cache, it jumps to 35 minutes. Occasionally, due to the heavy disk usage of the blog build, the base image may be evicted from the cache, leading to a slower build.

To circumvent this, the solution is to push the base step as an image and reference it directly in subsequent builds:

```Dockerfile
base:
    FROM ruby:2.7
    ARG TARGETARCH
    WORKDIR /site
    ...
    RUN apt-get install pandoc  pandocfilters -y

    # Manually cache the base image by pushing it to a registry
    SAVE IMAGE –push earthly/blog-base-image:latest

build:
    # Use the cached base image for builds  
    FROM earthly/blog-base-image:latest
    RUN ...
```

By doing this, we ensure that the build process is consistently swift, as the base layers do not need to be rebuilt. The trade-off is that the base target needs to be updated manually. For the Earthly website, we address this by running earthly `+base` once a week via a CI job, and on-demand whenever there are changes to the base image. You can see the full example, including flags for manual rerunning the base image, on GitHub.

#### Caveats to this approach

* Caching externally in an image registry adds download time to the build. This technique is most effective when the build time saved is significantly greater than the potential time to download the layer from a registry.
* By manually caching part of the build, you risk introducing inconsistencies. It's important to rerun the step that produces the image manually whenever there are changes. Scheduling a regular job can mitigate this risk.

#### Effective use cases

* **Expensive build steps that rarely change.** Earthly's cache operates on a least-recently-used (LRU) basis, trying to retain frequently used cache steps. However, some steps are more costly to regenerate than others. An external image can serve as a reliable fallback if an expensive step is evicted from the cache.
* **Benign Nondeterminism:** Earthly’s cache expects determinism. It assumes that if an input file changes, the associated build step must be rerun. If you know a step can be cached despite changes in inputs, using SAVE IMAGE for caching allows you to manage this manually and avoid unnecessary cache invalidation.

### Future: Saving an artifact even if the build fails

We are aware of the lack of capability here. Please follow GitHub issues [#988](https://github.com/earthly/earthly/issues/988) and [#587](https://github.com/earthly/earthly/issues/587) for updates.

There are currently workarounds for this (see [this comment](https://github.com/earthly/earthly/issues/988#issuecomment-870504677) and [this comment](https://github.com/earthly/earthly/issues/988#issuecomment-981088796)), however they have significant limitations.

# Caching

Caching is at the heart of how Earthly works. It is what makes Earthly builds fast. This page provides a high-level understanding of the main concepts.

1. **When is Earthly fast** - in what situations Earthly will be fast
2. **How caching works in Earthfiles**
3. **How to share cache** between machines, or between runs in ephemeral CIs
4. **Managing cache** - how to reset it, how to configure its size, etc.

## When is Earthly fast

The word "build" can mean many things across many different contexts. When we say that it makes builds faster, we generally mean CI/CD builds.

Here are contexts in which Earthly does a particularly good job in, thanks to its caching:

* Making CI builds faster, especially in these circumstances
  * The CI performs many redundant tasks upfront, like installing dependencies and pulling container images.
  * The CI is a sandboxed CI, where no state is transferred over from one run to the next without explicitly uploading / downloading on each run (e.g. GitHub Actions, Circle CI)
  * Monorepos and Polyrepos: The CI builds multiple interconnected projects or sub-projects at a time
* Making local builds faster, especially in these circumstances
  * The build being executed is the CI build itself (and not just of the component you’re working on)
  * The build is complex, involving multiple projects or sub-projects at a time, possibly using multiple programming languages, where some of the projects could be rebuilt with a lot of cache shared with the CI or with teammates
  * Your internet connection is slow, and you need to perform a lot of image pushes and/or pulls

Here are examples where Earthly doesn’t improve performance:

* Local builds, when you’re iterating in a tight loop in a single programming language. Usually the tools of that programming language are already highly optimized for this use-case and often work better natively.
* CI builds, when the environment is shared between runs (unsafe), and you’re building programming languages with good built-in caching.
* CI builds, when the redundant parts of the build, like installing dependencies, are cached, AND the CI setup preserves the cache well, WITHOUT the need for downloading or uploading.
* CI builds that involve working with large files (i.e. >1 GB files), due to some internal transferring of files that Earthly relies on.

Now all this might be too complicated to remember, so here’s a simplified version. Earthly is:

* Almost always faster in CI, and especially faster in sandboxed CI environments.
* Usually not faster for local builds where you’re iterating in a single programming language in a tight loop.
* Often faster locally, when intending to run the same build as the CI.

The sections below go into more detail about how you are able to get faster builds with Earthly.

## Caching in Earthfiles

Main article: [Caching in Earthfiles](https://docs.earthly.dev/docs/caching/caching-in-earthfiles)

There are three main ways in which Earthly performs caching of builds:

1. **Layer-based caching**. If an Earthfile command is run again, and the inputs to that command are the same, then the cache layer is reused. This allows Earthly to skip re-executing parts of the build that have not changed.
2. **Cache mounts**. Earthly allows you to mount directories into the build environment - either via [`RUN --mount type=cache`](https://docs.earthly.dev/earthfile#run), or via the [`CACHE`](https://docs.earthly.dev/earthfile#cache) command. These directories are persisted between runs, and can be used to store intermediate build files for incremental compilers, or dependencies that are downloaded from the internet.
3. **Auto-skip**. Earthly allows you to skip large parts of a build in certain situations via `earthly --auto-skip` (*experimental*) or `BUILD --auto-skip` (*coming-soon*). This is especially useful in monorepo setups, where you are building multiple projects at once, and only one of them has changed.

## Sharing Cache

The above capabilities can make your builds very fast. However, if you are using ephemeral CI runners, all of that valuable context can be lost between runs, resulting in poor build performance. Earthly's remote runners and caching via a registry capabilities solve this problem.

Since most CI platforms do not allow reusing state between runs efficiently, passing Earthly's cache via traditional CI cache constructs that rely on an upload and a download is too inefficient to be practical. Earthly's remote caching via a registry helps by optimizing what is uploaded and downloaded for maximum efficiency, although it does require experimentation to get right, and there are a number of limitations.

The most effective means of sharing cache between runs is to execute the Earthly builds remotely. This allows Earthly maintain the cache close to where it executes, thus being able to access it instantly without the need for an upload/download step. Because all Earthly builds are containerized, you still get the ephemeral nature of the CI runner, allowing for build repeatability, but you also get the benefits of a fast cache that is local to the execution environment.

Below is a comparison between remote runners, such as [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites), and remote caching via a registry.

| Cache characteristic                                         | Remote runners (e.g. Satellite) | Remote Cache via registry                            |
| ------------------------------------------------------------ | ------------------------------- | ---------------------------------------------------- |
| Storage location                                             | Runner (e.g. Satellite)         | A container registry of your choice                  |
| Proximity to compute                                         | ✅ Same machine                  | ❌ Performing upload/download is required             |
| Just works, no configuration necessary                       | ✅ Yes                           | ❌ Requires experimentation with the various settings |
| Concurrent access                                            | ✅ Yes                           | 🟡 Concurrent read access only                       |
| Retains entire cache of the build                            | ✅ Yes                           | ❌ Usually no, due to prohibitive upload time         |
| Retains cache for multiple historical builds                 | ✅ Yes                           | ❌ No, only one build retained                        |
| Cache mounts (`RUN --mount type=cache` and `CACHE`) included | ✅ Yes                           | ❌ No                                                 |

To read more, check out the [remote runners page](https://docs.earthly.dev/docs/remote-runners), and the [caching via a registry](https://docs.earthly.dev/docs/caching/caching-via-registry).

## Managing Cache

For information on how to manage cache either locally, or on a remote runner, like a satellite, see the [Managing Cache guide](https://docs.earthly.dev/docs/caching/managing-cache).

# Caching in Earthfiles

Caching is at the heart of how Earthly works. This page will walk you through the key concepts of caching in Earthfiles.

There are three main ways in which Earthly performs caching of builds:

1. **Layer-based caching**. If an Earthfile command is run again, and the inputs to that command are the same, then the cache layer is reused. This allows Earthly to skip re-executing parts of the build that have not changed.
2. **Cache mounts**. Earthly allows you to mount directories into the build environment - either via [`RUN --mount type=cache`](https://docs.earthly.dev/earthfile#run), or via the [`CACHE`](https://docs.earthly.dev/earthfile#cache) command. These directories are persisted between runs, and can be used to store intermediate build files for incremental compilers, or dependencies that are downloaded from the internet.
3. **Auto-skip**. Earthly allows you to skip large parts of a build in certain situations via `earthly --auto-skip` or `BUILD --auto-skip`. This is especially useful in monorepo setups, where you are building multiple projects at once, and only one of them has changed.

## 1. Layer-based caching

Most commands in an Earthfile create a cache layer as part of the way they execute. You can think of a target in an Earthfile as a cake with multiple layers. If a layer's ingredients change, you need to redo the affected layer, plus any layer on top. Similarly, in an Earthfile target, if the input to a command is different (different ARG values, different source files being COPY'd, or the command itself is different), then Earthly can reuse the layers from a previous run up to that command, but it would have to re-execute that command and what follows after it.

If you happen to be familiar with Dockerfile layer caching, then layer caching in Earthly targets will be very familiar to you as it works the same way.

Earthly supports inheriting from other targets, copying artifacts that result from them, or simply issuing the build of another target. These various target cross-references result in a build graph underneath. Thus, one target could influence whether another target is executed - for example, if a source file changes and that results in rebuilding an artifact in `target1`, but then `target2` performs a `COPY` of that artifact, then at least part of `target2` will need to be re-executed too as a result. Earthly deals with all of this automatically.

Because of how layer caching works, it is best to organize builds in a manner that best utilizes the cache. A common strategy is to download and install dependencies early on in the build. Since the list of dependencies doesn't change very often, this expensive operation will usually be cached. To achieve this, it is important to copy the minimal amount of source files (usually just the file that defines what the dependencies are) before issuing the command that installs the dependencies.

Here is a practical example:

```Dockerfile
# Avoid
COPY . .
RUN go mod download
RUN go build ...
```

In the above example, changing the project's `README.md` or running `git fetch` might cause slow commands like `go mod download` to be re-executed.

Earthly uses `COPY` commands (among other things) to mark certain files as inputs to the build. If any file included in a `COPY` changes, then the build will continue from that `COPY` command onwards. For this reason, you want to be as specific as possible when including files in a `COPY` command. In some cases, you might even have to list files individually.

Here are some possible ways to improve the above example:

```Dockerfile
# Better
COPY go.mod go.sum ./*.go ./
RUN go mod download
RUN go build ...
```

The above is better, as it avoids reacting to changes in `.git` or to unrelated files, like `README.md`. However, this can be arranged even better, to avoid downloading all the dependencies on every `*.go` file change.

```Dockerfile
# Best
COPY go.mod go.sum ./
RUN go mod download
COPY ./*.go ./
RUN go build ...
```

In general, including the smallest set of input files as possible at every step will result in the best cache performance.

## 2. Cache mounts

Sometimes layer caching is not enough to properly express the best way to cache something. Cache mounts help complement layer caching, by allowing the contents of a directory to be reused across multiple builds. Cache mounts can be helpful in cases where the tool you're using to build within Earthly is able to leverage incremental caching on its own. Some package managers are able to do that for downloaded dependencies.

Cache mounts can be used either via [`RUN --mount type=cache`](https://docs.earthly.dev/earthfile#run), or via the [`CACHE`](https://docs.earthly.dev/earthfile#cache) command. Although both allow you to define a path in your build environment where the cache directory would be mounted, there are a few important differences:

* Scope
  * `RUN --mount type=cache` only mounts the cache for that single `RUN` command.
  * `CACHE` mounts it for any `RUN` command that follows in the same target
* Final image
  * With `RUN --mount type=cache`, the contents of the cache are NOT persisted in the final image.
  * With `CACHE`, the contents of the cache are copied into in the final image, and also, as a result will be available to be read in targets inheriting from the original target
* Performance
  * `RUN --mount type=cache` is very performant as it does not require transferring contents at the end
  * `CACHE` can be slow in certain cases, if the contents are large, due to the need to copy the contents into the final image
* Consistency
  * `RUN --mount type=cache` is isolated to a single command, making it more difficult (but not impossible) to pass along files between steps via the cache
  * `CACHE` is available to all commands in the target, making it easier to pass along files between steps via the cache, and thus also easier to run into race conditions, if a parallel build changes the contents of the cache in unexpected ways

Cache mounts, by default, are only available within the same target. So if both `target1` and `target2` define `RUN --mount type=cache,target=/my-cache`, the contents would not be shared. If you would like to share the contents, you can use the `id` option. Setting the `id` makes the cache mount global, allowing any target to access the same contents, as long as they both use the same `id`: `RUN --mount type=cache,id=my-cache-id,target=/my-cache`.

Parallel builds using the same cache mount (or the same build where the mount is used in multiple targets) pose another aspect to be aware of: accessing the cache mount concurrently. By default, sharing is set to `locked` - meaning that parallel executions will wait for each other to complete, thus allowing access by one process at a time. While this is the safest option, it is also the slowest. Keep in mind that this will limit your build parallelism significantly if you overuse global cache mounts. Other possible options are `shared` (allows concurrent access), or `private` (if a parallel execution occurs, a new empty mount is created).

### Drawbacks of cache mounts

Cache mounts can be a versatile tool for controlling caching in ways that layer caching cannot. There are, however, important limitations to understand.

The most important limitation to be aware of is that reusing state from a previous run can be a source of build inconsistency. A test passing just because it starts off with the right contents in cache could later result in deploying a broken application to production.

Another limitation is that cache mounts are not great for passing files from one build step to another. This is because a parallel build could interfere with the cache between steps in ways that are difficult to debug. Be especially mindful that builds from different development branches might interact with each other unexpectedly in this situation. It is therefore best to avoid using cache mounts as a mechanism to pass along information. It is best to extract the result of an operation out of the cache mount within the same operation, to ensure that the cache is locked during this time.

Finally, another important limitation is the fact that cache mounts can grow in size indefinitely. While Earthly does garbage-collect layers and cache mounts on a least-recently-used basis, a cache mount that is used frequently could grow more than expected. In such situations, you should consider managing the lifecycle of the cache contents yourself, by removing unused files from it every few runs. A good place for such cleanup operations is within the same layer (same `RUN` command) that uses the contents, at the end.

## 3. Auto-skip

Auto-skip is a feature that allows Earthly to skip large parts of a build in certain situations. This is especially useful in monorepo setups, where you are building multiple projects at once, and only one of them has changed.

Unlike layer caching and cache mounts (which store cache local to the runner), auto-skip is a global cache stored in a cloud database. In order to use auto-skip, you will need an [Earthly Cloud](https://docs.earthly.dev/earthly-cloud/overview) account.

Auto-skip can be enabled for either an entire run, via `earthly --auto-skip` (*experimental*), or for a specific target, via `BUILD --auto-skip` (*coming soon*).

Unlike layer caching, auto-skip is an all-or-nothing type of cache. Either the entire target is skipped, or none of it is. This is because Earthly does not know which parts of the target are affected by the change. If auto-skip does not deem the run to be skipped, then Earthly will fallback to the other forms of caching to run the build as efficiently as possible.

### When auto-skip is not supported

As auto-skip relies on statically analyzing the structure of the build upfront, including the inter-dependencies between targets across multiple Earthfiles, it is not always possible to use it. If a target being involved has a dynamic name that would only be known at run-time, then auto-skip would have no way of knowing it upfront. In such cases, the build fails with an error message when `--auto-skip` is enabled.

#### Static inference of ARG values

For basic `ARG` operations, auto-skip is able to infer the value of the `ARG` statically, and therefore, it is able to support it. Here is a practical example.

```
# Supported
ARG MY_ARG=foo
BUILD $MY_ARG

# Not supported
ARG MY_ARG=$(cat ./file)
BUILD $MY_ARG
```

In the first case, the value of `MY_ARG` is known statically as its value can be propagated by the auto-skip algorithm. In the second case, the value of `MY_ARG` is not known statically as it depends on a file in the build environment. In such a case, auto-skip is not supported. Note that defining such dynamic `ARG`s is generally allowed, however, as long as the value of the `ARG` is not used in a way that would prevent auto-skip from working.

Similarly, the auto-skip algorithm is able to propagate `ARG`s across targets, as long as the value of the `ARG` is known statically. Here is a practical example:

```
# Supported
ARG MY_ARG=foo
BUILD +target --arg=$MY_ARG

# Might not be supported (depending on how the target uses the arg)
ARG MY_ARG=$(cat ./file)
BUILD +target --arg=$MY_ARG
```

#### Static inference of conditions

`IF` statements are generally supported by auto-skip, however there is a difference in behavior, depending on whether the outcome of the condition can be inferred statically. If the outcome of the condition can be inferred statically, then auto-skip uses the correct `IF` or `ELSE` block for analysis. If the outcome of the condition cannot be inferred statically, then the auto-skip algorithm will analyze both `IF` and `ELSE` blocks, and will only skip the target if both blocks are skipped.

Here is a practical example:

```
# Supported and efficient (only +target2 is analyzed)
ARG MY_ARG=bar
IF [ $MY_ARG = "foo" ]
  BUILD +target1
ELSE
  BUILD +target2
END

# Supported but inefficient (both +target1 and +target2 are analyzed)
ARG MY_ARG=$(cat ./file)
IF [ $MY_ARG = "foo" ]
  BUILD +target1
ELSE
  BUILD +target2
END

# Supported but inefficient (both +target1 and +target2 are analyzed)
IF grep ./file -e "foo" 
  BUILD +target1
ELSE
  BUILD +target2
END
```

#### Unsupported Earthfile features in auto-skip

Here is a list of unsupported features when `--auto-skip` is enabled:

* Dynamic target names, such as `BUILD $MY_TARGET`, `FROM $MY_TARGET`, or `BUILD $(...)`, unless the target name can be inferred statically.
* Dynamic `COPY` commands, such as `COPY $MY_FILE .`, or `COPY $(...) .`, unless the source can be inferred statically.
* Remote references (such as `BUILD github.com/foo/bar+my-target`), unless the remote reference is pinned to a specific SHA, or to an explicit tag expressed as a `tags/...` git reference. For example, `BUILD github.com/foo/bar:tags/v1.0.0+my-target` is supported, but `BUILD github.com/foo/bar:v1.0.0+my-target` is not.
* Remote imports, unless the remote reference is pinned to a specific SHA, or to an explicit tag expressed as a `tags/...` git reference. For example, `IMPORT github.com/foo/bar:tags/v1.0.0` is supported, but `IMPORT github.com/foo/bar:v1.0.0` is not.
* `GIT CLONE`, unless the remote reference is pinned to a specific SHA, or to an explicit tag expressed as a `tags/...` git reference.
* `FOR` loops, unless the list being iterated can be inferred statically.

### Auto-skipping `RUN --no-cache` and `RUN --push`

Unlike layer caching, auto-skip may also skip `RUN --no-cache` and `RUN --push` commands. This can be useful in situations when you would like to skip a deployment, if nothing has changed. Please note that rollbacks may be unintentionally skipped, if attempting to deploy on older version of the codebase that had been previously deployed. In such cases, you can either (a) remove the `--auto-skip` flag to force the deployment to occur, (b) [clear the auto-skip cache](https://docs.earthly.dev/docs/managing-cache#auto-skip-cache), or (c) use roll-forward practices (reverting problematic code changes, and re-deploying as a net-new version).

## Disabling caching

In certain situations, you might want to disable caching either for a specific command, or for the entire build.

To disable layer caching, you can use the `--no-cache` flag. For example, `RUN --no-cache echo "Hello"` will always execute the `echo` command, even if the `RUN` command was executed before with the same arguments. Note that this does not disable cache mounts, or auto-skip. A `RUN --no-cache` command can still be skipped by auto-skip.

To disable layer caching and mount caching for an entire run, you can use `earthly --no-cache +my-target`.

Another way to disable layer caching is to use the `RUN --push` flag. This flag is useful when you want to perform an operation with external effects (e.g. deploying to production). By default Earthly does not run `--push` commands unless the `--push` flag is also specified when invoking Earthly itself (`earthly --push +my-target`). `RUN --push` commands are never cached.

To disable auto-skip, simply remove the `--auto-skip` flag.

## Troubleshooting and gotchas

Debugging caching issues can be tricky. Here are some common issues that you might face and how to resolve them.

### Cache size

If the configured cache size is too small, then Earthly might garbage-collect cached layers more often than you might expect. This can manifest in builds randomly not using cache for certain layers. Usually it is the biggest layers that suffer from this (and oftentimes the biggest layers are the most expensive to recreate). This problem is most common on Mac and Windows, where Docker uses a VM with limited disk size. To resolve this, either configure a larger cache size if you are running local builds, or launch a larger Satellite if you are using remote builds via Earthly Satellites. For more information see the [managing cache page](https://docs.earthly.dev/docs/caching/managing-cache).

### ARGs

In Earthly, like in Dockerfiles, ARGs declared in Earthfiles also behave as environment variables within the target they are declared in. This means that if you declare an ARG, and then use it in a `RUN` command, then the `RUN` command will be invalidated if the ARG changes. This is sometimes not very obvious, especially if you are not actually using the value of that ARG.

For this reason, it is best to declare ARGs as late as possible within the target they are used in, and try to avoid declaring `--global` ARGs as much as possible. If an ARG is not yet declared, it will not influence the cache state of a layer, allowing for more cache hits. Limiting the scope of ARGs as much as possible will yield better cache performance.

Watch out especially for ARGs that change often, such as the built-in ARG `EARTHLY_GIT_HASH`. Declaring this ARG as late as possible in the build will cause less cache misses.

### Secrets

Note that secrets, unlike ARGs, do NOT contribute to the cache state of a layer. This means that if you use a secret in a `RUN` command, and the secret changes, the `RUN` command will not be invalidated.

### Remote caching via registry

Please note that remote caching via registry tends to be very difficult to get right. When using explicit caching, by default, only the layers of the target being directly called are included (if any). From there, you need to add `SAVE IMAGE --cache-hint` across various other targets to add more layers to the remote cache. There is often a trade-off between the upload/download size vs the actual time saved. Significant experimentation is necessary to get this right. Note also that main branch builds might overlap with PR builds, and therefore, you might need to use different cache destinations for each. Usually, using [remote runners](https://docs.earthly.dev/docs/caching/caching-via-remote-runners) is a better alternative to remote caching via registry.

### Force a build step to always cache

If you have already optimized your cache by maximizing its size, declaring arguments as late as possible, and implementing the other recommendations provided here, but you still encounter performance bottlenecks due to computationally intensive tasks being evicted from the cache, consider employing `SAVE IMAGE` commands at strategic points. These images can serve as manual caches and can improve efficiency at the cost of simplicity. For additional details, refer to the [Best Practices](https://docs.earthly.dev/guides/best-practices#use-save-image-to-always-cache) section.

### Debugging tips

If you are experiencing caching issues and have ruled out the above common situations, we would love to hear from you. Please open an issue in the [Earthly GitHub repository](https://github.com/earthly/earthly).

# Managing cache

This page describes how to manage the Earthly cache locally or on a remote runner, such as an Earthly Satellite.

## Local cache

### Local cache location

Earthly cache is persisted in a docker (or podman) volume called `earthly-cache` on your system. When Earthly starts for the first time, it brings up a BuildKit daemon in a Docker container, which initializes the `earthly-cache` volume. The volume is managed by Earthly's BuildKit daemon and there is a regular garbage-collection for old cache.

### Specifying the local cache size limit

The default cache size is adaptable depending on available space on your system. It defaults to 10% or 10 GB, whichever is greater. If you would like to change the cache size, you can specify a different limit by modifying the `cache_size_mb` and/or `cache_size_pct` settings in the [configuration](https://docs.earthly.dev/docs/earthly-config). For example:

```yaml
global:
  cache_size_mb: 30000
  cache_size_pct: 70
```

{% hint style="info" %}
**Checking current size of the cache volume**

You can check the current size of the cache volume by running:

```bash
sudo du -h /var/lib/docker/volumes/earthly-cache | tail -n 1
```

{% endhint %}

### Resetting the local cache

To reset the cache, you can issue the command

```bash
earthly prune
```

You can also safely delete the cache manually, if the daemon is not running

```bash
docker stop earthly-buildkitd
docker rm earthly-buildkitd
docker volume rm earthly-cache
```

Earthly also has a command that automates the above:

```bash
earthly prune --reset
```

## Cache on a remote runner / Earthly Satellite

### Configuring the cache size on a remote runner

If you are using [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites), you can simply launch a bigger satellite via the `--size` flag: `earthly sat launch --size ...`.

If you are using a self-hosted remote runner, you can configure the cache policy by passing the appropriate [buildkit configuration](https://github.com/moby/buildkit/blob/master/docs/buildkitd.toml.md) to the [buildkit container](https://docs.earthly.dev/ci-integration/remote-buildkit).

### Resetting the cache on a remote runner

The command `earthly prune` will work on remote runners too, albeit without the `--reset` flag, which is not supported in a remote setting.

To cause a satellite to restart with a fresh cache, you can use the command `earthly sat update --drop-cache`.

## Auto-skip cache

The auto-skip cache is a cache that is used to skip large parts of a build in certain situations. It is used by the `earthly --auto-skip` and `BUILD --auto-skip` commands.

Unlike the layer cache and the cache mounts, the auto-skip cache is global and is stored in a cloud database.

To clear the entire auto-skip cache for your Earthly org, you can use the command `earthly prune-auto-skip`.

To clear the auto-skip cache for an entire repository, you can use the command `earthly prune-auto-skip --path github.com/foo/bar --deep`.

To clear the auto-skip cache for a specific target, you can use the command `earthly prune-auto-skip --path github.com/foo/bar --target +my-target`.

# Caching via remote runners

Caching via remote runners (such as Earthly Satellites) works by simply reusing the same runner for multiple builds. The runner retains the cache between executions, and thus is able to perform significantly better than any caching mechanism that relies on upload and download. There is nothing special that needs to be configured for this to work. All of the features of caching in Earthly work as expected, including layer caching and cache mounts.

Remote runners can be either self-hosted, or managed by Earthly - see [Earthly Satellites](https://docs.earthly.dev/earthly-cloud/satellites). To learn more, see the [remote runners page](https://docs.earthly.dev/docs/remote-runners).

The [managing cache page](https://docs.earthly.dev/docs/caching/managing-cache) contains information about how to reset the cache remotely, if needed.

---

[Next Page](/llms-full.txt/1)
