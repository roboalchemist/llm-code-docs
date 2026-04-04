# Source: https://gitbook.com/docs/help-center/further-help/how-do-i-generate-a-har-file.md

# How do I generate a HAR file?

A **HAR capture** (HTTP Archives) records your browser's requests and responses with the GitBook Application, allowing our support team to investigate the issues you are experiencing further.&#x20;

{% tabs %}
{% tab title="Chrome" %}

1. In Chrome, go to the page within GitBook where you are experiencing trouble.
2. At the top-right of your browser window, click the Chrome menu (⋮).
3. Select **tools > developer tools**. The developer tools window opens as a docked panel at the side or bottom of Chrome.
4. Click the **network** tab.
5. Select **preserve log**.
6. You will see a red circle at the top left of the Network tab. This means the capture has started. If the circle is black, click the **black circle** to start recording activity in your browser.
7. **Refresh the page** and reproduce the problem while the capture is running.
8. After successfully reproducing the issue, right-click on any row of the activity pane and select **Save as HAR with content**.
9. Select the **console** tab.
10. Right-click anywhere in the console and select **save as...**
11. Name the log file **Chrome-console.log**.
12. Send both files as shared links in a reply to your case.
    {% endtab %}

{% tab title="Firefox" %}

1. In Firefox, go to the page within GitBook where you are experiencing trouble.
2. Click the Firefox menu (Three horizontal parallel lines) at the top-right of your browser window.
3. Select **web developer > network**.
4. The developer tools window opens as a docked panel at the side or bottom of Firefox.
5. Click the **network** tab.
6. Select **persist logs**.
7. **Refresh the page** and reproduce the problem while the capture is running.
8. After reproducing the issue, right-click any row of the activity pane and select **Save all as HAR**.
9. Select the **console** tab.
10. Right-click any row and select **select all**.
11. Paste the content in a text file and name it **console-log.txt**.
12. Send both files as shared links in a reply to your case.
    {% endtab %}

{% tab title="Safari" %}

1. In Safari, go to the page within GitBook where you are experiencing trouble.
2. In the menu bar at the top, click **Develop** and select **Show Web Inspector**.
3. Click the **console** tab and select **preserve log**.
4. Go back to the **network** tab.
5. **Refresh the page** and reproduce the problem while the capture is running.
6. After successfully reproducing the issue, right-click any row of the activity pane and select **export HAR**.
7. Click the **console** tab.
8. Right-click any row and select **select all**.
9. Paste the content in a text file and name it **console-log.txt**.
10. Send both files as shared links in a reply to your case.
    {% endtab %}

{% tab title="Internet Explorer (IE11)" %}

1. In Internet Explorer, go to the page within GitBook where you are experiencing trouble.
2. Click the gear icon in the top right.
3. Select **F12 developer** tools.
4. Click the **network** tab.
5. Clear the **entries on the navigate** option, which is selected by default. The icon looks like a blue arrow with a red X.
6. The green play button (**start profiling session**) should be selected by default. This means the capture function is running.
7. Refresh the page and reproduce the problem while the capture is running.
8. Once you have reproduced the issue, click the **export as HAR** icon. The icon looks like a floppy disk.
9. Click the **console** tab.
10. Right-click any row and select **copy all.**
11. Paste the content in a text file and name it **console-log.txt**.
12. Send both files as shared links in a reply to your case.
    {% endtab %}

{% tab title="Edge" %}

1. In Edge, go to the page within GitBook where you are experiencing trouble.
2. At the top-right of your browser window, click the Edge menu (⋮)
3. Select **developer tools**.
4. Click the **network** tab.
5. Clear the **entries on the navigate** option, which is selected by default. The icon looks like a blue arrow with a red X.
6. The green play button (**start profiling session**) should be selected by default. This means the capture function is running.
7. Refresh the page and reproduce the problem while the capture is running.
8. Once you have reproduced the issue, click the **export as HAR** icon. The icon looks like a floppy disk.
9. Click the **console** tab.
10. Right-click any row and select **copy all.**
11. Paste the content in a text file and name it **console-log.txt**.
12. Send both files as shared links in a reply to your case.
    {% endtab %}
    {% endtabs %}
