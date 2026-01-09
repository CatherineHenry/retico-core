import threading
# cozmo
# import cv2
import time
from datetime import datetime

import numpy as np

# retico
import retico_core
from retico_core.robot import IACMotorAction


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
        return IACMotorAction

    def __init__(self, **kwargs):
        # for exp room:exposure=0.05, gain=0.05
        super().__init__(**kwargs)


        # NOTE: was seeing intermittent issues when this was in setup -- the exposure/gain was not setting correctly and would be too bright
        # self.configure_camera()


    def process_update(self, _):
            time.sleep(5)
            inp = input("Blah")
            # output_iu.set_motor_action(motor_action=np.array([]), flow_uuid=str(uuid.uuid4()).split("-")[0], execution_uuid=f"manual_test_{datetime.now().strftime('%m_%d_%H'}"))
            output_iu = self.create_iu(grounded_in=None)
            output_iu.set_motor_action(motor_action=np.array([]), flow_uuid=inp, execution_uuid=f"manual_test_{datetime.now().strftime('%m_%d_%H')}")
            return retico_core.UpdateMessage.from_iu(output_iu, retico_core.UpdateType.ADD)

    def setup(self):
        x = threading.Thread(target=self.process_update, args="_")
        x.start()

