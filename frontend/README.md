<p align="center">
  <a href="http://39.108.51.116:443/#/" target="_blank" rel="noopener noreferrer">
    <img width="180" src="https://img.shields.io/badge/%E5%B0%8F%E5%BC%A0%E7%9A%84%E5%8D%9A%E5%AE%A2-v1.0.0-lightgrey" alt="Blog logo">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/npm-v6.14.17-blue" alt="npm version">
  <a href="https://nodejs.org/en/about/releases/">
    <img src="https://img.shields.io/badge/node-v16.17.0-green" alt="node compatibility">
  </a>
  <a href="https://element-plus.gitee.io/zh-CN/">
    <img src="https://img.shields.io/badge/ElementPlus-v2.2.17-blue" alt="Element Plus">
  </a>
  <a href="https://cn.vuejs.org/">
    <img src="https://img.shields.io/badge/Vue-v3.2.13-brightgreen" alt="Vue.js">
  </a>
  <a href="https://imzbf.github.io/md-editor-v3/docs#%F0%9F%A7%B1%20toolbarsExclude">
    <img src="https://img.shields.io/badge/md--editor--v3-v2.7.2-lightgrey" alt="md-editor-v3">
  </a>
  <a href="https://pinia.web3doc.top/">
    <img src="https://img.shields.io/badge/pinia-v2.0.28-yellowgreen" alt="pinia">
  </a>
  <a href="https://router.vuejs.org/zh/guide/">
    <img src="https://img.shields.io/badge/vue--router-v4.0.3-green" alt="vue-router">
  </a>
  <a href="https://vueuse.org/">
    <img src="https://img.shields.io/badge/vueuse-v%5E9.10.0-red" alt="vue-use">
  </a>
  <a href="https://www.axios-http.cn/docs/intro">
    <img src="https://img.shields.io/badge/axios-v%5E1.2.0-blueviolet" alt="axios">
  </a>
  <a href="https://www.dowebok.com/demo/2014/98/">
    <img src="https://img.shields.io/badge/animate-v%5E4.1.1-orange" alt="animate">
  </a>
</p>

## ⚡ 简介 introduction
一个前后端分离的个人博客项目 

已适配移动端、PC端，适合新手用于学习。

#### 前台

博客前台基于 vue3、element plus、pinia、axios、vue-router、vue-cli、vue-use、npm、scss 等主流技术

前台线上预览地址：http://mrzym.top

gitee 仓库地址：https://gitee.com/mrzym/blog-v3

#### 管理后台

博客管理后台基于 pureadmin、vue3、element plus、pinia、axios、vue-router、vue-use、pnpm、vite、sass、tailwindcss 等主流技术

后台线上预览地址：http://mrzym.top/admin

gitee 仓库地址： https://gitee.com/mrzym/blog-v3-admin

测试账户: test

密码: test123

也可以自行注册用户

#### 后端：

博客后端基于node.js、koa、koa-router、koa-body、seqlize、mysql、qiniu(七牛云对象存储)、bcryptjs、nodemon等主流技术

gitee仓库地址：https://gitee.com/mrzym/blogServer

## 🚀 博客前台下载运行

```git
# npm 版本 v6.14.17
# node 版本 v16.17.0

1、下载项目
git clone https://gitee.com/mrzym/blog-v3.git
tips: 也可以下载zip打开，这样不会和我的仓库关联，也可以自己去解除关联
2、打开项目，安装依赖（安装依赖报错可以降低自己的npm版本或者网上百度解决方法，一般情况下不会有问题）
npm i
3、运行项目 
npm run serve 
```

## ✔️ 预览

#### 功能总览

| 模块     | 功能                                                         |
| -------- | ------------------------------------------------------------ |
| 首页     | 分页查看文章、展示博客网站基础信息、博客公告、博主信息等     |
| 文章详情 | 浏览文章详情，根据当前文章进行文章推荐                       |
| 标签     | 展示博客所有的标签，点击标签会搜索出当前点击标签下的文章列表 |
| 分类     | 展示博客所有的分类，点击分类会搜索出当前点击分类下的文章列表 |
| 相册     | 展示博主的所有相册                                           |
| 相册详情 | 展示相册里的所有图片（懒加载）                               |

#### 首页

#### 文章详情页

#### 搜索页面

#### 标签页面

#### 相册页面

## 🛫 期待

#### 功能开发

目前只是想尽快发布项目到线上，熟悉一下整个项目的开发流程，开发的功能还不是很多（博客前台都是一点一点的照着之前自己魔改的hexo博客手敲的，花了好多的时间）。

后续会开发在线音乐播放器、留言、友链等

优化项目的动画

尝试一些新技术，比如：tailwind.css。博客前台是一个一个类堆出来的，不仅很长还不好看，当时在写的时候也没有考虑那么多。

其实评论功能在开发的时候组件都写好了，但是某天刷到一些个人博客网站不能开评论功能的问题，所以就没有进行开发，目前主要是开发了一些自己觉得必要且实用的功能，会尽快开发在线音乐播放器、留言功能，主要是因为自己喜欢听歌。

## 🌈部署

博客文章会出一系列的部署教程

教程地址：http://mrzym.top/#/articleList?id=2&type=category&name=%E5%8D%9A%E5%AE%A2%E9%83%A8%E7%BD%B2

## 🥰感谢

感谢我所使用的这些技术框架的开发者、维护者，每一个框架、库的开发，都需要长时间的技术沉淀，充分的思考与不断地踩坑。维护开源库所需要花费的时间和精力更是常人所难以想象的。

如果大家喜欢这个项目的话，麻烦大家点个star、fork，你们的鼓励是我最大的动力。