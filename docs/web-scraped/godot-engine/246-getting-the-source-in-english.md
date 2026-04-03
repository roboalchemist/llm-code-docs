# Getting the source in English

# Getting the source

## Downloading the Godot source code

Beforegetting into the SCons build systemand compiling Godot, you need to actually download the Godot source code.
The source code is available onGitHuband while you can manually download it via the website, in general you want to
do it via thegitversion control system.
If you are compiling in order to make contributions or pull requests, you should
follow the instructions from thePull Request workflow.
If you don't know much aboutgityet, there are a great number oftutorialsavailable on various websites.
In general, you need to installgitand/or one of the various GUI clients.
Afterwards, to get the latest development version of the Godot source code
(the unstablemasterbranch), you can usegitclone.
If you are using thegitcommand line client, this is done by entering
the following in a terminal:

```
git clone https://github.com/godotengine/godot.git
# You can add the --depth 1 argument to omit the commit history (shallow clone).
# A shallow clone is faster, but not all Git operations (like blame) will work.
```

For any stable release, visit therelease pageand click on the link for the release you want.
You can then download and extract the source from the download link on the page.
Withgit, you can also clone a stable release by specifying its branch or tag
after the--branch(or just-b) argument:

```
# Clone the continuously maintained stable branch (`4.6` as of writing).
git clone https://github.com/godotengine/godot.git -b 4.6

# Clone the `4.6-stable` tag. This is a fixed revision that will never change.
git clone https://github.com/godotengine/godot.git -b 4.6-stable

# After cloning, optionally go to a specific commit.
# This can be used to access the source code at a specific point in time,
# e.g. for development snapshots, betas and release candidates.
cd godot
git checkout f4af8201bac157b9d47e336203d3e8a8ef729de2
```

Themaintenance branchesare used to release further patches on each minor version.
You can get the source code for each release and pre-release in.tar.xzformat fromgodotengine/godot-builds on GitHub.
This lacks version control information but has a slightly smaller download size.
After downloading the Godot source code,
you cancontinue to compiling Godot.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
