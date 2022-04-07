info = []

links = ['https://www.linkedin.com/in/dulceortiz14/',
        ]

for link in links:
    browser.get(link)
    browser.implicitly_wait(1)
    def scroll_down_page(speed=8):
        current_scroll_position, new_height= 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            browser.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = browser.execute_script("return document.body.scrollHeight")

    scroll_down_page(speed=8)

    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')
    
    # Get Name of the person
    try:
        name_div = soup.find('div', {'class': 'pv-text-details__left-panel'})
        first_last_name = name_div.find('h1').get_text().strip()
    except:
        first_last_name = None
    
    # Get Talks about section info
    try:
        talksAbout_tag = talksAbout_tag.find('div', {'class': 'isplay-flex ph5 pv3'})
        talksAbout_tag = talksAbout_tag.find('span').get_text()
    except:
        talksAbout = None
    
    # Get Location of the Person
    try:
        location_tag = name_div.find('div', {'class': 'pb2 pv-text-details__left-panel'})
        location_tag= location_tag.find('span', {'class': 'text-body-small inline t-black--light break-words'}).get_text().strip()
        
        
    except:
        location = None
    
    # Get Title of the Person
    try:
        title = name_div.find('div', {'class': 'text-body-medium break-words'}).get_text().strip()
        
    except:
        title = None
    
    # Get Company Link of the Person
    try:
        contact_section = contact_section.find('section', {'class': 'pv-contact-info__contact-type ci-vanity-url'})
        a_tags = a_tags.find('a')
        company_link = a_tags['href']
        
    except:
        company_link = None

    # Get Job Title of the Person
    try:
        job_title = job_title.find('h3', {'class': 'pv-text-details__right-panel'}).get_text().strip()
    except:
        job_title = None
    
    # Get Company Name of the Person
    try:
        company_name = name_div.find('div', {'class': 'inline-show-more-text'}).get_text().strip()
    except:
        company_name = None

    contact_page = link + 'overlay/contact-info/'
    browser.get(contact_page)
    browser.implicitly_wait(1)

    contact_card = browser.page_source
    contact_page = BeautifulSoup(contact_card, 'lxml')
    # Get Linkdin Profile Link and Contact details of the Person
    try:
        contact_details = contact_page.find('section', {'class': 'pvpv-contact-info__ci-container t-14-profile-section pv-contact-info artdeco-container-card ember-view'})
        contacts = []
        for a in contact_details.find_all('a', href=True):
            contacts.append(a['href'])
    except:
        contacts.append('')
    info.append([first_last_name, title, company_link, job_title, company_name, talksAbout, location, contacts])
    time.sleep(5)


column_names = ["Full Name", "Title", "Company URl", 'Job Title', 
                'Company Name', 'Talks About', 'Location', 'Profile Link and Contact']
df = pd.DataFrame(info, columns=column_names)
df.to_csv('data.csv', index=False)

print(".................Done Scraping!.................")
browser.quit()