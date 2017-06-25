from selenium import webdriver
import time
import pyautogui


def loginFB():
    browserType=webdriver.Chrome("C:\Users\Brvno\Downloads\chromedriver.exe")
    browserType.maximize_window()
    browserType.get("https://facebook.com")
    login=browserType.find_element_by_id("email")
    password=browserType.find_element_by_id("pass")
    login.send_keys("username") 
    print("Username entered...")
    password.send_keys("password")
    print("Password entered...")
    browserType.find_element_by_id("u_0_r").click()
    print("Facebook successfully logged in...")
    pyautogui.moveTo(300,500,duration=1)
    pyautogui.click(300,500)
    browserType.find_element_by_xpath("//div[textarea/@name='xhpc_message']").click()
    post = browserType.find_element_by_xpath("//*[@id='composer_text_input_box']/div/div/div[2]/div/div/div/div]")
    post.send_keys("wasak")
    browserType.find_element_by_xpath("//div[textarea/@name='xhpc_message']").click()
    post = browserType.find_element_by_xpath("//*[@id='composer_text_input_box']/div/div/div[2]/div/div/div/div]")
    post.send_keys("wasak")
    browserType.find_element_by_xpath("//div[button/@data-testid='react-composer-post-button']").click()
    
    

def loginTwitter():
    browserType=webdriver.Chrome("C:\Users\Brvno\Downloads\chromedriver.exe")
    browserType.maximize_window()
    browserType.get("https://twitter.com/") 
    login=browserType.find_element_by_id("signin-email")
    password=browserType.find_element_by_id("signin-password")
    login.send_keys("username") 
    password.send_keys("password")   
    password.send_keys(u'\ue007')
    browserType.pause()

def loginIG():
    browserType=webdriver.Chrome("C:\Users\Brvno\Downloads\chromedriver.exe")
    browserType.maximize_window()
    browserType.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv1.0%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26scope%3Demail%26response_type%3Dtoken%252Cgranted_scopes%26client_id%3D124024574287414%26ret%3Dlogin%26logger_id%3Dd658acac-a0ea-2865-8b95-aa41b3034dee&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=page&locale=en_US&logger_id=d658acac-a0ea-2865-8b95-aa41b3034dee")
    login=browserType.find_element_by_id("email")
    password=browserType.find_element_by_id("pass")
    login.send_keys("username") 
    password.send_keys("password")
    browserType.find_element_by_id("loginbutton").click()
    browserType.pause()

def loginSteam():
        browserType=webdriver.Chrome("C:\Users\Brvno\Downloads\chromedriver.exe")
        browserType.maximize_window()
        browserType.get("https://store.steampowered.com//login/?redir=") 
        login=browserType.find_element_by_id("input_username")
        password=browserType.find_element_by_id("input_password")
        login.send_keys("xxxzaijanxxx") 
        password.send_keys("john009324407787")
        password.send_keys(u'\ue007')
        browserType.pause()
        

print("Brunomarvss social media auto-login")
print("[1] Facebook")
print("[2] Twitter")
print("[3] Instagram (if account connected to Facebook)")
print("[4] Steam")

choice = raw_input("Enter choice: ")

def main():
    if choice is "1":
            loginFB()

    elif choice is "2":
            loginTwitter()

    elif choice is "3":
            loginIG()

    elif choice is "4":
            loginSteam()
    elif choice is "0":
        browserType=webdriver.Chrome("C:\Users\Brvno\Downloads\chromedriver.exe")
        browserType.quit()

                                    

main()
