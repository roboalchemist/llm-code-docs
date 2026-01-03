# Source: https://braintrust.dev/docs/core/human-review.md

# Human review

Human review is a critical part of the evaluation process.

Although Braintrust helps you automatically evaluate AI software, human
review is a critical part of the process. Braintrust seamlessly integrates human
feedback from end users, subject matter experts, and product teams in one place. You can
use human review to evaluate/compare experiments, assess the efficacy of your automated scoring
methods, and curate log events to use in your evals. As you add human review scores, your logs will update in real time.

<img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/label.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=aab2f2c158d909ab8be2eaf438964971" alt="Human review label" data-og-width="2166" width="2166" data-og-height="1260" height="1260" data-path="images/guides/human-review/label.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/label.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=3a5f1e98ab2f25decfad184abb353acc 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/label.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=ad3d2f6a004004979cec1d647aa49a08 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/label.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=1c8992d9fcd6bcd5b21d412dd924bfbd 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/label.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=93a42413af4300f292a66abb4a4f7b17 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/label.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=887af3caccd6daa69dd08d958baf3610 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/label.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a5a5034b61b48c7059f8cae0ba28a1f2 2500w" />

## Configure human review

To set up human review, define the scores you want to collect in your
project's **Configuration** tab.

<img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/config-page.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=ab39a4ecc41c8984d64238993697b991" alt="Human Review Configuration" data-og-width="2164" width="2164" data-og-height="1212" height="1212" data-path="images/guides/human-review/config-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/config-page.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a66060ad380be1ef62da5d00a9f92025 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/config-page.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=912569b2bc0b753010ddd412da55169e 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/config-page.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=9af941071db4accc8ce8d28ef8f6f83f 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/config-page.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=5265b17559449d65ce7401d4c64eb88e 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/config-page.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=b2b7c7d246580f546ae4f13d9bf6603f 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/config-page.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=976d95b2fc9cdb30d836fb41cf57f1be 2500w" />

Select **Add human review score** to configure a new score. A score can be one of

* Continuous number value between `0%` and `100%`, with a slider input control.
* Categorical value where you can define the possible options and their scores. Categorical value options
  are also assigned a unique percentage value between `0%` and `100%` (stored as 0 to 1).
* Free-form text where you can write a string value to the `metadata` field at a specified path.

<img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/create-modal.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a34dc62e907d61215df45cc50d45c50e" alt="Create modal" data-og-width="2140" width="2140" data-og-height="1296" height="1296" data-path="images/guides/human-review/create-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/create-modal.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=21ed0f4e379cf3ae589ebdd8392b264f 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/create-modal.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a02bb5af4b8bd28a16ac40fa866681a4 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/create-modal.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=38703a1be02f0574740c243fb71f5e49 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/create-modal.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=56001ee96e558c47a3a8ffde80ab782c 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/create-modal.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=695aa37e201701169c22d9ea06e54623 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/create-modal.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=fb5638740eee6decade7a1daac7100f9 2500w" />

Created human review scores will appear in the **Human review** section in every experiment and log trace in the project. Categorical scores configured to "write to expected" and free-form scores will also appear on dataset rows.

### Write to expected fields

You may choose to write categorical scores to the `expected` field of a span instead of a score.
To enable this, check the **Write to expected field instead of score** option. There is also
an option to **Allow multiple choice** when writing to the expected field.

<Note>
  A numeric score will not be assigned to the categorical options when writing to the expected
  field. If there is an existing object in the expected field, the categorical value will be
  appended to the object.
</Note>

<img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=406359641fc9f3de4f70086d56f236dd" alt="Write to expected" data-og-width="1852" width="1852" data-og-height="966" height="966" data-path="images/guides/human-review/expected-fields.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=74c2817c643f44e6bf10b5c872ad988b 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2504bd28d1b54f4430d7458fd407be25 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=5691362eca4b4c03f9b2dbf32873bb51 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2d93b28ed1d8d7f62d65c15b4786a762 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=e2ee18d7f67b4b4f89c08d765a7734bb 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a44f9ea41167ce86f27a572aac1c3f7d 2500w" />

In addition to categorical scores, you can always directly edit the structured output for the `expected` field of any span through the UI.

## Review logs and experiments

To manually review results from your logs or experiment, select a row to open trace view. There, you can edit the human review scores you previously configured.

<video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/human-review/in-experiment-poster.png">
  <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/in-experiment.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=ece6a5e7cc413c6280a92198176873ce" type="video/mp4" data-path="images/guides/human-review/in-experiment.mp4" />
