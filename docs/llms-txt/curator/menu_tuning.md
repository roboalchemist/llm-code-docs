# Source: https://docs.curator.interworks.com/best_practices/performance/menu_tuning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Menu Tuning

> Optimize menu system performance with tips and configuration recommendations

## Menu Overview

While Curator’s menu system is about as streamlined as possible, there are some tips and tricks you can use to tune its
performance if fancy yourself as a Vin Diesel type. Most of the delays Curator clients see when rendering their
navigation relates to the permission checking that ensures each user only sees the links they have access to view. One
of the big selling points with Curator is that it inherits permissions from the connected platforms by default, so this
is a necessary step. The good news is that Curator does cache all of those permission checks, so it’s really only an
issue when users first log in to Curator for the day. However, that’s also the first impression users get to your
Curator portal, so it’s understandable that this should be as fast as possible. With a little thought, this is where
performance gains can be realized.

## The Obvious Stuff

The first thing to check is always that Curator and any platforms it is connected to are running at full speed. If your
Tableau Server is underpowered or is being bombarded by users, that will slow down the permission checks Curator needs
to make. Same goes if the network connection between Curator and the other platforms is handled by letter-carrying
snails instead of bullet train-esque transfers. Lastly, the most common cause of general performance issues with Curator
itself is file system speed. If the storage mounted to your Curator server runs through the laziest of digital
stonemasons hand chiseling each bit on the drive platters, it’s going to slow down things like Curator’s caching system
and generally make life unbearable. Many times, the file system itself is fast but malware detection running on the
server prevents it from running at full speed.

## Short-Circuiting

Let’s say your main navigation is organized by high level categories. If most of your users only have access to one or
two of those categories, then it doesn’t make sense to check permissions on each link under the others. By using
Curator’s restrict access functionality, you can set which groups have access to each category and this will essentially
short circuit the permission checking for any top-level categories where the user is restricted.

For instance, if you have a category for human resources and you set its restrict access to only allow users in the HR
group, any user who isn’t in the HR group will skip checking the links under the human resources category. Any
permission checks that get skipped means the navigation will render that much faster.

## Utilizing Landing Pages

If you’ve got hundreds or thousands of links in your navigation and can’t use the short-circuiting approach above, then
you could try creating landing pages for sections of the navigation to reduce the number of links it needs to check
permissions against.

Using the same human resources example, you could create a human resources page that has links to the various human
resources content using the built-in tiles or lists. When you add this page to the navigation, Curator only has to check
whether the user is allowed to see that page, which should be quick. Only when a user clicks to open that human
resources page will Curator check permissions for each of those links on the page. If you repeat this for several
sections of the navigation, it really cuts down on the number of permission checks the menu system needs to make before
showing the home page.
Combining Tableau Workbooks

The way Curator checks permissions for Tableau is by getting the list of workbooks a user has access to on a per site
basis and then checking which dashboards are in each of those workbooks. This means that if you have a million
dashboards and they are all in their own workbook, Curator is going to have to make a million API (application
programming interface – or a fancy way to say that Curator is talking to Tableau) calls to Tableau just to determine
whether a link should be shown in the navigation. On the other hand, if you combined those into a single workbook with a
million dashboards, Curator would only have to make one API request to Tableau to check. While your network connection
and Tableau Server might be supercharged, there will always be overhead delays when increasing the number of API calls
over the web. By minimizing the number of API calls, you’ll see better performance.

## Combining Tableau Sites

Tableau sites are wonderful for making sure your various audiences are segregated from each other, since each site is
independent from the others. However, this also means that if you have content published from multiple sites, Curator
has to make separate API calls to check permissions for each one. Like combining your dashboards into fewer workbooks,
combining your workbooks into fewer sites will also see those gains.
Connecting to Tableau Server’s Repository

As mentioned earlier, making API calls between Curator and Tableau incurs some overhead which slows down the process. An
alternative to that is allowing Curator to connect directly to Tableau Server’s underlying database (AKA repository).
This avoids a lot of that overhead. Additionally, Curator is able to create custom queries to pull exactly the
information it needs in a single request. This includes checking all workbooks at the same time as well as only
requiring Curator to authenticate once instead of once per Tableau site. Needless to say, whenever Curator can use the
repository connection instead of the API, it’s able to shave precious seconds off of its quarter mile time.

Unfortunately, connecting to the repository is only possible for Tableau Server; so if you’re using Tableau Cloud, this
won’t be an option for you.

## Warming the Cache (Advanced)

As you’ve probably seen in a lot of motor sports, racers often spin their tires to warm them up before a race. This
increases traction and allows them to go faster around the track. Since Curator uses cache for permission checks, one
way you can make it go faster around the track is to warm its cache at the beginning of each day. In a nutshell, this is
scheduling something each morning to call Curator’s API to generate the navigation for each user before they try to log
in for the first time. When a user does log in for the first time, all of the permission checks will have already been
cached, so Curator can build the navigation fast and furious.

Curator’s API end point can be found at /api/v1/Content/generateNavMenus. You’ll need to pass it a valid API key, the ID
of the menu to generate, and the username to generate it for. Documentation on how to call this API endpoint can be
found by navigating to Backend >Settings >Curator >API Keys, click on one of the keys, and change the drop-downs at the
bottom to “Content” and “generateNavMenus,” respectively.

If you don’t have a good way to schedule API calls, you can take advantage of Curator’s automation scripts. This feature
is disabled by default, so to enable it navigate to Backend >Settings >Curator >Portal Settings >Features tab >
Functionality Section >Integration Automation switch and save. Once enabled, refresh the page and you should see a new
section under Backend >Integrations >Automation to create scripts or commands. This is an advanced topic, so we’ll leave
the rest up to you to implement, but if you want to create a script to call the API you’ll use Manage Scripts. If you
want to issue commands on Curator’s server to call the API, you’ll use Manage Commands. Both can be configured for
whatever schedule makes sense in your environment.
