# Source: https://docs.debricked.com/product/administration/repositories/upload-a-dependency-file-manually.md

# Manually upload a dependency file

{% hint style="info" %}
*Keep in mind that this feature is accessible only to account admins.*
{% endhint %}

If you want to get the most out of OpenText Core SCA tool, setting up an integration is the preferred way of working with your repositories.

However, if you want to test a specific dependency file for vulnerabilities, you can do so by manually uploading the file(s):

1. Go to [Repository Settings](https://debricked.com/app/en/repository-settings) on the left side menu.
2. Click **Manual scan** on the top right area of the table.
3. Upload the file(s) you want to scan.
4. Click **Start scan**.
5. Once the scan is completed, click **View results** to see all discovered vulnerabilities.

This action will create a repository named "<firstname.lastname@domain.com> - \<date>" and will add this scan as a commit within a repository.
