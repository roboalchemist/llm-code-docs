# Source: https://help.aikido.dev/container-image-scanning/cloud-provider-registries/configuring-registry-scan-scope.md

# Configuring Registry Scan Scope

Use wildcard patterns to control which container images Aikido scans in your connected registries. This helps you focus on relevant containers and avoid clutter when working with registries containing hundreds of images across multiple projects.

#### How Scan Scope Works

You can configure scan scope in two ways:

* **Include containers matching**: Aikido will exclusively scan containers that match your specified patterns. All other containers will be ignored.
* **Exclude containers matching**: Aikido will scan all containers except those matching your patterns.

#### Setting Up Scan Scope

1. Navigate to [**Settings** > **Containers**](https://app.aikido.dev/settings/container-image-registry)&#x20;
2. Click the triple dots on the registry you want to configure, and click '**Edit Registry Configuration**'<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Ftc7P1C9acll1TVVsjv3p%2Fimage.png?alt=media&#x26;token=5099d1bd-6e85-45c5-8f95-f55b0eb9eb11" alt="" width="288"><figcaption></figcaption></figure>
3. In the **Registry Settings** modal, scroll to the **Registry Scan Scope** section<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FCOPa9n0Fc9ec2Oljwzc6%2Fimage.png?alt=media&#x26;token=2d8e2256-496a-44ed-b8e9-8e7036129c3e" alt="" width="375"><figcaption></figcaption></figure>
4. Select your scan mode:
   * **Include containers matching** to create an allowlist
   * **Exclude containers matching** to create a blocklist
5. Enter your wildcard pattern (e.g., `backend-*`)
6. Click **Add Pattern** to add additional patterns
7. Click **Save**

After saving, Aikido applies your scan scope rules **during the next scheduled scan**. Only containers matching your criteria will be added to your Aikido workspace and scanned.

#### Wildcard Pattern Examples

Wildcard patterns use the `*` character to match multiple container names:

* `frontend-*` - Matches all containers starting with "frontend-" (e.g., `frontend-web`, `frontend-api`)
* `*-prod` - Matches all containers ending with "-prod"
* `production/*` - Matches all containers in the production project or namespace
* `*test*` - Matches any container with "test" in the name
