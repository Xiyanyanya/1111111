from ncatbot.core import BotClient, GroupMessage, PrivateMessage
from ncatbot.utils import get_log
import jmcomic  # 确保已安装
import re
import asyncio
import os
import time
 
# ========== 初始化 ==========
bot = BotClient()
_log = get_log()
bot_id = Your QQ Account

# 加载配置文件（确保路径正确）
try:
    option = jmcomic.create_option_by_file('./option.yml')
except FileNotFoundError:
    _log.error("配置文件 option.yml 未找到，请检查路径！")
    option = None  # 或使用默认配置
 
# ========= 定时清理 ==========
async def delete_old_files(directory, minutes=30):
    """
    删除指定目录中超过指定分钟数的文件
    :param directory: 要监控的目录路径
    :param minutes: 文件存活时间（默认30分钟）
    """
    while True:
        current_time = time.time()  # 当前时间戳
        cutoff_time = current_time - (minutes * 60)  # 计算截止时间（30分钟前）
     
        for root, dirs, files in os.walk(directory, topdown=False):
            # 先处理文件
            for file in files:
                file_path = os.path.join(root, file)
                file_time = os.path.getmtime(file_path)
                if file_time < cutoff_time:
                    try:
                        os.remove(file_path)
                        _log.info(f"已删除文件: {file_path}")
                    except Exception as e:
                        _log.error(f"删除文件失败 {file_path}: {e}")
     
            # 再处理目录（检查是否为空）
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                dir_time = os.path.getmtime(dir_path)
                
                # 如果目录为空或超过截止时间，则删除
                if not os.listdir(dir_path) or dir_time < cutoff_time:
                    try:
                        os.rmdir(dir_path)  # 只能删除空目录
                        _log.info(f"已删除空目录: {dir_path}")
                    except Exception as e:
                        _log.error(f"删除目录失败 {dir_path}: {e}")
        
        asyncio.sleep(minutes*60)
 
# ========= 回调函数 ==========
async def handle_message(msg):
    """统一处理群聊和私聊消息"""
    #_log.info(msg)
    global bot_id
    
    _log.info(f"收到消息: {msg.raw_message} (来自: {msg.sender.user_id})")
    
    ##群聊如果没有at自己则不做回复
    if msg.message_type == "group" and not msg.raw_message.startswith(f"[CQ:at,qq={bot_id}]"):
        return
 
    pattern = r'/(\d+)'
    match = re.search(pattern, msg.raw_message)
    print(match)
 
    if match and option:
        album_id = match.group(1)
        filepath = "/root/JMComic/" + album_id + ".pdf"
        try:
            jmcomic.download_album(album_id, option)
            await msg.reply(text="NcatBot 下载成功喵~")
        except Exception as e:
            _log.error(f"下载失败: {e}")
            await msg.reply(text=f"NcatBot 下载失败nia(Ｔ▽Ｔ)，请查看日志")
    else:
        await msg.reply(text="NcatBot 输入不合法喵~\n请输入 /+本子id")
 
    try:
        if msg.message_type == "private":
            _log.info(f"{msg.sender.user_id} + {filepath}")
            await bot.api.post_private_file(msg.sender.user_id, file = filepath)
        else:
            _log.info(f"{msg.group_id} + {filepath}")
            await bot.api.post_group_file(msg.group_id, file = filepath)
    except Exception as e:
        _log.error(f"上传失败： {e}")
        await msg.reply(text=f"NcatBot 上传失败惹(Ｔ▽Ｔ)\n{e}")

# 注册事件监听
@bot.group_event()
async def on_group_message(msg: GroupMessage):
    await handle_message(msg)
 
@bot.private_event()
async def on_private_message(msg: PrivateMessage):
    await handle_message(msg)
 
# ========== 启动 Bot ==========
if __name__ == "__main__":
    delete_old_files("/root/JMComic/")
    bot.run(bt_uin = bot_id)  # 替换为你的 Bot QQ 号
