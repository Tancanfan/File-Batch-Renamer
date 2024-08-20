import os
import re

# Define the directory for video files
directory = 'C:\\Users\\Tanca\\Videos\\Cobra Kai'

# Define pattern to match video files
required_substrings = ["Cobra", "Kai", r"S\d{2}E\d{2}"] # Using regex for S##E##

# Define a function to filter and rename files
def rename_files(directory):
    for subdir, _, files in os.walk(directory):
        for filename in files:
            # Extract the parts of the filename that match the required substrings
            matched_parts = []
            for substring in required_substrings:
                match = re.search(substring, filename)
                if match:
                    matched_parts.append(match.group(0)) # match.group(0) method returns the first group of matched strings
            
            # If all required substrings are found, create a new filename
            if len(matched_parts) == len(required_substrings):
                new_filename = ' '.join(matched_parts) + '.mkv'
                old_filepath = os.path.join(subdir, filename)
                new_filepath = os.path.join(subdir, new_filename)

                # Print debugging information
                print(f"Old Path: {old_filepath}")
                print(f"New Path: {new_filepath}")
            
                # Rename the file
                os.rename(old_filepath, new_filepath)
                print(f"Renamed: {filename} to {new_filename}")
            else:
                print(f"Skipping: {filename} (not all substrings found)")

rename_files(directory)