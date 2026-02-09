# Source: https://docs.sonarsource.com/sonarqube-cloud/architecture.md

# Architecture (Beta)

{% hint style="warning" %}
The features described on this page are in Beta stage, with support currently available for C#, Java, JavaScript, Python and TypeScript. See the [Product release lifecycle](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle) page for more information.
{% endhint %}

### Overview

Software Architecture is in most cases not managed in organizations/teams, and when it is managed, this is done manually. Teams tend to, consciously or unconsciously, leave their software architecture unattended, and this results in what is called architecture erosion, or structural technical debt.

Architecture erosion has 3 major impacts:

* It requires more work to make changes.
* It makes it harder to keep the impact of changes under control.
* It eventually leads to making the application impossible to change due to accumulated structural technical debt.

The increasing use of AI coding has accelerated this phenomenon.

To help prevent and reduce architecture erosion, SonarQube Cloud provides tools that allow you to:

* Visualize your current codebase architecture.
* Create an intended architecture.
* Raise architecture issues when flaws or deviation from the intended architecture are detected.
* Raise code issues for underlying architecture issues, as part of existing workflows (quality gate for example).

The Sonar Architecture features are located in the **Architecture** tab of the SonarQube Cloud UI.

### Concepts and terminology

#### Architecture

The architecture of an application is about how its physical and logical containers are organized and interconnected.

When dealing with architecture, there are 3 parts that need to be managed, in this order:

* Structure: How code is organized into a hierarchy of containers.
* Relationships: How containers depend on each other.
* Design: How containers interact with each other.

#### Current architecture

How code is *currently* organized into containers, and how these containers actually interact. Current architecture is automatically derived from the code.

#### Intended architecture

How code *should* be organized into containers, and how these containers should interact. Intended architecture is defined by tech leads.

#### Tangles

A tangle is a set of classes/files which are cyclically-dependent - that is, there is a path from every item to every other item in the tangle’s dependency graph. Tangles make code more complex and harder to understand and maintain.

#### Containers

In the context of code architecture, containers are units of code. Their relationships with other containers forms the architecture of your software.

### Roles, approach and workflow

Sonar Architecture provides a solution for documenting, maintaining, improving, transforming and evolving software architectures. It aims to engage not only technical leads, but also developers, and reduce structural technical debt by becoming part of the development process.

#### Roles

The Sonar solution recognizes that there are 2 distinct activities or roles involved in the definition and evolution of a software architecture. These are often (but not always) performed by different team members:

**Tech lead**

Person in the team who has the skills and legitimacy to make architectural decisions. A tech lead:

