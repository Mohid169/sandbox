import numpy as np
import mujoco, mujoco.viewer
from mujoco import MjModel, MjData

XML_PATH = "assets/plunger_launcher.xml"  # or planar_arm_1dof.xml

m = MjModel.from_xml_path(XML_PATH)
d = MjData(m)

viewer = mujoco.viewer.launch_passive(m, d)
mujoco.mj_resetDataKeyframe(m, d, 0)

for _ in range(20000):
    mujoco.mj_step(m, d)

while viewer.is_running():
    mujoco.mj_step(m, d)
    viewer.sync()
