# ReadTS

**Purpose.** Read and explore magnetotelluric (MT) time series through a MATLAB App, with fast navigation, plotting, and basic exports.

## Main features

- **Load one or multiple time series** from the following instruments:
  - Metronix Geophysics **ADU-07 / ADU-07e / ADU-08e** (`.ats`)
  - Phoenix Geophysics **MTU5 / MTU5-A** (`.tsh`, `.tsl`)
  - Phoenix Geophysics **MTU5 / MTU5-A / V8** (`.ts*`)
  - Phoenix Geophysics **MTU5-C / MTU8-A** (`.td*`)
  - **LEMI 417** (`.b*`, `.t*`)
  - **LEMI 420 / 424** (`.txt`)
  - **LEMI 423** (`.b423`)
  - **Zonge** (supported formats)
- **Visualize power spectrum** in **linear** or **logarithmic** scale.
- Switch between **frequency** and **period** views.
- **Custom time-series filtering:** low-pass, high-pass, notch.
- **Export figures** as `.fig` or `.png`.
- **Toggle visibility** of individual channels/series.
- Show **station location** (map panel).
- Show **metadata** (instrument, sampling rate, units, etc.).
- **Send current series to MATLAB Workspace.**
- **Save series** for future use or processing.

## Additional tools

For the **visible** (active) time series:
- Plot in **time domain** (time series) or **frequency domain** (power spectrum).
- Display **calibrated data** in **field units**.
- Show **spectrograms** of the active series.

## Main GUI components

- <img src="../_static/icons/numeric_slider.svg" class="icon" alt="Navigation"> **Time navigation (slider)**  
  Jump to any time within the full duration of your time series.

- <img src="../_static/icons/button.svg" class="icon" alt="Previous"> **Previous (button)**  
  Move to the previous chunk/time window.

- <img src="../_static/icons/button.svg" class="icon" alt="Next"> **Next (button)**  
  Move to the next chunk/time window.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Start time"> **Start time (edit field)**  
  Jump directly to a typed timestamp.

- <img src="../_static/icons/drop_down.svg" class="icon" alt="Window units"> **Window units (drop-down)**  
  Set the viewing window in **seconds / minutes / hours / days**.

- <img src="../_static/icons/spinner.svg" class="icon" alt="Window length"> **Window length (spinner)**  
  Increase or decrease the window length using the selected units.

## Quick start (step-by-step)

1. **Open** the app: MATLAB → **APPS → FFMT → ReadTS**.
2. **Load data:** click **Load** and select one or more files (supported formats above).
3. **Navigate:** use the **slider**, **Previous**, **Next**, or type a **Start time**.
4. **View mode:** choose **Time series**, **Power spectrum** (linear/log), or **Spectrogram**.
5. **Filter (optional):** apply **LP / HP / Notch** and re-plot.
6. **Export:** save figures as **.fig / .png**, or **send** the series to **Workspace**.

```{note}
If a file does not load, verify the instrument format and sampling rate,
and check that you have read permissions in the selected directory.
