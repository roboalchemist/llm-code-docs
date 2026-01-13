# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-aws-ecs-fargate.md

---
title: Tutorial - Enabling Tracing for a Java Application on Amazon ECS with Fargate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Java
  Application on Amazon ECS with Fargate
source_url: >-
  https://docs.datadoghq.com/guide/tutorial-enable-java-aws-ecs-fargate/index.html
---

# Tutorial - Enabling Tracing for a Java Application on Amazon ECS with Fargate

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Java application installed in a cluster on AWS Elastic Container Service (ECS) with Fargate. In this scenario, the Datadog Agent is also installed in the cluster.

For other scenarios, including on a host, in a container, on other cloud infrastructure, and on applications written in other languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials). Some of those other tutorials, for example, the ones using containers or EKS, step through the differences seen in Datadog between automatic and custom instrumentation. This tutorial skips right to a fully custom instrumented example.

This tutorial also uses intermediate-level AWS topics, so it requires that you have some familiarity with AWS networking and applications. If you're not as familiar with AWS, and you are trying to learn the basics of Datadog APM setup, use one of the host or container tutorials instead.

See [Tracing Java Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/) for general comprehensive tracing setup documentation for Java.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- Git
- Docker
- Terraform
- Amazon ECS
- an Amazon ECR repository for hosting images
- An AWS IAM user with `AdministratorAccess` permission. You must add the profile to your local credentials file using the access and secret access keys. For more information, read [Using the AWS credentials file and credential Profiles](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-profiles.html).

## Install the sample Java application{% #install-the-sample-java-application %}

