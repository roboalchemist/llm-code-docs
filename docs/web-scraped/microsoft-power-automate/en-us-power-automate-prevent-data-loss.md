# Source: https://learn.microsoft.com/en-us/power-automate/prevent-data-loss

Title: Data loss prevention (DLP) policy creation - Power Automate

URL Source: https://learn.microsoft.com/en-us/power-automate/prevent-data-loss

Markdown Content:
An organization's data is critical to its success. Its data needs to be readily available for decision-making, but at the same time, data needs to be protected so that it isn't shared with audiences that shouldn't have access to it. To protect your business data, Power Automate gives you the ability to create and enforce policies that define which connectors can access and share it. The policies that define how data can be shared are referred to as data loss prevention (DLP) policies.

Administrators control DLP policies. If a DLP policy is blocking your flows from running, contact your administrator.

Learn more about protecting your data with Power Platform in [Data Loss Prevention (DLP) policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention).

Power Automate allows you to create and enforce DLP policies that classify desktop flow modules and individual module actions as **Business**, **Non-business**, or **Blocked**. This categorization prevents makers from combining modules and actions from different categories into a desktop flow or between a cloud flow and the desktop flows it uses.

Important

* DLP policy enforcement for desktop flows is available in all environments.
* DLP for desktop flows is available for versions of Power Automate for desktop 2.14.173.21294 or later. If you're using an earlier version, uninstall it and update to the latest version.

By default, desktop flow action groups don't appear when you're creating a DLP policy. You need to turn on the **Show desktop flow actions in DLP policies** setting in your tenant settings. After this setting is enabled, it can't be changed.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

2. On the left side panel, select **Settings**.

3. On the **Tenant settings** page, select **Desktop flow actions in DLP**.

4. Turn on **Show desktop flow actions in DLP policies**, and then select **Save**.

