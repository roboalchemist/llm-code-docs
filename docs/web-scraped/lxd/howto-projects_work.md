# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/projects_work/

[]

# How to work with different projects[¶](#how-to-work-with-different-projects "Link to this heading")

If you have more projects than just the [`default`] project, you must make sure to use or address the correct project when working with LXD.

Note

If you have projects that are [[confined to specific users]](../../explanation/projects/#projects-confined), only users with full access to LXD can see all projects.

Users without full access can only see information for the projects to which they have access.

## List projects[¶](#list-projects "Link to this heading")

CLI

API

UI

To list all projects (that you have permission to see), enter the following command:

    lxc project list

By default, the output is presented as a list:

[`user@host:~$`]` `

[[`lxc`]` `[`project`]` `[`list`]` `]

    +----------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------+---------+
    |      NAME            | IMAGES | PROFILES | STORAGE VOLUMES | STORAGE BUCKETS | NETWORKS | NETWORK ZONES |     DESCRIPTION     | USED BY |
    +----------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------+---------+
    | default              | YES    | YES      | YES             | YES             | YES      | YES           | Default LXD project | 19      |
    +----------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------+---------+
    | my-project (current) | YES    | NO       | NO              | NO              | YES      | YES           |                     | 0       |
    +----------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------+---------+

You can request a different output format by adding the [`--format`] flag. See [[[`lxc`]` `[`project`]` `[`list`]` `[`--help`]]](../../reference/manpages/lxc/project/list/#lxc-project-list-md) for more information.

To list all projects (that you have permission to see), send the following request:

    lxc query --request GET /1.0/projects

To display information about each project, use [[Recursion]](../../rest-api/#rest-api-recursion):

    lxc query --request GET /1.0/projects?recursion=1

See [[`GET`]` `[`/1.0/projects`]](/lxd/latest/api/#/projects/projects_get) and [[`GET`]` `[`/1.0/projects?recursion=1`]](/lxd/latest/api/#/projects/projects_get_recursion1) for more information.

To list all projects (that you have permission to see), expand the [Project] drop-down.

[]

## Switch projects[¶](#switch-projects "Link to this heading")

CLI

API

UI

By default, all commands that you issue in LXD affect the project that you are currently using. To see which project you are in, use the [[[`lxc`]` `[`project`]` `[`list`]]](../../reference/manpages/lxc/project/list/#lxc-project-list-md) command.

To switch to a different project, enter the following command:

    lxc project switch <project_name>

The API does not have the concept of switching projects. All requests target the default project unless a different project is specified (see [[Target a project]](#projects-target)).

To switch to another project, select a different project from the [Project] drop-down.

[]

## Target a project[¶](#target-a-project "Link to this heading")

When using the CLI or the API, you can target a specific project when running a command. Many LXD commands support the [`--project`] flag or the [`project`] parameter to run an action in a different project.

Note

You can target only projects that you have permission for.

An example for targeting another project instead of switching to it is listing the instances in a specific project:

CLI

API

UI

To list the instances in a specific project, add the [`--project`] flag to the [[[`lxc`]` `[`list`]]](../../reference/manpages/lxc/list/#lxc-list-md) command. For example:

    lxc list --project my-project

To list the instances in a specific project, add the [`project`] parameter to the request. For example:

    lxc query --request GET /1.0/instances?project=my-project

Or with [[Recursion]](../../rest-api/#rest-api-recursion):

    lxc query --request GET /1.0/instances?recursion=2\&project=my-project

The UI does not currently support targeting another project. Instead, [[switch to the other project]](#projects-switch).

[]

## Move an instance to another project[¶](#move-an-instance-to-another-project "Link to this heading")

CLI

API

UI

To move an instance from one project to another, enter the following command:

    lxc move <instance_name> <new_instance_name> --project <source_project> --target-project <target_project>

You can keep the same instance name if no instance with that name exists in the target project.

For example, to move the instance [`my-instance`] from the [`default`] project to [`my-project`] and keep the instance name, enter the following command:

    lxc move my-instance my-instance --project default --target-project my-project

To move an instance from one project to another, send a POST request to the instance:

    lxc query --request POST /1.0/instances/<instance_name>?project=<source_project> --data ''

If no instance with that name exists in the target project, you can leave out the name for the new instance to keep the existing name.

For example, to move the instance [`my-instance`] from the [`default`] project to [`my-project`] and keep the instance name, enter the following command:

    lxc query --request POST /1.0/instances/my-instance?project=default --data ''

Depending on your projects, you might need to change other configuration options when moving the instance. For example, you might need to change the root disk device if one of the projects uses isolated storage volumes.

See [[`POST`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_post) for more information.

The UI does not currently support moving instances between projects.

## Copy a profile to another project[¶](#copy-a-profile-to-another-project "Link to this heading")

If you create a project with the default settings, profiles are isolated in the project ([[`features.profiles`]](../../reference/projects/#project-features:features.profiles) is set to [`true`]). Therefore, the project does not have access to the default profile (which is part of the [`default`] project), and you will see an error similar to the following when trying to create an instance:

    Error: Failed instance creation: Failed creating instance record: Failed initialising instance: Failed getting root disk: No root device could be found

To fix this, you can copy the contents of the [`default`] project's default profile into the current project's default profile. To do so:

CLI

API

UI

Enter the following command:

    lxc profile show default --project default | lxc profile edit default

Send the following request, replacing [`<project>`] with the new project that has an empty default profile:

    lxc query --request PUT /1.0/profiles/default?projects=<project> --data \
      "$(lxc query --request GET /1.0/profiles/default)"

1.  Select the [`default`] project from the [Project] drop-down.

2.  Go to [Profiles] and select the default profile.

3.  In the profile view, switch to the [Configuration] tab.

4.  Select [YAML configuration] and copy the YAML representation of the profile.

5.  Select the project with the empty default profile from the [Project] drop-down.

6.  Go to [Profiles] and select the empty default profile for the project.

7.  In the profile view, switch to the [Configuration] tab.

8.  Select [YAML configuration] and click [Edit profile].

9.  Paste the YAML representation that you copied and save the changes.