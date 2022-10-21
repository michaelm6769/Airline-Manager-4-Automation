import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from datetime import datetime, timedelta
import logging


#Parameters

fuel_buy_price = 400
co2_buy_price = 120
AM4_URL = 'URL HERE'
#Random interval before script restarts (Minutes)
time_min = 15
time_max = 30
#Number of times to run (set to 'Y' for infinite)
runtime = 24
infinite = 'N'

#End of Parameters



#Log file config
logging.basicConfig(filename='AM4.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#Variable for while loop
count = 0
countinf = 0

while count < runtime or infinite == 'Y':


    #Loop and date/time variables
    loop_int = random.randint(time_min * 60, time_max * 60)


    if infinite == 'Y':
        countinf = countinf + 1
    else:
        count = count + 1


    #Logging break
    logging.info(f'=====================')
    logging.info(f'=====================')



    #Load webdrivers and login to site
    driver = webdriver.Firefox(executable_path="c:\webdrivers\geckodriver.exe")
    driver.get(AM4_URL)
    driver.minimize_window()



    #Fuel capacity and price DATA
    driver.get("https://www.airline4.net/fuel.php")
    price_f = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/span[2]/b').text
    holding_f = driver.find_element(By.XPATH, '//*[@id="holding"]').text
    capacity_f = driver.find_element(By.ID, 'remCapacity').text

        #Convert capacity into integer
    capacity_f = int(capacity_f.replace(',', ''))

        #Convert price into integer
    price_f = int(price_f.replace('$', '').replace(',', '').replace(' ', ''))
    print("Fuel Capacity:", capacity_f)
    print("Fuel Price:",price_f)
    time.sleep(0.5)



    #Co2 capacity and price DATA
    driver.get("https://www.airline4.net/co2.php")
    price_c = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/span[2]/b').text
    holding_c = driver.find_element(By.XPATH, '//*[@id="holding"]').text
    capacity_c = driver.find_element(By.ID, 'remCapacity').text

        #Convert capacity into integer
    capacity_c = int(capacity_c.replace(',', ''))

        #Convert price into integer
    price_c = int(price_c.replace('$', '').replace(',', '').replace(' ', ''))
    print("Co2 Capacity:", capacity_c)
    print("Co2 Price:",price_c)



    #Marketing DATA
    driver.get("https://www.airline4.net/marketing.php")
    pax_rep = int(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div').text)
    print("Pax Rep:", pax_rep)



    #Fuel Buy
    if price_f <= fuel_buy_price and capacity_f > 0:
        driver.get("https://www.airline4.net/fuel.php?mode=do&amount=" + str(capacity_f))
        print(capacity_f, "lbs Fuel Purchased for", "$", (capacity_f * price_f)/1000)
        logging.info(f'{capacity_f} lbs fuel purchased @ ${price_f}')

    else:
        print("Fuel not Purchased")

        if price_f > 400:
            print("--Too Expensive")

        if capacity_f == 0:
            print("--No Capacity")

    #Co2 Buy
    if price_c <= co2_buy_price and capacity_c > 0:
        driver.get("https://www.airline4.net/co2.php?mode=do&amount=" + str(capacity_c))
        print(capacity_c, "lbs Co2 Purchased for", "$", (capacity_c * price_c)/1000)
        logging.info(f'{capacity_c} Co2 quotas purchased @ ${price_c}')

    else:
        print("Co2 not Purchased")

        if price_f > 400:
            print("--Too Expensive")

        if capacity_f == 0:
            print("--No Capacity")


    def start_marketing_campaign(type, campaign, duration):
        campaign_map = {'type': {1: 'Airline', 2: 'Cargo', 5: 'Eco Friendly'},
                        'campaign': {1: '5-10%', 2: '10-18%', 3: '19-25%', 4: '25-35%'},
                        'duration': {1: '4', 2: '8', 3: '12', 4: '16', 5: '20', 6: '24'}}

        driver.get(
            f'https://www.airline4.net/marketing_new.php?type={type}&c={campaign}&mode=do&d={duration}')


    #Campaign Buy
    driver.get('https://www.airline4.net/marketing.php')
    campaign_table = driver.find_element(By.ID, 'active-campaigns')
    campaigns = campaign_table.find_elements(
            by=By.TAG_NAME, value='td')

    if len(campaigns) == 0:
        # start all campaigns
        start_marketing_campaign(1, 4, 3)
        start_marketing_campaign(5, 4, 3)
        print("All Campaigns Purchased")

    else:
        active_campaign = [campaign.text.strip()
                           for campaign in campaigns if campaign.text.strip() != '']

        if 'Airline reputation' not in active_campaign:
            # start airlines campaign
            start_marketing_campaign(1, 4, 3)
            print("Pax Campaign Purchased")

        if 'Eco friendly' not in active_campaign:
            # start aircraft campaign
            start_marketing_campaign(5, 4, 3)
            print("Eco Campaign Purchased")

        else:
            print("No Campaigns Purchased")


    #Depart Planes
    if pax_rep > 80:
        driver.get("https://www.airline4.net/route_depart.php?mode=all&ids=x")
        time.sleep(1)
        driver.get("https://www.airline4.net/route_depart.php?mode=all&ids=x")
        time.sleep(1)
        driver.get("https://www.airline4.net/route_depart.php?mode=all&ids=x")
        time.sleep(1)
        driver.get("https://www.airline4.net/route_depart.php?mode=all&ids=x")
        print("All Planes Departed")

    else:
        print("Planes not departed")
        print("--Low Reputation")


    #Print Balance
    driver.get('https://www.airline4.net/banking_account.php?id=0')
    balance = driver.find_element(By.XPATH, '/html/body/div[1]/div').text
    balance = balance.replace(" ", "")
    print(balance)


    #Closes window
    driver.close()


    #Logging
    logging.info(f'Fuel:{holding_f} lbs')
    logging.info(f'Co2:{holding_c} quotas')
    logging.info(f'Balance:{balance}')
    logging.info(f'Pax Rep:{pax_rep}')


    #Print time and time of next run
    minutes = round(loop_int/60)
    present_time = datetime.now()
    '{:%H:%M:%S}'.format(present_time)
    updated_time = datetime.now() + timedelta(minutes=minutes)
    print(updated_time)
    print(minutes, "Minutes till next run")
    print("Times Ran:", count + countinf)
    time.sleep(loop_int)
