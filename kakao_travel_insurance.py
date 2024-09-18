from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
import time

# 특정 element를 찾을때까지 기다림.
# XPATH를 사용함.
def wait_until(driver,xpath_str):
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, xpath_str)))
        element = driver.find_element(By.XPATH, value=xpath_str)
        return element
    except Exception as e:
        print("오류 발생: {}".format(e))
        print("해당 element를 찾을 수 없습니다. 다시 한번 확인해주세요: {}".format(xpath_str))

# 다음 버튼 선택
def click_next(driver):
    wait_until(driver,'//android.widget.Button[@text="다음"]').click()

# 카카오톡을 통해 카카오페이손해보험 해외여행보험 홈 > 내보험료 알아보기로 이동
def reopen_home(driver):
    # 최근 앱 메뉴 선택후 모두닫기 (카카오톡 세팅 초기화)
    driver.press_keycode(187)
    try :
        wait_until(driver,'//android.widget.Button[@text="모두 닫기"]').click()
    except:
         driver.press_keycode(187)
    # 홈 버튼 선택
    driver.press_keycode(3)
    # 카카오톡 선택
    wait_until(driver,'//android.widget.TextView[@content-desc="카카오톡"]').click()
    # wait 필요 ()
    # 검색 선택 > 카카오페이손해보험 검색
    
    wait_until(driver,'//android.widget.Button[contains(@content-desc,"검색")]').click()
    search_text_box = wait_until(driver,"//android.view.View[@resource-id=\"__root__\"]\
                                /android.view.View[1]/android.view.View/android.view.View/\
                                android.view.View/android.view.View/android.widget.EditText")
    search_text_box.send_keys("카카오페이손해보험")

    # 카카오페이손해보험 대화 선택
    # 채널 탭 > 카카오페이손해보험 선택 > 
    wait_until(driver,'(//android.widget.TextView[@text="채널"])[1]').click()
    wait_until(driver,'//android.view.View[@text="카카오페이손해보험"]').click()
    wait_until(driver,'//android.widget.ImageView[@content-desc="채팅하기"]').click()

    # 채널 더보기 > 홈 선택
    wait_until(driver,"//android.widget.Button[@content-desc=\"채널 메뉴 펼치기\"]").click()
    wait_until(driver,"//android.widget.Button[@text=\"홈\"]").click()

    # 카카오손해보험 > 해외여행보험 홈.
    wait_until(driver,"//android.widget.Button[contains(@text,'해외여행보험')]").click()

    # 내 보험료 알아보기 버튼 선택
    wait_until(driver,'//android.widget.Button[@text="내 보험료 알아보기"]').click()

# 여행 나라 선택 페이지
def select_country(driver) :     
    # 입력받은 나라 검색 후 해당 태그 선택, 다음 버튼 선택
    while(True):
        country = input("나라 이름을 입력하세요.")
        wait_until(driver,"//android.widget.EditText").send_keys(country)
        try:
            wait_until(driver,"//android.widget.Button[@text=\"{}\"]".format(country)).click()
            break
        except:
            print("잘못된 입력값입니다. 다시한 번 확인해주세요.")
    click_next(driver)

# 날짜 지정 페이지
def select_calendar(driver):
    # 다음달 1일부터 7일까지 선택하기
    wait_until(driver,"(//android.widget.Button[@text=\"1\"])[2]").click()
    wait_until(driver,"(//android.widget.Button[@text=\"7\"])[2]").click()
    wait_until(driver,'(//android.widget.Button[@text="다음"])[2]').click()
    click_next(driver)
    # 출발 시간 선택
    # driver.find_element(By.XPATH, value='//android.view.View[@text="집에서 출발하는 시간"]\
    #                     /following-sibling::android.widget.Button')
    # 시간 선택 

    # 도착 시간 선택
    # driver.find_element(By.XPATH, value='//android.view.View[@text="집에 도착하는 시간"]\
    #                     /following-sibling::android.widget.Button')
    # 시간 선택 

# 보장 선택 페이지
def select_guarantee(driver):
    # default 로 선택된 보장 선택 후 다음페이지로 이동
    
    # case 1 : 추천해주세요 > 기본형
    wait_until(driver,'//android.widget.Button[@text="추천해주세요 탭"]').click()
    wait_until(driver,'//android.widget.Button[contains(@text,"기본형")]').click()

    # case 2 : 추천해주세요 > 고급형
    wait_until(driver, '//android.widget.Button[@text="추천해주세요 탭"]').click()
    wait_until(driver,'//android.widget.Button[contains(@text,"고급형")]').click()
    

    # case 3 : 직접할게요 > 전체 min
    wait_until(driver, '//android.widget.Button[@text="직접할게요 탭"]').click()

    size = driver.get_window_rect()
    width = size['width']
    height = size['height']
    scroll_distance = height*3/4
    # TouchAction을 사용하여 화면 크기만큼 아래로 스크롤
    action = TouchAction(driver)
    
    action.press(x=width-1 , y=height-1).move_to(x=0, y=scroll_distance).release().perform()
    
    # 미가입 텍스트 x 위치 불러오기
    elements = driver.find_elements(By.XPATH, value='(//android.widget.TextView[@text="미가입"])')
    for element in elements:
        element.click()

    # case 4 : 직접할게요 > 전체 max
    elements = driver.find_elements(By.XPATH, value='(//android.widget.TextView[contains(@text,"만 원")])')
    for element in elements:
        element.click()

    # 다음 선택
    click_next(driver)

# 보장 상세보기 페이지
def chek_insurance(driver):
    # 바로 다음버튼 선택
    click_next(driver)

# 동행인 선택 페이지
def Choose_companion(driver):
    member = 1
    child = False
    # 동행인 X : 혼자 가입하기 
    if member == 1:
        wait_until(driver,'//android.widget.Button[@text="혼자 가입할게요"]').click()
    # 동행인 O : 다음
    else:
        click_next(driver)

# 가입 불가 항목 안내 페이지
def handle_ineligible_items(driver):
    # 없어요 선택
    wait_until(driver,'//android.widget.Button[@text="없어요"]').click()
# 가입 확인 페이지
def Confirm_subscription(driver):
    # 이렇게 가입할게요 버튼 > 맞아요 버튼 선택
    wait_until(driver,'//android.widget.Button[@text="이렇게 가입할게요"]').click()
    wait_until(driver,'//android.widget.Button[@text="맞아요"]').click()

def TOS(driver):
    # 해외여행보험 통합청약서
    # 확인했어요 선택
    wait_until(driver,'//android.widget.Button[@text="확인했어요"]').click()
    # 해외여행보험 보험약관
    # 확인했어요 선택
    time.sleep(10)
    wait_until(driver,'//android.widget.Button[@text="확인했어요"]').click()

    # 약관동의 페이지
    # 전체 동의 후 모든 내용에 동의할게요 버튼 선택
    wait_until(driver,'//android.widget.Button[@text=\"전체동의\"]').click()
    wait_until(driver,'//android.widget.Button[@text=\"모든 내용에 동의할게요\"]').click()



