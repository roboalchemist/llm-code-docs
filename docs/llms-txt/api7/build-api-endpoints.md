# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/api-implementation/build-api-endpoints.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/api-implementation/build-api-endpoints.md

# Build API Endpoints

An API endpoint provides the actual business logic and data for your API. You need to develop and deploy APIs before integrating them with API7 Enterprise.

## Develop API Endpoints[â](#develop-api-endpoints "Direct link to Develop API Endpoints")

This section lists the workflow to develop an API endpoint.

1. **Scheduling:** Scheduling is a key aspect of the API development process. People in your team should complete and report their work based on the scheduled timeline to ensure delivering the project in a timely manner.
2. **Development and Self-Testing:** Typically, development involves coding and debugging, while self-testing involves testing and validating developed APIs to ensure their functionality.
3. **Integration Testing:** Integration testing is a stage where APIs between different modules are debugged and tested to ensure correct and stable interactions and communications.
4. **QA Testing:** QA testing (or quality assurance testing) aims to identify and eliminate defects or vulnerabilities in an API before it is released. It is critical for API reliability and security.
5. **Product Acceptance:** Product acceptance involves comprehensive testing, evaluation, and confirmation to determine whether an API meets the expected goals and standards. This stage is vital for ensuring that the API is ready for production and meets your requirements.
6. **Deployment:** Once the API has passed all necessary tests and evaluations, it will be deployed to the production environment. Then, you can access and utilize the API.

## Deploy API Backend[â](#deploy-api-backend "Direct link to Deploy API Backend")

When deploying an API backend, you should consider API scalability, availability, portability, and so on.

* **Virtual Machines**: Deploy service binaries/packages on VMs directly.
* **Containers**: Package services as Docker containers and deploy on orchestrators like Kubernetes.
* **Serverless**: Develop functions and deploy on platforms like AWS Lambda.
* **On-premise**: Host services on existing on-premise infrastructure.

## Define API Endpoints[â](#define-api-endpoints "Direct link to Define API Endpoints")

Once deployed, the API backend must be configured with network endpoints that the API7 Enterprise can route requests to.

* **Virtual Machines**: Assign public IP addresses and open ports on VM firewalls for service endpoints.
* **Containers**: Use Kubernetes Ingress or LoadBalancer services to expose endpoints.
* **Serverless**: Most serverless platforms automatically assign invocation URLs for functions.
* **Serverless**: Most serverless platforms automatically assign invocation URLs for functions.

### Detect API Backends[â](#detect-api-backends "Direct link to Detect API Backends")

You can use either of the following ways to detect API backends:

* **Implement Health Checks (Highly Recommended)**

  Configure health check endpoints for backend services to allow API7 Enterprise to detect availability and route traffic accordingly.

* **Use Service Discovery (Optional)**

  Service discovery mechanisms, such as Consul, Eureka, Nacos or Kubernetes Service Discovery, can be used to dynamically detect backend nodes.
