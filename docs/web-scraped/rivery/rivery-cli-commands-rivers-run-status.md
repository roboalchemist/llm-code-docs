# Source: https://riveryio.github.io/rivery_cli/commands/rivers/run-status/

Title: rivers run status - Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/commands/rivers/run-status/

Markdown Content:
rivers run status - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/#run-status)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 rivers run status 

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
    *   [rivery](https://riveryio.github.io/rivery_cli/commands/rivery/)
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
            *   - [x]  rivers run status  [rivers run status](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/) Table of contents  
                *   [Usage](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/#usage)
                *   [Options](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/#options)
                *   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/#cli-help)

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
*   [Usage](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/#usage)
*   [Options](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/#options)
*   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/#cli-help)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/commands/rivers/run-status.md "Edit this page")
run status
==========

Check the run status by runId

Usage
-----

1```
Usage: rivery rivers run status [OPTIONS]
```

Options
-------

*   `runid` (REQUIRED): 
*   Type: STRING 
*   Default: `none`
*   Usage: `--runId`

The run id to check the status on.

*   `timeout`: 
*   Type: INT 
*   Default: `none`
*   Usage: `--timeout`

The number of seconds to wait for the run to complete until giving up.

 Eligible only on hitting --waitForEnd option

*   `waitforend`: 
*   Type: STRING 
*   Default: `false`
*   Usage: `--waitForEnd`

*   `help`:

*   Type: BOOL 
*   Default: `false`
*   Usage: `--help`

Show this message and exit.

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
11```
Usage: rivery rivers run status [OPTIONS]

  Check the run status by runId

Options:
  --runId TEXT       The run id to check the status on.  [required]
  --timeout INTEGER  The number of seconds to wait for the run to complete until
                     giving up.   Eligible only on hitting --waitForEnd option

  --waitForEnd
  --help             Show this message and exit.
```

[Previous rivers run fire](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/)[Next rivery activities](https://riveryio.github.io/rivery_cli/commands/activities/rivery-activities/)
