from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException     
from selenium.common.exceptions import TimeoutException
import unittest
 

class LoginTest(unittest.TestCase):
	
	mailData = []
	passwordData = []

	def setUp(self):
		pathToPasswords = "C:\\Users\\fournaki\\Desktop\\fbBot\\passwords.txt"
		pathToMails = "C:\\Users\\fournaki\\Desktop\\fbBot\\emails.txt"
		
		mailInputStream = open(pathToMails,"r")			
		passwordInputStream = open(pathToPasswords,"r")

		for line in mailInputStream:
			LoginTest.mailData.append(line)
		for line in passwordInputStream:
			LoginTest.passwordData.append(line)

		#Kanw reverse gia na ta fero stin swsti seira
		LoginTest.mailData.reverse()
		LoginTest.passwordData.reverse()

		self.driver = webdriver.Firefox()
		self.driver.get("https://www.facebook.com/login.php?login_attempt=1")

	def test_Login(self):
		#for i in range(0,846):
		
		driver = self.driver
		facebookUsername = LoginTest.mailData.pop()
		facebookPassword = LoginTest.passwordData.pop()
		emailFieldID     = "email"
		passFieldID      = "pass"
		loginButtonID    = "loginbutton"
		loginButtonXpath = "//input[@value='Log In]"
		fbLogoXpath		 = "(//a[contains(@href, 'logo')])[1]"
		fbLogoId		 = "u_0_e"
		errorMessageClassName = 'pam login_error_box uiBoxRed'

		emailFieldElement  = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_id(emailFieldID))
		passFieldElement   = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_id(passFieldID))
		loginButtonElement =  driver.find_element_by_id(loginButtonID)

		emailFieldElement.clear()
		emailFieldElement.send_keys(facebookUsername)
		passFieldElement.clear()
		passFieldElement.send_keys(facebookPassword)
		
		#Check if can find fblogo button top left.If true user has logged in
		try:
			WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(fbLogoId))
				
		except TimeoutException:
			print "Login failed"
		else:
			print "login successfull"
		

		#print "00000000000000"
			#def tearDown(self):
				#self.driver.back()


if __name__ == '__main__':
	unittest.main()