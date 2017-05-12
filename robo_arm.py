import vrep
import sys

vrep.simxFinish(-1)
clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

if clientID != -1:
	print('Connected to remove API server')
else:
	print("Connection not successful")
	sys.exit('Error: Could not connect')

errorCode,joint_2 = vrep.simxGetObjectHandle(clientID,'redundantRob_joint2',vrep.simx_opmode_oneshot_wait)

def joint_2_force():
	vrep.simxSetJointForce(clientID,joint_2,0.01,vrep.simx_opmode_oneshot)

while True:
	joint_2_force()
	returnCode,force=vrep.simxGetJointForce(clientID,joint_2,vrep.simx_opmode_streaming)
	print(force)