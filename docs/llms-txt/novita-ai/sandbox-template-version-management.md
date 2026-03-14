# Source: https://novita.ai/docs/guides/sandbox-template-version-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Version Management

export const SandboxBetaVersionWarning = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Warning>The following features require <Link href="/guides/sandbox-sdk-and-cli#install-beta-sdk" target="self">installing the Beta SDK & CLI</Link>. Please note that beta features are subject to change and may be less stable than production releases. If you encounter any issues while using these features, please <Link href="https://meetings-na2.hubspot.com/junyu" target="_blank">contact us</Link>.</Warning>;
  }
};

<SandboxBetaVersionWarning />

For the same sandbox template, each time it is built, the system will add a new version number (buildID), and the sandbox template will use the latest built version by default. In some scenarios, if you find that a newly built version has errors and need to rollback to a previous version, you can use the Novita Sandbox CLI to manage the versions of the sandbox template.

## View All Versions of a Sandbox Template

```bash Bash icon="terminal" theme={"system"}
# novita-sandbox-cli template version [templateID]
novita-sandbox-cli tpl version lovhlhmzeq6q0yh3lu9a
# Example output:
# Sandbox template versions
# Build ID Is Default Build  RAM MiB  VCPUs  Start  Cmd  Status    Created At             Finished At
# f15e442a-a825-4881-9bd8-ad70a96af372  true              1024     2      /root/.jupyter/start-up.sh  Uploaded  8/25/2025, 5:53:04 PM  8/25/2025, 5:55:43 PM
# f9e12c5a-8934-4b13-b574-2f7c211adba1  false             1024     2                                  Uploaded  8/25/2025, 4:52:30 PM  8/25/2025, 4:56:43 PM
```

## Rollback to a Specific Version

```bash Bash icon="terminal" theme={"system"}
# novita-sandbox-cli template version [templateID] -r [buildID]
novita-sandbox-cli tpl version lovhlhmzeq6q0yh3lu9a -r f9e12c5a-8934-4b13-b574-2f7c211adba1
```


Built with [Mintlify](https://mintlify.com).