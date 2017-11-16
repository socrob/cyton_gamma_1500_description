cmake_minimum_required(VERSION 2.8.3)
project(cyton_gamma_1500_description)

find_package(catkin REQUIRED COMPONENTS xacro)

catkin_package(
)


### INSTALLS

# to make the install effective you need to run
#    catkin build --this --make-args install

# install arm mesh files in gazebo path
set(GAZEBO_MODEL_PATH $ENV{HOME}/.gazebo/models)
add_custom_target(COMMAND cmake -E make_directory ${GAZEBO_MODEL_PATH}/${PROJECT_NAME})

install(DIRECTORY meshes
  DESTINATION ${GAZEBO_MODEL_PATH}/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.dae"
)
