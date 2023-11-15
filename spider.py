import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 创建 ChromeOptions 对象
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 无头模式，不显示浏览器界面

# 创建 Chrome 驱动器对象，传递 options 参数
# driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome(options)

url = "https://www.epicov.org/epi3/start"

id = "JiaTao"
pwd = "251810..aaa"

driver.get(url)
time.sleep(3)
# 获取账号输入框，输入账号
login_id = driver.find_element(By.ID, "elogin")
login_id.send_keys(id)

# 获取密码输入框，输入账号
login_pwd = driver.find_element(By.ID, "epassword")
login_pwd.send_keys(pwd)

btn = driver.find_element(By.XPATH, "//input[@value='Login']")
print(btn)
time.sleep(3)
btn.click()
# 获取新页面
# driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

# 进入指定流感病毒数据库
try:
    # 定位到 <a> 元素
    link_element = driver.find_element(By.XPATH, "//a[text()='EpiFlu™']")
    # 执行 <a> 元素的 onclick 方法
    driver.execute_script(link_element.get_attribute("onclick"))
    time.sleep(5)
    # 在执行操作后，可以进行其他操作...
finally:
    pass
#   time.sleep(15)
try:
    # 定位到具有指定 class 的 <div> 元素， 进入EplFlu的Search界面
    div_element = driver.find_element(By.XPATH, "//div[@class='sys-actionbar-action-ni' and contains(text(), 'Search')]")
    print(div_element.text)
    # 使用 execute_script() 调用 onclick 方法
    driver.execute_script(div_element.get_attribute("onclick"))
    # time.sleep(50)

    element_id = "ce_rzfvbw_ca_entry"

    # 设置等待时间，最多等待 20 秒
    wait = WebDriverWait(driver, 40)

    # 使用显式等待等待页面元素加载完成
    # 例如，等待一个特定的元素出现
    element = wait.until(EC.presence_of_element_located((By.ID, element_id)))
    # 执行其他操作，等待元素加载完成后再进行

    # 定位到 <input> 元素
    input_element = driver.find_element(By.ID, "ce_rzfvbw_ca_entry")
    # 输入文本值， 需要查询的毒株名
    input_element.send_keys("A/Beijing/262/1995")
    print("目前查询框类容")
    # print(input_element.value)
    # 点击查询
    # 定位到 <button> 元素
    # 使用CSS选择器定位按钮并点击
    button_element = driver.find_elements(By.CSS_SELECTOR, "button.sys-form-button")
    # 执行点击操作
    print("0000")
    print(button_element[1].text)
    driver.execute_script("arguments[0].dispatchEvent(new Event('click'));", button_element[1])


    # 现在已经进入查询结果界面
    time.sleep(4)
    # 如何保存查到的信息
    # list_a表示查询出来的毒株条数
    list_a = driver.find_elements(By.XPATH, "/html/body/form/div[5]/div/div[2]/div/div[2]/div/div[1]/div[3]/table/tbody[2]/tr")
    print(list_a)

    # TO DO






finally:
    # 关闭浏览器
    print("准备guanbi")
    time.sleep(50)
    driver.quit()

# 定义一个find 方法，输入为毒株名，该方法依据毒株名将查询结果写入到结果文件里面。使用循环调用该方法实现多个毒株序列的查找。

"""
定义两个文件，源文件是所有待查找的毒株序列，结果文件里面包含两列，name和seq,表示毒株名和对应序列。
通过循环从源文件获取name传递到find方法里面实现查找。
若果有结果，保留结果，查找为空保留一个空值。
"""

# 调用find方法是在EpiFlu的查询界面。
def find(strain_neme):
    result = ""  # 默认为空，有结果就使用seq结果替换result.
    if '/' not in strain_neme:  # 如果名称不符合
        return


    pass

