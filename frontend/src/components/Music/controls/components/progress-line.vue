<!--
* @Author: Zhang Yuming
* @Date: 2023-07-03 11:48:31
* @Description: 音乐进度组件
-->
<script setup>
import { ref, watch, defineComponent } from "vue";
import { music } from "@/store/index";

defineComponent({
  name: "ProgressLine",
});

const musicStore = music();

// 暴露出进度变化事件
const emits = defineEmits(["scheduleChange"]);

const props = defineProps({
  schedule: {
    // 进度
    type: Number,
    default: 0,
  },
});

const currentSchedule = ref(0);

const handleChange = () => {
  // 修改pina里的当前播放进度 统一状态管理
  musicStore.setCurrentSchedule(currentSchedule.value);
  // 通知父组件 当前播放进度改变了
  emits("scheduleChange");
};

watch(
  () => props.schedule,
  (newV) => {
    currentSchedule.value = newV;
  },
  {
    immediate: true,
  }
);
</script>

<template>
  <div ref="musicRef" class="music-line">
    <el-slider v-model="currentSchedule" :step="0.1" :show-tooltip="false" @change="handleChange" />
  </div>
</template>

<style lang="scss" scoped>
.music-line {
  width: 100%;
}

:deep(.el-slider__bar) {
  background-color: #62bf82;
}

:deep(.el-slider__button) {
  width: 8px;
  height: 8px;
  border: solid 2px #62bf82;
}

:deep(.el-slider.is-vertical .el-slider__runway) {
  width: 4px;
  margin: 0;
}

:deep(.el-slider.is-vertical .el-slider__button-wrapper) {
  left: -16px;
}

:deep(.el-slider.is-vertical .el-slider__bar) {
  width: 4px;
}
</style>