![Image 1: Screenshot of the DLP for desktop flows setting in the Power Platform admin center.](https://learn.microsoft.com/en-us/power-automate/media/prevent-data-loss/dlp-desktop-flows.png)

You can now classify desktop flow action groups when you create a data policy.

Important

If you began using DLP for desktop flows before 2022, you might notice the following:

* The tenant setting appears as 'false' in PowerShell even though it's enabled in the Power Platform admin center, _and_
* DLP connectors are active within your DLP policies.

When admins edit or create a policy, desktop flow action groups are added to the default group, and the policy is applied after it's saved. The policy is suspended if the default group is set to **Blocked** and the desktop flows are running in the target environments.

You can manage your DLP policies for desktop flows the same way you manage cloud flow connectors and actions. Desktop flow modules are groups of similar actions as displayed in the Power Automate for desktop user interface. A module is similar to connectors that are used in cloud flows. You can define a DLP policy that manages both desktop flow modules and cloud flow connectors. Some basic modules, such as **Variables**, can't be managed in the scope of DLP policy because almost all desktop flows need to use them. [Learn more about the fundamentals of DLP policies and how to create them](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention).

When your tenant is opted into the user experience in the Power Platform, your administrators automatically see the new desktop flow modules in the default data group of the DLP policy they're creating or updating.

![Image 2: Screenshot of a DLP policy under construction in the Power Platform admin center.](https://learn.microsoft.com/en-us/power-automate/media/prevent-data-loss/prevent-dlp.png)

Warning

When desktop flow modules are added to DLP policies, your tenant's desktop flows are evaluated against them, and they're suspended if they're non-compliant. If your administrator creates or updates the DLP policy without noticing the new modules, desktop flows can be unexpectedly suspended.

You have other options to govern desktop flows.

* **Ability to govern desktop flow orchestration**: The desktop flow connector can be governed in your policies like any other connector in all environments.

* **Ability to govern usage of Power Automate for desktop**: You can govern Power Automate for desktop flows through Group Policy objects (GPO). This governance allows you to turn on or off desktop flows for actions such as to restrict to a set of environments or regions, limit use of account types, and restrict manual updates.

[Learn more about governance in Power Automate](https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance).

The following desktop flow modules are available in DLP:

* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.ActiveDirectory ActiveDirectory
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.AWS AWS
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Azure Azure
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.WebAutomation Browser Automation
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Cmd CMD session
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Clipboard Clipboard
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Compression Compression
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Cryptography Cryptography
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.CyberArk CyberArk
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Database Database
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Email Email
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Excel Excel
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Exchange Exchange
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.FTP FTP
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.File File
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Folder Folder
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.GoogleCognitive Google cognitive
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Web HTTP
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.IBMCognitive IBM cognitive
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Display Message boxes
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.MicrosoftCognitive Microsoft cognitive
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.MouseAndKeyboard Mouse and keyboard
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.OCR OCR
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Outlook Outlook
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Pdf PDF
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.PowerAutomateSecretVariables Power Automate Secret Variables
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Runflow Run flow
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Scripting Scripting
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.System System
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.TerminalEmulation Terminal emulation
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.UIAutomation UI automation
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Services Windows Services
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.Workstation Workstation
* providers/Microsoft.ProcessSimple/operationGroups/DesktopFlow.XML XML

If you don't want to turn on the **Show desktop flow actions in DLP policies** setting, you can use the following PowerShell script to add all desktop flow modules to the **Blocked** group of a DLP policy. If you already turned on the setting, you don't need to use this script.

```
# Step #1: Retrieve a DLP policy named 'My DLP Policy' 
  $dlpPolicies = Get-DlpPolicy  
  $dlpPolicy = $dlpPolicies.value | where {$_.displayName -eq 'My DLP Policy'}  

# Step #2: Get all Power Automate for desktop flow modules 
  $desktopFlowModules = Get-DesktopFlowModules  

# Step #3: Convert the list of Power Automate for desktop flow modules to a format that can be added to the policy 
  $desktopFlowModulesToAddToPolicy = @()  
        foreach ($modules in $desktopFlowModules) {  
          $desktopFlowModulesToAddToPolicy += [pscustomobject]@{  
          id=$modules.id  
          name=$modules.Properties.displayName  
          type=$modules.type  
      }  
  }  

# Step #4: Add all desktop flow modules to the 'blocked' category of 'My DLP Policy' 
    Add-ConnectorsToPolicy -Connectors $desktopFlowModulesToAddToPolicy -PolicyName $dlpPolicy.name -classification Blocked -Verbose
```

The following PowerShell script adds two specific desktop flow modules to the default data group of a DLP policy.

```
# Step #1: Retrieve a DLP policy named 'My DLP Policy' 
  $dlpPolicies = Get-DlpPolicy  
  $dlpPolicy = $dlpPolicies.value | where {$_.displayName -eq 'My DLP Policy'}  

# Step #2: Get all Power Automate for desktop flow modules 
  $desktopFlowModules = Get-DesktopFlowModules  

# Step #3: Create a list with the 'Active Directory' and 'Workstation' modules 
  $desktopFlowModulesToAddToPolicy = @()  
  $activeDirectoryModule = $desktopFlowModules | where {$_.properties.displayName -eq "Active Directory"}  
  $desktopFlowModulesToAddToPolicy += [pscustomobject]@{  
    id=$activeDirectoryModule.id  
    name=$activeDirectoryModule.Properties.displayName  
    type=$activeDirectoryModule.type  
  }
  $clipboardModule = $desktopFlowModules | where {$_.properties.displayName -eq "Workstation"}  
  $desktopFlowModulesToAddToPolicy += [pscustomobject]@{  
    id=$clipboardModule.id  
    name=$clipboardModule.Properties.displayName  
    type=$clipboardModule.type  
  }  

# Step #4: Add both modules to the default data group of 'My DLP Policy' 
  Add-ConnectorsToPolicy -Connectors $desktopFlowModulesToAddToPolicy -PolicyName $dlpPolicy.name -Classification $dlpPolicy.defaultConnectorsClassification -Verbose
```

If you don't want to use the DLP for desktop flows feature, you can use the following PowerShell script to opt out.

```
# Step #1: Retrieve the DLP policy named 'My DLP Policy'

$policies = Get-DlpPolicy
$dlpPolicy = $policies.value | Where-Object { $_.displayName -eq "My DLP Policy" }

# Step #2: Get all Power Automate for desktop flow modules

$desktopFlowModules = Get-DesktopFlowModules
 
# Step #3: Remove Desktop Flow modules from all 3 connector groups of the policy

foreach ($connectorGroup in $dlpPolicy.connectorGroups) {
   $connectorGroup.connectors = $connectorGroup.connectors | Where-Object { $desktopFlowModules.id -notcontains $_.id }
}

# Step #4: Save the updated policy

Set-DlpPolicy -PolicyName $dlpPolicy.name -UpdatedPolicy $dlpPolicy
```

If your users don't have the latest Power Automate for desktop, DLP policy enforcement is limited. They don't see design-time error messages when they're trying to run, debug, or save desktop flows that violate DLP policies. Background jobs periodically scan desktop flows in the environment and automatically suspend any that violate DLP policies. Users can't run desktop flows from a cloud flow if the desktop flow violates any data loss prevention policy.

Makers who have the latest Power Automate for desktop can't debug, run, or save desktop flows that violate DLP policy. They also can't select a desktop flow that's in violation of a DLP policy from a cloud flow step.

1. When you create or edit a flow, Power Automate evaluates it against the current set of DLP policies.
    1.   Enforcement of flows without a child flow, which is 99% of flows, is synchronous and occurs in real-time.
    2.   Enforcement of a flow with a child flow is asynchronous, since the child flows need to be evaluated as well, and occurs within 24 hours.

2. When you create or change a DLP policy, a background job scans all active flows in the environment, evaluates them, and then suspends the flows that violate the policy. Enforcement is asynchronous and occurs within 24 hours. If a DLP policy change occurs when the previous DLP policy is being evaluated, then the evaluation restarts to make sure the latest policies are enforced.
3. Weekly, a background job does a consistency check of all active flows in the environment against the DLP policies to confirm that a DLP policy check wasn't missed.

If the DLP enforcement background job finds a desktop flow that no longer violates any DLP policy, then the background job automatically removes the suspension. Active cloud flows that were suspended in the previous seven (7) days are re-activated automatically if they no longer violate any DLP policy.

Periodically, DLP enforcement needs to change because new DLP capabilities or a bug fix are rolled out or an enforcement gap is filled. When changes can affect existing flows, apply the following staged DLP enforcement change management process:

1. **Investigating**: Confirm the need for a DLP enforcement change and investigate the specifics of the change.

2. **Learning**: Implement the change and gather data about the breadth of the effects of the change. Document DLP enforcement changes to explain the scope of the change. If the data suggests that customers will be greatly affected, then a communication might be sent to those customers to let them know that a change is coming. If the change has a broad impact on existing flows, then at a later stage in the learning phase, when the background DLP enforcement job finds a violation in an existing flow, Power Automate notifies the flow owners that the flow will be suspended, so that they have more time to respond.

3. **Notify only**: Turn on email notifications only for DLP violations so owners of existing flows get notified about the upcoming DLP enforcement change. When the background DLP enforcement job finds a violation in an existing flow, notify the flow owners that the flow will be suspended. This mechanism runs weekly.

4. **Design-time enforcement**: Turn on design-time enforcement of DLP violations so that owners of existing flows get notified about the upcoming DLP enforcement change, but any flows that are changed get a full DLP policy evaluation at design time. This is also known as _soft enforcement_.

    *   **Design-time**: When a flow is updated and saved, use the updated DLP enforcement and suspend the flow if needed so the maker is immediately aware of the enforcement.

    *   **Background process**: When the background DLP enforcement job finds a violation in a flow, notify the flow owners that the flow will be suspended. This mechanism includes creation or changes to DLP policy and consistency checks.

5.   **Full enforcement**: Turn on full enforcement of DLP violations, so DLP policies are fully enforced on all existing and new flows. The DLP policies are fully enforced when flows are saved during DLP enforcement background job evaluation. This is also known as _hard enforcement_.

The following table lists DLP enforcement changes and the date the changes were effective.

| Date | Description | Reason for change | Stage | Design-time enforcement availability* | Full enforcement availability* |
| --- | --- | --- | --- | --- | --- |
| May 2022 | Delegated authorization background job enforcement | DLP policies are enforced on flows that use delegated authorization while the flow is being saved, but not during background job evaluation. | Full | June 2, 2022 | July 21, 2022 |
| May 2022 | Request apiConnection trigger enforcement | DLP policies weren't enforced correctly for some triggers. The affected triggers have **type=Request** and **kind=apiConnection**. Many of the affected triggers are instant triggers, which are used in instant, or manually triggered, flows. The affected triggers include the following. - [Power BI](https://learn.microsoft.com/en-us/connectors/powerbi/): Power BI button clicked - [Teams](https://learn.microsoft.com/en-us/connectors/teams/): From the compose box (V2) - [OneDrive for Business](https://learn.microsoft.com/en-us/connectors/onedriveforbusiness/): For a selected file - [Dataverse](https://learn.microsoft.com/en-us/connectors/commondataserviceforapps/): When a flow step is run from a business process flow - [Dataverse (legacy)](https://learn.microsoft.com/en-us/connectors/commondataservice/): When a record is selected - [Excel Online (Business)](https://learn.microsoft.com/en-us/connectors/excelonlinebusiness/): For a selected row - [SharePoint](https://learn.microsoft.com/en-us/connectors/sharepointonline/): For a selected item - Microsoft Copilot Studio: When Copilot Studio calls a flow (V2) | Full | June 2, 2022 | August 25, 2022 |
| July 2022 | Enforce DLP policies on child flows | Enable the enforcement of DLP policies to include child flows. If a violation is found anywhere in the flow tree, the parent flow is suspended. After the child flow is edited and saved to remove the violation, the parent flows can be resaved or reactivated to run the DLP policy evaluation again. A change to no longer block child flows when the HTTP connector is blocked will roll out along with full enforcement of DLP policies on child flows. Once full enforcement is available, the enforcement includes child desktop flows. | Full | February 14, 2023 | March 2023 |
| January 2023 | Enforce DLP policies on child desktop flows | Enable the enforcement of DLP policies to include child desktop flows. If a violation is found anywhere in the flow tree, the desktop parent flow is suspended. After the child desktop flow is edited and saved to remove the violation, the parent desktop flows are automatically reactivated. | Full | - | August 2023 |
| October 2024 | Enforce [connector action control](https://learn.microsoft.com/en-us/power-platform/admin/connector-action-control) on triggers and internal actions | Expand enforcement of [connector action control](https://learn.microsoft.com/en-us/power-platform/admin/connector-action-control) to ensure that triggers and internal actions are covered. List them in Power Platform admin center and enforce blocking them if individually referenced in DLP policies or if the DLP policy doesn't include them as allowed. | Full | January 27, 2025 | February 10, 2025 |

*Availability schedule might change and depends on the rollout.

Suspended flows show as suspended in the Power Automate maker portal and the Power Platform admin center. When a flow is returned through an API, PowerShell, or the [Power Automate Management connector list flows "as Admin" action](https://learn.microsoft.com/en-us/connectors/flowmanagement/#list-flows-as-admin), the flow has **State=Suspended**, **FlowSuspensionReason=CompanyDlpViolation**, and a **FlowSuspensionTime** value indicating when the flow was suspended.

[Learn about DLP known issues](https://learn.microsoft.com/en-us/power-platform/admin/dlp-known-issues).

* [Power Platform DLP policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention)
* [Learn more about environments](https://learn.microsoft.com/en-us/power-automate/environments-overview-admin)
* [Learn more about Power Automate](https://learn.microsoft.com/en-us/power-automate/getting-started)
* [Learn more about the admin center](https://learn.microsoft.com/en-us/power-automate/admin-center-introduction)
