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


class IACMotorGoalIU(abstract.IncrementalUnit):
    """An incremental unit that holds the motor goal produced by IAC

    Attributes:
        creator (AbstractModule): The module that created this IU
        previous_iu (IncrementalUnit): A link to the IU created before the
            current one.
        grounded_in (IncrementalUnit): A link to the IU this IU is based on.
        created_at (float): The UNIX timestamp of the moment the IU is created.
    """

    @staticmethod
    def type():
        return "IAC Motor Goal"

    def __init__(self, creator=None, iuid=0, previous_iu=None, grounded_in=None, **kwargs):
        super().__init__(creator=creator, iuid=iuid, previous_iu=previous_iu,
                         grounded_in=grounded_in)
        self.payload = None
        self.flow_uuid = None
        self.execution_uuid = None

    def set_payload(self, motor_goal: [],):
        """
        Sets the motor goal taken so we can move the robot to the specified goal on the client side
        """
        self.payload = motor_goal

    def set_flow_uuid(self, flow_uuid):
        self.flow_uuid = flow_uuid # time (HH:MM:SS + action hash)

    def set_execution_uuid(self, execution_uuid):
        self.execution_uuid = execution_uuid