* Defines the [intended architecture](#intended-architecture).
* Sees the deviation between intended architecture and current architecture.
* Reviews flaws in the current architecture and suggests solutions for fixing them.

**Developer**

Person who makes code changes to the project on a daily basis. A developer:

* Has access to the intended architecture defined by tech leads.
* Makes sure no deviations are introduced in the code.
* Follows architectural recommendations.

#### Approach

Sonar has a divide to conquer approach, decoupling the multiple dimensions of architecture:

1. **Comprehend current architecture:** Enable human and AI stakeholders to understand the current architecture, with a live reference point.
2. **Formalize intended architecture**: Enable tech leads to define the intended architecture, to be enforced, easily and incrementally. The model is usable by AI, for example by providing it as context in a request.
3. **Prioritize architectural problems**: Enable tech leads to get a clear view of architectural issues, with clear priorities.
4. **Make structural problems actionable**: Leverage SonarQube to stop human or AI from further eroding the architecture, and divide the remediation of existing problems into smaller actionable actions for developers and/or AI.

#### Workflow

Sonar provides a complete workflow which ensures that:

* The whole team understands the current architecture, and the evolving intended architecture.
* Tech leads can incrementally formalize architectural decisions.

Architectural decisions that imply code changes raise [SonarQube issues](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/introduction) that can be resolved by developers.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-fc6836afd0f4587184b5659c16a9c507a31d200b%2Farchitecture-workflow.png?alt=media" alt=""><figcaption></figcaption></figure>

Without action from tech leads, no SonarQube issues are raised.

### How to use Sonar Architecture

The process is driven by the tech leads who:

1. Understand the [current architecture](#current-architecture).
2. Define the [intended architecture](#intended-architecture) to constrain the most important structure and relationships, by starting at the top-level and working down into the structure. The intended architecture will be compared to the current architecture to raise architecture deviation issues during analysis.
3. Review flaws in the current structure automatically identified by SonarQuble, and make suggestions for repairs.
4. Iteratively evolve and extend the intended architecture as the code and priorities change.

As a developer, your role is to:

1. Fix the [code issues](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues) that are raised by SonarQube following tech lead input.
2. Explore the evolving intended architecture to ensure compliance as you add or modify code, and when addressing raised SonarQube issues.
3. Explore the current architecture to refresh your understanding of the project topology, and to gain insights for specific tasks.

#### Viewing the current architecture

SonarQube Cloud provides an interactive visual map to explore the structure and relationships within your codebase.

The map allows you to:

* Understand the current topology of the project.
* Navigate to understand the map in more or less detail.
* Focus on the relationships of a specific container.

There is no special setup or input needed to view and use the map. It is automatically updated after each analysis so it is always up to date.

**How to read the map**

To access the current architecture map, go to **Architecture** > **Open structure map**.

Classes/files are recursively grouped within their packages/folders/modules. The size of containers generally reflects the number of underlying containers, but the white space inside a container also characterizes it.

In every container (also true for top level containers), sub-containers are levelized, which means they are organized as follows:

* Containers that have no outgoing relationships are located on the right.
* Every container in a column has at least one dependency on the next column on the right.
* Containers in a column have no dependencies between themselves.

This means that relationships will generally flow from left to right. This conveys the flow of relationships without showing all the specific relationships.

To display direct relationships to/from selected containers, click on the container.

**How to use the map**

To explore the map, just pan, zoom and click:

* Zoom to see more or less detail.
* Select any item at any level to see its relationships.
* Pan across the map or zoom out to see regions or relationships that are off-screen.

#### Creating an intended architecture

You can create and update a visual model that expresses the intended structure and relationships within your codebase. This intended architecture will serve as the reference: during analysis, deviation issues are raised when the intended architecture and current architecture don’t match.

The intended architecture editor lets you:

* Formalize the structure and relationships in a way that is straightforward and incremental: you can stop at any point in time.
* Decide which containers should be inspected, as SonarQube inspects them only once they are added to the intended architecture.
* Define a structure using a top-down approach.

Note that to create the intended architecture, you only define allowed relationships between sibling containers. Relationships are inherited by sub-containers.

All the above tasks require the **Administer project** permissions. See [Setting user permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions) for more information.

#### How to use the intended architecture editor

To access the intended architecture editor, go to **Architecture** > **Intended architecture**.

Your goal is to define the structure and relationships in your code.

* Structure: Which containers you care about, and where they should be located.
* Relationships: How should the containers in the model depend on any of their peers in the model.

Starting at the top-level of your structure, add the containers and sub-containers that you most care about. Additionally, containers may:

* Be placeholders for for code that does not exist.

and/or

* Map to code currently at a location that is different to the model location, that should be moved to the model location.

Every time you add a container to the model, you should immediately define the allowed relationships to its siblings to keep the model complete. Indeed, any non-defined dependency between siblings will be considered as forbidden.

You can follow your progress by looking at the treeview on the left. Every time you add a container to the map, the corresponding containers in the treeview are grayed out.

You can stop at any time, and start again. You should expect to regularly modify the intended architecture as the codebase evolves.

{% hint style="success" %}
Remember to click **Save** so that your updated model is picked up and used by the next analysis.
{% endhint %}

### Architecture issues

Issues in the current architecture are detected automatically during the project analysis. The scope of issues will depend upon the intended architecture provided, issues are made of a mix of flaws and deviations.

#### Understanding architecture issues

* If you have not defined an intended architecture, only architectural flaws will be detected. At this stage, flaws are made only of tangles.
* If you have defined an intended architecture, analysis will also raise issues from architectural deviations, i.e. differences between current and intended architecture. At this stage, SonarQube can detect 2 types of deviations: wrong dependencies and wrong locations.
* For each type of issue, you will get a list of issues, ordered by priority.
* For tangles, you will get a visual representation of the issue and be able to instruct developers how to solve the issue.

#### Fixing architecture issues

When you review the list of issues:

* For deviations, make sure that they are in line with your intention.
* For flaws (tangles at this stage), pick the ones you wish to solve, review them and provide instructions to developers by selecting the undesirable relationships. The next analysis will raise code issues when these relationships are detected.
