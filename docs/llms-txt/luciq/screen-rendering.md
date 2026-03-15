# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-application-performance-monitoring/screen-rendering.md

# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/application-performance-monitoring/screen-rendering.md

# Screen Rendering

Identify **spans that most commonly correlate** with Slow and Frozen Frames. These spans are likely root causes of rendering issues on this screen.

![](https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FCo5BPpEHeMBkiZ10Zj06%2F29c466c78dadf58556e7051247a20985f91c457300836701c5b2f487ee9912f1%20image.png?alt=media\&token=cbabf5b2-e2da-4afc-8340-ea09f41841e6)

The suspect spans table shows for every span captured on this screen:

* **Frozen Frames %:** What percentage of the occurrences of this span correlated with a frozen frame.
* **Slow Frames %:** What percentage of the occurrences of this span correlated with a slow frame.
* **Change:** How each of those percentages changed in the selected date period compared to the previous period of the same length.

Learn more about spans and how they can help you identify the root cause of performance issues in the documentation: <https://docs.luciq.ai/docs/android-apm-instrumentation>

#### Patterns

Understand your rendering performance across different dimensions: App versions, Devices, OS versions, etc., allowing you to narrow down into segments of your user base to identify and debug issues.

#### Occurrence View

Navigate to the occurrences page of any screen to view individual screen visit occurrences in full detail.

* View metadata about each occurrence, including frozen and slow frames %, device and app information, and other parameters.
* View a detailed span timeline of the complete screen visit, highlighting frozen frames (in red) and slow frames (in yellow).
* Hover over any frozen or slow frame to highlight that frame’s suspect spans, a likely root cause of this rendering delay.

![](https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F84PmAQbWVVc9QwFS22fX%2F96d48a6c609bb5574d4593d569cd61fb536f7233db14dd3ca62380913258c342%20image.png?alt=media\&token=cf18e733-f8fe-4512-b41a-0b5efd74753b)

### Apdex Calculation

Luciq calculates an Apdex score that reflects the rendering performance of every screen or custom UI trace of your application. An Apdex score ranges between 0 and 1; the higher the value, the better the performance:

* Apdex score ≥ 0.94 — Excellent
* Apdex score ≥ 0.85 and < 0.94 — Good
* Apdex score ≥ 0.7 and < 0.85 — Fair
* Apdex score ≥ 0.5 and < 0.7 — Poor
* Apdex score < 0.5 — Unacceptable

The following color-code criteria is also applied:

![](https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FbNxuf72z443qFg3ayNj0%2F37326bd3bb8e04554de60dd1926b184486e649a006fc16eb204fa6e3623fe739%20image.png?alt=media\&token=237e7bad-2164-444f-bbff-ed3c99dd8955)

#### How is the Screen Rendering Apdex Calculated?

Every screen visit is categorized based on the frozen frames % and slow frames % of that occurrence using the logic shown below:

![](https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F9rPREgkoJA3qvhkeg66A%2Fee644093d60ddb1369b584928a6316eab0825ff7f3a88c48600733d4012b3652%20image.png?alt=media\&token=f3d2ca06-ddba-435f-b934-a91aadea38f0)

Following that logic, a Screen rendering occurrence is considered:

* **Satisfying:** if it has NO frozen frames & ≤ 10% Slow frames.
* **Tolerable:** if it has NO frozen frames & ≤ 50% Slow Frames.
* **Frustrating:** if it has ANY frozen frames & > 50% Slow Frames.

#### Screen Group Apdex Calculation

The Apdex score for the entire Screen Rendering group is then calculated as follows:

Apdex score = (Satisfying occurrences + 0.5 \* Tolerable occurrences) / Total occurrences

Where Total occurrences = Satisfying occurrences + Tolerable occurrences + Frustrating occurrences

Example occurrences:

{% stepper %}
{% step %}

### Occurrence A

5% Frozen Frames, 0% Slow Frames → Frustrating
{% endstep %}

{% step %}

### Occurrence B

0% Frozen Frames, 30% Slow Frames → Tolerable
{% endstep %}

{% step %}

### Occurrence C

0% Frozen Frames, 6% Slow Frames → Satisfying
{% endstep %}
{% endstepper %}

Apdex for that screen = (Satisfying occurrences + 0.5 \* Tolerable occurrences) / Total occurrences\
\= (1 + 0.5 \* 1) / 3 = 0.5
