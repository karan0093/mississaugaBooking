import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

class Automate:

	def __init__(self,arg1,arg2,arg3):
		self.arg1 = arg1
		self.arg2 = arg2
		self.arg3 = arg3

	def runSequence(self):
		driver = self.startSeq()		
			
			##necessary if you're not running headless
			#driver.maximize_window()
		
		driver.get(self.arg3)
		time.sleep(5)
					
			##necessary if you're not running headless 
			#closeMess = driver.find_element_by_xpath("//body/div[@id='jpWalkthrough']/div[@id='jpwTooltip']/div[@id='tooltipWrapper']/div[@id='tooltipInner']/div[@id='type-intro']/a[1]")
			#closeMess.click()
			#time.sleep(2)
			#driver.switch_to.parent_frame();
		
		#showAll Button
		self.findAndClick(driver,"//body/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ul[1]/li[2]/div[3]")

		#registerButton
		if "valley" in self.arg3:
			self.findAndClick(driver,"//body/div[5]/div[3]/div[7]/ul[1]/li[1]/div[2]/p[1]/button[1]")
		else:
			self.findAndClick(driver,"//body/div[5]/div[3]/div[3]/ul[1]/li[1]/div[2]/p[1]/button[1]")
		
		#(clicking register generates new tab) so traverse to new tab
		self.switchContext(driver,1)

		
		try:
			#wait or add button
			self.findAndClick(driver,"/html[1]/body[1]/div[2]/div[3]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]")

		except NoSuchElementException:	#only triggered if you're trying to book too far into future (added functionality in case you don't book at 6am)
			self.switchContext(driver,0)
		
			#register button
			self.findAndClick(driver,"//body/div[5]/div[3]/div[2]/ul[1]/li[1]/div[2]/p[1]/button[1]")
	
			self.switchContext(driver,2)
			
			#wait or add button
			self.findAndClick(driver,"/html[1]/body[1]/div[2]/div[3]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]")
		
		#enters loginID
		self.enterKey(driver,"//input[@id='ClientBarcode']",self.arg1)

		#enter password
		self.enterKey(driver,"//input[@id='AccountPIN']",self.arg2)

		#loginButton
		self.findAndClick(driver,"//input[@id='Enter']")

		#client button
		self.findAndClick(driver,"//tbody/tr[1]/td[1]/div[1]/span[2]/select[1]/option[2]")
		
		#checkout button
		self.findAndClick(driver,"//body/div[1]/div[2]/form[1]/div[3]/div[1]/span[1]/span[1]/input[1]")
		
		try:
			#agree conditions button
			self.findAndClick(driver,"//body/div[1]/div[2]/form[1]/div[3]/span[1]/input[1]")
			print ("Signed up " +self.arg1) 
			
		except NoSuchElementException:
			#if agree conditions button doesn't show you're waitlisted
			print ("Waitlisted " +self.arg1)

		time.sleep(5)
		driver.quit()
		time.sleep(5)
				
	def runSequenceMV(self):
		driver = self.startSeq()


	def startSeq(self):
		options = Options()
		options.add_argument("--headless")
		options.add_argument('--no-sandbox')
		return webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
		
	def findAndClick(self,driver,xpath):
		driver.find_element_by_xpath(xpath).click()
		time.sleep(5)

	def enterKey(self,driver,xpath,key):
		driver.find_element_by_xpath(xpath).send_keys(key)
		
	def switchContext(self,driver,x):
		driver.switch_to.window(driver.window_handles[x])
		time.sleep(5)
