-- 创建商城核心数据库
CREATE DATABASE IF NOT EXISTS mall_system;
USE mall_system;

-- 用户表：存储账户信息
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100)
) ENGINE=InnoDB;

-- 商品表：存储手机商城产品
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0
) ENGINE=InnoDB;

-- 插入初始化测试数据
INSERT INTO products (name, price, stock) VALUES ('iPhone 15', 5999.00, 50), ('Mate 60', 6999.00, 30);