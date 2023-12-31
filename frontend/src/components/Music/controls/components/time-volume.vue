<!--
* @Author: Zhang Yuming
* @Date: 2023-07-03 11:48:49
* @Description: 展示音量、进度等 后续可能加随机播放等
-->
<script setup>
import { defineComponent, ref, watch } from "vue";
import { music } from "@/store/index";
import { storeToRefs } from "pinia";
import { MODELLIST } from "@/utils/enum";
import CustomMusicList from "../../list/custom-music-list.vue";

const musicStore = music();
const { getPlayModel, getVolume } = storeToRefs(musicStore);

defineComponent({
  name: "TimeVolume",
});

const playModel = {
  RANDOM: "icon-suijibofang",
  LISTLOOP: "icon-liebiaoxunhuan",
  SINGLECYCLE: "icon-danquxunhuan",
};

const emits = defineEmits(["update:volume"]);

const props = defineProps({
  // 当前播放时长
  currentTime: {
    type: String,
    default: "00:00",
  },
  // 总的播放时长
  duration: {
    type: String,
    default: "00:00",
  },
});

const currentVolume = ref(0);
const elPopoverRef = ref();
// 切换音乐播放模式
const changeModel = () => {
  let index = MODELLIST.findIndex((item) => item == getPlayModel.value);
  if (index != -1) {
    if (index == 2) {
      index = 0;
    } else {
      index = index + 1;
    }
  }
  musicStore.setPlayModel(MODELLIST[index]);
};

// 手动关闭popover
const closePopover = () => {
  elPopoverRef.value.hide();
};

watch(
  () => getVolume.value,
  (newV) => {
    // 根据pina存的声音来改变播放器声音大小
    currentVolume.value = newV;
  },
  {
    immediate: true,
  }
);
watch(
  () => currentVolume.value,
  () => {
    // 修改音乐大小 外面会根据音乐大小去调节音乐播放器的声音大小
    musicStore.setVolume(currentVolume.value);
  }
);
</script>

<template>
  <div class="time-volume">
    <!-- 音乐模式 -->
    <i :class="['change-color', 'iconfont', playModel[getPlayModel]]" @click="changeModel"></i>
    <!-- 时间显示 -->
    <span class="time">{{ currentTime }} / {{ duration }}</span>
    <!-- 音量调节 -->
    <el-popover placement="top" trigger="click" :width="40">
      <template #reference>
        <i class="iconfont icon-yinliang change-color"> </i>
      </template>
      <template #default>
        <el-slider v-model="currentVolume" :show-tooltip="false" vertical height="60px" />
      </template>
    </el-popover>
    <!-- 歌曲列表 -->
    <el-popover ref="elPopoverRef" placement="top" :width="400" :show-arrow="false" :teleported="false" trigger="click" @touchmove.native.stop.prevent>
      <template #reference>
        <i class="iconfont icon-bofangliebiao change-color"></i>
      </template>
      <div class="pop">
        <i class="iconfont icon-off-search" @click="closePopover"></i>
        <CustomMusicList />
      </div>
    </el-popover>
  </div>
</template>

<style lang="scss" scoped>
.time-volume {
  position: relative;
  width: 120px;
  display: flex;
  justify-content: space-around;
  align-items: center;

  .time {
    font-size: 1rem;
  }
}
.volume {
  position: absolute;
  top: -22px;
  right: -8px;
}
.icon-yinliang {
  font-size: 1.6rem;
}

.change-color:hover {
  cursor: pointer;
  color: #62c28a;
}

.pop {
  position: relative;
  .icon-off-search {
    position: absolute;
    top: 0px;
    right: 10px;
    font-size: 1.2rem;
    color: var(--top);
    cursor: pointer;
    z-index: 3001;

    &:hover {
      transform: scale(1.1);
      color: var(--hot-color);
    }
  }
}

// mobile
@media screen and (max-width: 768px) {
  .icon-yinliang {
    display: none;
  }
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
