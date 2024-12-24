import os
import whisper

# Load the Whisper model
model = whisper.load_model("medium")  # Choose model size: tiny, base, small, medium, large

# Define input and output directories
input_folder = "/home/meow/projects/asr/emscall_whisper-20241224T134244Z-001/emscall_whisper"  # Replace with your input folder path
output_folder = "/home/meow/projects/asr/output_emscall_whisper_medium"  # Replace with your output folder path

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each WAV file in the input directory
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

        # Transcribe audio using Whisper
        result = model.transcribe(input_path, language="en")  # Set language to English

        # Save transcription to a text file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"Processed file: {filename}")
