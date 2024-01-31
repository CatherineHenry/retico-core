"""
This module redefines the abstract classes to fit the needs of internal robot state processing.
"""

from retico_core import abstract


class RobotStateIU(abstract.IncrementalUnit):
    """An image incremental unit that receives raw image data from a source.

    Attributes:
        creator (AbstractModule): The module that created this IU
        previous_iu (IncrementalUnit): A link to the IU created before the
            current one.
        grounded_in (IncrementalUnit): A link to the IU this IU is based on.
        created_at (float): The UNIX timestamp of the moment the IU is created.
        state (dict): The state of the robot 
    """

    @staticmethod
    def type():
        return "Robot State IU"

    def __init__(self, creator=None, iuid=0, previous_iu=None, grounded_in=None, state=None,
                 **kwargs):
        super().__init__(creator=creator, iuid=iuid, previous_iu=previous_iu,
                         grounded_in=grounded_in, payload=state)
        self.state = state

    def set_state(self, state):
        """Sets the state of the robot"""
        self.state = state
        self.payload = state


class IACMotorAction(abstract.IncrementalUnit):
    """An incremental unit that holds object information (id, name, pose information)

    Attributes:
        creator (AbstractModule): The module that created this IU
        previous_iu (IncrementalUnit): A link to the IU created before the
            current one.
        grounded_in (IncrementalUnit): A link to the IU this IU is based on.
        created_at (float): The UNIX timestamp of the moment the IU is created.
    """

    @staticmethod
    def type():
        return "IAC Request Camera IU"

    def __init__(self, creator=None, iuid=0, previous_iu=None, grounded_in=None, **kwargs):
        super().__init__(creator=creator, iuid=iuid, previous_iu=previous_iu,
                         grounded_in=grounded_in)
        self.motor_action = None
        self.flow_uuid = None
        self.execution_uuid = None

    def set_motor_action(self, motor_action: [], flow_uuid, execution_uuid):
        """
        Sets the motor action taken to request image
        :param motor_action: motor action list
        :param motor_action_uuid: uuid of action

        """
        self.motor_action = motor_action
        self.flow_uuid = flow_uuid # time (HH:MM:SS + action hash)
        self.execution_uuid = execution_uuid

