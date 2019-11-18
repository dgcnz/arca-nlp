from lib.actuators.actuator_base import Actuator
from lib.types import Action, Identifier
from subprocess import call
from typing import List, Any
import platform

class Speech(Actuator):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = self.get_logger()
        os_ = platform.system()
        if os_ == "Linux":
            self.program = "lib/utilities/pico_speak.py"
        else:
            self.program = "lib/utilities/speak.py"

    def do(self, action: Action) -> None:
        self.logger.info(f"Saying: {action.data}")
        call(["python", self.program, action.data["data"]])

    def pass_msg(self, msg: str) -> None:
        pass

    def get_destinations_ID(self, raw_data: Any) -> List[Identifier]:
        pass

    def dump_history(self, filename: str, data: List[Any]) -> None:
        pass
