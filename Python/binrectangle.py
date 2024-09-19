import numpy as np
import math
from collections import defaultdict


def generate_square_like_rectangle(area):
    side = int(math.sqrt(area))
    width = side
    height = area // side
    if width * height < area:
        width += 1
    return (width, height)

def pack_rectangles(layout_size, areas, fixed_positions=None):
    layout = np.zeros(layout_size)
    if fixed_positions is None:
        fixed_positions = {}
    
    # Place fixed rectangles first
    for id, (area, position) in fixed_positions.items():
        x, y = position
        rectangle = generate_square_like_rectangle(area)
        if can_place_rectangle(layout, x, y, rectangle):
            place_rectangle(layout, x, y, rectangle, id)
        else:
            print(f"Warning: Cannot place fixed rectangle {id} at position {position}")
    
    # Sort remaining areas for non-fixed rectangles
    remaining_areas = [(i, area) for i, area in enumerate(areas, 1) if i not in fixed_positions]
    remaining_areas.sort(key=lambda x: x[1], reverse=True)
    
    # Place non-fixed rectangles
    current_x, current_y = 0, 0
    for id, area in remaining_areas:
        rectangle = generate_square_like_rectangle(area)
        placed = False
        
        while not placed:
            if can_place_rectangle(layout, current_x, current_y, rectangle):
                place_rectangle(layout, current_x, current_y, rectangle, id)
                placed = True
            else:
                current_x += 1
                if current_x + rectangle[0] > layout_size[1]:
                    current_x = 0
                    current_y += 1
                if current_y + rectangle[1] > layout_size[0]:
                    print(f"Warning: Could not place rectangle {id} with area {area}")
                    break
        
        # Update current_x and current_y for the next rectangle
        if placed:
            current_x += rectangle[0]
            if current_x >= layout_size[1]:
                current_x = 0
                current_y += 1
    
    return layout

def can_place_rectangle(layout, x, y, rectangle):
    width, height = rectangle
    if y + height > layout.shape[0] or x + width > layout.shape[1]:
        return False
    return np.all(layout[y:y+height, x:x+width] == 0)

def place_rectangle(layout, x, y, rectangle, id):
    width, height = rectangle
    layout[y:y+height, x:x+width] = id

def visualize_layout(layout):
    print("Factory Layout:")
    print("  " + " ".join(f"{i:2d}" for i in range(layout.shape[1])))
    for i, row in enumerate(layout):
        print(f"{i:2d}", end=" ")
        for cell in row:
            if cell == 0:
                print(" .", end=" ")
            else:
                print(f"{int(cell):2d}", end=" ")
        print()






def parse_layout_to_profiles(layout):
    # Find unique IDs (excluding 0 which represents empty space)
    unique_ids = np.unique(layout)[1:]
    
    # Dictionary to store coordinates for each ID
    id_coordinates = defaultdict(list)
    
    # Collect coordinates for each ID
    for y in range(layout.shape[0]):
        for x in range(layout.shape[1]):
            id = layout[y, x]
            if id != 0:
                id_coordinates[id].append((x, y))
    
    # Convert coordinates to closed profiles
    profiles = {}
    for id, coords in id_coordinates.items():
        profile = get_closed_profile(coords)
        profiles[id] = profile
    
    return profiles

def get_closed_profile(coords):
    # Find the bounding box
    min_x = min(coord[0] for coord in coords)
    max_x = max(coord[0] for coord in coords)
    min_y = min(coord[1] for coord in coords)
    max_y = max(coord[1] for coord in coords)
    
    # Create the closed profile (clockwise direction)
    profile = [
        (min_x, min_y),  # Top-left
        (max_x + 1, min_y),  # Top-right
        (max_x + 1, max_y + 1),  # Bottom-right
        (min_x, max_y + 1),  # Bottom-left
        (min_x, min_y)  # Back to top-left to close the profile
    ]
    
    return profile




# Define the factory layout size
layout_size = (7, 9)

# Define areas of rectangles (number of grids)
areas = [7, 4, 4, 6, 10, 4, 4, 6, 4]

# Define fixed positions for some rectangles (id: (area, (x, y)))
fixed_positions = {
    5: (10, (3, 3)),  # Fix rectangle 1 with area 6 at position (0, 0)
    2: (4, (0,0)),  # Fix rectangle 3 with area 4 at position (6, 0)
}

# Pack rectangles
packed_layout = pack_rectangles(layout_size, areas, fixed_positions)

# Parse the layout and get closed profiles
profiles = parse_layout_to_profiles(packed_layout)

# Print the results
print("\nClosed Profiles:")
for id, profile in profiles.items():
    print(f"Part {id}: {profile}")


# Visualize the layout
visualize_layout(packed_layout)





