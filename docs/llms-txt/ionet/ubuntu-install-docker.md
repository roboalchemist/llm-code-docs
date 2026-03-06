# Source: https://io.net/docs/guides/workers/ubuntu-install-docker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ubuntu: Install Docker

> A step-by-step guide for installing Docker on Linux-based machines

<iframe width="100%" src="https://www.youtube.com/embed/phTIvWLXj-I" title="Docker Guide for Linux" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### What is Docker?

Let's take a quick look at what **Docker** is? Imagine Docker as a magic box where you put your software and everything it needs to run. This box can be easily carried to any computer, and when you open it, your software works just the way you packed it, without needing anything extra from that computer. Here are a few steps to install Docker:

### Before installing Docker, please check if it is already installed

Run the following command to verify if Docker is not installed:

```
docker compose version
```

If you see the following error, you can proceed with this guide:

```
Command 'docker' not found, but can be installed with:
sudo snap install docker         # version 24.0.5, or
sudo apt  install podman-docker  # version 3.4.4+ds1-1ubuntu1.22.04.2
sudo apt  install docker.io      # version 24.0.7-0ubuntu2~22.04.1
See 'snap info docker' for additional versions.
```

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e06b3d21ffe000c4d763fe95aecab800" alt="" data-og-width="2096" width="2096" data-og-height="534" height="534" data-path="images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=9ae01ddd61368915829a1b4ec097ac3b 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f6ac90637c019a9c7c909a8c07d04e78 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=a7cf7f0143e2f75f8f52fcad6056ccc3 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=bf7e121ee3e3862fd3aca4f608c9bd6c 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=46e456959ed2eca2411e73c5c9dcdaf6 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42529592fb80df67a21db51dba23f3047b7e4a44e8bd8749aef557d622818a54-linuxDocker1.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=53617097ac8e7f6919f6d31d59a5cccf 2500w" />
</Frame>

### 1. Download Docker

