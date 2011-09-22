import logging


def setupAcceptanceTests(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    portal = context.getSite()

    if context.readDataFile('plone.app.deco.acceptance.txt') is None:
        return

    # Add additional setup code here
    createContent(portal)


def createContent(portal):
    """Delete the standard Plone content that we don't need"""

    log = logging.getLogger("plone.app.deco")
    portal.invokeFactory('page', 'deco-page', title="Deco page",
            description="for acceptance test")
    log.info("Content created")
