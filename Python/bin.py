import matplotlib.pyplot as plt
from rectpack import newPacker
import random
import numpy as np

def get_hardcoded_input():
    # Hardcoded input data: Room name, Width, Height, Priority
    return [
        {'Room': 'Office', 'Width': 10, 'Height': 8, 'Priority': 3},
        {'Room': 'Workshop', 'Width': 15, 'Height': 12, 'Priority': 2},
        {'Room': 'Storage', 'Width': 12, 'Height': 10, 'Priority': 1},
        {'Room': 'Cafeteria', 'Width': 10, 'Height': 6, 'Priority': 2},
        {'Room': 'Conference Room', 'Width': 8, 'Height': 6, 'Priority': 3},
        {'Room': 'Restroom', 'Width': 5, 'Height': 4, 'Priority': 2},
        {'Room': 'Server Room', 'Width': 4, 'Height': 6, 'Priority': 3},
        {'Room': 'Reception', 'Width': 6, 'Height': 5, 'Priority': 3},
    ]

def pack_rooms(rooms, factory_width, factory_height):
    # Sort rooms by priority (descending) and height (descending)
    sorted_rooms = sorted(rooms, key=lambda x: (-x['Priority'], -x['Height']))
    
    packed_rooms = []
    shelves = []
    
    for room in sorted_rooms:
        packed = False
        for shelf in shelves:
            if room['Width'] <= shelf['remaining_width'] and room['Height'] <= shelf['height']:
                x = factory_width - shelf['remaining_width']
                y = shelf['y']
                packed_rooms.append({
                    'Room': room['Room'],
                    'x': x,
                    'y': y,
                    'Width': room['Width'],
                    'Height': room['Height']
                })
                shelf['remaining_width'] -= room['Width']
                packed = True
                break
        
        if not packed:
            if factory_height - (len(shelves) * room['Height']) >= room['Height']:
                y = len(shelves) * room['Height']
                packed_rooms.append({
                    'Room': room['Room'],
                    'x': 0,
                    'y': y,
                    'Width': room['Width'],
                    'Height': room['Height']
                })
                shelves.append({
                    'y': y,
                    'height': room['Height'],
                    'remaining_width': factory_width - room['Width']
                })
            else:
                print(f"Warning: Not enough space to pack {room['Room']}")
    
    return packed_rooms


def pack_roomsold(rooms, factory_width, factory_height):
    packer = newPacker(rotation=True)  # Allow rotation for better packing
    
    # Sort rooms by priority (descending) and area (descending)
    sorted_rooms = sorted(rooms, key=lambda x: (-x['Priority'], -(x['Width'] * x['Height'])))
    
    # Add rectangles to packer
    for room in sorted_rooms:
        packer.add_rect(room['Width'], room['Height'], room['Room'])
    
    # Add bin (factory floor)
    packer.add_bin(factory_width, factory_height)
    
    # Pack rectangles
    packer.pack()
    
    return packer[0]

def visualize_layout(packed_rooms, factory_width, factory_height):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(packed_rooms)))
    
    for room, color in zip(packed_rooms, colors):
        x, y, w, h = room['x'], room['y'], room['Width'], room['Height']
        ax.add_patch(plt.Rectangle((x, y), w, h, fill=True, facecolor=color, edgecolor='black'))
        ax.text(x + w/2, y + h/2, room['Room'], ha='center', va='center', wrap=True)
    
    ax.set_xlim(0, factory_width)
    ax.set_ylim(0, factory_height)
    ax.set_aspect('equal')
    ax.set_title('Factory Layout')
    plt.tight_layout()
    plt.show()
    
def visualize_layoutold(packed_rooms, factory_width, factory_height):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(packed_rooms)))
    
    for rect, color in zip(packed_rooms, colors):
        x, y, w, h, room_name = rect.x, rect.y, rect.width, rect.height, rect.rid
        ax.add_patch(plt.Rectangle((x, y), w, h, fill=True, facecolor=color, edgecolor='black'))
        ax.text(x + w/2, y + h/2, room_name, ha='center', va='center', wrap=True)
    
    ax.set_xlim(0, factory_width)
    ax.set_ylim(0, factory_height)
    ax.set_aspect('equal')
    ax.set_title('Factory Layout')
    plt.tight_layout()
    plt.show()

def main():
    factory_width = 50  # Adjust as needed
    factory_height = 40  # Adjust as needed
    
    rooms = get_hardcoded_input()
    packed_rooms = pack_rooms(rooms, factory_width, factory_height)
    
    print("Room Coordinates:")
    for rect in packed_rooms:
        print(f"{rect['Room']}: ({rect['x']}, {rect['y']}), {rect['Width']}x{rect['Height']}")
        #print(f"{rect.rid}: ({rect.x}, {rect.y}), {rect.width}x{rect.height}")
    
    visualize_layout(packed_rooms, factory_width, factory_height)

if __name__ == "__main__":
    main()