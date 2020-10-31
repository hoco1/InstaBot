from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep
import random
import sys
import sqlite3 as db
from datetime import datetime

conn = db.connect('userData.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS listUser(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT COLLATE NOCASE,
    password TEXT,
    msg TEXT,
    date TEXT
)''')

def addUser(user,password,msg = None):
    timeDate = datetime.now().strftime('%Y - %m - %d | %H : %M')
    c.execute('INSERT INTO listUser VALUES (:id,:user,:password,:msg,:date)'
    ,{'id':None,'user':user,'password':password,'msg':msg,'date':timeDate})
    conn.commit()
    conn.close()

def show():
    c.execute('SELECT * FROM listUser')
    res = c.fetchall()
    c.execute('SELECT COUNT(*) FROM listUser')
    countRes = c.fetchone()[0]
    return res,countRes

def lastJoin():
    c.execute('SELECT MAX(id) FROM listUser')
    last = c.fetchone()[0]
    c.execute('SELECT user FROM listUser WHERE id >= :id',
        {'id':last})
    user = c.fetchone()[0]
    c.execute('SELECT password FROM listUser WHERE id >= :id',
        {'id':last})
    password = c.fetchone()[0]
    return user,password
class instabot:
    def __init__(self,userName,pas):
        self.driver = webdriver.Chrome()
        self.userName = userName
        self.pas = pas
    def closeBrowser(self):
        self.driver.close()

    @property
    def SignIn(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        userNameInput = self.driver.find_element_by_xpath('//input[@name= "username"]')
        passwordInput = self.driver.find_element_by_xpath('//input[@name = "password"]')
        userNameInput.send_keys(self.userName)
        passwordInput.send_keys(self.pas)
        passwordInput.send_keys(Keys.ENTER)
        notNowButton = WebDriverWait(self.driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
        notNowButton.click()

    
    def likeTagPhoto(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/{}/".format(hashtag))
        sleep(2)

        pic_hrefs = []
        for i in range(1,2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            except Exception:
                continue

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            sleep(2)
            try:
                sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_class_name('fr66n').click()
                like_button()
                sleep(2)
            except Exception as e:
                sleep(2)
    
    def likeUserPhoto(self,user):
        driver = self.driver
        driver.get('https://www.instagram.com/{}'.format(user))
        sleep(2)

        pic_hrefs = []
        for i in range(1,2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            except Exception:
                continue

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            sleep(2)
            try:
                sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_class_name('fr66n').click()
                like_button()
                sleep(2)
            except Exception as e:
                sleep(2)

    
    def follow(self,user):
        driver = self.driver
        driver.get('https://www.instagram.com/{}/'.format(user))

        followButtom = driver.find_element_by_css_selector('button')
        followButtom.click()
        sleep(3)

    def unFollow(self,user):
        driver = self.driver
        driver.get('https://www.instagram.com/{}/'.format(user))

        unfollowStepOne = driver.find_element_by_css_selector('button')
        unfollowStepOne.click()
        unfollowButtom = driver.find_element_by_class_name('aOOlW.-Cab_')
        unfollowButtom.click()
    
    def seenStroy(self,user):
        driver = self.driver
        driver.get('https://www.instagram.com/{}/'.format(user))

        story = driver.find_element_by_class_name('_2dbep')
        story.click()
        sleep(2)
        while True:
            try:
                nextBottom = driver.find_element_by_class_name('coreSpriteRightChevron')
                nextBottom.click()
                sleep(2)
            except Exception:
                break
    def reportUser(self,user):
        driver = self.driver
        driver.get('https://www.instagram.com/{}/'.format(user))

        threePoint = driver.find_element_by_class_name('AFWDX')
        threePoint.click()
        sleep(random.randint(2,5))
        reportButtom = driver.find_element_by_xpath('//button[text() = "Report User"]')
        reportButtom.click()
        sleep(random.randint(2,5))
        resoneButtom = driver.find_element_by_css_selector('div[role=\'list\'] button')
        resoneButtom.click()
        sleep(random.randint(2,5))

        close = driver.find_element_by_xpath('//button[text() = "Close"]')
        close.click()
        sleep(6)
    
    def blockUser(self,user):
        driver = self.driver
        driver.get('https://www.instagram.com/{}/'.format(user))

        threePoint = driver.find_element_by_class_name('AFWDX')
        threePoint.click()
        sleep(2)

        blockButtom = driver.find_element_by_xpath('//button[text() = "Block this user"]')
        blockButtom.click()

        sureBlock = driver.find_element_by_class_name('aOOlW.bIiDR')
        sureBlock.click()

        dismiss = driver.find_element_by_class_name('aOOlW.HoLwm')
        dismiss.click()
        sleep(3)
    
    def getUserFollowers(self, username):
        driver = self.driver
        driver.get('https://www.instagram.com/{}'.format(username)
        followersLink = driver.find_element_by_css_selector('ul li a')
        followersLink.click()
        sleep(2)
        followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
    
        followersList.click()
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            followers.append(userLink)
            if (len(followers) == max):
                break
        listId = []
        for idName in followers:
            listId.append(idName[26:-1])

        return listId
    
    def getUserFollowing(self,username):
        driver = self.driver
        driver.get('https://www.instagram.com/{}'.format(username))
        followingLink = driver.find_elements_by_css_selector('ul li a')[1]
        followingLink.click()
        sleep(2)
        followingList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        followingList.click()
        following = []
        for user in followingList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            following.append(userLink)
        listId = []
        for idName in following:
            listId.append(idName[26:-1])
        return listId

              
if __name__ == "__main__":

    username = "hocoHelper"
    password = "##########"

    ig = instabot(username, password)
    ig.SignIn

    ig.closeBrowser()
    conn.close()


        
