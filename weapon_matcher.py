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
    
    def filter_weapons(
        self,
        substrate_base: str = None,
        substrate_additional: str = None,
        substrate_skill: str = None
    ) -> List[Dict]:
        """
        根据指定属性筛选武器，未指定的属性将不作为筛选条件
        
        Args:
            substrate_base: 基础属性（可选）
            substrate_additional: 附加属性（可选）
            substrate_skill: 技能属性（可选）
        
        Returns:
            返回符合条件的武器列表
        """
        filtered = self.weapons
        
        if substrate_base:
            filtered = [w for w in filtered if w['base_attribute'] == substrate_base]
        if substrate_additional:
            filtered = [w for w in filtered if w['additional_attribute'] == substrate_additional]
        if substrate_skill:
            filtered = [w for w in filtered if w['skill_attribute'] == substrate_skill]
        
        return [{
            'name': w['name'],
            'stars': w['stars'],
            'type': w['type']
        } for w in filtered]
        self, 
        substrate_base: str, 
        substrate_additional: str, 
        substrate_skill: str
    ) -> List[Dict]:
        """
        根据基质的三种属性查找所有完美匹配的武器
        
        Args:
            substrate_base: 基质的基础属性
            substrate_additional: 基质的附加属性
            substrate_skill: 基质的技能属性
        
        Returns:
            返回包含所有匹配武器信息的列表；如果没有匹配则返回空列表
        """
        matching_weapons = []
        for weapon in self.weapons:
            if (weapon['base_attribute'] == substrate_base and 
                weapon['additional_attribute'] == substrate_additional and 
                weapon['skill_attribute'] == substrate_skill):
                matching_weapons.append({
                    'name': weapon['name'],
                    'stars': weapon['stars'],
                    'type': weapon['type']
                })
        return matching_weapons
    
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
        results = self.filter_weapons(substrate_base, substrate_additional, substrate_skill)
        
        if results:
            if len(results) == 1:
                return f"武器名称: {results[0]['name']}\n星级: {results[0]['stars']}\n类型: {results[0]['type']}"
            else:
                output = f"找到 {len(results)} 个匹配的武器:\n" + "="*30 + "\n"
                for i, weapon in enumerate(results, 1):
                    output += f"\n武器 {i}:\n"
                    output += f"  名称: {weapon['name']}\n"
                    output += f"  星级: {weapon['stars']}\n"
                    output += f"  类型: {weapon['type']}\n"
                return output
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
