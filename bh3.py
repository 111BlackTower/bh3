import pyautogui
import time


time.sleep(3)


# 点出击
pyautogui.click(1663, 254, button='left')  # 点出击
time.sleep(1)
pyautogui.click(91, 305, button='left')  # 点出击
time.sleep(1)
pyautogui.click(1623, 841, button='left')  # 点材料远争
time.sleep(1)
pyautogui.click(1734, 1004, button='left')  # 点材料远争减负
time.sleep(1)
pyautogui.click(919, 796, button='left')  # 点材料远争减负2
time.sleep(0.8)
pyautogui.click(919, 796, button='left')  # 点材料远争减负2确定
time.sleep(0.8)
pyautogui.press('Home')  # 退出材料远争
time.sleep(1)
# 点家园
pyautogui.click(1573, 975, button='left')  # 点家园
time.sleep(1.8)
pyautogui.mouseDown(529, 208)  # 鼠标按下# 点金币
time.sleep(0.1)
pyautogui.mouseUp(529, 208)  # 鼠标释放
time.sleep(0.8)
pyautogui.click(529, 208, button='left')
time.sleep(0.3)
pyautogui.click(305,226, button='left')
time.sleep(0.8)
pyautogui.click(1065,830, button='left')
time.sleep(0.5)
pyautogui.click(1274, 990, button='left')
time.sleep(0.3)
# 点家园远争
pyautogui.click(1274, 990, button='left')  # 点远争
time.sleep(0.5)
pyautogui.click(1390, 361, button='left')
time.sleep(0.8)
pyautogui.click(963, 809, button='left')
time.sleep(1)
pyautogui.click(1399, 361, button='left')  # 点开始远征1
time.sleep(1)
pyautogui.click(1197, 975, button='left')  # 点一键派遣
time.sleep(1)
pyautogui.click(1655, 982, button='left')  # 点确定派遣
time.sleep(1)
pyautogui.click(1428, 554, button='left')  # 点开始远征2
time.sleep(1)
pyautogui.click(1197, 975, button='left')  # 点一键派遣
time.sleep(1)
pyautogui.click(1655, 982, button='left')  # 点确定派遣
time.sleep(1)
pyautogui.click(1415, 746, button='left')  # 点开始远征3
time.sleep(1)
pyautogui.click(1197, 975, button='left')  # 点一键派遣
time.sleep(1)
pyautogui.click(1655, 982, button='left')  # 点确定派遣
time.sleep(1)
pyautogui.click(1412, 938, button='left')  # 点开始远征4
time.sleep(1)
pyautogui.click(1197, 975, button='left')  # 点一键派遣
time.sleep(1)
pyautogui.click(1655, 982, button='left')  # 点确定派遣
time.sleep(1)
pyautogui.press('~')  # 退出远争
time.sleep(1.8)
#点打工
pyautogui.click(1510, 1009, button='left')  # 点打工
time.sleep(2)
pyautogui.click(1869, 532, button='left')#打开打工列表
time.sleep(1)

rgb = pyautogui.screenshot().getpixel((1816, 69))
time.sleep(0.5)
while True:
    rgb1 = pyautogui.screenshot().getpixel((1816, 69))
    time.sleep(0.5)
    if rgb1 == rgb:
        pyautogui.click(1632, 146, button='left')  # 收打工
        time.sleep(1)
        pyautogui.click(965, 803, button='left')  # 点确定
        time.sleep(1)
    else:
        print('结束收打工')
        break
while True:
    rgb = pyautogui.screenshot().getpixel((1284, 65))
    if rgb == (255, 235, 0) or rgb == (244, 162, 255):
        pyautogui.click(1632, 146, button='left')  # 点打工
        time.sleep(1.5)
        pyautogui.click(1265, 1002, button='left')  # 点快速派遣
        time.sleep(1)
        pyautogui.click(1677, 996, button='left')  # 点开始打工
        time.sleep(1.5)
    else:
        pyautogui.press('~')  # 退出派遣
        time.sleep(1)
        pyautogui.press('~')
        break
time.sleep(1)
# 点舰团
pyautogui.click(1318, 972, button='left')
time.sleep(1)
pyautogui.click(705, 997, button='left')  # 点回收
time.sleep(1)
pyautogui.click(272, 968, button='left')  # 点申请
time.sleep(1)
pyautogui.click(1634,384, button='left')  # 点接受
time.sleep(0.5)
pyautogui.click(1446, 970, button='left')  # 点提交
time.sleep(0.5)
for i in range(8):  # 点8次
    pyautogui.click(1446, 970, button='left')  # 点提交
    time.sleep(0.3)
    pyautogui.click(1135, 825, button='left')  # 点提交委托
    time.sleep(0.3)
    pyautogui.click(1135, 825, button='left')  # 点提交委托
    time.sleep(0.2)
    pyautogui.click(1135, 825, button='left')
    time.sleep(0.5)
pyautogui.click(1771,340, button='left')#点奖池
time.sleep(1)
pyautogui.click(1362,961, button='left')#点领取
time.sleep(0.2)
pyautogui.click(1362,961, button='left')
time.sleep(0.5)
pyautogui.press('Home')  # 退出家园
time.sleep(1)
#收每日
time.sleep(3)
pyautogui.click(73,195, button='left')
time.sleep(0.8)
pyautogui.click(73,195, button='left')
time.sleep(0.5)
pyautogui.click(1719,166, button='left')
time.sleep(1)
pyautogui.click(969,820, button='left')
time.sleep(0.3)
pyautogui.click(1820,956, button='left')
time.sleep(0.8)
pyautogui.click(969,820, button='left')
time.sleep(0.8)
pyautogui.press('Home')