# Source: https://dagshub.com/docs/feature_guide/dagshub_discussions/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/dagshub_discussions.md "Edit this page")

# Discussions[¶](#discussions "Permanent link")

At DagsHub, we\'re tackling collaboration on data science projects as a first-class problem. **DagsHub Discussions are a way to communicate with collaborators in context. We like to call it the \"comment on everything\" feature.**

Instead of having long discussions in Slack with links and screenshots that get lost over time and hurt reproducibility and your ability to build a knowledge base,

DagsHub discussions let you discuss model architecture right under the model file, review annotations on the image files, and talk about the custom metrics you\'re using to visualize your experiment right under the relevant notebook cell.

## Discussions Tab[¶](#discussions-tab "Permanent link")

The discussions tab is where you see all the discussions happening in your project. You can see the type of file (notebook, model, folder, etc.), last edit time, discussion participants and the amount of comments involved.

The discussions are sorted by most recent reply, so you can always easily find where the action is.

[![Discussions Tab](../assets/discussions/discussions_tab.png)](../assets/discussions/discussions_tab.png)

~Discussions\ tab~

## Comment Types[¶](#comment-types "Permanent link")

Data scientists need context to build a knowledge base. We know that issues don\'t cut it, but sometimes even commenting on entire files isn\'t good enough. That\'s why we support commenting in various contexts, including commenting on code lines, notebook cells, bounding boxes and more.

At the top of each file, you will also find the Discussion button, that will lead you directly to where the magic is happening.

[![Discussions Button](../assets/discussions/discussions_button.png)](../assets/discussions/discussions_button.png)

~Discussions\ button~

### Comment on files & folders[¶](#comment-on-files-folders "Permanent link")

This is the basic type of comments. You can start a discussion on any file or folder in your project. This covers use cases like discussing model architecture and which data points should be added to the data folder.

[![Discussions on a model file](../assets/discussions/file_discussion.png)](../assets/discussions/file_discussion.png)

~Discussing\ model\ architecture~

### Comment on code lines[¶](#comment-on-code-lines "Permanent link")

Code is a central part of every machine learning project on DagsHub. Since code files might be very large, commenting on an entire file might not be granular enough. To counter that, DagsHub Discussions lets you comment on any code line. Each comment made on a line of code will appear under that line, and as part of the broader discussion at the bottom of the file.

\

\

~Use\ DagsHub\ Diffing\ on\ a\ Commit~

\

### Comment on notebook cells[¶](#comment-on-notebook-cells "Permanent link")

Data scientists love notebooks, but interacting with them in version control is notoriously difficult. Discussions enable you to comment on notebook cells, so you can discuss that visualization or prediction right under where it was calculated.

\

\

~Use\ DagsHub\ Diffing\ on\ a\ Commit~

\

### Comment on image bounding boxes[¶](#comment-on-image-bounding-boxes "Permanent link")

If you work with images, you sometimes want to point a teammate to a specific part of the image, for example an area where annotation is a bit off. Discussions let you mark an area in an image and add a comment that will be tied to that area.

When your teammate clicks that area, they\'ll see where it refers to in the image.

\

\

~Use\ DagsHub\ Diffing\ on\ a\ Commit~

\

### Comment on file diffs[¶](#comment-on-file-diffs "Permanent link")

Sometime knowledge building happens between versions of files. You might want to add a note on how a data file changed, or mention a team member if they accidentally remove an import piece of code. With Discussions, you can comment on [file diffs](../dagshub_diffing/), so that information is preserved.

This commenting also works for diffs in pull requests, so you can always add the relevant note.

[![Diff comment in Pull Request view](../assets/discussions/diff_comment.png)](../assets/discussions/diff_comment.png)

~Diff\ comment\ in\ Pull\ Request\ view~

### Which comment support do you need?[¶](#which-comment-support-do-you-need "Permanent link")

Want to comment on something not yet supported? Let us know in our [Discord community\'s suggestions channel](https://discord.gg/X6ugUwcPAs)

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).