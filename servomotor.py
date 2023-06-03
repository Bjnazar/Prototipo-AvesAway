import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

pwm1 = GPIO.PWM(18, 50)
pwm1.start(0)

pwm2 = GPIO.PWM(17, 50)
pwm2.start(0)

def set_angle(servo, angle):
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Mueve el primer servomotor entre 0 y 180 grados en incrementos de 10
        for angle in range(0, 181, 10):
            set_angle(18, angle)
            time.sleep(0.5)

        # Mueve el primer servomotor de regreso a 0 grados
        set_angle(18, 0)
        time.sleep(1)

        # Mueve el segundo servomotor entre 45 y 135 grados en incrementos de 15
        for angle in range(45, 136, 15):
            set_angle(17, angle)
            time.sleep(0.5)

        # Mueve el segundo servomotor de regreso a 45 grados
        set_angle(17, 45)
        time.sleep(1)

except KeyboardInterrupt:
    pass

pwm1.stop()
pwm2.stop()
GPIO.cleanup()


# que se muevan una vez
# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(17, GPIO.OUT)

# pwm1 = GPIO.PWM(18, 50)
# pwm1.start(0)

# pwm2 = GPIO.PWM(17, 50)
# pwm2.start(0)

# def set_angle(servo, angle):
#     duty = angle / 18 + 2
#     GPIO.output(servo, True)
#     pwm.ChangeDutyCycle(duty)
#     time.sleep(1)
#     GPIO.output(servo, False)
#     pwm.ChangeDutyCycle(0)

# set_angle(18, 90)  # Gira el primer servo a 90 grados
# set_angle(17, 45)  # Gira el segundo servo a 45 grados

# pwm1.stop()
# pwm2.stop()
# GPIO.cleanup()

# que se mueva un solo motor
# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)

# pwm = GPIO.PWM(18, 50)
# pwm.start(0)

# def set_angle(angle):
#     duty = angle / 18 + 2
#     GPIO.output(18, True)
#     pwm.ChangeDutyCycle(duty)
#     time.sleep(1)
#     GPIO.output(18, False)
#     pwm.ChangeDutyCycle(0)

# set_angle(90)  # Gira el servo a 90 grados

# pwm.stop()
# GPIO.cleanup()
