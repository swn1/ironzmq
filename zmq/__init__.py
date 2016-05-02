import clr
import os
#zmqdll = os.path.join(os.path.dirname(__file__), "zeromq.dll")
assm=clr.LoadAssemblyFromFile("ZeroMQ.dll")
clr.AddReference(assm)
import ZeroMQ
# make an object to force static class initializations
ZeroMQ.ZFrame()

from .constants import *
from .error import ZMQError
from .socket import Socket
from .context import Context
from .sugar import Poller, MessageTracker