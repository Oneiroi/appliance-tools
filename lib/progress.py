import sys

'''
__author__="David Busby"
__copyright__="David Busby <d.busby@saiweb.co.uk>, Psycle Interactive Limited <david.busby@psycle.com>"
__license__="GNU v3 + part 5d section 7: Redistribution/Reuse of this code is permitted under the GNU v3 license, as an additional term ALL code must carry the original Author(s) credit in comment form."
'''

class opts:
        slen = 0

def _progressBar(cPer,cLen):
        str = '['
        it = 100/cLen
        offset = 0
        while offset < 100:
                if offset >= cPer:
                        str = '%s ' % str
                else:
                        str = '%s=' % str
                offset += it
        str = '%s]' % str
        return str

def _cliProgress(str):
        str = " %s" % str

        while len(str) < opts.slen:
            str = '%s ' % str
        opts.slen = len(str)
        sys.stderr.write(str + '\r')
        sys.stderr.flush()
