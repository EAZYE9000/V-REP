import vrep
import sys
# In v-rep add a cuboid, Right click on it in Scene Hierachy: Add->Associated child script->Threaded, and paste simExtRemoteApiStart(19999)
vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

if clientID != -1:
	print('Connected to remote API server')
else:
	print("Connection not successful")
	sys.exit("Error: Could not connect")

errorCode, phantom_joint_1 = vrep.simxGetObjectHandle(clientID,'PhantomXPincher_joint1',vrep.simx_opmode_oneshot_wait)
errorCode, phantom_joint_2 = vrep.simxGetObjectHandle(clientID,'PhantomXPincher_joint2',vrep.simx_opmode_oneshot_wait)
errorCode, phantom_joint_3 = vrep.simxGetObjectHandle(clientID,'PhantomXPincher_joint3',vrep.simx_opmode_oneshot_wait)
errorCode, phantom_joint_4 = vrep.simxGetObjectHandle(clientID,'PhantomXPincher_joint4',vrep.simx_opmode_oneshot_wait)
errorCode, phantom_gripper_joint = vrep.simxGetObjectHandle(clientID,'PhantomXPincher_gripperCenter_joint',vrep.simx_opmode_oneshot_wait)
errorCode, phantom_gripper_close_joint = vrep.simxGetObjectHandle(clientID,'PhantomXPincher_gripperClose_joint',vrep.simx_opmode_oneshot_wait)


def joint_force1(x):
    returnCode=vrep.simxSetJointTargetPosition(clientID,phantom_joint_1,x,vrep.simx_opmode_oneshot)
def joint_force2(x):
    returnCode=vrep.simxSetJointTargetPosition(clientID,phantom_joint_2,x,vrep.simx_opmode_oneshot)
def joint_force3(x):
    returnCode=vrep.simxSetJointTargetPosition(clientID,phantom_joint_3,x,vrep.simx_opmode_oneshot)
def joint_force4(x):
    returnCode=vrep.simxSetJointTargetPosition(clientID,phantom_joint_4,x,vrep.simx_opmode_oneshot)
def operate_gripper(x):
    # Set x to 0 to open, 1 to close the gripper
    if x == 0:
        returnCode_1, signalValue = vrep.simxGetIntegerSignal(clientID, "_gripperClose", vrep.simx_opmode_streaming)
        returnCode_2 = vrep.simxSetIntegerSignal(clientID, "_gripperClose", 0, vrep.simx_opmode_oneshot)
        returnCode_3 = vrep.simxSetJointTargetVelocity(clientID, phantom_gripper_close_joint, 2, vrep.simx_opmode_oneshot)
    elif x == 1:
        returnCode_1, signalValue = vrep.simxGetIntegerSignal(clientID, "_gripperClose", vrep.simx_opmode_streaming)
        returnCode_2 = vrep.simxSetIntegerSignal(clientID, "_gripperClose", 1, vrep.simx_opmode_oneshot)
        returnCode_3 = vrep.simxSetJointTargetVelocity(clientID, phantom_gripper_close_joint, -2, vrep.simx_opmode_oneshot)

opmode=vrep.simx_opmode_blocking
res, cuboid0Handle=vrep.simxGetObjectHandle(clientID,"Cuboid0",vrep.simx_opmode_oneshot_wait)
res, cuboidHash0Handle=vrep.simxGetObjectHandle(clientID,"Cuboid0#0",opmode)

errorCode,cuboid0=vrep.simxGetObjectHandle(clientID,'cuboid0',vrep.simx_opmode_blocking)

returnCode_1,cuboid_position=vrep.simxGetObjectPosition(clientID,cuboid0Handle,-1,vrep.simx_opmode_streaming)

print(res)
print(cuboid_position)

while True:
    joint_force1(0.0)
    joint_force2(1.6)
    joint_force3(0.0)
    joint_force4(1.75)
    #returnCode=vrep.simxSetJointTargetVelocity(clientID,phantom_gripper_close_joint,0.00,vrep.simx_opmode_oneshot)
    #returnCode = vrep.simxSetJointForce(clientID, phantom_gripper_close_joint,5.0, vrep.simx_opmode_oneshot)
    #print(force)
    operate_gripper(0)
    #print(position)
    res, cuboid0Handle = vrep.simxGetObjectHandle(clientID, "Cuboid0", vrep.simx_opmode_oneshot_wait)
    returnCode_1, cuboid_position = vrep.simxGetObjectPosition(clientID, cuboid0Handle, -1, vrep.simx_opmode_streaming)
    #print(cuboid_position)
    res, landing_zone = vrep.simxGetObjectHandle(clientID,"landing_zone",vrep.simx_opmode_oneshot_wait)
    returnCode_2, landing_zone_position = vrep.simxGetObjectPosition(clientID, landing_zone, -1, vrep.simx_opmode_streaming)
    #print("Landing Zone:", landing_zone_position)
    returnCode,handle_1=vrep.simxGetCollisionHandle(clientID,"Collision0",vrep.simx_opmode_blocking)
    returnCode, collisionState=vrep.simxReadCollision(clientID,handle_1,vrep.simx_opmode_streaming)
    print(collisionState)
