# Source: https://getlago.com/docs/guide/lago-self-hosted/update-instance.md

# Versions update

Lago's speed is rapidly increasing—remarkably fast. Billing updates occur frequently, precisely every 1 or 2 weeks. Over the course of a year, we've completed over 70 releases, culminating in approximately 30 comprehensive product updates. Maintaining the currency of your self-hosted instance is paramount for optimal billing engine functionality and alignment with the newest features. Below is a guide to achieve this seamlessly, all within the span of just 5 seconds.

<Frame type="glass">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/updates.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=d38fea58f8a50765387cf4ef3bf4c802" data-og-width="1456" width="1456" data-og-height="910" height="910" data-path="guide/images/updates.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/updates.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=3da91620d58ee73aca4be811564c7a46 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/updates.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9d1ec7af9d9cc41332332df63000f098 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/updates.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=d79101aa013272ae7fcbcf75d179fe1a 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/updates.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=d865cff5b1aa90d5ee926b005ecc249d 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/updates.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=13a85f563c9b9ea0e83800a537ceb719 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/updates.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=0c3c60bb0c9982df30497b9d8a1dc1c1 2500w" />
</Frame>

## Why update your Lago self-hosted instance?

### Bug fixes and security enhancements

Updating your Lago open source instance serves a key purpose: resolving bugs and enhancing security protocols.
Just like any software, glitches may emerge, impacting operations and even jeopardizing security.
This is particularly vital in intricate tasks like metering, billing calculations, tax application, and managing financial statements.
By keeping up with updates, you guarantee your instance remains unaffected by recognized problems and vulnerabilities.
This proactive approach maintains a resilient and secure operational landscape for your company.

### Access to new features

Lago consistently evolves to meet the needs of its users. Each update introduces a host of new features aimed at enhancing the user
experience and expanding the capabilities of the platform. Some notable new features that updates might bring include core billing
enhancements, tax-related features, and additional settings options. By updating regularly, you can take advantage of these features and
streamline your workflows.

## Determining update frequency

The frequency of updates varies based on the development cycle of Lago. Generally, updates are released approximately once a week.
Keeping an eye on the [release notes](https://github.com/getlago/lago/releases) provided by the Lago team will give you insight into when updates are available and what changes they
entail. Regularly monitoring these release notes will allow you to stay informed and plan your updates accordingly. Billing updates occur
frequently, precisely every 1 or 2 weeks. Over the course of a year, we've completed over 70 releases, culminating in approximately
30 comprehensive [product updates](https://www.getlago.com/changelog).

## A seamless update process

Updating your Lago open source instance doesn't have to be a daunting task. With a clear procedure in place, you can ensure
a smooth transition to the latest version. Here's a step-by-step guide to help you navigate the update process:

### 1. Access your instance repository

Navigate to the repository where your Lago open source instance is stored. This is typically where you initially cloned or
downloaded the instance.

### 2. Check you current version

In the repository directory, execute the following command to check the current Lago version:

```bash  theme={"dark"}
git describe --tags --abbrev=0
```

### 3. Check for the bridge releases

<Note>
  Bridge releases are released as mandatory intermediary relased that must be installed before upgrading to higher versions.
</Note>

Check the migration guides for (bridge releases)\[[https://getlago.com/docs/guide/migration](https://getlago.com/docs/guide/migration)] and follow the update instructions for each intermediary releases.

### 4. Fetch the latest release

Still in the repository directory, execute the following command to pull the latest release from the remote repository:

```bash  theme={"dark"}
# Fetch all tags
git fetch --tags

# Checkout the latest tag
git checkout $(git describe --tags --abbrev=0)
```

This command fetches the most recent release from the remote repository and merges them into your local instance.

<Note>
  To fetch the code of a specif release, use the following command:

  ```bash  theme={"dark"}
  git checkout v1.29.0 # Replace with the right version number
  ```
</Note>

### 5. Restart the updated instance

Once the code is up-to-date, navigate to the directory containing your Docker Compose file.
Execute the following command to start the updated instance:

```bash  theme={"dark"}
docker compose up
```

This command will rebuild and launch your Lago instance with the latest changes.

### 6. Testing new features

After the instance restarts, you can now test our new features and give feedback to the team.

## Addressing concerns about breaking changes

It's natural to be cautious about updates, especially if you fear breaking changes that might disrupt your operations. However, the Lago team understands this concern and takes proactive measures to ensure a smooth update experience. By applying careful consideration to database and UI migrations, Lago mitigates the risk of breaking your application during updates. This thoughtful approach ensures that your workflows and user interfaces remain consistent even after applying the latest updates.

In conclusion, updating your Lago open source instance is a proactive step toward maintaining a secure and feature-rich environment for your operations. By staying current with bug fixes, security enhancements, and new features, you can harness the full potential of the platform. With a well-defined update process and the Lago team's commitment to stability, you can confidently keep your instance up-to-date, ensuring a seamless and productive experience.
