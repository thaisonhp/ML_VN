from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

def download_reports():
    # Thiết lập đường dẫn đến ChromeDriver
    service = Service('/Users/luongthaison/Documents/Third_years_student/ML_basic_VietNguyen/chromedriver-mac-arm64/chromedriver')
    
    # Khởi tạo WebDriver với Service
    driver = webdriver.Chrome(service=service)

    # Mở trang web của GSO
    driver.get('https://www.gso.gov.vn/bai-top/2024/07/bao-cao-tinh-hinh-kinh-te-xa-hoi-thang-bay-va-7-thang-nam-2024/?fbclid=IwY2xjawEqwHBleHRuA2FlbQIxMAABHUD0rLnfwnhK05oxZQSI4gMMLX7mPs4ERvai1rp7O6i53HTViOd0R14eog_aem_X4iQwOK8gKhYd37ANhovHg')

    # Đợi trang web tải (có thể điều chỉnh thời gian chờ)
    time.sleep(5)

    # Tạo thư mục để lưu các tệp tin tải về
    download_dir = "/Users/luongthaison/Downloads/GSO_reports"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Tìm tất cả các thẻ <a> trên trang
    links = driver.find_elements(By.TAG_NAME, 'a')

    # Danh sách để lưu các liên kết tải về
    download_links = []

    for link in links:
        href = link.get_attribute('href')
        if (href and href.endswith('.docx')) or (href and href.endswith('.xlsx')):
            download_links.append(href)

    # Tải về tất cả các tài liệu từ danh sách liên kết
    for url in download_links:
        driver.get(url)
        time.sleep(5)  # Đợi cho đến khi tải về hoàn tất

    print(f"Đã tải về {len(download_links)} tài liệu.")

    # Thao tác tiếp theo hoặc thoát trình duyệt
    driver.quit()

if __name__ == "__main__":
    download_reports()
