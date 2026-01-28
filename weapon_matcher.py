import json
from typing import Dict, List, Optional, Tuple

class WeaponMatcher:
    def __init__(self, weapons_file: str):
        """
        初始化武器匹配器
        
        Args:
            weapons_file: 武器数据JSON文件路径
        """
        with open(weapons_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.weapons = data['weapons']
    
    def find_matching_weapon(
        self, 
        substrate_base: str, 
        substrate_additional: str, 
        substrate_skill: str
    ) -> Optional[Dict]:
        """
        根据基质的三种属性查找完美匹配的武器
        
        Args:
            substrate_base: 基质的基础属性
            substrate_additional: 基质的附加属性
            substrate_skill: 基质的技能属性
        
        Returns:
            如果找到完美匹配，返回包含武器信息的字典；否则返回None
        """
        for weapon in self.weapons:
            if (weapon['base_attribute'] == substrate_base and 
                weapon['additional_attribute'] == substrate_additional and 
                weapon['skill_attribute'] == substrate_skill):
                return {
                    'name': weapon['name'],
                    'stars': weapon['stars'],
                    'type': weapon['type']
                }
        return None
    
    def match_substrate(
        self, 
        substrate_base: str, 
        substrate_additional: str, 
        substrate_skill: str
    ) -> str:
        """
        匹配基质并返回结果字符串
        
        Args:
            substrate_base: 基质的基础属性
            substrate_additional: 基质的附加属性
            substrate_skill: 基质的技能属性
        
        Returns:
            匹配结果字符串
        """
        result = self.find_matching_weapon(substrate_base, substrate_additional, substrate_skill)
        
        if result:
            return f"武器名称: {result['name']}\n星级: {result['stars']}\n类型: {result['type']}"
        else:
            return "很抱歉，没有对应武器"


def main():
    # 初始化匹配器
    matcher = WeaponMatcher('weapons.json')
    
    print("=" * 50)
    print("欢迎使用武器匹配系统")
    print("=" * 50)
    print("\n基础属性: 敏捷、力量、意志、智识、主能力")
    print("附加属性: 攻击、生命、物理伤害、灼热伤害、电磁伤害、寒冷伤害、")
    print("          自然伤害、暴击率、源石技艺、治疗效率、终结技效率、法术伤害")
    print("技能属性: 强攻、压制、追袭、粉碎、昂扬、巧技、残暴、附术、")
    print("          医疗、切骨、迸发、夜幕、流转、效益")
    print("\n" + "=" * 50 + "\n")
    
    while True:
        try:
            substrate_base = input("请输入基础属性: ").strip()
            substrate_additional = input("请输入附加属性: ").strip()
            substrate_skill = input("请输入技能属性: ").strip()
            
            if not substrate_base or not substrate_additional or not substrate_skill:
                print("错误：属性不能为空，请重新输入\n")
                continue
            
            print("\n" + "-" * 50)
            print(f"查询基质 - 基础属性: {substrate_base}, 附加属性: {substrate_additional}, 技能属性: {substrate_skill}")
            print("-" * 50)
            result = matcher.match_substrate(substrate_base, substrate_additional, substrate_skill)
            print(result)
            print("-" * 50 + "\n")
            
            # 询问是否继续
            continue_choice = input("是否继续查询？(y/n, 默认y): ").strip().lower()
            if continue_choice == 'n':
                print("谢谢使用！")
                break
            print()
            
        except KeyboardInterrupt:
            print("\n\n已退出程序")
            break
        except Exception as e:
            print(f"发生错误: {e}\n")


if __name__ == '__main__':
    main()
