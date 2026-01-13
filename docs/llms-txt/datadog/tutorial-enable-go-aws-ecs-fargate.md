# Source: https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-aws-ecs-fargate.md

---
title: Tutorial - Enabling Tracing for a Go Application on Amazon ECS with Fargate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Tutorial - Enabling Tracing for a Go Application
  on Amazon ECS with Fargate
source_url: https://docs.datadoghq.com/guide/tutorial-enable-go-aws-ecs-fargate/index.html
---

# Tutorial - Enabling Tracing for a Go Application on Amazon ECS with Fargate

## Overview{% #overview %}

This tutorial walks you through the steps for enabling tracing on a sample Go application installed in a cluster on AWS Elastic Container Service (ECS) with Fargate. In this scenario, the Datadog Agent is also installed in the cluster.

For other scenarios, including the application and Agent on a host, the application in a container and Agent on a host, the application and Agent on cloud infrastructure, and on applications written in other languages, see the other [Enabling Tracing tutorials](https://docs.datadoghq.com/tracing/guide/#enabling-tracing-tutorials). Some of those other tutorials, for example, the ones using containers or EKS, step through the differences seen in Datadog between automatic and custom instrumentation. This tutorial skips right to a fully custom instrumented example.

This tutorial also uses intermediate-level AWS topics, so it requires that you have some familiarity with AWS networking and applications. If you're not as familiar with AWS, and you are trying to learn the basics of Datadog APM setup, use one of the host or container tutorials instead.

See [Tracing Go Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go/) for general comprehensive tracing setup documentation for Go. **Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

### Prerequisites{% #prerequisites %}

- A Datadog account and [organization API key](https://docs.datadoghq.com/account_management/api-app-keys/)
- Git
- Docker
- Terraform
- Amazon ECS
- an Amazon ECR repository for hosting images
- An AWS IAM user with `AdministratorAccess` permission. You must add the profile to your local credentials file using the access and secret access keys. For more information, read [Configuring the AWS SDK for Go V2](https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/#specifying-credentials).

## Install the sample Go application{% #install-the-sample-go-application %}

Next, install a sample application to trace. The code sample for this tutorial can be found at [github.com/DataDog/apm-tutorial-golang.git](https://github.com/DataDog/apm-tutorial-golang). Clone the git repository by running:

```shell
git clone https://github.com/DataDog/apm-tutorial-golang.git
```

The repository contains a multi-service Go application pre-configured to run inside Docker containers. The `docker-compose` YAML files to make the containers are located in the `docker` directory. This tutorial uses the `service-docker-compose-ECS.yaml` file, which builds containers for the `notes` and `calendar` service that make up the sample application.

In addition, this tutorial uses several configuration files in the `terraform/Fargate` directory to create the environment to deploy the sample application to ECS with Fargate.

### Initial ECS setup{% #initial-ecs-setup %}

The application requires some initial configuration, including adding your AWS profile (already configured with the correct permissions to create an ECS cluster and read from ECR), AWS region, and Amazon ECR repository.

Open `terraform/Fargate/global_constants/variables.tf`. Replace the variable values below with your correct AWS account information:

```tf
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

Leave the `datadog_api_key` section commented for now. You'll set up Datadog later in the tutorial.

### Build and upload the application images{% #build-and-upload-the-application-images %}

If you're not familiar with Amazon ECR, a registry for container images, it might be helpful to read [Using Amazon ECR with the AWS CLI](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html).

In the sample project's `/docker` directory, run the following commands:

1. Authenticate with ECR by supplying your username and password in this command:

   ```shell
   aws ecr get-login-password --region us-east-1 | docker login --username <YOUR_AWS_USER> --password-stdin <USER_CREDENTIALS>
```



1. Build a Docker image for the sample apps, adjusting the platform setting to match yours:

   ```shell
   DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f service-docker-compose-ECS.yaml build
```



1. Tag the containers with the ECR destination:

   ```shell
   docker tag docker_notes:latest <ECR_REGISTRY_URL>:notes
   docker tag docker_calendar:latest <ECR_REGISTRY_URL>:calendar
```



1. Upload the container to the ECR registry:

   ```shell
   docker push <ECR_REGISTRY_URL>:notes
   docker push <ECR_REGISTRY_URL>:calendar
```

Your application (without tracing enabled) is containerized and available for ECS to pull.

### Deploy the application{% #deploy-the-application %}

Start the application and send some requests without tracing. After you've seen how the application works, you'll instrument it using the tracing library and Datadog Agent.

To start, use a Terraform script to deploy to Amazon ECS:

1. From the `terraform/Fargate/deployment` directory, run the following commands:

   ```shell
   terraform init
   terraform apply
   terraform state show 'aws_alb.application_load_balancer'
   ```

**Note**: If the `terraform apply` command returns a CIDR block message, the script to obtain your IP address did not work on your local machine. To fix this, set the value manually in the `terraform/Fargate/deployment/security.tf` file. Inside the `ingress` block of the `load_balancer_security_group`, switch which `cidr_blocks` line is commented out and update the now-uncommented example line with your machine's IP4 address.

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
`curl -X PUT 'BASE_DOMAIN:8080/notes/1?desc=UpdatedNote'`
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

   ```shell
   terraform destroy
```

## Enable tracing{% #enable-tracing %}

Next, configure the Go application to enable tracing.

To enable tracing support:

1. Uncomment the following imports in `apm-tutorial-golang/cmd/notes/main.go`:

In the `cmd/notes/main.go` file:

   ```go
        sqltrace "github.com/DataDog/dd-trace-go/contrib/database/sql/v2"
        chitrace "github.com/DataDog/dd-trace-go/contrib/go-chi/chi/v2"
        httptrace "github.com/DataDog/dd-trace-go/contrib/net/http/v2"
        "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
      
```

1. In the `main()` function, uncomment the following lines:

In the `cmd/notes/main.go` file:

   ```go
      tracer.Start()
      defer tracer.Stop()
```

In the `cmd/notes/main.go` file:

   ```go
      client = httptrace.WrapClient(client, httptrace.RTWithResourceNamer(func(req *http.Request) string {
         return fmt.Sprintf("%s %s", req.Method, req.URL.Path)
      }))
```

In the `cmd/notes/main.go` file:

   ```go
      r.Use(chitrace.Middleware(chitrace.WithService("notes")))
```

1. In `setupDB()`, uncomment the following lines:

In the `cmd/notes/main.go` file:

   ```go
      sqltrace.Register("sqlite3", &sqlite3.SQLiteDriver{}, sqltrace.WithService("db"))
      db, err := sqltrace.Open("sqlite3", "file::memory:?cache=shared")
```



In the `cmd/notes/main.go` file:

   ```go
      db, err := sql.Open("sqlite3", "file::memory:?cache=shared")
```

1. The steps above enabled automatic tracing with fully supported libraries. In cases where code doesn't fall under a supported library, you can create spans manually.

Open `notes/notesController.go`. This example already contains commented-out code that demonstrates the different ways to set up custom tracing on the code.

1. The `makeSpanMiddleware` function in `notes/notesController.go` generates middleware that wraps a request in a span with the supplied name. Uncomment the following lines:

In the `notes/notesController.go` file:

   ```go
      r.Get("/notes", nr.GetAllNotes)                // GET /notes
      r.Post("/notes", nr.CreateNote)                // POST /notes
      r.Get("/notes/{noteID}", nr.GetNoteByID)       // GET /notes/123
      r.Put("/notes/{noteID}", nr.UpdateNoteByID)    // PUT /notes/123
      r.Delete("/notes/{noteID}", nr.DeleteNoteByID) // DELETE /notes/123
```

In the `notes/notesController.go` file:

   ```go
      r.Get("/notes", makeSpanMiddleware("GetAllNotes", nr.GetAllNotes))               // GET /notes
      r.Post("/notes", makeSpanMiddleware("CreateNote", nr.CreateNote))                // POST /notes
      r.Get("/notes/{noteID}", makeSpanMiddleware("GetNote", nr.GetNoteByID))          // GET /notes/123
      r.Put("/notes/{noteID}", makeSpanMiddleware("UpdateNote", nr.UpdateNoteByID))    // PUT /notes/123
      r.Delete("/notes/{noteID}", makeSpanMiddleware("DeleteNote", nr.DeleteNoteByID)) // DELETE /notes/123
```

Also remove the comment around the following import:

In the `notes/notesController.go` file:

   ```go
       "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
      
```

1. The `doLongRunningProcess` function creates child spans from a parent context. Remove the comments to enable it:

In the `notes/notesHelper.go` file:

   ```go
      func doLongRunningProcess(ctx context.Context) {
       childSpan, ctx := tracer.StartSpanFromContext(ctx, "traceMethod1")
       childSpan.SetTag(ext.ResourceName, "NotesHelper.doLongRunningProcess")
       defer childSpan.Finish()
   
       time.Sleep(300 * time.Millisecond)
       log.Println("Hello from the long running process in Notes")
       privateMethod1(ctx)
     }
```



1. The `privateMethod1` function demonstrates creating a completely separate service from a context. Remove the comments to enable it:

In the `notes/notesHelper.go` file:

   ```go
   func privateMethod1(ctx context.Context) {
      childSpan, _ := tracer.StartSpanFromContext(ctx, "manualSpan1",
         tracer.SpanType("web"),
         tracer.ServiceName("noteshelper"),
      )
      childSpan.SetTag(ext.ResourceName, "privateMethod1")
      defer childSpan.Finish()
   
      time.Sleep(30 * time.Millisecond)
      log.Println("Hello from the custom privateMethod1 in Notes")
   }
```

For more information on custom tracing, see [Go Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/).

1. Open `terraform/Fargate/deployment/main.tf`. The sample app already has the base configurations necessary to run the Datadog Agent on ECS Fargate and collect traces: the API key (which you configure in the next step), enabling ECS Fargate, and enabling APM. The definition is provided in both the `notes` task and the `calendar` task.

1. Provide the API key variable with a value. Open `terraform/Fargate/global_constants/variables.tf`, uncomment the `output "datadog_api_key"` section, and provide your organization's Datadog API key.

1. [Universal Service Tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) identify traced services across different versions and deployment environments so that they can be correlated within Datadog, and so you can use them to search and filter. The three environment variables used for Unified Service Tagging are `DD_SERVICE`, `DD_ENV`, and `DD_VERSION`. For applications deployed on ECS, these environment variables are set within the task definition for the containers.

For this tutorial, the `/terraform/Fargate/deployment/main.tf` file already has these environment variables defined for the notes and calendar applications. For example, for `notes`:

   ```yaml
   {
    ...
   
      name : "notes-task",
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
          value : "calendar.apmlocalgo"
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
    },
   
    ...
   ```

And for `calendar`:

   ```yaml
   ...
   
      name : "calendar-task",
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

### Rebuild and upload the application image{% #rebuild-and-upload-the-application-image %}

Rebuild the image with tracing enabled using the same steps as before:

```shell
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

1. Redeploy the application to Amazon ECS using the same terraform commands as before, but with the instrumented version of the configuration files. From the `terraform/Fargate/deployment` directory, run the following commands:

   ```shell
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
`curl -X PUT 'BASE_DOMAIN:8080/notes/1?desc=UpdatedNote'`
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

1. Wait a few moments, and take a look at your Datadog UI. Navigate to [**APM > Traces**](https://app.datadoghq.com/apm/traces). The Traces list shows something like this:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-traces2.a4c96e77ce9bab870c5aca8b6586fdf0.png?auto=format"
      alt="Traces view shows trace data coming in from host." /%}



There are entries for the database (`db`) and the `notes` app. The traces list shows all the spans, when they started, what resource was tracked with the span, and how long it took.

If you don't see traces, clear any filter in the **Traces** Search field (sometimes it filters on an environment variable such as `ENV` that you aren't using).

### Examine a trace{% #examine-a-trace %}

On the Traces page, click on a `POST /notes` trace, to see a flame graph that shows how long each span took and what other spans occurred before a span completed. The bar at the top of the graph is the span you selected on the previous screen (in this case, the initial entry point into the notes application).

The width of a bar indicates how long it took to complete. A bar at a lower depth represents a span that completes during the lifetime of a bar at a higher depth.

The flame graph for a `POST` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-post-flame.15c3bd9a147f4bd3225aeea40068792f.png?auto=format"
   alt="A flame graph for a POST trace." /%}

A `GET /notes` trace looks something like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-get-flame.ef3917fad9625764ca7790a4b2c57084.png?auto=format"
   alt="A flame graph for a GET trace." /%}

For more information, read [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/).

Tracing a single application is a great start, but the real value in tracing is seeing how requests flow through your services. This is called *distributed tracing*. Click the trace for the last API call, the one that added a date to the note, to see a distributed trace between the two services:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/tutorials/tutorial-go-host-distributed.e2788e7116cc2a1554b5b714407b536a.png?auto=format"
   alt="A flame graph for a distributed trace." /%}

