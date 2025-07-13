需求环境：  
    &emsp;·Debian6.1以上版本（实测6.1.27没问题，估计更低版本也没啥问题）  
    &emsp;·Python3.10以上版本  
    &emsp;·NcatBot 需要使用 3000、3001、6099 三个端口, 请确保你的服务器以及系统均已经放通了这三个端口.  
    &emsp;·Debian/Ubuntu 系统通常预装了 UFW, 但默认未启用. 如果未安装，可以通过以下命令安装:  
        &emsp;&emsp;·sudo apt update  
        &emsp;&emsp;·sudo apt install ufw  
        &emsp;&emsp;·sudo ufw status  
        &emsp;&emsp;·sudo ufw disable  
        &emsp;&emsp;·sudo ufw allow 3000/tcp  
        &emsp;&emsp;·sudo ufw allow 3001/tcp  
        &emsp;&emsp;·sudo ufw allow 6099/tcp  
	&emsp;·pip 安装工具：  
		&emsp;&emsp;·sudo apt install pip  
		&emsp;&emsp;·sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.bk  
		&emsp;&emsp;·这里需要把3.11换成实际安装的Python版本  
	&emsp;·img2pdf 插件  
		&emsp;&emsp;·pip install img2pdf  
	&emsp;·curl 工具  
		&emsp;&emsp;·sudo apt install curl  
准备安装：  
	&emsp;·pip install ncatbot -U -i https://mirrors.aliyun.com/pypi/simple  
		&emsp;&emsp;#安装ncatbot  
	&emsp;·pip install git+https://github.com/hect0x7/JMComic-Crawler-Python  
		&emsp;&emsp;#安装jmcomic项目  
配置脚本：  
	&emsp;·修改main.py中的bot_id为你实际申请的QQ小号的账号  
	&emsp;·将main.py和option.yml一起放入服务器root目录下  
启动脚本：   
	&emsp;·python3 main.py  
		&emsp;&emsp;#直接启动，初次运行会自动下载NapCatQQ框架，如果有提示的话无脑输入Y回车就好  
	        &emsp;&emsp;·现在可以用注册的bot账号的好友给bot账号发送 / 加想要下载的jm代码获取对应的本子  
		&emsp;&emsp;#示例： /422866  
	        &emsp;&emsp;·群聊的话得先@bot账号再加上 / 和想要下载的jm代码即可  
		&emsp;&emsp;#示例： @bot /422866  
