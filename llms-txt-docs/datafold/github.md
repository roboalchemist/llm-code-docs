# Source: https://docs.datafold.com/integrations/code-repositories/github.md

# GitHub

<Note>
  **PREREQUISITES**

  * Datafold Admin role
  * Your GitHub account must be a member of the GitHub organization where the Datafold app is to be installed
  * Approval of your request to add the Datafold app to your repo must be granted by a GitHub repo admin or GitHub organization owner.
</Note>

To set up a new integration, click the repository field and select the **Install GitHub app** button.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=05a583165e696cf4d8191cefb37d6ed9" data-og-width="2200" width="2200" data-og-height="926" height="926" data-path="images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=84e1ae6bce9b0005b6bebe64cdd50419 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9938eca7a9b6e490e78b5cdb157e0c90 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fcadb062275a2f2a19a1cad8565afd12 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=aa5415f0b1d845bf78dd0fb9f394dff3 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5bb5b709bf66c29e08f9278a03d5912f 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/github_install_button-27ecc75b58ccbe7681aa70223cc0e21b.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=226f0c8dcc9b79efee20a28cc23ab2ce 2500w" />
</Frame>

From here, GitHub will redirect you to login to your account and choose which organization you would like to connect. After choosing the right organization, you may choose to allow access to all repositories or specific ones.

Once complete, you will be redirected back to Datafold, where you can select the appropriate repository for connection.

<Tip>
  **TIP**

  If you lack permission to add the Datafold app, request approval from a GitHub admin.

  After installation, click **Refresh** to display the newly added repositories in the dropdown list.
</Tip>

To complete the setup, click **Save**!

<Note>
  **INFO**
  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## GitHub integration for VPC / single-tenant Datafold deployments

### Create a GitHub application

VPC clients of Datafold need to create their own GitHub app, rather than use the shared Datafold GitHub application.

Start by navigating to **Settings** → **Global Settings**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=064ce50091eaab88a16f0314e60103b0" data-og-width="2522" width="2522" data-og-height="1252" height="1252" data-path="images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3e56fc9b9cd2b1c23e4dc6afca485b59 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=33871ca1d5cd170f7b0393445b8dc553 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa0b6b1cfc74be40ee5eb534ce0972fe 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=508aa055d66678e9fc08fe19be33d61b 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e5903eb74f03ac6d5b07109d61114e9d 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_settings-4ba347a4179f693ad9cf851188d3cd3c.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2244e0facc8b84411a791d5d7c78c8ae 2500w" />
</Frame>

To begin the set up process, enter the domain that was registered for the VPC deployment in [AWS](/datafold-deployment/dedicated-cloud/aws) or [GCP](/datafold-deployment/dedicated-cloud/gcp). Then, enter the name of the GitHub organization where you'd like to install the application. When filled, click **Create GitHub App**.

This will redirect the admin to GitHub, where they may need to authenticate. **The GitHub user must be an admin of the GitHub organization.**

After authentication, you should be directed to enter a description for the GitHub App. After entering the description, click **Create GitHub app**.

Once the application is created, you should be returned to the Datafold settings screen. The button should then have disappeared, and the details for the GitHub App should be visible.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1f647e225a50e347520543a74fb723f5" data-og-width="1421" width="1421" data-og-height="1017" height="1017" data-path="images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c023b6d6e7864ca9472c63ce96232117 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=77e0cc92b48c790229f8b19c3aaf4a97 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cdaaa3e226a502fa20d171c786652bbc 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3b3b4d3a9d91b52dacc47b170e1b0eaf 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=af589570089dce593316a501c0ac0902 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_github_confirmation-040de7316a509d880b13d6be431da24d.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=47b8dd90d161524aecfb53fdeb1794fb 2500w" />
</Frame>

### Making the GitHub application public

If you have a private GitHub instance with multiple organizations and want to use the Datafold app across all of them, you'll need to make the app public on your private server.

You can do so in GitHub by following these steps:

1. Navigate to the GitHub organization where the app was created.
2. Click **Settings**.
3. Go to **Developer Settings** → **GitHub Apps**.
4. Select the **Datafold app**.
5. Click **Advanced**, then **Make public**.

<Note>
  The app will be public **only on your private GitHub server**, ensuring it can be accessed across all your organizations.
</Note>

### Configure GitHub in Datafold

If you see this screen with all the details, you've successfully created a GitHub App! Now that the app is created, you have to install it using the [GitHub integration setup](/integrations/code-repositories/github).
