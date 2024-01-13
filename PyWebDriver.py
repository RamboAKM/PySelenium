# @Author : Arun Kumar M WX437455

# coding=utf-8
""""""" Common selenium operations file """""""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.select import Select
import time


class PyWebDriver:
    """"""" Common selenium operations """""""
    browserPage = None
    wait = None

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.browserPage = webdriver.Chrome(chrome_options=chrome_options)
        self.wait = WebDriverWait(self.browserPage, 60)

    def launch_browser(self, url):
        """"""" Launch browser function """""""
        self.browserPage.get(url)
        return self.browserPage

    def close_browser(self):
        """"""" Close browser function """""""
        self.browserPage.close()
        self.browserPage.quit()

    def close_window(self):
        """"""" Close tab function """""""
        self.browserPage.close()

    def click_on_element_by_text(self, text_value):
        """"""" Click on element by link text function """""""
        element = self.browserPage.find_element_by_link_text(text_value)
        element.click()

    def click_on_element_by_partial_text(self, partial_text_value):
        """"""" Click on element by partial link text function """""""
        element = self.browserPage.find_element_by_partial_link_text(partial_text_value)
        element.click()

    def click_on_element_by_id(self, id_value):
        """"""" Click on element by ID function """""""
        element = self.browserPage.find_element_by_id(id_value)
        element.click()

    def click_on_element_by_class_name(self, class_name):
        """"""" Click on element by class name function """""""
        element = self.browserPage.find_element_by_class_name(class_name)
        element.click()

    def click_on_element_by_name(self, name_value):
        """"""" Click on element by name function """""""
        element = self.browserPage.find_element_by_name(name_value)
        element.click()

    def click_on_element_by_css_selector(self, css_selector_value):
        """"""" Click on element by css selector function """""""
        element = self.browserPage.find_element_by_css_selector(css_selector_value)
        element.click()

    def click_on_element_by_xpath(self, xpath_value):
        """"""" Click on element by xpath function """""""
        element = self.browserPage.find_element_by_xpath(xpath_value)
        element.click()

    def scroll_to_element(self, element_attribute, element_value):
        """"""" Scroll to element function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        actions = ActionChains(self.browserPage)
        scroll_to_element = self.browserPage.find_element(attribute_dict[element_attribute], element_value)
        actions.move_to_element(to_element=scroll_to_element)

    def hover_over_element(self, element_attribute, element_value, click=False):
        """"""" Hover over an element function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        hover_to_element = self.browserPage.find_element(attribute_dict[element_attribute], element_value)
        hover_action = ActionChains(self.browserPage).move_to_element(to_element=hover_to_element)
        if click:
            hover_action.click().perform()
        else:
            hover_action.perform()

    def right_click_on_element(self, element_attribute, element_value):
        """"""" Perform right click on element function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        actions = ActionChains(self.browserPage)
        element_handler = self.browserPage.find_element(attribute_dict[element_attribute], element_value)
        actions.move_to_element(to_element=element_handler)
        actions.context_click().perform()

    def wait_for_element_visible(self, element_attribute, element_value, wait_time=60, exception=True):
        """"""" Explicit wait function until element is visible """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        if exception:
            if wait_time == 60:
                self.wait.until(
                    expected_conditions.visibility_of_element_located(
                        (attribute_dict[element_attribute], element_value)))
            else:
                WebDriverWait(self.browserPage, wait_time).until(
                    expected_conditions.visibility_of_element_located(
                        (attribute_dict[element_attribute], element_value)))
        else:
            try:
                if wait_time == 60:
                    self.wait.until(
                        expected_conditions.visibility_of_element_located(
                            (attribute_dict[element_attribute], element_value)))
                    return True
                else:
                    WebDriverWait(self.browserPage, wait_time).until(
                        expected_conditions.visibility_of_element_located(
                            (attribute_dict[element_attribute], element_value)))
                    return True
            except TimeoutException:
                return False

    def wait_for_element_invisible(self, element_attribute, element_value, wait_time=60):
        """"""" Explicit wait function until element is invisible """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        if wait_time == 60:
            self.wait.until(
                expected_conditions.invisibility_of_element_located((attribute_dict[element_attribute], element_value)))
        else:
            WebDriverWait(self.browserPage, wait_time).until(
                expected_conditions.visibility_of_element_located((attribute_dict[element_attribute], element_value)))

    def wait_until_element_can_be_clicked(self, element_attribute, element_value):
        """"""" Explicit wait function until element can be clicked """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        self.wait.until(
            expected_conditions.element_to_be_clickable((attribute_dict[element_attribute], element_value)))

    def switch_to_frame(self, frame_value):
        """"""" Switching to frames function """""""
        self.wait.until(
            expected_conditions.frame_to_be_available_and_switch_to_it(frame_value))

    def switch_to_parent_frame(self):
        """"""" Switching to parent frame function """""""
        self.browserPage.switch_to.parent_frame()

    def switch_to_window(self, window_value):
        """"""" Switching to windows function """""""
        window_handler = self.browserPage.window_handles[window_value]
        self.browserPage.switch_to.window(window_handler)

    def wait_for_new_window(self, window_number):
        """"""" Waiting for window function """""""
        for _ in range(5):
            try:
                if self.browserPage.window_handles[window_number]:
                    break
            except NoSuchWindowException:
                time.sleep(2)
                continue

    def check_if_window_exists(self, window_number):
        """"""" Checking if window exists function """""""
        window_number += 1
        for _ in range(5):
            if len(self.browserPage.window_handles) == window_number:
                return True
                break
            else:
                time.sleep(2)
                continue
        return False

    def get_actual_xpath_using_text(self, main_path, text_value, fuzzy=False, start_node=1):
        """"""" To get actual xpath function using text value"""""""
        for i in range(start_node, 100):
            try:
                actual_xpath = main_path.replace("replaceValue", str(i))
                element = self.browserPage.find_element_by_xpath(actual_xpath)
                if element.text == '':
                    continue
                if fuzzy:
                    if element.text in text_value:
                        return actual_xpath
                else:
                    if element.text == text_value:
                        return actual_xpath
                continue
            except NoSuchElementException:
                print("Text not found and final xpath is : ", actual_xpath)
                return False

    def get_xpath_list_using_text(self, main_path, text_value, start_node=1):
        """"""" To get actual xpath function using text value"""""""
        xpath_list = []
        for i in range(start_node, 100):
            try:
                actual_xpath = main_path.replace("replaceValue", str(i))
                self.scroll_to_element(element_attribute='XPATH', element_value=actual_xpath)
                element = self.browserPage.find_element_by_xpath(actual_xpath)
                if element.text == text_value:
                    xpath_list.append(actual_xpath)
                continue
            except NoSuchElementException:
                return xpath_list

    def get_xpath_list(self, main_path, start_node=1):
        """ To get the all available xpath for the main path """
        xpath_list = []
        for i in range(start_node, 100):
            try:
                actual_xpath = main_path.replace("replaceValue", str(i))
                self.browserPage.find_element_by_xpath(actual_xpath)
                xpath_list.append(actual_xpath)
                continue
            except NoSuchElementException:
                return xpath_list

    def input_text(self, element_attribute, element_value, text_value, clear_status=True):
        """"""" Input text function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        element = self.browserPage.find_element(attribute_dict[element_attribute], element_value)
        if clear_status:
            element.clear()
        element.send_keys(text_value)

    def get_text(self, element_attribute, element_value):
        """"""" Get text function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        element = self.browserPage.find_element(attribute_dict[element_attribute], element_value)
        return element.text

    def select_element_from_drop_down(self, element_attribute, element_value, select_type, select_value):
        """"""" Get text function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        element = Select(self.browserPage.find_element(attribute_dict[element_attribute], element_value))
        if select_type == 'VALUE':
            element.select_by_value(value=select_value)
        elif select_type == 'INDEX':
            element.select_by_index(index=select_value)
        elif select_type == 'TEXT' :
            element.select_by_visible_text(text=select_value)
        else:
            raise "Error : select_type option is invalid. Please select a valid option."

    def get_element_attribute(self, element_attribute, element_value, attribute_name):
        """"""" Get element attribute function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        element = self.browserPage.find_element(attribute_dict[element_attribute], element_value)
        return element.get_attribute(name=attribute_name)

    def get_child_node_xpath_list(self, element_value):
        """"""" Get child node list function """""""
        xpath_list = []
        for i in range(1, 100):
            try:
                self.browserPage.find_element(By.XPATH, element_value.replace('replace_value', str(i)))
                xpath_list.append(element_value.replace('replace_value', str(i)))
            except NoSuchElementException:
                break
        return xpath_list

    def get_child_node_list(self, element_attribute, element_value):
        """"""" Get element attribute function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        element = self.browserPage.find_elements(attribute_dict[element_attribute], element_value)
        return element

    def check_if_element_exists(self, element_attribute, element_value, time_out=5):
        """"""" Check if element exists function """""""
        attribute_dict = {'ID': By.ID, 'CLASS': By.CLASS_NAME, 'XPATH': By.XPATH, 'CSS': By.CSS_SELECTOR,
                          'PARTIAL_TEXT': By.PARTIAL_LINK_TEXT, 'TEXT': By.LINK_TEXT, 'NAME': By.NAME}
        try:
            WebDriverWait(self.browserPage, time_out).until(
                expected_conditions.visibility_of_element_located((attribute_dict[element_attribute], element_value)))
            return True
        except TimeoutException:
            return False

    def window_refresh(self):
        """"""" Refresh the webpage """""""
        self.browserPage.refresh()
