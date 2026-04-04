# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/tcp-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TCP Endpoints

<img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/15715dc-tcp-endpoints.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8407205ce22c7fb0282cb866f7f4955d" alt="Image" data-og-width="1280" width="1280" data-og-height="720" height="720" data-path="images/15715dc-tcp-endpoints.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/15715dc-tcp-endpoints.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=d620696943f5519117ac8b19d637aa75 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/15715dc-tcp-endpoints.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=d7636d2d24b7e638df577435dc1e75ff 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/15715dc-tcp-endpoints.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=efe62411da4b0f1bcd6837665a344a58 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/15715dc-tcp-endpoints.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8dab5aca85ce60c7db6641ea1fe67480 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/15715dc-tcp-endpoints.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=523a7b066761dad276ba7bfd5da95e9f 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/15715dc-tcp-endpoints.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=5faac17ee276512e0bdbe57b1acc3c26 2500w" />

TCP Endpoints can be created using the [`aptible endpoints:tcp:create`](/reference/aptible-cli/cli-commands/cli-endpoints-tcp-create) command.

# Traffic

TCP Endpoints pass the TCP traffic they receive directly to your app.

# Container Ports

When creating a TCP Endpoint, you can specify the container ports the Endpoint should listen on. If you don't specify a port, Aptible will use all the ports exposed by your [Image](/core-concepts/apps/deploying-apps/image/overview).

The TCP Endpoint will listen for traffic on the ports you expose and transfer that traffic to your app [Containers](/core-concepts/architecture/containers/overview) on the same port.

For example, if you expose ports `123` and `456`, the Endpoint will listen on those two ports. Traffic received by the Endpoint on port `123` will be sent to your app containers on port `123`, and traffic received by the Endpoint on port `456` will be sent to your app containers on port `456`.

You may expose at most 10 ports. Note that this means that if your image exposes more than 10 ports, you will need to specify which ones should be exposed to provision TCP Endpoints.

# FAQ

<AccordionGroup>
  <Accordion title="Do TCP Endpoints support SSL?">
    If you need a higher level of control over TLS negotiation, we would suggest using a TCP Endpoint so that you can perform TLS termination in your application containers with the level of control that you need.
  </Accordion>

  <Accordion title="Are TCP Endpoints safe without SSL?">
    Some resources (postgresql for example, in unison with [pgbouncer](https://www.pgbouncer.org/)) have TLS built into their protocols, which means utilizing a TCP endpoint would be necessary, appropriate, and safe. Reviewing and aligning with protocols associated with your application requirements can provide insight on whether TCP endpoints are applicable.
  </Accordion>
</AccordionGroup>

> ❗️ Unlike [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview), TCP Endpoints currently do not provide [Zero-Downtime Deployment](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview#zero-downtime-deployment). If you require Zero-Downtime Deployment for a TCP app, you'd need to architect it yourself, e.g. at the DNS level.
