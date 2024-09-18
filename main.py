from appium import webdriver
from appium.options.common.base import AppiumOptions
from kakao_travel_insurance import *
from datetime import datetime

adp_info = input("please insert idp code : ")
# adp_info = "RF9R501VDPW" 
options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": adp_info,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

# 카카오페이손해보험 해외여행보험 홈 > 내보험료 알아보기로 이동
reopen_home(driver)

# 여행 나라 선택 페이지
select_country(driver)

# 날짜 지정 페이지
select_calendar(driver)

# 보장 선택 페이지
select_guarantee(driver)

# 보장 상세보기 페이지
chek_insurance(driver)

# 동행인 선택 페이지
Choose_companion(driver)

# 가입 확인 페이지
handle_ineligible_items(driver)

# 가입 확인 페이지
Confirm_subscription(driver)

# 해외여행보험 통합청약서 및 약관 동의 페이지
TOS(driver)


# 현재 시간을 가져오기
current_time = datetime.now()
# 출력 형식 지정 (예: 년-월-일 시:분:초)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
print("{} 에 문자 메시지 발송 확인".format(formatted_time))

driver.quit()