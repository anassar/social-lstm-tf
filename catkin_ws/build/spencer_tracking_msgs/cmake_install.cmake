# Install script for directory: /home/BB/catkin_ws/src/spencer_tracking_msgs

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/BB/catkin_ws/install")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/msg" TYPE FILE FILES
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/DetectedPerson.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/DetectedPersons.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/CompositeDetectedPerson.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/CompositeDetectedPersons.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/TrackedPerson.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/TrackedPersons.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/TrackedPerson2d.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/TrackedPersons2d.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/TrackedGroup.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/TrackedGroups.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/ImmDebugInfo.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/ImmDebugInfos.msg"
    "/home/BB/catkin_ws/src/spencer_tracking_msgs/msg/TrackingTimingMetrics.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/srv" TYPE FILE FILES "/home/BB/catkin_ws/src/spencer_tracking_msgs/srv/GetPersonTrajectories.srv")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/cmake" TYPE FILE FILES "/home/BB/catkin_ws/build/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgs-msg-paths.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/BB/catkin_ws/devel/include/spencer_tracking_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/BB/catkin_ws/devel/share/common-lisp/ros/spencer_tracking_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/BB/catkin_ws/devel/lib/python2.7/dist-packages/spencer_tracking_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/BB/catkin_ws/devel/lib/python2.7/dist-packages/spencer_tracking_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/BB/catkin_ws/build/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgs.pc")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/cmake" TYPE FILE FILES "/home/BB/catkin_ws/build/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgs-msg-extras.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/cmake" TYPE FILE FILES
    "/home/BB/catkin_ws/build/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgsConfig.cmake"
    "/home/BB/catkin_ws/build/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgsConfig-version.cmake"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs" TYPE FILE FILES "/home/BB/catkin_ws/src/spencer_tracking_msgs/package.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

