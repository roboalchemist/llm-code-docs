# Source: https://docs.edgeimpulse.com/tutorials/topics/data/generate-time-series-data-pybullet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate time-series data using PyBullet

<a href="https://colab.research.google.com/github/edgeimpulse/notebooks/blob/main/notebooks/generate-physics-simulation-dataset.ipynb" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" noZoom />
</a>

This notebook takes you through a basic example of using the physics simulation tool PyBullet to generate an accelerometer dataset representing dropping the Nordic Thingy:53 devkit from different heights. This dataset can be used to train a regression model to predict drop height.

This idea could be used for a wide range of simulatable environments- for example generating accelerometer datasets for pose estimation or fall detection. The same concept could be applied in an FMEA application for generating strain datasets for structural monitoring.

There is also a video version of this tutorial:

<iframe src="https://www.youtube.com/embed/73PtAfYKLJg" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Local Software Requirements

* Python 3
* Pip package manager
* Jupyter Notebook: [https://jupyter.org/install](https://jupyter.org/install)
* Bullet3: [https://github.com/bulletphysics/bullet3](https://github.com/bulletphysics/bullet3)&#x20;

The dependencies can be installed with:

```python  theme={"system"}
! pip install pybullet numpy
```

```python  theme={"system"}
# Imports
import pybullet as p
import pybullet_data
import os
import shutil
import csv
import random
import numpy as np
import json

```

## Create object to simulate

We need to load in a Universal Robotics Description Format file describing an object with the dimensions and weight of a Nordic Thingy:53. In this case, measuring our device it is 64x60x23.5mm and its weight 60g. The shape is given by a .obj 3D model file.

```
	<visual>
		<origin xyz="0.02977180615936878 -0.01182944632717566 0.03176079914341195" rpy="1.57079632679 0.0 0.0" />
		<geometry>
			<mesh filename="thingy53/thingy53 v2.obj" scale="1 1 1" />
		</geometry>
		<material name="texture">
			<color rgba="1.0 1.0 1.0 1.0" />
		</material>
	</visual>
	<collision>
		<origin xyz="0.02977180615936878 -0.01182944632717566 0.03176079914341195" rpy="1.57079632679 0.0 0.0" />
		<geometry>
			<mesh filename="thingy53/thingy53 v2.obj" scale="1 1 1" />
		</geometry>
	</collision>
	<inertial>
		<mass value="0.06" />
  		<inertia ixx="0.00002076125" ixy="0" ixz="0" iyy="0.00002324125" iyz="0" izz="0.00003848"/>
	</inertial>
</link>
```

## Visualizing the problem&#x20;

To generate the required data we will be running PyBullet in headless "DIRECT" mode so we can iterate quickly over the parameter field. If you run the python file below you can see how pybullet simulates the object dropping onto a plane

```python  theme={"system"}
! python ../.assets/pybullet/single_simulation.py
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-physics-simulation.gif?s=58a5d20b4aba95c1434f0e318ce7e772" alt="" width="752" height="582" data-path=".assets/images/tutorial-physics-simulation.gif" />
</Frame>

## Setting up the simulation environment

First off we need to set up a pybullet physics simulation environment. We load in our object file and a plane for it to drop onto. The plane's dynamics can be adjusted to better represent the real world (in this case we're dropping onto carpet)

```python  theme={"system"}
# Set up PyBullet physics simulation (change from p.GUI to p.DIRECT for headless simulation)
physicsClient = p.connect(p.DIRECT)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load object URDF file
obj_file = "../.assets/pybullet/thingy53/thingy53.urdf"
obj_id = p.loadURDF(obj_file, flags=p.URDF_USE_INERTIA_FROM_FILE)

# Add a solid plane for the object to collide with
plane_id = p.loadURDF("plane.urdf")

# Set length of simulation and sampling frequency
sample_length = 2 # Seconds
sample_freq = 100 # Hz

```

We also need to define the output folder for our simulated accelerometer files

```python  theme={"system"}
output_folder = 'output/'
# Check if output directory for noisey files exists and create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    shutil.rmtree(output_folder)
    os.makedirs(output_folder)
```

And define the drop parameters

```python  theme={"system"}
# Simulate dropping object from range of heights
heights = 100
sims_per_height = 20
min_height = 0.1 # Metres
max_height = 0.8 # Metres
```

We also need to define the characteristics of the IMU on the real device we are trying to simulate. In this case the Nordic Thingy:53 has a Bosch BMI270 IMU ([https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi270/](https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi270/)) which is set to a range of +-2g with a resolution of 0.06g. These parameters will be used to restrict the raw acceleration output:

```python  theme={"system"}

range_g = 2
range_acc = range_g * 9.81
resolution_mg = 0.06
resolution_acc = resolution_mg / 1000.0 * 9.81
```

Finally we are going to give the object and plane restitution properties to allow for some bounce. In this case I dropped the real Thingy:53 onto a hardwood table. You can use p.changeDynamics to introduce other factors such as damping and friction.

```python  theme={"system"}
p.changeDynamics(obj_id, -1, restitution=0.3)
p.changeDynamics(plane_id, -1, restitution=0.4)
```

## Drop simulation

Here we iterate over a range of heights, randomly changing its start orientation for i number of simulations per height. The acceleration is calculated relative to the orientation of the Thingy:53 object to represent its onboard accelerometer.

```python  theme={"system"}
metadata = []
for height in np.linspace(max_height, min_height, num=heights):
    print(f"Simulating {sims_per_height} drops from {height}m")
    for i in range(sims_per_height):
        # Set initial position and orientation of object
        x = 0
        y = 0
        z = height
        orientation = p.getQuaternionFromEuler((random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi)))
        p.resetBasePositionAndOrientation(obj_id, [x, y, z], orientation)

        prev_linear_vel = np.zeros(3)

        # Initialize the object position and velocity
        pos_prev, orn_prev = p.getBasePositionAndOrientation(obj_id)
        vel_prev, ang_vel_prev = p.getBaseVelocity(obj_id)
        timestamp=0
        dt=1/sample_freq
        p.setTimeStep(dt)
        filename=f"drop_{height}m_{i}.csv"
        with open(f"output/{filename}", mode="w") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['timestamp','accX','accY','accZ'])
        while timestamp < sample_length:
            p.stepSimulation()
            linear_vel, angular_vel = p.getBaseVelocity(obj_id)
            lin_acc = [(v - prev_v)/dt for v, prev_v in zip(linear_vel, prev_linear_vel)]
            prev_linear_vel = linear_vel
            timestamp += dt
            # Get the current position and orientation of the object
            pos, orn = p.getBasePositionAndOrientation(obj_id)

            # Get the linear and angular velocity of the object in world coordinates
            vel, ang_vel = p.getBaseVelocity(obj_id)

             # Calculate the change in position and velocity between steps
            pos_diff = np.array(pos) - np.array(pos_prev)
            vel_diff = np.array(vel) - np.array(vel_prev)

            # Convert the orientation quaternion to a rotation matrix
            rot_matrix = np.array(p.getMatrixFromQuaternion(orn)).reshape(3, 3)

            # Calculate the local linear acceleration of the object, subtracting gravity
            local_acc = np.dot(rot_matrix.T, vel_diff / dt) - np.array([0, 0, -9.81])
            # Restrict the acceleration to the range of the accelerometer
            imu_rel_lin_acc_scaled = np.clip(local_acc, -range_acc, range_acc)
            # Round the acceleration to the nearest resolution of the accelerometer
            imu_rel_lin_acc_rounded = np.round(imu_rel_lin_acc_scaled/resolution_acc) * resolution_acc
            # Update the previous position and velocity
            pos_prev, orn_prev = pos, orn
            vel_prev, ang_vel_prev = vel, ang_vel

            # Save acceleration data to CSV file
            with open(f"{output_folder}{filename}", mode="a") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([timestamp*1000] + imu_rel_lin_acc_rounded.tolist())

        nearestheight = round(height, 2)
        metadata.append({
            "path": filename,
            "category": "training",
            "label": { "type": "label", "label": str(nearestheight)}
        })

```

Finally we save the metadata file to the output folder. This can be used to tell the edge-impulse-uploader CLI tool the floating point labels for each file.

```python  theme={"system"}
jsonout = {"version": 1, "files": metadata}

with open(f"{output_folder}/files.json", "w") as f:
    json.dump(jsonout, f)

# Disconnect from PyBullet physics simulation
p.disconnect()
```

These files can then be uploaded to a project with these commands (run in a separate terminal window):

```python  theme={"system"}
! cd output
! edge-impulse-uploader --info-file files.json
```

(run edge-impulse-uploader --clean if you have used the CLI before to reset the target project)

## What next?

Now you can use your dataset a drop height detection regression model in Edge Impulse Studio!

See if you can edit this project to simulate throwing the object up in the air to predict the maximum height, or add in your own custom object. You could also try to better model the real environment you're dropping the object in- adding air resistance, friction, damping and material properties for your surface.


Built with [Mintlify](https://mintlify.com).