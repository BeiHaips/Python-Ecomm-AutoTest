<template>
  <div class="product-card">
    <img :src="product.image" :alt="product.name" class="product-img">
    <h3 class="product-name">{{ product.name }}</h3>
    <p class="product-price">￥{{ product.price }}</p>
    <button @click="addToCart(product.id)" class="buy-btn">加入购物车</button>
  </div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: ['product'], // 接收父组件传递的商品数据
  methods: {
    addToCart(id) {
      console.log(`商品 ID: ${id} 已加入购物车`);
      this.$emit('add-success', id); // 向上通信
    }
  }
}
</script>

<style scoped>
.product-card { border: 1px solid #eee; padding: 10px; border-radius: 8px; text-align: center; }
.product-img { width: 100%; height: auto; }
.product-price { color: #ff4400; font-weight: bold; }
.buy-btn { background: #007bff; color: white; border: none; padding: 5px 15px; border-radius: 4px; cursor: pointer; }
</style>