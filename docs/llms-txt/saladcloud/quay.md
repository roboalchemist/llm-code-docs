# Source: https://docs.salad.com/container-engine/how-to-guides/registries/quay.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quay Container Registry

*Last Updated: October 15, 2024*

In order to use Quay you need to have an organization and account at Quay. If you already have, you can skip step 1 and
follow the guide from step 2.

### Step 1: Create Quay Account

Begin by creating a Quay account for yourself or your organization at [Quay](https://quay.io).

### Step 2: Create Public/Private Repository

Inside your Quay account, create a public/private repository where you'll store your Docker images securely.
<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-create-repo.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=225cd723272a678f950cdf09c735a7e5" alt="Create private repository" data-og-width="1130" width="1130" data-og-height="333" height="333" data-path="container-engine/images/quay-create-repo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-create-repo.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=eb7766066824446f126ee9fe7be62540 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-create-repo.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b3d6dbcf06a234cba826e83c33ff4ec9 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-create-repo.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c95aa7c746451b3c33d3fd79970c2a16 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-create-repo.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2b462a3627e8842cab57789418ee1edc 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-create-repo.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b35be7f685dc8317373fbf96d567d952 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-create-repo.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=861e77eb844caf9edad8d0bed3110254 2500w" />

### Step 3: Initialize the Repository

Initialize your private repository in one of these ways:

1. **Dockerfile**: If you have a Dockerfile, you can use it to initialize your repository.
2. **GitHub Repository Path**: Link your Quay repository to a GitHub repository to automate image pushes.
3. **Bitbucket**: Similar to GitHub, link your Quay repository to a Bitbucket repository for automated image pushes.
4. **Custom Git Repository**: Link to a custom Git repository if your code is hosted elsewhere.

### Step 4: Build the Image on Quay Portal

Use the Quay portal to build the Docker image associated with your private repository. Follow the on-screen
instructions. <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-build.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=760cddf93d75a8509742264e95226eda" alt="Build image on Quay portal" data-og-width="1259" width="1259" data-og-height="324" height="324" data-path="container-engine/images/quay-build.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-build.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c19fcb042ec763b5c3984a9b0c9ff4e0 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-build.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=74c2c76555f1845755b8a05b1d373631 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-build.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3330bbd029f062f909ed8d1e716498bb 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-build.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c2cf0ceb8fc05283b05934c80963d6ce 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-build.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=cfe441c90d3ffc1e2d4166645ca0e951 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-build.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=1552579292f4ab58286d5c38cbdce242 2500w" />

### Step 5: Configure SaladCloud Container Environment (SCE):

Access the SaladCloud portal and set up your SCE by selecting the private registry tab when setting the image source. In
the service dropdown option, choose "Quay Container Registry," and provide the following information:

1. Quay username and password.
2. Image name from your private Quay repository

<img src="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/configure-quay.png?fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=8b96bd10ffbd37dbd4d5f620a7354569" data-og-width="1279" width="1279" data-og-height="847" height="847" data-path="container-engine/images/configure-quay.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/configure-quay.png?w=280&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=3673b373b9c8c08981dd05edb96a7ab0 280w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/configure-quay.png?w=560&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=e91d4421af87a846517c76fc7b6740f4 560w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/configure-quay.png?w=840&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=3f4ad4acb88a7ce677ddbd22a94b5421 840w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/configure-quay.png?w=1100&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=d111539941ce74daac974d4d3a95dcc4 1100w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/configure-quay.png?w=1650&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=cea2d192dcbc4799463c906c0cea8fe0 1650w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/configure-quay.png?w=2500&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=e9866f335590c60b6316d78f45879a34 2500w" />

### Step 6: Start the Container

With all configurations in place, click the "Start" button in the SaladCloud portal to launch your container using the
private Quay registry image.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-running-group.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e4c109540f0c1af6df0cd330777e066d" data-og-width="1312" width="1312" data-og-height="496" height="496" data-path="container-engine/images/quay-running-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-running-group.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f7cf0b081bc3b1128ada0dc1e5a1571d 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-running-group.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=454efa9a01592b618fd639b97c648ecf 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-running-group.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=677393bab8e23e87672e431e21dc9512 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-running-group.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=125b5224828618c89876b3d9eef50022 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-running-group.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=39bba7269564f0a157f6466b12172891 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/quay-running-group.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=26e83dd32c385c8d64ff176d234da607 2500w" />

> 👍 Congratulations!
>
> Your container is now up and running, utilizing the image stored securely in your private Quay repository.
