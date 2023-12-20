# custom.py 만드는 이유
# 개인별로 바퀴 회전수, Servo Motor 각도가 다르다
# 따라서, 미세조정한 값들을 담아두는 python파일이 필요하다
from jetbot import Robot

robot = Robot()

def forward():
    robot.left_motor.value = 0.5
    robot.right_motor.value = 0.6
    
def backword():
    robot.left_motor.value = -0.5
    robot.right_motor.value = -0.6

def left():
    robot.left_motor.value = 0.6
    robot.right_motor.value = 0.3
    
def right():
    robot.left_motor.value = 0.3
    robot.right_motor.value = 0.6

def stop():
    robot.left_motor.value = 0.0
    robot.right_motor.value = 0.0    

print('Hello World')

# 내가 직접 해당 python을 실행(run)하면
# __name__ 내장변수가 __main__로 바뀐다
# 외부에서 해당 python을 import해서 사용하면
# __name__ 내장변수가 안 바뀐다!!

if __name__ == '__main__':
    print('크리티컬한 작업')