The code sample for this tutorial is on GitHub, at [github.com/DataDog/apm-tutorial-java-host](https://github.com/DataDog/apm-tutorial-java-host). To get started, clone the repository:

```sh
git clone https://github.com/DataDog/apm-tutorial-java-host.git
```

The repository contains a multi-service Java application pre-configured to run inside Docker containers. The `docker-compose` YAML files to make the containers are located in the `docker` directory. This tutorial uses the `service-docker-compose-ECS.yaml` file, which builds containers for the application.

In each of the `notes` and `calendar` directories, there are two sets of Dockerfiles for building the applications, either with Maven or with Gradle. This tutorial uses the Maven build, but if you are more familiar with Gradle, you can use it instead with the corresponding changes to build commands.

The sample application is a simple multi-service Java application with two APIs, one for a `notes` service and another for a `calendar` service. The `notes` service has `GET`, `POST`, `PUT`, and `DELETE` endpoints for notes stored within an in-memory H2 database. The `calendar` service can take a request and return a random date to be used in a note. Both applications have their own associated Docker images, and you deploy them on Amazon ECS as separate services, each with its own tasks and respective containers. ECS pulls the images from ECR, a repository for application images that you publish the images to after building.

### Initial ECS setup{% #initial-ecs-setup %}

The application requires some initial configuration, including adding your AWS profile (already configured with the correct permissions to create an ECS cluster and read from ECR), AWS region, and Amazon ECR repository.

Open `terraform/Fargate/global_constants/variables.tf`. Replace the variable values below with your correct AWS account information:

```
output "aws_profile" {
    value = "<AWS_PROFILE>"
    sensitive = true
}

output "aws_region" {
    value = "<AWS_REGION>"
    sensitive = true
}

output "aws_ecr_repository" {
    value = "<AWS_ECR_REPOSITORY_URL>"
    sensitive = true
}
```

### Build and upload the application images{% #build-and-upload-the-application-images %}

If you're not familiar with Amazon ECR, a registry for container images, it might be helpful to read [Using Amazon ECR with the AWS CLI](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html).

In the sample project's `/docker` directory, run the following commands:

1. Authenticate with ECR by supplying your username and password in this command:

   ```sh
   aws ecr get-login-password --region us-east-1 | docker login --username <YOUR_AWS_USER> --password-stdin <USER_CREDENTIALS>
```



1. Build a Docker image for the sample apps, adjusting the platform setting to match yours:

   ```sh
   DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f service-docker-compose-ECS.yaml build
```



1. Tag the containers with the ECR destination:

   ```sh
   docker tag docker_notes:latest <ECR_REGISTRY_URL>:notes
   docker tag docker_calendar:latest <ECR_REGISTRY_URL>:calendar
```



1. Upload the container to the ECR registry:

   ```sh
   docker push <ECR_REGISTRY_URL>:notes
   docker push <ECR_REGISTRY_URL>:calendar
```

Your application (without tracing enabled) is containerized and available for ECS to pull.

### Deploy the application{% #deploy-the-application %}

Start the application and send some requests without tracing. After you've seen how the application works, you'll instrument it using the tracing library and Datadog Agent.

To start, use a terraform script to deploy to Amazon ECS:

1. From the `terraform/Fargate/Uninstrumented` directory, run the following commands:

   ```sh
   terraform init
   terraform apply
   terraform state show 'aws_alb.application_load_balancer'
   ```

**Note**: If the `terraform apply` command returns a CIDR block message, the script to obtain your IP address did not work on your local machine. To fix this, set the value manually in the `terraform/Fargate/Uninstrumented/security.tf` file. Inside the `ingress` block of the `load_balancer_security_group`, switch which `cidr_blocks` line is commented out and update the now-uncommented example line with your machine's IP4 address.

1. Make note of the DNS name of the load balancer. You'll use that base domain in API calls to the sample app. Wait a few minutes for the instances to start up.

1. Open up another terminal and send API requests to exercise the app. The notes application is a REST API that stores data in an in-memory H2 database running on the same container. Send it a few commands:

   {% dl %}
   
   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes'`
   {% /dt %}

   {% dd %}
`[]`
   {% /dd %}

   {% dt %}
`curl -X POST 'BASE_DOMAIN:8080/notes?desc=hello'`
   {% /dt %}

   {% dd %}
`{"id":1,"description":"hello"}`
   {% /dd %}

   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes?id=1'`
   {% /dt %}

   {% dd %}
`{"id":1,"description":"hello"}`
   {% /dd %}

   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes'`
   {% /dt %}

   {% dd %}
`[{"id":1,"description":"hello"}]`
   {% /dd %}

   {% dt %}
`curl -X PUT 'BASE_DOMAIN:8080/notes?id=1&desc=UpdatedNote'`
   {% /dt %}

   {% dd %}
`{"id":1,"description":"UpdatedNote"}`
   {% /dd %}

   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes'`
   {% /dt %}

   {% dd %}
`[{"id":1,"description":"UpdatedNote"}]`
   {% /dd %}

   {% dt %}
`curl -X POST 'BASE_DOMAIN:8080/notes?desc=NewestNote&add_date=y'`
   {% /dt %}

   {% dd %}
   `{"id":2,"description":"NewestNote with date 12/02/2022."}`
This command calls both the `notes` and `calendar` services.
   {% /dd %}

      {% /dl %}

1. After you've seen the application running, run the following command to stop it and clean up the AWS resources so that you can enable tracing:

   ```sh
   terraform destroy
```

## Enable tracing{% #enable-tracing %}

Now that you have a working Java application, configure it to enable tracing.

1. Edit the dockerfile to add the Java tracing package which is needed by the application to generate traces. Open the `notes/dockerfile.notes.maven` file and uncomment the line that downloads `dd-java-agent`:

   ```
   RUN curl -Lo dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'
   ```

1. Within the same `notes/dockerfile.notes.maven` file, comment out the `ENTRYPOINT` line for running without tracing. Then uncomment the `ENTRYPOINT` line, which runs the application with tracing enabled:

   ```
   ENTRYPOINT ["java" , "-javaagent:../dd-java-agent.jar", "-Ddd.trace.sample.rate=1", "-jar" , "target/notes-0.0.1-SNAPSHOT.jar"]
   ```

Repeat this step with the other service, `calendar`. Open `calendar/dockerfile.calendar.maven`, and comment out the `ENTRYPOINT` line for running without tracing. Then uncomment the `ENTRYPOINT` line, which runs the application with tracing enabled:

   ```
   ENTRYPOINT ["java", "-javaagent:../dd-java-agent.jar", "-Ddd.trace.sample.rate=1", "-jar" , "target/calendar-0.0.1-SNAPSHOT.jar"]
   ```

Now both services will have automatic instrumentation.
Important alert (level: warning): The flags on these sample commands, particularly the sample rate, are not necessarily appropriate for environments outside this tutorial. For information about what to use in your real environment, read Tracing configuration.
1. Automatic instrumentation is convenient, but sometimes you want more fine-grained spans. Datadog's Java DD Trace API allows you to specify spans within your code using annotations or code. Add some annotations to the code to trace into some sample methods.

Open `/notes/src/main/java/com/datadog/example/notes/NotesHelper.java`. This example already contains commented-out code that demonstrates the different ways to set up custom tracing on the code.

1. Uncomment the lines that import libraries to support manual tracing:

   ```java
   import datadog.trace.api.Trace;
   import datadog.trace.api.DDTags;
   import io.opentracing.Scope;
   import io.opentracing.Span;
   import io.opentracing.Tracer;
   import io.opentracing.tag.Tags;
   import io.opentracing.util.GlobalTracer;
   import java.io.PrintWriter;
   import java.io.StringWriter
   ```

1. Uncomment the lines that manually trace the two public processes. These demonstrate the use of `@Trace` annotations to specify aspects such as `operationName` and `resourceName` in a trace:

   ```java
   @Trace(operationName = "traceMethod1", resourceName = "NotesHelper.doLongRunningProcess")
   // ...
   @Trace(operationName = "traceMethod2", resourceName = "NotesHelper.anotherProcess")
   ```

1. You can also create a separate span for a specific code block in the application. Within the span, add service and resource name tags and error handling tags. These tags result in a flame graph showing the span and metrics in Datadog visualizations. Uncomment the lines that manually trace the private method:

   ```java
           Tracer tracer = GlobalTracer.get();
           // Tags can be set when creating the span
           Span span = tracer.buildSpan("manualSpan1")
               .withTag(DDTags.SERVICE_NAME, "NotesHelper")
               .withTag(DDTags.RESOURCE_NAME, "privateMethod1")
               .start();
           try (Scope scope = tracer.activateSpan(span)) {
               // Tags can also be set after creation
               span.setTag("postCreationTag", 1);
               Thread.sleep(30);
               Log.info("Hello from the custom privateMethod1");
   ```

And also the lines that set tags on errors:

   ```java
        } catch (Exception e) {
            // Set error on span
            span.setTag(Tags.ERROR, true);
            span.setTag(DDTags.ERROR_MSG, e.getMessage());
            span.setTag(DDTags.ERROR_TYPE, e.getClass().getName());
   
            final StringWriter errorString = new StringWriter();
            e.printStackTrace(new PrintWriter(errorString));
            span.setTag(DDTags.ERROR_STACK, errorString.toString());
            Log.info(errorString.toString());
        } finally {
            span.finish();
        }
   ```

1. Update your Maven build by opening `notes/pom.xml` and uncommenting the lines configuring dependencies for manual tracing. The `dd-trace-api` library is used for the `@Trace` annotations, and `opentracing-util` and `opentracing-api` are used for manual span creation.

1. Add the Datadog Agent to each of the `notes` and `calendar` task definitions, adding an Agent in a container beside each AWS task rather than installing it anywhere. Open `terraform/Fargate/Instrumented/main.tf` and see that this sample already has the base configurations necessary to run the Datadog Agent on ECS Fargate and collect traces: the API key (which you configure in the next step), enabling ECS Fargate, and enabling APM. The definition is provided in both the `notes` task and the `calendar` task.

1. Provide the API key variable with a value. Open `terraform/Fargate/global_constants/variables.tf` and uncomment the `output "datadog_api_key"` section and provide your organization's Datadog API key.

1. [Universal Service Tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) identify traced services across different versions and deployment environments so that they can be correlated within Datadog, and so you can use them to search and filter. The three environment variables used for Unified Service Tagging are `DD_SERVICE`, `DD_ENV`, and `DD_VERSION`. For applications deployed on ECS, these environment variables are set within the task definition for the containers.

For this tutorial, the `/terraform/Fargate/Instrumented/main.tf` file already has these environment variables defined for the notes and calendar applications, for example, for `notes`:

   ```yaml
   ...
   
      name : "notes",
      image : "${module.settings.aws_ecr_repository}:notes",
      essential : true,
      portMappings : [
        {
          containerPort : 8080,
          hostPort : 8080
        }
      ],
      memory : 512,
      cpu : 256,
      environment : [
        {
          name : "CALENDAR_HOST",
          value : "calendar.apmlocaljava"
        },
        {
          name : "DD_SERVICE",
          value : "notes"
        },
        {
          name : "DD_ENV",
          value : "dev"
        },
        {
          name : "DD_VERSION",
          value : "0.0.1"
        }
      ],
      dockerLabels : {
        "com.datadoghq.tags.service" : "notes",
        "com.datadoghq.tags.env" : "dev",
        "com.datadoghq.tags.version" : "0.0.1"
      },
      ...
   ```

And for `calendar`:

   ```yaml
    ...
       name : "calendar",
       image : "${module.settings.aws_ecr_repository}:calendar",
       essential : true,
       environment : [
         {
           name : "DD_SERVICE",
           value : "calendar"
         },
         {
           name : "DD_ENV",
           value : "dev"
         },
         {
           name : "DD_VERSION",
           value : "0.0.1"
         }
      ],
      dockerLabels : {
        "com.datadoghq.tags.service" : "calendar",
        "com.datadoghq.tags.env" : "dev",
        "com.datadoghq.tags.version" : "0.0.1"
      },
     ...
   ```

You can also see that Docker labels for the same Universal Service Tags `service`, `env`, and `version` values are set. This allows you also to get Docker metrics once your application is running.

### Tracing configuration{% #tracing-configuration %}

The Java tracing library uses Java's built-in agent and monitoring support. The flag `-javaagent:../dd-java-agent.jar` in the Dockerfile tells the JVM where to find the Java tracing library so it can run as a Java Agent. Learn more about Java Agents at [https://www.baeldung.com/java-instrumentation](https://www.baeldung.com/java-instrumentation).

The `dd.trace.sample.rate` flag sets the sample rate for this application. The ENTRYPOINT command in the Dockerfile sets its value to `1`, meaning that 100% of all service requests are sent to the Datadog backend for analysis and display. For a low-volume test application, this is fine. Do not do this in production or in any high-volume environment, because this results in a very large volume of data. Instead, sample some of your requests. Pick a value between 0 and 1. For example, `-Ddd.trace.sample.rate=0.1` sends traces for 10% of your requests to Datadog. Read more about [tracing configuration settings](https://docs.datadoghq.com/tracing/trace_collection/library_config/java/) and [sampling mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/?tab=java).

Notice that the sampling rate flag in the commands appears *before* the `-jar` flag. That's because this is a parameter for the Java Virtual Machine, not your application. Make sure that when you add the Java Agent to your application, you specify the flag in the right location.

### Rebuild and upload the application image{% #rebuild-and-upload-the-application-image %}

Rebuild the image with tracing enabled using the same steps as before:

```sh
aws ecr get-login-password --region us-east-1 | docker login --username <YOUR_AWS_USER> --password-stdin <USER_CREDENTIALS>
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f service-docker-compose-ECS.yaml build
docker tag docker_notes:latest <ECR_REGISTRY_URL>:notes
docker tag docker_calendar:latest <ECR_REGISTRY_URL>:calendar
docker push <ECR_REGISTRY_URL>:notes
docker push <ECR_REGISTRY_URL>:calendar
```



Your multi-service application with tracing enabled is containerized and available for ECS to pull.

## Launch the app to see traces{% #launch-the-app-to-see-traces %}

Redeploy the application and exercise the API:

1. Redeploy the application to Amazon ECS using the same terraform commands as before, but with the instrumented version of the configuration files. From the `terraform/Fargate/Instrumented` directory, run the following commands:

   ```sh
   terraform init
   terraform apply
   terraform state show 'aws_alb.application_load_balancer'
   ```

1. Make note of the DNS name of the load balancer. You'll use that base domain in API calls to the sample app.

1. Wait a few minutes for the instances to start up. Wait a few minutes to ensure the containers for the applications are ready. Run some curl commands to exercise the instrumented app:

   {% dl %}
   
   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes'`
   {% /dt %}

   {% dd %}
`[]`
   {% /dd %}

   {% dt %}
`curl -X POST 'BASE_DOMAIN:8080/notes?desc=hello'`
   {% /dt %}

   {% dd %}
`{"id":1,"description":"hello"}`
   {% /dd %}

   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes?id=1'`
   {% /dt %}

   {% dd %}
`{"id":1,"description":"hello"}`
   {% /dd %}

   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes'`
   {% /dt %}

   {% dd %}
`[{"id":1,"description":"hello"}]`
   {% /dd %}

   {% dt %}
`curl -X PUT 'BASE_DOMAIN:8080/notes?id=1&desc=UpdatedNote'`
   {% /dt %}

   {% dd %}
`{"id":1,"description":"UpdatedNote"}`
   {% /dd %}

   {% dt %}
`curl -X GET 'BASE_DOMAIN:8080/notes'`
   {% /dt %}

   {% dd %}
`[{"id":1,"description":"hello"}]`
   {% /dd %}

   {% dt %}
`curl -X POST 'BASE_DOMAIN:8080/notes?desc=NewestNote&add_date=y'`
   {% /dt %}

   {% dd %}
`{"id":2,"description":"NewestNote with date 12/02/2022."}`
   {% /dd %}

   {% dd %}
   This command calls both the `notes` and `calendar` services.
      {% /dd %}

      {% /dl %}

1. Wait a few moments, and go to [**APM > Traces**](https://app.datadoghq.com/apm/traces) in Datadog, where you can see a list of traces corresponding to your API calls:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-traces2.598507141baa139ec3a2f5fc5b0157b0.png?auto=format"
      alt="Traces from the sample app in APM Trace Explorer" /%}

The `h2` is the embedded in-memory database for this tutorial, and `notes` is the Spring Boot application. The traces list shows all the spans, when they started, what resource was tracked with the span, and how long it took.

If you don't see traces after several minutes, clear any filter in the Traces Search field (sometimes it filters on an environment variable such as `ENV` that you aren't using).

### Examine a trace{% #examine-a-trace %}

On the Traces page, click on a `POST /notes` trace to see a flame graph that shows how long each span took and what other spans occurred before a span completed. The bar at the top of the graph is the span you selected on the previous screen (in this case, the initial entry point into the notes application).

The width of a bar indicates how long it took to complete. A bar at a lower depth represents a span that completes during the lifetime of a bar at a higher depth.

On the Trace Explorer, click into one of the `GET` requests, and see a flame graph like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-custom-flame.3faa56c8907d0876ffdf0f8ff95cf532.png?auto=format"
   alt="A flame graph for a GET trace with custom instrumentation." /%}

