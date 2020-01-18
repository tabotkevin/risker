<template>
  <div class="landing">
    <div class="container">
    <img src="../assets/logo.png" alt="Logo" class="center">
    </div>
  </div>
</template>

<script>

export default {
  name: 'hello'
}
</script>


<style scoped>

.center {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%)
}
</style>
