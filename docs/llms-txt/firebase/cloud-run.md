# Source: https://firebase.google.com/docs/hosting/cloud-run.md.txt

<br />

<br />

PairCloud RunwithFirebase Hostingto generate and serve your dynamic content or build REST APIs as microservices.

Using[Cloud Run](https://cloud.google.com/run/docs/), you can deploy an application packaged in a container image. Then, usingFirebase Hosting, you can direct HTTPS requests to trigger your containerized app.

- Cloud Runsupports[several languages](https://cloud.google.com/run/docs/quickstarts/build-and-deploy#writing)(including Go, Node.js, Python, and Java), giving you the flexibility to use the programming language and framework of your choice.
- Cloud Run[automatically and horizontally scales](https://cloud.google.com/run/docs/about-concurrency)your container image to handle the received requests, then scales down when demand decreases.
- You only[pay](https://cloud.google.com/run/pricing)for the CPU, memory, and networking consumed during request handling.

**For example use cases and samples forCloud Runintegrated withFirebase Hosting, visit our[serverless overview](https://firebase.google.com/docs/hosting/serverless-overview).**

<br />

This guide shows you how to:

1. [Write a simple Hello World application](https://firebase.google.com/docs/hosting/cloud-run#write)
2. [Containerize an app and upload it toArtifact Registry](https://firebase.google.com/docs/hosting/cloud-run#containerize)
3. [Deploy the container image toCloud Run](https://firebase.google.com/docs/hosting/cloud-run#deploy)
4. [DirectHostingrequests to your containerized app](https://firebase.google.com/docs/hosting/cloud-run#direct_requests_to_container)

Note that to improve the performance of serving dynamic content, you can optionally tune your[cache settings](https://firebase.google.com/docs/hosting/manage-cache).

## Before you begin

Before usingCloud Run, you need to complete some initial tasks, including setting up aCloud Billingaccount, enabling theCloud RunAPI, and installing the`gcloud`command line tool.

### Set up billing for your project

Cloud Runoffers[free usage quota](https://cloud.google.com/run/pricing), but you still must have a[Cloud Billingaccount](https://cloud.google.com/billing/docs/how-to/manage-billing-account)associated with your Firebase project to use or try outCloud Run.
| If your Firebase project is on the Spark pricing plan, and you associate your Firebase project with aCloud Billingaccount, then your Firebase project is automatically upgraded to the Blaze pricing plan. Review the[Firebase pricing page](https://firebase.google.com/pricing)for a comparison of the Spark and Blaze plans. Also, make sure to reviewCloud Run[pricing](https://cloud.google.com/run/pricing)and its[quotas and limits](https://cloud.google.com/run/quotas).
| **Note:** Every Firebase project is also aGoogle Cloudproject.  
| Visit[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship)to learn more about the Firebase andGoogle Cloudproject relationship.

### Enable the API and install the SDK

1. Enable theCloud RunAPI in the Google APIs console:

   1. Open the[Cloud RunAPI page](https://console.cloud.google.com/apis/library/run.googleapis.com?project=_)in the Google APIs console.

   2. When prompted, select your Firebase project.

   3. Click**Enable** on theCloud RunAPI page.

2. [Install and initialize](https://cloud.google.com/sdk/docs/)the Cloud SDK.

3. Check that the`gcloud`tool is configured for the correct project:

   ```
   gcloud config list
   ```

## **Step 1**: Write the sample application

Note thatCloud Runsupports[many other languages](https://cloud.google.com/run/docs/quickstarts/build-and-deploy#writing)in addition to the languages shown in the following sample.  

### Go

1. Create a new directory named`helloworld-go`, then change directory into it:

   ```
   mkdir helloworld-go
   ```  

   ```
   cd helloworld-go
   ```
2. Create a new file named`helloworld.go`, then add the following code:

       package main

       import (
       	"fmt"
       	"log"
       	"net/http"
       	"os"
       )

       func handler(w http.ResponseWriter, r *http.Request) {
       	log.Print("helloworld: received a request")
       	target := os.Getenv("TARGET")
       	if target == "" {
       		target = "World"
       	}
       	fmt.Fprintf(w, "Hello %s!\n", target)
       }

       func main() {
       	log.Print("helloworld: starting server...")

       	http.HandleFunc("/", handler)

       	port := os.Getenv("PORT")
       	if port == "" {
       		port = "8080"
       	}

       	log.Printf("helloworld: listening on port %s", port)
       	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
       }  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-go/helloworld.go

   This code creates a basic web server that listens on the port defined by the`PORT`environment variable.

Your app is finished and ready to be containerized and uploaded toArtifact Registry.

### Node.js

1. Create a new directory named`helloworld-nodejs`, then change directory into it:

   ```
   mkdir helloworld-nodejs
   ```  

   ```
   cd helloworld-nodejs
   ```
2. Create a`package.json`file with the following contents:

       {
         "name": "knative-serving-helloworld",
         "version": "1.0.0",
         "description": "Simple hello world sample in Node",
         "main": "index.js",
         "scripts": {
           "start": "node index.js"
         },
         "author": "",
         "license": "Apache-2.0",
         "dependencies": {
           "express": "^4.21.2"
         }
       }  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-nodejs/package.json

3. Create a new file named`index.js`, then add the following code:

       const express = require('express');
       const app = express();

       app.get('/', (req, res) => {
         console.log('Hello world received a request.');

         const target = process.env.TARGET || 'World';
         res.send(`Hello ${target}!\n`);
       });

       const port = process.env.PORT || 8080;
       app.listen(port, () => {
         console.log('Hello world listening on port', port);
       });  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-nodejs/index.js

   This code creates a basic web server that listens on the port defined by the`PORT`environment variable.

Your app is finished and ready to be containerized and uploaded toArtifact Registry.

### Python

1. Create a new directory named`helloworld-python`, then change directory into it:

   ```
   mkdir helloworld-python
   ```  

   ```
   cd helloworld-python
   ```
2. Create a new file named`app.py`, then add the following code:

       import os

       from flask import Flask

       app = Flask(__name__)

       @app.route('/')
       def hello_world():
           target = os.environ.get('TARGET', 'World')
           return 'Hello {}!\n'.format(target)

       if __name__ == "__main__":
           app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-python/app.py

   This code creates a basic web server that listens on the port defined by the`PORT`environment variable.

Your app is finished and ready to be containerized and uploaded toArtifact Registry.

### Java

1. Install[Java SE 8 or later JDK](https://www.oracle.com/technetwork/java/javase/downloads/index.html)and[CURL](https://curl.haxx.se).

   Note that we only need to do this to create the new web project in the next step. The Dockerfile, which is described later, will load all dependencies into the container.
2. From the console, create a new empty web project using cURL then unzip commands:

   ```
   curl https://start.spring.io/starter.zip \
       -d dependencies=web \
       -d name=helloworld \
       -d artifactId=helloworld \
       -o helloworld.zip
   ```  

   ```
   unzip helloworld.zip
   ```

   This creates a SpringBoot project.
3. Update the`SpringBootApplication`class in`src/main/java/com/example/helloworld/HelloworldApplication.java`by adding a`@RestController`to handle the`/`mapping and also add a`@Value`field to provide the`TARGET`environment variable:

       package com.example.helloworld;

       import org.springframework.beans.factory.annotation.Value;
       import org.springframework.boot.SpringApplication;
       import org.springframework.boot.autoconfigure.SpringBootApplication;
       import org.springframework.web.bind.annotation.GetMapping;
       import org.springframework.web.bind.annotation.RestController;

       @SpringBootApplication
       public class HelloworldApplication {

         @Value("${TARGET:World}")
         String target;

         @RestController
         class HelloworldController {
           @GetMapping("/")
           String hello() {
             return "Hello " + target + "!";
           }
         }

         public static void main(String[] args) {
           SpringApplication.run(HelloworldApplication.class, args);
         }
       }  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-java-spring/src/main/java/com/example/helloworld/HelloworldApplication.java

   This code creates a basic web server that listens on the port defined by the`PORT`environment variable.

Your app is finished and ready to be containerized and uploaded toArtifact Registry.

## **Step 2** : Containerize an app and upload it toArtifact Registry

1. Containerize the sample app by creating a new file named`Dockerfile`in the same directory as the source files. Copy the following content into your file.

   ### Go

   <br />

       # Use the official Golang image to create a build artifact.
       # This is based on Debian and sets the GOPATH to /go.
       FROM golang:latest AS builder

       ARG TARGETOS
       ARG TARGETARCH

       # Create and change to the app directory.
       WORKDIR /app

       # Copy local code to the container image.
       COPY . ./

       # Install dependencies and tidy up the go.mod and go.sum files.
       RUN go mod tidy

       # Build the binary.
       # -mod=readonly ensures immutable go.mod and go.sum in container builds.
       RUN CGO_ENABLED=0 GOOS=${TARGETOS} GOARCH=${TARGETARCH} go build -mod=readonly -v -o server

       # Use the official Alpine image for a lean production container.
       # https://hub.docker.com/_/alpine
       # https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
       FROM alpine:3
       RUN apk add --no-cache ca-certificates

       # Copy the binary to the production image from the builder stage.
       COPY --from=builder /app/server /server

       # Run the web service on container startup.
       CMD ["/server"]  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-go/Dockerfile

   <br />

   ### Node.js

   <br />

       # Use the official lightweight Node.js 12 image.
       # https://hub.docker.com/_/node
       FROM node:12-slim

       # Create and change to the app directory.
       WORKDIR /usr/src/app

       # Copy application dependency manifests to the container image.
       # A wildcard is used to ensure both package.json AND package-lock.json are copied.
       # Copying this separately prevents re-running npm install on every code change.
       COPY package*.json ./

       # Install production dependencies.
       RUN npm install --only=production

       # Copy local code to the container image.
       COPY . ./

       # Run the web service on container startup.
       CMD [ "npm", "start" ]  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-nodejs/Dockerfile

   <br />

   ### Python

   <br />

       # Use the official lightweight Python image.
       # https://hub.docker.com/_/python
       FROM python:3.7-slim

       # Allow statements and log messages to immediately appear in the Knative logs
       ENV PYTHONUNBUFFERED True

       # Copy local code to the container image.
       ENV APP_HOME /app
       WORKDIR $APP_HOME
       COPY . ./

       # Install production dependencies.
       RUN pip install Flask gunicorn

       # Run the web service on container startup. Here we use the gunicorn
       # webserver, with one worker process and 8 threads.
       # For environments with multiple CPU cores, increase the number of workers
       # to be equal to the cores available.
       CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-python/Dockerfile

   <br />

   ### Java

   <br />

       # Use the official maven/Java 8 image to create a build artifact: https://hub.docker.com/_/maven
       FROM maven:3.5-jdk-8-alpine AS builder

       # Copy local code to the container image.
       WORKDIR /app
       COPY pom.xml .
       COPY src ./src

       # Build a release artifact.
       RUN mvn package -DskipTests

       # Use the Official OpenJDK image for a lean production stage of our multi-stage build.
       # https://hub.docker.com/_/openjdk
       # https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
       FROM openjdk:8-jre-alpine

       # Copy the jar to the production image from the builder stage.
       COPY --from=builder /app/target/helloworld-*.jar /helloworld.jar

       # Run the web service on container startup.
       CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/helloworld.jar"]  
       https://github.com/knative/docs/blob/6c9f7c1a8d2a64879be5af432136e767e40011f8/code-samples/serving/hello-world/helloworld-java-spring/Dockerfile

   <br />

2. Build your container image usingCloud Buildby running the following command from the directory containing your Dockerfile:

   ```
   gcloud builds submit --tag gcr.io/PROJECT_ID/helloworld
   ```

   Upon success, you will see a SUCCESS message containing the image name  
   (`gcr.io/`<var translate="no">PROJECT_ID</var>`/helloworld`).

The container image is now stored inArtifact Registryand can be re-used if desired.

Note that, instead ofCloud Build, you can use a locally installed version of Docker to[build your container locally](https://cloud.google.com/run/docs/building/containers#building_locally_and_pushing_using_docker).

## **Step 3** : Deploy the container image toCloud Run

<br />

**AllowedCloud Runregions**

<br />

For the best performance, colocate yourCloud Runservice withHostingusing the following regions:

- `us-west1`
- `us-central1`
- `us-east1`
- `europe-west1`
- `asia-east1`

Rewrites toCloud RunfromHostingare supported in the following regions:

- `asia-east1`
- `asia-east2`
- `asia-northeast1`
- `asia-northeast2`
- `asia-northeast3`
- `asia-south1`
- `asia-south2`
- `asia-southeast1`
- `asia-southeast2`
- `australia-southeast1`
- `australia-southeast2`
- `europe-central2`
- `europe-north1`
- `europe-southwest1`
- `europe-west1`
- `europe-west12`
- `europe-west2`
- `europe-west3`
- `europe-west4`
- `europe-west6`
- `europe-west8`
- `europe-west9`
- `me-central1`
- `me-west1`
- `northamerica-northeast1`
- `northamerica-northeast2`
- `southamerica-east1`
- `southamerica-west1`
- `us-central1`
- `us-east1`
- `us-east4`
- `us-east5`
- `us-south1`
- `us-west1`
- `us-west2`
- `us-west3`
- `us-west4`
- `us-west1`
- `us-central1`
- `us-east1`
- `europe-west1`
- `asia-east1`

<br />

<br />

1. Deploy using the following command:

   <br />

   ```
   gcloud run deploy --image gcr.io/PROJECT_ID/helloworld
   ```

   <br />

2. When prompted:

   - Select a region (for example`us-central1`)
   - Confirm the service name (for example,`helloworld`)
   - Respond`Y`to**[allow unauthenticated invocations](https://cloud.google.com/run/docs/securing/authenticating#public)**

   | **Important:** Remember the region and the service name so that you can use these values when defining the`region`and`serviceID`, respectively, in the[`firebase.json`rewrite rule](https://firebase.google.com/docs/hosting/cloud-run#direct_requests_to_container)later.
3. Wait a few moments for the deploy to complete. On success, the command line displays the service URL. For example:https://helloworld-<var translate="no">RANDOM_HASH</var>-us-central1.a.run.app

4. Visit your deployed container by opening the service URL in a web browser.

| **Note:** Consider applying a[maximum instance limit](https://cloud.google.com/run/docs/about-instance-autoscaling#max-instances)to prevent unexpected scaling of theCloud Runservice.

The next step walks you through how to access this containerized app***from aFirebase HostingURL***so that it can generate dynamic content for your Firebase-hosted site.

## **Step 4:**Direct hosting requests to your containerized app

With[rewrite rules](https://firebase.google.com/docs/hosting/full-config#rewrites), you can direct requests that match specific patterns to a single destination.

The following example shows how to direct all requests from the page`/helloworld`on yourHostingsite to trigger the startup and running of your`helloworld`container instance.

1. Make sure that:

   - You have the[latest version of theFirebaseCLI](https://firebase.google.com/docs/cli#update-cli).

   - You have initializedFirebase Hosting.

   For detailed instructions about installing the CLI and initializingHosting, see the[Get Started guide forHosting](https://firebase.google.com/docs/hosting/quickstart).
2. Open your[`firebase.json`file](https://firebase.google.com/docs/cli#the_firebasejson_file).

3. Add the following`rewrite`configuration under the`hosting`section:

   ```verilog
   "hosting": {
     // ...

     // Add the "rewrites" attribute within "hosting"
     "rewrites": [ {
       "source": "/helloworld",
       "run": {
         "serviceId": "helloworld",  // "service name" (from when you https://firebase.google.com/docs/hosting/cloud-run#deploy)
         "region": "us-central1",    // optional (if omitted, default is us-central1)
         "pinTag": true              // optional (see note below)
       }
     } ]
   }
   ```
4. Deploy your hosting configuration to your site by running the following command from the root of your project directory:

   ```
   firebase deploy --only hosting
   ```

<br />

**How`pinTag`works within the`run`block**

<br />

> With this feature, you can ensure that the revision of yourCloud Runservice for generating your site's dynamic content is kept in sync with your staticHostingresources andHostingconfig. Also, this feature allows you to preview your rewrites toCloud RunonHostingpreview channels.
>
> If you add`"pinTag": true`to a`run`block of the`hosting.rewrites`config, your staticHostingresources and configuration will be pinned to the most recent revision of theCloud Runservice, at the time of deploy. If you roll back a version of your site, the revision of the "pinned"Cloud Runservice is also rolled back.
>
> This feature relies on[Cloud Runtags](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags), which have a limit of 1000 tags per service and 2000 tags per region. This means that after hundreds of deploys, the oldest versions of a site may stop working.

<br />

<br />

Your container is now reachable via the following URLs:

- Your Firebase subdomains:  
  <var translate="no">PROJECT_ID</var>`.web.app/`and<var translate="no">PROJECT_ID</var>`.firebaseapp.com/`

- Any connected[custom domains](https://firebase.google.com/docs/hosting/custom-domain):  
  <var translate="no">CUSTOM_DOMAIN</var>`/`

| **Note:** Firebase Hostingis subject to a 60-second request timeout. If your app requires more than 60 seconds to run, you'll receive an HTTPS status code`504`(request timeout). To support dynamic content that requires longer compute time, consider using an[App Engineflexible environment](https://cloud.google.com/appengine/docs/flexible/).

Visit theHostingconfiguration page for[more details about rewrite rules](https://firebase.google.com/docs/hosting/full-config#rewrites). You can also learn about the[priority order of responses](https://firebase.google.com/docs/hosting/full-config#hosting_priority_order)for variousHostingconfigurations.

## Test locally

During development, you can run and test your container image locally. For detailed instructions, visit the[Cloud Rundocumentation](https://cloud.google.com/run/docs/testing/local).

## Next steps

- [Set up caching](https://firebase.google.com/docs/hosting/manage-cache)of your dynamic content on a global CDN.

- Interact with other Firebase services using the[Firebase Admin SDK](https://firebase.google.com/docs/admin/setup).

- Learn more aboutCloud Run, including[detailed how-to guides](https://cloud.google.com/run/docs/how-to)for setting up, managing, and configuring containers.

- Review the[pricing](https://cloud.google.com/run/pricing)and the[quotas and limits](https://cloud.google.com/run/quotas)forCloud Run.