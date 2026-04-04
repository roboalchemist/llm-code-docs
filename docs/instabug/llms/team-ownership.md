# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/automation-and-workflows/team-ownership.md

# Team ownership

To set up team ownership in the Luciq dashboard, you will need to go through a couple of steps. Team ownership will help ensure every crash and bug gets assigned to the corresponding team. Assignment can be done either manually or automatically. These steps will ensure you create the best possible team definitions. It will enable you to then prioritize issues related to your team and get alerted about them. These are the quick few steps needed to complete team ownership on the dashboard

1. Team Creation
2. Team Assignment
   * Automatic Approach which is done through Team Definition
   * Manual Approach
3. Prioritization
4. Alerting
5. Team Performance Dashboard

### Team Creation

The first step of team ownership is creating the team using the following steps.

To create a team, you will go through “Account management” (on the organizational level) at the top right corner of the dashboard

<figure><img src="https://files.readme.io/65962bdeb9b45d0869e2c4515251227cc2e221e31aeb6910f85258de7ac2ff31-image.png" alt=""><figcaption></figcaption></figure>

Then, from the left list choose “Teams”, then “Create a team”

<figure><img src="https://files.readme.io/00c6b4eccb5e9a92734804a0b18b65d014a1926e496fa1935a78e4a4d8978384-image.png" alt=""><figcaption></figcaption></figure>

Choose the most suitable Team name, example "Payment"

<figure><img src="https://files.readme.io/9127128f62c57540755e4ae8f4ad5047af6756ac4d46dca9392373dfdcae346c-image.png" alt=""><figcaption></figcaption></figure>

### Team Assignment <a href="#team-assignment" id="team-assignment"></a>

#### Automatic Assignment to Corresponding Teams

* **Assign Ownership Type:**
  * **Bugs**: Define teams based on categories, user attributes, and current view (screen name).
  * **Crashes**: Use path/package or filename to assign ownership.
  * **Screen loading, UI hangs, App Launch**: Assign teams based on screen names.
  * **Networks**: Assign teams based on the URL.

To define the team, you will need to go to “Settings” (on the app level) from the bottom of the sidebar (on the left)

Then, choose “Team ownership”, then "Create Definition"

<figure><img src="https://files.readme.io/9047758885c456eaf691736f09c2c68c4d973a452e8f0f9f78dc07d0545a4106-image.png" alt=""><figcaption></figcaption></figure>

Choose the **Type** that you want to define team ownership for.

<figure><img src="https://files.readme.io/7f9c3bbb77124ddf759405382d8b296a1fd3e965178e41bce08d83dba6b5979b-image.png" alt=""><figcaption></figcaption></figure>

#### Automatically Assigning Bugs to the Corresponding Team

Choose the team that you created. For example, “Payment” Team

<figure><img src="https://files.readme.io/58afa7575d95dcc5674eecb898dc5669f407adcbdbcf8a798d2efd103657d736-image.png" alt=""><figcaption></figcaption></figure>

Start adding conditions to define the team by choosing from the following:

* Categories
* User Attributes
* Current View

<figure><img src="https://files.readme.io/b9f36e25f58be04b618bb061bc8170e98ef141ae943fe9075a60abb9ed5e04b7-image.png" alt=""><figcaption></figcaption></figure>

#### Automatically Assigning Crashes to the Corresponding Team

And now defining the **Payment** team that is responsible for Crashes

<figure><img src="https://files.readme.io/6d92fadc473de9403f2a0efae4a2df4e45f9a5b947e1cf9fcd8b835851ba6838-image.png" alt=""><figcaption></figcaption></figure>

Start adding conditions to define the team by choosing from the following:

* Path (iOS)/Package (Android)
* Filename

<figure><img src="https://files.readme.io/cd711115ad791248e68f9b83f40fbcb64090d1e5e35b3ecfd610bd8e1e20c21c-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}

#### Path/Package or Filename

NOTE: Whenever you type the path/package you need to press Enter in order to lock it in
{% endhint %}

