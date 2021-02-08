#Made by JohnTrunix, free to use!
#Add this file to crontab for periodic execution

import os

#Add your bluetooth Adress
bluetoth_status = os.system('sudo l2ping -c1 -s32 -t1 XX:XX:XX:XX:XX:XX')

#If it can ping successfully, you will get code 0
if bluetoth_status == 0:
    os.system("vcgencmd display_power 1")

else:
    os.system("vcgencmd display_power 0")
