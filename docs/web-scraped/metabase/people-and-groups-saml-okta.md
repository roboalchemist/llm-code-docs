# Source: https://www.metabase.com/docs/latest/people-and-groups/saml-okta

<div>

1.  [Home](/docs/latest/)
2.  [People and Groups](/docs/latest/people-and-groups/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# SAML with Okta

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Okta SAML authentication is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

1.  [Turn on SAML-based SSO in Metabase](#turn-on-saml-based-sso-in-metabase)
2.  [Set up SAML in Okta](#set-up-saml-in-okta).
3.  [Set up SAML up in Metabase](#set-up-saml-in-metabase).

You can also optionally [configure group mappings](#configure-group-mappings) to automatically assign Okta users to Metabase groups.

See [authenticating with SAML](./authenticating-with-saml) for general SAML info.

## Turn on SAML-based SSO in Metabase

In the **Admin**\>**Settings** section of the Admin area, go to the **Authentication** tab and click on **Set up** under **SAML**.

You'll see a SAML configuration form like this:

![SAML form](images/saml-form.png)

You'll need to use the information in this form to set up SAML in Okta.

## Set up SAML in Okta

Before configuring SAML authentication in Metabase, you'll need to create a new SAML app integration in Okta.

### Create an app integration in Okta

From the Okta **Admin** console, [create a new SAML app integration](https://help.okta.com/oie/en-us/content/topics/apps/apps_app_integration_wizard_saml.htm) to use with Metabase.

### Configure Okta SAML settings

To configure Okta app integration with Metabase, you'll need to use the information found in Metabase in the **Admin panel** \> **Authentication** \> **SAML** section.

#### General settings

  Okta SAML                         Metabase SAML
  --------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Single sign-on URL**            **URL the IdP should redirect to**. This is your Metabase [Site URL](../configuring-metabase/settings#site-url) -- it should start with `https://` and end with `/auth/sso`.
  **Audience URI (SP Entity ID)**   **SAML Application Name** ("Metabase" by default)

#### Attribute statements

In the **Attribute statements (optional)** section of the Okta application SAML setting, create the following attribute statements:

-   email address
-   first name (given name)
-   last name (surname)

Even though Okta says these are optional, Metabase requires them. Okta will pass these attributes to Metabase during authentication to automatically log people in to Metabase.

  Name                                                                                                           Value
  -------------------------------------------------------------------------------------------------------------- ----------------
  `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`   user.email
  `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`      user.firstName
  `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`        user.lastName

The names of attribute statement in Okta should match the attribute names in Metabase (names are case sensitive). If you want to use non-default attribute names in you Okta app configuration, you will also need to change the names for the attribute fields in Metabase in **Admin panel** \> **Authentication** \> **SAML**.

> **Make sure that people [cannot edit their email address attribute](https://help.okta.com/oie/en-us/content/topics/users-groups-profiles/usgp-user-edit-attributes.htm)**. To log people in to your Metabase (or to create a Metabase account on first login), your IdP will pass the email address attribute to Metabase. If a person can change the email address attribute, they'll potentially be able to access Metabase accounts other than their own.

### Example of an Okta assertion

You can click **Preview SAML assertion** to view the XML file generated by Okta. It should look something like this:

``` highlight
<saml2:Assertion
    xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion" ID="id4170618837332381492734749" IssueInstant="2019-03-27T17:56:11.067Z" Version="2.0">
    <saml2:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">http://www.okta.com/Issuer</saml2:Issuer>
    <saml2:Subject>
        <saml2:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">userName</saml2:NameID>
        <saml2:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
            <saml2:SubjectConfirmationData NotOnOrAfter="2019-03-27T18:01:11.246Z" Recipient="https://metabase.mycompany.com/auth/sso"/>
        </saml2:SubjectConfirmation>
    </saml2:Subject>
    <saml2:Conditions NotBefore="2019-03-27T17:51:11.246Z" NotOnOrAfter="2019-03-27T18:01:11.246Z">
        <saml2:AudienceRestriction>
            <saml2:Audience>my-metabase-app</saml2:Audience>
        </saml2:AudienceRestriction>
    </saml2:Conditions>
    <saml2:AuthnStatement AuthnInstant="2019-03-27T17:56:11.067Z">
        <saml2:AuthnContext>
            <saml2:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml2:AuthnContextClassRef>
        </saml2:AuthnContext>
    </saml2:AuthnStatement>
    <saml2:AttributeStatement>
        <saml2:Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
            <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
              Cam
            </saml2:AttributeValue>
        </saml2:Attribute>
        <saml2:Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
            <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
              Saul
            </saml2:AttributeValue>
        </saml2:Attribute>
        <saml2:Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
            <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
              cam@metabase.com
            </saml2:AttributeValue>
        </saml2:Attribute>
    </saml2:AttributeStatement>
</saml2:Assertion>
```

## Set up SAML in Metabase

Once you set up your SAML app in Okta, you'll need to configure SAML in Metabase. You'll need some information from Okta:

1.  In Okta, go to the page for your Metabase app integration.
2.  Go to the **Sign On** tab.
3.  Click on **View SAML setup instructions**.

Use the information from Okta SAML instructions to fill the Metabase SAML form in **Admin panel** \> **Authentication** \> **SAML**:

  Metabase SAML                        Okta SAML
  ------------------------------------ --------------------------------------
  SAML Identity Provider URL           Identity Provider Single Sign-On URL
  SAML Identity Provider Certificate   X.509 Certificate\*
  SAML Identity Provider Issuer        Identity Provider Issuer

\*Make sure to include any header and footer comments, like `---BEGIN CERTIFICATE---` and `---END CERTIFICATE---`.

## Configure group mappings

You can configure Metabase to automatically assign people to Metabase groups when they log in. You'll need to create a SAML attribute statement that will pass the groups information to Metabase, and then configure Metabase to read this attribute and map its contents to Metabase groups.

You can use either:

-   [A custom user profile attribute](#use-a-user-profile-attribute-to-assign-groups) that contains user's Metabase groups.
-   [Okta User Groups](#map-okta-user-groups-to-metabase-groups).

### Use a user profile attribute to assign groups

You can create a custom user profile attribute and fill it with the Metabase groups for each user.

1.  In Okta **Profile Editor**, [create a new User Profile attribute](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-add-custom-user-attributes.htm) called `metabaseGroups`, which can be a `string` or a `string array`. ![New User Profile attribute](images/okta-new-attribute.png)

2.  For each user in Okta, fill the `metabaseGroups` attribute with their Metabase group(s).

    ![Metabase groups attribute](images/okta-adding-groups.png)

    We recommend that you use the same names for the groups in Okta as you would use in Metabase.

    Metabase groups don't have to correspond to Okta User Groups. If you'd like to use Okta User Groups to set up Metabase Groups, see [Map Okta User Groups to Metabase groups](#map-okta-user-groups-to-metabase-groups).

    > Your Okta account has to have `SAML_SUPPORT_ARRAY_ATTRIBUTES` enabled, as Metabase expects Okta to pass attributes as an array. If your Okta account is old, you might need to reach out to Okta support to enable `SAML_SUPPORT_ARRAY_ATTRIBUTES`.

3.  In the **Okta SAML settings** for the Metabase app integration, add a new attribute statement `MetabaseGroupName` with the value `user.metabaseGroups` (the profile attribute you just created)

    ![New attribute statement referencing the attribute](images/okta-new-attribute-custom.png)

4.  In **Metabase SAML settings**:

-   Turn on **Synchronize Group Memberships**.

-   For each of the groups you added to Okta users, set up a new mapping to a Metabase group.

-   In **Group attribute name**, enter `MetabaseGroupName` (the name of the SAML attribute statement).

    ![Metabase group mapping](images/saml-okta-groups.png)

### Map Okta User Groups to Metabase groups

1.  Create Okta User groups corresponding to Metabase groups and assign them to Okta users.

2.  In Okta's **SAML Settings** for the Metabase app integration, add a new attribute statement `MetabaseGroupName`, set the type to "Basic", and the value to:

    ::: 
    ::: highlight
    ``` highlight
    Arrays.flatten(getFilteredGroups(, "group.name", 100))
    ```
    :::
    :::

    where the Group IDs in `` are the groups that you would like to map to Metabase groups. You can find the Okta Group ID in the URL of the group's page: `https://your-okta-url.okta.com/admin/group/GROUP_ID`.

    This expression will retrieve the names of Okta User Groups that a user is a part of and return them as an array.

    ![New attribute statement for groups](images/okta-group-attribute.png)

    > Your Okta account has to have `SAML_SUPPORT_ARRAY_ATTRIBUTES` enabled, as Metabase expects Okta to pass attributes as an array. If your Okta account is old, you might need to reach out to Okta support to enable `SAML_SUPPORT_ARRAY_ATTRIBUTES`.

    Next, you'll need to tell Metabase how to map Okta groups to Metabase groups.

3.  In **Metabase SAML settings**:

-   Turn on **Synchronize Group Memberships**.

-   For each of the groups you added to Okta users, set up a new mapping to a Metabase group.

-   In **Group attribute name**, enter `MetabaseGroupName` (the name of the SAML attribute statement).

    ![Metabase group mapping](images/saml-okta-groups.png)

## Troubleshooting SAML issues

For common issues, go to [Troubleshooting SAML](../troubleshooting-guide/saml).

## Further reading

-   [User provisioning](./user-provisioning)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/people-and-groups/saml-okta.md) ]