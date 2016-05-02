#-----------------------------------------------------------------------------
# Python module level constants
#-----------------------------------------------------------------------------

from ZeroMQ.lib.zmq import Version
VERSION = Version.ToString()
VERSION_MAJOR = Version.Major
VERSION_MINOR = Version.Minor
VERSION_PATCH = Version.Build
del Version

from ZeroMQ.ZSocketOption import NOBLOCK
from ZeroMQ.ZSocketFlags import DontWait as DONTWAIT
#NOBLOCK = ZMQ_NOBLOCK
#DONTWAIT = ZMQ_DONTWAIT

from ZeroMQ.ZPoll import In as POLLIN, Out as POLLOUT, Err as POLLERR
#POLLIN = ZMQ_POLLIN
#POLLOUT = ZMQ_POLLOUT
#POLLERR = ZMQ_POLLERR
#POLLPRI = ZMQ_POLLPRI
#SNDMORE = ZMQ_SNDMORE
#STREAMER = ZMQ_STREAMER
#FORWARDER = ZMQ_FORWARDER
#QUEUE = ZMQ_QUEUE
#IO_THREADS_DFLT = ZMQ_IO_THREADS_DFLT
#MAX_SOCKETS_DFLT = ZMQ_MAX_SOCKETS_DFLT
#POLLITEMS_DFLT = ZMQ_POLLITEMS_DFLT
#THREAD_PRIORITY_DFLT = ZMQ_THREAD_PRIORITY_DFLT
#THREAD_SCHED_POLICY_DFLT = ZMQ_THREAD_SCHED_POLICY_DFLT

from ZeroMQ.ZSocketType import PAIR, PUB, SUB, REQ, REP, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB
#PAIR = ZMQ_PAIR
#PUB = ZMQ_PUB
#SUB = ZMQ_SUB
#REQ = ZMQ_REQ
#REP = ZMQ_REP
#DEALER = ZMQ_DEALER
#ROUTER = ZMQ_ROUTER
#XREQ = ZMQ_XREQ
#XREP = ZMQ_XREP
#PULL = ZMQ_PULL
#PUSH = ZMQ_PUSH
#XPUB = ZMQ_XPUB
#XSUB = ZMQ_XSUB

#UPSTREAM = ZMQ_UPSTREAM
#DOWNSTREAM = ZMQ_DOWNSTREAM
#STREAM = ZMQ_STREAM
#CLIENT = ZMQ_CLIENT
#SERVER = ZMQ_SERVER
#EVENT_CONNECTED = ZMQ_EVENT_CONNECTED
#EVENT_CONNECT_DELAYED = ZMQ_EVENT_CONNECT_DELAYED
#EVENT_CONNECT_RETRIED = ZMQ_EVENT_CONNECT_RETRIED
#EVENT_LISTENING = ZMQ_EVENT_LISTENING
#EVENT_BIND_FAILED = ZMQ_EVENT_BIND_FAILED
#EVENT_ACCEPTED = ZMQ_EVENT_ACCEPTED
#EVENT_ACCEPT_FAILED = ZMQ_EVENT_ACCEPT_FAILED
#EVENT_CLOSED = ZMQ_EVENT_CLOSED
#EVENT_CLOSE_FAILED = ZMQ_EVENT_CLOSE_FAILED
#EVENT_DISCONNECTED = ZMQ_EVENT_DISCONNECTED
#EVENT_ALL = ZMQ_EVENT_ALL
#EVENT_MONITOR_STOPPED = ZMQ_EVENT_MONITOR_STOPPED
#globals()['NULL'] = ZMQ_NULL
#PLAIN = ZMQ_PLAIN
#CURVE = ZMQ_CURVE
#GSSAPI = ZMQ_GSSAPI

