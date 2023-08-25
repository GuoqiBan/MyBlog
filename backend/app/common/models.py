# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, DateTime, Float, Integer, String, Text, text
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BlogArticle(Base):
    __tablename__ = 'blog_article'

    id = Column(Integer, primary_key=True)
    article_title = Column(String(255), comment='文章标题 不能为空')
    author_id = Column(Integer, server_default=text("'1'"), comment='文章作者 不能为空')
    category_id = Column(Integer, comment='分类id 不能为空')
    article_content = Column(Text, comment='文章内容')
    article_cover = Column(String(1234), server_default=text("'	https://mrzym.gitee.io/blogimg/html/rabbit.png'"), comment='文章缩略图')
    is_top = Column(Integer, server_default=text("'2'"), comment='是否置顶 1 置顶 2 取消置顶')
    status = Column(Integer, server_default=text("'1'"), comment='文章状态  1 公开 2 私密 3 草稿箱')
    type = Column(Integer, server_default=text("'1'"), comment='文章类型 1 原创 2 转载 3 翻译')
    origin_url = Column(String(255), comment='原文链接 是转载或翻译的情况下提供')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    view_times = Column(Integer, server_default=text("'0'"), comment='文章访问次数')
    article_description = Column(String(255), comment='描述信息 不能为空')
    thumbs_up_times = Column(Integer, server_default=text("'0'"), comment='文章点赞次数')
    reading_duration = Column(Float(asdecimal=True), server_default=text("'0'"), comment='文章阅读时长')


class BlogArticleTag(Base):
    __tablename__ = 'blog_article_tag'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, comment='文章id')
    tag_id = Column(Integer, comment='标签id')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogCategory(Base):
    __tablename__ = 'blog_category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(55), unique=True, comment='分类名称 唯一')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogComment(Base):
    __tablename__ = 'blog_comment'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, comment='评论父级id')
    for_id = Column(Integer, comment='评论的对象id 比如说说id、文章id等')
    type = Column(Integer, comment='评论类型 1 文章 2 说说 3 留言 ...')
    from_id = Column(Integer, comment='评论人id')
    from_name = Column(String(255), comment='评论人昵称')
    from_avatar = Column(String(555), comment='评论人头像')
    to_id = Column(Integer, comment='被回复的人id')
    to_name = Column(String(255), comment='被回复人的昵称')
    to_avatar = Column(String(555), comment='被回复人的头像')
    content = Column(String(555), comment='评论内容')
    thumbs_up = Column(Integer, server_default=text("'0'"), comment='评论点赞数')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    ip = Column(String(255), comment='ip地址')


class BlogConfig(Base):
    __tablename__ = 'blog_config'

    id = Column(Integer, primary_key=True)
    blog_name = Column(String(55), server_default=text("'小张的博客'"), comment='博客名称')
    blog_avatar = Column(String(255), server_default=text("'https://mrzym.gitee.io/blogimg/html/rabbit.png'"), comment='博客头像')
    avatar_bg = Column(String(255), comment='博客头像背景图')
    personal_say = Column(String(255), comment='个人签名')
    blog_notice = Column(String(255), comment='博客公告')
    qq_link = Column(String(255), comment='qq链接')
    we_chat_link = Column(String(255), comment='微信链接')
    github_link = Column(String(255), comment='github链接')
    git_ee_link = Column(String(255), comment='git_ee链接')
    bilibili_link = Column(String(255), comment='bilibili链接')
    view_time = Column(BigInteger, comment='博客被访问的次数')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogHeader(Base):
    __tablename__ = 'blog_header'

    id = Column(Integer, primary_key=True)
    bg_url = Column(String(255), comment='背景图')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    route_name = Column(String(555), comment='路由名称')


