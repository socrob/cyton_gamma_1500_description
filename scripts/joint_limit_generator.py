#!/usr/bin/env python

import math

'''
This code can be used to generate URDF joint limits from dynamixel joint bit limits

Usage : modify joint_limits_in_bits vector with your own values and run this code by doing:

python joint_limit_generator.py

'''

# --------- MODIFY HERE WITH YOUR VALUES FROM WINDOWS DYNAMIXEL APP EEPROM REGISTERS -------------

# joint limits = [[CW_angle_limit_joint0, CCW_angle_limt_joint0], [CW_angle_limit_joint1, CCW_angle_limt_joint1] etc...] 
joint_limits_in_bits = [[385, 3715], [935, 3115], [1040, 3175], [1000, 3100], [825, 3000], [1020, 3050], [400, 3700], [200, 1190]]

# -------------------------------------------------------------------------------------------------

# to store the joint limits in degrees
joint_limits_in_deg = []

# to store the joint limits in radians
joint_limits_in_rad = []

# to store the ROS URDF joint limits in radians, ROS ANGLE = DYNAMIXEL ANGLE - 180 deg
joint_limits_urdf = []

def bit_to_deg(bit_angle):
    '''
    Function to convert angles expressed in bits to degrees
    '''
    return bit_angle * 360.0 / 4095.0

def bit_to_rad(bit_angle):
    '''
    Function to convert angles expressed in bits to radians
    '''
    return bit_angle * 6.283185307179586 / 4095.0

def dynamixel_to_urdf_angle(dynamixel_angle_in_rad):
    '''
    Function to convert angles expressed in dynamixel format to URDF format
    '''
    return dynamixel_angle_in_rad - math.pi

# convert bit joint limits to degrees
for joint in joint_limits_in_bits:
    joint_limits_in_deg.append([bit_to_deg(joint[0]), bit_to_deg(joint[1])])

# convert bit joint limits to radians
for joint in joint_limits_in_bits:
    joint_limits_in_rad.append([bit_to_rad(joint[0]), bit_to_rad(joint[1])])

# convert bit joint limits to urdf format
for joint in joint_limits_in_rad:
    joint_limits_urdf.append([dynamixel_to_urdf_angle(joint[0]), dynamixel_to_urdf_angle(joint[1])])

# print 'joint limits in degrees : ' + str(joint_limits_in_deg)
# print 'joint limits in radians : ' + str(joint_limits_in_rad)

# print URDF angles with 4 decimals
i = 0
for joint in joint_limits_urdf:
    print 'joint' + str(i) + ' URDF limits = (' + str(round(joint[0], 4)) + ', ' + str(round(joint[1], 4)) + ')'
    i = i + 1

