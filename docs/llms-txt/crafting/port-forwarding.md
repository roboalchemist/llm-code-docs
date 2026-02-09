# Port-forwarding for hybrid development

Source: https://docs.sandboxes.cloud/docs/port-forwarding.md

In this page, we describe how to use Crafting's port-forwarding feature for hybrid development, which combines the power of cloud with the familiarity of the development environments on local machine.

<Image align="center" width="60% " src="https://files.readme.io/1f16189-concepts-hybrid-dev.png" />

When a developer wants to make code change in a service, e.g. `Service B`, ideally it's best to be able to run it with its upstream and downstream services, e.g. `Service A`, and `Service C`, so that the code change can be tested in an end-to-end product flow. However, due to setup complexity or lack of local resources, running the entire product on local machine is infeasible, making development and testing difficult.

Crafting allows the developer to only run the target service, i.e., `Service B` on the local machine, but it would be virtually plugged in the sandbox, having an end-to-end context for testing. It achieves this by **two-way port-forwarding**.

```shell
$ cs portforward
```

With a single command `cs portforward`, Crafting connects your local machine with a sandbox that runs on the cloud with multiple services end-to-end, and use the service running on your local machine to "replace" the selected service. In the example above, the `Service B` is selected as target, then all the incoming traffic to the ports defined for `Service B` on the sandbox will be forward to the local machine, hitting the `Local Service B` that runs there. At the same time, traffic hitting the local ports from `Local Service B` are forwarded to corresponding services running in the sandbox on cloud, e.g. `Service A` and `Service C`. That way, an end-to-end product flow, hitting `Service A`, `Service B`, and `Service C` in this sequence, will actually hit `Service A`(on cloud), `Local Service B`, and `Service C` (on cloud), allowing the developer to test the `Local Service B` easily.

Key advantages of using Crafting port forwarding

* Developers have near-zero workflow change from their local machine dev experience, same machine, same IDE, same local tools, same workflow.
  * The IDE doesn't need to have remote development capability.
  * The developer still manages local code branch and commit code from local.
* Heavy dependencies and services are off-load to cloud and no longer consumes local resources.

## Integration testing example

Here we use an example on integration testing to illustrate port-forwarding. The demo video can be found [here](https://youtu.be/AodElect3Ks?t=225). In this example, we are using the demo app we talked about before, and we are going to replace the API service, by the local version.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/642bbf9-image.png" />

Just simply run the `cs portforward` and select the sandbox (`pr-21`) and workspace (`api`), the Crafting CLI established forwarding as follows:

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/4ee893c-use-case-preview-portforward.JPG" />

For the locally running API service, it forwards the 3001 port from the cloud workspace to the localhost 3001, so that the locally running API service just needs to listen to the localhost 3001 to get all the requests forwarded to it. For the outgoing traffic from the local API service, it forwards the local ports 2181, 3306, 8087, and 9092 to the corresponding services running on the Crafting sandbox on cloud, so that the local API service can call database as well as other services on cloud.

Then we launch the local API service in RubyMine IDE, which runs the source code locally with our local code change we want to test. We can also add a breakpoint in the IDE just like when we need to debug the local service.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/f344e35-use-case-preview-local-breakpoint.JPG" />

Then we hit the endpoint for the sandbox online, to test the flow end-to-end, which triggers a request to the API service.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/03b34f5-image.png" />

However, this time, with the **port forwarding** turned on, instead of hitting the version running on the cloud sandbox, it hits the locally running API service, triggering the breakpoint.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/287fda3-use-case-preview-local-IDE.JPG" />

Here we can inspect the value and continue the execution, then the locally running API service will fetch data from the cloud mysql and return to the frontend.

### Setup notes

#### Define ports and port-forwarding

First, as `cs portforward` is a local machine-based command, you need to have the Crafting CLI downloaded on to your local machine. The command `cs port-forward` will reply on the `Sandbox Definition` and local additional flags to decide which incoming and outgoing forwarding to be established. In each workspace,

* `ports` are used to define incoming traffic, which are for incoming forwarding.
* `port_forward_rules` are used to define outgoing traffic, which are for outgoing forwarding.

For example, with the following `Sandbox Definition`:

```yaml
workspaces:
- name: frontend
  ports:
  - name: http
    port: 3000
    protocol: HTTP/TCP
  port_forward_rules:
  - local: '8080'
    remote:
      target: backend
      port: api
  - local: '6379'
    remote:
      target: cache
      port: redis
- name: backend
  ports:
  - name: api
    port: 8080
    protocol: HTTP/TCP
dependencies:
- name: cache
  service_type: redis
```

Running the command `cs port-forward` targeting `frontend` workspace will establish 1 incoming forward and 2 outgoing forward:

```text
$ cs port-forward -W demo/frontend

TYPE    FROM           TO             STATE #CONN DETAILS
Reverse 3000           localhost:3000 OK                 
Forward localhost:8080 backend:8080   OK                 
Forward localhost:6379 redis:6379     OK
```

#### Make sure config in source code points to the local target

In a Crafting sandbox, there are two ways for a service (e.g., service `api`) to talk to another one (e.g., service `backend`):

* The direct way is to let the config in `api` directly address to the host name `backend`, just like in docker-compose or Kubernetes namespace. e.g., `http://backend:8080` is hitting the `backend` service's port 8080.
* The port forwarding way is set up port forwarding rule on `api` service, to point its local port (e.g. 8080) to `backend` service's port 8080. With that setup, the `api` service can address `http://localhost:8080` to hit `backend` service's port 8080. After setting up the port forwarding, the direct way to address hostname of `backend` would continue to work.

For hybrid development, since local machine is not part of the sandbox's overlay network, the port-forwarding setup is necessary for the local service to have outbound network connections to services running on cloud. It is because the `cs portforward` command will use that configuration to establish forwarding rules between local machine and sandbox on cloud. In this use case, we recommend also using the port forwarding way for services in the sandbox to talk to each other so that the config can be kept same no matter the service process is running on local machine or in cloud sandbox.

#### Make sure the local ports are available for outbound forwarding

One error that is often encountered is the port conflict when starting the port forwarding. For example, a developer may have their local redis running and listening to port 6379 on the localhost for the local machine. Then when starting a port forwarding session, the attempt to setup forwarding from the same local port 6379 to cloud will fail because the port is already taken by local redis.

In this case, we recommend to turn off the local service to free the port. Alternatively, you can skip the outbound forwarding by adding the option `-F, --skip-forward-rules` to the `cs portforward` command.
