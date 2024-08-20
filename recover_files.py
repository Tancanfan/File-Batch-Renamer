import os

# Define the directory for video files
directory = 'C:\\Users\\Tanca\\Videos\\Cobra Kai'

def recover_files(directory):
    for subdir, _, files in os.walk(directory):
        for filename in files:
            # Example pattern to identify files that were renamed incorrectly
            if ' ' in filename and filename.endswith('.mkv'):
                # Extract the original name (this is a placeholder, adjust according to your needs)
                original_filename = filename.replace(' ', '_') # Example adjustment
                old_filepath = os.path.join(subdir, filename)
                new_filepath = os.path.join(subdir, original_filename)
                
                # Move files back
                os.rename(old_filepath, new_filepath)
                print(f"Recovered: {filename} to {original_filename}")

# Run the recovery function
recover_files(directory)