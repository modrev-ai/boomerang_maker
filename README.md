# Boomerang Maker
Creates boomerang video from a source video file. Edit images and creates repeats of the source file in reverse `N` times.

<table style="border: none;">
    <tr>
        <td>
            <h3>Original</h3>
            <img src="img/output_video_1.5s.gif" alt="First GIF" style="max-width: 80%; border: none;">
        </td>
        <td>
            <h3>Boomerang</h3>
            <img src="img/output_video_0.8s_concat.gif" alt="Second GIF" style="max-width: 80%; border: none;">
        </td>
    </tr>
</table>

## Video Processing Script

This script processes a video file by cropping, reversing, and concatenating clips based on specified parameters.

## Requirements

- Python 3.x
- moviepy

You can install the required Python packages using pip:

```bash
pip install moviepy
```

## Usage
Run the script with the following command:

```bash
python video_processing.py <input_file> <output_file> [--start_time START_TIME] [--end_time END_TIME] [--x_offset X_OFFSET] [--y_offset Y_OFFSET] [--repetition REPETITION] [--playback_speed PLAYBACK_SPEED]
```

## Arguments
- `input_file`: Path to the input video file.
- `output_file`: Path to the output video file.
- `--start_time`: (Optional) Start time in seconds. Default is 0.
- `--end_time`: (Optional) End time in seconds. Default is 0.8.
- `--x_offset`: (Optional) X offset in pixels. Default is 200.
- `--y_offset`: (Optional) Y offset in pixels. Default is 100.
- `--repetition`: (Optional) Number of repetitions. Default is 2.
- `--playback_speed`: (Optional) Playback speed. Default is 0.8.

## Example
```bash
python video_processing.py whatsapp_hello_vid.mp4 output_video.mp4 --start_time 0 --end_time 0.8 --x_offset 200 --y_offset 100 --repetition 2 --playback_speed 0.8
```

This command will process the `whatsapp_hello_vid.mp4` video file and save the output to `output_video.mp4` with the specified parameters.