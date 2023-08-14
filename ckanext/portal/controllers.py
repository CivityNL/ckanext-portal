from ckan.plugins import toolkit


class PortalController(toolkit.BaseController):

    def portal_index(self):
        return toolkit.render('dataplatform-portal/index.html')