from ZeroMQ.ZError import EAGAIN, EINVAL, EFAULT, ENOMEM, ENODEV, EMSGSIZE
#EAGAIN = ZMQ_EAGAIN
#EINVAL = ZMQ_EINVAL
#EFAULT = ZMQ_EFAULT
#ENOMEM = ZMQ_ENOMEM
#ENODEV = ZMQ_ENODEV
#EMSGSIZE = ZMQ_EMSGSIZE
from ZeroMQ.ZError import EAFNOSUPPORT, ENETUNREACH, ECONNABORTED, ECONNRESET, ENOTCONN
#EAFNOSUPPORT = ZMQ_EAFNOSUPPORT
#ENETUNREACH = ZMQ_ENETUNREACH
#ECONNABORTED = ZMQ_ECONNABORTED
#ECONNRESET = ZMQ_ECONNRESET
#ENOTCONN = ZMQ_ENOTCONN
from ZeroMQ.ZError import ETIMEDOUT, EHOSTUNREACH, ENETRESET, ENOTSUP, EPROTONOSUPPORT
#ETIMEDOUT = ZMQ_ETIMEDOUT
#EHOSTUNREACH = ZMQ_EHOSTUNREACH
#ENETRESET = ZMQ_ENETRESET
#HAUSNUMERO = ZMQ_HAUSNUMERO
#ENOTSUP = ZMQ_ENOTSUP
#EPROTONOSUPPORT = ZMQ_EPROTONOSUPPORT
from ZeroMQ.ZError import ENOBUFS, ENETDOWN, EADDRINUSE, EADDRNOTAVAIL
#ENOBUFS = ZMQ_ENOBUFS
#ENETDOWN = ZMQ_ENETDOWN
#EADDRINUSE = ZMQ_EADDRINUSE
#EADDRNOTAVAIL = ZMQ_EADDRNOTAVAIL
from ZeroMQ.ZError import ECONNREFUSED, EINPROGRESS, ENOTSOCK, EFSM, ENOCOMPATPROTO
#ECONNREFUSED = ZMQ_ECONNREFUSED
#EINPROGRESS = ZMQ_EINPROGRESS
#ENOTSOCK = ZMQ_ENOTSOCK
#EFSM = ZMQ_EFSM
#ENOCOMPATPROTO = ZMQ_ENOCOMPATPROTO
from ZeroMQ.ZError import ETERM, EMTHREAD
#ETERM = ZMQ_ETERM
#EMTHREAD = ZMQ_EMTHREAD

