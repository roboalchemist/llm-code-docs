# Source: https://riveryio.github.io/rivery_cli/commands/rivery/

Title: Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/commands/rivery/

Markdown Content:
rivery - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/commands/rivery/#rivery)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 rivery 

 Initializing search 

[RiveryIo/rivery_cli](https://github.com/RiveryIo/rivery_cli/ "Go to repository")

*   [Home](https://riveryio.github.io/rivery_cli/)
*   [Getting Started](https://riveryio.github.io/rivery_cli/getting-started/)
*   [Reference](https://riveryio.github.io/rivery_cli/reference/authentication/)
*   [Commands](https://riveryio.github.io/rivery_cli/commands/rivery/)
*   [Resources](https://riveryio.github.io/rivery_cli/resources/glossary/)

[![Image 2: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)") Rivery Command Line Tool (CLI)  

[RiveryIo/rivery_cli](https://github.com/RiveryIo/rivery_cli/ "Go to repository")

*   [Home](https://riveryio.github.io/rivery_cli/)
*   [Getting Started](https://riveryio.github.io/rivery_cli/getting-started/)
*   - [x]  Reference   Reference  
    *   [Authentication](https://riveryio.github.io/rivery_cli/reference/authentication/)
    *   [Basics](https://riveryio.github.io/rivery_cli/reference/best-practice/)
    *   [Project](https://riveryio.github.io/rivery_cli/reference/project/)
    *   - [x]  Models   Models  
        *   [Basic Reference](https://riveryio.github.io/rivery_cli/reference/reference/)
        *   - [x]  River   River  
            *   [Yaml Reference](https://riveryio.github.io/rivery_cli/reference/rivers/river/)
            *   - [x]  Properties   Properties  
                *   [Logic](https://riveryio.github.io/rivery_cli/reference/rivers/logic/logic/)

*   - [x]  Commands   Commands  
    *   - [x]  rivery  [rivery](https://riveryio.github.io/rivery_cli/commands/rivery/) Table of contents  
        *   [Usage](https://riveryio.github.io/rivery_cli/commands/rivery/#usage)
        *   [Options](https://riveryio.github.io/rivery_cli/commands/rivery/#options)
        *   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivery/#cli-help)

    *   [init](https://riveryio.github.io/rivery_cli/commands/rivery-init/)
    *   [configure](https://riveryio.github.io/rivery_cli/commands/rivery-configure/)
    *   - [x]  profiles   profiles  
        *   [profiles](https://riveryio.github.io/rivery_cli/commands/profiles/profiles/)
        *   [profiles get](https://riveryio.github.io/rivery_cli/commands/profiles/profiles-get/)

    *   - [x]  rivers   rivers  
        *   [rivery rivers](https://riveryio.github.io/rivery_cli/commands/rivers/rivery-rivers/)
        *   [rivers import](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/)
        *   [rivers push](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-push/)
        *   - [x]  rivers run   rivers run  
            *   [rivers run](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-run/)
            *   [rivers run fire](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/)
            *   [rivers run status](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/)

    *   - [x]  activities   activities  
        *   [rivery activities](https://riveryio.github.io/rivery_cli/commands/activities/rivery-activities/)
        *   - [x]  activities logs   activities logs  
            *   [activities logs](https://riveryio.github.io/rivery_cli/commands/activities/activities-logs/)
            *   [activities logs fetch](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/)

*   - [x]  Resources   Resources  
    *   [Glossary](https://riveryio.github.io/rivery_cli/resources/glossary/)
    *   [FAQ](https://riveryio.github.io/rivery_cli/resources/faq/)
    *   [Link and Examples](https://riveryio.github.io/rivery_cli/resources/extras/)

 Table of contents  
*   [Usage](https://riveryio.github.io/rivery_cli/commands/rivery/#usage)
*   [Options](https://riveryio.github.io/rivery_cli/commands/rivery/#options)
*   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivery/#cli-help)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/commands/rivery.md "Edit this page")
rivery
======

Rivery CLI

Usage
-----

1```
Usage: rivery [OPTIONS] COMMAND [ARGS]...
```

Options
-------

*   `region`: 
*   Type: Choice('['us-east-2', 'eu-west-1']') 
*   Default: `us-east-2`
*   Usage: `--region`

The region of the profile to connect

*   `host`: 
*   Type: STRING 
*   Default: `https://console.rivery.io`
*   Usage: `--host`

Connect to specific Rivery host (for example: https://eu-west-1.console.rivery.io)

*   `debug`: 
*   Type: BOOL 
*   Default: `false`
*   Usage: `--debug`

Show debug log

*   `ignoreerros`: 
*   Type: BOOL 
*   Default: `false`
*   Usage: `--ignoreErros`

Ignore errors during run.

*   `help`: 
*   Type: BOOL 
*   Default: `false`
*   Usage: `--help`

Show this message and exit.

*   `version`:
*   type: BOOL
*   default: `false'
*   usage `--version`

CLI Help
--------

1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20```
Usage: rivery [OPTIONS] COMMAND [ARGS]...

  Rivery CLI

Options:
  --region [us-east-2|eu-west-1]  The region of the profile to connect
                                  [default: us-east-2]

  --host TEXT                     Connect to specific Rivery host (for example:
                                  https://eu-west-1.console.rivery.io)

  --debug                         Show debug log
  --ignoreErros                   Ignore errors during run.
  --help                          Show this message and exit.
  --version                      Get the current version.

Commands:
  configure  Configure new profile and the authentication.
  init       Make a initiation project.yaml in the current path
  rivers     Rivers operations (push, pull/import)
```

[Previous Logic](https://riveryio.github.io/rivery_cli/reference/rivers/logic/logic/)[Next init](https://riveryio.github.io/rivery_cli/commands/rivery-init/)
