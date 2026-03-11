# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/multilingual-support.md

# Multilingual Support

Enate Work Manager supports the following languages:

1. English (British)
2. English (US)
3. French
4. German
5. Romanian
6. Hungarian
7. Polish
8. Spanish
9. Portuguese Brazilian
10. Russian

The Operations environment for end users to deliver the service fully supports these languages and each user will be allowed to choose their preferred language along with date-time pattern in their user profile settings.

To set a preferred language, select a language from the Language dropdown list in User Settings.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCCjQMZrIXW_c-JAut%2F-MZCWE2H20vuRKMcEY_D%2FChange-Language.gif?alt=media\&token=112e24b6-1177-4eba-8d46-043d1fae0317)

The display of labels will appear in the logged-on user’s preferred language - this is achieved by adding a ‘language package’ into **Enate**. Each language package will have mapping for user-specific language like Portuguese, for example, ‘**Queue**’ will be ‘**Fila’** and ‘**Action’** will be ‘**Açao’** in Portuguese.

Here is the list of UI elements which will be available in the logged-on user’s preferred language:

| Item               | Details                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Home Page          | <ol><li>RAG filters</li><li>My Team</li><li>Bot Farm</li><li>Queue</li><li>Chart</li><li>Grids and column settings</li></ol><p>Same behaviour in Inbox page as well.</p> |
| Quick Find         | People, Comms and work items search                                                                                                                                      |
| Queue Page         |                                                                                                                                                                          |
| Navigation Links   | Link to Builder, Queue Page or recent accessed work items etc.                                                                                                           |
| User Profile Page  | Here user can also change preferred language along with datetime pattern.                                                                                                |
| Call Handling Page | This page shows all communications and work items related to individual users                                                                                            |
| Work item UI       | Labels and Button like Category picker, state etc.                                                                                                                       |

{% hint style="info" %}
Note – Real names such as customer names and usernames will be remained in the original language, as entered by the configurers in Builder.
{% endhint %}

## Data entered by Work Manager End Users <a href="#data-entered-by-work-manager-end-users" id="data-entered-by-work-manager-end-users"></a>

Enate fully supports a User’s preferred language in Work Manager display and UI elements including labels, links and buttons, however anything added by you will stay in same language you originally entered it in and will not be auto-translated into any other language when being viewed by other users with a different preferred language.

For example, if a Brazilian user adds a note to a Case in Portuguese, Enate will then save the note in Portuguese in the database and will only ever show the note in Portuguese.

Here is full list of items which will be driven by user input and which **WILL NOT** be auto translated by the product:

| Item               | Detail                                                                                                                                                                                                                                                     |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Case               | <p></p><ol><li>Notes</li><li>Emails</li><li>Case - short description/title</li><li>Override Action instruction o new Action launched by end user</li></ol>                                                                                                 |
| Action             | <p></p><ol><li>Notes</li><li>Emails</li><li>Checklist comments</li><li>Action State- 'Unable to complete' reason text</li><li>Override Action Instruction of new Action launched by end user</li><li>Action Peer Review note entered by reviewer</li></ol> |
| Ticket             | <p></p><ol><li>Title and description of new child Tickets</li><li>Name of new Action launched by user</li><li>Name of new Case launched by user</li></ol>                                                                                                  |
| Contact            | Details about contact like address.                                                                                                                                                                                                                        |
| Files              | File name and note about file                                                                                                                                                                                                                              |
| Defect             | Defect description                                                                                                                                                                                                                                         |
| Reassignment Notes | Text entered by user while reassigning a piece of work to another teammate.                                                                                                                                                                                |

### Custom Data and Cards <a href="#custom-data-and-cards" id="custom-data-and-cards"></a>

The initial releases of multilingual functionality will not support configurers defining multiple languages when creating Custom Data and Smart Cards in Builder. Multiple cards and data items would be required for this.

### In App Notifications <a href="#in-app-notifications" id="in-app-notifications"></a>

The initial releases of multilingual functionality will not support notifications in languages other than English.
