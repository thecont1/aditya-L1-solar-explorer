# SoLEXS Solar Flare Explorer

## TL;DR

Aditya-L1 is a solar observatory positioned 1.5 million kilometers from Earth at a place called the Lagrangian point L1, providing a continuous view of the Sun. SoLEXS is a spectrometer aboard Aditya-L1 that monitors X-ray emissions from the Sun, every second. This data is valuable for studying solar flares, which are bursts of energy released by the Sun. Now start exploring solar flares by forking the jupyter notebook: [`sun-explorer.ipynb`](sun-explorer.ipynb)

<div style="padding: 30px; font-size: 16px; line-height: 1.5; width: 600px">
<p>🛰️ 🛰️ 🛰️ 🛰️ 🛰️ 🛰️ 🛰️ 🛰️ 🛰️ 🛰️ <br><br> 🌞 A photon emitted on the surface of the Sun takes ≈494 seconds to reach Aditya-L1. Thereafter, the data generated and collected within SoLEXS is transmitted to ISSDC in Bengaluru – **a journey of ≈1.5 million Km in about 5 seconds** – where it is processed and made available to researchers. Are we truly privileged or what?! 😇</p>
<img src="image3-orbit.jpg" style="padding: 20px; width: 500px; height: 335px;" alt="Aditya-L1 in position within the Sun-Earth system.">



## Introduction

*Hello, my name is Mahesh Shantaram. I am not an astronomer or even specially qualified in physics beyond a Bachelors degree. But I look 😎 at the sun every day and I wonder, I wonder, I wonder...*

<div style="display: flex; padding-top: 20px; padding-bottom: 20px;">
  <img src="image1-launch.jpg" style="height: 650px;" alt="A rocket carrying Aditya-L1 is launched from ISRO's Satish Dhawan Space Centre in Sriharikota, Andhra Pradesh.">
  <img src="image2-trajectory.png" style="padding-top: 80px; height: 650px;" alt="Trajectory to L1">
</div>

### **Aditya-L1 and a faraway place we call L1**

