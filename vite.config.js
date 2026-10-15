import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  // 相对 base：构建产物使用相对路径，确保部署到 GitHub Pages 子路径（用户名.github.io/仓库名/）时资源不会 404
  base: './',
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
  },
})
