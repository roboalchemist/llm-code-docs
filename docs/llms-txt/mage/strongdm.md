# Source: https://docs.mage.ai/integrations/strongdm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# StrongDM

![StrongDM](https://www.strongdm.com/docs/images/logos/strongdm.svg)

## Setup Docker environment

To effectively connect on a StrongDM Resource inside Mage's docker, you may need to add:

<br />

If using docker run command:

<br />

`--add-host=host.docker.internal:host-gateway`

<br />

If using docker-compose setup:

<br />

```yaml  theme={"system"}
services:
    server:
        .....
        extra_hosts:
            - "host.docker.internal:host-gateway"
```

## Install StrongDM CLI tool

To install StrongDM CLI tool, first access Mage's docker bash and execute the installation script:

```bash  theme={"system"}
./scripts/strongdm/install.sh
```

(In case you receive a "Permission denied" error, executing `chmod u+x scripts/strongdm/install.sh` should fix this issue)

Now, login in your StrongDM account using:

```bash  theme={"system"}
sdm login
```

And connect to the desired Resources using:

```bash  theme={"system"}
sdm connect RESOURCE-NAME
```

## Accessing StrongDM Resources

Now, to connect to a Resource, simply add the required host parameter as "localhost" and the respective port number

MongoDB Source example:

```yaml  theme={"system"}
database: admin
host: localhost
password: example
port: 10006 # Specified in StrongDM Resource Generation
user: root
```


Built with [Mintlify](https://mintlify.com).