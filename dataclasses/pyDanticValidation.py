from pydantic import BaseModel, validator, ValidationError
from dataclasses import dataclass
from typing import List, Literal

# sample in using dataclass decorator to remove boiler template code from standard class 
# this type of class is used to declare immutable datastructures
class PyDanticToolB(BaseModel):
    name:str
    desc:str
    step:Literal["start", "step1", "step2", "step3", "completed"]

    @validator("step")
    def step_validator(cls, value):
        #ensure only step1, step2, step3 are being called
        if value not in ["step1", "step2", "step3"]:
            raise ValueError("steps must be", steps)
        return value

toolb:PyDanticToolB = PyDanticToolB(name="car_tools", desc="tool for getting cheap car repair quotes", step="step1")
print(toolb.name, toolb.desc)
print(toolb.step)
