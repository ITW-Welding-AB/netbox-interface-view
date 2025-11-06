from django.shortcuts import render, get_object_or_404
from django.views import View
from dcim.models import Device, Interface
from ipam.models import VLAN


class InterfaceGridView(View):
    """View for displaying device interfaces in a grid layout"""
    
    def get(self, request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        
        # Get grid dimensions from custom fields (with defaults)
        grid_rows = device.custom_field_data.get('grid_rows', 2)
        grid_columns = device.custom_field_data.get('grid_columns', 24)
        
        # Get filter parameters
        filter_types = request.GET.getlist('exclude_type', [])
        
        # Get all interfaces for this device
        interfaces = Interface.objects.filter(device=device).order_by('name')
        
        # Apply type filters
        if filter_types:
            interfaces = interfaces.exclude(type__in=filter_types)
        
        # Build interface data with VLAN colors and connection status
        interface_list = []
        for interface in interfaces:
            # Get VLAN colors
            untagged_vlan = None
            tagged_vlans = []
            
            if interface.untagged_vlan:
                vlan_color = interface.untagged_vlan.custom_field_data.get('color', '#cccccc')
                untagged_vlan = {
                    'id': interface.untagged_vlan.id,
                    'vid': interface.untagged_vlan.vid,
                    'name': interface.untagged_vlan.name,
                    'color': vlan_color
                }
            
            for vlan in interface.tagged_vlans.all():
                vlan_color = vlan.custom_field_data.get('color', '#cccccc')
                tagged_vlans.append({
                    'id': vlan.id,
                    'vid': vlan.vid,
                    'name': vlan.name,
                    'color': vlan_color
                })
            
            # Check connection status
            is_connected = interface.cable is not None
            is_enabled = interface.enabled
            
            interface_list.append({
                'id': interface.id,
                'name': interface.name,
                'type': interface.type,
                'description': interface.description,
                'enabled': is_enabled,
                'connected': is_connected,
                'untagged_vlan': untagged_vlan,
                'tagged_vlans': tagged_vlans,
            })
        
        # Get unique interface types for filter dropdown
        all_interface_types = Interface.objects.filter(device=device).values_list('type', flat=True).distinct()
        
        context = {
            'device': device,
            'interfaces': interface_list,
            'grid_rows': grid_rows,
            'grid_columns': grid_columns,
            'total_cells': grid_rows * grid_columns,
            'interface_types': list(all_interface_types),
            'excluded_types': filter_types,
        }
        
        return render(request, 'netbox_interface_view/interface_grid.html', context)
