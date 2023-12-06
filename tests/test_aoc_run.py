import os
from pathlib import Path
import synapse.exc as s_exc
import synapse.common as s_common
import pprint
import synapse.tests.utils as s_test


import synapse.tests.utils as s_test

configdir = Path(__file__).parent.parent
dirname = os.path.abspath(os.path.dirname(__file__))

class AOCTestRun(s_test.StormPkgTest):

    assetdir = os.path.join(dirname, 'testassets')
    pkgprotos = (os.path.join(configdir, 'aoc.yaml'),)

    async def test_aoc_run(self):

        async with self.getTestCore() as core:

            msgs = await core.stormlist(
                'aoc.run --debug --day=1 --part=b'
            )
            pprint.pprint(msgs)
            self.stormHasNoWarnErr(msgs)


