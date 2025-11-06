from extras.plugins import PluginConfig


class NetBoxInterfaceViewConfig(PluginConfig):
    name = 'netbox_interface_view'
    verbose_name = 'NetBox Interface View'
    description = 'NetBox Plugin for viewing interfaces with stylish layout'
    version = '0.1'
    base_url = 'interface-view'


config = NetBoxInterfaceViewConfig
