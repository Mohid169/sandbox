# pos control of a joint actuator in a 2dof arm
import os

os.environ["MUJOCO_GL"] = "glfw"  # macOS-friendly
import numpy as np
import mujoco, mujoco.viewer
from mujoco import MjModel, MjData

XML_PATH = "assets/planar_arm_2dof.xml"  # or planar_arm_1dof.xml

m = MjModel.from_xml_path(XML_PATH)
d = MjData(m)


viewer = mujoco.viewer.launch_passive(m, d)
while viewer.is_running():
    # torque = amplitude * sin(2π * freq * time)
    amp = .5   # torque amplitude
    freq = .01  # Hz (half a cycle per second)
    d.ctrl[0] = amp * np.sin(2 * np.pi * freq * d.time)

    mujoco.mj_step(m, d)
    viewer.sync()
