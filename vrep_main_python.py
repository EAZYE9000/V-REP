import vrep
import sys
import numpy as np
import cv2

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

if clientID!=-1:
    print ('Connected to remote API server')
else:
	print("Connection not successful")
	sys.exit('Error: Could not connect')

errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait)
errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)
errorCode,sensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultasoniceSensor1',vrep.simx_opmode_oneshot_wait)
errorCode, cam_handle=vrep.simxGetObjectHandle(clientID,'cam1',vrep.simx_opmode_oneshot_wait)

errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,0.2,vrep.simx_opmode_streaming)
errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,0.2,vrep.simx_opmode_streaming)
returnCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming)

returnCode,resolution,image=vrep.simxGetVisionSensorImage(clientID,cam_handle,0,vrep.simx_opmode_streaming)

while True:
	im = np.array(image, dtype=np.uint8)
	"""cv2.imread(im, 0)
	cv2.imshow('image', im)
	cv2.waitKey()"""