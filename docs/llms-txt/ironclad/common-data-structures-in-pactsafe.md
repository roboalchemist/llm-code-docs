# Source: https://clickwrap-developer.ironcladapp.com/docs/common-data-structures-in-pactsafe.md

# Ironclad Clickwrap Terminology

Within Ironclad Clickwrap, there is a set of data structures to consider when interacting with the API that will help you formulate the ideal integration:

### Templates / Contract

* A contract managed within Ironclad Clickwrap
* Can have many versions that are drafted and published
* Has both a latest\_version and a published\_version (if a version has been published)

### Contract Version

* An instance of a template that is created as a draft, published, and timestamped by its publish or effective date
* Acceptances will be tied to a specific contract version and template

### Clickwraps / Clickwrap Groups

* "Container" for your contracts where you can manage visual and overall settings
* Can contain one or more contracts to present to an individual for review and acceptance

### Snapshot

* Screenshot of a webpage or application where a Clickwrap Group is embedded, that represents what a user was presented at time of acceptance.
* Can be captured manually or on an automated frequency

### Snapshot Location

* A specific container of snapshots that corresponds to the webpage or application where a Snapshot is taken
* Snapshot Location types include:
  * Desktop Web Browser
  * Mobile Web Browser
  * Native App

### Legal Centers

* A public web page to publicly host and display your legal Contracts. It maintains a version history of the Contracts that you've published and made available.

### Signer

* Any person or organization identified by any unique identifier (Signer ID) to your company that is accepting documents
* Can accept contracts via clickwrap through a series of events we call Activity .

### Activity

* An event that’s logged for a Signer against a given Contract Version and, optionally, a Group.
* Common types of events include:
  * Visited - An individual views a template in the Legal Center
  * Displayed - An individual viewed the full text of the clickwrap contract (usually by clicking on the link in the clickwrap)
  * Agreed - A specific `Signer` agreed to a clickwrap contract(s)
  * Disagreed (optional) - A specific `Signer` disagreed to a clickwrap contract(s).

### Sites

* An instance within your Account that holds Templates, Clickwrap Groups, etc.
* Sites can be configured as a Sandbox site or a Production site.

### Account

* All Signers, Contracts, and Activities live within a Site, which a Site lives within an Account
* An Account can have many Sites which act as a sub-tenant within your environment. One Site is your default, which controls how a Contract can be shared across an Account.