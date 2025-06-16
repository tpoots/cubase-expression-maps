import os
import xml.etree.ElementTree as ET
import argparse

# Key, MIDI Value,  Name, 
# C-2,    0, Long
# C#-2,   1, Legato,
# D-2,    2, Marcato
# D#-2,   3, Tremolo
# E-2,    4, Spiccato
# F-2,    5, Staccato
# F#-2,   6, Short/Tenuto
# G-2,    7, Pizzicato
# G#-2,   8, Trill min
# A-2,    9, Trill Maj

# Map of MIDI values to their corresponding names as lists
MIDI_TO_NAME = {
    0: {
        "names": ["Long"],
        "exclusions": ["Marcato", "Marc", "Detache", "Det", "Portato", "Tenuto"]
    },
    1: {
        "names": ["Legato", "Leg.", "Leg"],
        "exclusions": ["Marcato", "Marc", "Detache", "Det", "Portato", "Tenuto"]
    },
    2: {
        "names": ["Marcato", "Long Marcato", "Marc.", "Marc"],
        "exclusions": []
    },
    3: {
        "names": ["Tremolo", "Trem", "Trems", "Fluttertongue", "Flutter"],
        "exclusions": []
    },
    4: {
        "names": ["Spiccato", "Spic", "Spicc"],
        "exclusions": []
    },
    5: {
        "names": ["Staccato", "Stac", "Stacc"],
        "exclusions": []
    },
    6: {
        "names": ["Detache", "Tenuto", "Short", "Portato"],
        "exclusions": []
    },
    7: {
        "names": ["Pizzicato", "Pizz"],
        "exclusions": []
    },
    8: {
        "names": ["Trill HT", "Trill min2"],
        "exclusions": []
    },
    9: {
        "names": ["Trill WT", "Trill Maj2"],
        "exclusions": []
    }
}

# List of all valid names for validation
VALID_NAMES = [name for data in MIDI_TO_NAME.values() for name in data['names']]

def name_to_data1(slot_name):
    slot_name_lower = slot_name.lower()
    for midi_value, data in MIDI_TO_NAME.items():
        if any(slot_name_lower.startswith(name.lower()) for name in data['names']):
            return midi_value
    return None

def process_expressionmap_file(filepath, reset, dry_run):
    tree = ET.parse(filepath)
    root = tree.getroot()
    changed = False
    # Dictionary to track found articulations
    found_articulations = {midi_value: False for midi_value in MIDI_TO_NAME.keys()}
    print("-" * 80)

    done_reset = False
    if reset:
        for psoundslot in root.findall(".//obj[@class='PSoundSlot']"):
            name_member = psoundslot.find("./member[@name='name']/string[@name='s']")
            slot_name = name_member.get('value') if name_member is not None else None
            trigger = psoundslot.find("./obj[@class='PSlotThruTrigger']")

            if trigger is not None:
                data1 = trigger.find("./int[@name='data1']")
                new_value = -1
                if not dry_run:
                    print(f"Resetting {slot_name}: {new_value}")
                    data1.set('value', '-1')
                    changed = True
    else:
        # Find all PSoundSlot objects
        for psoundslot in root.findall(".//obj[@class='PSoundSlot']"):
            # Find the slot name
            name_member = psoundslot.find("./member[@name='name']/string[@name='s']")
            slot_name = name_member.get('value') if name_member is not None else None
            instrument_name = filepath.split('/')[-1].split('.expressionmap')[0]
            print(f"{instrument_name}: slot_name: {slot_name}")

            if slot_name:
                # Find the PSlotThruTrigger in this slot
                trigger = psoundslot.find("./obj[@class='PSlotThruTrigger']")
                match_found = False
                if trigger is not None:
                    data1 = trigger.find("./int[@name='data1']")
                    # Check if slot_name matches any values in MIDI_TO_NAME (case insensitive)
                    slot_name_lower = slot_name.lower()
                    for midi_value, data in MIDI_TO_NAME.items():
                        matching_name = next((name for name in data['names'] if slot_name_lower.startswith(name.lower())), None)
                        exclude = any(exclusion.lower() in slot_name_lower for exclusion in data['exclusions'])
                        if matching_name and not exclude:
                            match_found = True
                            print(f"Found {matching_name} in {slot_name}")
                            if not found_articulations[midi_value]:
                                print(f"Found substring match: {slot_name} -> MIDI value {midi_value}")
                                found_articulations[midi_value] = True
                                if data1.get('value') != str(midi_value):
                                    if not dry_run:
                                        print(f"Setting {instrument_name}: {slot_name} data1 {data1.get('value')} -> {midi_value}")
                                        data1.set('value', str(midi_value))
                                        changed = True
                                break
                            else:
                                print(f"Found duplicate substring match: {slot_name}")
                                new_value = -1
                                if data1.get('value') != '-1':
                                    if not dry_run:
                                        print(f"Setting dupe {instrument_name}: {slot_name} data1 {data1.get('value')} -> {new_value}")
                                        data1.set('value', '-1')
                                        changed = True
                    if not match_found:
                        new_value = -1
                        if data1.get('value') != str(new_value):
                            if not dry_run:
                                print(f"Setting {instrument_name}: {slot_name} data1 {data1.get('value')} -> {new_value}")
                                data1.set('value', '-1')
                                changed = True

    if changed:
        # Backup original
        os.rename(filepath, filepath + ".bak")
        tree.write(filepath, encoding="utf-8", xml_declaration=True)
        print("-" * 80)

def process_directory(directory, reset, prefixes, dry_run):
    for root_dir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".expressionmap.xml") and (not prefixes or any(file.startswith(prefix) for prefix in prefixes)):
                process_expressionmap_file(os.path.join(root_dir, file), reset, dry_run)
                print(os.path.join(root_dir, file), reset)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze and modify Cubase Expression Map files.")
    parser.add_argument('--reset', action='store_true', help='Set all data1 values to -1, then set first non-empty slot to 0')
    parser.add_argument('--directory', type=str, default='VSL Template v10', help='Directory to process')
    parser.add_argument('--prefixes', type=str, nargs='+', help='List of filename prefixes to process')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without making changes')
    args = parser.parse_args()

    if not hasattr(args, 'reset'):
        args.reset = False
    if not hasattr(args, 'directory'):
        args.directory = 'VSL Template v10'
    if not hasattr(args, 'prefixes'):
        args.prefixes = []
    if not hasattr(args, 'dry_run'):
        args.dry_run = True
    # Use args.reset as a boolean flag in your logic
    if args.reset:
        print("Reset mode enabled!")
    else:
        print("Normal mode.")

    print(f"Valid names: {VALID_NAMES}")

    process_directory(args.directory, args.reset, args.prefixes, args.dry_run)