# Source: https://dagshub.com/docs/feature_guide/topics/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/topics.md "Edit this page")

# DagsHub Topics[¶](#dagshub-topics "Permanent link")

To help other people find and contribute to your project, you can add topics to your repository related to your project\'s intended purpose, subject area, affinity groups, or other important qualities.

## About topics[¶](#about-topics "Permanent link")

Using topics, you can explore repositories in a particular subject area, find projects to contribute to, and discover new solutions to a specific problem. Topics appear on the main page of a repository or in the route path where they were added. You can click a topic name to see a list of other repositories classified with that topic. Repository admins can add any topics they\'d like to a repository. Helpful topics to classify a repository include the repository\'s intended purpose, subject area, community, or language.

[![List of topics](../assets/topics/topics_home.png)](../assets/topics/topics_home.png)\
~Topics\ in\ DagsHub~

## How do DagsHub Topics work?[¶](#how-do-dagshub-topics-work "Permanent link")

In order to add topics to a repository, we have added two options, through the UI (using an autocomplete input) or creating a topics file, which we will track and parse. Topics can be added at project level or at a specific path, either on a folder or a file.

## How to use DagsHub Topics?[¶](#how-to-use-dagshub-topics "Permanent link")

### Add topics through the UI[¶](#add-topics-through-the-ui "Permanent link")

~Adding\ topics\ with\ the\ UI~

1.  Click `+ Add topics`
2.  Type the desired topic name in the autocomplete input or search it in the dropdown.
3.  Click Submit
4.  Topics are added to the repository

### Add topics through topics files[¶](#add-topics-through-topics-files "Permanent link")

1.  Create a topics file, possible names are: `topics`, `dagshub-topics`. Possible file extensions are `YAML` or `JSON` files

2.  You can create the file through our UI or by committing one using Git.
    [![Upload file button](../assets/topics/add_new_file.png)](../assets/topics/add_new_file.png)\
    ~Upload\ a\ file\ via\ the\ UI~

3.  The desired format for a topics file is:

    ::: highlight
        Category:
          - TopicName
          - TopicName
          - TopicName
    :::

    To get all the possible categories and topics please refer to our [explore page](https://dagshub.com/explore).

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).