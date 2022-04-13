from smartcard.Exceptions import CardConnectionException, NoCardException
from smartcard.CardConnection import CardConnection

from smartcard.System import *
from smartcard.util import toHexString, toBytes

from instrumental import instrument, list_instruments
from instrumental.log import log_to_screen # to test import with log_to_screen()
import instrumental.drivers.scopes.lecroy # to test import by directly importing

import numpy as np

def main():
    #log_to_screen()
    paramsets = list_instruments()
    print(paramsets)
    oscillo = instrument(paramsets[0])
    
def rest():
    reader = readers()[0]
    print("Connecting to ", reader)
    connection = reader.createConnection()
    
    connection.connect(CardConnection.T1_protocol)
    
    command = "00 A4 04 00 10 A0 00 00 03 96 56 43 41 03 F0 15 40 00 00 00 0B 00"
    print("CMD: ", command)    
    data, sw1, sw2 = connection.transmit(toBytes(command))
    print("Data: {}\tStatus: {}".format(toHexString(data), toHexString([sw1, sw2])))
    
    # SET TO SINGLE TRIGGER
    oscillo.arm_acquisition()
    
    command = "90 71 00 00 03 00 01 00 00"
    print("CMD: ", command)    
    data, sw1, sw2 = connection.transmit(toBytes(command))
    print("Data: {}\tStatus: {}".format(toHexString(data), toHexString([sw1, sw2])))
    
    trace = oscillo.get_waveform('C1', verbose=True)
    np.save("C:\\Users\\qasem.HQ\\OneDrive - Kudelski Group\\Desktop\\traces_py\\trace.npy", trace)
    
if __name__ == '__main__':
    main()