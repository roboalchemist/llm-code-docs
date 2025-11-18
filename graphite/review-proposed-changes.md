# Source: https://graphite-58cc94ce.mintlify.dev/docs/review-proposed-changes.md

# Review Pull Requests

> Learn how to review pull requests on the Graphite dashboard.

You can be notified that a PR needs your review in Graphite in one of two ways:

* Pull requests appear in the *Needs Review* section of your pull request inbox

* Through the Graphite integration for Slack

## Start a review

You can start a review by hovering over a line number to leave a comment. Clicking the line number will allow you to leave a comment on a single line, and clicking and dragging across multiple lines will allow you to leave a comment that spans multiple lines of code. Graphite allows you to comment on both changed and unchanged lines of code.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a3cddb8a1be44bfd9be0ccb748350fbb" data-og-width="1350" width="1350" data-og-height="756" height="756" data-path="images/8e7821f8-1700537924-frame-10123324.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c354b2cfe20252b990a94c1f99c76976 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=695e76c722d87e0ba3f415ef0aa029c1 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f5870826f8d76933986ca1e65ab10aad 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=50ff5662a6a0d807c613aff35b5b3543 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7116104bae1b14be334211a2a2037fc3 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/8e7821f8-1700537924-frame-10123324.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f54915f21ff24162f360b31746ccd4d2 2500w" />
</Frame>

In the comment field, leave your comment. The commenting box provides a number of markdown formatting options to select from in the footer. You can switch between markdown and preview format for each comment by clicking the "eye" icon near the right corner of each comment box.

### One-off or batched comments

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=16d0d73b5cdf67cc8ec0d66d32972827" data-og-width="1350" width="1350" data-og-height="756" height="756" data-path="images/fe71f73c-1700538055-frame-10123325.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ed4e365009a99a30243ef3f4ad616549 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=a5d42ded91c75ab5fb2e675444adebc9 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=08a4149e2e7a71159ce7ff8e97eb88b1 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2226e2ddfa5643d27fad2ace7d92c7aa 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c54a0a8ddcef6ddff287d75d06e6c2e1 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fe71f73c-1700538055-frame-10123325.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1bd214d0a5c49d550fdeddf2ad867872 2500w" />
</Frame>

When you finish entering your comment, you can click the dropdown on the `post thread` button to either:

* Post thread: this posts the comment immediately. Great for one-off, non-opinionated comments.

* Add to review: this will add the comment to a "batch." Once you batch the comment, it will be pending and only visible to you until you've submitted your final review, at which point all of your batched comments will also be submitted.

If you chose to add your comment to your review, the review bar that's pinned to the bottom of the PR will light up to show how many comments you have pending.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=5e6bb7a4c2e760ea3a4c3c61be51fa7d" data-og-width="1350" width="1350" data-og-height="626" height="626" data-path="images/7a69657b-1700538163-frame-10123326.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=10f607834807ddef1f22484f64825307 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=dcda6110ab217771aa06d5f96d83d471 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=80e22dfb7bfb818ebbbdea1ad3a627ff 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f1c792a7c6b5e8ff19094746b4a9117d 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=e72dfb2d4440d1fabbcadfbbff197ce5 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/7a69657b-1700538163-frame-10123326.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=f2e86bd52d358b46e76fa0cd021dc992 2500w" />
</Frame>

### Suggested edits

While reviewing, you can directly leave a suggested code edit to streamline the review process. You can either add these manually yourself, or leverage Graphite AI to turn your plain English suggestion into a code edit - saving both reviewer and author time.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ff59645669a4317ae7d30e125e29c84c" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/ddb190d4-1705423210-ai-suggested-edit_static.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=8dedbd942c0c22496c1a487f9d1256ff 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2a4b6817b1fd1ea0a84a8501ee4add90 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=191e39ed1800008341bfef7eee6cf508 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=92f5cdff3eb33a1f6b88bdcac53fd9e2 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=c1d2f52b10f52493fecc74e93ad05310 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/ddb190d4-1705423210-ai-suggested-edit_static.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=2419bdb1b3504fb0e7c20fb14b54c3ea 2500w" />
</Frame>

## Leave a final review

Once you finish reading through and commenting on the contents of the pull request, you can leave a final review by hovering over the review bar that's pinned to the bottom of the PR page.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=16480ab9ab1f58f715ff40dee2ba26d6" data-og-width="1350" width="1350" data-og-height="626" height="626" data-path="images/465cf66a-1700538277-frame-10123327.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=280&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=bfb1f3a5b4eb5ffb1556c2c1d5cfb1d9 280w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=560&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=ad1b6386cdfa8b531b7afb39c5f4bfe5 560w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=840&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=46474eb9561e04bd31ff05e85cef686f 840w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=1100&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=02a36d193698ee5052d2dd8d919b26f1 1100w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=1650&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=aec111e5f5b513170f3071d30f9cce71 1650w, https://mintcdn.com/graphite-58cc94ce/vY1t0Vsr-LRJgMIn/images/465cf66a-1700538277-frame-10123327.png?w=2500&fit=max&auto=format&n=vY1t0Vsr-LRJgMIn&q=85&s=7cfb7b6754c7045b556407d2c52c3e52 2500w" />
</Frame>

After you've added a summary of your review, you have three options:

* Request changes

* Just add comments

* Approve

<Note>
  If you have any pending comments at the time you're leaving your final review, they will all be posted with your final review at once.
</Note>
