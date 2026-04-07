
import time

import numpy as np
# from cozmoclad.clad.externalInterface.messageEngineToGame import RobotState

# retico
import retico_core
from retico_core.robot import RobotStateIU #IACMotorAction,


class UserInputModule(retico_core.AbstractProducingModule):

    @staticmethod
    def name():
        return "User Input Module"

    @staticmethod
    def description():
        return "A module looks for any user input before sending an IU. Useful for debugging"

    @staticmethod
    def output_iu():
        # return TextIU # probably more ideal but the IAC motor action is already set up for what I need
        # return IACMotorAction
        return RobotStateIU

    def __init__(self, robot, **kwargs):
        # for exp room:exposure=0.05, gain=0.05
        super().__init__(**kwargs)
        self.robot = robot

    def process_update(self, update_message):
        while True:
            self.robot.camera.image_stream_enabled = True
            time.sleep(5)
            starting_pose = self.robot.pose.position.x_y_z
            while True:
                prior_pose = self.robot.pose
                time.sleep(5)
                # If the robot hasn't moved _at all_ don't break out of loop but if it has moved *and* is no longer moving, then break
                if starting_pose != self.robot.pose.position.x_y_z and self.robot.pose.position.x_y_z == prior_pose.position.x_y_z:
                    break

            # inp = input("Blah")
            # output_iu.set_motor_action(motor_action=np.array([]), flow_uuid=str(uuid.uuid4()).split("-")[0], execution_uuid=f"manual_test_{datetime.now().strftime('%m_%d_%H'}"))
            output_iu = self.create_iu(None)
            return retico_core.UpdateMessage.from_iu(output_iu, retico_core.UpdateType.ADD)
