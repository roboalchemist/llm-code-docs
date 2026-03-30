# Source: https://riveryio.github.io/rivery_cli/getting-started/

Title: Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/getting-started/

Markdown Content:
Getting Started - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/getting-started/#getting-started)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 Getting Started 

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
*   - [x]  Getting Started  [Getting Started](https://riveryio.github.io/rivery_cli/getting-started/) Table of contents  
    *   [Requirements](https://riveryio.github.io/rivery_cli/getting-started/#requirements)
    *   [Install](https://riveryio.github.io/rivery_cli/getting-started/#install)
    *   [Check Installation](https://riveryio.github.io/rivery_cli/getting-started/#check-installation)
    *   [Initiate a new project](https://riveryio.github.io/rivery_cli/getting-started/#initiate-a-new-project)
    *   [Create the first profile](https://riveryio.github.io/rivery_cli/getting-started/#create-the-first-profile)

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
            *   [activities logs fetch](https://riveryio.github.io/rivery_cli/commands/activities/logs-fetch/)

*   - [x]  Resources   Resources  
    *   [Glossary](https://riveryio.github.io/rivery_cli/resources/glossary/)
    *   [FAQ](https://riveryio.github.io/rivery_cli/resources/faq/)
    *   [Link and Examples](https://riveryio.github.io/rivery_cli/resources/extras/)

 Table of contents  
*   [Requirements](https://riveryio.github.io/rivery_cli/getting-started/#requirements)
*   [Install](https://riveryio.github.io/rivery_cli/getting-started/#install)
*   [Check Installation](https://riveryio.github.io/rivery_cli/getting-started/#check-installation)
*   [Initiate a new project](https://riveryio.github.io/rivery_cli/getting-started/#initiate-a-new-project)
*   [Create the first profile](https://riveryio.github.io/rivery_cli/getting-started/#create-the-first-profile)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/getting-started.md "Edit this page")
Getting started
===============

Requirements
------------

1.   You must have Python 3.6 or later installed. For installation instructions, see the [Downloading Python](https://www.python.org/downloads/) page in Python's Beginner Guide.

2.   An API Token with the following scopes:

1
2
3
4
5
6
7
8```
* me:list
    * river:execute
    * river:edit
    * river:list
    * river:delete
    * connection:edit
    * connection:list
    * connection:delete
```
 In order to create a new API token, [please refer to our docs](https://rivery.io/docs/api-documentation)

Install
-------

Install Rivery CLI, by using the next command:

1```
> pip install rivery-cli
```

Check Installation
------------------

In order to see if Rivery CLI was installed in your client, check the version option by the next command:

1```
> rivery --version
```

Result should be:

1```
Rivery CLI, version ...
```

Initiate a new project
----------------------

in order to start new _project_: 1. create new project directory, for example in linux base OS:

1```
> mkdir /home/my-project
```
 or in windows: 
1```
> mkdir c:\my-project
```

1.   Go into the `my-project` directory you've created: `cd my-project`
2.   run the next command and choose your project name. 
1```
> rivery init
```

Create the first profile
------------------------

Rivery CLI store defaults and credentials under an "entity" called `profile`.

Each profile has its name and the configurations under it. Due to every API token refers to specific `account`+`environment` inside your Rivery console, and every account+environment pair has its own credentials, it is likely you'll have a profile per each account+environment coupling.

For creating your first profile use the next command:

1```
> rivery configure
```

And Follow the prompt:

1
2
3
4```
> Please enter your token. (******): ...
> Choose your Region () [...]: ...
> Thank you for entering auth credentials. 
> Please check your profile at: ~/.rivery/auth
```

And you're good to go!

[Previous Home](https://riveryio.github.io/rivery_cli/)[Next Authentication](https://riveryio.github.io/rivery_cli/reference/authentication/)
