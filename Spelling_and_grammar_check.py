from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import language_tool_python
from datetime import datetime
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(("driver/chromedriver"),   options=chrome_options)
baseurl = "https://deligram.com/product/nestle-koko-krunch-330gm"
driver.get(baseurl)
time.sleep(5)
eles = (driver.find_elements_by_tag_name('div'))
#print(eles[4].text + eles[5].text)
total = (len(eles))
res = []
rest = []
for num in range(total):
    try:
        a_string = eles[num].text
        if(a_string != ''):
            ab_string = a_string.replace('\n',' ')
            res.append(ab_string)
    except:
        print()


result = set(res)
result = str(result)
baseurl = baseurl.replace('/','_')
time.sleep(2)
tool = language_tool_python.LanguageTool('en-US')
matches = tool.check(result)
total_mathes = len(matches)
res_count = ("Total Spelling or Grammar Problem " + "  :  " + str(total_mathes))
current_datetime = (datetime.now().strftime("%Y%m%d_%I%M%S%p"))
report_file_name = "MH_"+ baseurl +'_'+current_datetime + ".txt"
f=open(("Report" + '/' +report_file_name), "a+")
f.write("======================================================================= \n")
f.write(res_count)
f.write("\n=======================================================================")
for number in range(total_mathes):
    f.write('\n' + "Problem " + str([1+number]) + ' :- ' + str(matches[number]))
    f.write("\n==========================================================================")
f.close()
#print(print(res_count))
print("Test Successfully executed .Test Result added to Result File,please check the file. Name of the File is :-- " + report_file_name)
