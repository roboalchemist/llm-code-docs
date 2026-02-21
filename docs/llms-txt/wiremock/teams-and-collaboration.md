# Source: https://docs.wiremock.io/security/teams-and-collaboration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Teams and Collaboration

> Working with teams & sharing Mock APIs in WireMock Cloud

The basic unit of ownership in WireMock Cloud is the Organisation. Mock APIs,
users and teams all belong to a single organisation. View your organisation by
clicking on the [Organisation page](https://app.wiremock.cloud/account/organisation) under your account.

Here you will see all the teams and users in your organisation:

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/organisation.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=02c299fc174294879d2f287f7a40fd7d" title="Organisation details" data-og-width="1190" width="1190" data-og-height="1098" height="1098" data-path="images/screenshots/organisation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/organisation.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=fe406b11a52815a366533d9b48da1b2e 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/organisation.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=cbf67d1aa3ff53d5d1ad1b773615d0a5 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/organisation.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=59cbd1d085a2e898c39d3e2847f15150 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/organisation.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=dacf54fe8dc6690ad9767d602b0b416b 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/organisation.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=7ff6ec9266a6a2d0421cee3417f7e711 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/organisation.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=bc8b88d3a6e0c25f0310c7e7a61ef038 2500w" />

There are two roles for users in an organisation: **Member** and **Admin**.

A **Member** can create and interact with mock APIs, API templates and teams.

In addition an **Admin** can:

* invite other users to the organisation
* remove users from the organisation (provided at least one Admin remains)
* change the role of any member of the organisation (provided at least one Admin
  remains)
* administer all mock APIs, teams and other resources belonging to the
  organisation

### Inviting users

An admin can enter the email address of a person not yet in the organisation,
and a role, to invite that person to join the organisation. They will then show
up in the "Pending Invites" section.

Organisation members and pending invitations count towards your subscription plan's total number
of seats. You can see your usage and limits on the [Usage page](https://app.wiremock.cloud/account/usage) under your account.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/usage.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0389c718a8ebde933c54b78c6d63c533" title="Subscription plan usage" data-og-width="842" width="842" data-og-height="1041" height="1041" data-path="images/screenshots/usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/usage.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=af6d25a3fe23bb12eca24a20cb3a5c2c 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/usage.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=46a1ed75259aa30832c9466130832048 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/usage.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=c3ecf73743ed5672a0acf5aa6de67e48 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/usage.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5466d0823a64a70668a2a763876c3cb5 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/usage.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ff705c36a5b4a85efcbb987db687baf8 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/usage.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=d348c5da1e91841ea66d7b8b156b4e33 2500w" />

## Teams

Any member of an organisation can create a team (provided the organisation is on
a plan which allows multiple members).

The person who creates the Team will automatically be given the Admin
role on that team. In addition all organisation admins can administer a team.

There are two roles for users in a team: **Member** and **Admin**.

A **Member** will inherit whatever permissions the team has been granted.

In addition an **Admin** can:

* add other members of the organisation to the team
* remove users from the team
* change the role of any member of the team

An organisation admin can enter the email address of a person not yet in the
organisation, and a role, to simultaneously invite that person to join the
organisation *and* add them to the team.

## Mock APIs

Any member of an organisation can create a mock API.

The person who creates the mock API will automatically be given the Admin
role on that mock API. In addition all organisation admins can administer a mock
API.

Mock APIs can be shared with other members of your organisation by clicking the
"Share" button on the API:

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/share-mock-api.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0fc061864027a812c6a538fb2c28723b" title="Share Mock API with others" data-og-width="786" width="786" data-og-height="416" height="416" data-path="images/screenshots/share-mock-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/share-mock-api.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a9290ac6a35b5c2be5b615ccea278283 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/share-mock-api.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=8cdbe1428803826746f50b2f8be041c7 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/share-mock-api.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=05b4b41b045218033f31371d0fbb8dbb 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/share-mock-api.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=421b75cf10ee32f2a42e6e5d9dc5956d 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/share-mock-api.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=85a727c0012efb62895862a9cda2fad3 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/share-mock-api.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=2ab7ceded8e23165e86f2fab3ce6ed3a 2500w" />

Mock APIs can be shared with "All in organisation", any of the Teams
belonging to the same organisation as the mock API, and any individual members of the organisation.

When sharing a mock API, you can choose the role of the organisation, team or
person you are sharing the API with as one of **Admin**, **Write** or **Read**.

* **Read** allows: viewing the API, its stubs, and who else has permissions on it.

* **Write** also allows changing the settings of the API, and adding, changing or
  deleting the stubs on the API.

* **Admin** also allows deleting the mock API, and adding & removing people, teams & the organisation, or
  changing their roles, in the "Share" widget.

An organisation admin can enter the email address of a person not yet in the
organisation, and a role, to simultaneously invite that person to join the
organisation *and* give them that role on the mock API.

## Single Sign-on (SSO)

WireMock Cloud supports auto-provisioning and SSO for user management via any SAML 2.x capable IdP.
