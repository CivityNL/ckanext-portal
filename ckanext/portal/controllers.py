from ckan.plugins import toolkit


class PortalController(toolkit.BaseController):

    def portal_page(self):
        return toolkit.render('dataplatform-portal/index.html')



def redirect_to_portal(map):
    with map.submapper(controller='portal') as m:
        m.connect('index', '/', action='index')
        m.connect('dataplatform-portal', '/portal', action='portal_page')