# Source: https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/

Title: activities logs fetch - Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/

Markdown Content:
activities logs fetch - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/#logs-fetch)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 activities logs fetch 

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
            *   [rivers run status](https://riveryio.github.io/rivery_cli/commands/rivers/run-status/)

    *   - [x]  activities   activities  
        *   [rivery activities](https://riveryio.github.io/rivery_cli/commands/activities/rivery-activities/)
        *   - [x]  activities logs   activities logs  
            *   [activities logs](https://riveryio.github.io/rivery_cli/commands/activities/activities-logs/)
            *   - [x]  activities logs fetch  [activities logs fetch](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/) Table of contents  
                *   [Usage](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/#usage)
                *   [Options](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/#options)
                *   [CLI Help](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/#cli-help)

*   - [x]  Resources   Resources  
    *   [Glossary](https://riveryio.github.io/rivery_cli/resources/glossary/)
    *   [FAQ](https://riveryio.github.io/rivery_cli/resources/faq/)
    *   [Link and Examples](https://riveryio.github.io/rivery_cli/resources/extras/)

 Table of contents  
*   [Usage](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/#usage)
*   [Options](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/#options)
*   [CLI Help](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/#cli-help)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/commands/activities/logs-fetch.md "Edit this page")
logs fetch
==========

None

Usage
-----

1```
Usage: rivery activities logs fetch [OPTIONS]
```

Options
-------

*   `runid` (REQUIRED): 
*   Type: STRING 
*   Default: `none`
*   Usage: `--runId`

The run id that will be used to filter the logs.

*   `filepath`: 
*   Type: STRING 
*   Default: `none`
*   Usage: `--filePath`

The file that the logs should be saved to.

*   `pretty`: 
*   Type: BOOL 
*   Default: `false`
*   Usage: `--pretty`

Whether logs should be in a pretty table format or not.

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
7```
Usage: rivery activities logs fetch [OPTIONS]

Options:
  --runId TEXT     The run id that will be used to filter the logs.  [required]
  --filePath TEXT  The file that the logs should be saved to.
  --pretty TEXT  Whether logs should be in a pretty table format or not.
  --help           Show this message and exit.
```

[Previous activities logs](https://riveryio.github.io/rivery_cli/commands/activities/activities-logs/)[Next Glossary](https://riveryio.github.io/rivery_cli/resources/glossary/)
