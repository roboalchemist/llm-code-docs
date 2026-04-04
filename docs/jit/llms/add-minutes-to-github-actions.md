# Source: https://docs.jit.io/docs/add-minutes-to-github-actions.md

# Add minutes to GitHub Actions

## Overview

Jit uses GitHub Actions to run its scans, both daily/weekly and PR scans. GitHub offers free minutes for all GitHub customers, however, these may be used up not only by Jit but by other tools and pipelines. When these free minutes run out, if there is a plan limit, Jit may stop working.

| Plan                          | Free Minutes (per month) |
| :---------------------------- | :----------------------- |
| GitHub Free                   | 2,000                    |
| GitHub Pro                    | 3,000                    |
| GitHub Free for organizations | 2,000                    |
| GitHub Team                   | 3,000                    |
| GitHub Enterprise Cloud       | 50,000                   |

## Solution

Follow [GitHub's documentation ](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)to add GitHub Action minutes