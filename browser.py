import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlencode
import random
import time

def get_options():
    options = uc.ChromeOptions()
    options.add_argument('--host-resolver-rules=MAP duckduckgo.com 52.149.246.39')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--metrics-recording-only")
    options.add_argument("--mute-audio")
    options.add_argument("--no-first-run")
    options.add_argument("--password-store=basic")
    options.add_argument("--use-mock-keychain")
    options.add_argument("--lang=en-US,en")
    options.add_argument("--window-size=1280,800")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36".format(
        f"{random.randint(100, 120)}.0.{random.randint(4000, 5000)}.{random.randint(100, 200)}"
    )
    options.add_argument(f"user-agent={user_agent}")
    return options

def google_queries(queries):
    res = []
    try:
        driver = uc.Chrome(options=get_options(), headless=False, version_main=138)
        wait = WebDriverWait(driver, 30)
    except:
        return []

    for query in queries:
        q = urlencode({'q': query})
        try:
            driver.get(f'https://www.google.com/search?client=chrome&{q}&udm=14&filter=0')
        except:
            driver.quit()
            return []
        page_count = 0
        while page_count < 5:
            try:
                results = wait.until(EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, 'MjjYud')
                ))
                for block in results:
                    try:
                        title_elem = block.find_element(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")
                        link_elem = block.find_element(By.CSS_SELECTOR, "a[jsname='UWckNb']")
                        desc_elem = block.find_element(By.CSS_SELECTOR, "div.VwiC3b")
                        res.append([title_elem.text.strip(), link_elem.get_attribute("href"), desc_elem.text.strip()])
                    except:
                        continue
            except:
                break

            page_count += 1
            try:
                next_button = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.ID, "pnnext"))
                )
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(2)
            except:
                break

    driver.quit()
    return res


def bing_queries(queries):
    res = []
    try:
        driver = uc.Chrome(options=get_options(), headless=False, version_main=138)
        wait = WebDriverWait(driver, 30)
    except:
        return []

    for query in queries:
        q = urlencode({'q': query})
        try:
            driver.get(f'https://www.bing.com/search?{q}')
        except:
            driver.quit()
            return []

        page_count = 0
        while page_count < 5:
            try:
                result_blocks = wait.until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.b_algo'))
                )
                for block in result_blocks:
                    try:
                        title_elem = block.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
                        desc_elem = block.find_element(By.CLASS_NAME, "b_caption")
                        res.append([title_elem.text.strip(), title_elem.get_attribute("href"), desc_elem.text.strip()])
                    except:
                        continue
            except:
                break

            page_count += 1
            try:
                next_button = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "a.sb_pagN"))
                )
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(2)
            except:
                break

    driver.quit()
    return res


def duckduckgo_queries(queries):
    res = []
    try:
        driver = uc.Chrome(options=get_options(), headless=False, version_main=138)
        wait = WebDriverWait(driver, 15)
    except:
        return []

    for query in queries:
        q = urlencode({'q': query})
        try:
            driver.get(f'https://duckduckgo.com/?t=h_&{q}&ia=web')
        except:
            driver.quit()
            return []

        click_count = 0
        while click_count < 5:
            try:
                result_blocks = wait.until(EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'article[data-testid="result"]')
                ))
                for block in result_blocks[len(res):]:
                    try:
                        title_elem = block.find_element(By.CSS_SELECTOR, 'h2 a[data-testid="result-title-a"]')
                        desc_elem = block.find_element(By.CSS_SELECTOR, 'div[data-result="snippet"]')
                        res.append([title_elem.text.strip(), title_elem.get_attribute("href"), desc_elem.text.strip()])
                    except:
                        continue
            except:
                break

            click_count += 1
            try:
                more_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.ID, "more-results"))
                )
                driver.execute_script("arguments[0].click();", more_button)
                time.sleep(2)
            except:
                break

    driver.quit()
    return res


def yahoo_queries(queries):
    res = []
    try:
        driver = uc.Chrome(options=get_options(), headless=False, version_main=138)
        wait = WebDriverWait(driver, 15)
    except:
        return []

    for query in queries:
        q = urlencode({'q': query})
        try:
            driver.get(f'https://search.yahoo.com/search?{q}')
        except:
            driver.quit()
            return []

        page_count = 0
        while page_count < 5:
            try:
                result_blocks = wait.until(EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'li div.dd.algo')
                ))
                for block in result_blocks:
                    try:
                        title_elem = block.find_element(By.CSS_SELECTOR, 'h3.title > span')
                        link_elem = block.find_element(By.CSS_SELECTOR, 'a')
                        desc_elem = block.find_element(By.CSS_SELECTOR, 'div.compText p')
                        res.append([title_elem.text.strip(), link_elem.get_attribute("href"), desc_elem.text.strip()])
                    except:
                        continue
            except:
                break

            page_count += 1
            try:
                next_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.next"))
                )
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(2)
            except:
                break

    driver.quit()
    return res


def scribd_queries(queries):
    res = []
    try:
        driver = uc.Chrome(options=get_options(), headless=False, version_main=138)
        wait = WebDriverWait(driver, 15)
    except:
        return []

    for query in queries:
        q = urlencode({'query': query})
        try:
            driver.get(f'https://www.scribd.com/search?{q}')
        except:
            driver.quit()
            return []

        page_count = 0
        while page_count < 5:
            try:
                result_blocks = wait.until(EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'ul[data-e2e="ugc-search-results"] > li article')
                ))
                for block in result_blocks:
                    try:
                        title_elem = block.find_element(By.CSS_SELECTOR, 'h3[data-e2e="title"]')
                        link_elem = block.find_element(By.CSS_SELECTOR, 'a.ListItem-module_linkOverlay__H60l3')
                        desc_elem = block.find_element(By.CSS_SELECTOR, 'div.Document-module_authorDateCategories__8dnW3')
                        res.append([title_elem.text.strip(), link_elem.get_attribute("href"), desc_elem.text.strip()])
                    except:
                        continue
            except:
                break

            page_count += 1
            try:
                next_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="next"]'))
                )
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(2)
            except:
                break

    driver.quit()
    return res


def brave_queries(queries):
    res = []
    try:
        driver = uc.Chrome(options=get_options(), headless=False, version_main=138)
        wait = WebDriverWait(driver, 15)
    except:
        return []

    for query in queries:
        q = urlencode({'q': query})
        try:
            driver.get(f'https://search.brave.com/search?{q}&source=web')
        except:
            driver.quit()
            return []

        page_count = 0
        while page_count < 5:
            try:
                result_blocks = wait.until(EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, '.snippet.svelte-1o29vmf')
                ))
                for block in result_blocks:
                    try:
                        link_elem = block.find_element(By.CSS_SELECTOR, 'a.heading-serpresult')
                        desc_elem = block.find_element(By.CSS_SELECTOR, '.snippet-description')
                        res.append([link_elem.get_attribute("title") or link_elem.text.strip(), link_elem.get_attribute("href"), desc_elem.text.strip()])
                    except:
                        continue
            except:
                break

            page_count += 1
            try:
                next_link_elem = driver.find_element(
                    By.XPATH, "//a[normalize-space()='Next' and @role='link']"
                )
                next_href = next_link_elem.get_attribute("href")
                if not next_href:
                    break
                driver.get(next_href)
                time.sleep(2)
            except:
                break

    driver.quit()
    return res
