<!--
* @Author: Zhang Yuming
* @Date: 2023-07-03 11:35:38
* @Description: 播放器首页
-->
<script setup>
import MusicList from "./list/index.vue";
import MusicControl from "./controls/index.vue";
import { defineComponent, ref } from "vue";

import { music } from "@/store/index";
import { storeToRefs } from "pinia";

const musicStore = music();
const { getIsShow, getIsPaused, getIsToggleImg } = storeToRefs(musicStore);

defineComponent({
  name: "MusicPlayer",
});

// 页面初始化播放器隐藏的时候不要做动画
const clickFlag = ref(false);

const toggleDisc = () => {
  musicStore.setIsShow();
  if (!clickFlag.value) {
    clickFlag.value = true;
  }
};
</script>

<template>
  <div :class="['music', getIsShow ? 'show-music' : '', !getIsShow && clickFlag ? 'hide-music' : '']">
    <div class="p-[10px]">
      <i class="iconfont icon-off-search change-color" @click="toggleDisc"></i>
      <!-- 播放器列表 -->
      <MusicList class="list" />
      <!-- 播放器控制器 -->
      <MusicControl :autoplay="false" class="control" />
    </div>
  </div>
  <svg-icon :class="['music-disc', getIsToggleImg ? '' : 'disc-rotate', getIsPaused ? 'paused' : '']" name="disc" width="5rem" @click="toggleDisc"></svg-icon>
</template>

<style lang="scss" scoped>
.music {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fafafa;
  border-radius: 8px;
  z-index: 2000;
  transform: translateX(-2000px);
  opacity: 0;

  .list {
    max-width: 1080px;
  }

  .control {
    max-width: 1080px;
  }
}

.icon-off-search {
  position: absolute;
  top: 70px;
  right: 30px;
  font-size: 1.4rem;
  z-index: 3001;
}

.show-music {
  animation: showPlayer 0.3s ease-in-out forwards;
}

.hide-music {
  animation: hidePlayer 0.4s ease-in-out forwards;
}

.music-disc {
  position: fixed;
  bottom: 50px;
  left: -30px;
  transition: all 0.3s;
  z-index: 3002;
  &:hover {
    left: 2px;
  }
}

.change-color:hover {
  cursor: pointer;
  color: #62c28a;
}

.disc-rotate {
  animation: rotate360 18s infinite linear;
}

.paused {
  animation-play-state: paused;
}

// mobile
@media screen and (max-width: 768px) {
  .show-music {
    animation: mShowPlayer 0.3s ease-in-out forwards;
  }

  .hide-music {
    animation: mHidePlayer 0.4s ease-in-out forwards;
  }
}

@keyframes showPlayer {
  0% {
    transform: translateX(-2000px);
    opacity: 0.7;
  }

  100% {
    transform: translateX(0px);
    opacity: 1;
  }
}

@keyframes hidePlayer {
  0% {
    transform: translateX(0px);
    opacity: 1;
  }

  100% {
    transform: translateX(-2000px);
    opacity: 0;
  }
}

@keyframes mShowPlayer {
  0% {
    transform: translateX(-1000px);
    opacity: 0.7;
  }

  100% {
    transform: translateX(0px);
    opacity: 1;
  }
}

@keyframes mHidePlayer {
  0% {
    transform: translateX(0px);
    opacity: 1;
  }

  100% {
    transform: translateX(-1000px);
    opacity: 0;
  }
}

@keyframes rotate360 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
