import serial

class UsbRelay():
    def __init__(self, port, baud_rate=9600, byte_size=8):
        """
        Function Name: __init__
        *
        Description: close and open LCUS-1 Usb relay by sending Hexadecimal numbers
        *
        Argument: None
        *
        Parameters: port [int] -> choose your COM number
                    baud_rate [int] -> baudrate
                    btye_size [int] -> byte size for serial
        *
        Return: None
        *
        Edited by: [2020-10-13] [Bill Gao]
        """
        port_name = "COM" + str(port)
        self.serial = serial.Serial(port_name, baudrate=baud_rate, bytesize=byte_size)

        # sending Hexadecimal code A0 01 01 A2 to open relay
        self.__open = [0xA0,0x01,0x01,0xA2]


        # sending Hexadecimal code A0 01 00 A1 to open relay
        self.__close = [0xA0,0x01,0x00,0xA1]
    
    def open(self):
        """
        Function Name: open
        *
        Description: Sending Hexadecimal numbers to open relay
        *
        Argument: None
        *
        Parameters: None
        *
        Return: None
        *
        Edited by: [2020-10-13] [Bill Gao]
        """        
        self.serial.write(self.__open)
        # self.serial.close()
    
    def close(self):
        """
        Function Name: close
        *
        Description: Sending Hexadecimal numbers to close relay
        *
        Argument: None
        *
        Parameters: None
        *
        Return: None
        *
        Edited by: [2020-10-13] [Bill Gao]
        """   
        self.serial.write(self.__close)
        # self.serial.close()

Relay = UsbRelay(5)
Relay.open()
# Relay.close()

