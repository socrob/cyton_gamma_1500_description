cmake_minimum_required(VERSION 2.8.3)
project(cyton_gamma_1500_description)

find_package(catkin REQUIRED COMPONENTS xacro)

catkin_package(
)

set(GAZEBO_MODEL_PATH $ENV{HOME}/.gazebo/models)


### INSTALLS

# to make the install effective you need to run
#    catkin build --this --make-args install

install(DIRECTORY meshes/arm
  DESTINATION ${GAZEBO_MODEL_PATH}/mbot
  FILES_MATCHING PATTERN "*.dae"
  PATTERN "*.png"
)

install(DIRECTORY meshes/gripper
  DESTINATION ${GAZEBO_MODEL_PATH}/mbot
  FILES_MATCHING PATTERN "*.dae"
  PATTERN "*.png"
)
