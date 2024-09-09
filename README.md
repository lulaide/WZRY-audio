# 王者荣耀语音数据集

## 项目简介

本项目基于王者荣耀官网 [pvp.qq.com](https://pvp.qq.com) 通过抓包获取英雄语音数据。我使用了王者荣耀官网提供的英雄列表接口和语音文件接口，抓取并整理了所有英雄的语音，形成了一个语音数据集，我已制作好适用于GPT-Sovits的list文件。

数据集包含每个英雄的语音信息，能够应用于语音识别、语音合成、情感分析、语音分类等相关的研究和开发中。

### 数据来源

1. **英雄列表接口**：`https://pvp.qq.com/zlkdatasys/yuzhouzhan/list/heroList.json`
   - 此接口返回的是王者荣耀中的英雄列表及其相关信息。
   
2. **语音接口**：`https://pvp.qq.com/zlkdatasys/yuzhouzhan/herovoice/{hero_id}.json`
   - 该接口用于获取每个英雄的语音信息，`{hero_id}` 代表英雄的唯一标识符。

## 数据结构

数据集的结构基于英雄的语音文件，按照英雄和皮肤分类。对于每个英雄，语音数据都保存在一个以英雄ID命名的文件夹中，每个文件夹中包含以下内容：

```
/dataset/
    /hero_name_1/
        /skin_name_1/
            voice_1.mp3
            hero-skin.list
        ...
    /hero_name_2/
        /skin_name_1/
            voice_1.mp3
            hero-skin.list
        ...
    ...
```

## 使用脚本获取音频
- 克隆项目
```bash
git clone https://github.com/lulaide/WZRY-audio.git
```
- 进入文件夹
```bash
cd WZRY-audio
```
- 运行`fetch.py`

```bash
python fetch.py
```

## 许可证

请注意，抓取和使用王者荣耀官网的资源需要遵守其服务条款和版权规定。此数据集仅供学习和研究使用，禁止用于商业用途。王者荣耀及其语音资源的版权归腾讯公司所有。

## 致谢

感谢腾讯公司提供的王者荣耀官方网站 [pvp.qq.com](https://pvp.qq.com) 以及相应的语音资源。

---

### 注意事项

1. **数据的更新**：王者荣耀官网可能会定期更新英雄的语音数据，因此需要定期通过接口重新抓取以确保数据的时效性。
2. **合法使用**：确保你在使用数据集时遵守了相关的版权和法律规定。
3. **文件完整性**：下载语音文件时，建议对下载的数据进行校验，确保文件完整无损。

---
