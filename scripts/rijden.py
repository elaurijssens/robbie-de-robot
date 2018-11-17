from gpiozero import Robot
robby = Robot(left = (7, 8), right = (9, 10))
while True:
	robby.forward()
	sleep(3)
	robby.stop()
	robby.right()
	sleep(1)
	robby.stop()

