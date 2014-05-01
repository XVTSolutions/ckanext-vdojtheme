import ckan.plugins as plugins
from pylons import app_globals
import ckan.lib.helpers as helpers
from helpers import init_translation, translate_dropdown_text

def is_dataset_page():
        current_url = helpers.full_current_url()
        dataset_page = app_globals.site_url + '/dataset'

        if current_url == dataset_page:
            return True
        else:
            return False


class VDOJThemePluginClass(plugins.SingletonPlugin):
    """
    Setup plugin
    """

    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IConfigurable, inherit=True)

    def update_config(self, config):
        plugins.toolkit.add_template_directory(config, 'templates')
        plugins.toolkit.add_public_directory(config, 'public')

        #configure vicdoj logo
        config['ckan.site_logo'] = 'vdoj-logo-white-transparent.png'



    def get_helpers(self):
        return {
            'is_dataset_page': is_dataset_page,
            'translate_dropdown_text':translate_dropdown_text,
        }

    def configure(self, config):
        #init translation dictionary
        init_translation()


