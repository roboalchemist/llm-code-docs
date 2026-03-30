# Source: https://docs.edgeimpulse.com/projects/expert-network/cv-punchcards-lattepanda.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recognizing Punch Cards with LattePanda IOTA and Edge Impulse

Created By: Roni Bandini

Public Project Link: [https://studio.edgeimpulse.com/studio/863714](https://studio.edgeimpulse.com/studio/863714)

GitHub Repo: [https://github.com/ronibandini/PunchedCards](https://github.com/ronibandini/PunchedCards)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/CxQFXJepqQEJmrqF/.assets/images/cv-punchcards-lattepanda/01.jpg?fit=max&auto=format&n=CxQFXJepqQEJmrqF&q=85&s=1b5e84a4bab374df41cb553883b30274" width="1248" height="832" data-path=".assets/images/cv-punchcards-lattepanda/01.jpg" />
</Frame>

## Intro

In 1804, Joseph Marie Jacquard demonstrated a mechanism to automate loom operation using a sequence of punched cards. Each card mechanically defined which warp threads were lifted for that pass, enabling programmable weaving patterns. This established the first industrial use of binary logic (hole or no hole) for machine control.  Punched cards evolved from this mechanical origin, into a standardized data storage medium for computing. While the Jacquard loom used physical needles to sense holes, later systems like the 1890 Hollerith tabulator introduced electrical sensing, using spring-loaded pins to complete circuits through the perforations. This technology eventually culminated in the IBM 80-column / 12-row format (standardized in 1928), where card readers detected electrical continuity via wire brushes, or in later decades, utilized optical sensors to read data at high speeds.

As a tribute to this technology and to test the LattePanda IOTA mini PC, this project recognizes visually "punched" cards — printed and tagged here instead of punched — using a camera and machine learning.

## Hardware

The [LattePanda IOTA](https://www.lattepanda.com/lattepanda-iota) is an x86 mini PC SBC designed by [DFRobot](http://dfrobot.com) with enough performance to run traditional robotics workloads and on-device AI inference. It features an Intel Processor N150 (4C/4T), 8GB or 16GB of LPDDR5 memory, 64GB or 128GB of eMMC storage, and an onboard RP2040 microcontroller for real time sensors and actuators.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/CxQFXJepqQEJmrqF/.assets/images/cv-punchcards-lattepanda/02.jpg?fit=max&auto=format&n=CxQFXJepqQEJmrqF&q=85&s=2bd5d1e5be19ecdcaeb7eafad1478553" width="1894" height="1088" data-path=".assets/images/cv-punchcards-lattepanda/02.jpg" />
</Frame>

## Parts Required

* LattePanda IOTA
* Active cooler
* USB Webcam
* USB Pendrive 16GB or more
* Power supply

## Cards

To simplify training, a single row with eight binary positions is used to represent characters. Instead of physical holes, printed circles represent binary "1" positions. Misalignment is intentional to give the model tolerances similar to physical punch cards.

Example:

* A 01000001
* B 01000010

## Edge Impulse Model Creation

Seven characters were chosen for this demo. Each character corresponds to ASCII BIN:

```
A 01000001
B 01000010
C 01000011
H 01001000
E 01000101
L 01001100
O 01001111
```

A template was created in Photoshop as a PSD file, and 11 variants per character were exported as .PNG image files with the circles displaced in different directions. All the images were uploaded to a new Edge Impulse project using Data Acquisition, with one label per image and an 82/18 split between Training and Testing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/CxQFXJepqQEJmrqF/.assets/images/cv-punchcards-lattepanda/03.jpg?fit=max&auto=format&n=CxQFXJepqQEJmrqF&q=85&s=28133e833165e6bf9bd857fe57bf7417" width="2876" height="1528" data-path=".assets/images/cv-punchcards-lattepanda/03.jpg" />
</Frame>

An Impulse with a Classification Learning block and Grayscale color depth achieved perfect recognition, with only 50 training cycles and a 0.0005 learning rate:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/CxQFXJepqQEJmrqF/.assets/images/cv-punchcards-lattepanda/04.jpg?fit=max&auto=format&n=CxQFXJepqQEJmrqF&q=85&s=76ce7b227968fbb6f0e23f7b42d231e7" width="2880" height="1528" data-path=".assets/images/cv-punchcards-lattepanda/04.jpg" />
</Frame>

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/CxQFXJepqQEJmrqF/.assets/images/cv-punchcards-lattepanda/05.jpg?fit=max&auto=format&n=CxQFXJepqQEJmrqF&q=85&s=fc676e6ec7a35f65d084b062edd89378" width="2880" height="1518" data-path=".assets/images/cv-punchcards-lattepanda/05.jpg" />
</Frame>

## Setup and Deployment

The LattePanda IOTA originally shipped with Windows pre-installed on the eMMC, but Ubuntu LTS was installed instead for this project. After flashing the Ubuntu image to a USB stick with balenaEtcher, the device was booted from USB by pressing `F7` and selecting the USB pen drive.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/CxQFXJepqQEJmrqF/.assets/images/cv-punchcards-lattepanda/06.jpg?fit=max&auto=format&n=CxQFXJepqQEJmrqF&q=85&s=e8d66781a05ec90a734f103ef2d3e8d3" width="1598" height="1002" data-path=".assets/images/cv-punchcards-lattepanda/06.jpg" />
</Frame>

After installation, the following commands prepare the needed environment in Ubuntu:

#### Update 

```
sudo apt update
```

#### Optional: enable ssh for remote console access 

```
sudo apt install openssh-server -y sudo systemctl enable ssh sudo systemctl start ssh
```

#### Install Node 

```
sudo apt install curl -y curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - sudo apt install nodejs -y
```

#### Install Edge Impulse 

```
sudo npm install -g edge-impulse-linux –unsafe-perm sudo npm install -g edge-impulse-cli –unsafe-perm
```

Now that everything is installed,  you can execute:  `edge-impulse-linux-runner`

Log in, select the Edge Impulse project (if you have more than 1), and inference output begins immediately.

For example:

```
classifyRes 1ms. {
  A: 0.9214,
  B: 0.4301,
  C: 0.2434,
  E: 0.1809,
  H: 0.1588,
  L: 0.0557,
  O: 0.0096
}
```

Values represent probabilities for each class.

Live visualization is also available at port 4912 on the IP address of the LattePanda on your network.  For example, `http://192.168.0.100:4912`.  This is helpful if you need to adjust the web cam position or punch card position.

## Parsing Results in Python

I have also included a Python script to execute the runner, capture the output, parse the result block and display the most probable character.

After cloning the GitHub repo linked above, you can launch the runner with:

`python3 runner.py`

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/CxQFXJepqQEJmrqF/.assets/images/cv-punchcards-lattepanda/07.jpg?fit=max&auto=format&n=CxQFXJepqQEJmrqF&q=85&s=8811fc474979b3cb75dee1cdccc9e829" width="2880" height="1358" data-path=".assets/images/cv-punchcards-lattepanda/07.jpg" />
</Frame>

## Final Notes

The DFRobot LattePanda IOTA provided stable inference performance and a straightforward deployment path for Edge Impulse. While this project is a tribute to punched-card computing, the same principles apply to recognizing visual states in control panels, tags, physical tokens, or other symbolic markers captured by a camera.

## Project Links

[https://studio.edgeimpulse.com/public/863714/live](https://studio.edgeimpulse.com/public/863714/live)
[https://github.com/ronibandini/PunchedCards](https://github.com/ronibandini/PunchedCards)

## References

[https://www.lattepanda.com/lattepanda-iota](https://www.lattepanda.com/lattepanda-iota)
[https://www.ascii-code.com](https://www.ascii-code.com) [https://artsandculture.google.com/story/punched-card-machines-the-national-museum-of-computing/bwWBrooyeGKPiA?hl=en](https://artsandculture.google.com/story/punched-card-machines-the-national-museum-of-computing/bwWBrooyeGKPiA?hl=en)  [https://www.ibm.com/history/punched-card](https://www.ibm.com/history/punched-card)


Built with [Mintlify](https://mintlify.com).