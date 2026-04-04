# Source: https://docs.intelligems.io/analytics/how-orders-and-sessions-are-attributed-to-experiments.md

# How Orders and Sessions are Attributed

## Attributing Orders to Sessions

Under the hood, Intelligems aggregates visitor actions into sessions. A visitor must visit a non-checkout page to initiate a session. Orders are attributed to the customer’s most recent session that was started before the order was placed.

For an order to match to a session, they need to be within 48 hours of each other. For example, if a user browses a store, adds to cart, but does not place an order, then, a few days later, receives an abandoned cart email with a direct checkout link and places the order, this order would not be attributed to the original session. This is because checkout page views are treated as a special case, and do not create a new session. So, the only session preceding the order is the original session, and that session is too far away to match since it occurred over 48 hours prior.

## Attributing Sessions to Experiments

The way Intelligems determines whether a session counts towards an experiment is simple: if the visitor was exposed to the experiment during the session, then it counts. So, if the customer was exposed to an experiment during the session that’s matched to an order, then the order counts towards the experiment’s results.

User attributes like source site/channel, country, etc. are taken from the first session for that user for that experiment. For example, if a user has a first session where their referrer was Facebook, and then comes back later directly and makes an order, and in both sessions the visitor was exposed to the experiment, then that would be: one visitor in the experiment (with two sessions), the order would count (because the order is attributed to the second session, which is included in the experiment), and the source site for that user (and order) would be Facebook, because that was the source of the first session for that user for that experiment.
