from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['revcoin_testnet']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 60*60//10 # shares
REAL_CHAIN_LENGTH = 60*60//10 # shares
TARGET_LOOKBEHIND = 5 # shares
SPREAD = 3 # blocks
IDENTIFIER = '1122334455667788'.decode('hex')
PREFIX = 'aabbccddeeff0011'.decode('hex')
P2P_PORT = 18571
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 18572
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = ''
VERSION_CHECK = lambda v: None if 70000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
#SOFTFORKS_REQUIRED = set(['bip65', 'csv'])
#MINIMUM_PROTOCOL_VERSION = 1600
