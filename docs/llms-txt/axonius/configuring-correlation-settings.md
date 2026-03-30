# Source: https://docs.axonius.com/docs/configuring-correlation-settings.md

# Configuring Correlation Settings

## Correlation Settings

It is not recommended to change the correlation settings without consulting with your Account Manager.
For more details about correlation settings, contact [Axonius Support](mailto:support@axonius.com).

## Correlation Schedule Settings

**To configure correlation schedule:**

1. From the top right corner of any page, click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Data**, select **Correlations**, and scroll to the bottom of the page to the **Correlation Schedule** section.

![CorrelationSchedule](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CorrelationSchedule.png)

**Enable correlation schedule** *(required, default: switched off)*

* Toggle on to specify the number of hours between asset correlation calculations. Only one correlation can run at once, meaning, correlation runs as part of each discovery cycle and is based on the configured scheduling.

* Toggle off to calculate asset correlation as part of the discovery cycle.