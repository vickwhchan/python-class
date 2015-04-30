'''
#-- Circuitous(tm), name matters
#-- elevator pitch, one sentence to intro yourself/project/what your startup company does, like mission statement (-> focus), help to get money, and employees

smart advanced circle analytic technology
'''

#-- inheritance <- sole purpose is code reuse (one class can
#-- new-style classes inherit from object giving them extra
#-- documenting first focuses the mind
#-- python makes documenting easy and there are early payoffs
#-- help() tooltops() pydoc sphinx
#-- test first

class circle(object):
    '''An advanced circle analytic toolkit'''

#-- "this" is a cultural norm in the python which lowers the TCO
#-- when copying data from one namespace another, prefer to keep the name same

def __init__(self, r):
    "Initialize by storing the radius"
    self.r = r


