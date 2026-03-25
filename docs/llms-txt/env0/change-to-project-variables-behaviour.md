# Source: https://docs.envzero.com/changelogs/2023/11/change-to-project-variables-behaviour.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ☢️ Breaking Change to Parent and Sub Projects Variables Behaviour

> We're happy to announce that starting Dec 10th, variables defined in projects would cascade down to their sub projects. Environments would not receive only the variables of the project they're defined in, but also the variables of any ancestor project. By incorporating these changes, we aim to fulfill user requests, achieve a more uniform configuration, enhance security, and streamline the overall variable management process.

We're happy to announce that starting Dec 10th, variables defined in projects would cascade down to their sub projects.\
Environments would not receive only the variables of the project they're defined in, but also the variables of any ancestor project.

By incorporating these changes, we aim to fulfill user requests, achieve a more uniform configuration, enhance security, and streamline the overall variable management process.

# How could this affect you?

For the purpose of explanation, consider a hierarchical structure comprising a Parent project and a sub-project, Sub Project, with an associated environment in the Sub project. The impending modification may influence the environment in the following ways:

1. ***Variable Overwriting***:\
   Scenario: Global variable "A" initialized to "global". Project variable "A" in the Parent project set to "project".
   1. Prior to this change, the environment contains the variable "A" with the value "global."
   2. After to the change, the environment will host a variable "A" with the value "project," potentially resulting in the overwrite of the previous value.
2. ***Introduction of New Variables***:\
   Scenario: Project variable "X" and Parent project, and Project Variable "Y" on Sub Proejct.
   1. Prior to this change, the environment lacks variable "X" but includes variable "Y."
   2. After to the change, both variables "X" and "Y" will exist in the environment.

# Why the change?

* ***User Requests***:\
  This modification responds to numerous user requests for a streamlined process in defining variables across multiple projects within a hierarchical structure.
* ***Uniform Configuration***:\
  The proposed change addresses the recurring need for users to define variables across projects and their children. This ensures a consistent configuration across all projects beneath a parent project.
* ***Enhanced Security***:\
  Especially beneficial when sensitive variables are involved, the modification allows for centralized management without exposing sensitive information to users who do not require access to higher-level projects.
* ***Streamlining Configuration***:\
  The adjustment significantly reduces redundancy in variable definition, simplifying the configuration process for users and administrators alike.

Built with [Mintlify](https://mintlify.com).
