from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import time
from datetime import datetime

# Constants
TARGET_VOLUME = 100  # Set this to your desired volume level (0-100)

def get_microphone_volume():
    """Get the current system microphone volume level (scaled to 0-100)."""
    devices = AudioUtilities.GetMicrophone()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume.GetMasterVolumeLevelScalar() * 100

def set_microphone_volume(target_volume):
    """Set the system microphone volume to the specified level (0-100)."""
    devices = AudioUtilities.GetMicrophone()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(target_volume / 100, None)

def get_timestamp():
    """Get the current timestamp in a readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    print(f"[{get_timestamp()}] Monitoring system microphone volume changes...")
    print(f"[{get_timestamp()}] Target microphone volume: {TARGET_VOLUME}%")

    try:
        while True:
            current_volume = get_microphone_volume()

            # If the volume has changed, force it back to the target volume
            if abs(current_volume - TARGET_VOLUME) > 1:  # Allow a small tolerance
                print(f"[{get_timestamp()}] Microphone volume changed! Current volume: {current_volume:.2f}%")
                print(f"[{get_timestamp()}] Resetting microphone volume to {TARGET_VOLUME}%...")
                set_microphone_volume(TARGET_VOLUME)

            time.sleep(1)  # Check every second

    except KeyboardInterrupt:
        print(f"[{get_timestamp()}] Stopping...")

if __name__ == "__main__":
    main()