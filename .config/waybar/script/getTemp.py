#!/usr/bin/env python3

import json
import os

result = os.popen("sensors -j")
result = json.loads(result.read())

core_temp = result.get("coretemp-isa-0000")
cpu_temp = core_temp["Package id 0"]["temp1_input"]
core0 = core_temp["Core 0"]["temp2_input"]
core1 = core_temp["Core 1"]["temp3_input"]
core2 = core_temp["Core 2"]["temp4_input"]
core3 = core_temp["Core 3"]["temp5_input"]
tooltip = f"""
cpu:        {cpu_temp}°C
  core0:    {core0}°C
  core1:    {core1}°C
  core2:    {core2}°C
  core3:    {core3}°C
"""

text = {"text": f"{cpu_temp}°C ", "tooltip": tooltip}
print(json.dumps(text))
