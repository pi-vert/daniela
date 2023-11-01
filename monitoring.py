#! /usr/bin/env python
import os
import drivers
from datetime import datetime
from subprocess import check_output
import psutil
display = drivers.Lcd()
display.lcd_display_string(str(datetime.now().time()), 1)

# Adress IP
IP = check_output(["hostname", "-I"], encoding="utf8").split()[0]
display.lcd_display_string(str(IP), 2)

# Temperature
temp=check_output(["vcgencmd", "measure_temp"], encoding="utf8")
display.lcd_display_string(str(temp), 3)

# CPU sur 15 minutes
load1, load5, load15 = psutil.getloadavg()
cpu_usage = (load15/os.cpu_count()) * 100
print("The CPU usage is : ", cpu_usage)

# Memoire utilisée
mem_usage = psutil.virtual_memory()[2]

display.lcd_display_string('CPU: '+str(round(cpu_usage))+'% | Memory:'+str(round(mem_usage))+'%',4)
