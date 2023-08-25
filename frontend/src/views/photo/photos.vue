<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { getAllPhotosByAlbumId } from "@/api/photo";

const route = useRoute();
const photoList = ref([]);
const loading = ref(false);

const pageGetPhotos = async (id) => {
  loading.value = true;
  let res = await getAllPhotosByAlbumId(id);
  if (res.code == 0) {
    photoList.value = res.result;
    loading.value = false;
  }
};

onMounted(() => {
  if (route.query.id) {
    pageGetPhotos(Number(route.query.id));
  }
});
</script>

<template>
  <PageHeader :bgUrl="route.query.bg" />
  <div class="photoList">
    <el-row class="center_box">
      <el-col :span="24">
        <el-card class="photoList-card">
          <el-row v-if="loading" class="row-space">
            <el-col class="col-space" :xs="12" :sm="6" v-for="(item, index) in 8" :key="index">
              <div class="image-box image">
                <el-skeleton :rows="1" animated> </el-skeleton>
              </div>
            </el-col>
          </el-row>
          <el-row v-else="photoList.length" class="row-space">
            <el-col class="col-space" :xs="12" :sm="6" v-for="(item, index) in photoList" :key="index">
              <div v-image :data-src="item.url" class="image-box flex_center animate__animated animate__fadeIn">
                <el-image class="image" :src="item.url" fit="cover" lazy preview-teleported :initial-index="index" :preview-src-list="photoList.map((v) => v.url)">
                  <template #error>
                    <svg-icon name="image" :width="8" :height="6"></svg-icon>
                  </template>
                </el-image>
              </div>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<style lang="scss" scoped>
.photoList {
  .photoList-card {
    padding: 10px;
    min-height: 8rem;
  }

  .image-box {
    width: 100%;
    height: 100%;
  }

  .image {
    vertical-align: middle;
    cursor: pointer;
    width: 100%;
    object-fit: cover;
  }
}

.row-space {
  padding: 0 !important;
}

.col-space {
  padding: 1px !important;
}

@media screen and (min-width: 769px) {
  .image {
    height: 10rem;
  }
}

@media screen and (max-width: 768px) {
  .image {
    height: 8rem;
  }
}
</style>
