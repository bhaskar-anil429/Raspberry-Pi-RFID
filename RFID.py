import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

while True:
    string = ser.read(12)

    if len(string) == 0:
        print "Please insert a tag"

    else:
        string = string[1:11]
        print "string",string
        if string == '650033A2E5':
            print "hello bhakasr"

