

ArmAccelLimit = 100 # slows down arm.

class DiggerArm:
	def __init__(self, maestro,chDigger, chArm):
		self.maestro = maestro
		self.chDigger = chDigger
		self.chArm = chArm
		# Init motor accel/speed params
		self.maestro.setAccel(chDigger,0)
		self.maestro.setAccel(chArm,0)
		self.maestro.setSpeed(chDigger,0)
		self.maestro.setSpeed(chArm,ArmAccelLimit)
		# Right motor min/center/max vals
		self.minR = 3000
		self.centerMotorArm = 6000
		self.maxMotorArm = 9000
		# Left motor min/center/max vals
		self.minMotorDig = 3000
		self.centerMotorDig = 6000
		self.maxMotorDig = 9000


	# Scale motor speeds (-1 to 1) to maestro servo target values
	def maestroScale(self, motorArm, motorDig):
		if (motorArm >= 0) :
			r = int(self.centerMotorArm + (self.maxMotorArm - self.centerMotorArm) * motorArm)
		else:
			r = int(self.centerMotorArm + (self.centerMotorArm - self.minMotorArm) * motorArm)
		if (motorDig >= 0) :
			l = int(self.centerMotorDig + (self.maxMotorDig - self.centerMotorDig) * motorDig)
		else:
			l = int(self.centerMotorDig + (self.centerMotorDig - self.minMotorDig) * motorDig)
		return (r, l)


	def setMotorPower(self, motorArm, motorDig):
		(servoArm, servoDig) = self.maestroScale(motorArm, motorDig)
		self.maestro.setTarget(self.chArm, servoArm)
		self.maestro.setTarget(self.chDigger, servoDig)

	def stop(self):
		self.setMotorPower(0, 0)

	def close(self):
		self.stop()
