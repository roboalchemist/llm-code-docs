# Source: https://docs.debricked.com/product/vulnerability-management/solve-vulnerabilities-manually-with-root-fixes.md

# Solve vulnerabilities manually with root fixes

{% hint style="info" %}
*Currently, this feature is available for JavaScript, Java, Go, and NuGet.*
{% endhint %}

**Root fixes** contain the first next version of the direct dependency in the dependency tree that does not contain a vulnerable version of the affected dependency. In simpler terms, a Root fix is a solution to a dependency vulnerability that starts at the root of the dependency tree.

By addressing the root cause of the vulnerability, Root fixes ensure that the entire dependency tree is updated, using the version constraints set up by its dependencies. This way of updating dependencies is generally preferred over updating the vulnerable dependency directly, as it has a much lower risk of errors and breaking changes. It also eliminates the need for manually researching the required direct dependency update, saving developers valuable time.

### **Solve a vulnerability using root fix**

1. Click **Repositories** in the left side menu and select your project. Here you can see a list with all the CVEs found.&#x20;
2. Click one CVE to open the vulnerability page.
3. Go to the **Introduced through** section and select the dependency file to analyze. In some cases, the scan can find more than one dependency file within your project. You can see in green which is the closest secure version of the root package to update.&#x20;

   If OpenText Core SCA is not able to find a secure version to solve the vulnerability, the **Introduced through** section shows an *unknown.*
4. Before updating the package, keep in mind some packages might introduce breaking changes. To see if there is any risk, check the **Breaking Changes** section of the package's readme file.
5. Update the package through the package manager (in this example, using npm: *npm update hbs >= 4.1.1 )*
6. Commit and push the updates.

Once the scanning is completed, the repository should no longer have this vulnerability.

### Solve a vulnerability using root fix - video guide <a href="#solveavulnerabilityusingthe-rootfix-videoguide" id="solveavulnerabilityusingthe-rootfix-videoguide"></a>

{% embed url="<https://www.youtube.com/watch?v=-Y5G5ao32-o>" %}
