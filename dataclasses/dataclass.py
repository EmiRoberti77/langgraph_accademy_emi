from dataclasses import dataclass
from typing import List

#standard class decleration
class ToolA:
    def __init__(self, name:str, desc:str):
        self.name = name
        self.desc = desc


tool:ToolA = ToolA("flight_tool", "search for flights tool")
print(tool.name, tool.desc)

# sample in using dataclass decorator to remove boiler template code from standard class 
# this type of class is used to declare immutable datastructures
@dataclass
class ToolB:
    name:str
    desc:str
    steps:List[str]

steps:List = ['step1', 'step2', 'step3']
toolb:ToolB = ToolB("car_tools", "tool for getting cheap car repair quotes", steps)
print(toolb.name, toolb.desc)
print(toolb.steps)

