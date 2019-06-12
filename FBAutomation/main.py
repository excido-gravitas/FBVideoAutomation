from selenium import webdriver
import time
import pyautogui
import requests

driver = webdriver.Chrome('LOCATION OF WEBDRIVER')
driver.get("https://www.facebook.com")

email = driver.find_element_by_name("email")
#Your email here
email.send_keys("YOUR EMAIL")

password = driver.find_element_by_name("pass")
#Your password here
password.send_keys("YOUR PASSWORD")


loginLabel = driver.find_element_by_id("loginbutton")
idOfButton = loginLabel.get_attribute("for")
submit = driver.find_element_by_id(idOfButton)
submit.submit()

time.sleep(2)

#Whatever FB Group you want to use
driver.get("https://www.facebook.com/groups/1993297350955377/videos/")

time.sleep(1)

pyautogui.press("esc")

time.sleep(1)

videos = driver.find_elements_by_class_name("_400z")
urls = [v.get_attribute("href") for v in videos]
count = 0

#Change the number based on how many urls you want to download
for i in urls[0:3]:
    count = count + 1
    url = i.replace("www", "m")
    print(url)

    driver.get(url)

    time.sleep(1)

    pyautogui.click(500,800)

    time.sleep(3)


    # the javascript code is inspired by https://stackoverflow.com/questions/20621084/how-to-get-list-of-network-requests-done-by-html

    js = """
    function getLargestFile() {
    
        var capture_resource = performance.getEntriesByType("resource");
        var largestFileSize = 0;
        var largestFile= '';
        for (var i = 0; i < capture_resource.length; i++) {
                // if (capture_resource[i].initiatorType == "fetch" || capture_resource[i].initiatorType == "video") {
                    if (capture_resource[i].initiatorType != "script" && capture_resource[i].decodedBodySize > largestFileSize) {
                        largestFileSize = capture_resource[i].decodedBodySize;
                        largestFile = capture_resource[i];
                    }
                // }
    
        }
        return largestFile;
    }
    
    var name = getLargestFile().name;
    return name
    """

    name = driver.execute_script(js)
    print(name)


    def download_video_series(link):

            r = requests.get(link, stream=True)

            # download started
            with open("video%s.mp4" % count, 'wb+') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)


    download_video_series(name)



