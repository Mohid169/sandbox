import mujoco, mujoco.viewer.viewer
from mujoco import MjModel, MjData, MjViewer

model = MjModel.from_file("assets/bouncing_ball.xml")
data = MjData(model)
viewer = MjViewer(model, data)

while True:
    viewer.render()
