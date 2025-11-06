from extras.plugins import PluginConfig


class NetBoxInterfaceViewConfig(PluginConfig):
    name = 'netbox_interface_view'
    verbose_name = 'NetBox Interface View'
    description = 'NetBox Plugin for viewing interfaces with stylish layout'
    version = '0.1'
    base_url = 'interface-view'
    min_version = '3.5.0'
    
    def ready(self):
        from .template_content import template_extensions
        self.template_extensions = template_extensions
        super().ready()


config = NetBoxInterfaceViewConfig
