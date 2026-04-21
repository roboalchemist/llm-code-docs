<!-- Source: https://namespace.so/docs/solutions/github-actions/optimizing-usage -->

# Optimizing Usage

Monitor and optimize your GitHub Actions resource usage with Namespace's built-in insights dashboard. Understanding how your workflows consume resources helps you select the right machine shapes and reduce costs while maintaining performance.

## Resource Usage Insights

The insights dashboard provides detailed visibility into your workflow resource consumption across all your jobs.

![Resource usage insights dashboard showing job analytics](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finsights-resources.aa62444b.png&w=1920&q=75)

To get the most comprehensive view of your resource usage:

1. Navigate to [GitHub Actions → Insights](https://cloud.namespace.so/workspace/ghrunners/insights)
2. Change the view to **Sequential** (to see all job values back to back)
3. Set breakdown to **Job** (should be the default)
4. Change display to **Max Memory Used per Job (Percentage)**

This configuration will show you the peak memory usage for each job, making it easier to identify jobs that are over or under-utilizing their allocated resources.

## Finding Optimization Opportunities

If you have too many jobs to go through, you can easily filter them down to the right opportunities.

### Step 1: Filter Out High Memory Usage Jobs

1. Use **Alt+Shift+Cmd** (or **Alt+Shift+Ctrl** on Windows/Linux) to click on jobs that have more than 50% memory usage — this will filter that job type out
2. Keep doing this until you're only left with jobs under 50% memory usage
3. These are your optimization opportunities

### Step 2: Verify CPU Underutilization

1. Now switch the display to **Max CPU Usage**
2. Check if the same jobs also under-utilize their CPU
3. Jobs that show both low memory and CPU usage are prime candidates for smaller machine shapes

Jobs consistently running under 50% for both CPU and memory usage can likely be moved to smaller, more cost-effective machine shapes without impacting performance.

## Best Practices

1. **Regular monitoring**: Review insights weekly to identify optimization opportunities
2. **Baseline performance**: Establish performance baselines before making changes
3. **Gradual optimization**: Make incremental changes and measure impact
4. **Test configurations**: Use feature branches to test different machine shapes safely

The insights dashboard updates automatically, providing real-time visibility into how your optimization efforts impact resource usage and costs.

## Related Documentation

**[Caching Solutions →](/docs/solutions/github-actions/caching)**
Implement cross-invocation caching for dependencies and build artifacts to reduce execution time and resource usage.

**[Custom Base Images →](/docs/solutions/github-actions/custom-base-images)**
Pre-install dependencies in custom runner images to reduce startup time and optimize resource utilization.

**[High-Performance Docker Builds →](/docs/solutions/github-actions/docker-builds)**
Optimize Docker build performance with Remote Builders and caching strategies.

**[Advanced Configuration →](/docs/reference/github-actions/runner-configuration)**
Configure machine shapes and runner settings for optimal performance and cost efficiency.

Last updated March 9, 2026
