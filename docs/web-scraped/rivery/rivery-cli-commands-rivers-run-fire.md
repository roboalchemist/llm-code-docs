# Source: https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/

Title: rivers run fire - Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/

Markdown Content:
rivers run fire - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/#run-fire)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 rivers run fire 

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
            *   - [x]  rivers run fire  [rivers run fire](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/) Table of contents  
                *   [Usage](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/#usage)
                *   [Options](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/#options)
                *   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/#cli-help)

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
*   [Usage](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/#usage)
*   [Options](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/#options)
*   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivers/run-fire/#cli-help)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/commands/rivers/run-fire.md "Edit this page")
run fire
========

Run a river whitin the current profile (account+environment). Gets a riverid key, with the river id to run and just run it in the platform.

Usage
-----

1```
Usage: rivery rivers run fire [OPTIONS]
```

Options
-------

*   `riverid` (REQUIRED): 
*   Type: STRING 
*   Default: `none`
*   Usage: `--riverId`

Please provide at least one river id to run.

River Id can be found in the river url, structured as this:

1```
https://<cli-console>/#/river/<accountId>/<environmentId>/river/**<RiverId>**
```

*   `entityname`: 
*   Type: STRING 
*   Default: `none`
*   Usage: `--entityName`

*   `waitforend`:

*   Type: BOOL 
*   Default: `false`
*   Usage: `--waitForEnd`

*   `timeout`:

*   Type: INT 
*   Default: `none`
*   Usage: `--timeout`

The number of seconds to wait for the run to complete until giving up.

 Eligible only on hitting --waitForEnd option

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
11
12
13
14
15
16
17```
Usage: rivery rivers run fire [OPTIONS]

   Run a river whitin the current profile (account+environment). Gets a
   riverid key, with the river id to run and just run it in the platform.

Options:
  --riverId TEXT     Please provide at least one river id to run. River Id can
                     be found in the river url, structured as this:
                     https://<cli-console>/#/river/<accountId>/<environmentId>/r
                     iver/**<RiverId>**  [required]

  --entityName TEXT
  --waitForEnd
  --timeout INTEGER  The number of seconds to wait for the run to complete until
                     giving up.   Eligible only on hitting --waitForEnd option

  --help             Show this message and exit.
```

[Previous rivers run](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-run/)[Next rivers run status](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/)
