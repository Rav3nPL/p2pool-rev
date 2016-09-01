import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '81abaa68'.decode('hex')
P2P_PORT = 17571
ADDRESS_VERSION = 111
RPC_PORT = 17572
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '00000000053db42cc4eb4f24cf78f26ac099557065043ba9651680c32eb349be')) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'RVCt'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'revcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/revcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.revcoin'), 'revcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = ''
ADDRESS_EXPLORER_URL_PREFIX = ''
TX_EXPLORER_URL_PREFIX = ''
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
