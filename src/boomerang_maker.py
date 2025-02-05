from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop, time_mirror
from moviepy.editor import concatenate_videoclips, vfx
import argparse


def process_video(
    input_file,
    output_file,
    start_time,
    end_time,
    x_offset,
    y_offset,
    repetition,
    playback_speed,
):
    all_clips = []
    video = VideoFileClip(input_file)

    cut_video = video.subclip(start_time, end_time)
    x_length = cut_video.size[0] - x_offset
    y_length = cut_video.size[1] - y_offset

    cropped_video = crop(cut_video, x2=x_length, y2=y_length)
    cropped_video = cropped_video.fx(vfx.speedx, playback_speed)

    reversed_video = time_mirror(cropped_video)

    for i in range(repetition):
        all_clips += [cropped_video, reversed_video]

    final_video = concatenate_videoclips(all_clips)
    final_video.write_videofile(
        output_file,
        codec="libx264",
        preset="ultrafast",
        ffmpeg_params=[
            "-q:v",
            "0",
            "-vf",
            f"scale={y_length}:{x_length}",  # may want to adjust the scale based on your video
        ],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a video file with specified parameters.",
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input video file.",
    )
    parser.add_argument(
        "output_file",
        type=str,
        help="Path to the output video file.",
    )
    parser.add_argument(
        "--start_time",
        type=float,
        default=0,
        help="Start time in seconds.",
    )
    parser.add_argument(
        "--end_time",
        type=float,
        default=0.8,
        help="End time in seconds.",
    )
    parser.add_argument(
        "--x_offset",
        type=int,
        default=200,
        help="X offset in pixels.",
    )
    parser.add_argument(
        "--y_offset",
        type=int,
        default=100,
        help="Y offset in pixels.",
    )
    parser.add_argument(
        "--repetition",
        type=int,
        default=2,
        help="Number of repetitions.",
    )
    parser.add_argument(
        "--playback_speed",
        type=float,
        default=0.8,
        help="Playback speed.",
    )

    args = parser.parse_args()

    process_video(
        args.input_file,
        args.output_file,
        args.start_time,
        args.end_time,
        args.x_offset,
        args.y_offset,
        args.repetition,
        args.playback_speed,
    )
