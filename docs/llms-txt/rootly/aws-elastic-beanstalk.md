# Source: https://docs.rootly.com/integrations/aws-elastic-beanstalk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS Elastic Beanstalk

> Deploy Rootly configurations to AWS Elastic Beanstalk environments using .ebextensions configuration files.

## Installation

* Create a `.ebextensions/rootly.config` file. (The name does not have to be 'rootly'.)
* Put this content into the file (Adapt for your use case)

```Shell Shell theme={null}
files:
"/opt/elasticbeanstalk/hooks/appdeploy/pre/01rootly.sh" :
    mode: "000775"
    owner: root
    group: users
    content: |
        #!/bin/bash

        rootly_api_key="$(/opt/elasticbeanstalk/bin/get-config container -k rootly_api_key)";
        environment="$(/opt/elasticbeanstalk/bin/get-config container -k environment)";
        service="$(/opt/elasticbeanstalk/bin/get-config container -k service)";
        labels="key=value,key2=value2"

        # install rootly cli
        curl -fsSL https://raw.githubusercontent.com/rootly-io/cli/main/install.sh | sh

        # log a pulse
        rootly pulse --api-key "${rootly_api_key}" --quiet --environments "${environment}" --services "${service}" --labels "${labels}" Deploy in progress...
```


Built with [Mintlify](https://mintlify.com).