#### **Matching Paths/Packages**

**iOS**

When setting up the definition, Luciq supports partial matching of paths using the **match** condition (not case sensitive), let's take a look at some examples:

**Sample Crash**

Actual Crash Path: luciq/crashes/list/singleCrash

| Successful Match                                                                                                                                                | Unsuccessful Match                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>luciq</li><li>luciq/crashes</li><li>luciq/crashes/list/singleCrash</li><li>luciq/crashes/list</li><li>/crashes/list</li><li>/list/singleCrash</li></ul> | <ul><li>luciq//crashes</li><li>/luciq/crashes</li><li>/luciq/crashes/list/singleCrash/</li><li>luciq/crashes/list/singleCrash/Occurrence</li><li>luciq/cr/list</li><li>crashes/luciq</li></ul> |

**Unsuccessful Matches:**

* luciq//crashes - *contains an extra slash in the middle*
* /luciq/crashes - *contains an extra slash before luciq*
* com/luciq/crashes/list/singleCrash/ - *contains an extra slash after singleCrash*
* luciq/crashes/list/singleCrash/Occurrence - *contains an extra sub-path*
* luciq/cr/list - *Luciq does not match partial words (cr and crashes in this case)*
* crashes/luciq - *path is written in a wrong order*

**Android**

When setting up the definition, Luciq supports partial matching of package names using the **match** condition (not case sensitive), let's take a look at some examples:

**Sample Crash**

Sample Package: com.luciq.crashes.list.singleCrash

| Successful Match                                                                                                                                           | Unsuccessful Match                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>luciq</li><li>com.luciq.crashes</li><li>com.luciq.crashes.list</li><li>luciq.crashes.list</li><li>.crashes.list</li><li>list.singleCrash</li></ul> | <ul><li>com..luciq.crashes</li><li>.com.luciq.crashes</li><li>com.luciq.crashes.list.singleCrash.</li><li>crashes.list.singleCrash.Occurrence</li><li>luciq.cr.list</li><li>crashes.luciq</li></ul> |

**Unsuccessful Matches:**

* com..luciq.crashes - *contains an extra dot in the middle*
* .com.luciq.crashes - *contains an extra dot before com*
* com.luciq.crashes.list.singleCrash. - *contains an extra dot after singleCrash*
* crashes.list.singleCrash.Occurrence - *actual path does not contain 'Occurrence'*
* luciq.cr.list - *Luciq does not match partial words (cr and crashes in this case)*

#### Automatically Assigning Performance Metrics to the Corresponding Team

And now defining the **Screen loading, UI hangs, and App Launches** that the payments team is responsible for:

Choose the **“Screen loading, UI hangs, and App Launches”** type, then choose the payments team.

<figure><img src="https://files.readme.io/a6258c8f5a60a971ea1cec8316188153e3d52180a91cc60fa7be3b8146dac806-image.png" alt=""><figcaption></figcaption></figure>

Start adding conditions by choosing the **Screen Names** your team is responsible for

<figure><img src="https://files.readme.io/b12a15d2857cad767599a79687576c852d167158f21c9f34ad178733d427a25a-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}

#### Screen Name Assignment

For **Screen loading, UI hangs, and App Launch**, the same team can be assigned to multiple screen names, but the same screen cannot be assigned to multiple teams.
{% endhint %}

### Manual Assignment to Corresponding Teams

#### Manually Assigning Bugs to the Corresponding Team

You can also assign the team manually from within the bug itself without defining it.

Go to bugs from the left sidebar of the dashboard and then click on the bug that you want to assign to a certain team

Navigate to the right sidebar “Actions” and change the Team to the corresponding team. For example, choosing the “Payment”

<figure><img src="https://files.readme.io/4fbc7441352fa9bd244c41d0366828213b0e714716134976a7780feff14c30f0-image.png" alt=""><figcaption></figcaption></figure>

#### Manually Assigning Crashes to the Corresponding Team

You can also assign the team manually from within the crash itself without defining it.

