# Source: https://docs.debricked.com/product/open-source-select/search-for-projects.md

# Search projects

Finding the right open source project to solve your specific problem can be difficult, especially when you want to make informed decisions before choosing what to bring into your codebase. [Open Source Select](https://debricked.com/select/) is OpenText Core SCA’s database of all open source projects available on GitHub. It enables you to search, compare and evaluate packages based on different health metrics and quality scores.&#x20;

### **How do i search?** <a href="#howdoisearch" id="howdoisearch"></a>

With Open Source Select, you can search for packages, projects or functionalities and get all relevant information presented in one place. You can further refine your search using filters.

When searching, use a few good keywords describing what you're looking for. For example, try searching for “frontend graphs” if you're looking for a project to help you create nice-looking visualizations, or search for “message broker” if you're looking for data streaming projects.

### **Search on project names**

Enter the name of the project you wish to know more about and hit enter. A list of projects matching the search string fully or partially will be shown.

### **Search on project functionality**

As a developer you often know the problem you want to solve, but not necessarily all projects that exist to address that problem. Searching for the functionality that you're after helps you discover these projects.

### **Search for repositories**

Open Source Select isn't limited to packages, it is also possible to search for repositories using the *repository\_owner/repository\_name* format. Keep in mind that the results from this query can be both dependencies that are repository-only, and dependencies that have a package and hold their code in the searched repository.

### **Search using pURL standard** <a href="#searchusingthepurlstandard" id="searchusingthepurlstandard"></a>

It is also possible to search for dependencies using the common pURL format:

```
pkg:type/namespace/name
```

The *type* section of the pURL corresponds to the package manager used by the dependency or the version control system used (in case of repository-only dependencies).

The *namespace* is used mainly for repository-only dependencies, corresponding to the repository owner.

The *name* section corresponds to the package or repository’s name.

The pURL standard is also supported directly in the url: *<https://debricked.com/en/select/package/{purl}>*

Here are some examples of pURL searches and their corresponding results:

*pkg:pypi/tensorflow* → Tensorflow

*pkg:npm/react* → React

*pkg:github/debricked/debricked-cli* → Debricked-cli

### **Refine your search using filters** <a href="#refineyoursearchusingfilters" id="refineyoursearchusingfilters"></a>

The most powerful way to search the Select database is by combining project name or project functionality searches with filters narrowing down the results to your preferences.

You can filter by:

* programming language
* package manager
* excluded licenses

### Choose open source components with OpenText Core SCA's open source select and start left - video guide <a href="#choosingopensourcecomponentswithdebrickedsopensourceselectandstartleft-videoguide" id="choosingopensourcecomponentswithdebrickedsopensourceselectandstartleft-videoguide"></a>

{% embed url="<https://www.youtube.com/watch?v=JCgA1DjAq8A>" %}
