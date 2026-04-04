# Source: https://uptrace.dev/raw/features/sso/keycloak.md

# Keycloak Single Sign-On

> Deploy Keycloak and configure OpenID Connect SSO with Uptrace using realms, clients, redirect URIs, and client credentials.

[Keycloak](https://www.keycloak.org/) is an open-source identity and access management solution that<br />


supports OpenID Connect, SAML 2.0, and OAuth 2.0. You can also use Keycloak to connect to existing<br />


user directories such as LDAP and Active Directory.

Single Sign-On allows you to manage users using OIDC providers. After logging in, such users are<br />


automatically added to a team and can access team projects. When users are removed from Keycloak,<br />


they automatically lose granted access in Uptrace.

## Step 1. Create OIDC SSO in Uptrace

1. In Uptrace, go to **Organization** -> **Single Sign-On**
2. Click **New SSO** -> **New OIDC**
3. Fill out the form:
  - **Domain**: your unique domain name (can be any string; it will be used later during the sign-in<br />
  
  
  process)
  - **User team**: select the team that will be automatically assigned to new users
  - **User role**: select the role that will be automatically assigned to new users

![OIDC](/features/keycloak/new-oidc.png)

1. Click **Create** and you will be presented with a redirect URL to configure Keycloak

Leave this form open â you will need to enter the **Client ID** and **Client Secret** from Keycloak<br />


to finish the setup.

## Step 2. Run Keycloak

Start Keycloak in development mode using Docker:

```shell
docker run --name keycloak --rm -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak:26 start-dev
```

<alert type="warning">

The `start-dev` command runs Keycloak in development mode without HTTPS. For production deployments, see the [Keycloak Server Installation Guide](https://www.keycloak.org/guides#getting-started) to configure TLS and a database.

</alert>

## Step 3. Log in to Keycloak admin console

1. Open [http://localhost:8080](http://localhost:8080)
2. Click **Administration Console**
3. Log in with `admin` / `admin`

## Step 4. Create a realm

Keycloak uses realms to manage sets of users and credentials. Create a new realm named **uptrace**:

1. In the top-left dropdown (which shows "master"), click **Create realm**

![Create realm](/features/keycloak/create-realm.png)

1. Set the **Realm name** to `uptrace`
2. Click **Create**

The realm name is part of the OIDC issuer URL (`/realms/<realm-name>`), so remember what you chose.

## Step 5. Create a user

1. Go to **Users** in the left sidebar and click **Create new user**
2. Fill in the **Username** and **Email** fields (email is required for Uptrace)
3. Click **Create**

![Create user](/features/keycloak/create-user.png)

1. Go to the **Credentials** tab and click **Set password**
2. Enter a password and set **Temporary** to **OFF**
3. Click **Save**

![User password](/features/keycloak/user-password.png)

## Step 6. Create a client for Uptrace

1. Go to **Clients** in the left sidebar and click **Create client**
2. Set **Client ID** to `uptrace` (or any name you prefer)
3. Make sure **Client authentication** is turned **ON** (this enables confidential access with a<br />


client secret)
4. Click **Save**

![Client settings](/features/keycloak/client-settings.png)

![Client config](/features/keycloak/client-config.png)

## Step 7. Configure redirect URI

1. In the client settings, go to the **Settings** tab (or **Access settings** section)
2. Set **Valid redirect URIs** to the redirect URL you received from Uptrace in Step 1
3. Click **Save**

![Access settings](/features/keycloak/access-settings.png)

## Step 8. Get client credentials

1. In the client settings, go to the **Credentials** tab
2. Copy the **Client secret** â you will need it for the Uptrace configuration

![Client credentials](/features/keycloak/client-credentials.png)

## Step 9. Finish configuring Uptrace

1. Go back to the OIDC SSO form you left open in Step 1
2. Enter the **Client ID** (`uptrace`) and the **Client Secret** you copied in Step 8
3. Set the **Issuer URL** to `http://<keycloak-host>/realms/<realm-name>` (e.g.,<br />

`http://localhost:8080/realms/uptrace`)
4. Click **Save**

<alert type="info">

The issuer URL must be accessible from the Uptrace host so that Uptrace can perform [OIDC Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) by fetching `<issuer_url>/.well-known/openid-configuration`. If Keycloak and Uptrace run on different machines or in separate Docker networks, make sure the URL is reachable.

</alert>

You can now log in to Uptrace using Keycloak by opening<br />

`https://uptrace.dev/auth/sso/<your-domain>`.

## Troubleshooting

**"issuer did not match" error** â Ensure the `issuer_url` in the Uptrace config exactly matches<br />


the realm URL, including the protocol and port. For example, `http://localhost:8080/realms/uptrace`<br />


will not match `http://keycloak:8080/realms/uptrace` if Uptrace accesses Keycloak via a different<br />


hostname.

**Redirect URI mismatch** â The redirect URI configured in Keycloak must exactly match what Uptrace<br />


uses: `http://uptrace.dev/api/v1/sso/keycloak/callback`. Make sure the protocol (`http` vs<br />

`https`), host, and port all match.

**User has no email** â Uptrace requires an email address for SSO users. Make sure the Keycloak user<br />


has an email configured in their profile.
