import os
import requests

# 基本配置
base_url = "https://pvp.qq.com/zlkdatasys/yuzhouzhan/"
hero_list_url = base_url + "list/heroList.json"
hero_voice_url_template = base_url + "herovoice/{}.json"

def fetch_heroes_list():
    try:
        response = requests.get(hero_list_url)
        response.raise_for_status()  # 检查请求是否成功
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch hero list: {e}")
        return {}

def process_hero(hero_name, hero_id):
    print(f"Processing hero: {hero_name} (ID: {hero_id})")
    
    # 创建英雄目录
    hero_dir = os.path.join("dataset", hero_name)
    os.makedirs(hero_dir, exist_ok=True)
    
    # 获取英雄语音数据
    hero_voice_url = hero_voice_url_template.format(hero_id)
    try:
        response_voice = requests.get(hero_voice_url)
        response_voice.raise_for_status()  # 检查请求是否成功
        voice_data = response_voice.json()
    except requests.RequestException as e:
        print(f"Failed to get voice data for hero {hero_name}: {e}")
        return
    
    # 处理语音数据
    dqpfyy_data = voice_data.get("dqpfyy_5403", [])
    
    if not isinstance(dqpfyy_data, list):
        print(f"Unexpected data format for hero {hero_name}: {dqpfyy_data}")
        return
    
    for skin in dqpfyy_data:
        if not isinstance(skin, dict):
            print(f"Unexpected skin format for hero {hero_name}: {skin}")
            continue
        
        skin_name = skin.get("pfmczt_7754", "UnknownSkin")
        print(f"  Processing skin: {skin_name}")
        
        skin_dir = os.path.join(hero_dir, skin_name)
        os.makedirs(skin_dir, exist_ok=True)
        
        list_file_path = os.path.join(skin_dir, f"{hero_name}-{skin_name}.list")
        with open(list_file_path, "w", encoding="utf-8") as list_file:
            voice_entries = skin.get("yylbzt_9132", [])
            num_voices = len(voice_entries)
            print(f"    Found {num_voices} voices for skin {skin_name}")
            
            for idx, voice in enumerate(voice_entries, start=1):
                if not isinstance(voice, dict):
                    print(f"  Unexpected voice format for hero {hero_name}, skin {skin_name}: {voice}")
                    continue
                
                voice_text = voice.get("yywbzt_1517", "UnknownText")
                voice_url = "https:" + voice.get("yywjzt_5304", "")
                
                # 下载音频文件
                if voice_url:
                    try:
                        audio_response = requests.get(voice_url)
                        audio_response.raise_for_status()  # 检查请求是否成功
                        audio_filename = f"{hero_name}_{skin_name}_{idx}.mp3"
                        audio_path = os.path.join(skin_dir, audio_filename)
                        
                        with open(audio_path, "wb") as audio_file:
                            audio_file.write(audio_response.content)
                        
                        # 写入list文件
                        list_file.write(f"{audio_filename}|{hero_name}|ZH|{voice_text}\n")
                    except requests.RequestException as e:
                        print(f"    Failed to download audio for {hero_name}, skin {skin_name} (Index: {idx}): {e}")
                        continue

def main():
    print("Fetching hero list...")
    heroes_data = fetch_heroes_list()
    if not heroes_data:
        print("No heroes data available.")
        return
    
    # 遍历每个英雄获取详细信息
    for hero_list in heroes_data.values():
        for hero in hero_list:
            hero_name = hero.get("yzzyxm_4588", "UnknownHero")
            hero_id = hero.get("yzzyxi_2602", "UnknownID")
            process_hero(hero_name, hero_id)

if __name__ == "__main__":
    main()