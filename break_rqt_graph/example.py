import rospkg, sys, os
rospack = rospkg.RosPack()
sys.path = [os.path.join(rospack.get_path('break_rqt_graph'),'lib/python2.7/site-packages')] + sys.path

print "import pyparsing"
import pyparsing
print pyparsing


