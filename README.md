需求环境：
	·Debian6.1以上版本（实测6.1.27没问题，估计更低版本也没啥问题）
	·Python3.10以上版本
	·NcatBot 需要使用 3000、3001、6099 三个端口, 请确保你的服务器以及系统均已经放通了这三个端口.
	·Debian/Ubuntu 系统通常预装了 UFW, 但默认未启用. 如果未安装，可以通过以下命令安装:
		·sudo apt update
		·sudo apt install ufw
		·sudo ufw status
		·sudo ufw disable
		·sudo ufw allow 3000/tcp
		·sudo ufw allow 3001/tcp
		·sudo ufw allow 6099/tcp
	·pip 安装工具：
		·sudo apt install pip
		`sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.bk
		`这里需要把3.11换成实际安装的Python版本
	·img2pdf 插件
		·pip install img2pdf
	·curl 工具
		·sudo apt install curl
准备安装：
	·pip install ncatbot -U -i https://mirrors.aliyun.com/pypi/simple
		#安装ncatbot
	·pip install git+https://github.com/hect0x7/JMComic-Crawler-Python
		#安装jmcomic项目
配置脚本：
	·修改main.py中的bot_id为你实际申请的QQ小号的账号
	·将main.py和option.yml一起放入服务器root目录下
启动脚本：
	·python3 main.py
		#直接启动，初次运行会自动下载NapCatQQ框架，如果有提示的话无脑输入Y回车就好
	·现在可以用注册的bot账号的好友给bot账号发送 / 加想要下载的jm代码获取对应的本子
		#示例： /422866
	·群聊的话得先@bot账号再加上 / 和想要下载的jm代码即可
		#示例： @bot /422866