#IO_THREADS = ZMQ_IO_THREADS
#MAX_SOCKETS = ZMQ_MAX_SOCKETS
#SOCKET_LIMIT = ZMQ_SOCKET_LIMIT
#THREAD_PRIORITY = ZMQ_THREAD_PRIORITY
#THREAD_SCHED_POLICY = ZMQ_THREAD_SCHED_POLICY
#BLOCKY = ZMQ_BLOCKY
#IDENTITY = ZMQ_IDENTITY
#SUBSCRIBE = ZMQ_SUBSCRIBE
#UNSUBSCRIBE = ZMQ_UNSUBSCRIBE
#LAST_ENDPOINT = ZMQ_LAST_ENDPOINT
#TCP_ACCEPT_FILTER = ZMQ_TCP_ACCEPT_FILTER
#PLAIN_USERNAME = ZMQ_PLAIN_USERNAME
#PLAIN_PASSWORD = ZMQ_PLAIN_PASSWORD
#CURVE_PUBLICKEY = ZMQ_CURVE_PUBLICKEY
#CURVE_SECRETKEY = ZMQ_CURVE_SECRETKEY
#CURVE_SERVERKEY = ZMQ_CURVE_SERVERKEY
#ZAP_DOMAIN = ZMQ_ZAP_DOMAIN
#CONNECT_RID = ZMQ_CONNECT_RID
#GSSAPI_PRINCIPAL = ZMQ_GSSAPI_PRINCIPAL
#GSSAPI_SERVICE_PRINCIPAL = ZMQ_GSSAPI_SERVICE_PRINCIPAL
#SOCKS_PROXY = ZMQ_SOCKS_PROXY
#XPUB_WELCOME_MSG = ZMQ_XPUB_WELCOME_MSG
#FD = ZMQ_FD
#RECONNECT_IVL_MAX = ZMQ_RECONNECT_IVL_MAX
#SNDTIMEO = ZMQ_SNDTIMEO
#RCVTIMEO = ZMQ_RCVTIMEO
#SNDHWM = ZMQ_SNDHWM
#RCVHWM = ZMQ_RCVHWM
#MULTICAST_HOPS = ZMQ_MULTICAST_HOPS
#IPV4ONLY = ZMQ_IPV4ONLY
#ROUTER_BEHAVIOR = ZMQ_ROUTER_BEHAVIOR
#TCP_KEEPALIVE = ZMQ_TCP_KEEPALIVE
#TCP_KEEPALIVE_CNT = ZMQ_TCP_KEEPALIVE_CNT
#TCP_KEEPALIVE_IDLE = ZMQ_TCP_KEEPALIVE_IDLE
#TCP_KEEPALIVE_INTVL = ZMQ_TCP_KEEPALIVE_INTVL
#DELAY_ATTACH_ON_CONNECT = ZMQ_DELAY_ATTACH_ON_CONNECT
#XPUB_VERBOSE = ZMQ_XPUB_VERBOSE
#EVENTS = ZMQ_EVENTS
#TYPE = ZMQ_TYPE
#LINGER = ZMQ_LINGER
#RECONNECT_IVL = ZMQ_RECONNECT_IVL
#BACKLOG = ZMQ_BACKLOG
#ROUTER_MANDATORY = ZMQ_ROUTER_MANDATORY
#FAIL_UNROUTABLE = ZMQ_FAIL_UNROUTABLE
#ROUTER_RAW = ZMQ_ROUTER_RAW
#IMMEDIATE = ZMQ_IMMEDIATE
#IPV6 = ZMQ_IPV6
#MECHANISM = ZMQ_MECHANISM
#PLAIN_SERVER = ZMQ_PLAIN_SERVER
#CURVE_SERVER = ZMQ_CURVE_SERVER
#PROBE_ROUTER = ZMQ_PROBE_ROUTER
#REQ_RELAXED = ZMQ_REQ_RELAXED
#REQ_CORRELATE = ZMQ_REQ_CORRELATE
#CONFLATE = ZMQ_CONFLATE
#ROUTER_HANDOVER = ZMQ_ROUTER_HANDOVER
#TOS = ZMQ_TOS
#IPC_FILTER_PID = ZMQ_IPC_FILTER_PID
#IPC_FILTER_UID = ZMQ_IPC_FILTER_UID
#IPC_FILTER_GID = ZMQ_IPC_FILTER_GID
#GSSAPI_SERVER = ZMQ_GSSAPI_SERVER
#GSSAPI_PLAINTEXT = ZMQ_GSSAPI_PLAINTEXT
#HANDSHAKE_IVL = ZMQ_HANDSHAKE_IVL
#XPUB_NODROP = ZMQ_XPUB_NODROP
#XPUB_MANUAL = ZMQ_XPUB_MANUAL
#STREAM_NOTIFY = ZMQ_STREAM_NOTIFY
#INVERT_MATCHING = ZMQ_INVERT_MATCHING
#XPUB_VERBOSER = ZMQ_XPUB_VERBOSER
#HEARTBEAT_IVL = ZMQ_HEARTBEAT_IVL
#HEARTBEAT_TTL = ZMQ_HEARTBEAT_TTL
#HEARTBEAT_TIMEOUT = ZMQ_HEARTBEAT_TIMEOUT
#CONNECT_TIMEOUT = ZMQ_CONNECT_TIMEOUT
#TCP_MAXRT = ZMQ_TCP_MAXRT
#THREAD_SAFE = ZMQ_THREAD_SAFE
#MULTICAST_MAXTPDU = ZMQ_MULTICAST_MAXTPDU
#VMCI_CONNECT_TIMEOUT = ZMQ_VMCI_CONNECT_TIMEOUT
#USE_FD = ZMQ_USE_FD
#AFFINITY = ZMQ_AFFINITY
#MAXMSGSIZE = ZMQ_MAXMSGSIZE
#HWM = ZMQ_HWM
#SWAP = ZMQ_SWAP
#MCAST_LOOP = ZMQ_MCAST_LOOP
#RECOVERY_IVL_MSEC = ZMQ_RECOVERY_IVL_MSEC
#VMCI_BUFFER_SIZE = ZMQ_VMCI_BUFFER_SIZE
#VMCI_BUFFER_MIN_SIZE = ZMQ_VMCI_BUFFER_MIN_SIZE
#VMCI_BUFFER_MAX_SIZE = ZMQ_VMCI_BUFFER_MAX_SIZE
#RATE = ZMQ_RATE
#RECOVERY_IVL = ZMQ_RECOVERY_IVL
#SNDBUF = ZMQ_SNDBUF
#RCVBUF = ZMQ_RCVBUF
#RCVMORE = ZMQ_RCVMORE
#MORE = ZMQ_MORE
#SRCFD = ZMQ_SRCFD
#SHARED = ZMQ_SHARED

