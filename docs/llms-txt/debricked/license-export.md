# Source: https://docs.debricked.com/product/exporting-sbom/license-export.md

# License export

{% hint style="info" %}
*This feature is only available for* [*SCA Premium & Enterprise*](https://debricked.com/pricing/) *users. Already have an account?* [*Click here to upgrade.*](https://debricked.com/app/en/repositories?billingModal=enterprise,free)
{% endhint %}

Knowing what kind of licenses you have imported through your dependencies is crucial, as failing to comply with open-source licenses puts you at legal risk. OpenText Core SCA allows you to make an export with all licenses and the affected repositories. This enables you to let relevant stakeholders get an easy overview of the state of compliance and keep track of your progress over time.

### Generate a license export

1. Click **Generate Export** on the top right corner of the page.
2. Select the scope of the export as wither global, repositories or groups.
3. Under **Export Type***,* select **License Export.**
4. Check your email for the exported data, which will be sent to you in the .xslx format. If you cannot find the email in your inbox, check the SPAM folder.&#x20;

Depending on the selected scope, you might receive three different types of exported data:

#### all\_licenses.xlsx

The excel sheet is divided into three columns:

* License - The name of the license.
* Repositories - The name of the repository using that license, the latest commit hash, and the creation date of that commit.
* License family - The name of the license family.

#### licenses\_per\_repo.xlsx

The excel sheet contains the name of the repository in the first row, divided into five columns:

* Dependency - The name of the dependency.
* Dependency id - The ID number of the dependency.
* License - The name of the licenses used by the dependency.
* Version - The version of the dependency.
* Direct/Indirect - The type of the dependency, which can be listed as "D = Direct", "I = Indirect" and "? = undefined".

#### licenses.xlsx

The excel sheet contains the name of the license in the first row, divided into two columns:

* Repositories - The name of all the repositories using that license.
* Dependencies - The name of all the dependencies using that license per repository.
