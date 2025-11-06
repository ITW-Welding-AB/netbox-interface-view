# Examples and Screenshots

This document provides examples of how to use the NetBox Interface View plugin.

## Example 1: 48-Port Switch (2 Rows)

For a typical 48-port network switch with ports arranged in 2 rows:

**Configuration:**
- Device Custom Field `grid_rows`: `2`
- Device Custom Field `grid_columns`: `24`

This will create a grid that looks like:
```
[Port 1 ] [Port 2 ] [Port 3 ] ... [Port 24]
[Port 25] [Port 26] [Port 27] ... [Port 48]
```

## Example 2: 24-Port Switch (3 Rows)

For a 24-port switch with ports arranged in 3 rows:

**Configuration:**
- Device Custom Field `grid_rows`: `3`
- Device Custom Field `grid_columns`: `8`

This will create a grid that looks like:
```
[Port 1] [Port 2] [Port 3] ... [Port 8 ]
[Port 9] [Port 10] [Port 11] ... [Port 16]
[Port 17] [Port 18] [Port 19] ... [Port 24]
```

## Example 3: VLAN Color Scheme

Here's a recommended color scheme for different VLAN types:

| VLAN Type | Purpose | Hex Color | Visual |
|-----------|---------|-----------|--------|
| Management | Network device management | `#0066CC` | Blue |
| Data | User data traffic | `#00CC66` | Green |
| Voice | VoIP traffic | `#FF9900` | Orange |
| Guest | Guest network | `#9966CC` | Purple |
| Server | Server VLAN | `#CC0000` | Red |
| DMZ | Demilitarized zone | `#FFCC00` | Yellow |
| Storage | Storage network | `#00CCCC` | Cyan |

## Example 4: Filtering Interfaces

When viewing the grid, you can filter out virtual and logical interfaces:

1. Click the **Exclude Interface Types** dropdown
2. Select types to exclude:
   - `Virtual`
   - `LAG`
   - `Loopback`
   - `Bridge`
3. Click **Apply Filter**

This is useful when you want to see only physical ports.

## Example 5: Interface Status Indicators

The grid uses color-coded indicators to show interface status:

- **Green dot (●)**: Interface has a cable connected and is enabled
- **Gray dot (●)**: Interface is not connected
- **Red dot (●)**: Interface is administratively disabled

## Example 6: VLAN Visualization

Each interface cell shows VLAN information:

- **Border Color**: The color of the untagged VLAN
- **Small Colored Dots**: Each dot represents a tagged VLAN

For example, an interface with:
- Untagged VLAN 10 (blue, `#0066CC`)
- Tagged VLANs 20 (green, `#00CC66`) and 30 (orange, `#FF9900`)

Would display with:
- A blue border
- Two small dots (one green, one orange) in the cell

## Workflow Example

### Setting Up a New Device

1. **Create the device** in NetBox with all interfaces
2. **Set grid dimensions**:
   - Navigate to the device
   - Click Edit
   - Set `grid_rows` and `grid_columns` to match the physical layout
   - Save
3. **Configure VLANs** with colors:
   - Navigate to each VLAN
   - Set the `color` custom field with a hex code
   - Save
4. **Assign VLANs to interfaces** as needed
5. **View the grid**:
   - Navigate to the device
   - Click **View Interface Grid**
   - Use filters to customize the view

## Tips and Best Practices

1. **Match Physical Layout**: Set grid dimensions to match the actual physical port layout of your devices for the most intuitive visualization

2. **Consistent Color Scheme**: Use a consistent color scheme across all VLANs in your organization for easier recognition

3. **Filter Virtual Interfaces**: When viewing physical switches, filter out virtual interface types for a cleaner view

4. **Use Descriptive Interface Names**: The grid displays interface names, so use clear naming conventions

5. **Document Color Codes**: Keep a reference document with your organization's VLAN color scheme

6. **Grid Size Limits**: For devices with many interfaces (e.g., 96+ ports), consider using larger column counts but fewer rows for better visibility

## Troubleshooting Common Issues

### Issue: Grid doesn't match physical layout
**Solution**: Adjust the `grid_rows` and `grid_columns` custom fields on the device to match the actual port layout.

### Issue: All interfaces show gray
**Solution**: VLANs need the `color` custom field set. Edit each VLAN and add a hex color code.

### Issue: Too many empty cells
**Solution**: Reduce the grid dimensions to better match the number of interfaces on the device.

### Issue: Can't see physical ports
**Solution**: Use the interface type filter to exclude virtual, LAG, and other logical interface types.

## Advanced Usage

### Custom Layouts for Modular Devices

For modular devices with line cards, you might want to create a grid that represents multiple rows per line card:

- Line Card 1: Ports 1-24 (rows 1-2)
- Line Card 2: Ports 25-48 (rows 3-4)

Set `grid_rows` = `4` and `grid_columns` = `12` to create this layout.

### Color-Coding Best Practices

1. Use high-contrast colors for frequently used VLANs
2. Avoid similar colors for different VLAN types
3. Consider color-blind friendly palettes
4. Use darker colors for borders (better visibility)
5. Reserve red for critical/security VLANs

## Integration with NetBox Workflows

The plugin integrates seamlessly with NetBox's existing workflows:

1. **Device Provisioning**: After creating a device, set grid dimensions and view the layout
2. **VLAN Management**: As you create VLANs, assign colors for instant visualization
3. **Cable Management**: The connection indicators update automatically as you document cables
4. **Interface Configuration**: The grid reflects all interface assignments and status changes

## Future Enhancements

Some ideas for future versions:

- Export grid view as PDF or image
- Customizable cell content (show speed, duplex, etc.)
- Drag-and-drop interface to rearrange ports
- Support for stacked switches
- PoE status indicators
- Port utilization graphs
