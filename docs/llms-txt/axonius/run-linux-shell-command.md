# Source: https://docs.axonius.com/docs/run-linux-shell-command.md

# Axonius - Deploy Files and Run Shell Command on Linux Assets

**Axonius - Deploy Files and Run Shell Command on Linux Assets** (Deploy Files and Run Linux Shell Command) action allows you to populate a field with the output of running the command supplied in the Command field via SSH, on each of the query results entities, which are Linux devices.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

To configure the **Deploy Files and Run Linux Shell Command** action, do as follows:

1. From the **Action Library**, click **Deploy Files and Run Commands**, and then click **Deploy Files and Run Linux Shell Command**.

2. Define a unique action name.

3. Specify the information required to run the Linux Shell Command. Most of the action configuration and logic are the same as the ones used when [Connecting Linux SSH Adapter](/docs/linux-ssh).

4. Specify the command you want to run on the Linux device. Add a condition to the command (for example, *'&& echo Success || echo Fail'*)  to print the result into the Command Name field. This field can then be used in future queries.

5. To deploy a single or multiple files on the Linux device:
   1. Choose a file to be uploaded. You can upload one or multiple files. Existing files will be overridden.
   2. Specify the path on the Linux device the files will be uploaded. If not populated, the files are uploaded to "*/tmp*" folder.
   3. To delete the files afer executing the specified command line, select the **Delete Files After Execution** checkbox.
   4. Specify the permissions given to the uploded files. This Defaults to "777".

6. If you are using multi-nodes, choose the Axonius node to use to interact with the adapter when executing the enforcement action.

7. Save the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).