#-----------------------------------------------------------------------------
# Symbols to export
#-----------------------------------------------------------------------------
x__all__ = [
  "VERSION",
  "VERSION_MAJOR",
  "VERSION_MINOR",
  "VERSION_PATCH",
  "NOBLOCK",
  "DONTWAIT",
  "POLLIN",
  "POLLOUT",
  "POLLERR",
  "POLLPRI",
  "SNDMORE",
  "STREAMER",
  "FORWARDER",
  "QUEUE",
  "IO_THREADS_DFLT",
  "MAX_SOCKETS_DFLT",
  "POLLITEMS_DFLT",
  "THREAD_PRIORITY_DFLT",
  "THREAD_SCHED_POLICY_DFLT",
  "PAIR",
  "PUB",
  "SUB",
  "REQ",
  "REP",
  "DEALER",
  "ROUTER",
  "XREQ",
  "XREP",
  "PULL",
  "PUSH",
  "XPUB",
  "XSUB",
  "UPSTREAM",
  "DOWNSTREAM",
  "STREAM",
  "CLIENT",
  "SERVER",
  "EVENT_CONNECTED",
  "EVENT_CONNECT_DELAYED",
  "EVENT_CONNECT_RETRIED",
  "EVENT_LISTENING",
  "EVENT_BIND_FAILED",
  "EVENT_ACCEPTED",
  "EVENT_ACCEPT_FAILED",
  "EVENT_CLOSED",
  "EVENT_CLOSE_FAILED",
  "EVENT_DISCONNECTED",
  "EVENT_ALL",
  "EVENT_MONITOR_STOPPED",
  "NULL",
  "PLAIN",
  "CURVE",
  "GSSAPI",
  "EAGAIN",
  "EINVAL",
  "EFAULT",
  "ENOMEM",
  "ENODEV",
  "EMSGSIZE",
  "EAFNOSUPPORT",
  "ENETUNREACH",
  "ECONNABORTED",
  "ECONNRESET",
  "ENOTCONN",
  "ETIMEDOUT",
  "EHOSTUNREACH",
  "ENETRESET",
  "HAUSNUMERO",
  "ENOTSUP",
  "EPROTONOSUPPORT",
  "ENOBUFS",
  "ENETDOWN",
  "EADDRINUSE",
  "EADDRNOTAVAIL",
  "ECONNREFUSED",
  "EINPROGRESS",
  "ENOTSOCK",
  "EFSM",
  "ENOCOMPATPROTO",
  "ETERM",
  "EMTHREAD",
  "IO_THREADS",
  "MAX_SOCKETS",
  "SOCKET_LIMIT",
  "THREAD_PRIORITY",
  "THREAD_SCHED_POLICY",
  "BLOCKY",
  "IDENTITY",
  "SUBSCRIBE",
  "UNSUBSCRIBE",
  "LAST_ENDPOINT",
  "TCP_ACCEPT_FILTER",
  "PLAIN_USERNAME",
  "PLAIN_PASSWORD",
  "CURVE_PUBLICKEY",
  "CURVE_SECRETKEY",
  "CURVE_SERVERKEY",
  "ZAP_DOMAIN",
  "CONNECT_RID",
  "GSSAPI_PRINCIPAL",
  "GSSAPI_SERVICE_PRINCIPAL",
  "SOCKS_PROXY",
  "XPUB_WELCOME_MSG",
  "FD",
  "RECONNECT_IVL_MAX",
  "SNDTIMEO",
  "RCVTIMEO",
  "SNDHWM",
  "RCVHWM",
  "MULTICAST_HOPS",
  "IPV4ONLY",
  "ROUTER_BEHAVIOR",
  "TCP_KEEPALIVE",
  "TCP_KEEPALIVE_CNT",
  "TCP_KEEPALIVE_IDLE",
  "TCP_KEEPALIVE_INTVL",
  "DELAY_ATTACH_ON_CONNECT",
  "XPUB_VERBOSE",
  "EVENTS",
  "TYPE",
  "LINGER",
  "RECONNECT_IVL",
  "BACKLOG",
  "ROUTER_MANDATORY",
  "FAIL_UNROUTABLE",
  "ROUTER_RAW",
  "IMMEDIATE",
  "IPV6",
  "MECHANISM",
  "PLAIN_SERVER",
  "CURVE_SERVER",
  "PROBE_ROUTER",
  "REQ_RELAXED",
  "REQ_CORRELATE",
  "CONFLATE",
  "ROUTER_HANDOVER",
  "TOS",
  "IPC_FILTER_PID",
  "IPC_FILTER_UID",
  "IPC_FILTER_GID",
  "GSSAPI_SERVER",
  "GSSAPI_PLAINTEXT",
  "HANDSHAKE_IVL",
  "XPUB_NODROP",
  "XPUB_MANUAL",
  "STREAM_NOTIFY",
  "INVERT_MATCHING",
  "XPUB_VERBOSER",
  "HEARTBEAT_IVL",
  "HEARTBEAT_TTL",
  "HEARTBEAT_TIMEOUT",
  "CONNECT_TIMEOUT",
  "TCP_MAXRT",
  "THREAD_SAFE",
  "MULTICAST_MAXTPDU",
  "VMCI_CONNECT_TIMEOUT",
  "USE_FD",
  "AFFINITY",
  "MAXMSGSIZE",
  "HWM",
  "SWAP",
  "MCAST_LOOP",
  "RECOVERY_IVL_MSEC",
  "VMCI_BUFFER_SIZE",
  "VMCI_BUFFER_MIN_SIZE",
  "VMCI_BUFFER_MAX_SIZE",
  "RATE",
  "RECOVERY_IVL",
  "SNDBUF",
  "RCVBUF",
  "RCVMORE",
  "MORE",
  "SRCFD",
  "SHARED",
]
