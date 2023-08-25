<template>
  <div :class="[backTopShow ? 'back-top-show' : 'back-top-hidden', 'back-top']" :style="`bottom: ${backTopProps.bottom};right:${backTopProps.right};height: ${backTopProps.width};width:${backTopProps.width};`">
    <svg-icon :style="{ transform: `rotateZ(${props.rotateDeg}deg)` }" :name="svgThemeName" :width="svgWidth" @click="scrollToTop"></svg-icon>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive, watch, computed } from "vue";
import { useRoute } from "vue-router";
import { storeToRefs } from "pinia";
import { staticData } from "@/store/index.js";

const { mainTheme } = storeToRefs(staticData());

const route = useRoute();
const props = defineProps({
  bottom: {
    type: [String, Number],
    default: "100px",
  },
  right: {
    type: [String, Number],
    default: "0px",
  },
  // 图标
  svgName: {
    type: String,
    default: "Rocket",
  },
  svgWidth: {
    type: Number,
    default: 6,
  },
  animation: {
    type: Boolean,
    default: true,
  },
  rotateDeg: {
    type: Number,
    default: 0,
  },
});

const backTopProps = reactive({
  bottom: "",
  right: "",
  width: "",
});

watch(
  () => props,
  (newV) => {
    backTopProps.bottom = /^[\d|.]*$/g.test(props.bottom) ? props.bottom + "rem" : props.bottom;
    backTopProps.right = /^[\d|.]*$/g.test(props.right) ? props.right + "rem" : props.right;
  },
  {
    immediate: true,
    deep: true,
  }
);

const svgThemeName = computed(() => {
  return mainTheme.value ? "dark" + props.svgName : "light" + props.svgName;
});

onMounted(() => {
  // 注册滚动
  window.addEventListener("scroll", scroll);
});
const backTopShow = ref(false);
const scroll = () => {
  let scrollTop = ref(0);
  scrollTop.value = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
  if (scrollTop.value > 200) {
    // 大于200显示
    backTopShow.value = true;
  } else {
    backTopShow.value = false;
  }
};

const scrollToTop = () => {
  const c = document.documentElement.scrollTop || document.body.scrollTop;
  if (c > 0) {
    const duration = 600;
    const startTime = Date.now();
    // 图片页面不适合动画滚动
    if (route.path != "/photos") {
      return new Promise((res) => {
        const fnc = () => {
          const timestamp = Date.now();
          const time = timestamp - startTime;
          const nextScrollTop = easeInOut(Math.min(time, duration), c, 0, duration);
          window.scrollTo(0, nextScrollTop);
          if (time < duration) {
            window.requestAnimationFrame(fnc); // 动画函数
          } else {
            // 由于上面步骤设置了scrollTop, 滚动事件可能未触发完毕
            // 此时应该在下一帧再执行res
            window.requestAnimationFrame(res);
          }
        };
        window.requestAnimationFrame(fnc);
      });
    } else {
      const fnc = () => {
        window.scrollTo(0, 0);
      };
      window.requestAnimationFrame(fnc);
    }
  }
};
const easeInOut = (current, start, end, duration) => {
  const change = (end - start) / 2;
  let time = current / (duration / 2);
  if (time < 1) {
    return change * time * time * time + start;
  }
  time -= 2;
  return change * (time * time * time + 2) + start;
};
</script>
<style lang="scss" scoped>
.back-top {
  position: fixed;
  overflow: hidden;
  transition: all ease-in-out 0.3s;
  &-show {
    animation: show 0.8s ease-in-out forwards;
  }
  &-hidden {
    animation: hide 0.8s ease-in-out forwards;
  }
}
@keyframes show {
  0% {
    transform: translateX(0);
    transform: translateY(100px);
    opacity: 0;
  }

  80% {
    transform: translateY(0px);
    opacity: 1;
  }
}

@keyframes hide {
  0% {
    opacity: 1;
    transform: translateX(0px);
  }

  80% {
    opacity: 0;
    transform: translateY(300px);
  }

  100% {
    transform: translateX(300px);
  }
}
</style>
