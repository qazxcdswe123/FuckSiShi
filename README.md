# Fuck Stupid Timewaster SiShi (实屎)

- 关键词
  - 华南师范大学
  - 四史
  - 砺儒云课堂
  - 脚本
  - 自动化答题
  - 答案
 
## Quick Start
1. 修改 `final.txt` . 删除所有开刷 **之前** 的答案 (对照 pdf 或 docx 文件)
2. `pip3 install pyperclip`
3. `python3 main.py` 
4. 输入题目个数
5. 此时答案会自动复制到剪切板
6. 打开浏览器控制台( `F12` or `Ctrl + Shift + I` )，粘贴命令
7. 循环 `4 - 6` 步

## Known Issues
1. 所有答案重复的都只能选到第一个，后面的要手动点选
2. 非正常退出后需要手动修改 `final.txt`
3. **在答案匹配错误后会阻塞后面命令运行，在多页测试时可以先做第二页删掉命令后再做第一页**
3. 部分题目对不上 无解