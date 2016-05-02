""" wrapper class built from parts scavenged from pyzmq sugar/context.py"""

from ZeroMQ import ZContext
from zmq.socket import Socket

class Context:

    sockopts = None
    _shadow = False
    _zcontext = None
    def __init__(self, io_threads=1, **kwargs):
        #super(Context, self).__init__(io_threads=io_threads, **kwargs)
        #if kwargs.get('shadow', False):
        #    self._shadow = True
        #else:
        #    self._shadow = False
        self.sockopts = {}
        self._zcontext = ZContext()

    _instance = None
    # static method copied from tornado IOLoop.instance
    @classmethod
    def instance(cls, io_threads=1):
        """Returns a global Context instance.
        Most single-threaded applications have a single, global Context.
        Use this method instead of passing around Context instances
        throughout your code.
        A common pattern for classes that depend on Contexts is to use
        a default argument to enable programs with multiple Contexts
        but not require the argument for simpler applications:
            class MyClass(object):
                def __init__(self, context=None):
                    self.context = context or Context.instance()
        """
        if cls._instance is None or cls._instance.closed:
            cls._instance = cls(io_threads=io_threads)
        return cls._instance

    @property
    def _socket_class(self):
        return zmq.Socket
    
    def socket(self, socket_type, **kwargs):
        """Create a Socket associated with this Context.
        Parameters
        ----------
        socket_type : int
            The socket type, which can be any of the 0MQ socket types:
            REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, etc.
        **kwargs
            will be passed to the __init__ method of the socket class.
        """
        if self.closed:
            raise ZMQError(ENOTSUP)
        s = self._socket_class(self, socket_type, **kwargs)
        for opt, value in self.sockopts.items():
            try:
                s.setsockopt(opt, value)
            except ZMQError:
                # ignore ZMQErrors, which are likely for socket options
                # that do not apply to a particular socket type, e.g.
                # SUBSCRIBE for non-SUB sockets.
                pass
        return s 

__all__ = [ 'Context' ]