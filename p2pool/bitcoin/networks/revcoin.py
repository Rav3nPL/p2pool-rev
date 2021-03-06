import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '5331cdbb'.decode('hex')
P2P_PORT = 7571
ADDRESS_VERSION = 60
RPC_PORT = 7572
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '00000000053db42cc4eb4f24cf78f26ac099557065043ba9651680c32eb349be')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'RVC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'revcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/revcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.revcoin'), 'revcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://www.blockexperts.com/rvc/hash/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://www.blockexperts.com/rvc/address/'
TX_EXPLORER_URL_PREFIX = 'https://www.blockexperts.com/rvc/tx/'
SANE_TARGET_RANGE = (2**256//2**32//10000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
