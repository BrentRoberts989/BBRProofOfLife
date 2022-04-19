import xbox
import maestro
import drive
import time
import digger

CH_LEFT_MOTOR  = 1
CH_RIGHT_MOTOR = 0
CH_DIGGER_MOTOR = 2
CH_ARM_MOTOR = 3

j = xbox.Joystick(0)
time.sleep(3)
# Maestro Controllers
servo = maestro.Controller()
# DriveTrain
drivetrain = drive.DriveTrain(servo,CH_RIGHT_MOTOR,CH_LEFT_MOTOR)
digger = digger.DiggerArm(servo, CH_DIGGER_MOTOR, CH_ARM_MOTOR)

connected = False
try:
    while True :
        armPower = 0;
        digPower = 0;

        if j.connected():
            if connected == False:
                print("Joystick connected")
                connected = True
            else:
                drivetrain.drive(j.leftX() * .40, -(j.leftY() * .5))  
                
                #Arm/digger
                """ Commented out for now
                if j.A() :
                    armPower = 0.2
                else:
                    armPower = 0
                if j.B():
                    digPower = 0.2
                else:
                    digPower = 0
                digger.setMotorPower(armPower, digPower)
                """
            
                  
        else:
            drivetrain.stop()
            digger.stop()
            if connected == True:
                print("Joystick disconnected "+ j.connected())
            connected = False

        

    time.sleep(0.02)

except:
    drivetrain.close
    digger.close
    raise