</video>

As you set scores, they will be automatically saved and reflected in the summary metrics. The process is the same whether you're reviewing logs or experiments.

### Leave comments

In addition to setting scores, you can also add comments to spans and update their `expected` values. These updates
are tracked alongside score updates to form an audit trail of edits to a span.

If you leave a comment that you want to share with a teammate, you can copy a link that will deeplink to the comment.

<Note>
  Comments are searchable. Use the [Filter menu](/core/logs/view#filter-menu) on the **Logs** or **Experiments** page to find traces by comment.
</Note>

<video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/human-review/comment-poster.png">
  <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/comment.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=b8aeec14bc3456cc40591c3e3a1e085c" type="video/mp4" data-path="images/guides/human-review/comment.mp4" />
</video>

## Focused review mode

If you or a subject matter expert is reviewing a large number of logs or experiments, you can use **Review** mode to enter
a UI that's optimized specifically for review. To enter review mode, hit the "r" key or the expand (<Icon icon="maximize" className="size-3 inline" />)
icon next to the **Human review** header in a span.

<video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/human-review/review-mode-poster.png">
  <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/review-mode.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=e3c0c752242fbbe2f84c698bca7f4c5d" type="video/mp4" data-path="images/guides/human-review/review-mode.mp4" />
</video>

In review mode, you can set scores, leave comments, and edit expected values. Review mode is optimized for keyboard
navigation, so you can quickly move between scores and rows with keyboard shortcuts. You can also share a link to the
review mode view with other team members, and they'll drop directly into review mode.

### Review data that matches a specific criteria

To easily review a subset of your logs or experiments that match a given criteria, you can filter using English or [BTQL](/reference/btql#btql-query-syntax), then enter review mode.

In addition to filters, you can use [tags](/core/logs#tags-and-queues) to mark items for `Triage`, and then review them all at once.

You can also save any filters, sorts, or column configurations as views. Views give you a standardized place to see any current or future logs that match a given criteria, for example, logs with a Factuality score less than 50%. Once you create your view, you can enter review mode right from there.

<video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/human-review/filter-view-review-poster.png">
  <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/filter-view-review.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2de455f84682dc366558af1481bd01af" type="video/mp4" data-path="images/guides/human-review/filter-view-review.mp4" />
</video>

Reviewing is a common task, and therefore you can enter review mode from any experiment or log view. You can also re-enter review mode from any view to audit
past reviews or update scores.

### Dynamic review with views

* Designed for optimal productivity: The combination of views and human review mode simplifies the review process with intuitive filters, reusable configurations, and keyboard navigation, enabling fast and efficient evaluation and feedback.

* Dynamic and flexible views: Views dynamically update with new rows matching saved criteria, without requiring the need to set up and maintain complex automation rules.

* Easy collaboration: Sharing review mode links allows for team collaboration without requiring intricate permissions or setup overhead.

## Select spans for review

The **Review** list is a centralized annotation queue to see all spans that have been marked for review across your project. This complements focused reviews by
giving you a curated queue of items that need attention, regardless of where they appear in your project.

To mark a span for review, select **Flag for review** in the span header. You can also bulk select rows that need review and select **Flag for review**.
Additionally, you can assign spans to specific users so they can view all spans pending their review.

<video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/human-review/mark-for-review-poster.png">
  <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/mark-for-review.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=3469c63c86fa05e4f3ad3db63aa2748d" type="video/mp4" data-path="images/guides/human-review/mark-for-review.mp4" />
</video>

Navigate to **Review** from the sidebar to see all marked spans across your project.

### Review in context

When you open a span in the list, you'll see it in the context of its full trace. This allows you to understand the span's role within the larger request and
review parent and child spans for additional context.

Once you've finished reviewing a span, you can mark it as **Complete** or navigate to the next item in the queue.

## Filter using feedback

In the UI, you can filter on log events with specific scores by adding a filter using the filter button, like "Preference is greater than 75%",
and then add the matching rows to a dataset for further investigation.

You can also programmatically filter log events using the API using a query and the project ID:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  await braintrust.projects.logs.fetch(projectId, { query });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import braintrust

  braintrust.projects.logs.fetch("<project_id>", "scores.Preference > 0.75")
  ```
</CodeGroup>

This is a powerful way to utilize human feedback
to improve your evals.

## Capture end-user feedback

The same set of updates — scores, comments, and expected values — can be captured from end-users as well. Check out
[Write logs](/core/logs/write#user-feedback) for more details.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt