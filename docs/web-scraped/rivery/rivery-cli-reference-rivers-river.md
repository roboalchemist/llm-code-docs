# Source: https://riveryio.github.io/rivery_cli/reference/rivers/river/

Title: Rivery Command Line Tool (CLI)

URL Source: https://riveryio.github.io/rivery_cli/reference/rivers/river/

Markdown Content:
Yaml Reference - Rivery Command Line Tool (CLI)
===============
- [x] - [x] 

[Skip to content](https://riveryio.github.io/rivery_cli/reference/rivers/river/#river-yaml-reference)

[![Image 1: logo](https://riveryio.github.io/rivery_cli/assets/Rivery%20-%20favicon.png)](https://riveryio.github.io/rivery_cli/ "Rivery Command Line Tool (CLI)")

 Rivery Command Line Tool (CLI) 

 Yaml Reference 

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
            *   - [x]  Yaml Reference  [Yaml Reference](https://riveryio.github.io/rivery_cli/reference/rivers/river/) Table of contents  
                *   [Notifications](https://riveryio.github.io/rivery_cli/reference/rivers/river/#notifications)
                *   [Schedule](https://riveryio.github.io/rivery_cli/reference/rivers/river/#schedule)

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
*   [Notifications](https://riveryio.github.io/rivery_cli/reference/rivers/river/#notifications)
*   [Schedule](https://riveryio.github.io/rivery_cli/reference/rivers/river/#schedule)

[](https://github.com/RiveryIo/rivery_cli/edit/docs/docs/reference/rivers/river.md "Edit this page")
River Yaml Reference
====================

River yaml reference has couple of mandatory keys needed to be provided in the yaml.

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
name: River name. 
description: River Description. 
type: logic # The type of the river, we now support only *logic* type of river. 
group_name: The river group name.
notifications: 
  <notifications block>
schedule: 
  <schedule block>
properties: 
  <properties block by type>
```

Notifications
-------------

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
14```
notifications: 
  on_failure: 
    # On failure notification. 
    email: myemail@mycomp.com # email to send notifications
    enabled: true|false 
  on_warning:
    # On warning notifications
    email: myemail@mycomp.com # email to send notifications
    enabled: true|false 
  on_run_threshold:
    # On runtime notification 
    email: myemail@mycomp.com # email to send notifications
    enabled: true|false
  run_notification_timeout: 43200  # The number of seconds for sending a notification timeout, up to 43200 (12 hours).
```

Schedule
--------

Schedule block, define the scheduling method of the river

All scheduling in Rivery uses [quartz expression](https://www.freeformatter.com/cron-expression-generator-quartz.html) as the scheduling expression to fire the river.

1
2
3
4
5```
schedule:
  cronExp: 0 55 14 1 1 ? * # Quartz expression to run
  endDate: 2020-01-03T00:00:00 # Start date of the scheduling
  isEnabled: true|false # Does the scheduling enabled
  startDate:  2020-01-03T00:00:00 # End date of the scheduling
```

[Previous Basic Reference](https://riveryio.github.io/rivery_cli/reference/reference/)[Next Logic](https://riveryio.github.io/rivery_cli/reference/rivers/logic/logic/)