The `privateMethod` around which you created a manual span shows up as a separate block from the other calls and is highlighted by a different color. The other methods where you used the `@Trace` annotation show under the same service and color as the `GET` request, which is the `notes` application. Custom instrumentation is valuable when there are key parts of the code that need to be highlighted and monitored.

For more information, read [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/).

Tracing a single service is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*. Click the trace for the last API call, the one that added a date to the note, to see a distributed trace between the two services:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-java-container-distributed.b52699b2e5afbb870e36d38586a62d3a.png?auto=format"
   alt="A flame graph for a distributed trace." /%}

Note that you didn't change anything in the `notes` application. Datadog automatically instruments both the `okHttp` library used to make the HTTP call from `notes` to `calendar`, and the Jetty library used to listen for HTTP requests in `notes` and `calendar`. This allows the trace information to be passed from one application to the other, capturing a distributed trace.

When you're done exploring, clean up all resources and delete the deployments:

```sh
aws ecs delete-service --cluster apm-tutorial-ec2-java --service datadog-agent --profile <PROFILE> --region <REGION>
terraform destroy
```

## Troubleshooting{% #troubleshooting %}

If you're not receiving traces as expected, set up debug mode for the Java tracer. Read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/#enable-debug-mode) to find out more.

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/java/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/)
- [Supported Java frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-java)
