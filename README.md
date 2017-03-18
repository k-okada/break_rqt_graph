# break_rqt_graph

!!!CAUTION!!!

If we build this package, we'll break RQT graph tools

```
k-okada@p40-yoga:/tmp/pip$ echo $ROS_PACKAGE_PATH 
/opt/ros/indigo/share:/opt/ros/indigo/stacks
k-okada@p40-yoga:/tmp/pip$ echo $PYTHONPATH 
/home/k-okada/work/pynaoqi:/opt/ros/indigo/lib/python2.7/dist-packages
k-okada@p40-yoga:/tmp/pip$ rqt_graph 
(Works OK)
k-okada@p40-yoga:/tmp/pip$ catkin build
---------------------------------------------
Profile:                     default
Extending:             [env] /opt/ros/indigo
Workspace:                   /tmp/pip
---------------------------------------------
Source Space:       [exists] /tmp/pip/src
Log Space:         [missing] /tmp/pip/logs
Build Space:        [exists] /tmp/pip/build
Devel Space:        [exists] /tmp/pip/devel
Install Space:      [unused] /tmp/pip/install
DESTDIR:            [unused] None
---------------------------------------------
Devel Space Layout:          linked
Install Space Layout:        None
---------------------------------------------
Additional CMake Args:       None
Additional Make Args:        None
Additional catkin Make Args: None
Internal Make Job Server:    True
Cache Job Environments:      False
---------------------------------------------
Whitelisted Packages:        None
Blacklisted Packages:        None
---------------------------------------------
Workspace configuration appears valid.

NOTE: Forcing CMake to run for each package.
---------------------------------------------
[build] Found '1' packages in 0.0 seconds.                                     
[build] Updating package table.                                                
Starting  >>> catkin_tools_prebuild                                            
Finished  <<< catkin_tools_prebuild                [ 1.3 seconds ]             
Starting  >>> break_rqt_graph                                                  
_______________________________________________________________________________
Warnings   << break_rqt_graph:cmake /tmp/pip/logs/break_rqt_graph/build.cmake.000.log
CMake Warning (dev) at /opt/ros/indigo/share/catkin_pip/cmake/catkin-pip-env.cmake:27 (message):
  Incomplete catkin-pip setup detected.This is expected if you use catkin-pip
  from source, and did not source the current develspace yet.Quick patch will
  be applied to the current cmake process environment.
Call Stack (most recent call first):
  /opt/ros/indigo/share/catkin_pip/cmake/catkin-pip-prefix.cmake:127 (catkin_pip_check_env)
  /opt/ros/indigo/share/catkin_pip/cmake/catkin-pip.cmake:63 (catkin_pip_setup_prefix)
  /opt/ros/indigo/share/catkin_pip/cmake/catkin_pipConfig.cmake:190 (include)
  /opt/ros/indigo/share/catkin/cmake/catkinConfig.cmake:76 (find_package)
  CMakeLists.txt:11 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

cd /tmp/pip/build/break_rqt_graph; catkin build --get-env break_rqt_graph | catkin env -si  /usr/bin/cmake /tmp/pip/src/break_rqt_graph --no-warn-unused-cli -DCATKIN_DEVEL_PREFIX=/tmp/pip/devel/.private/break_rqt_graph -DCMAKE_INSTALL_PREFIX=/tmp/pip/install; cd -
...............................................................................
Finished  <<< break_rqt_graph                      [ 13.7 seconds ]            
[build] Summary: All 2 packages succeeded!                                     
[build]   Ignored:   None.                                                     
[build]   Warnings:  1 packages succeeded with warnings.                       
[build]   Abandoned: None.                                                     
[build]   Failed:    None.                                                     
[build] Runtime: 15.1 seconds total.                                           
[build] Note: Workspace packages have changed, please re-source setup files to use them.
k-okada@p40-yoga:/tmp/pip$ source devel/setup.bash 
k-okada@p40-yoga:/tmp/pip$ echo $ROS_PACKAGE_PATH 
/tmp/pip/src/break_rqt_graph:/opt/ros/indigo/share:/opt/ros/indigo/stacks
k-okada@p40-yoga:/tmp/pip$ echo $PYTHONPATH 
/tmp/pip/src/break_rqt_graph:/tmp/pip/devel/.private/break_rqt_graph/lib/python2.7/site-packages:/opt/ros/indigo/lib/python2.7/dist-packages:/home/k-okada/work/pynaoqi
k-okada@p40-yoga:/tmp/pip$ rqt_graph 
Couldn't import dot_parser, loading of dot files will not be possible.
PluginHandlerDirect._restore_settings() plugin "rqt_graph/RosGraph#0" raised an exception:
Traceback (most recent call last):
  File "/opt/ros/indigo/lib/python2.7/dist-packages/qt_gui/plugin_handler_direct.py", line 116, in _restore_settings
    self._plugin.restore_settings(plugin_settings_plugin, instance_settings_plugin)
  File "/opt/ros/indigo/lib/python2.7/dist-packages/rqt_graph/ros_graph.py", line 203, in restore_settings
    self._refresh_rosgraph()
  File "/opt/ros/indigo/lib/python2.7/dist-packages/rqt_graph/ros_graph.py", line 227, in _refresh_rosgraph
    self._update_graph_view(self._generate_dotcode())
  File "/opt/ros/indigo/lib/python2.7/dist-packages/rqt_graph/ros_graph.py", line 260, in _update_graph_view
    self._redraw_graph_view()
  File "/opt/ros/indigo/lib/python2.7/dist-packages/rqt_graph/ros_graph.py", line 293, in _redraw_graph_view
    same_label_siblings=True)
  File "/opt/ros/indigo/lib/python2.7/dist-packages/qt_dotgraph/dot_to_qt.py", line 234, in dotcode_to_qt_items
    graph = pydot.graph_from_dot_data(dotcode.encode("ascii", "ignore"))
  File "/usr/lib/python2.7/dist-packages/pydot.py", line 220, in graph_from_dot_data
    return dot_parser.parse_dot_data(data)
NameError: global name 'dot_parser' is not defined

```
