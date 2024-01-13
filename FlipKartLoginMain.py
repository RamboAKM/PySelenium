""" Flip kart login code"""
import PyWebDriver
import time


class FlipKart(PyWebDriver):
    """ Flip Kart operations """

    def login(self, user_name, password):
        """ Login function """
        self.launch_browser(url='https://www.flipkart.com/')
        self.wait_for_element_visible(element_attribute='PARTIAL_TEXT', element_value='Login')
        self.click_on_element_by_xpath(xpath_value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
        self.input_text(element_attribute='XPATH',
                        element_value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input',
                        text_value=user_name)
        self.click_on_element_by_xpath(xpath_value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
        self.input_text(element_attribute='XPATH',
                        element_value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input',
                        text_value=password)
        self.click_on_element_by_xpath(
            xpath_value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button/span')

    def search_for_item(self, item_name):
        """ Search for an item """
        self.wait_for_element_visible(element_attribute='XPATH', element_value='//*[@name="q"]')
        time.sleep(2)
        self.wait_until_element_can_be_clicked(element_attribute='XPATH', element_value='//*[@name="q"]')
        self.click_on_element_by_xpath(xpath_value='//*[@name="q"]')
        self.input_text(element_attribute='XPATH', element_value='//*[@name="q"]', text_value=item_name)
        self.wait_until_element_can_be_clicked(element_attribute='XPATH', element_value='//*[@type="submit"]')
        # time.sleep(5)
        self.click_on_element_by_xpath(xpath_value='//*[@type="submit"]')


flip_kart_object = FlipKart()
flip_kart_object.login(user_name='789879879798', password='78987979878')
flip_kart_object.search_for_item(item_name='Honor Play')
