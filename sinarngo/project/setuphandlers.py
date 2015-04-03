from collective.grok import gs
from sinarngo.project import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.project', 
    title=_('sinarngo.project import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.project.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
