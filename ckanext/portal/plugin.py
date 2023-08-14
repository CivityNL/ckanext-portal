import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.portal.logic.auth.get as auth_get
import ckanext.portal.logic.action.get as action_get
import controllers

class PortalPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'portal')

    # IConfigurer
    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator('ignore_missing')
        unicode_safe = toolkit.get_validator('unicode_safe')
        schema.update({
            'ckanext.portal.intro_text': [ignore_missing, unicode_safe]
        })
        return schema

    # IAuthFunctions
    def get_auth_functions(self):
        return {
            'config_option_show': auth_get.config_option_show
        }
    #
    # def get_actions(self):
    #     return {
    #         'scheming_package_show': action_get.scheming_package_show
    #     }

    def after_map(self, map):
        map.connect('portal', '/portal',
            controller='ckanext.portal.controller:PortalController',
            action='portal_index')
        return map