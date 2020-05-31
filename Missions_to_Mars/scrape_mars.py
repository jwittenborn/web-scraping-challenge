def scrape():

    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    import time

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    time.sleep(2)

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    title = soup.find('div',class_='content_title').text
    print(title)

    # Mars now
    paragraph=soup.find('div',class_='article_teaser_body').text
    print(paragraph)



    #JPL
    print("JPL page")
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    jplNasa_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jplNasa_url)
    time.sleep(2)

    JPL_html = browser.html
    # Parse HTML with Beautiful Soup
    JPL_soup = bs(JPL_html, 'html.parser')

    carousel_item =  JPL_soup.find('article', class_='carousel_item')
    print(carousel_item.prettify())

    style = carousel_item["style"]

    split_style = style.split("'")
    print(split_style[1])

    featured_image_url = 'https://www.jpl.nasa.gov' + split_style[1]
    print(featured_image_url)

    browser.quit()

    # Mars Weather
    mars_weather = "weather text goes here"
    print(mars_weather)

    # Mars facts
    print("Mars facts")
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    facts_url = 'http://space-facts.com/mars/'
    browser.visit(facts_url)
    time.sleep(2)

    # Visit the Mars Facts webpage
    mars_facts='https://space-facts.com/mars/'
    mars_fact_table=pd.read_html(mars_facts)

    #Create Dataframe to store table data
    df = mars_fact_table[0]
    df
    df.columns = ['0', '1']

    html_table = df.to_html()
    print(html_table)

    browser.quit()

    # Mars hemispheres
    print("Mars hemispheres")
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    hemisphere_image_urls = []

    hemis_titles = soup.find_all('h3')

    for i in range(len(hemis_titles)):
        hemis_title = hemis_titles[i].text
        print(hemis_title)
        
        hemis_images = browser.find_by_tag('h3')
        hemis_images[i].click()
        
        html = browser.html
        soup = bs(html, 'html.parser')
    
        img_url = soup.find('img', class_='wide-image')['src']
        img_url = "https://astrogeology.usgs.gov" + img_url
        print(img_url)
        
        hemis_dictionary = {"title": hemis_title, "img_url":img_url}
        hemisphere_image_urls.append(hemis_dictionary)
        
        browser.back()
        time.sleep(2)

    browser.quit()


    mars_data = {
        "title": title,
        "paragraph": paragraph,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "html_table": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    return mars_dictionary