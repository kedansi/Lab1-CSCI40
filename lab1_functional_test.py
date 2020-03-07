from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_can_display_a_heroes_list_and_more_information_per_hero(self):
		# Widget has heard about a new wiki app for the game called The Will of the Wisps. 
		# She goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention 
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage

		cloud = self.browser.find_element_by_id('cloud')
		jester = self.browser.find_element_by_id('jester')
		sunflowey = self.browser.find_element_by_id('sunflowey')
		self.assertIn('Cloud', cloud.text)
		self.assertIn('Jester', jester.text)
		self.assertIn('Sunflowey', sunflowey.text)
		self.assertIn('Health Points', cloud.text)
		self.assertIn('Base Attack Damage', cloud.text)
		self.assertIn('Health Points', jester.text)
		self.assertIn('Base Attack Damage', jester.text)
		self.assertIn('Health Points', sunflowey.text)
		self.assertIn('Base Attack Damage', sunflowey.text)
		
		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		cloud_view = self.browser.find_element_by_id('cloud-view')	
		cloud_view.click()
		self.assertEquals('http://localhost:8000/hero/cloud/',
		self.browser.current_url)
		list_of_attributes = self.browser.find_elements_by_tag_name('dt')
		self.assertIn('Health Points', list_of_attributes[0].text)
		self.assertIn('Base Attack Damage', list_of_attributes[1].text)
		self.assertIn('Skills', list_of_attributes[2].text)
		self.assertIn('Lore', list_of_attributes[3].text)
		# She spots the page title and header mentions the name of the hero she selected.
		self.assertIn('Detail - Cloud', self.browser.title)

		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.
		back_to_heroes_list_button = self.browser.find_element_by_tag_name('button')
		self.assertIn('Back to Heroes List', back_to_heroes_list_button.text)
		back_to_heroes_list_button.click()
		self.assertEquals('http://localhost:8000/heroes/',self.browser.current_url)

		#time 
		time.sleep(5)
		


if __name__ == '__main__':
	unittest.main(warnings='ignore')