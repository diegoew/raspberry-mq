from MQ2 import *
from MQ9 import *
from MQ135 import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
    MQ2 = MQ2();
    MQ9 = MQ9();
    MQ135 = MQ135();
    while True:
        perc_mq2 = MQ2.MQPercentage()
        perc_mq9 = MQ9.MQPercentage()
        perc_mq135= MQ135.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm, H2: %g ppm, CH4: %g ppm, , Alc: %g ppm, C3H8: %g ppm, LPG-2: %g ppm, CO-2: %g ppm, CH4-2: %g ppm, CO2: %g ppm, CO-3: %g ppm, Alc-2: %g ppm, NH4: %g ppm, CH3: %g ppm, (CH3)2CO: %g ppm" % (perc_mq2["GAS_LPG"], perc_mq2["GAS_CO"], perc_mq2["GAS_SMOKE"], perc_mq2["GAS_HYDROGEN"], perc_mq2["GAS_METHANE"], perc_mq2["GAS_PROPANE"], perc_mq9["GAS_LPG"], perc_mq9["GAS_CO"], perc_mq9["GAS_METHANE"], perc_mq135["GAS_CO2"], perc_mq135["GAS_CO"], perc_mq135["GAS_ALCOHOL"], perc_mq135["GAS_AMMONIUM"], perc_mq135["GAS_TOLUENE"], perc_mq135["GAS_ACETONE"]))
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")
