execute_process(COMMAND "/home/BB/catkin_ws/build/animated_markers/animated_marker_tutorial/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/BB/catkin_ws/build/animated_markers/animated_marker_tutorial/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
