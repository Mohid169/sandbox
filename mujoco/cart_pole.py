import mujoco
from mujoco import viewer

m = mujoco.MjModel.from_xml_path("assets/cartpole.xml")  # point to the file from #1
d = mujoco.MjData(m)

viewer = mujoco.viewer.launch_passive(m, d)

while viewer.is_running():
    for _ in range(1000):
        mujoco.mj_step(m, d)
        d.ctrl[0] = 1.0
        viewer.sync()