class BlogLike(Base):
    __tablename__ = 'blog_like'

    id = Column(Integer, primary_key=True)
    type = Column(Integer, comment='点赞类型 1 文章 2 说说 3 留言 4 评论')
    for_id = Column(Integer, comment='点赞的id 文章id 说说id 留言id')
    user_id = Column(Integer, comment='点赞用户id')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogLink(Base):
    __tablename__ = 'blog_links'

    id = Column(Integer, primary_key=True)
    site_name = Column(String(55), comment='网站名称')
    site_desc = Column(String(255), comment='网站描述')
    site_avatar = Column(String(555), comment='网站头像')
    url = Column(String(255), comment='网站地址')
    status = Column(Integer, comment='友链状态 1 待审核 2 审核通过')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogMessage(Base):
    __tablename__ = 'blog_message'

    id = Column(Integer, primary_key=True)
    tag = Column(VARCHAR(255), comment='标签')
    message = Column(String(555), comment='留言内容')
    color = Column(String(255), server_default=text("'#676767'"), comment='字体颜色')
    font_size = Column(Integer, server_default=text("'12'"), comment='字体大小')
    bg_color = Column(String(255), comment='背景颜色')
    bg_url = Column(String(255), comment='背景图片')
    user_id = Column(Integer, comment='留言用户的id')
    like_times = Column(Integer, server_default=text("'0'"), comment='点赞次数')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    font_weight = Column(Integer, server_default=text("'500'"), comment='字体宽度')
    nick_name = Column(String(255), comment='游客用户的昵称')


class BlogNotify(Base):
    __tablename__ = 'blog_notify'

    id = Column(Integer, primary_key=True)
    message = Column(String(555), comment='通知内容')
    user_id = Column(Integer, comment='通知给谁')
    type = Column(Integer, comment='通知类型 1 文章 2 说说 3 留言 4 友链')
    to_id = Column(Integer, comment='说说或者是文章的id 用于跳转')
    isView = Column(Integer, server_default=text("'1'"), comment='是否被查看 1 没有 2 已经查看')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogPhoto(Base):
    __tablename__ = 'blog_photo'

    id = Column(Integer, primary_key=True)
    album_id = Column(Integer, comment='相册 id 属于哪个相册')
    url = Column(String(555), comment='图片地址')
    status = Column(Integer, server_default=text("'1'"), comment='状态 1 正常 2 回收站')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogPhotoAlbum(Base):
    __tablename__ = 'blog_photo_album'

    id = Column(Integer, primary_key=True)
    album_name = Column(String(26), comment='相册名称')
    description = Column(String(55), comment='相册描述信息')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    album_cover = Column(String(555), comment='相册封面')


class BlogRecommend(Base):
    __tablename__ = 'blog_recommend'

    id = Column(Integer, primary_key=True)
    title = Column(String(55), comment='推荐网站标题')
    link = Column(String(255), comment='网站地址')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogTag(Base):
    __tablename__ = 'blog_tag'

    id = Column(Integer, primary_key=True)
    tag_name = Column(String(55), unique=True, comment='标签名称 唯一')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogTalk(Base):
    __tablename__ = 'blog_talk'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, comment='发布说说的用户id')
    content = Column(String(255), comment='说说内容')
    status = Column(Integer, server_default=text("'1'"), comment='说说状态 1 公开 2 私密 3 回收站')
    is_top = Column(Integer, server_default=text("'2'"), comment='是否置顶 1 置顶 2 不置顶')
    like_times = Column(Integer, server_default=text("'0'"), comment='点赞次数')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogTalkPhoto(Base):
    __tablename__ = 'blog_talk_photo'

    id = Column(Integer, primary_key=True)
    talk_id = Column(Integer, comment='说说的id')
    url = Column(String(255), comment='图片地址')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)


class BlogUser(Base):
    __tablename__ = 'blog_user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, comment='账号，唯一')
    password = Column(CHAR(64), nullable=False, comment='密码')
    role = Column(Integer, nullable=False, server_default=text("'2'"), comment='用户角色 1 管理员 2 普通用户')
    nick_name = Column(String(255), server_default=text("''"), comment='用户昵称')
    avatar = Column(String(255), server_default=text("''"), comment='用户头像')
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    qq = Column(String(255), server_default=text("''"), comment='用户QQ 用于联系')
    ip = Column(String(255), server_default=text("''"), comment='ip属地')
