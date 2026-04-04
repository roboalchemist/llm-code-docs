# Source: https://uptrace.dev/raw/guides/opentelemetry-nginx.md

# OpenTelemetry NGINX Instrumentation

> Instrument NGINX with OpenTelemetry using ngx_otel_module. Auto-trace HTTP requests, propagate context, configure sampling, and export to OTLP collectors with 10-15% overhead.

OpenTelemetry NGINX instrumentation provides [distributed tracing](/opentelemetry/distributed-tracing) support for [NGINX](https://nginx.org/) and NGINX Plus through the `ngx_otel_module` dynamic module. With this integration, NGINX can automatically trace HTTP requests, propagate trace context to upstream services, and export telemetry data to OpenTelemetry collectors with minimal performance overhead (10-15% compared to 50%+ for alternative solutions).

## What is NGINX?

NGINX is a high-performance web server, reverse proxy, load balancer, and HTTP cache. Originally created to solve the C10K problem (handling 10,000 concurrent connections), NGINX uses an asynchronous, event-driven architecture that enables it to handle hundreds of thousands of concurrent connections with low resource consumption.

NGINX serves as a critical component in modern infrastructure:

- **Reverse Proxy**: Routes client requests to backend application servers
- **Load Balancer**: Distributes traffic across multiple servers
- **API Gateway**: Manages and secures API traffic
- **Static Content Server**: Efficiently serves static files
- **SSL/TLS Termination**: Handles encryption/decryption at the edge

## What is OpenTelemetry?

[OpenTelemetry](/opentelemetry) is an open-source observability framework that aims to standardize and simplify the collection, processing, and export of telemetry data from applications and systems.

OpenTelemetry supports multiple programming languages and platforms, making it suitable for a wide range of applications and environments.

OpenTelemetry enables developers to instrument their code and collect telemetry data, which can then be exported to various [OpenTelemetry backends](/blog/opentelemetry-backend) or observability platforms for analysis and visualization.

## Installation

The OpenTelemetry module is available for both NGINX Open Source and NGINX Plus as a dynamic module.

### NGINX Open Source

For NGINX Open Source, build the module from source or use pre-built packages:

**From Package Repository (Ubuntu/Debian):**

```bash
# Add NGINX repository
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null

echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

# Install NGINX and OpenTelemetry module
sudo apt update
sudo apt install nginx nginx-module-otel
```

**From Source:**

```bash
# Clone the repository
git clone https://github.com/nginxinc/nginx-otel.git
cd nginx-otel

# Build as dynamic module
./configure --with-compat --add-dynamic-module=nginx-otel
make modules

# Copy module to NGINX modules directory
sudo cp objs/ngx_otel_module.so /etc/nginx/modules/
```

### NGINX Plus

For NGINX Plus subscribers, install the pre-built module:

```bash
sudo apt install nginx-plus-module-otel
```

### Verify Installation

Confirm the module is available:

```bash
nginx -V 2>&1 | grep otel
```

## Configuration

### Loading the Module

Add the module to your main NGINX configuration (`nginx.conf`):

```nginx
load_module modules/ngx_otel_module.so;

events {}

http {
    # OpenTelemetry configuration goes here
}
```

### Basic Configuration

Configure the exporter and enable tracing:

```nginx
load_module modules/ngx_otel_module.so;

http {
    # Configure OTel exporter
    otel_exporter {
        endpoint localhost:4317;
    }

    # Set service name
    otel_service_name "nginx-gateway";

    server {
        listen 80;
        server_name example.com;

        location / {
            # Enable tracing for this location
            otel_trace on;

            # Inject trace context into upstream requests
            otel_trace_context propagate;

            proxy_pass http://backend;
        }
    }
}
```

### Exporter Configuration

The `otel_exporter` directive configures OTLP/gRPC export parameters:

```nginx
http {
    otel_exporter {
        # OTLP endpoint
        endpoint https://api.uptrace.dev:4317;

        # Custom headers for authentication
        header uptrace-dsn "your-dsn-here";

        # TLS configuration
        trusted_certificate /etc/nginx/ssl/ca-bundle.crt;

        # Export interval (default: 5s)
        interval 5s;

        # Batch size (default: 512 spans)
        batch_size 512;

        # Pending batches per worker (default: 4)
        batch_count 4;
    }
}
```

### Trace Context Propagation

Control how NGINX handles W3C trace context headers:

```nginx
server {
    location /api {
        otel_trace on;

        # extract - Use existing trace context from request
        # inject - Add new context, overwriting existing headers
        # propagate - Update existing context (extract + inject)
        # ignore - Skip header processing
        otel_trace_context propagate;

        proxy_pass http://backend;
    }
}
```

<table>
<thead>
  <tr>
    <th>
      Mode
    </th>
    
    <th>
      Behavior
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        extract
      </code>
    </td>
    
    <td>
      Uses trace context from incoming request headers
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        inject
      </code>
    </td>
    
    <td>
      Creates new trace context, overwrites existing
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        propagate
      </code>
    </td>
    
    <td>
      Combines extract and inject (recommended)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ignore
      </code>
    </td>
    
    <td>
      No trace context processing
    </td>
  </tr>
</tbody>
</table>

### Custom Span Names and Attributes

Customize span names and add attributes:

```nginx
server {
    location /checkout {
        otel_trace on;

        # Custom span name
        otel_span_name "checkout_request";

        # Add custom attributes
        otel_span_attr "http.endpoint" "/checkout";
        otel_span_attr "user.region" "$geoip_country_code";
        otel_span_attr "cache.status" "$upstream_cache_status";

        proxy_pass http://checkout-service;
    }
}
```

## Advanced Patterns

### Dynamic Trace Sampling

Implement percentage-based sampling using NGINX variables:

```nginx
http {
    otel_exporter {
        endpoint localhost:4317;
    }

    # Sample 10% of traces
    split_clients "$otel_trace_id" $trace_sampler {
        10%    on;
        *      off;
    }

    server {
        location / {
            # Dynamic sampling based on variable
            otel_trace $trace_sampler;
            otel_trace_context propagate;

            proxy_pass http://backend;
        }
    }
}
```

### Conditional Tracing

Enable tracing based on request properties:

```nginx
http {
    # Trace only requests with specific header
    map $http_x_debug_trace $enable_tracing {
        default  off;
        "true"   on;
        "1"      on;
    }

    server {
        location / {
            otel_trace $enable_tracing;
            otel_trace_context propagate;

            proxy_pass http://backend;
        }
    }
}
```

### Multi-Environment Configuration

Configure different exporters per environment:

```nginx
http {
    # Production exporter
    otel_exporter {
        endpoint https://prod-otel-collector:4317;
        header authorization "Bearer ${PROD_TOKEN}";
        trusted_certificate /etc/nginx/ssl/prod-ca.crt;
    }

    otel_service_name "nginx-prod";

    server {
        listen 443 ssl;
        server_name api.example.com;

        location / {
            otel_trace on;
            otel_trace_context propagate;

            # Add environment tag
            otel_span_attr "deployment.environment" "production";

            proxy_pass http://backend;
        }
    }
}
```

## Embedded Variables

Access trace identifiers in NGINX configuration:

```nginx
server {
    location / {
        otel_trace on;

        # Add trace ID to response headers
        add_header X-Trace-ID $otel_trace_id;

        # Log trace information
        access_log /var/log/nginx/access.log combined;
        log_format trace '$remote_addr - $otel_trace_id [$time_local] '
                        '"$request" $status $body_bytes_sent';

        proxy_pass http://backend;

        # Pass trace ID to upstream
        proxy_set_header X-Trace-ID $otel_trace_id;
        proxy_set_header X-Span-ID $otel_span_id;
    }
}
```

Available variables:

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        $otel_trace_id
      </code>
    </td>
    
    <td>
      Current trace identifier
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        $otel_span_id
      </code>
    </td>
    
    <td>
      Current span identifier
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        $otel_parent_id
      </code>
    </td>
    
    <td>
      Parent span identifier
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        $otel_parent_sampled
      </code>
    </td>
    
    <td>
      Parent sampling decision (0 or 1)
    </td>
  </tr>
</tbody>
</table>

## NGINX Ingress Controller

For Kubernetes environments, enable OpenTelemetry in the NGINX Ingress Controller:

### Installation

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-configuration
  namespace: ingress-nginx
data:
  enable-opentelemetry: "true"
  otlp-collector-host: "otel-collector.observability.svc.cluster.local"
  otlp-collector-port: "4317"
  otel-service-name: "nginx-ingress"
  otel-sampler: "AlwaysOn"
  otel-sampler-ratio: "1.0"
```

### Helm Installation

```bash
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --create-namespace \
  --set controller.config.enable-opentelemetry=true \
  --set controller.config.otlp-collector-host=otel-collector.observability.svc \
  --set controller.config.otlp-collector-port=4317 \
  --set controller.config.otel-service-name=nginx-ingress
```

### Per-Ingress Configuration

Configure tracing for specific Ingress resources:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/enable-opentelemetry: "true"
    nginx.ingress.kubernetes.io/opentelemetry-operation-name: "api-gateway"
    nginx.ingress.kubernetes.io/opentelemetry-trust-incoming-span: "true"
spec:
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: backend-service
            port:
              number: 8080
```

## Docker Configuration

### Dockerfile

```dockerfile
FROM nginx:1.25

# Install OpenTelemetry module
RUN apt-get update && \
    apt-get install -y nginx-module-otel && \
    rm -rf /var/lib/apt/lists/*

# Copy custom configuration
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  nginx:
    build: .
    ports:
      - "80:80"
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
    depends_on:
      - otel-collector
      - backend

  backend:
    image: your-backend-app:latest
    expose:
      - "8080"

  otel-collector:
    image: otel/opentelemetry-collector:latest
    command: ["--config=/etc/otel-collector-config.yaml"]
    volumes:
      - ./otel-collector-config.yaml:/etc/otel-collector-config.yaml
    ports:
      - "4317:4317"
      - "4318:4318"
```

## Performance Considerations

The `ngx_otel_module` is optimized for production use with minimal overhead:

- **Request latency overhead**: 10-15% (vs 50%+ for other solutions)
- **Memory overhead**: ~2MB per worker process
- **CPU overhead**: Negligible for typical workloads

### Optimization Tips

1. **Use appropriate sampling**: Not all traffic needs tracing```nginx
split_clients "$otel_trace_id" $sampler {
    1%     on;  # Sample 1% in high-traffic scenarios
    *      off;
}
```
2. **Adjust batch size**: Larger batches reduce export frequency```nginx
otel_exporter {
    endpoint localhost:4317;
    batch_size 1024;  # Increase from default 512
    interval 10s;     # Increase from default 5s
}
```
3. **Selective location tracing**: Only trace critical paths```nginx
location /api {
    otel_trace on;  # Trace API calls
    proxy_pass http://api-backend;
}

location /static {
    # No tracing for static content
    root /var/www/static;
}
```

## What is Uptrace?

Uptrace is a [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## FAQ

**Does OpenTelemetry work with NGINX Open Source and NGINX Plus?** Yes, the `ngx_otel_module` supports both NGINX Open Source and NGINX Plus. The module is available as a pre-built package for NGINX Open Source and comes bundled with NGINX Plus subscriptions. Both versions provide the same OpenTelemetry capabilities including distributed tracing, context propagation, and OTLP export.

**What's the performance impact of the NGINX OpenTelemetry module?** The official `ngx_otel_module` introduces only 10-15% overhead compared to 50%+ for third-party solutions. This minimal impact is achieved through kernel-level optimizations and efficient eBPF-free implementation. For high-traffic scenarios, use sampling to reduce overhead further while maintaining observability coverage.

**Can I use OpenTelemetry with NGINX Ingress Controller on Kubernetes?** Yes, the NGINX Ingress Controller supports OpenTelemetry through ConfigMap settings or Helm values. Enable it cluster-wide or per-Ingress using annotations. The controller automatically instruments all HTTP/HTTPS traffic passing through the ingress, making it ideal for Kubernetes service mesh observability without sidecar proxies.

**How does NGINX propagate trace context to upstream services?** NGINX uses the `otel_trace_context` directive with W3C Trace Context standard. Set it to `propagate` mode to automatically inject `traceparent` and `tracestate` headers into upstream requests. This enables distributed tracing across your entire service architecture, even if upstream services use different instrumentation libraries.

**Does the OpenTelemetry module support encrypted HTTPS traffic?** Yes, the module captures traces for both HTTP and HTTPS traffic transparently. TLS/SSL termination at NGINX doesn't affect tracing - spans are created after decryption, so you get full visibility into request processing regardless of encryption. TLS configuration for the OTLP exporter is supported via the `trusted_certificate` directive.

**Can I selectively trace specific routes or disable tracing for static content?** Yes, use NGINX's location blocks to control tracing granularly. Enable `otel_trace on` for API endpoints while leaving it off for static content like `/static/` or `/assets/`. You can also use NGINX variables and the `map` directive to implement complex conditional tracing based on request headers, paths, or other criteria.

## What's next?

NGINX is now instrumented with OpenTelemetry, providing distributed tracing and trace context propagation. For complete end-to-end observability, instrument your backend applications with guides like [Django](/guides/opentelemetry-django), [Flask](/guides/opentelemetry-flask), [FastAPI](/guides/opentelemetry-fastapi), or [OpenTelemetry Go](/get/opentelemetry-go) for Go-based services.