* On **September 2, 2023, 11:20 IST**, [ISRO](https://www.isro.gov.in/) launched [Aditya-L1](https://www.issdc.gov.in/adityal1.html), a space-based observatory-class mission to study the Sun.

* The satellite attained orbital insertion at [Lagrange Point 1](https://in.mashable.com/science/78263/isros-aditya-l1-completes-first-orbit-at-lagrange-point-1-what-is-it) (L1), ~1.5 million kilometers from Earth, on **January 6, 2024, 4:17 PM IST**, marking a significant milestone for India's first solar observatory.

* The advantage of being perched (in a halo orbit) at L1 is that Aditya-L1 has secured for itself an astronomical seat with a forever uninterrupted view of the Sun.

### **The Source of Our Data**

* The spacecraft carries seven payloads to observe the photosphere, chromosphere and the corona of the Sun. As far as this notebook is concerned, we will focus our attention on the **Solar Low Energy X-ray Spectrometer (SoLEXS)**, a sun-as-a-star spectrometer developed by the *U.R. Rao Satellite Centre, Bengaluru*.

* The primary science objectives of SoLEXS are:
  * [Flares and Coronal Heating](https://pubs.aip.org/physicstoday/article/76/4/34/2879433/Unveiling-the-mystery-of-solar-coronal)
  * [Coronal Abundances and FIP](https://link.springer.com/article/10.1007/s11207-020-01738-5)
  * [Flare – CME studies](https://www.sciencedirect.com/science/article/pii/S2090997712000235)

### **Getting to Know That Data**

* Solar flares are classified on a scale of A, B, C, M and X. Each class is 10 times stronger than the last, with X-class flares being the most powerful

* SoLEXS is capable of covering an extensive dynamic range from A-class to X-class flares. As we will see in the plots, when the Sun flares, the intensity of X-Ray counts can be several standard deviations above the mean.

* Data transmissions started soon after Aditya-L1 reached its destination and its instruments gradually came online. However, the dataset published by ISRO begins from July 1, 2024 onwards.

* ISRO releases data in tranches. The first tranche of solar datasets was released on January 6, 2025, marking the one-year anniversary of Aditya-L1's arrival at L1.

* SoLEXS data is hosted by ISRO's *Indian Space Science Data Centre* (ISSDC) on the [PRADAN portal](https://pradan1.issdc.gov.in/al1/), where one can access it after a quick registration process.

* The FITS (Flexible Image Transport System) is the data format of choice for astroniomical data. SoLEXS data files are provided as gzip compressed FITS files.


## Features

- *Efficient Data Processing*: Reads compressed FITS files directly from ZIP archives with optimized I/O operations. Ingest data at blazing speeds 🚀

- *Intelligent Data Management*: Reads data from multiple directories via a config file. Stores processed data in a `parquet` file for fast access 🚀

- *Robust Error Handling*: Includes smart caching and validation to handle data inconsistencies, ensuring reliable results even with large or incomplete datasets.

- *Automated Flare Detection*: Identifies solar flares using configurable window parameters and annotates them on a line plot 🚀

- *Interactive Analysis*: Provides widget-based date/time selection and parameter adjustment for rapid, fuss-free solar flare analysis 🚀

- *Dynamic Visualizations*: Offers real-time, interactive plots like light curves and zoomed-in flare details, providing clear insights into solar activity with smooth user-controlled refreshes.


## Installation (Simplified for Beginners)

Don't worry if you're new to this—installing and running the Solar Flare Analyzer is easy! Just follow these steps to get started.

### Step 1: Clone the Repository

Download the project files using this command in your terminal (or command prompt on Windows). If you don't have Git, you can download the ZIP from GitHub and unzip it:

```bash
git clone https://github.com/thecont1/aditya-L1-solar-explorer.git
```

### Step 2: Create a Virtual Environment (Optional but Helpful)

This step keeps everything organized and prevents issues with other programs. Run these commands in your terminal:

* Create the environment: `python -m venv env`
* Activate it:
  * On Windows: `env\Scripts\activate`
  * On macOS/Linux: `source env/bin/activate`

### Step 3: Install the Required Tools

Install the necessary packages with one simple command. Make sure your virtual environment is activated if you created one:

```bash
pip install numpy pandas matplotlib astropy tqdm ipywidgets jupyter-ui-poll ipydatetime
```

### Step 4: Set Up Interactive Features (If Needed)

To make the interface work smoothly, enable Jupyter widgets with this command:

```bash
jupyter nbextension enable --py widgetsnbextension
```

### Step 5: Launch the Analyzer

Open the notebook in Jupyter to start exploring solar flares:

```bash
jupyter notebook
```
Then, find and open `sun-explorer.ipynb` in your browser.

You're all set! If you run into any issues, check the troubleshooting section or let us know.


## Usage

1. **Data Setup**:
   * Place your Aditya-L1 SoLEXS ZIP files in a directory
   * Create a `SoLEXS_dataset.paths` file listing the directories containing your data

2. **Run the Notebook**:
   * Open `sun-explorer.ipynb` in Jupyter
   * Run all cells to load data and initialize the interface

3. **Analyze Solar Flares**:
   * Use the date/time selectors to choose a time range
   * Adjust the sigma threshold to control flare detection sensitivity
   * Modify the gap parameter to distinguish between separate flare events
   * Set the zoom window to control the detail view of detected flares


## Data Format

The tool expects Aditya-L1 SoLEXS data in ZIP files with the following structure:

```text
AL1_SLX_L1_YYYYMMDD_v1.0.zip
└── AL1_SLX_L1_YYYYMMDD_v1.0/
    └── SDD2/
        └── AL1_SOLEXS_YYYYMMDD_SDD2_L1.lc.gz
```

The processed data is stored in a Parquet file (`SoLEXS_dataset.parquet`) with the following columns:

* `DATE`: Observation date
* `TIME`: Seconds since midnight
* `COUNTS`: X-ray counts

## Acknowledgements

* Indian Space Research Organisation (ISRO) for the Aditya-L1 mission and data
* The scientific teams behind the SoLEXS instrument

## License

This project is licensed under the MIT License - see the LICENSE file for details.