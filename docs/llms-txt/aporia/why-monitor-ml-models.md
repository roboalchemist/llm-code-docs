# Source: https://docs.aporia.com/core-concepts/why-monitor-ml-models.md

# Source: https://docs.aporia.com/v1/core-concepts/why-monitor-ml-models.md

# Source: https://docs.aporia.com/core-concepts/why-monitor-ml-models.md

# Source: https://docs.aporia.com/v1/core-concepts/why-monitor-ml-models.md

# Why Monitor ML Models?

You spent *months* working on a sophisticated model, and finally deployed it to production.

8 months later, and the model is still running. Making amazing predictions. Increasing business KPIs by a ton - boss is happy. Satisfied with the results, you move on to this next-gen super cool deep learning computer vision project.

**Sounds like a dream?**

![To Production and Beyond](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F9gzmVNCmvR26i4areXJs%2Fto-production-and-beyond.jpg?alt=media)

***

### The Real Work Begins

Even though we spend a lot of time training and testing our models, *the real work begins when we deploy them to production.* It's one of the most fundamental differences between ML and traditional software engineering.

With traditional software, most of the work is done during the development phase, and once the system is up and running - as long as we've tested it thoroughly - it usually works the way we planned.

With Machine Learning, it *doesn't matter* how well we test our models after training them. **When models run in production, they are exposed to data that's different from what they've been trained on.** Naturally, their performance degrades over time.

### Simple Workflow for ML in Production

Don't panic! Even though models in production do degrade over time, it doesn't mean you'll have to actively take care of each one of them every single minute they're in production.

With two simple principles, you'll be able to move on to that super cool next-gen computer vision project, while knowing your production models are in safe hands:

#### 1. Build a Custom Dashboard

Each one of your models should have a customized production dashboard where you can easily see *the most important metrics* about it. **Put something on your calendar**, and take a look at these dashboards from time to time, to make sure your models are on track!

![Custom Dashboards](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FidvRA9LWpa0iR2EPITs4%2Fcustom-dashboards.png?alt=media)

**Bonus points** if you put your dashboard on a big TV screen in the office!

#### 2. Set up important alerts

You should also set up alerts to detect drift, performance degradation, data integrity issues, anomalies in your custom metrics, etc.

To avoid false positives and alert fatigue, make sure to customize the alerts so they only trigger when something important happens.

![Monitor Builder](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FPw4zlFSBxKwWZwDfZ0d2%2Fmonitor-builder.png?alt=media)