Go to the [Docker website](https://www.docker.com/products/docker-desktop/) and click on "**Download for Linux**." You will be redirected to a page with supported Linux platforms.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=7afab17a24779fab604400caaf843b73" alt="" className="mx-auto" style={{ width:"76%" }} data-og-width="1930" width="1930" data-og-height="1162" height="1162" data-path="images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=92aa48df9e5e414aab4105e55e1d9619 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=2c72e605f14f79f08e147cd333d08d50 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=29bafcab7471707ea1fd5fc2c089d166 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=017862f178dc10fcae07bbd15979d8e6 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=dac9d39844f0d5a0b8c3935c13d7515b 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ecc37b57949cf7c8f434d6e045dcd8aa81a6d5975d34f4fb21014f90ab35f58d-linuxDocker2.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=04c95d0874b023d75f10bab3d4514b44 2500w" />
</Frame>

### 2. Download the appropriate version for your system

Select the appropriate version for your system, such as Ubuntu, and click on the link in the **"Supported platforms"** section of the page. Downloading the Docker file may take some time. Please be patient.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=3faace4f006f82899961f3664a6636e7" alt="" data-og-width="1910" width="1910" data-og-height="902" height="902" data-path="images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f445f0852bafe631230a861e24c161d6 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2001bcaaca58036cde3210c41c00e1c5 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f4cb56e11bc6b5c2e678db3083072b13 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=25d7024474ef912d1ef75029dabf7c78 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=89d7ac4f41122d55eb1ddbf98a42c92c 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/42f5d44e9cd5deb0958b35ab51ba2d630c22c6e1dac908cf0a0bedb0e2127a5d-linuxDocker3.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=81b899bfd937cd34bfff8f8d2455345b 2500w" />
</Frame>

### 3.Open the Ubuntu Terminal

through the Start Menu

**Terminal** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

Click the **Start Menu** icon, start typing "**Terminal**" in the search field, then click the **Terminal** icon:

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=8767ecb91e33a58431b6c72bd805e253" alt="" className="mx-auto" style={{ width:"69%" }} data-og-width="1830" width="1830" data-og-height="1036" height="1036" data-path="images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=1a3bd73ebed4388eb817d8a699f7aaae 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=b841cfeec0da9b039e5834f3107035d9 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=01b63561689eda313bc2ada867f1f29e 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=efdd79a5edd76917f9783501f9cd491f 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6ea4f17b497b5a519383117b56ccb2ca 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/45446c6e23adfd8969639f804c3a830b2c163b30ac23016a865eae007ad2aafd-linuxDocker4.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=0d36d3c0c0e2ba3a2955416bf0f33797 2500w" />
</Frame>

### 4. Copy and run the first command

Return to the Docker page and copy the first command from the "Install Docker Desktop" section:

```
sudo apt-get update
```

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=b7d4d76c939046af087fb27cda81cadf" alt="" data-og-width="1556" width="1556" data-og-height="962" height="962" data-path="images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=aba712dcf456046cf68d793752eeb8d7 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=969ef36f7bf1efc5adffa416dc2528be 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=db5a0277b2c3cba07f012f93276936f4 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ab485ec3664973d091adaa81a081cad1 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=8b9541c1edb888fd42276d49832da40a 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/20d54c1ef7cf10e2fb4be5b56139d90d1683fc7bba629d8acc4796285f7fb0eb-linuxDocker5.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=a71d0177069d8431b8a7c80ec12b1b54 2500w" />
</Frame>

Paste the command into the Terminal and press Enter. After that, you will be prompted to enter your password for confirmation. Type your password (note that it will not be visible while typing) and press Enter again.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=45daabe953a4b92818678a123b86605e" alt="" data-og-width="2096" width="2096" data-og-height="1516" height="1516" data-path="images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=22f28d64b1eb726e4876b8c03e3a73e5 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=fcc240a0b43c601cbb606639992eadc5 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=1f6e6d0ed73c8b32366713733a677a4e 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=afcc5e685e7c67762c1338f2bd97dbbd 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=ff283abc3b74b63d32da0b72841a60c6 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a909e45586db81618cb470b43d4723916606aef957e20b32c7df3f9859bb8b2d-linuxDocker6.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=3fc40b6a37b49afc0c4926deb70ab544 2500w" />
</Frame>

### 5. Check the .deb package

In the Terminal, you need to check the name of the downloaded file. First, navigate to the "Downloads" folder by typing this command:

```
cd Downloads/
```

Then, enter the following command to see the list of files in the "Downloads" folder:

```
ls
```

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=dd7b3b415fc8483750903ba86509e92e" alt="" data-og-width="2096" width="2096" data-og-height="560" height="560" data-path="images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=7b3784c760055d373d5a985afaef4fab 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=38a0127d13bd37498adc169cef15d1a2 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=ad8dfdd0fb894896eae4bb3841b3eaa7 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=24a3db14cc9dc40468fd0f9425101c55 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=15dcc01d62009c61b43e76586ccce4da 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9d80b344194b1b96b8bf698940278a7ce741e6f63a75a30abe354dd8a058716-linuxDocker7.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=1fd43203166c3d21766de033befb6fd8 2500w" />
</Frame>

### 6. Copy the installation command

Return to the Docker installation page and copy the second command from the "Install Docker Desktop" section:

```
 sudo apt-get install ./docker-desktop-amd64.deb
```

<Warning>
  Make sure to replace the package name with the correct one from the Terminal (based on what you saw in the previous step).
</Warning>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=ad838fcd33517a0f07754241d16252cd" alt="" data-og-width="1556" width="1556" data-og-height="962" height="962" data-path="images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4a793a06525fb522a418a4d485750528 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=219b090aa6f227cc71a59915d1486f21 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=af8a3dc54922677ed3ab45e970dad82e 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=c43e5969c678fa70b751c55a9c3f4b77 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=39c0de31c3e64b148a4687b6c6372142 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e97ccf28cd35400b306b483990d8256a596438b8db37321ecb49db2a4b8b74a8-linuxDocker8.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6bd047c32b6d04603f48f6fff0107a66 2500w" />
</Frame>

Paste the command into the **Terminal** and press Enter. After that, you will be prompted to enter your password for confirmation. Type your password (note that it will not be visible while typing) and press Enter again.

<Danger>
  If you encounter an error related to the absence of Docker CE-CLI during the installation, you can follow this detailed guide: [How to Install Docker CE on Ubuntu](https://www.rosehosting.com/blog/how-to-install-docker-ce-on-ubuntu-22-04).

  After completing the steps, you can continue installing Docker Desktop from where you left off.
</Danger>

During the installation process, you will be asked to confirm if Docker can use some space on your computer. Type **Yes** to complete the installation successfully..

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=ba068d1ea4a4a777e03ce304ece09878" alt="" data-og-width="2096" width="2096" data-og-height="1736" height="1736" data-path="images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=72d6ae7fa3196ab323d0b97d8f5f7acf 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=b7021a5b80eef7fb5ba78a837b996b12 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=7e5e1d8eeb587c0e834e878ee531a2f5 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=8adffc984a8c40d3765e4c22cb7bb35c 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=205862b16a7e73555b87090c40fd9749 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/19518168ba3e69135722b37e366099499016b3eec1f2ea07a84caf0508b18e5c-linuxDocker9.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e4f70da32690a84263a4975543ffd127 2500w" />
</Frame>

<Warning>
  You must restart your device after installing Docker Desktop; otherwise, the system may not allow you to use it properly, even if Docker appears to be running.
</Warning>

### 7. Run the Docker Desktop

Return to the Docker installation page and copy the command from the "Launch Docker Desktop" section:

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=ec651838777c58a5140dd52dc226312b" alt="" data-og-width="1556" width="1556" data-og-height="1030" height="1030" data-path="images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=85aeb7ba661f169bb4bdfd8d8ea005ad 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=ea47b8628acce48246916d40f540958b 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c3e78e2a1876fdc9840a515b4cdcafaa 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=1f3c73d3b7544f4c8b992b121dba2dc8 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=58e717041342fee24e63f2384b530a17 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/69088b96ed2cd5660233bb54cb1391580328cb16a8551dc49b2bcab4607955ca-linuxDocker10.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=bfd5c190c4c2ec749bc6ef4fcb3b1647 2500w" />
</Frame>

Paste the command into the Terminal and press Enter. If there are no issues with the installation, Docker should be running.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=418679661108723d3e53d91943374afc" alt="" data-og-width="2096" width="2096" data-og-height="438" height="438" data-path="images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=99ae5a936c37d4ec87a2bf3579ef51fd 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=002483e6fe3a47e0bd57457ef7d21d40 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=079f182a162300aee0a03221e489eca5 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ead2c0c0c3d247c334ae2e8052b72096 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=477033acc3b933283829d141b15f9b5d 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fc9e20d29d8f572a676c8e58e41aefb2c44e252e72223c155289d02cdb30033-linuxDocker11.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=0c76fdd84c40dcc587dbb053d89deb9a 2500w" />
</Frame>

### 7. Verify that Docker Desktop is Successfully Installed

Copy and paste the following line into Terminal.

<CodeGroup>
  ```Text Terminal Command theme={null}
  sudo systemctl status docker
  ```
</CodeGroup>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=f3f941fec8681c7b2ce76978758292be" alt="" data-og-width="2096" width="2096" data-og-height="990" height="990" data-path="images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=36e80706d7c1a469ae321b9d85a355a7 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4a83bfea4f0be30402bd375e7fa363b4 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=19d6285d13ae5a00e6ab7677140c7611 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=febb7adbfa5b1c92e352a7b3a64ab3c9 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=86d5af03691715b8e4c8e55cff327b1d 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d1adae840c242b42659a546f99705a705e5a5682d3ca78446b048b7052ef5dba-linuxDocker12.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=07011199c88c54158341f3d1008cf0ef 2500w" />
</Frame>

The result will be the current version of running Docker.

```
● docker.service  - Docker Application Container Engine
          Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
          Active: active (running) since Thu 2023-02-09 03:02:24 CST; 10s ago
     TriggeredBy: ● docker.socket
            Docs: https://docs.docker.com
        Main PID: 2361 (dockerd)
           Tasks: 9
          Memory: 26.2M
             CPU: 780ms
          CGroup: /system.slice/docker.service
                 └─2361 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock 
```

### 8. Verify Docker Installation with GPU

Confirmation Command:

* To confirm that your setup is working correctly, run:

  <CodeGroup>
    ```Text Terminal Command theme={null}
    docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
    ```
  </CodeGroup>
* The output should resemble the information displayed by `nvidia-smi`.
* This command verifies that Docker is correctly utilizing your GPU.

### Congratulations on Successfully Setting up Docker

Now that Docker has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-ubuntu).

### Troubleshoot Docker Installation

Use the Reset Script (end of page):

* If the confirmation command fails, use the reset\_drivers\_and\_docker script:

  <CodeGroup>
    ```Text Terminal Command theme={null}
    chmod +x reset_drivers_and_docker.sh  
    ./reset_drivers_and_docker.sh
    ```
  </CodeGroup>
* After running the script, restart your device.
* Rerun the setup from the website. After an automatic restart, rerun the setup to complete the installation.
* If the confirmation command continues to fail, seek assistance on the community support channel.

<Info>
  If you encounter issues with Docker, please refer to our [Troubleshooting Docker guide](/guides/workers/troubleshoot-docker). If the problem persists or if you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
