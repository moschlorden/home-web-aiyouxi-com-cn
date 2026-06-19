from typing import List, Dict, Any
import json


def load_site_profiles() -> List[Dict[str, Any]]:
    """
    加载内置站点资料列表，每条记录包含关键词、URL、标签和简短说明。
    """
    return [
        {
            "keywords": ["爱游戏", "游戏门户", "娱乐平台"],
            "url": "https://home-web-aiyouxi.com.cn",
            "tags": ["游戏", "门户", "娱乐"],
            "description": "爱游戏综合门户，提供最新游戏资讯、评测与社区互动。"
        },
        {
            "keywords": ["单机游戏", "经典游戏", "怀旧"],
            "url": "https://classicgames.example.com",
            "tags": ["单机", "怀旧", "经典"],
            "description": "怀旧单机游戏资料站，收录大量经典作品介绍与攻略。"
        },
        {
            "keywords": ["手游", "手机游戏", "移动游戏"],
            "url": "https://mobilegames.example.com",
            "tags": ["手游", "移动端", "推荐"],
            "description": "手机游戏推荐平台，每日更新热门手游榜单与评测。"
        },
        {
            "keywords": ["电竞", "电子竞技", "赛事"],
            "url": "https://esports.example.com",
            "tags": ["电竞", "赛事", "直播"],
            "description": "电子竞技资讯站，涵盖LOL、DOTA2、CS2等赛事报道。"
        }
    ]


def format_site_summary(profile: Dict[str, Any], index: int) -> str:
    """
    将单个站点资料格式化为一条结构化的摘要字符串。
    """
    kw_str = "、".join(profile["keywords"])
    tag_str = "，".join(f"#{tag}" for tag in profile["tags"])
    lines = [
        f"站点 {index + 1}：",
        f"  关键词：{kw_str}",
        f"  URL：{profile['url']}",
        f"  标签：{tag_str}",
        f"  说明：{profile['description']}"
    ]
    return "\n".join(lines)


def generate_full_summary(sites: List[Dict[str, Any]]) -> str:
    """
    根据所有站点资料生成完整的结构化摘要。
    """
    header = "【站点资料结构化摘要】\n"
    separator = "-" * 48
    parts = [header, separator]
    for idx, site in enumerate(sites):
        block = format_site_summary(site, idx)
        parts.append(block)
        parts.append(separator)
    footer = f"\n摘要共包含 {len(sites)} 个站点。"
    parts.append(footer)
    return "\n".join(parts)


def export_summary_to_json(sites: List[Dict[str, Any]], indent: int = 2) -> str:
    """
    将站点资料列表序列化为格式化的JSON字符串。
    """
    return json.dumps(sites, ensure_ascii=False, indent=indent)


def main() -> None:
    """
    主流程：加载资料，打印纯文本摘要，并输出JSON表示。
    """
    profiles = load_site_profiles()
    summary_text = generate_full_summary(profiles)
    print(summary_text)
    print("\n--- JSON 表示 ---")
    print(export_summary_to_json(profiles))


if __name__ == "__main__":
    main()