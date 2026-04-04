# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/clone-an-integration-across-your-snyk-organizations.md

# Clone an integration across your Snyk Organizations

You can choose to use the same brokered Git integration across multiple Organizations in Snyk by copying and duplicating the Organization you have already configured.

For example, you can integrate Snyk Organizations X, Y, and Z with your single Git repo X.

To clone Organization configurations, you must have teams and groups enabled.

1. From the **Organization** list, choose an Organization in the Group that you are working with.\ <img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c8f66d013a9e786c46bb9fab56d7ca38c7aca8eb%2Fswitch_org_02oct2022.png?alt=media" alt="Choose Organization" data-size="original">
2. From the same **Organization** dropdown, click **+Create new Organization.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d0dfc17caf5d7dbaa08bf31c8095db056addc7ef%2Fclone-organization1_02oct2022.png?alt=media" alt="Select +Create new Organization"><figcaption><p>Select +Create new Organization</p></figcaption></figure>
3. In the next window, enter a name for your new Organization.
4. In the **Copy settings from an existing org** section, choose an Organization that you have already configured for the Broker token.
5. Review the summary of what will be copied across to the new Organization and click **Create organization** to confirm.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fdd1d6601fc6c91853308972c273c561fea7cd1a%2Fclone-org-3screens_02oct2022.png?alt=media" alt="Review summary of what will be copied to the new Organization and Create"><figcaption><p>Review summary of what will be copied to the new Organization and Create</p></figcaption></figure>

The **Dashboard** for the Organization that you just created opens. The Broker integration is duplicated and set up, and the Broker token is identical to the token for the original Organization.
