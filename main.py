import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/MacBook-Apple-Memory-256GB-Space/dp/B08PNQTYV2/ref=sr_1_1?crid=11WYR5LQNRYW8&dib=eyJ2IjoiMSJ9.HCRa0IJexEMLZXC_oOtl5xOyszQK5Bt0n4NBgmYyUGbqPTDs2jfhUQYZnLqJiuVanSchluCOaoZUxBaZELU7rBXxFoa-3dMe7UIA1C85KoU8hVE4ANAN2ymbjuggIXLKh07HKVIwVVynWYXxmuoj282Fm3kuQT9Ixcyh9hdJJjapMPxo_CiuxS46nsmfJpyGqFPJFa3IRnYg-6mq-vw1-afTsZ7C5qgj1yMW6_2MZXQ.B12eeGG_STANjOKWg5Cxw9uuAuOEWi0Hv7CxuDuIqSU&dib_tag=se&keywords=macbook&qid=1708860527&sprefix=macbo%2Caps%2C216&sr=8-1&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,sv-SE;q=0.8,sv;q=0.7"
}

BUYPRICE = 600

response = requests.get(url, headers=header)


soup = BeautifulSoup(response.content, "lxml")

#print(soup)
getPrice = soup.find(class_="a-offscreen").getText()

formatPrice = getPrice[1:]
formatPrice = float(formatPrice)

print(formatPrice)

if(formatPrice <= BUYPRICE):
    print("EMAIL SENT, TIME TO BUY")
    email = "YOUR EMAIL"
    APP_PASSWORD = "YOUR APP PASSWORD"
    message = "TIME TO BUY" + url

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, APP_PASSWORD)

    server.sendmail(email, email, message)

