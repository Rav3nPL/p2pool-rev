from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['revcoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 12*60*60//20 # shares
REAL_CHAIN_LENGTH = 12*60*60//20 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'f8ee33a077c1aa53'.decode('hex')
PREFIX = 'f9002e447ac1e466'.decode('hex')
P2P_PORT = 8571
MIN_TARGET = 10000
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 8572
BOOTSTRAP_ADDRS = 'rav3n.dtdns.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: None if 70000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
#SOFTFORKS_REQUIRED = set(['bip65', 'csv'])
#MINIMUM_PROTOCOL_VERSION = 1600
