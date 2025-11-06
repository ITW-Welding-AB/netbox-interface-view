from extras.plugins import PluginTemplateExtension
from django.urls import reverse


class DeviceInterfaceGridButton(PluginTemplateExtension):
    """Add Interface Grid View button to device pages"""
    
    model = 'dcim.device'
    
    def buttons(self):
        """Add button to device detail page"""
        obj = self.context['object']
        return f'''
        <a href="{reverse('plugins:netbox_interface_view:interface_grid', kwargs={'device_id': obj.pk})}" 
           class="btn btn-sm btn-primary" 
           title="View Interface Grid">
            <i class="mdi mdi-view-grid"></i> View Interface Grid
        </a>
        '''


template_extensions = [DeviceInterfaceGridButton]
