import os

os.environ["MUJOCO_GL"] = "glfw"
import mujoco, mujoco.viewer
from mujoco import MjModel, MjData

m = MjModel.from_xml_path("assets/bouncing_balls.xml")
d = MjData(m)

viewer = mujoco.viewer.launch_passive(m, d)
print("Close window to stop.")
while viewer.is_running():
    mujoco.mj_step(m, d)
    viewer.sync()
viewer.close()
