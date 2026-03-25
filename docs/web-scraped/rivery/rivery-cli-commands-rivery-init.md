# Source: https://riveryio.github.io/rivery_cli/commands/rivery-init/

Title: Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/commands/rivery-init/

Markdown Content:
init - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/commands/rivery-init/#rivery-init)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 init 

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
    *   - [x]  init  [init](https://riveryio.github.io/rivery_cli/commands/rivery-init/) Table of contents  
        *   [Usage](https://riveryio.github.io/rivery_cli/commands/rivery-init/#usage)
        *   [Options](https://riveryio.github.io/rivery_cli/commands/rivery-init/#options)
        *   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivery-init/#cli-help)

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
*   [Usage](https://riveryio.github.io/rivery_cli/commands/rivery-init/#usage)
*   [Options](https://riveryio.github.io/rivery_cli/commands/rivery-init/#options)
*   [CLI Help](https://riveryio.github.io/rivery_cli/commands/rivery-init/#cli-help)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/commands/rivery-init.md "Edit this page")
rivery init
===========

Make a initiation project.yaml in the current path

Usage
-----

1```
Usage: rivery init [OPTIONS]
```

Options
-------

*   `name`: 
*   Type: STRING 
*   Default: `none`
*   Usage: `--name`

Project name

*   `models`: 
*   Type: STRING 
*   Default: `models`
*   Usage: `--models`

The Models (entities) directory

*   `sqls`: 
*   Type: STRING 
*   Default: `sqls`
*   Usage: `--sqls`

The sqls (queries) directory

*   `maps`: 
*   Type: STRING 
*   Default: `maps`
*   Usage: `--maps`

The mapping directory

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
10```
Usage: rivery init [OPTIONS]

  Make a initiation project.yaml in the current path

Options:
  --name TEXT    Project name
  --models TEXT  The Models (entities) directory
  --sqls TEXT    The sqls (queries) directory
  --maps TEXT    The mapping directory
  --help         Show this message and exit.
```

[Previous rivery](https://riveryio.github.io/rivery_cli/commands/rivery/)[Next configure](https://riveryio.github.io/rivery_cli/commands/rivery-configure/)
