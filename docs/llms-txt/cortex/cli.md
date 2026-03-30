# Source: https://docs.cortexlabs.com/clients/cli.md

# Source: https://docs.cortexlabs.com/0.41/clients/cli.md

# Source: https://docs.cortexlabs.com/0.40/clients/cli.md

# Source: https://docs.cortexlabs.com/0.39/clients/cli.md

# Source: https://docs.cortexlabs.com/0.38/clients/cli.md

# Source: https://docs.cortexlabs.com/0.37/clients/cli.md

# Source: https://docs.cortexlabs.com/0.36/clients/cli.md

# Source: https://docs.cortexlabs.com/0.35/clients/cli.md

# Source: https://docs.cortexlabs.com/0.34/clients/cli.md

# Source: https://docs.cortexlabs.com/0.33/clients/cli.md

# Source: https://docs.cortexlabs.com/0.32/clients/cli.md

# Source: https://docs.cortexlabs.com/0.31/clients/cli.md

# Source: https://docs.cortexlabs.com/0.30/clients/cli.md

# Source: https://docs.cortexlabs.com/0.29/clients/cli.md

# Source: https://docs.cortexlabs.com/0.28/clients/cli.md

# CLI commands

## deploy

```
create or update apis

Usage:
  cortex deploy [CONFIG_FILE] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -y, --yes             skip prompts
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for deploy
```

## get

```
get information about apis or jobs

Usage:
  cortex get [API_NAME] [JOB_ID] [flags]

Flags:
  -e, --env string      environment to use
  -w, --watch           re-run the command every 2 seconds
  -o, --output string   output format: one of pretty|json (default "pretty")
  -v, --verbose         show additional information (only applies to pretty output format)
  -h, --help            help for get
```

## logs

```
stream logs from a single replica of an api or a single worker for a job

Usage:
  cortex logs API_NAME [JOB_ID] [flags]

Flags:
  -e, --env string   environment to use
  -y, --yes          skip prompts
  -h, --help         help for logs
```

## patch

```
update API configuration for a deployed API

Usage:
  cortex patch [CONFIG_FILE] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for patch
```

## refresh

```
restart all replicas for an api (without downtime)

Usage:
  cortex refresh API_NAME [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for refresh
```

## delete

```
delete any kind of api or stop a batch job

Usage:
  cortex delete API_NAME [JOB_ID] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           delete the api without confirmation
  -c, --keep-cache      keep cached data for the api
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for delete
```

## cluster up

```
spin up a cluster on aws

Usage:
  cortex cluster up [flags]

Flags:
  -c, --config string               path to a cluster configuration file
      --aws-key string              aws access key id
      --aws-secret string           aws secret access key
      --cluster-aws-key string      aws access key id to be used by the cluster
      --cluster-aws-secret string   aws secret access key to be used by the cluster
  -e, --configure-env string        name of environment to configure (default "aws")
  -y, --yes                         skip prompts
  -h, --help                        help for up
```

## cluster info

```
get information about a cluster

Usage:
  cortex cluster info [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -n, --name string            name of the cluster
  -r, --region string          aws region of the cluster
      --aws-key string         aws access key id
      --aws-secret string      aws secret access key
  -e, --configure-env string   name of environment to configure
  -d, --debug                  save the current cluster state to a file
  -y, --yes                    skip prompts
  -h, --help                   help for info
```

## cluster configure

```
update a cluster's configuration

Usage:
  cortex cluster configure [flags]

Flags:
  -c, --config string               path to a cluster configuration file
      --aws-key string              aws access key id
      --aws-secret string           aws secret access key
      --cluster-aws-key string      aws access key id to be used by the cluster
      --cluster-aws-secret string   aws secret access key to be used by the cluster
  -e, --configure-env string        name of environment to configure
  -y, --yes                         skip prompts
  -h, --help                        help for configure
```

## cluster down

```
spin down a cluster

Usage:
  cortex cluster down [flags]

Flags:
  -c, --config string       path to a cluster configuration file
  -n, --name string         name of the cluster
  -r, --region string       aws region of the cluster
      --aws-key string      aws access key id
      --aws-secret string   aws secret access key
  -y, --yes                 skip prompts
  -h, --help                help for down
```

## cluster export

```
download the code and configuration for APIs

Usage:
  cortex cluster export [API_NAME] [API_ID] [flags]

Flags:
  -c, --config string       path to a cluster configuration file
  -n, --name string         name of the cluster
  -r, --region string       aws region of the cluster
      --aws-key string      aws access key id
      --aws-secret string   aws secret access key
  -h, --help                help for export
```

## cluster-gcp up

```
spin up a cluster on gcp

Usage:
  cortex cluster-gcp up [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -e, --configure-env string   name of environment to configure (default "gcp")
  -y, --yes                    skip prompts
  -h, --help                   help for up
```

## cluster-gcp info

```
get information about a cluster

Usage:
  cortex cluster-gcp info [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -n, --name string            name of the cluster
  -p, --project string         gcp project id
  -z, --zone string            gcp zone of the cluster
  -e, --configure-env string   name of environment to configure
  -d, --debug                  save the current cluster state to a file
  -y, --yes                    skip prompts
  -h, --help                   help for info
```

## cluster-gcp down

```
spin down a cluster

Usage:
  cortex cluster-gcp down [flags]

Flags:
  -c, --config string    path to a cluster configuration file
  -n, --name string      name of the cluster
  -p, --project string   gcp project id
  -z, --zone string      gcp zone of the cluster
  -y, --yes              skip prompts
  -h, --help             help for down
```

## env configure

```
configure an environment

Usage:
  cortex env configure [ENVIRONMENT_NAME] [flags]

Flags:
  -o, --operator-endpoint string   set the operator endpoint without prompting
  -h, --help                       help for configure
```

## env list

```
list all configured environments

Usage:
  cortex env list [flags]

Flags:
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for list
```

## env default

```
set the default environment

Usage:
  cortex env default [ENVIRONMENT_NAME] [flags]

Flags:
  -h, --help   help for default
```

## env delete

```
delete an environment configuration

Usage:
  cortex env delete [ENVIRONMENT_NAME] [flags]

Flags:
  -h, --help   help for delete
```

## version

```
print the cli and cluster versions

Usage:
  cortex version [flags]

Flags:
  -e, --env string   environment to use
  -h, --help         help for version
```

## completion

```
generate shell completion scripts

to enable cortex shell completion:
    bash:
        add this to ~/.bash_profile (mac) or ~/.bashrc (linux):
            source <(cortex completion bash)

        note: bash-completion must be installed on your system; example installation instructions:
            mac:
                1) install bash completion:
                   brew install bash-completion
                2) add this to your ~/.bash_profile:
                   source $(brew --prefix)/etc/bash_completion
                3) log out and back in, or close your terminal window and reopen it
            ubuntu:
                1) install bash completion:
                   apt update && apt install -y bash-completion  # you may need sudo
                2) open ~/.bashrc and uncomment the bash completion section, or add this:
                   if [ -f /etc/bash_completion ] && ! shopt -oq posix; then . /etc/bash_completion; fi
                3) log out and back in, or close your terminal window and reopen it

    zsh:
        option 1:
            add this to ~/.zshrc:
                source <(cortex completion zsh)
            if that failed, you can try adding this line (above the source command you just added):
                autoload -Uz compinit && compinit
        option 2:
            create a _cortex file in your fpath, for example:
                cortex completion zsh > /usr/local/share/zsh/site-functions/_cortex

Note: this will also add the "cx" alias for cortex for convenience

Usage:
  cortex completion SHELL [flags]

Flags:
  -h, --help   help for completion
```
