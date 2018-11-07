# 1.模块
- 使用模块
    - 模块导入：
        - 方式1：import name
        - 方式2：import 模块 as 别名
        - 方式3：from 模块 import function_name,class_name
        - 方式4：from 模块 import *
        
        
 # 2.模块的搜索路径和存储
 - 系统默认搜索路径: 
    import sys
    sys.path
 - 添加搜索路径
    sys.path.append(dir)
 - 搜索顺序
    1.搜索内存中已经加载好的模块
    2.搜索python内置模块
    3.搜索sys.path路径
    
    
  # 3.包
  - 包的导入操作:
    - import package_name
  
 