This flame graph combines interactions from multiple applications:

- The first span is a POST request sent by the user and handled by the `chi` router through the supported `go-chi` library.
- The second span is a `createNote` function that was manually traced by the `makeSpanMiddleware` function. The function created a span from the context of the HTTP request.
- The next span is the request sent by the notes application using the supported `http` library and the client initialized in the `main.go` file. This GET request is sent to the calendar application. The calendar application spans appear in blue because they are separate service.
- Inside the calendar application, a `go-chi` router handles the GET request and the `GetDate` function is manually traced with its own span under the GET request.
- Finally, the purple `db` call is its own service from the supported `sql` library. It appears at the same level as the `GET /Calendar` request because they are both called by the parent span `CreateNote`.

When you're done exploring, clean up all resources and delete the deployments:

```shell
terraform destroy
```

## Troubleshooting{% #troubleshooting %}

If you're not receiving traces as expected, set up debug mode for the Go tracer. Read [Enable debug mode](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/?code-lang=go) to find out more.

## Further reading{% #further-reading %}

- [Additional tracing library configuration options](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/)
- [Detailed tracing library setup instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go/)
- [Supported Go frameworks for automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/go/)
- [Manually configuring traces and spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/)
- [Ingestion mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/)
- [Tracing library open source code repository](https://github.com/DataDog/dd-trace-Go)
