# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/team-dashboard.md

# Team Dashboard

The Team Dashboard page helps track and improve your team’s ownership of screens by monitoring performance and stability metrics like app launch time, loading speed, UI hangs, and crashes. It allows leaders to identify and address issues affecting their team's areas, ensuring alignment with overall app performance goals.

<figure><img src="https://files.readme.io/221692d3fb8985968c8b5b2ddbaebe4e847303f000997ce84a68bd786432f3ed-flutter-team-dashboard-1.png" alt=""><figcaption></figcaption></figure>

You can find the page under the “App Overview” section in the Navbar

### Metrics Supported

#### **Performance Metrics Supported:**

* Cold app launch
* Hot app launch
* Screen loading
* UI hangs

#### **Issues you can assign to your team:**

* Fatal crashes
* App hangs
* Non-fatal crashes

#### **Team Dashboard Score Calculation**

Here’s the breakdown of the weighted average we use across the performance metrics supported to come up with your team’s dashboard score:

* Cold app launches weight: 24%
* Screen loading weight: 36%
* UI hangs weight: 40%

#### **Team Stability Score Calculation**

Here’s how we calculate your team's overall stability:

* Team stability = Number of screen visits of the screens assigned to your team that didn't end in a crash / Total number of screen visits of the screens assigned to your team.

### Setup Guide

To start using the Team Dashboard page, you need to follow these simple steps:

#### **Step 1: Create A Team**

If you don’t already have teams defined on your Luciq dashboard, you can do so by:

1. Click on your name at the top right corner
2. Choose Account Management
3. Choose teams
4. Click on Create your first team
5. Name your team and assign team members to it

#### **Step 2: Define Performance Metrics Ownership**

In order to see your team’s dashboard score, stability score, cold app launch apdex, screen loading apdex and UI hangs apdex, you need to define ownership for performance metrics.

<figure><img src="https://files.readme.io/dd4f20c3808e750b46aa4ccaf9b0cbb2d2670b1d88ee1f893c13f135e20bc258-flutter-team-dashboard-3.png" alt=""><figcaption></figcaption></figure>

1. Go to the settings page at the bottom left of the navbar
2. Choose Team Ownership
3. Click Define ownership
4. Choose Type “Performance metrics”
5. Choose the team you’d like to assign screens to
6. Choose condition Screens
7. For Screen name, you can search and select all screens you’d like to assign to that team

#### **Step 3: Define Crash Ownership**

In order to automatically assign fatal crashes, app hangs and non fatal crashes to your team, you need to define the ownership of crashes

<figure><img src="https://files.readme.io/b0b02c6e32cf19b0c1b3789e59350064e47bb2000518e8e77aefe3b54e0d6038-flutter-team-dashboard-5.png" alt=""><figcaption></figcaption></figure>

1. Go to the settings page at the bottom left of the navbar
2. Choose Team Ownership
3. Click Define ownership
4. Choose Type “Crashes”
5. Define the path, package, or file you’d like to assign crashes happening on to your team
6. You can also assign a specific crash to a team from the specific crash’s page
