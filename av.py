"""
Minimal stub for PyAV to satisfy `import av` when we don't decode files.
Our pipeline feeds raw PCM via ffmpeg TCP, so this module should never be used.
If you later install real PyAV, delete this file.
"""
def open(*args, **kwargs):
    raise RuntimeError("PyAV not installed; this setup expects raw PCM via ffmpeg, not file decoding.")
