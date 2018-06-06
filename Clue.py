import time
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
#The purpose of this program is to read RFID tags from a USB based sensor in Linux.
#It will compare flagPerson against the person.txt file and flagWeapon against the weapon.txt file to set flags, when both flags are set, it will trigger
#a relay connected with a grove connector to trigger a PLC, and open a magnetic lock.

const = 1 #for permanenet while loops
counter = 0 #initialize timer
counterMax = 30 #counter time in seconds before resetting registered input
flagPerson = False #flag for correct person selected
flagWeapon = False #flag for correct weapon selected
#no flag for room since the rfid sensor will be behind the room on the game board
#relay object - does it need to be a variable? 

while const == 1:
    while counter < counterMax:
        counter+1
        tagIn = ser.readline()
        file = open("person.txt","r")
        fileIn = file.readline()
        if tagIn == fileIn:
            flagPerson = True
            counter = 0 #reset counter on valid input
        file.close()
        file = open("weapon.txt","r")
        fileIn = file.readline()
        if tagIn == fileIn:
            flagWeapon = True
            counter = 0 #reset counter on valid input
        file.close()
        if flagPerson == True:
            if flagWeapon == True:
                #trigger relay open
            else:
                #trigger relay closed
        else:
            #trigger relay closed
        time.sleep (1) #sleep for 1 second between passes
    #end of while counter < counterMax loop
    flagPerson = False; flagWeapon = False; counter = 0
    #loop to beginning of while counter < counterMax loop
