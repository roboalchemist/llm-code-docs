# Source: https://docs.intelligems.io/analytics/experiment-analytics/how-experiment-targeting-affects-analytics.md

# How Experiment Targeting Affects Analytics

For each test, you can either apply targeting rules or let it run for all visitors. If you do set up targeting, it can impact how the experiment interacts with analytics in a few different ways:

## Audience Targeting

Audience targeting defines which visitors are eligible to enter an experiment. By default, if a visitor does not meet targeting rules, they will not enter an experiment, but may still enter in the future if they do meet the rules. If the visitor does enter the experiment in the future, they would then be included in analytics. Instead of this default behavior, there is an option to exclude visitors if they do not meet the targeting rules. In this case, the visitor would be permanently excluded from the experiment and therefore analytics.

## Page Targeting

When using page targeting, an experiment is active only on the targeted pages. A visitor must reach a targeted page to be included in experiment analytics, and if they make an order, that order 1) must be attributed to a session in which they were exposed to the experiment and 2) must have have been placed after the visitor entered the experiment. For example, if my experiment is targeted on the homepage, and a visitor lands on a product page, adds to cart, and makes an order, then afterwards goes to the homepage, they will have entered the experiment and count as a visitor (because they went to the homepage), but their order will not count towards the experiment, because it was placed before the visitor entered the experiment.

## Split URL and Template Tests

For a visitor to enter a Split URL or template test (experiments that include a page redirect), they must go through the redirect by visiting the origin URL or a page using the control template. Unlike with page targeting, on subsequent sessions, even if they do not go through the redirect again, Intelligems will still consider them as being exposed to the experiment. For example, say a visitor goes through a redirect in one session, leaves the site and returns in a new session the next day, then immediately places an order. That order will be included in analytics, even though the visitor did not go through the redirect in the second session which created the order, because Intelligems still considers the experiment active in the second session.
