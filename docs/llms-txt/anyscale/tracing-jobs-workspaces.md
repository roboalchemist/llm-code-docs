# Source: https://docs.anyscale.com/monitoring/tracing-jobs-workspaces.md

# Tutorial: Export traces from Anyscale jobs and workspaces

[View Markdown](/monitoring/tracing-jobs-workspaces.md)

# Tutorial: Export traces from Anyscale jobs and workspaces

This tutorial provides an example of configuring an Anyscale job or workspace to export OpenTelemetry traces to an external observability platform.

note

This feature is experimental, reach out to Anyscale with feedback or any issues.

In this tutorial, you complete the following steps:

1. Create a Python package with a tracing exporter that integrates with Ray's startup hooks to automatically instrument your jobs.
2. Build a container image that includes your environment variables and tracing exporter Python package.
3. Run an Anyscale job with your image and manually validate your configuration.

## Requirements[​](#requirements "Direct link to Requirements")

Complete the steps of this tutorial using a running Anyscale workspace. See [Tutorial: Create a workspace](/get-started/create-workspace.md).

This tutorial assumes you use Honeycomb and have access to the API credentials for your Honeycomb account.

note

This example uses Honeycomb. You can adapt it to any OpenTelemetry-compatible backend, such as Jaeger, Datadog, or New Relic.

Use the `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_EXPORTER_OTLP_HEADERS` environment variables to configure credentials for your integration.

## Step 1: Create the custom tracing package[​](#package "Direct link to Step 1: Create the custom tracing package")

Create a Python package that handles trace export configuration.

1. Use the VS Code terminal in an Anyscale workspace to create a new Python module, a `pyproject.toml` file, and `__init__.py` file in the workspace directory:

   ```
   mkdir -p ~/$ANYSCALE_PROJECT/honeycomb_tracing_module/honeycomb_tracing;
   touch ~/$ANYSCALE_PROJECT/honeycomb_tracing_module/pyproject.toml;
   touch ~/$ANYSCALE_PROJECT/honeycomb_tracing_module/honeycomb_tracing/__init__.py
   ```

2. Copy the following code into the `__init__.py` file:

   ```
   import os
   from opentelemetry import trace
   from opentelemetry.sdk.trace import TracerProvider
   from opentelemetry.sdk.trace.export import SimpleSpanProcessor
   from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
   from opentelemetry.sdk.resources import Resource

   __version__ = "0.1.0"
   __all__ = ["setup_honeycomb_tracing"]

   def setup_honeycomb_tracing() -> None:
       """Initialize OpenTelemetry trace export to configured backend.
       
       Ray calls this function during worker startup when ANYSCALE_TRACING_EXPORTER_PATH
       environment variable points to this function.
       """
       endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
       headers_str = os.getenv("OTEL_EXPORTER_OTLP_HEADERS")
       
       if not endpoint or not headers_str:
           print(f"OTEL environment variables not set, skipping tracing (PID: {os.getpid()})")
           return

       # Only configure if not already set up
       if not isinstance(trace.get_tracer_provider(), TracerProvider):
           # Configure service metadata
           resource = Resource.create({
               "service.name": "ray-job", 
               "service.version": "1.0.0",
           })
           
           # Set up tracer provider
           trace.set_tracer_provider(TracerProvider(resource=resource))
           
           # Parse headers from comma-separated key=value pairs
           headers = dict(header.split("=", 1) for header in headers_str.split(","))
           
           # Configure OTLP exporter
           exporter = OTLPSpanExporter(endpoint=endpoint, headers=headers)
           processor = SimpleSpanProcessor(exporter)
           
           trace.get_tracer_provider().add_span_processor(processor)
           trace.get_tracer_provider().force_flush(timeout_millis=5000)
           
           print(f"✅ Tracing configured for worker (PID: {os.getpid()})")
   ```

3. Copy the following code into the `pyproject.toml` file:

   ```
   [build-system]
   requires      = ["setuptools>=69", "wheel"]
   build-backend = "setuptools.build_meta"

   [project]
   name            = "honeycomb_tracing"
   version         = "0.1.0"
   requires-python = ">=3.8"

   dependencies = [
     "opentelemetry-api>=1.15.0",
     "opentelemetry-sdk>=1.15.0",
     "opentelemetry-exporter-otlp-proto-http>=1.15.0",
   ]

   [tool.setuptools.packages.find]
   include = ["honeycomb_tracing"]
   ```

## Step 2: Define and build a custom container image[​](#build-image "Direct link to Step 2: Define and build a custom container image")

Define a containerfile and build a custom image for your workspace.

note

This example uses an Anyscale feature to [edit containerfiles](/dependency-management/containerfiles.md) for workspaces. You can also [build a custom container image](/container-image/build-image.md) and use this in your jobs or workspaces.

1. In the Anyscale console for your workspace, click the **Dependencies** tab.

2. Click **Build custom image**.

3. Add the following code to install your package and configure your API credentials:

   ```
   # Copy the tracing module from the workspace to container. 
   COPY --chown=ray:ray working_dir/honeycomb_tracing_module /home/ray/default/honeycomb_tracing_module

   # Install the Python package.
   RUN cd /home/ray/default/honeycomb_tracing_module && pip install .

   # Define environment variables for Honeycomb.
   # The path to the custom function in your Python tracing module.
   ENV ANYSCALE_TRACING_EXPORTER_PATH=honeycomb_tracing:setup_honeycomb_tracing 
   # The OLTP endpoint for Honeycomb.
   ENV OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io/v1/traces 
   # The Honeycomb API key.
   ENV OTEL_EXPORTER_OTLP_HEADERS=x-honeycomb-team=<your-honeycomb-api-key> 
   ```

   note

   This example uses the path `/home/ray/default/honeycomb_tracing_module`. If your Anyscale project name is something other than `default`, update this path.

   This example is for Honeycomb. You must replace the `<your-honeycomb-api-key>` variable with your API key.

4. Click **Build image**.

5. Click **Build and apply**. Logs display progress as the image builds and the cluster restarts.

## Step 4: Validate the setup[​](#validate "Direct link to Step 4: Validate the setup")

Create and run a test job to verify tracing works.

1. Create a file named `main.py` in your home directory and add the following code:

   ```
   import ray
   from opentelemetry import trace

   # Get a tracer for creating custom spans
   tracer = trace.get_tracer(__name__)

   @ray.remote
   def outer_task():
       return ray.get(inner_task.remote())

   @ray.remote
   def inner_task():
       # Create a custom span with attributes
       with tracer.start_as_current_span("custom_operation") as span:
           span.set_attribute("operation.type", "example")
           span.set_attribute("worker.id", ray.get_runtime_context().get_worker_id())
           return 42

   def main():
       ray.init()
       result = ray.get(outer_task.remote())
       print(f"Result: {result}")

   if __name__ == "__main__":
       main()
   ```

2. Run the following code in the VS Code terminal to submit an Anyscale job:

   ```
   anyscale job submit -- python main.py
   ```

3. If successful, the following result should display:

   ```
   ✅ Tracing configured for worker (PID: 12345)
   Result: 42
   ```

   note

   If you get an authentication error, make sure you've correctly configured an API key that has write permissions.

4. Navigate to your Honeycomb account and login. The following traces appear:

   * **Ray task spans**: Automatic traces for each `@ray.remote` function call.
   * **Custom spans**: Your manually created spans with attributes.
   * **Performance data**: Task duration, worker information, and resource usage.
   * **Distributed traces**: Complete request flows across multiple Ray workers.

   note

   If no traces appear, verify that you've set your environment variables correctly.
