# PSP Nest: Energy Optimization For Ameren Power Smart Pricing Users

## Overview
PSP Nest is a project aimed at optimizing energy consumption and saving money by dynamically adjusting Google Nest settings based on real-time electricity prices. This program utilizes Google Smart Device Management (SDM) API to synchronize your Nest devices with fluctuating energy costs, ensuring you make energy-efficient decisions and reduce your electricity bills.

## Features
### Automated Nest Adjustments
Automatically adjusts your Google Nest settings to optimize energy usage during high-price periods.
### Customization
Allows users to set preferences and priorities for energy conservation and cost savings.

## How It Works
### Data Collection
A parser will collect Ameren Power Smart Pricing data and make it avalible through API. For more detail see https://github.com/wenshanxiong/psp-parser
### Analysis
High-price periods will be determine by the standard deviation of hourly prices.
### Nest Adjustment
During high-price periods, Nest devices are adjusted to conserve energy. For example, adjusting thermostat temperatures, managing lighting, and controlling smart appliances.
### User Preferences
Users can customize preferences and override automated settings through setting.

## Installation
Create virtual environment (optional but recommanded)
```
python3 -m venv venv
source venv/bin/activate
```
Install libraries
```
pip install -r requirements.txt
```

## Usage
TODO

## Contributing
We welcome contributions from the community! If you have ideas for improvements, feature requests, or find any issues, please open an issue or submit a pull request.