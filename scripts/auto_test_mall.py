import unittest
import time

# 模拟商城核心业务逻辑类
class MallSystem:
    def __init__(self):
        self.inventory = {"iPhone 15": 50, "Mate 60": 30}
        self.login_status = False

    def login(self, user, pwd):
        if user == "admin" and pwd == "123456":
            self.login_status = True
            return True
        return False

    def create_order(self, item_name, quantity):
        if not self.login_status:
            return "Error: Please Login First"
        if self.inventory.get(item_name, 0) >= quantity:
            self.inventory[item_name] -= quantity
            return "Success"
        return "Error: Low Stock"

# 编写自动化测试用例 (CARL: Action)
class TestMallWorkflow(unittest.TestCase):
    def setUp(self):
        self.mall = MallSystem()

    def test_login_and_order_flow(self):
        """测试路径：登录 -> 下单 -> 检查库存"""
        # 1. 模拟登录
        self.assertTrue(self.mall.login("admin", "123456"))
        
        # 2. 模拟下单支付
        result = self.mall.create_order("iPhone 15", 1)
        self.assertEqual(result, "Success")
        
        # 3. 验证库存是否正确扣减
        self.assertEqual(self.mall.inventory["iPhone 15"], 49)

    def test_unauthorized_order(self):
        """边界测试：未登录状态下单"""
        result = self.mall.create_order("Mate 60", 1)
        self.assertIn("Error", result)

if __name__ == "__main__":
    unittest.main()