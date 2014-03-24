import ckan.plugins as plugins



class VDOJThemePluginClass(plugins.SingletonPlugin):
    """
    Setup plugin
    """


    plugins.implements(plugins.IConfigurer, inherit=True)

    def update_config(self, config):
        plugins.toolkit.add_template_directory(config, 'templates')
        plugins.toolkit.add_public_directory(config, 'public')
        print config



