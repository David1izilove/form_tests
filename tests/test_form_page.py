import fake_data


class TestFormPage:

    def test_open_form_page(self, chrome_browser):
        chrome_browser.get('https://yuri-reigo.github.io/')

    def test_first_name_input_error_message(self, chrome_browser):
        expected_error_message = 'Please fill in this field.'
        chrome_browser.find_element_by_xpath('//*[@id="fs-frm"]/input').click()
        error_message = chrome_browser.find_element_by_name('name').get_attribute('validationMessage')
        assert expected_error_message == error_message

    def test_input_fullname(self, chrome_browser):
        chrome_browser.find_element_by_name('name').send_keys(fake_data.fake_name())

    def test_input_email_address(self, chrome_browser):
        chrome_browser.find_element_by_name('_replyto').send_keys(fake_data.fake_email())

    def test_placeholder_massage(self, chrome_browser):
        message_placeholder = chrome_browser.find_element_by_name('message').get_attribute('placeholder')
        assert isinstance(message_placeholder, str)

    def test_input_massage(self, chrome_browser):
        chrome_browser.find_element_by_name('message').send_keys(fake_data.fake_text())

    def test_submit_form(self, chrome_browser):
        chrome_browser.find_element_by_xpath('//*[@id="fs-frm"]/input').click()

    def test_form_submitted(self, chrome_browser):
        expected_text = 'The form was submitted successfully.'
        text_form_page = chrome_browser.find_element_by_xpath('//*[@class="col-1-1"]/p').text
        assert expected_text == text_form_page

