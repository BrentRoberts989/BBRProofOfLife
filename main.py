import xbox
import maestro
import drive
import time

CH_LEFT_MOTOR  = 1
CH_RIGHT_MOTOR = 0

j = xbox.Joystick(0)
time.sleep(3)
# Maestro Controllers
servo = maestro.Controller()
# DriveTrain
drivetrain = drive.DriveTrain(servo,CH_RIGHT_MOTOR,CH_LEFT_MOTOR)

connected = False
try:
    while True :
        
        if j.connected():
            if connected == False:
                print("Joystick connected")
                connected = True
            else:
                drivetrain.drive(j.leftX() * .40, -(j.leftY() * .5))         
        else:
            drivetrain.stop()
            if connected == True:
                print("Joystick disconnected "+ j.connected())
            connected = False

    time.sleep(0.02)

except:
    drivetrain.close

    raise