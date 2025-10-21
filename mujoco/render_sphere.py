import mujoco, mujoco.viewer
from mujoco import MjModel, MjData

model = MjModel.from_xml_string(
    "<mujoco><worldbody><geom type='sphere' size='0.05'/></worldbody></mujoco>"
)
data = MjData(model)

viewer = mujoco.viewer.launch_passive(model, data)

while viewer.is_running():
    mujoco.mj_step(model, data)
    viewer.sync()