Go to crashes from the left sidebar of the dashboard and then click on the crash that does not have a team assigned to it

<figure><img src="https://files.readme.io/990830d38a82c672bc6dff92a182e573c415cb317d6876d2d050b8140d92db9f-image.png" alt=""><figcaption></figcaption></figure>

Navigate to the right sidebar “Actions” and change the Team to the corresponding team. For example, choosing the “Payment”

<figure><img src="https://files.readme.io/45395cfde156d667fe6f198e99d83aa8924843cfb326807c385860471557f939-image.png" alt=""><figcaption></figcaption></figure>

### Prioritizing

#### Bugs Prioritization

Prioritizing bugs related to your team can be done through the Team filter at the top bar of the "Bugs" main page\
Select your team from the dropdown list, you can even search by the team’s name. For example, “Payment” Team

<figure><img src="https://files.readme.io/250e776e003c784bbd7575f2de96a61424abea01f9624e59ba0e0376f17df746-image.png" alt=""><figcaption></figcaption></figure>

As you can see below, you can prioritize the bugs related to your team only and get more granular with the options to filter. For example, Payment team wants to focus on *bugs status' new or in-progress*. Also, you will be able to save those filters and you can access them from the right side of the filter bar.

<figure><img src="https://files.readme.io/b7155213f66caee1d302e5b14e6460eb2219f06bfc39bbfc36e55ee20fc7304a-image.png" alt=""><figcaption></figcaption></figure>

### Crash Prioritization

Prioritizing crashes related to your team can be done through the Team filter at the top bar of the "Crashes" main page.

Select your team from the dropdown list, you can even search by the team’s name.&#x20;

For example, “Payment” Team

<figure><img src="https://files.readme.io/b6a8d985c5167edca38397d25a4acfe58cebe5765aaddb4d4f4f2e1f1d93b6a1-image.png" alt=""><figcaption></figcaption></figure>

As you can see below, you can prioritize the crashes related to your team only and get more granular with the options to filter. For example, Payment Team wants to focus on *crashes seen in a certain app version*. Also, you will be able to save those filters and you can access them from the right side of the filter bar.

<figure><img src="https://files.readme.io/c1eca471c1bc86298c4004b44e8a8536a2f00426cea9751f9503f1f302ac6516-image.png" alt=""><figcaption></figcaption></figure>

### Alerting

If you’d like to get alerted as soon as you receive any crash related to your Team, you will be able to do that through our “Alerts and Rules” engine.

Go to “Alerts and Rules” and "Create" a new Alert

**Use Case**:

* Regressing crash assigned to team “Payment”
* Choose the condition (Regression) you want to be alerted to whenever it is assigned to “Payment” team

<figure><img src="https://files.readme.io/aabe857ec8bfabcff2a30d605e14e0d449a43e12c91cb44aa0fdb6102a0444c8-image.png" alt=""><figcaption></figcaption></figure>

**For more details on the different use cases of Alerting, please refer to** [**Alerts & Rules**](https://docs.luciq.ai/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules) **product guides.**

Then, Forward it to your favorite tool (Ex: Slack, MS Teams, PagerDuty, … etc). Thus, Payment Team will be notified about this regression through that tool.

<figure><img src="https://files.readme.io/93ebb2ddbc9cca6c6da2d60403e45fa9a61d62976695a6a86d55986d7e393be0-image.png" alt=""><figcaption></figcaption></figure>

**For more details on the different integrations that is supported, please refer to** [**Luciq's Integrations Docs**](https://docs.luciq.ai/product-guides-and-integrations/integrations)

You can assign this Alert/Rule to a certain team through "Owned by" section at the bottom of the rule. This enables you to figure out who to contact if there was a problem with any of the Alerts/Rules

<figure><img src="https://files.readme.io/b22edd50bed7165186cb1ec14e093364f8e6e1dc0172bd0f38e6de978ce43f65-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}

#### Unassigned Rules

If the Alert/Rule does not have a team assigned to it, then by default the value will be **Unassigned**
{% endhint %}
