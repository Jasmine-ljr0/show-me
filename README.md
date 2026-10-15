# 丁凯悦 · 个人作品集网站

基于 React 18 + Vite 5 构建的简约风个人简历 / 作品集单页网站。

## 本地预览

```bash
npm install
npm run dev      # 开发预览 http://localhost:5173
npm run build    # 生产构建，产物在 dist/
```

## 部署到 GitHub Pages（推荐：自动构建）

本仓库已配置 GitHub Actions（`.github/workflows/deploy.yml`），推送即自动构建并发布，**无需手动上传 dist**。

1. 在 GitHub 新建一个仓库（公开），把本项目源码推送到 `main` 分支（注意：`.gitignore` 已忽略 `node_modules` 和 `dist`）。
2. 仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
3. 推送代码后，Actions 会自动运行；完成后在 `https://<用户名>.github.io/<仓库名>/` 访问。

> 已通过 `vite.config.js` 的 `base: './'` 设为相对路径，因此在 GitHub 子路径下资源不会 404。

## 备选方案：直接上传构建产物（不依赖 Actions）

若不想用自动构建，可把本地 `npm run build` 生成的 `dist/` 文件夹**全部内容**上传到仓库根目录，然后：

- Settings → Pages → Source 选 **Deploy from a branch**，分支选 `main`、目录选 **/ (root)**；
- 注意此时需让 dist 被提交：临时把 `.gitignore` 里的 `dist` 那行删掉，或 `git add -f dist`。

之后访问 `https://<用户名>.github.io/<仓库名>/` 即可。

## 目录说明

```
personal-site/
├── index.html              # 入口 HTML（含字体非阻塞、首屏预加载）
├── vite.config.js          # 已设 base: './'，适配 GitHub 子路径
├── public/                 # 静态资源（图片等，构建时原样拷贝到根）
│   ├── work/               # 精选项目相册图片
│   ├── about-photo.webp    # 证件照
│   ├── about-frame.png     # 相框
│   ├── hero-bg.webp        # 首屏背景
│   ├── portrait-stroke.webp# 人物抠图
├── src/
│   ├── data.js             # 全站文字 / 数据内容（在这里改文案）
│   ├── index.css           # 全站样式
│   ├── components/         # 各板块组件
│   └── lib/renderHl.jsx    # 重点标记解析
├── .github/workflows/      # GitHub Pages 自动部署工作流
└── dist/                   # 构建产物（部署用）
```
