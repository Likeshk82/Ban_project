import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome(executable_path='path/to/chromedriver')
t='https://twitter.com/twitter_username'
def scrape_twitter_profile(url):
    d.get(url)
    time.sleep(3)  
    try:
        bio=d.find_element(By.XPATH, "//div[@data-testid='UserDescription']//span").text
        following_count=d.find_element(By.XPATH, "//a[@href='/twitter_username/following']//span[1]").text
        followers_count=d.find_element(By.XPATH, "//a[@href='/twitter_username/followers']//span[1]").text
        location=d.find_element(By.XPATH, "//div[@data-testid='UserProfileHeader_Items']//span").text
        website=d.find_element(By.XPATH, "//a[@data-testid='UserUrl']").get_attribute("href")
        data={'Bio': bio,'Following Count': following_count,'Followers Count': followers_count,'Location': location,'Website': website}
        return data
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
profile_data=scrape_twitter_profile(t)
if profile_data:
    df=pd.DataFrame([profile_data])
    df.to_csv('twitter_profile_data.csv', index=False)
    print("Data saved to 'twitter_profile_data.csv'")
else:
    print("Failed to retrieve profile data.")
d.quit()