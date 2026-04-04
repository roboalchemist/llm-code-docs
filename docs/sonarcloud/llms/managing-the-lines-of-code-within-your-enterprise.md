# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-lines-of-code-within-your-enterprise.md

# Managing the lines of code within your enterprise

### About the enterprise lines of code limit (Shared LOC and Allocated LOC) <a href="#about-enterprise-loc-limit" id="about-enterprise-loc-limit"></a>

Your enterprise license entitles you to a maximum lines of code (enterprise LOC limit). For more information about lines of code, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/managing-subscription/subscription-plans#loc-based-pricing "mention").

By default, the enterprise LOC limit is *shared* by all organizations in the enterprise: the total LOC consumed by all organizations in the enterprise cannot exceed this limit.

You have the flexibility to **allocate** an individual LOC limit to one or more organizations within your enterprise (including the option to apply it to all): the LOC consumed by the organization cannot exceed the limit allocated to this organization. The other organizations in your enterprise will share the remaining LOC limit. For example, an enterprise with a total LOC limit of 5 M and containing 4 organizations may be configured as follows:

* Organization1 is allocated a 2M LOC limit.
* Organization2 is allocated a 1.3M LOC limit.
* Organization3 and Organization4 share the remaining LOC limit, i.e. 1.7 M.

We use the following concepts to refer to the different LOC limit uses:

* **Shared LOC** refers to the collective lines of code limit shared by organizations within the enterprise.
* **Allocated LOC** refers to the individual lines of code limits allocated to organizations within the enterprise.

{% hint style="info" %}
An allocated LOC must be a multiple of 100k with a minimum allocation of 100k. If you have less than 1M LOC limit in your enterprise, we recommend that you use only the Shared LOC.
{% endhint %}

### Allocating a LOC limit to an organization <a href="#allocating-loc-limit" id="allocating-loc-limit"></a>

You can allocate a LOC limit to an organization within your enterprise, as long as the enterprise LOC limit has not been fully allocated. The remaining LOC available for allocation are determined by subtracting already allocated LOC limits from the enterprise LOC limit.

To allocate a LOC limit to an organization within your enterprise:

1. Retrieve your enterprise.
2. Go to the **Billing and usage** tab.
3. In front of **Usage**, select the **Manage lines of code** link.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4e878a69bf22b54d34e7b80f3ca22ed518d39406%2Fsonarqube-cloud-enterprise-manage-lines-of-code-link_Cs0099.png?alt=media" alt="Select Manage lines of code to allocate a specific LOC limit to an organization within your enterprise"><figcaption></figcaption></figure>

In the page that opens, the **Shared LOC** tab lists the organizations that use the shared LOC.

4. Locate the organization in the list (navigate to the next page if necessary) and select **Allocate LOC**. The corresponding dialog opens.
5. Enter the LOC limit value to be allocated and select **Allocate LOC**. The LOC limit is allocated and the organization is moved to the **Allocated LOC** tab.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-13b46da15ae7f86f7700495fe499f39343bead0c%2Fsonarqube-cloud-allocate-loc-limit-to-organization-within-enterprise_Cs0100.png?alt=media" alt="Select the Shared LOC tab to allocate a LOC limit to an organization within your enterprise"><figcaption></figcaption></figure>

### Changing the LOC limit allocated to an organization <a href="#changing-loc-limit-of-organization" id="changing-loc-limit-of-organization"></a>

To change the allocated LOC limit of an organization within your enterprise:

1. Retrieve your enterprise.
2. Go to the **Billing and usage** tab.
3. In front of **Usage**, select the **Manage lines of code** link. In the page that opens, select the **Allocated LOC** tab. The tab lists the organizations using an allocated lines of code limit.
4. Locate the organization in the list (navigate to the next page if necessary). Select the three-dot menu and then **Modify LOC limit**. The corresponding dialog opens.
5. Enter the new LOC limit value and select **Modify limit**. The limit is changed.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-6460f26a55b98e58e36500d077af6f71e4712c76%2Fsonarqube-cloud-modify-loc-allocated-to-organization-within-enterprise_Cs0101.png?alt=media" alt="Select the Allocated LOC tab to change the specific LOC limit assigned to an organization within your enterprise"><figcaption></figcaption></figure>

### Changing the enterprise LOC limit <a href="#changing-loc-limit-of-enterprise" id="changing-loc-limit-of-enterprise"></a>

To change your enterprise LOC limit, you must change your enterprise license: [contact our team](https://www.sonarsource.com/products/sonarcloud/contact-enterprise-sales/).

### Removing the LOC limit allocated to an organization <a href="#removing-allocated-loc-limit" id="removing-allocated-loc-limit"></a>

To remove the allocated LOC limit of an organization within your enterprise:

1. Retrieve your enterprise.
2. Go to the **Billing and usage** tab.
3. In front of **Usage**, select the **Manage lines of code** link. In the page that opens, select the **Allocated LOC** tab. The tab lists the organizations using an allocated lines of code limit.
4. Locate the organization in the list (navigate to the next page if necessary). Select the three-dot menu and then **Remove LOC limit**. The confirmation dialog opens.
5. Select **Confirm removal.** The allocated limit is removed and the organization is moved to the **Shared LOC** tab.

### Viewing the lines of code consumption <a href="#loc-consumption" id="loc-consumption"></a>

1. Retrieve your enterprise.
2. Go to the **Billing and usage** tab.
3. In front of **Usage**, select the **Manage lines of code** link. In the page that opens:
   * The **Shared LOC** tab shows the consumption of the organizations using the shared LOC.
   * The **Allocated LOC** tab shows the allocated LOC consumption for each organization.

### Related pages <a href="#related-pages" id="related-pages"></a>

[retrieving-and-viewing-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/retrieving-and-viewing-your-enterprise "mention")\
[creating-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/creating-your-enterprise "mention")\
[enterprise-security](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security "mention")\
[adding-organizations-to-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/adding-organizations-to-your-enterprise "mention")\
[managing-the-enterprise-related-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-enterprise-related-permissions "mention")\
[changing-enterprise-settings](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/changing-enterprise-settings "mention")\
[downgrading-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/downgrading-your-enterprise "mention")
