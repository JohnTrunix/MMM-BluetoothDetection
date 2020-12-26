import os
import time

bluetoth_status = os.system('sudo l2ping -c1 -s32 -t1 XX:XX:XX:XX:XX:XX')

if bluetoth_status == 0:
    os.system("vcgencmd display_power 1")

else:
    os.system("vcgencmd display_power 0")
