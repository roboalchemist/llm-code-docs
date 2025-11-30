# Source: https://dagshub.com/docs/faq/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/faq.md "Edit this page")

# FAQ[¶](#faq "Permanent link")

#### Q: I\'m experiencing a problem or something isn\'t working, what should I do?[¶](#q-im-experiencing-a-problem-or-something-isnt-working-what-should-i-do "Permanent link")

A: First, check if this is a common problem with a solution in our [Troubleshooting](../troubleshooting/) page. If not, head over to our [Discord](https://discord.gg/WNQmawBfCS) server\'s support channel, where are team is waiting to help you out.

------------------------------------------------------------------------

#### Q: So what IS DagsHub exactly?[¶](#q-so-what-is-dagshub-exactly "Permanent link")

A: DagsHub is a web platform for data version control and collaboration for data scientists and machine learning engineers.

------------------------------------------------------------------------

#### Q: Seriously, I donâ€™t get it\...what is it?[¶](#q-seriously-i-dont-get-itwhat-is-it "Permanent link") 

A: Itâ€™s like [GitHub](https://github.com/) for data science and machine learning.

------------------------------------------------------------------------

#### Q: Why canâ€™t I just use Git?[¶](#q-why-cant-i-just-use-git "Permanent link") 

A: Basically, regular [Git](https://git-scm.com/) is not so good at versioning large files, which is important for many data science and machine learning projects.

[git-lfs](https://git-lfs.github.com/) is an extension to Git that can be used to version large files, but that\'s only half of the problem.

**Git and git-lfs don\'t version the data pipeline.** Therefore, when one of the pipeline\'s components is modified, you won\'t know that the pipeline (e.g., the trained model) should be reproduced. You would have to manually ensure the downstream stages are run with the updated data/code. DagsHub integrated tools can also skip cached stages and run only updated files within your data pipeline.

Using DagsHub\'s suite of tools, it\'s possible to push and effectively version your large-data files, in a way that can be obtained from pointer files present within the Git repository.

------------------------------------------------------------------------

#### Q: So, then, does DagsHub do all of that stuff?[¶](#q-so-then-does-dagshub-do-all-of-that-stuff "Permanent link")

A: The short answer is YES.

The longer answer is that DagsHub is built on Git and [DVC](https://dvc.org/), which is an open source command-line tool built for data and pipeline versioning. You use Git for the exact same things you would in a regular code project, and you use DVC on top for the DS/ML versioning stuff. DagsHub adds visualizations and automation features on top of that. We have connectors to both GitHub Actions and Jenkins, which lets you automate things like training and deployment on top of Git and DVC.

------------------------------------------------------------------------

#### Q: Does that mean I need to learn a whole new framework again?[¶](#q-does-that-mean-i-need-to-learn-a-whole-new-framework-again "Permanent link")

A: The great thing about DVC is that it doesnâ€™t affect code versioning. You still use plain old Git for that.

DVC adds commands for DS and ML on top of that, but the syntax is similar to Git, so itâ€™s not entirely unfamiliar. Most Git commands have a direct equivalent in DVC.

------------------------------------------------------------------------

#### Q: So why not just use Git and DVC through the command line?[¶](#q-so-why-not-just-use-git-and-dvc-through-the-command-line "Permanent link")

A: In a nutshell: DagsHub is for DVC what GitHub is for Git.

DVC is great, and so is Git. But they are both command line tools, and as such have some inconveniences which DagsHub works to resolve.

First of all, there is no convenient [interface for visualizing your pipeline](../feature_guide/pipeline/) or getting an [overview your project metrics](../feature_guide/experiment_tracking/). DagsHub shows your pipeline as a\... wait for it\... [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (!!!), where every node is a file, with important details and a direct link to the file itself. This is especially important for team projects, where you want everyone on the same page and seeing the same high level picture.

You can send someone a link to your DagsHub repo, and give them a way to explore your project, including **downloading your data and models from any past version, experiment, or branch**, without forcing them to clone or run any code.

Building on the powerful foundations of Git and DVC, we have many more features in the works, which should make life easier for everyone.

------------------------------------------------------------------------

#### Q: Most tools that offer data pipeline versioning require adding lines of code to my project and/or importing libraries, what does DagsHub or DVC require me to do?[¶](#q-most-tools-that-offer-data-pipeline-versioning-require-adding-lines-of-code-to-my-project-andor-importing-libraries-what-does-dagshub-or-dvc-require-me-to-do "Permanent link")

A: NOTHING! This is why we love DVC so much. Just like Git, it is non-intrusive and not bloated. You just install the program and it works.

------------------------------------------------------------------------

#### Q: Then surely, it works only for certain languages and with certain ML libraries?[¶](#q-then-surely-it-works-only-for-certain-languages-and-with-certain-ml-libraries "Permanent link")

A: Nope. Completely, 100% language and library agnostic. DVC, and DagsHub, donâ€™t care if youâ€™re using Python or R, Keras or Pytorch.

------------------------------------------------------------------------

#### Q: Is DagsHub secure enough for my company/organization to use?[¶](#q-is-dagshub-secure-enough-for-my-companyorganization-to-use "Permanent link")

A: Yes, we have many companies and teams using DagsHub. There are varying degrees of security levels depending on what you need. You can use our data storage, connect external storage with your own access management, or in more extreme cases install a private instance of DagsHub on your own cloud or physical servers.

------------------------------------------------------------------------

#### Q: OK, but I like GitHub, and thatâ€™s what Iâ€™m using for my project. So you canâ€™t help me, right?[¶](#q-ok-but-i-like-github-and-thats-what-im-using-for-my-project-so-you-cant-help-me-right "Permanent link") 

A: Actually, we can. You can [connect](https://dagshub.com/docs/integration_guide/github) a project from GitHub to DagsHub and enjoy the best of both worlds! The repository on DagsHub will be subscribed to a GitHub webhooks and automatically synced on push. On top of that, Pull Requests & Issues created on GitHub are shown in DagsHub and vice versa. You can use DagsHub to review code, data & models, and when done, simply click the merge button to merge on both platforms.

------------------------------------------------------------------------

#### Q: Sounds good\...How much will it cost me?[¶](#q-sounds-goodhow-much-will-it-cost-me "Permanent link") 

A: Starting at a whopping ***\$0***, DagsHub is completely free for open source projects. Private repos are currently free with up to 2 additional collaborators. If you need more collaborators, early access to new features or other special requests, you can contact us through our [plans page](https://dagshub.com/pricing) for more details.

------------------------------------------------------------------------

#### Q: So how do I use DagsHub?[¶](#q-so-how-do-i-use-dagshub "Permanent link")

A: You can start with [the tutorial](../tutorials/experiment_tutorial/).

#### Q: Does DagsHub support DVC 3.0?[¶](#q-does-dagshub-support-dvc-30 "Permanent link") 

A: Yes, DagsHub supports DVC 3.x!

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).