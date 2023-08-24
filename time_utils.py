import re

def vtt_time_to_seconds(time_str):
    """Converts VTT time format (HH:MM:SS.mmm) to seconds."""
    hours, minutes, rest = time_str.split(":")
    seconds, milliseconds = rest.split(".")
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000


def seconds_to_vtt_time(seconds):
    """Convert seconds to VTT time format (hh:mm:ss.ms)."""
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds %= 60
    return "{:02}:{:02}:{:02}.{:03}".format(hours, minutes, int(seconds), int((seconds % 1) * 1000))
