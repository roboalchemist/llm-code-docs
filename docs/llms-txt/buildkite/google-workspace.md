# Source: https://buildkite.com/docs/platform/sso/google-workspace.md

# Single sign-on with Google Workspace

Google Workspace (previously G Suite and Google Apps) can be used as an SSO provider for your Buildkite organization. To complete this tutorial, you will need admin privileges for Buildkite.

## Step 1. Create an SSO provider

In your [Buildkite organization **Settings**](https://buildkite.com/organizations/~/settings)' **Single Sign On** menu item, choose the Google G Suite provider:

<div style="max-width: 858px"><div class="responsive-image-container"><img alt="Screenshot of the Buildkite SSO Settings Page" src="/docs/assets/sso-settings-oR3nQgc8.png" /></div></div>

> 📘 You can also set up SSO providers manually with GraphQL.
> See the <a href="/docs/platform/sso/sso-setup-with-graphql">SSO Setup with GraphQL Guide</a> for detailed instructions and code samples.

## Step 2. Perform a test login

Follow the instructions to perform a test login. Performing a test login will verify that SSO is working correctly before you activate it for your organization members.

## Step 3. Enable the new SSO provider

Once you've performed a test login you can enable your provider. Activating SSO will not force a log out of existing users, but will cause all new or expired sessions to authorize through G Suite before organization data can be accessed.

If you need to edit or update your G Suite provider settings at any time, you will need to disable the provider first. For more information on disabling a provider, see the [disabling SSO](/docs/platform/sso#disabling-and-removing-sso) section of the SSO overview.

## SAML user attributes

<p>Buildkite accepts a subset of the SAML attributes from identity providers. The accepted attributes are:</p>

<table>
    <tr>
        <th>
            Attribute
        </th>
        <th>
            Description
        </th>
    </tr>
    <tr>
        <td>
            <code>admin</code>
        </td>
        <td>
            A boolean value that describes whether the user should be provisioned with admin permissions<br>
            <em>Example:</em> true
        </td>
    </tr>
    <tr>
        <td>
            <code>email</code>
        </td>
        <td>
            A string of the user's email address<br>
            <em>Example:</em> "person@company.com"
        </td>
    </tr>
    <tr>
        <td>
            <code>name</code>
        </td>
        <td>
            A string of the user's full name<br>
            <em>Example:</em> "Han Solo"
        </td>
    </tr>
    <tr>
        <td>
            <code>teams</code>
        </td>
        <td>
          A comma separated list of team UUIDs. A team's UUID can be found on the <em>Team Settings</em> page in Buildkite.<br>
          <em>Example:</em> <code>a1aaaa1a-b2bb-cccc-d4dd-aa2aaa6aaaaa,b5bbbbbb-3aaa-dd1d-aaa1-eee4eee6eeee</code>
        </td>
    </tr>
</table>

<p>When using the <code>teams</code> attribute, you can also specify roles. The <code>maintainer</code> or <code>member</code> role can be appended to the team UUID.</p>

<p>For example, the following code will specify the member role for the first team and the maintainer role for the second team:</p>
<div class="highlight"><pre class="highlight plaintext"><code>teams="b5bbbbbb-3aaa-dd1d-aaa1-eee4eee6eeee/member, a1aaaa1a-b2bb-cccc-d4dd-aa2aaa6aaaaa/maintainer"
</code></pre></div>
