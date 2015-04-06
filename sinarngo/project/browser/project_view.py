from five import grok
from plone.directives import dexterity, form
from sinarngo.project.content.project import IProject

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IProject)
    grok.require('zope2.View')
    grok.template('project_view')
    grok.name('view')

