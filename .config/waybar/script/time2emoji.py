#!/usr/bin/env python3

import json
import time
clock = {
    "c1": "🕐",
    "c2": "🕑",
    "c3": "🕒",
    "c4": "🕓",
    "c5": "🕔",
    "c6": "🕕",
    "c7": "🕖",
    "c8": "🕗",
    "c9": "🕘",
    "c10": "🕙",
    "c11": "🕚",
    "c12": "🕛"
}


localtime = time.localtime(time.time())
hour = localtime[3]
emoji = clock.get(f"c{hour-12}")
format = time.strftime(f"{emoji} %I:%M %p  📅 %d/%m/%Y", time.localtime())
result = {"text": format, "tooltip": "tips"}
print(json.dumps(result))
