# Source: https://docs.debricked.com/product/vulnerability-management/reachability-analysis.md

# Reachability Analysis

{% hint style="info" %}
*OpenText Core SCA currently supports the Reachability Analysis feature for Java and Go.*&#x20;
{% endhint %}

OpenText Core SCA's Reachability Analysis helps you automatically determine if a vulnerability in a library affects your project. It analyzes which parts of the library are vulnerable and checks if your code uses those parts. To do this, OpenText Core SCA needs to understand how your open source dependencies are used. This information is collected by using OpenText Core SCA's CLI tool to generate a call graph for your project. For instructions on creating the required call graph, see how to [Set up Reachability Analysis for Java](https://docs.debricked.com/product/vulnerability-management/reachability-analysis/set-up-reachability-analysis).

### **How does** OpenText Core SCA **know the vulnerable parts of libraries?**

OpenText Core SCA identifies vulnerable parts of libraries through the following steps:

1. **Fetch the relevant versions**: Retrieve the latest vulnerable version and the first fixed version from OpenText Core SCA's database.
2. **Pinpoint the smallest change**: Use information from various sources to narrow down to two specific versions — one that is vulnerable and one that is fixed. These versions can be released versions, Git tags, Git commits, or similar.
3. **Analyze code differences**: Download the code for these two versions, identify the changes between them, and translate these changes into functions, classes, and other code symbols. Store this information in OpenText Core SCA's database.
4. **Identify vulnerable symbols**: This process reveals which parts of the library are affected by a given vulnerability. These affected parts are known as *vulnerable symbols* for that vulnerability.

### **Am I using vulnerable parts?**

To perform the analysis, OpenText Core SCA needs to know which parts of a library are vulnerable and whether your code uses those parts. This is determined by generating a call graph for your program and its libraries. The call graph is then uploaded along with your dependency files and scanned for the vulnerable symbols identified in the previous step.

* **If vulnerable symbols are found**: This indicates that your code uses the parts of the library affected by the vulnerability, meaning your project is likely at risk.
* **If vulnerable symbols are not found**: This suggests that your code probably does not use the vulnerable parts and is less likely to be affected.

{% hint style="info" %}
**Important**: Call graphs do not have perfect recall or accuracy. They might include calls that cannot actually occur or miss calls that can. Therefore, even if OpenText Core SCA reports that you are not using the vulnerable function, you should still upgrade the dependency—though it might not need to be your highest priority.
{% endhint %}

### **Examples**

For projects using Netty versions between 4.1.0 and 4.1.43, OpenText Core SCA's public vulnerability database identifies the following vulnerabilities:

* CVE-2019-20444
* CVE-2019-20445
* CVE-2020-11612

However, not all of these vulnerabilities may affect your project:

* CVE-2019-20444 and CVE-2019-20445 impact the web server component of Netty.
* CVE-2020-11612 affects decompression functionality.

If your project does not use Netty for decompression, CVE-2020-11612 will not pose a risk. In this case, upgrading to version 4.1.44 instead of 4.1.46 might be sufficient. Similarly, if your project does not use the web server part of Netty, an upgrade might not be necessary at all, saving significant time and resources.\
However, it is still recommended to upgrade to a safe version, even if the priority may be lower when vulnerable symbols are not in use.\
Normally, determining this would require manual investigation, involving a deep understanding of both your project and Netty, as well as reviewing CVE specifications to find which parts of Netty are affected. With OpenText Core SCA's Reachability Analysis, this process is fully automated.

### **Different statuses of** OpenText Core SCA **Reachability Analysis**

In the tool, a vulnerability can have one of the following Reachability Analysis statuses:

* **Found**: The vulnerable functionality was detected as reachable through your code.
* **Not Found**: The vulnerable functionality was not detected as reachable through your code.

{% hint style="info" %}
**Note:** As mentioned earlier, call graphs do not have perfect recall or accuracy. It is still recommended to upgrade the dependency eventually, even if this status is shown.
{% endhint %}

* **Missing data**: There is not enough information available to determine if the vulnerable functionality is reachable.
* **Unknown**: The analysis was not run for this commit and vulnerability.
