# run_arm.py
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
    for i in range(1000):
        mujoco.mj_step(m, d)
        d.ctrl[0] = 0.8 * np.sin(2 * np.pi * 0.5 * d.time)
        d.ctrl[1] = 0.6 * np.sin(2 * np.pi * 0.8 * d.time + 1.0)
        viewer.sync()
