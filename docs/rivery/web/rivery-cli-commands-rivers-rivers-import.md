# Source: https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/

Title: Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/

Markdown Content:
rivers import - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/#rivers-import)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 rivers import 

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
        *   - [x]  rivers import  [rivers import](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/) Table of contents  
            *   [Usage](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/#usage)
            *   [Options](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/#options)
            *   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/#cli-help)

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
*   [Usage](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/#usage)
*   [Options](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/#options)
*   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/#cli-help)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/commands/rivers/rivers-import.md "Edit this page")
rivers import
=============

Import current river(s) into a yaml files. Get a group or river ID in the right env and account and create a yaml file per the source

Usage
-----

1```
Usage: rivery rivers import [OPTIONS]
```

Options
-------

*   `riverid`: 
*   Type: STRING 
*   Default: `none`
*   Usage: `--riverId`

Please provide at least one river id. River Id can be found in the river url, structured as this: https:///#/river///river/

*   `groupname`: 
*   Type: STRING 
*   Default: `none`
*   Usage: `--groupName`

Please provide a group name of rivers. The group name can be found near every river, in the river screen at cli.

*   `path`: 
*   Type: STRING 
*   Default: `none`
*   Usage: `--path`

The path you want to import into.

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
15```
Usage: rivery rivers import [OPTIONS]

  Import current river(s) into a yaml files. Get a group or river ID in the
  right env and account and create a yaml file per the source

Options:
  --riverId TEXT    Please provide at least one river id. River Id can be found
                    in the river url, structured as this: https://<cli-console>/
                    #/river/<accountId>/<environmentId>/river/**<RiverId>**

  --groupName TEXT  Please provide a group name of rivers. The group name can be
                    found near every river, in the river screen at cli.

  --path TEXT       The path you want to import into.
  --help            Show this message and exit.
```

[Previous rivery rivers](https://riveryio.github.io/rivery_cli/commands/rivers/rivery-rivers/)[Next rivers push](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-push/)
