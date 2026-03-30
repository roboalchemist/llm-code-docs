# Source: https://riveryio.github.io/rivery_cli/reference/project/

Title: Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/reference/project/

Markdown Content:
Project - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/reference/project/#projectyaml)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 Project 

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
    *   - [x]  Project  [Project](https://riveryio.github.io/rivery_cli/reference/project/) Table of contents  
        *   [What is it for?](https://riveryio.github.io/rivery_cli/reference/project/#what-is-it-for)
        *   [Reference](https://riveryio.github.io/rivery_cli/reference/project/#reference)
        *   [Init a new project](https://riveryio.github.io/rivery_cli/reference/project/#init-a-new-project)
        *   [Importing groups/rivers](https://riveryio.github.io/rivery_cli/reference/project/#importing-groupsrivers)

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
            *   [activities logs fetch](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/)

*   - [x]  Resources   Resources  
    *   [Glossary](https://riveryio.github.io/rivery_cli/resources/glossary/)
    *   [FAQ](https://riveryio.github.io/rivery_cli/resources/faq/)
    *   [Link and Examples](https://riveryio.github.io/rivery_cli/resources/extras/)

 Table of contents  
*   [What is it for?](https://riveryio.github.io/rivery_cli/reference/project/#what-is-it-for)
*   [Reference](https://riveryio.github.io/rivery_cli/reference/project/#reference)
*   [Init a new project](https://riveryio.github.io/rivery_cli/reference/project/#init-a-new-project)
*   [Importing groups/rivers](https://riveryio.github.io/rivery_cli/reference/project/#importing-groupsrivers)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/reference/project.md "Edit this page")
`project.yaml`
==============

What is it for?
---------------

The `project.yaml` is the file define the project structure and basic configuration. Evert Rivery IaC project needs its own `project.yaml` file, which indicates that the project dir is a Rivery IaC project. The CLI command knows to handle the references and connectivity between entities inside the project only under project dir.

For example, a directory of `my-project` includes a `project.yaml` file, and should be used as a Rivery IaC reference project.

Reference
---------

1
2
3
4
5```
name: <string> # my-project-name
version: 1.0 # Rivery Iac reference version. 
models: <string> # the name of the "models" or "entities" dir inside the project.
sqls: <string> # the name of the "sql" files dir isnide the project
maps: <string> # the name of the mapping (table references) dir inside the project
```

Init a new project
------------------

In order to create new project inside a dir, just run the [`rivery init`](https://riveryio.github.io/rivery_cli/reference/commands/rivery-init.md) command.

Importing groups/rivers
-----------------------

Rivery CLI provide a command to create local entity `yaml` files from rivers in a live account/env. In order to import river or an entire group of rivers from your account to your local project, you can run the next command:

1```
> rivery rivers import --groupName='my-group'/--riverId='123475658493782612' --path=/import/path/under/models/dir
```

Check out the [`rivery rivers import` reference](https://riveryio.github.io/rivery_cli/commands/rivers/rivers-import/) for more info.

[Previous Basics](https://riveryio.github.io/rivery_cli/reference/best-practice/)[Next Basic Reference](https://riveryio.github.io/rivery_cli/reference/reference/)
