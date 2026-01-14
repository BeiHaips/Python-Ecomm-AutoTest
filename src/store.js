// 模拟简单的状态管理逻辑
export const store = {
  state: {
    cart: [],
    products: [
      { id: 1, name: 'iPhone 15', price: 5999, image: 'phone1.jpg' },
      { id: 2, name: 'Mate 60', price: 6999, image: 'phone2.jpg' }
    ]
  },
  // 模拟加入购物车动作
  addToCart(productId) {
    const item = this.state.products.find(p => p.id === productId);
    if (item) {
      this.state.cart.push(item);
      console.log(`成功将 ${item.name} 加入购物车，当前件数：${this.state.cart.length}`);
    }
  }
};