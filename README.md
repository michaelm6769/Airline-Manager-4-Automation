# Airline-Manager-4-Automation
 Simple automations for airline manager 4

# Getting Started
This is just a python script to automate certain aspects of AM4. It is my first python project and has a long ways to go before it is complete. The script can autobuy fuel and co2 and auto departs on a random interval. All parameters can be easily adjusted to your liking. Requires selenium and webdriver. The script is set up to use geckodriver and firefox right now.

Install Steps
1. Install Selenium
```
pip install selenium
```
2. Install latest version of webdriver and firefox
```
https://github.com/mozilla/geckodriver/releases
```
```
https://www.mozilla.org/en-US/firefox/developer/
```
3. Create new folder in C:\ Drive named ```webdrivers``` and move geckodriver.exe to it
3. Download the python script and open in a text editor or IDE
4. Adjust parameters to your liking (Lines 11-16)

# How to get AM4_URL
1. Go to help tab on AM4
2. Open any topic
3. Right click on any players name and click copy link address
- if on ios or android, hold on player name![AM4 URL](https://user-images.githubusercontent.com/116333746/197123312-216bdf22-5ac9-4c68-891f-5fde026b44e5.png)

5. Paste link into quotes on AM4_URL parameter

# Future Updates
1. A-Checks and maintenance automated
2. List income from departures
3. Depart based on demand instead of departing all every time
4. Buy and route planes and configure seating and ticket pricing
5. GUI for data and log file
6. Fuel and Co2 graphs
